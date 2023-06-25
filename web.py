import streamlit as st
import requests

API_KEY = "sqaKjy3ISCx7DT3uRA5tjtaP92f5z2g5ipyV6hq4"

url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

response = requests.get(url)
content = response.json()


title = st.title(content['title'])
image = st.image(content['url'])
description = st.write(content['explanation'])
