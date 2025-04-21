import streamlit as st

st.title("programming language App")

if st.button("programming language"):
    st.success("programming language success ")

programming_language = st.checkbox("python")

programming_languages = st.multiselect(
    "Select programming languages you know:",
    ["Python", "Java", "JavaScript", "C++"]
)

tea_type = st.radio("Pick your programming language: ", ["Python", "Java", "javascript", "C++"])


if tea_type == "Python":
    st.success(f"programming language {tea_type} ")
else:
     st.success(f"programming language {tea_type} not ")


st.write(f"Selected base {tea_type}")

flavour = st.selectbox("Choose flavour: ", ["Adrak", "Kesar", "Tulsi"])
st.write(f"Selected Flavour {flavour}")

sugar = st.slider("Sigar level (spoon)", 0, 5, 4)
st.write(f"Selected sugar level {sugar}")

cups = st.number_input("How many cups", min_value=1, max_value=10, step=1)
st.write(f"Selected sugar level {cups}")

name = st.text_input("Enter your name")
if name:
    st.write(f"Welcome, {name} ")

dob = st.date_input("Select your date of birth")
st.write(f"Your date of birth {dob}")