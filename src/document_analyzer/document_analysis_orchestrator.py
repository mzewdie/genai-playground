import logging

from src.common.document.analysis_document import AnalysisDocument
from src.common.llm.llm_factory import LLMFactory
from src.document_analyzer.action import Action


logger = logging.getLogger(__name__)

llm_debug_logger = logging.getLogger("llm_debug")


class DocumentAnalysisOrchestrator:
    
    def __init__(self,
        llm_service,
        summary_service,
        quiz_service = None,
        flashcard_service = None,
        translation_service = None,
        metadata_service = None):
        self.llm_service=llm_service
        self.summary_service = summary_service
        self.quiz_service = quiz_service
        self.flashcard_service = flashcard_service
        self.translation_service = translation_service
        self.metadata_service = metadata_service
        
    def execute(self,
                document: AnalysisDocument,
                action: Action):
        
        match action:
            case Action.SUMMARY:
                if self.summary_service is None:
                    raise ValueError("SummaryService is not configured.")
                return self.__summarize(document=document)
                
          
            case _:
                raise ValueError(
                    f"Unsupported action: {action}")
                
                
    def __summarize(self,document: AnalysisDocument) -> str:
        prompt=self.summary_service.generate_prompt(document=document)
        
        logger.info(f"Prompt is: {prompt}")
        
        llm_debug_logger.info(f"Document length: {len(document.content)}")
        llm_debug_logger.debug(f"Prompt:\n{document.content[:500]}")
        response: str = self.llm_service.invoke(prompt)
        return response

    