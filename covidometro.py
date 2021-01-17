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
df['% Mortalidade'] =  df['deaths'] / df['confirmed'] * 100  
df = df.iloc[0:10]   

### ========= ARQUITETURA DA PÁGINA ========= ###


### ==== FUNÇÃO PARA CRIAR PÁGINA COVID ==== ###

# Gerando Gráfico de Barras dos 10+
def graf_bar(covid_paises, df):
    fig = go.Figure()
    fig.update_layout(
        title= 'Covidômetro - Os 10+', 
        barmode='stack',
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='rgb(82, 82, 82)',
            ),
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=True,
            showline=True,
            showticklabels=True,
        ),
        autosize=True,
        margin=dict(
            autoexpand=True,
            l=100,
            r=20,
            t=110,
        ),
        showlegend=True,
        plot_bgcolor='white',
        legend= dict(
            font=dict(
                family='Arial',
                size=9)
        )
        )
    return (
        fig.add_trace(go.Scatter(x=covid_paises['name'], y=df['confirmed'], visible='legendonly')),
        fig.add_trace(go.Scatter(x=covid_paises['name'], y=df['active'], visible='legendonly')),
        fig.add_trace(go.Scatter(x=covid_paises['name'], y=df['deaths'], visible=True)),
        fig.add_trace(go.Scatter(x=covid_paises['name'], y=df['% Mortalidade'], visible='legendonly'))
    )

def pag_covid():
# Fazendo a verificação do subtópico abordado
    lst_paises = st.sidebar.selectbox('Selecione o tópico que deseja abordar:',covid_paises)
    period = st.sidebar.slider('select',1980,2021,(2019,2021))
    st.write(df)
    st.write(graf_bar(covid_paises, df))