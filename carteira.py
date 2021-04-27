import pandas as pd 
import streamlit as st
import options as opt
from pandas_datareader import data
from func_pyeconomics import  graf_plotly
import plotly.graph_objects as go

### ========= ARQUITETURA DA PÁGINA ========= ###


### ==== FUNÇÃO PARA CRIAR PÁGINA DE ANÁLISE DE CARTEIRA ==== ###

def pag_carteira():
# ESCOLHENDO ATIVOS PARA ENTRAR NA CARTEIRA
    n_stocks = st.sidebar.slider('Quantos ativos irá compor a carteira?:', 1,10,(1))
    period = st.sidebar.slider('Selecione o Período:',2000,2022,(2015,2022))
    a = period[0]
    b = period[1]

    