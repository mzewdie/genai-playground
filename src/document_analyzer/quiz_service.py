from .action_service import ActionService
from src.common.document.analysis_document import AnalysisDocument
from pathlib import Path
class QuizService(ActionService):


    prompt_template_path = Path("src/common/prompts/quiz_prompt.md")
    #prompt_template_path = Path("src/common/prompts/test_prompt_ollama.md")


