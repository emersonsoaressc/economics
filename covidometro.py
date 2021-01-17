import pandas as pd 
import streamlit as st
import options as opt
import sgs
from func_pyeconomics import  graf_plotly
import plotly.graph_objects as go
from covid import Covid

### ========= TRATAMENTO DE DADOS REFERENTE AO COVID ========= ###

# Listando países para criar dataframe
covid = Covid()
covid_paises = covid.list_countries()
covid_paises = pd.DataFrame(covid_paises)
covid_paises = covid_paises.set_index('id')
df = pd.DataFrame()
for i in covid_paises['name']:
  df1 = covid.get_status_by_country_name(i)
  df1 = pd.DataFrame.from_dict(df1, orient='index').T
  df = pd.concat([df,df1])


### ========= ARQUITETURA DA PÁGINA ========= ###


### ==== FUNÇÃO PARA CRIAR PÁGINA COVID ==== ###

def pag_covid():
# Fazendo a verificação do subtópico abordado
    lst_paises = st.sidebar.selectbox('Selecione o tópico que deseja abordar:',covid_paises)
    period = st.sidebar.slider('select',1980,2021,(2019,2021))
    st.write(df)
# Gerando base de dados
 