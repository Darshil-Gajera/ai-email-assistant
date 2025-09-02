# app.py
import streamlit as st
from email_generator import generate_email

st.set_page_config(page_title="AI Email Assistant", page_icon="📧")

st.title("📧 AI Email Assistant")
st.write("Generate, reply, or summarize emails with AI (formal or friendly tone).")

# User inputs
task = st.selectbox("Select Task", ["write", "reply", "summarize"])
tone = st.selectbox("Select Tone", ["formal", "friendly"])
content = st.text_area("Enter email prompt or text")

if st.button("Generate Email"):
    if content.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        with st.spinner("Generating email..."):
            email_output = generate_email(task, tone, content)
        st.success("✅ Email Generated!")
        st.text_area("AI Generated Email:", email_output, height=300)
