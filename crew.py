from crewai import Crew

from agents import build_agents
from tasks import create_tasks


def run_crew(job_description: str, resume_text: str, api_key: str) -> dict:
    agents = build_agents(api_key)
    tasks = create_tasks(agents, job_description, resume_text)

    crew = Crew(agents=list(agents.values()), tasks=tasks, verbose=False)
    crew.kickoff()

    return {
        "jd_analysis": str(tasks[0].output),
        "resume_match": str(tasks[1].output),
        "cover_letter": str(tasks[2].output),
        "interview_prep": str(tasks[3].output),
    }
