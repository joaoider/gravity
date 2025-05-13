import pandas as pd
import streamlit as st
@st.cache_data
def analisar_seofernandes_likes_comentarios():
    caminho_arquivo = 'curtidas_comentarios_seo/flavio_50k_seofernandes_dados_completos.csv'
    df = pd.read_csv(caminho_arquivo, sep=';')

    resultados = []
    resultados.append(f"Tamanho da base: {len(df)}")
    resultados.append(f"Quantidade de usernames únicos: {df['username'].nunique()}")
    resultados.append(f"Média de seguidores: {df['seguidores'].mean():,.2f}")
    resultados.append(f"Média de seguindo: {df['seguindo'].mean():,.2f}")
    resultados.append(f"Média de posts: {df['posts'].mean():,.2f}")

    caminho_arquivo2 = 'base/Base_Seofernandes.csv'
    df2 = pd.read_csv(caminho_arquivo2, sep=';')

    # Verificar quais usernames estão também na coluna login
    usernames_em_ambos = df[df['username'].isin(df2['login'])]
    resultados.append(f"Usernames que também estão na coluna 'login' da base principal: {len(usernames_em_ambos)}")

    # Tabela com os dados encontrados
    tabela = usernames_em_ambos[['username', 'seguidores', 'seguindo']].drop_duplicates()

    return '\n'.join(resultados), tabela
