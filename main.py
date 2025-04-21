import streamlit as st

st.title("HI")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first interative app")
st.write("Chooose your fav. variety of chai")

chai = st.selectbox("Your fav programming language: ", ["Python", "Java", "javascript", "C++"])
st.write(f"Your choose {chai}. Excellent choise")

st.success("Your programming language has been Good")