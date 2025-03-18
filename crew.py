from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from dotenv import load_dotenv

load_dotenv()


@CrewBase
class newtesting():
	"""newtesting crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			tools=[SerperDevTool()],
			verbose=True
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			tools=[ScrapeWebsiteTool()],
			verbose=True
		)
	@agent
	def file_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['file_writer'],
			verbose=True
		)

	@task
	def researcher_task(self) -> Task:
		return Task(
			config=self.tasks_config['researcher_task'],
			tools=[SerperDevTool()],
			verbose=True
		)

	@task
	def reporting_analyst_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_analyst_task'],
			tools=[ScrapeWebsiteTool()],
			verbose=True
		)
	@task
	def file_writer_task(self) -> Task:
		return Task(
			config=self.tasks_config['file_writer_task'],
			output_file='output.md',
			expected_output='Expected output description here',
			verbose=True
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the newtesting crew"""
	

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True
			
		)
