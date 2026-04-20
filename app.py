import streamlit as st
import pandas as pd
from recommender import recommend

# Load data
df = pd.read_csv("data/courses.csv")

st.set_page_config(page_title="Course Recommender", layout="wide")

st.markdown("<h1 style='text-align: center;'>🎓 Course Recommendation System</h1>", unsafe_allow_html=True)

# Sidebar filters
st.sidebar.header("🎯 Filters")

category = st.sidebar.selectbox("Select Category", ["All"] + list(df['Category'].unique()))

if category != "All":
    df = df[df['Category'] == category]

# Search
search = st.text_input("🔍 Search course")

filtered = df[df['Title'].str.contains(search, case=False, na=False)]

# Select course
course = st.selectbox("Select a course", filtered['Title'])

# Show selected course details
selected = df[df['Title'] == course]

st.markdown("## 📖 Course Details")
st.write(f"**Category:** {selected['Category'].values[0]}")
st.write(f"**Rating:** ⭐ {selected['Rating'].values[0]}")
st.write(selected['Description'].values[0])

# Recommendation
if st.button("🚀 Recommend"):
    results = recommend(course)

    st.markdown("## 📚 Recommended Courses")

    cols = st.columns(2)

    for i, r in enumerate(results):
        course_data = df[df['Title'] == r]

        with cols[i % 2]:
            st.markdown(f"""
            ### 🎓 {r}
            **Category:** {course_data['Category'].values[0]}  
            **Rating:** ⭐ {course_data['Rating'].values[0]}  
            """)
