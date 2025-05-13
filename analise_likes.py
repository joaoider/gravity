import pandas as pd
import glob
import os
import streamlit as st
@st.cache_data
def analisar_likes():
    caminho_arquivo = 'base/Base_Seofernandes.csv'
    df = pd.read_csv(caminho_arquivo, sep=';')

    pasta = r'C:\Users\joao.silva\Documents\GitHub\gravity\Resultados\Arquivos Individuais - Likes'
    arquivos_csv = glob.glob(os.path.join(pasta, "*.csv"))
    lista_dfs = []

    for arquivo in arquivos_csv:
        try:
            df_temp = pd.read_csv(arquivo, sep=';', on_bad_lines='skip')
            lista_dfs.append(df_temp)
        except pd.errors.ParserError:
            continue

    if not lista_dfs:
        return "Nenhum arquivo CSV válido encontrado para likes.", None

    df_final = pd.concat(lista_dfs, ignore_index=True)

    resultados = []
    resultados.append(f"Média de seguidores: {df_final['seguidores'].mean():,.2f}")
    resultados.append(f"Média de seguindo: {df_final['seguindo'].mean():,.2f}")
    resultados.append(f"Tamanho da base: {len(df_final)}")
    resultados.append(f"Quantidade de usernames únicos: {df_final['username'].nunique()}")

    usuarios_em_ambos = df_final[df_final['username'].isin(df['login'])]
    resultados.append(f"Usernames que também estão na coluna login da base principal: {len(usuarios_em_ambos)}")

    tabela = usuarios_em_ambos[['username', 'seguidores', 'seguindo']].drop_duplicates()

    return '\n'.join(resultados), tabela
