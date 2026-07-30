from src.common.llm.llm_service import LLMService
from ollama import chat
from ollama import ChatResponse

import logging


logger = logging.getLogger(__name__)
llm_debug_logger = logging.getLogger("llm_debug")

class OllamaLLMService(LLMService):
    
    def __init__(self,model):
        self.model=model
        
    def invoke(self, prompt):
        #return super().invoke(prompt)
        #return self.llm.invoke(prompt).content
        logger.info(f"Ollama is processing the document with model: {self.model}")
        llm_debug_logger.debug(f"Ollama is processing the document with model: {self.model}")
        response: ChatResponse = chat(model=self.model, messages=[
            {
                'role': 'user',
                'content': prompt,
            },
        ])
        return response.message.content