from pathlib import Path
from src.document_analyzer.action_service import ActionService

class SummaryService(ActionService):


    prompt_template_path = Path(
        "src/common/prompts/summary_prompt.md"
    )


