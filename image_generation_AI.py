import requests
import streamlit as st

api_key = ''

def openai_request(prompt):
    
    headers = {'Authorization':  f'Bearer {api_key}'}
    response = 