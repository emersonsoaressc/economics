import pandas as pd 
import streamlit as st
import options as opt
from pandas_datareader import data
from func_pyeconomics import  graf_plotly, gera_carteira
import plotly.graph_objects as go

### ========= ARQUITETURA DA PÁGINA ========= ###


### ==== FUNÇÃO PARA CRIAR PÁGINA DE ANÁLISE DE CARTEIRA ==== ###

def pag_carteira():
# ESCOLHENDO ATIVOS PARA ENTRAR NA CARTEIRA
    stocks_csv = pd.read_csv('base_csv/stocks.csv')
    stocks = st.sidebar.multiselect('Insira o ticker das ações na carteira:',stocks_csv)
    period = st.sidebar.slider('A partir de qual ano deseja analisar?:',2000,2022,(2015))
    n_stocks = len(stocks)
    dataframe = gera_carteira(stocks,period)
    st.write('Você escolheu:', dataframe)