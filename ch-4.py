import streamlit as st
import pandas as pd

# Data analysis 

st.title("Chai Sales Dashboard")

# File uploader
file  = st.file_uploader("UPload your csv file", type=["csv"])

# Data analysis using Pandas function
if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)
    # st.dataframe(df.head(3))

if file:
    st.subheader("Summary Stats")
    st.write(df.describe())
    st.bar_chart(df['City'])

if file:
    cities = df["City"].unique()
    selected_city = st.selectbox("Filter by cities", cities)
    filtered_data = df[df["City"] == selected_city]
    st.dataframe(filtered_data)