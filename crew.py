import google.generativeai as genai

def run_crew(job_description: str, resume_text: str, api_key: str) -> dict:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")

    # Agent 1 — JD Analyst
    jd_prompt = f"""You are an expert HR analyst with 10 years experience.
Analyze this job description and extract:
1. Must-have technical skills
2. Nice-to-have skills
3. Experience level required
4. Key responsibilities
5. Red flags or concerns

Job Description:
{job_description}"""

    jd_result = model.generate_content(jd_prompt).text

    # Agent 2 — Resume Matcher
    match_prompt = f"""You are an experienced technical recruiter.
Compare this resume against the job analysis below.
Provide:
1. Match Score (0-100)
2. Strong matches (skills candidate clearly has)
3. Skill gaps (skills missing or unclear)
4. Top 3 recommendations to strengthen the application

Job Analysis:
{jd_result}

Resume:
{resume_text}"""

    match_result = model.generate_content(match_prompt).text

    # Agent 3 — Cover Letter Writer
    cover_prompt = f"""You are a professional career coach who has helped 500+ developers land jobs.
Write a compelling, personalized cover letter based on the analysis below.
- Highlight strongest matches
- Address gaps positively
- Keep it under 300 words
- Professional but warm tone

Job Analysis: {jd_result}
Match Analysis: {match_result}
Resume: {resume_text}"""

    cover_result = model.generate_content(cover_prompt).text

    # Agent 4 — Interview Coach
    interview_prompt = f"""You are a senior engineering manager who has conducted 200+ technical interviews.
Based on the job description and candidate profile, generate:
- Top 10 likely interview questions (mix of technical, behavioral, situational)
- For each question, provide a 2-line tip on how to answer it well

Job Analysis: {jd_result}
Candidate Resume: {resume_text}"""

    interview_result = model.generate_content(interview_prompt).text

    return {
        "jd_analysis": jd_result,
        "resume_match": match_result,
        "cover_letter": cover_result,
        "interview_prep": interview_result,
    }
