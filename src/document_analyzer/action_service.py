from pathlib import Path

from src.common.document.analysis_document import AnalysisDocument



class ActionService:

    prompt_template_path = None

    def generate_prompt(self,  document: AnalysisDocument):

        prompt_template = self.prompt_template_path.read_text(encoding="utf-8")

        prompt = prompt_template.replace(
            "{{document}}",
            document.content,)

        if "{{document}}" in prompt:
            raise ValueError("Document placeholder was not replaced.")

        if not document.content.strip():
            raise ValueError("Document content is empty.")

        return prompt