import pandas as pd
import streamlit as st
import options as opt
import sgs
from func_pyeconomics import graf_plotly, graf_covid_wbar
import plotly.graph_objects as go
from covid import Covid

### ========= TRATAMENTO DE DADOS REFERENTE AO COVID ========= ###

# Listando países para criar dataframe
def cria_df_covid():
    covid = Covid()
    covid_paises = covid.list_countries()
    covid_paises = pd.DataFrame(covid_paises)
    covid_paises = covid_paises.set_index('id')
    df = pd.DataFrame()
    for i in covid_paises['name']:
        df1 = covid.get_status_by_country_name(i)
        df1 = pd.DataFrame.from_dict(df1, orient='index').T
        df = pd.concat([df, df1])
    df['% Mortalidade'] = df['deaths'] / df['confirmed'] * 100
    df = df.iloc[0:10]
    return (covid_paises, df)

### ========= ARQUITETURA DA PÁGINA ========= ###


### ==== FUNÇÃO PARA CRIAR PÁGINA COVID ==== ###

def pag_covid():
# Fazendo a verificação do subtópico abordado
    covid_paises, df = cria_df_covid()
    lst_paises = st.sidebar.selectbox('Selecione o tópico que deseja abordar:',covid_paises)
    period = st.sidebar.slider('select',1980,2021,(2019,2021))
    st.write(df)
    st.write(covid_paises)
    st.write(graf_covid_wbar(df))
