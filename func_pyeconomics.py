import numpy as np 
import pandas as pd  
import sgs
import plotly.graph_objects as go
import options as opt
from covid import Covid

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


### ==== FUNÇÃO PARA CRIAR GRÁFICOS DO PLOTLY A PARTIR DE BASE DE DADOS SGS BACEN ==== ###
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

def graf_covid_wbar(data_frame):
    covid_paises, df = cria_df_covid()
    fig = go.Figure(data=[
    go.Bar(name='Casos confirmados', x=data_frame['country'], y=df['confirmed'], visible='legendonly'),
    go.Bar(name='Casos Ativos', x=data_frame['country'], y=df['active'], visible='legendonly'),
    go.Bar(name='Mortes', x=data_frame['country'], y=df['deaths'], visible=True),
    go.Bar(name='% Mortalidade', x=data_frame['country'], y=df['% Mortalidade'], visible='legendonly')])
    fig.update_layout(barmode='stack', xaxis_tickangle=-45)
    fig.show()
    
