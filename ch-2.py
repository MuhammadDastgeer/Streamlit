import streamlit as st

st.title("programming language App")

# button
if st.button("programming language"):
    st.success("programming language success ")

# checkbox
programming_language = st.checkbox("python")

# multiselect
programming_languages = st.multiselect(
    "Select programming languages you know:",
    ["Python", "Java", "JavaScript", "C++"]
)
# radio
tea_type = st.radio("Pick your programming language: ", ["Python", "Java", "javascript", "C++"])

# condition
if tea_type == "Python":
    st.success(f"programming language {tea_type} ")
else:
     st.success(f"programming language {tea_type} not ")

# Passing arguments
st.write(f"Selected base {tea_type}")

# selectbox
flavour = st.selectbox("Choose flavour: ", ["Adrak", "Kesar", "Tulsi"])
st.write(f"Selected Flavour {flavour}")

# slider
sugar = st.slider("Sigar level (spoon)", 0, 5, 4)
st.write(f"Selected sugar level {sugar}")


# Number input
cups = st.number_input("How many cups", min_value=1, max_value=10, step=1)
st.write(f"Selected sugar level {cups}")

# Text input
name = st.text_input("Enter your name")
if name:
    st.write(f"Welcome, {name} ")

# Date input
dob = st.date_input("Select your date of birth")
st.write(f"Your date of birth {dob}")