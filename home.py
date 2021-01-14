import streamlit as st
import numpy as np 
import pandas as pd 

import options as opt
import functions as fc
from ipca import pag_ipca



## PÁGINA INICIAL
st.title('PY ECONOMICS - A Economia em dados!')


st.sidebar.subheader('Menu Principal')
slt = st.sidebar.selectbox('Selecione o tipo de análise:', opt.option)
    
## MENU PRINCIPAL
if slt == 'Home':
    ''
elif slt == 'Covidômetro':
    cvd = st.sidebar.selectbox('Selecione o tópico que deseja abordar:',opt.covid)
    
elif slt == 'Indicadores Econômicos':
    iec = st.sidebar.selectbox('Selecione o tópico que deseja abordar:',opt.iecon)
    
    # Layout da escolha IPCA
    if iec == 'IPCA': 
        pag_ipca()               
    elif iec == 'IGPM':
        ''      

    # Layout da escolha SELIC
    elif iec == 'SELIC':
        lst_selic = st.sidebar.selectbox('Selecione o tópico que deseja abordar:',opt.lista_selic)
        period = st.sidebar.slider('select',1980,2021,(2019,2021)) 
        # SELIC - % Taxa de Juros
        if lst_selic == 'SELIC - % Taxa de Juros':
            cod_selic = opt.cod_selic['cod']
            st.write(fc.graf_plotly(cod_selic, f'01/01/{period[0]}', f'01/01/{period[1]}', 'SELIC - % Taxa de Juros'))
            

elif slt == 'Análise de Ativos':
    atv = st.sidebar.selectbox('Selecione o tópico que deseja abordar:',opt.atvs)