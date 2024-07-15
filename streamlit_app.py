import streamlit as st
import downloadfile as df
st.title("Job Scraper")
st.write(
    "Lets you search for jobs on specified websites, according to your needs.\n"
)
file_url = "https://raw.githubusercontent.com/AzeemChaudhry/Job-scraper/main/LearnMore.txt" #file url to download 

with st.expander("Click to learn more"): 
    LearnMore = df.download_file(file_url)
    if LearnMore:
       st.write(LearnMore)
