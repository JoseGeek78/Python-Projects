import pyshorteners
import streamlit as st

def shorten_url(url):
    s = pyshorteners.Shortener()