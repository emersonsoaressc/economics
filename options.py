import pandas as pd 

## Escolhendo tipo de análise a ser feita ##
option = [
    'Home',
    'Indicadores Econômicos',
    'Análise de Ativos'
]
covid = [
    'Casos x Mortes',
    'Políticas de isolamento adotadas',
    'Comparativo COVID x Imdicadores Econômicos',
]
iecon = [
    'IPCA',
    'IGPM',
    'SELIC',
    'CDI',
    'PIB',
]
atvs = [
    'Análise de Índices da B3',
    'Análise de Empresas listadas',
    
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

cod_ipca = pd.read_csv('base_csv/cod_ipca.csv', encoding='UTF-8', sep=';')
cod_selic = pd.read_csv('base_csv/cod_selic.csv', encoding='UTF-8', sep=';')


#df_setor = pd.DataFrame(df_base['Alimentos e bebidas', 'Habitação', 'Bens domésticos', 'Vestuário', 'Transportes', 'Comunicação', 'Saúde e cuidados pessoais', 'Despesas pessoais', 'Educação'])
