from crewai import Task

def location_task(agent, from_city, destination_city, date_from, date_to):
    return Task(
        description=f"""
        In French: This task involves a comprehensive data collection process to provide the traveler with essential information about their destination...
        Traveling from: {from_city}
        Destination city: {destination_city}
        Arrival Date: {date_from}
        Departure Date: {date_to}
        Follow this rule: If {destination_city} is in a French country, respond in FRENCH.
        """,
        expected_output=f"""
        If {destination_city} is in a French country, respond in FRENCH.
        In markdown format: A detailed markdown report that includes a curated list of recommended places to stay, a breakdown of daily living expenses, and practical travel tips.
        """,
        agent=agent,
        output_file='city_report.md',
    )

def guide_task(agent, destination_city, interests, date_from, date_to):
    return Task(
        description=f"""
        Tailored to the traveler's personal {interests}, this task focuses on creating an engaging and informative guide to the city's attractions...
        Destination city: {destination_city}
        Interests: {interests}
        Arrival Date: {date_from}
        Departure Date: {date_to}
        Follow this rule: If {destination_city} is in a French country, respond in FRENCH.
        """,
        expected_output=f"""
        An interactive markdown report with a personalized itinerary of activities and attractions.
        """,
        agent=agent,
        output_file='guide_report.md',
    )

def planner_task(context, agent, destination_city, interests, date_from, date_to):
    return Task(
        description=f"""
        This task synthesizes all collected information into a detailed introduction to the city and a practical travel plan...
        Destination city: {destination_city}
        Interests: {interests}
        Arrival Date: {date_from}
        Departure Date: {date_to}
        Follow this rule: If {destination_city} is in a French country, respond in FRENCH.
        """,
        expected_output="""
        A rich markdown document with emojis, a city introduction, daily plan, and highlights.
        """,
        context=context,
        agent=agent,
        output_file='travel_plan.md',
    )
