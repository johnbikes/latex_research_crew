from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class LatexSplitterToolInput(BaseModel):
    # tex_output: str = Field(..., description="LaTeX output containing document tex")
    # bib_output: str = Field(..., description="LaTeX output containing bib entries")
    tex_context: str = Field(..., description="LaTeX output containing document tex")
    bib_context: str = Field(..., description="LaTeX output containing bib entries")

class LatexSplitterTool(BaseTool):
    name: str = "LaTeX splitter"
    description: str = (
        "Splits the LaTeX output into tex and bib files."
    )
    args_schema: Type[BaseModel] = LatexSplitterToolInput

    # def _run(self, tex_output: str, bib_output: str) -> str:
    def _run(self, tex_context: str, bib_context: str) -> str:

        with open("report_new.tex", "w") as f:
            # f.write(tex_output)
            f.write(tex_context)
            # TODO: may need to do the actual line splitting
            # f.writelines(["This is the second line.\n", "This is the third line.\n"])

        with open("report_new.bib", "w") as f:
            # f.write(bib_output)
            f.write(bib_context)

        return "tool success"
