import pandas as pd 
import streamlit as st
import options as opt
import sgs
from func_pyeconomics import  graf_plotly
import plotly.graph_objects as go

### ========= TRATAMENTO DE DADOS REFERENTE A SELIC ========= ###




### ========= ARQUITETURA DA PÁGINA ========= ###


### ==== FUNÇÃO PARA CRIAR PÁGINA IPCA ==== ###

def pag_selic():
# Fazendo a verificação do subtópico abordado
    lst_selic = st.sidebar.selectbox('Selecione o tópico que deseja abordar:',opt.lista_selic)
    period = st.sidebar.slider('select',1980,2022,(2019,2022))
# Gerando base de dados
    df_base = pd.read_csv('base_csv/base_selic.csv', encoding='UTF-8', sep=',', index_col=0)
    a = period[0]
    b = period[1]
    interval = (df_base.index >= f'{a}-01-01') & (df_base.index <= f'{b}-01-01')
    df_interval = df_base[interval]
    graf_plotly(df_interval,'SELIC (Taxa de Juros diária)')
#  SELIC - % Taxa de Juros
    if lst_selic == 'SELIC (Taxa de Juros Diária)':
        df = pd.DataFrame(df_interval['SELIC (Taxa de Juros diária)'])
        st.write(graf_plotly(df,'SELIC (Taxa de Juros diária)'))

    elif lst_selic == 'SELIC (Taxa de Juros Anual)':
        df = pd.DataFrame(df_interval['SELIC (Taxa de Juros Anual)'])
        st.write(graf_plotly(df,'SELIC (Taxa de Juros Anual)'))

    elif lst_selic == 'SELIC (Taxa de Juros Meta Anual)':
        df = pd.DataFrame(df_interval['SELIC (Taxa de juros meta)'])
        st.write(graf_plotly(df,'SELIC (Taxa de Juros Meta Anual)'))

    elif lst_selic == 'SELIC (Taxa de Juros Acumulado Mês)':
        df = pd.DataFrame(df_interval['SELIC (Taxa de Juros acumulado Mês)'])
        st.write(graf_plotly(df,'SELIC (Taxa de Juros Acumulado Mês'))
        