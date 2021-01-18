import pandas as pd
import streamlit as st
import options as opt
import sgs
from func_pyeconomics import graf_plotly, graf_covid_wbar, cria_df_covid
import plotly.graph_objects as go
from covid import Covid

### ========= TRATAMENTO DE DADOS REFERENTE AO COVID ========= ###



### ========= ARQUITETURA DA PÁGINA ========= ###


### ==== FUNÇÃO PARA CRIAR PÁGINA COVID ==== ###

def pag_covid():
# Fazendo a verificação do subtópico abordado
    df = cria_df_covid()
    #lst_paises = st.sidebar.selectbox('Selecione o tópico que deseja abordar:',paises)
    #period = st.sidebar.slider('select',1980,2021,(2019,2021))
    st.write(df)
    st.write(graf_covid_wbar(df))
