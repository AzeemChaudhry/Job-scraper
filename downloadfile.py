import streamlit as st
import requests

file_url = "https://raw.githubusercontent.com/AzeemChaudhry/Job-scraper/main/LearnMore.txt"
def download_file(url):
    try : 
        response = requests.get(file_url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching file : {e}")
        return None

