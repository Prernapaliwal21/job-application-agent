from crewai import Agent, LLM


def build_agents(api_key: str):
    llm = LLM(
        model="gemini/gemini-2.5-flash-lite",
        api_key=api_key,
        temperature=0.3,
    )

    job_analyst = Agent(
        role="Job Description Analyst",
        goal="Extract key requirements, skills, and expectations from job descriptions",
        backstory="Expert HR analyst with 10 years reading JDs across tech companies",
        llm=llm,
        verbose=False,
    )

    resume_matcher = Agent(
        role="Resume Match Specialist",
        goal="Compare resume against job requirements and produce a match score with gaps",
        backstory="Experienced technical recruiter who evaluates developer profiles daily",
        llm=llm,
        verbose=False,
    )

    cover_letter_writer = Agent(
        role="Cover Letter Writer",
        goal="Write compelling, personalized cover letters that highlight relevant experience",
        backstory="Professional career coach who has helped 500+ developers land jobs",
        llm=llm,
        verbose=False,
    )

    interview_coach = Agent(
        role="Interview Preparation Coach",
        goal="Generate likely interview questions based on the job description and candidate profile",
        backstory="Senior engineering manager who has conducted 200+ technical interviews",
        llm=llm,
        verbose=False,
    )

    return {
        "job_analyst": job_analyst,
        "resume_matcher": resume_matcher,
        "cover_letter_writer": cover_letter_writer,
        "interview_coach": interview_coach,
    }
