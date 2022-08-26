from PIL import Image
import streamlit as st
image = Image.open('sunrise.jpg')
st.image(image, caption='Sunrise by the mountains')
