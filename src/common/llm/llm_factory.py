from .gemini_llm_service import GeminiLLMService
from .ollama_llm_service import OllamaLLMService



class LLMFactory:
    
    @staticmethod
    def create(configuration):
        
        match configuration.provider:
            
            case "Gemini":
                return GeminiLLMService(model=configuration.model)
            
            case "Ollama":
                return OllamaLLMService(model=configuration.model)
            
            case _:
                raise ValueError(f"Unsupporetd provider: {configuration.provider}")