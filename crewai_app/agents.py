from crewai import Agent
from .llm import llm
from .tools import search_web_tool

guide_expert= Agent( 
    role="City Local Guide Expert",
    goal="Provides information on things to do in the city based on the user's interests in english language.",
    backstory="""A local expert with a passion for sharing the best experiences and hidden gems of their city.""",
    tools=[search_web_tool],
    verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
    )

location_expert = Agent(
    role="Travel Trip Expert",
    goal="Gather helpful information about to the city and city during travel plan in english language",
    backstory="""A seasoned traveler who has explored various destinations and knows the ins and outs of travel logistics.""",
    tools=[search_web_tool],
    verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
    )

planner_expert = Agent(
    role="Travel Planning Expert",
    goal="Compiles all gathered information to provide a comprehensive travel plan in english language.",
    backstory="""
    You are a professional guide with a passion for travel.
    An organizational wizard who can turn a list of possibilities into a seamless itinerary You are an expert travel planner.
    """,
    tools=[search_web_tool],
    verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
    )
