import streamlit as st
import tempfile
import logging

from src.common.config.configuration import Configuration
from src.common.llm.llm_configuration import LLMConfiguration
from src.common.document.pdf_loader import PDFLoader
from src.common.document.analysis_document import AnalysisDocument
from src.common.utils.logging_config import  configure_logging
from pathlib import  Path


configure_logging()
logger = logging.getLogger(__name__)

# print(logger.handlers)
# print(logger.level)
#
# logger.debug("DEBUG TEST")
# logger.info("INFO TEST")
# logger.warning("WARNING TEST")


with st.popover("About"):
    st.write("Designed and implemented by: Mulugeta Zewdie")
    st.write("Application version: 2.0")


uploaded_file=st.file_uploader("Upload PDF","pdf")



col1, col2 = st.columns(2)

configuration = Configuration.load()
with col1:
    selected_provider = st.selectbox("Provider",configuration.get_providers())
    st.session_state["selected_llm_provider"]=selected_provider

with col2:
    selected_model = st.selectbox("Model",configuration.get_models(selected_provider))
    st.session_state["selected_llm_model"]= selected_model




llm_configuration=LLMConfiguration(selected_provider,selected_model)
if st.button("Load Document"):
    if not uploaded_file:
        st.error("Please upload the document to be processed!")
    else:
        #pdf_bytes = uploaded_file.getvalue()
        st.session_state["uploaded_file"] = uploaded_file
        pdf_bytes = uploaded_file.getvalue()
        st.session_state["pdf_bytes"] = pdf_bytes

        with tempfile.NamedTemporaryFile(delete=False,
                                     suffix=".pdf"
                                     ) as tmp_file:
            #tmp_file.write(uploaded_file.getvalue())
            tmp_file.write(pdf_bytes)
            tmp_file.flush()
            pdf_path=tmp_file.name
            #print("Checking file size")
            #print(Path(pdf_path).stat().st_size)
            with st.spinner("Loading the document ..."):

                pdfloader=PDFLoader()
                analysis_document:AnalysisDocument=pdfloader.load(pdffile=pdf_path)
                st.success("Document loaded successfully. You can select an Action from the sidebar")
                st.session_state["created_analysis_document"]=analysis_document
                st.session_state["selected_document"]=st.session_state["uploaded_file"].name
                #st.session_state["selected_llm_provider"]=selected_provider
                #st.session_state["selected_llm_model"]= selected_model

