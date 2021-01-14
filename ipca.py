# ipca.py
import pandas as pd 
import streamlit as st
import functions as fc
import home as h
import options as opt
import sgs
import plotly.graph_objects as go

### ========= TRATAMENTO DE DADOS REFERENTE AO IPCA ========= ###




### ========= ARQUITETURA DA PÁGINA ========= ###


def pag_ipca():
# Fazendo a verificação do subtópico abordado
    lst_ipca = st.sidebar.selectbox('Selecione o tópico que deseja abordar:',opt.lista_ipca)
    period = st.sidebar.slider('select',1980,2021,(2019,2021))
# Gerando base de dados
    df_base = fc.gera_base(period[0], period[1])
#  IPCA - % Variação Mensal Total
    if lst_ipca == 'IPCA - % Acumulado em 12 meses':
        df = pd.DataFrame(df_base['IPCA Acumulado 12 meses'])
        st.write(fc.graf_plotly(df,'IPCA % Acumulado em 12 meses'))
    elif lst_ipca == 'IPCA - % Variação Mensal Total':
        df = pd.DataFrame(df_base['Variação Mensal Total'])
        st.write(fc.graf_plotly(df,'IPCA - % Variação Mensal Total'))
    elif lst_ipca == 'IPCA - % Variação Mensal Setorizado':
        df = pd.DataFrame(df_base)
        df
        st.write(fc.graf_plotly(df,'IPCA - % Variação Mensal Setorizado'))
        
        





