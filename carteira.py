import pandas as pd 
import streamlit as st
import options as opt
from pandas_datareader import data
from func_pyeconomics import  graf_plotly, gera_carteira, normaliza_carteira
import plotly.graph_objects as go

### ========= ARQUITETURA DA PÁGINA ========= ###


### ==== FUNÇÃO PARA CRIAR PÁGINA DE ANÁLISE DE CARTEIRA ==== ###

def pag_carteira():
# ESCOLHENDO ATIVOS PARA ENTRAR NA CARTEIRA
    stocks_csv = (pd.read_csv('base_csv/stocks.csv'),sorted)
    stocks = st.sidebar.multiselect('Insira o ticker das ações na carteira:',stocks_csv)
    period = st.sidebar.slider('A partir de qual ano deseja analisar?:',2000,2022,(2015))
    n_stocks = len(stocks)
    dataframe = gera_carteira(stocks,period)
    df_norm = normaliza_carteira(dataframe)
    benchmark = pd.DataFrame(df_norm['BOVA11.SA'])
    carteira = df_norm.drop(columns='BOVA11.SA')
    carteira['CARTEIRA'] = carteira.sum(axis=1) / len(carteira.columns)
    carteira = pd.DataFrame(carteira['CARTEIRA'])
    cart_bench = pd.concat([carteira, benchmark], axis = 1)
    st.write(graf_plotly(cart_bench))