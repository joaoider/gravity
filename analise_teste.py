import pandas as pd
import glob
import os

pasta = r'C:\Users\joao.silva\Documents\GitHub\gravity\Resultados\Arquivos Individuais - Followings'
arquivos_csv = glob.glob(os.path.join(pasta, "*.csv"))
lista_dfs = []

for arquivo in arquivos_csv:
    try:
        df_temp = pd.read_csv(arquivo, sep=';', on_bad_lines='skip')
        lista_dfs.append(df_temp)
    except pd.errors.ParserError:
        continue

if not lista_dfs:
    print("Nenhum arquivo CSV válido encontrado.", None, None, None)

df_final = pd.concat(lista_dfs, ignore_index=True)
print(df_final)

resultados = []
resultados.append(f"Tamanho da base: {len(df_final)}")
resultados.append(f"Média de seguidores: {df_final['seguidores'].mean():,.2f}")
resultados.append(f"Média de seguindo: {df_final['seguindo'].mean():,.2f}")

top_usernames = df_final['username'].value_counts()
print(top_usernames)
seguidores = df_final.groupby('username')['seguidores'].mean()
print(seguidores)
# Criar DataFrame alinhado
resultado = pd.DataFrame(index=top_usernames.index)
resultado['aparicoes'] = top_usernames
resultado['seguidores'] = seguidores.reindex(top_usernames.index)
resultado['seguidores'] = resultado['seguidores'].astype(float)
print("Antes do dropna:", resultado.shape)
print(resultado[resultado['seguidores'].isna()])
# Remover possíveis NaNs em 'seguidores'
resultado = resultado.dropna(subset=['seguidores'])
# Calcular coluna de taxa
resultado['aparicoes_por_seguidor'] = (resultado['aparicoes'] / resultado['seguidores']) * 100000
# Ordenar
resultado_ordenado = resultado.sort_values(by='aparicoes', ascending=False)
print(resultado_ordenado)