import pandas as pd
import glob
import os
import streamlit as st

@st.cache_data
def analisar_likes_comments():
    # Base principal
    caminho_arquivo = 'base/Base_Seofernandes.csv'
    df = pd.read_csv(caminho_arquivo, sep=';')  

    # Amostra
    caminho_arquivo_amostra = 'base/Base_Seofernandes.csv'  # você pode trocar para outro caminho se necessário
    df_amostra = pd.read_csv(caminho_arquivo_amostra, sep=';')  

    # -------------------- Likes --------------------
    pasta_likes = r'C:\Users\joao.silva\Documents\GitHub\gravity\Resultados\Arquivos Individuais - Likes'
    arquivos_likes = glob.glob(os.path.join(pasta_likes, "*.csv"))
    lista_likes = []

    for arquivo in arquivos_likes:
        try:
            df_temp = pd.read_csv(arquivo, sep=';', on_bad_lines='skip')
            lista_likes.append(df_temp)
        except pd.errors.ParserError:
            continue

    if not lista_likes:
        return "Nenhum arquivo válido de likes encontrado.", None

    df_likes = pd.concat(lista_likes, ignore_index=True)

    # -------------------- Comments --------------------
    pasta_comments = r'C:\Users\joao.silva\Documents\GitHub\gravity\Resultados\Arquivos Individuais - Comments'
    arquivos_comments = glob.glob(os.path.join(pasta_comments, "*.csv"))
    lista_comments = []

    for arquivo in arquivos_comments:
        try:
            df_temp = pd.read_csv(arquivo, sep=';', on_bad_lines='skip')
            lista_comments.append(df_temp)
        except pd.errors.ParserError:
            continue

    if not lista_comments:
        return "Nenhum arquivo válido de comments encontrado.", None

    df_comments = pd.concat(lista_comments, ignore_index=True)

    # -------------------- Interseções --------------------
    usernames_likes = set(df_likes['username'].dropna().unique())
    usernames_comments = set(df_comments['username'].dropna().unique())
    usernames_em_ambos = usernames_likes.intersection(usernames_comments)

    texto = []
    texto.append(f"Quantidade de nomes que aparecem em likes e comments: {len(usernames_em_ambos)}")

    # Tabela de usernames em ambos
    tabela = pd.DataFrame(sorted(usernames_em_ambos), columns=["usernames_em_ambos"])

    # -------------------- Análises com amostra --------------------

    # Likes que estão na amostra
    usernames_likes_amostra = df_likes[df_likes['username'].isin(df_amostra['login'])]
    texto.append(f"Usernames de likes que estão na amostra: {len(usernames_likes_amostra['username'].unique())}")
    tabela_likes_amostra = usernames_likes_amostra[['username', 'seguidores', 'seguindo']].drop_duplicates()

    # Comments que estão na amostra
    usernames_comments_amostra = df_comments[df_comments['username'].isin(df_amostra['login'])]
    texto.append(f"Usernames de comments que estão na amostra: {len(usernames_comments_amostra['username'].unique())}")
    tabela_comments_amostra = usernames_comments_amostra[['username', 'seguidores', 'seguindo']].drop_duplicates()

    return '\n'.join(texto), tabela, tabela_likes_amostra, tabela_comments_amostra
