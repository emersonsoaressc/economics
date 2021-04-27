import streamlit as st
import numpy as np 
import pandas as pd  
import sgs
import plotly.graph_objects as go
import options as opt
from func_pyeconomics import  graf_plotly
from ipca import pag_ipca
from selic import pag_selic
from setorial import pag_setorial
from covidometro import pag_covid
import locale
locale.setlocale(locale.LC_ALL, )





### ========= FUNÇÕES PARA CRIAR A ARQUITETURA DA PÁGINA ========= ###

## PÁGINA INICIAL
st.title('Coleta e Análise de Indicadores Econômicos utilizando o Python')
st.subheader('Desenvolvido por Emerson Soares')
st.subheader('Aluno do curso de Ciências Econômicas - UDESC')
st.sidebar.subheader('Menu Principal')
slt = st.sidebar.selectbox('Selecione o tipo de análise:', opt.option)
    
## MENU PRINCIPAL
if slt == 'Home':
    ''
#elif slt == 'Covidômetro':
#    cvd = st.sidebar.selectbox('Selecione o tópico que deseja abordar:',opt.covid)
#    if cvd == 'Casos x Mortes':
#        pag_covid()
elif slt == 'Indicadores Econômicos':
    iec = st.sidebar.selectbox('Selecione o tópico que deseja abordar:',opt.iecon)
    
    # Layout da escolha IPCA
    if iec == 'IPCA': 
        pag_ipca()               
    elif iec == 'IGPM':
        ''      
    elif iec == 'SELIC':
        pag_selic()
    # Layout da escolha SELIC
    elif iec == 'SELIC':
        lst_selic = st.sidebar.selectbox('Selecione o tópico que deseja abordar:',opt.lista_selic)
        period = st.sidebar.slider('select',1980,2021,(2019,2021)) 
        # SELIC - % Taxa de Juros
        if lst_selic == 'SELIC - % Taxa de Juros':
            '  '

elif slt == 'Bolsa de Valores':
    atv = st.sidebar.selectbox('Selecione o tópico que deseja abordar:',opt.atvs)

    # Layout da escolha SETORIAL
    if atv == 'Análise Setorial':
        pag_setorial()
    elif atv == 'Análise de Carteira de Ações'