import pandas as pd
import glob
import os
import streamlit as st
@st.cache_data
def analisar_following():
    caminho_arquivo = 'base/Base_Seofernandes.csv'
    df = pd.read_csv(caminho_arquivo, sep=';')

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
        return "Nenhum arquivo CSV válido encontrado.", None, None, None

    df_final = pd.concat(lista_dfs, ignore_index=True)

    resultados = []
    resultados.append(f"Tamanho da base: {len(df_final)}")
    resultados.append(f"Média de seguidores: {df_final['seguidores'].mean():,.2f}")
    resultados.append(f"Média de seguindo: {df_final['seguindo'].mean():,.2f}")

    top_usernames = df_final['username'].value_counts()
    seguidores = df_final.groupby('username')['seguidores'].mean()
    # Criar DataFrame alinhado
    resultado = pd.DataFrame(index=top_usernames.index)
    resultado['aparicoes'] = top_usernames
    resultado['seguidores'] = seguidores.reindex(top_usernames.index)
    # Remover possíveis NaNs em 'seguidores'
    resultado = resultado.dropna(subset=['seguidores'])
    # Calcular coluna de taxa
    resultado['aparicoes_por_seguidor'] = (resultado['aparicoes'] / resultado['seguidores']) * 100000
    # Ordenar
    resultado_ordenado = resultado.sort_values(by='aparicoes', ascending=False)

    # Verificar quais top_usernames estão na coluna login do df base
    usernames_na_base = resultado.index.intersection(df['login'])
    top_usernames_na_base = resultado.loc[usernames_na_base].sort_values(by='aparicoes', ascending=False)

    # Verificar quais logins estão entre os top usernames
    nomes_top = top_usernames.index
    logins_encontrados = df[df['login'].isin(nomes_top)][['login']].drop_duplicates()

    # Nomes em comum entre source e username
    sources = set(df_final['source'].dropna().unique())
    usernames = set(df_final['username'].dropna().unique())
    nomes_em_ambas = sources.intersection(usernames)
    nomes_comuns_df = pd.DataFrame(sorted(nomes_em_ambas), columns=["nomes_em_ambas"])
    resultados.append(f"Nomes em comum entre 'source' e 'username': {len(nomes_em_ambas)}")

    return '\n'.join(resultados), resultado_ordenado, logins_encontrados, nomes_comuns_df, top_usernames_na_base

