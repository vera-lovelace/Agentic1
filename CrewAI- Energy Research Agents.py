import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI

# Set API keys
openai_api_key="your api key"
os.environ["OPENAI_API_KEY"] = openai.api_key
os.environ["SERPER_API_KEY"] = "Your Key"
search_tool = SerperDevTool()

# Initialize the LLM
llm=ChatOpenAI(
    model="gpt-4-turbo",
    temperature=0.7
)

# Creating a senior researcher agent with memory and verbose mode
researcher = Agent(
    role='Senior Researcher',
    goal='Uncover groundbreaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
    "Driven by curiosity, you're at the forefront of"
    "innovation, eager to explore and share knowledge that could change"
    "the world."
    ),
    tools=[search_tool],
    allow_delegation=False,
    llm=llm
)

# Creating a summarizer agent with memory and verbose mode
summarizer=Agent(
    role='content summarizer',
    goal='Create concise and informative summaries of reserch findings',
    verbose=True,
    memory=True,
    backstory=("You are a skilled writer who can distill complex information into clear, concise and engaging summaries."
    "You excel at indentifying key points and presenting them in a logica and accessible manner."),
    tools=[search_tool],
    allow_delegation=False,
    llm=llm
)

# Creating tasks for each agent

research_task=Task()

summary_task=Task()


# Creating the crew
energy_research_crew=Crew(
    agents=[researcher,summarizer],
    tasks=[research_task,summary_task]
    verbose=True   #more detailed logs
)


#Run the crew
result=energy_research_crew.kickoff()

print("FINAL RESULT ")
print(result)