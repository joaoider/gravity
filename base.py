import pandas as pd
from funcao import analisar_csv
# Caminho até o arquivo
caminho_arquivo = 'base/Base_Seofernandes.csv'
df = pd.read_csv(caminho_arquivo, sep=';')
print('dataframe')
print(df)

print('tamanho da bae')
print(len(df))

print('colunas do dataframe')
print(df.columns)

# Análise
print(df.info(verbose=True))
print(df.describe())

print('número médio de seguidores')
print(df['fol_cnt'].mean())

print('seguidor com mais seguidores')
print(df['fol_cnt'].max(), df.loc[df['fol_cnt'].idxmax(), 'login'])

print('seguindo, número médio')
print(df['sub_cnt'].mean())

print('seguindo, número posts')
print(df['post_cnt'].mean())



