import requests
import streamlit as st

api_key = ''

def openai_request(prompt):
    
    headers = {'Authorization':  f'Bearer {api_key}'}
    response = requests.post(
        'https://api.openai.com/v1/images/generations',
        headers=headers,
        json={
            'prompt': prompt,
            'model': 'dall-e-3',
            'size': '1792x1024',
            'quality': 'standard',
            'n': 1
        }
    )
    if response.status_code != 200:
        raise Exception(response.jason())
    else:
        image_url = response.json()['data'][0]['url']
        
    return image_url

def download_image(url, filename):
    response = requests.get(url)
    with open(filename, 'wd') as file:
        file.write(response.content)
        
        
st.set_page_config(page_title="AI Image Generator", page_icon="🤖", layout="centered")


st.image('images/full.jpg', use_column_width=True)
st.title('AI Image Generator')
description = st.text_area('Prompt')

if st.button('Generate Image'):
    with st.spinner('Generating your image...'):
        url = openai_request(description)
        filename = 'AI_images/image_generator.png'