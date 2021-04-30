import pandas as pd 
import numpy as np 
import streamlit as st
import options as opt
from pandas_datareader import data
from func_pyeconomics import  graf_plotly, gera_carteira, normaliza_carteira
import plotly.graph_objects as go


### ==== FUNÇÃO PARA CRIAR PÁGINA DE ANÁLISE DE CARTEIRA ==== ###

def pag_carteira():
# ESCOLHENDO ATIVOS PARA ENTRAR NA CARTEIRA
    stocks_csv = pd.read_csv('base_csv/stocks.csv')
    stocks = st.sidebar.multiselect('Insira o ticker das ações na carteira:',stocks_csv)
    period = st.sidebar.slider('A partir de qual ano deseja analisar?:',2010,2021,(2010))
    n_stocks = len(stocks)  
    st.write(
        'Nesta página você poderá realizar a simulação de uma carteira de ações e compará-la com o benchmark (Ibovespa). Basta escolher os ativos e o período inicial na barra lateral. Os dados são extraídos de diversas fontes, sendo a fonte principal o YAHOO FINANCE. Também será realizada diversas análises referente ao portfólio.'
    )
    st.sidebar.write(
        'Coloque o peso que cada ativo terá na carteira'
    )
    peso = []
    for i in range(0,n_stocks):
        ps = st.sidebar.number_input(f'Peso do ativo {stocks[i]}',0,100,key=f'peso_{i}')
        peso.append(ps)
    if (sum(peso) != 100) & (n_stocks > 0):
        st.sidebar.write('A soma dos pesos tem que ser de 100%')
    elif (sum(peso) == 100):
        if st.sidebar.button('Gerar Carteira'):
            ### ========= ARQUITETURA DA PÁGINA ========= ### 

            ### ========= COMPARATIVO CARTEIRA X IBOVESPA ========= ### 
            st.write(
                '"COMPARATIVO - CARTEIRA X IBOVESPA"'
            )
            dataframe = gera_carteira(stocks,period)
            df_norm = normaliza_carteira(dataframe)
            df_norm.rename(columns={'^BVSP':'IBOVESPA'}, inplace=True)
            benchmark = pd.DataFrame(df_norm['IBOVESPA'])
            carteira = df_norm.drop(columns='IBOVESPA')
            carteira = carteira * peso/100
            carteira['CARTEIRA'] = carteira.sum(axis=1)
            cart = pd.DataFrame(carteira['CARTEIRA'])
            cart_bench = pd.concat([cart, benchmark], axis = 1)
            ativos_ibov = pd.concat([carteira, benchmark], axis = 1)
            st.write(graf_plotly(cart_bench))
            st.write(
                '"COMPARATIVO - ATIVOS X IBOVESPA"'
            )
            st.write(graf_plotly(df_norm))
            st.write(df_norm)
            st.write(carteira)
            ### ========= TAXA DE RETORNO DA CARTEIRA ========= ###
            st.write(
            '"TAXA DE RETORNO DA CARTEIRA"'
            )
            tx_retorno = (df_norm / df_norm.shift(1)) - 1
            retorno_anual = tx_retorno.mean() * 246
            st.write(retorno_anual)
            st.write(tx_retorno)
                ### ========= CORRELAÇÃO ENTRE OS ATIVOS ========= ###
            st.write(
            '"CORRELAÇÃO ENTRE OS ATIVOS"'
            )