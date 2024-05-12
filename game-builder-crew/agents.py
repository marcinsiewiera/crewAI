from textwrap import dedent
from crewai import Agent
from groq import Groq
from langchain_groq import ChatGroq
import os

os.environ["GROQ_API_KEY"] = "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"
llm = ChatGroq(temperature=0, model_name="llama3-70b-8192")

class GameAgents():
	def senior_engineer_agent(self):
		return Agent(
			role='Senior Software Engineer',
			goal='Create software as needed',
			backstory=dedent("""\
				You are a Senior Software Engineer at a leading tech think tank.
				Your expertise in programming in python. and do your best to
				produce perfect code"""),
			allow_delegation=False,
			verbose=True,
			llm=llm,
			max_rpm=30,
			max_tpm=1000
		)

	def qa_engineer_agent(self):
		return Agent(
			role='Software Quality Control Engineer',
  		goal='create prefect code, by analizing the code that is given for errors',
  		backstory=dedent("""\
				You are a software engineer that specializes in checking code
  			for errors. You have an eye for detail and a knack for finding
				hidden bugs.
  			You check for missing imports, variable declarations, mismatched
				brackets and syntax errors.
  			You also check for security vulnerabilities, and logic errors"""),
			allow_delegation=False,
			verbose=True,
			llm=llm,
			max_rpm=30,
			max_tpm=1000
		)

	def chief_qa_engineer_agent(self):
		return Agent(
			role='Chief Software Quality Control Engineer',
  		goal='Ensure that the code does the job that it is supposed to do',
  		backstory=dedent("""\
				You feel that programmers always do only half the job, so you are
				super dedicate to make high quality code."""),
			allow_delegation=True,
			verbose=True,
			llm=llm,
			max_rpm=30,
			max_tpm=1000
		)
