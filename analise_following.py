import pandas as pd
import glob
import os

caminho_arquivo = 'base/Base_Seofernandes.csv'
df = pd.read_csv(caminho_arquivo, sep=';')
print('dataframe')
print(df)

pasta = r'C:\Users\joao.silva\Documents\GitHub\gravity\scrapegram\seofernandes\Resultados\Arquivos Individuais - Followings'
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
df_final['seguidores'].mean()

print('seguindo, em média')
df_final['seguindo'].mean()

#print(df_final.loc[df_final['username']=='seofernandes'])


print('__________________________________________________________________________________________')
# Top 100 usernames mais frequentes
top_usernames = df_final['username'].value_counts().head(100)
# Média de seguidores por username
seguidores = df_final.groupby('username')['seguidores'].mean()
# Juntar as informações
resultado = pd.DataFrame({
    'aparicoes': top_usernames,
    'seguidores': seguidores[top_usernames.index]
})
# Exibir resultado
# Adicionar a coluna com o valor de aparições dividido por seguidores
resultado['aparicoes_por_seguidor'] = (resultado['aparicoes'] / resultado['seguidores'])*100000
# Ordenar do maior para o menor com base na nova coluna
resultado_ordenado = resultado.sort_values(by='aparicoes_por_seguidor', ascending=False)
# Exibir resultado
print('resultado dos mais seguidores, número de seguidores e aparições por seguidor')
print(resultado_ordenado)



print('__________________________________________________________________________________________')
# Obter os nomes dos top usernames (índice do value_counts)
nomes_top = top_usernames.index
# Verificar quais logins estão entre os top usernames
logins_encontrados = df[df['login'].isin(nomes_top)]
# Exibir os resultados
print(f"{len(logins_encontrados)} logins encontrados que estão entre os top usernames:")
print(logins_encontrados)


print('__________________________________________________________________________________________')
# Conjuntos únicos de valores
sources = set(df_final['source'].dropna().unique())
usernames = set(df_final['username'].dropna().unique())
# Interseção entre os dois conjuntos
nomes_em_ambas = sources.intersection(usernames)
# Exibir resultado
print(f"Quantidade de nomes que aparecem tanto em 'source' quanto em 'username': {len(nomes_em_ambas)}")
print("Nomes que aparecem em ambas as colunas:")
print(nomes_em_ambas)