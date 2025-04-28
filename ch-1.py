import streamlit as st

# Title
st.title("HI")

st.subheader("Brewed with streamlit")

# Text
st.text("Welcome to your first interative app")

# Write
st.write("Chooose your fav. variety of chai")

# SelectBox  CheckBox
chai = st.selectbox("Your fav programming language: ", ["Python", "Java", "javascript", "C++"])

# Passing arguments
st.write(f"Your choose {chai}. Excellent choise")

# Alters
st.success("Your programming language has been Good")