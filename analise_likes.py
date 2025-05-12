import pandas as pd
import glob
import os

caminho_arquivo = 'base/Base_Seofernandes.csv'
df = pd.read_csv(caminho_arquivo, sep=';')
print('dataframe')
print(df)

pasta = r'C:\Users\joao.silva\Documents\GitHub\gravity\scrapegram\seofernandes\Resultados\Arquivos Individuais - Likes'
arquivos_csv = glob.glob(os.path.join(pasta, "*.csv"))
lista_dfs = []

for arquivo in arquivos_csv:
    try:
        df_temp = pd.read_csv(arquivo, sep=';', on_bad_lines='skip')  # ajuste o sep se necessário
        lista_dfs.append(df_temp)
    except pd.errors.ParserError as e:
        print(f"Erro no arquivo {arquivo}: {e}")

if lista_dfs:
    df_final = pd.concat(lista_dfs, ignore_index=True)
    print(df_final.head())
else:
    print("Nenhum arquivo CSV válido encontrado.")

print('média de seguidores')
print(df_final['seguidores'].mean())

print('seguindo, em média')
print(df_final['seguindo'].mean())

#print(df_final.loc[df_final['username']=='seofernandes'])

print('__________________________________________________________________________________________________________________')
print('tamanho base')
print(len(df_final))

print('____________________________________________________________________________________________________________')
num_unicos = df_final['username'].nunique()
print(f"Quantidade de nomes únicos na coluna 'username': {num_unicos}")


print('_____________________________________________________________________________________________________')
# Verifica quais usernames do df_final também estão na coluna login do df
usuarios_em_ambos = df_final[df_final['username'].isin(df['login'])]
# Exibe o total e os dados encontrados
print(f"Quantidade de usernames que também estão na coluna login: {len(usuarios_em_ambos)}")
print(usuarios_em_ambos[['username', 'seguidores', 'seguindo']].drop_duplicates())




print('__________________________________________________________________________________________')



print('__________________________________________________________________________________________')