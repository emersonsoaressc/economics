import streamlit as st
import numpy as np 
import pandas as pd  
import sgs
import plotly.graph_objects as go
import options as opt
import locale
locale.setlocale(locale.LC_ALL, )

### ==== FUNÇÃO PARA CRIAR GRÁFICOS DO PLOTLY A PARTIR DE BASE DE DADOS SGS BACEN ==== ###
def graf_plotly(data_frame, titulo):
    fig = go.Figure()
    fig.update_layout(
    title= f'{titulo}', 

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
        title= '%',
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
    count = 0
    for i in data_frame.columns:
        if count < 2:
            count += 1
            lines = fig.add_trace(go.Scatter(x=data_frame.index, y=data_frame[f'{i}'], name= f"{i}", mode="markers+lines", visible=True))
        elif count == 2:
            count += 1
            lines = fig.add_trace(go.Scatter(x=data_frame.index, y=data_frame[f'{i}'], name= f"{i}", mode="lines", visible=True))
        elif count >2:
            count += 1
            lines = fig.add_trace(go.Scatter(x=data_frame.index, y=data_frame[f'{i}'], name= f"{i}", mode="lines", visible='legendonly'))
    return lines


### ========= FUNÇÕES PARA CRIAR A ARQUITETURA DA PÁGINA ========= ###

### ==== FUNÇÃO PARA CRIAR PÁGINA IPCA ==== ###

def pag_ipca():
# Fazendo a verificação do subtópico abordado
    lst_ipca = st.sidebar.selectbox('Selecione o tópico que deseja abordar:',opt.lista_ipca)
    period = st.sidebar.slider('select',1980,2021,(2019,2021))
# Gerando base de dados
    df_base = pd.read_csv('base_csv/base_ipca.csv', encoding='UTF-8', sep=',', index_col=0')
#  IPCA - % Variação Mensal Total
    if lst_ipca == 'IPCA - % Acumulado em 12 meses':
        df = pd.DataFrame(df_base['IPCA Acumulado 12 meses'])
        st.write(graf_plotly(df,'IPCA % Acumulado em 12 meses'))
    elif lst_ipca == 'IPCA - % Variação Mensal Total':
        df = pd.DataFrame(df_base['Variação Mensal Total'])
        st.write(graf_plotly(df,'IPCA - % Variação Mensal Total'))
    elif lst_ipca == 'IPCA - % Variação Mensal Setorizado':
        df = pd.DataFrame(df_base)
        st.write(graf_plotly(df,'IPCA - % Variação Mensal Setorizado'))


## PÁGINA INICIAL
st.title('PY ECONOMICS - A Economia em dados!')
st.sidebar.subheader('Menu Principal')
slt = st.sidebar.selectbox('Selecione o tipo de análise:', opt.option)
    
## MENU PRINCIPAL
if slt == 'Home':
    ''
elif slt == 'Covidômetro':
    cvd = st.sidebar.selectbox('Selecione o tópico que deseja abordar:',opt.covid)
    
elif slt == 'Indicadores Econômicos':
    iec = st.sidebar.selectbox('Selecione o tópico que deseja abordar:',opt.iecon)
    
    # Layout da escolha IPCA
    if iec == 'IPCA': 
        pag_ipca()               
    elif iec == 'IGPM':
        ''      

    # Layout da escolha SELIC
    elif iec == 'SELIC':
        lst_selic = st.sidebar.selectbox('Selecione o tópico que deseja abordar:',opt.lista_selic)
        period = st.sidebar.slider('select',1980,2021,(2019,2021)) 
        # SELIC - % Taxa de Juros
        if lst_selic == 'SELIC - % Taxa de Juros':
            '  '

elif slt == 'Análise de Ativos':
    atv = st.sidebar.selectbox('Selecione o tópico que deseja abordar:',opt.atvs)