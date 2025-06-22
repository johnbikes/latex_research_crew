from typing import List

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

from .tools.latex_splitter_tool import LatexSplitterTool

latex_splitter_tool = LatexSplitterTool()

@CrewBase
class ResearchTeam():
    """ResearchTeam crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'], # type: ignore[index]
            # tools=[latex_splitter_tool],
            verbose=True,
        )
    
    @agent
    def latex_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['latex_expert'], # type: ignore[index]
            tools=[latex_splitter_tool],
            verbose=True,
        )

    # @agent
    # def latex_verifier(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['latex_verifier'],
    #         verbose=True,
    #         allow_code_execution=True,
    #         code_execution_mode="safe",  # Uses Docker for safety
    #         max_execution_time=60, 
    #         max_retry_limit=3
    #     )
    # # TODO: reference a Dockerfile based on an image that supports pdflatex and bibtex - pandoc/latex should work

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'], # type: ignore[index]
            # output_file='report.txt',
        )
    
    @task
    def splitter_task(self) -> Task:
        return Task(
            config=self.tasks_config['splitter_task'], # type: ignore[index]
            output_file='result.txt'
        )
    
    # @task
    # def reporting_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['verifier_task'], # type: ignore[index]
    #         output_file='can_compile.txt'
    #     )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
