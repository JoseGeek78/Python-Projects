import qrcode
import streamlit as st

filename = 'qr_codes/qr_code.png'

def generate_qr_code(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color='black', back_color='white')
    img.save(filename)
    
st.set_page_config((page_title="QR Code Generator", page_icon="🌐", layout="centered")
