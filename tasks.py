from crewai import Task

def create_tasks(agents, job_description, resume_text):

    analyze_jd = Task(
        description=f"""Analyze this job description and extract:
        1. Must-have technical skills
        2. Nice-to-have skills  
        3. Experience level required
        4. Key responsibilities
        
        Job Description: {job_description}""",
        agent=agents['job_analyst'],
        expected_output="Structured analysis of job requirements"
    )

    match_resume = Task(
        description=f"""Compare the resume against the analyzed job requirements.
        Provide:
        1. Match score (0-100)
        2. Strong matches (skills candidate has)
        3. Gaps (skills candidate is missing)
        4. Recommendations to improve application
        
        Resume: {resume_text}""",
        agent=agents['resume_matcher'],
        expected_output="Match score with detailed gap analysis",
        context=[analyze_jd]
    )

    write_cover_letter = Task(
        description="""Write a professional, personalized cover letter 
        based on the job analysis and resume match. 
        Highlight strongest matches. Address gaps positively.""",
        agent=agents['cover_letter_writer'],
        expected_output="Complete cover letter ready to send",
        context=[analyze_jd, match_resume]
    )

    prep_interview = Task(
        description="""Generate top 10 likely interview questions for this role.
        Mix of technical, behavioral, and role-specific questions.
        Include brief tips on how to answer each.""",
        agent=agents['interview_coach'],
        expected_output="10 interview questions with answering tips",
        context=[analyze_jd, match_resume]
    )

    return [analyze_jd, match_resume, write_cover_letter, prep_interview]