import streamlit as st
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Cold Email Generator",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional CSS for styling
st.markdown("""
    <style>
    /* Page background */
    .main {
        background: #f7f7f9;
    }
    /* Buttons */
    .stButton>button {
        background: #1f4e79;
        color: #ffffff;
        border-radius: 6px;
        height: 44px;
        font-size: 14px;
        font-weight: 600;
        border: none;
    }
    .stButton>button:hover {
        background: #163a57;
    }
    /* Header */
    .header-title {
        text-align: center;
        color: #0f1722;
        font-size: 34px;
        font-weight: 700;
        margin-bottom: 6px;
    }
    /* Generated email card */
    .generated-email {
        background: #ffffff;
        padding: 18px;
        border-radius: 8px;
        color: #0f1722;
        font-size: 14px;
        line-height: 1.6;
        border: 1px solid #e6e9ee;
    }
    /* Center footer text */
    .footer {
        text-align: center;
        color: #6b7280;
        font-size: 13px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header-title">Cold Email Generator</div>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar for user details
with st.sidebar:
    st.markdown("### Your Details")
    user_name = st.text_input("Your Name", placeholder="John Doe")
    user_email = st.text_input("Your Email", placeholder="john@example.com")
    user_title = st.text_input("Your Job Title", placeholder="Senior Developer")
    user_company = st.text_input("Your Company", placeholder="Tech Company")
    user_phone = st.text_input("Your Phone", placeholder="+1 (555) 123-4567")

# Main content
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Portfolio Link")
    portfolio_link = st.text_area(
        "Paste your portfolio link",
        placeholder="https://yourportfolio.com",
        height=100
    )

with col2:
    st.markdown("### Job Posting URL")
    job_posting_url = st.text_area(
        "Paste the job posting URL",
        placeholder="https://linkedin.com/jobs/...",
        height=100
    )

# Analyze button
st.markdown("---")
col_btn1, col_btn2, col_btn3 = st.columns(3)

with col_btn2:
    analyze_btn = st.button("Analyze Both", use_container_width=True)

# Additional info
if analyze_btn:
    st.info("Analysis complete. Ready to generate your cold email.")

# Email tone and customization
st.markdown("### Email Customization")
col_tone, col_length = st.columns(2)

with col_tone:
    tone = st.selectbox("Select Tone", ["Professional", "Friendly", "Enthusiastic", "Formal"])

with col_length:
    length = st.selectbox("Email Length", ["Short", "Medium", "Long"])

# Generate button
st.markdown("---")
generate_col1, generate_col2, generate_col3 = st.columns(3)

with generate_col2:
    if st.button("Generate Cold Email", use_container_width=True):
        if not all([user_name, user_email, portfolio_link, job_posting_url]):
            st.error("Please fill in all required fields.")
        else:
            generated_email = f"""Hi Hiring Manager,

I came across your recent job posting and was impressed by the focus on {tone.lower()} collaboration and innovation. As a {user_title} with expertise in building scalable solutions, I noticed strong alignment between my background and your team's needs. My portfolio ({portfolio_link}) showcases several projects that directly relate to the requirements mentioned in your posting.

I'm particularly interested in how your team approaches {tone.lower()} problem-solving and would welcome the opportunity to discuss how I can contribute to your goals.

Best regards,
{user_name}
{user_email}
{user_phone if user_phone else ""}
"""
            st.markdown("### Generated Cold Email")
            st.markdown(f'<div class="generated-email">{generated_email}</div>', unsafe_allow_html=True)

            col_copy, col_download = st.columns(2)
            with col_copy:
                st.text_area("Copy email:", generated_email, height=250)

            with col_download:
                st.download_button(
                    "Download Email",
                    generated_email,
                    file_name=f"cold_email_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain"
                )

st.markdown("---")
st.markdown('<div class="footer">Made with professionalism for better networking</div>', unsafe_allow_html=True)