import logging
import tempfile

import streamlit as st
import json

from src.common.config.configuration import Configuration
from src.common.document.analysis_document import AnalysisDocument
from src.common.document.pdf_loader import PDFLoader
from src.common.llm.llm_configuration import LLMConfiguration
from src.common.llm.llm_factory import LLMFactory
from src.common.llm.llm_service import LLMService
from src.common.utils.logging_config import configure_logging
from src.document_analyzer.action import Action
from src.document_analyzer.document_analysis_orchestrator import DocumentAnalysisOrchestrator
from src.document_analyzer.summary_service import SummaryService
from src.document_analyzer.quiz_service import  QuizService

configure_logging()
logger = logging.getLogger(__name__)

def get_analysis_document(pdfpath) -> AnalysisDocument:
    logger.debug(f"PDF loader called with path {pdfpath}")
    pdfloader=PDFLoader()
    analysis_document:AnalysisDocument=pdfloader.load(pdffile=pdf_path)
    return analysis_document


st.title("AI Document Analyzer")

#with st.popover("⚙️ Settings"):
with st.popover("About"):
     st.write("Designed and implemented by: Mulugeta Zewdie")
     st.write("Application version: 1.0")
  

uploaded_file=st.file_uploader("Upload PDF",
                 "pdf")

col1, col2 = st.columns(2)

configuration = Configuration.load()
with col1:
    selected_provider = st.selectbox("Provider",configuration.get_providers(),)
    summary_button = st.button("Generate Summary")
with col2:
     selected_model = st.selectbox("Model",configuration.get_models(selected_provider),)
     quiz_button = st.button("Generate Quiz")
                                     
                              
     
llm_configuration=LLMConfiguration(selected_provider,selected_model)          
    
            
    
selected_action = st.selectbox(
    "Action",
    [
        "Summarize",
        "Quiz",
        "Flashcards",
        "Translation",
    ]
)

#summary_button = st.button("Generate Summary")


#data = ConfigurationLoader.load_config2()
#logger.info(f"Yamlentries read: {data}")

if summary_button or quiz_button:
    if not uploaded_file:
        st.error("Please upload the document first!")
    else:
        with tempfile.NamedTemporaryFile(delete=False,
                                         suffix=".pdf"
                                        ) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            pdf_path=tmp_file.name
            if summary_button:
                with st.spinner("Summarizing the document ..."):
                    analysis_document=get_analysis_document(pdf_path)
                    summary_service=SummaryService()
                    llm_service:LLMService=LLMFactory.create(llm_configuration)
                    document_analysis_orchestrator=DocumentAnalysisOrchestrator(llm_service=llm_service,
                                                                                summary_service=summary_service,
                                                                                quiz_service=None)
                    response=document_analysis_orchestrator.execute(document=analysis_document,action=Action.SUMMARY)
                    if response:
                        with st.expander("Summary"):
                            st.markdown(response)

            elif quiz_button:
                with st.spinner("Creating quiz ..."):
                    analysis_document=get_analysis_document(pdf_path)
                    quiz_service=QuizService()
                    llm_service:LLMService=LLMFactory.create(llm_configuration)
                    document_analysis_orchestrator=DocumentAnalysisOrchestrator(llm_service=llm_service,
                                                                                summary_service=None,
                                                                                quiz_service=quiz_service)
                    response=document_analysis_orchestrator.execute(document=analysis_document,action=Action.QUIZ)
                    logger.info(f"type of response: {type(response)}")
                    if response:
                        with st.expander("Summary"):
                            st.markdown(response)
                            #st.markdown(json.load(response))






            
if uploaded_file and summary_button:
    st.download_button(
        label="Download Summary",
        data=response,
        file_name=f"{uploaded_file.name}_summary_model_{selected_model}.md",
        mime="text/markdown",)
    


st.markdown("---")
st.caption(
    "Disclaimer: The generated summary is AI-produced and should be "
    "reviewed before use in legal, financial, medical, or other "
    "high-stakes contexts."
)