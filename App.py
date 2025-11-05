import streamlit as st
from PIL import Image
import pandas as pd
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="My Portfolio", page_icon="🎯", layout="wide")

# --- HEADER ---
st.title("👋 Hello, I'm John Kevin Muyco")
st.subheader("Aspiring Software Architect | Data Science Enthusiast | Tech Explorer")

# --- SIDEBAR ---
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio("Go to:", ["About Me", "Portfolio", "Skills", "Contact"])

# --- ABOUT ME ---
if page == "About Me":
    st.header("👨‍💻 About Me")
    st.write("""
    I'm John Kevin Muyco, a passionate learner in software development and data science.  
    I enjoy solving real-world problems through code and creative thinking.
    
    In my free time, I love exploring new technologies, working on side hustles, and 
    experimenting with ideas like predictive maintenance and frozen dairy desserts! 🍦
    """)

    st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f", caption="Coding in progress", use_container_width=True)

    st.success("🎯 Current Goal: Become a professional Software Architect!")

# --- PORTFOLIO SECTION ---
elif page == "Portfolio":
    st.header("💼 My Portfolio")

    st.write("Here are some of the projects I’ve worked on:")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://images.unsplash.com/photo-1581090700227-1e37b190418e", use_container_width=True)
        st.markdown("**Expense Tracker App**")
        st.caption("A Spring Boot & React web app for managing income and expenses.")

    with col2:
        st.image("https://images.unsplash.com/photo-1556157382-97eda2d62296", use_container_width=True)
        st.markdown("**Predictive Maintenance System**")
        st.caption("A data science capstone project predicting machine failure.")

    with col3:
        st.image("https://www.allrecipes.com/thmb/YdAwH8wydX0R4qKnw8bI0-tt3ss=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/21105-butter-pecan-ice-cream-VAT-001-4x3-f9f792b2e8ac43c7b0aa8e37f2f8a608.jpg", use_container_width=True)
        st.markdown("**Frozen Dessert Business Concept**")
        st.caption("A small venture exploring dairy-based desserts.")

# --- SKILLS SECTION ---
elif page == "Skills":
    st.header("🧠 Skills & Tools")
    st.write("Here are some of my technical skills and ongoing learning progress:")

    skills = {
        "Python": 90,
        "Pandas": 80,
        "Machine Learning": 70,
        "Spring Boot": 75,
        "Frontend (React, HTML, CSS)": 65
    }

    for skill, percent in skills.items():
        st.text(skill)
        st.progress(percent)

    # Sample chart
    df = pd.DataFrame({
        "Skill": list(skills.keys()),
        "Proficiency": list(skills.values())
    })

    st.bar_chart(df.set_index("Skill"))

# --- CONTACT FORM ---
elif page == "Contact":
    st.header("📬 Contact Me")
    st.write("Let’s connect! Fill out the form below to reach me.")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send")

        if submitted:
            if name and email and message:
                with st.spinner("Sending your message..."):
                    time.sleep(1.5)
                st.success(f"Thanks {name}! I’ll get back to you at {email} soon.")
            else:
                st.warning("Please fill in all fields before submitting.")