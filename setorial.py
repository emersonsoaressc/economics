import pandas as pd 
import streamlit as st
import options as opt
import sgs
from func_pyeconomics import  graf_plotly
import plotly.graph_objects as go

### ========= ARQUITETURA DA PÁGINA ========= ###


### ==== FUNÇÃO PARA CRIAR PÁGINA DE ANÁLISE SETORIAL ==== ###

def pag_setorial():
# Fazendo a verificação do subtópico abordado
    lst_setorial = st.sidebar.selectbox('Selecione o setor que deseja abordar:',opt.lista_setorial)

