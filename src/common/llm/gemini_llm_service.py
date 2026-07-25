from src.common.llm.llm_service import LLMService
import os
import logging
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


 # Load environment variables from .env
load_dotenv()

# Read the API key
api_key = os.getenv("GEMINI_API_KEY")

llm_debug_logger = logging.getLogger("llm_debug")



class GeminiLLMService(LLMService):
    
    def __init__(self, model):
        self.model=model
        self.llm=ChatGoogleGenerativeAI(model=model,google_api_key=api_key)
        
    def invoke(self, prompt) -> str:
        llm_debug_logger.debug(f"Gemini is summarizing the document with model: {self.model}")
        return self.llm.invoke(prompt).content