import pandas as pd
import glob
import os

pasta = r'C:\Users\joao.silva\Documents\GitHub\gravity\scrapegram\seofernandes\Resultados\Arquivos Individuais - Followers'
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

print('tamanho base')
print(len(df_final))

print('média de seguidores')
print(df_final['seguidores'].mean())

print('seguindo, em média')
print(df_final['seguindo'].mean())

#print(df_final.loc[df_final['username']=='seofernandes'])

#print(df_final['username'].value_counts().head(10))

# Conjuntos únicos de valores
sources = set(df_final['source'].dropna().unique())
usernames = set(df_final['username'].dropna().unique())

# Interseção entre os dois conjuntos
nomes_em_ambas = sources.intersection(usernames)

# Exibir resultado
print(f"Quantidade de nomes que aparecem tanto em 'source' quanto em 'username': {len(nomes_em_ambas)}")
print("Nomes que aparecem em ambas as colunas:")
print(nomes_em_ambas)