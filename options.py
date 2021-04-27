import pandas as pd 

## Escolhendo tipo de análise a ser feita ##
option = [
    'Home',
    'Indicadores Econômicos',
    'Bolsa de Valores'
]
iecon = [
    'IPCA',
    'IGPM',
    'SELIC',
    'CDI',
    'PIB',
]
atvs = [
    'Análise de Carteira de Ações',
    'Análise Setorial',
    
]
lista_ipca = [
    'IPCA - % Acumulado em 12 meses',
    'IPCA - % Variação Mensal Total',
    'IPCA - % Variação Mensal Setorizado',   
]
lista_selic = [
    'SELIC (Taxa de Juros Diária)',
    'SELIC (Taxa de Juros Anual)',
    'SELIC (Taxa de Juros Meta Anual)', 
    'SELIC (Taxa de Juros Acumulado Mês)',  
]
lista_setorial = [
    'IEEX - ENERGIA ELÉTRICA',
  
]



cod_ipca = pd.read_csv('base_csv/cod_ipca.csv', encoding='UTF-8', sep=';')
cod_selic = pd.read_csv('base_csv/cod_selic.csv', encoding='UTF-8', sep=';')


#df_setor = pd.DataFrame(df_base['Alimentos e bebidas', 'Habitação', 'Bens domésticos', 'Vestuário', 'Transportes', 'Comunicação', 'Saúde e cuidados pessoais', 'Despesas pessoais', 'Educação'])
