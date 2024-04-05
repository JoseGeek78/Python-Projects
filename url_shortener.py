import pyshorteners
import streamlit as st

def shorten_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

#APP Web con streamlit
st.set_page_config(page_title="URL Shortener", page_icon="✏️", Layout="centered")
st.image("images/www.png", use_column_width=True)