import streamlit as st
import numpy as np 
import pandas as pd 
from PIL import Image

## PÁGINA INICIAL

def main():
    st.title('PY ECONOMICS - A Economia em dados!')
    st.subheader('Projeto realizado por Emerson Soares')
    img_head = Image.open('imagens\python.jpg')
    st.sidebar.image(img_head, width= 300)
    st.sidebar.subheader('Menu Principal')

if __name__ == '__main__':
    main()

