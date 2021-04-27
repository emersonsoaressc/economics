import numpy as np 
import pandas as pd  
import sgs
import plotly.graph_objects as go
import options as opt
from pandas_datareader import data

### ==== FUNÇÃO PARA CRIAR GRÁFICOS DO PLOTLY A PARTIR DE BASE DE DADOS SGS BACEN ==== ###
def graf_plotly(data_frame, titulo=""):
    fig = go.Figure()
    fig.update_layout(
    title= f'{titulo}', 

    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=1,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        title= '',
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
            lines = fig.add_trace(go.Scatter(x=data_frame.index, y=data_frame[f'{i}'], name= f"{i}", mode="lines", visible=True))
        elif count == 2:
            count += 1
            lines = fig.add_trace(go.Scatter(x=data_frame.index, y=data_frame[f'{i}'], name= f"{i}", mode="lines", visible=True))
        elif count >2:
            count += 1
            lines = fig.add_trace(go.Scatter(x=data_frame.index, y=data_frame[f'{i}'], name= f"{i}", mode="lines", visible='legendonly'))
    return lines


### ==== FUNÇÃO PARA CRIAR DATAFRAMES A PARTIR DE DADOS DO YAHOO ==== ###
def gera_carteira(ativos,ano_inicio):
    lista_ativos = ativos + ['BOVA11.SA']
    dataframe = pd.DataFrame()
 
    for i in lista_ativos:
        frame = data.DataReader(i, data_source='yahoo', start=f'{ano_inicio}-01-01')
        frame = frame['Adj Close']
        frame = pd.DataFrame(frame)
        frame = frame.rename(columns={'Adj Close':f'{i}'})
        dataframe = pd.concat([frame, dataframe], axis = 1)
    return dataframe