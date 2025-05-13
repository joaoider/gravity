import pandas as pd
import os
import glob
import streamlit as st
@st.cache_data
def analisar_followers():
    pasta = r'C:\Users\joao.silva\Documents\GitHub\gravity\Resultados\Arquivos Individuais - Followers'
    arquivos_csv = glob.glob(os.path.join(pasta, "*.csv"))
    lista_dfs = []

    for arquivo in arquivos_csv:
        try:
            df_temp = pd.read_csv(arquivo, sep=';', on_bad_lines='skip')
            lista_dfs.append(df_temp)
        except pd.errors.ParserError as e:
            continue

    if not lista_dfs:
        return "Nenhum arquivo CSV válido encontrado.", None

    df_final = pd.concat(lista_dfs, ignore_index=True)

    resultados = []
    resultados.append(f"Tamanho da base: {len(df_final)}")
    resultados.append(f"Média de seguidores: {df_final['seguidores'].mean():,.2f}")
    resultados.append(f"Média de seguindo: {df_final['seguindo'].mean():,.2f}")

    # Conjuntos únicos de valores
    sources = set(df_final['source'].dropna().unique())
    usernames = set(df_final['username'].dropna().unique())
    nomes_em_ambas = sources.intersection(usernames)

    resultados.append(f"Nomes em comum entre 'source' e 'username': {len(nomes_em_ambas)}")

    # Tabela com os nomes (convertendo set para DataFrame)
    tabela = pd.DataFrame(sorted(nomes_em_ambas), columns=["nomes_em_ambas"])

    return '\n'.join(resultados), tabela
