import streamlit as st

from crew import run_crew

st.set_page_config(
    page_title="AI Job Application Agent",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 AI Job Application Agent")
st.markdown(
    "*Powered by CrewAI + Google Gemini — paste a JD and your resume, "
    "get JD analysis, match score, cover letter, and interview prep.*"
)
st.divider()

with st.sidebar:
    st.header("🔑 API Key")
    api_key = st.text_input(
        "Google Gemini API Key",
        type="password",
        placeholder="AIza...",
        help="Get a free key at https://aistudio.google.com/apikey",
    )
    st.caption("Your key is used only for this session and never stored.")
    st.divider()
    st.markdown("### How it works")
    st.markdown(
        "1. Paste the job description\n"
        "2. Paste your resume\n"
        "3. Click **Analyze**\n"
        "4. Four AI agents collaborate to help you apply"
    )

col1, col2 = st.columns(2)
with col1:
    job_description = st.text_area(
        "📋 Job Description",
        height=320,
        placeholder="Paste the full job description here...",
    )
with col2:
    resume_text = st.text_area(
        "📄 Your Resume",
        height=320,
        placeholder="Paste your resume text here...",
    )

run_button = st.button("🚀 Analyze & Generate", use_container_width=True, type="primary")

if run_button:
    if not api_key:
        st.error("⚠️ Please enter your Gemini API key in the sidebar.")
    elif not job_description.strip() or not resume_text.strip():
        st.warning("⚠️ Please paste both the job description and your resume.")
    else:
        with st.spinner("🤖 Four agents are collaborating... this takes 30–60 seconds"):
            try:
                results = run_crew(job_description, resume_text, api_key)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
                st.stop()

        st.success("✅ Analysis complete!")
        st.divider()

        tab1, tab2, tab3, tab4 = st.tabs(
            ["📊 JD Analysis", "🎯 Resume Match", "✉️ Cover Letter", "🎤 Interview Prep"]
        )

        with tab1:
            st.markdown("### Job Description Analysis")
            st.markdown(results["jd_analysis"])

        with tab2:
            st.markdown("### Resume Match Score & Gap Analysis")
            st.markdown(results["resume_match"])

        with tab3:
            st.markdown("### Personalized Cover Letter")
            st.markdown(results["cover_letter"])
            st.download_button(
                "⬇️ Download as .txt",
                results["cover_letter"],
                file_name="cover_letter.txt",
                use_container_width=True,
            )

        with tab4:
            st.markdown("### Likely Interview Questions & Answer Tips")
            st.markdown(results["interview_prep"])
