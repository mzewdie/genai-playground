import streamlit as st

from src.document_analyzer.summary_service import SummaryService
from src.common.llm.llm_factory import LLMFactory
from src.common.llm.llm_service import LLMService
from src.common.llm.llm_configuration import LLMConfiguration
from src.document_analyzer.document_analysis_orchestrator import DocumentAnalysisOrchestrator
from src.document_analyzer.action import Action

st.title("Summary Page")

if "selected_document" in st.session_state:
    st.write(f"Selected Document: {st.session_state['selected_document']}")
else:
    st.error("You must first load the document from the Sidebar Load Document")
    st.stop()

if "selected_llm_provider" in st.session_state:
    st.write(f"LLM: {st.session_state['selected_llm_provider']}")
if "selected_llm_model" in st.session_state:
    st.write(f"Model: {st.session_state['selected_llm_model']}")


summary_button = st.button("Summarize Document")
#already_clicked = st.session_state.get("summary_key", False)
llm_configuration=LLMConfiguration(st.session_state["selected_llm_provider"],st.session_state["selected_llm_model"])

if summary_button:
    #summary_button = st.button("Summarize Document", key="summary_key", disabled=already_clicked)
    with st.spinner("Summarizing the document ..."):
        analysis_document=st.session_state["created_analysis_document"]
        summary_service=SummaryService()
        llm_service:LLMService=LLMFactory.create(llm_configuration)
        document_analysis_orchestrator=DocumentAnalysisOrchestrator(llm_service=llm_service,
                                                                    summary_service=summary_service,
                                                                    quiz_service=None)
        response=document_analysis_orchestrator.execute(document=analysis_document,action=Action.SUMMARY)
        if response:
            with st.expander("Summary"):
                st.markdown(response)


