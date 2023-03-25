import requests
import streamlit as st

# Things to define:
# Content <>
# Date
# Explanation
# URL <>
# title <>

st.set_page_config(layout="centered")

api_key = "ReQ9VzraozX7tQCzpKP4Bvxbkm4OgYQawXUUZumi"
text_url = "https://api.nasa.gov/planetary/apod?api_key=ReQ9VzraozX7tQCzpKP4Bvxbkm4OgYQawXUUZumi"
image_url = "https://apod.nasa.gov/apod/image/2303/_GHR3094-venerelunafirma800.jpg"

text_responses = requests.get(url=text_url)
image_responses = requests.get(url=image_url)
image = image_responses.content
texts = text_responses.json()

st.write(f"<h3><center><i> Date: {texts['date']} </i></center></h3>", unsafe_allow_html=True)
st.write(f"<h1><center> {texts['title']} </center></h1>", unsafe_allow_html=True)
st.image('_GHR3094-venerelunafirma800.jpg')
st.write(f"<center> {texts['explanation']} </center>", unsafe_allow_html=True, element_justification='justify')
st.write(f"<center> <a href{texts['url']} </center>", unsafe_allow_html=True)






