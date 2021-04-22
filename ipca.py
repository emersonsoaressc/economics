import pandas as pd 
import streamlit as st
import options as opt
import sgs
from func_pyeconomics import  graf_plotly
import plotly.graph_objects as go

### ========= TRATAMENTO DE DADOS REFERENTE AO IPCA ========= ###




### ========= ARQUITETURA DA PÁGINA ========= ###


### ==== FUNÇÃO PARA CRIAR PÁGINA IPCA ==== ###

def pag_ipca():
# Fazendo a verificação do subtópico abordado
    lst_ipca = st.sidebar.selectbox('Selecione o tópico que deseja abordar:',opt.lista_ipca)
    period = st.sidebar.slider('select',1980,2022,(2019,2022))
# Gerando base de dados
    df_base = pd.read_csv('base_csv/base_ipca.csv', encoding='UTF-8', sep=',', index_col=0)
    a = period[0]
    b = period[1]
    interval = (df_base.index >= f'{a}-01-01') & (df_base.index <= f'{b}-01-01')
    df_interval = df_base[interval]
    graf_plotly(df_interval,'IPCA % Acumulado em 12 meses')
#  IPCA - % Variação Mensal Total
    if lst_ipca == 'IPCA - % Acumulado em 12 meses':
        df = pd.DataFrame(df_interval['IPCA Acumulado 12 meses'])
        st.write(graf_plotly(df,'IPCA % Acumulado em 12 meses'))
    elif lst_ipca == 'IPCA - % Variação Mensal Total':
        df = pd.DataFrame(df_interval['Variação Mensal Total'])
        st.write(graf_plotly(df,'IPCA - % Variação Mensal Total'))
    elif lst_ipca == 'IPCA - % Variação Mensal Setorizado':
        df = pd.DataFrame(df_interval)
        st.write(graf_plotly(df,'IPCA - % Variação Mensal Setorizado'))
        
        





