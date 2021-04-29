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
    stocks_csv = pd.read_csv('base_csv/stocks.csv').sort_values('cod_ativo',ascending=True)
    stocks = st.sidebar.multiselect('Insira o ticker das ações na carteira:',stocks_csv)
    period = st.sidebar.slider('A partir de qual ano deseja analisar?:',2000,2021,(2002))
    n_stocks = len(stocks)
    if st.sidebar.button('Gerar Carteira'):
        cart_bench = None
        dataframe = gera_carteira(stocks,2010)
        df_norm = normaliza_carteira(dataframe)
        benchmark = pd.DataFrame(df_norm['^BVSP'])
        carteira = df_norm.drop(columns='^BVSP')
        carteira['CARTEIRA'] = carteira.sum(axis=1) / len(carteira.columns)
        cart = pd.DataFrame(carteira['CARTEIRA'])
        cart_bench = pd.concat([cart, benchmark], axis = 1)
        st.write(graf_plotly(cart_bench))
        st.write(cart_bench)
        st.write(carteira)