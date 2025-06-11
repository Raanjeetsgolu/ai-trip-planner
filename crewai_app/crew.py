from crewai import Crew, Process
from .agents import guide_expert, location_expert, planner_expert
from .tasks import location_task, guide_task, planner_task

def build_crew(from_city, destination_city, interests, date_from, date_to):
    loc_task = location_task(location_expert, from_city, destination_city, date_from, date_to)
    gui_task = guide_task(guide_expert, destination_city, interests, date_from, date_to)
    plan_task = planner_task([loc_task, gui_task], planner_expert, destination_city, interests, date_from, date_to)
    return Crew(
        agents=[location_expert, guide_expert, planner_expert],
        tasks=[loc_task, gui_task, plan_task],
        process=Process.sequential,
        verbose=True
    )
