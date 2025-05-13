import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")


from analise_comments import analisar_comentarios
from analise_followers import analisar_followers
from analise_following import analisar_following
from analise_likes_comments import analisar_likes_comments
from analise_likes import analisar_likes
from analise_seofernandes_likes_comentarios import analisar_seofernandes_likes_comentarios

# Pré-carregar as análises (cache garante que não serão reprocessadas)
texto_comments, tabela_comments = analisar_comentarios()
texto_followers, tabela_followers = analisar_followers()
texto_followings, tabela1_followings, tabela2_followings, tabela3_followings = analisar_following()
texto_likes_comments, tabela_likes_comments = analisar_likes_comments()
texto_likes, tabela_likes = analisar_likes()
texto_seofernandes, tabela_seofernandes = analisar_seofernandes_likes_comentarios()


st.title("Gravity")

# Criar colunas para o layout: botões à esquerda e resultado à direita
col1, col2 = st.columns([1, 3])

# Variável de controle
selecao = None

# Coluna 1: botões
with col1:
    st.image("seofernandes.PNG", width=150, caption="Seo Fernandes")
    st.markdown("### Análises")
    if st.button("Comments"):
        selecao = "comments"
    if st.button("Followers"):
        selecao = "followers"
    if st.button("Followings"):
        selecao = "followings"
    if st.button("Likes & Comments"):
        selecao = "likes_comments"
    if st.button("Likes"):
        selecao = "likes"
    if st.button("SeoFernandes - Likes & Comments"):
        selecao = "seofernandes"

# Coluna 2: exibir resultado com base na seleção
with col2:
    if selecao == "comments":
        st.subheader("Análise de Comments")
        st.text_area("Resumo da análise", texto_comments, height=250)
    
        if tabela_comments is not None and not tabela_comments.empty:
            st.dataframe(tabela_comments)

    elif selecao == "followers":
        st.subheader("Análise de Followers")

        st.text_area("Resumo da análise de followers", texto_followers, height=250)
        if tabela_followers is not None and not tabela_followers.empty:
            st.dataframe(tabela_followers)

    elif selecao == "followings":
        st.subheader("Análise de Followings")
        st.text_area("Resumo da análise de followings", texto_followings, height=250)

        if tabela1_followings is not None and not tabela1_followings.empty:
            st.write("Top usernames com mais aparições por seguidor:")
            st.dataframe(tabela1_followings)

        if tabela2_followings is not None and not tabela2_followings.empty:
            st.write("Logins encontrados entre os top usernames:")
            st.dataframe(tabela2_followings)

        if tabela3_followings is not None and not tabela3_followings.empty:
            st.write("Nomes em comum entre 'source' e 'username':")
            st.dataframe(tabela3_followings)


    elif selecao == "likes_comments":
        st.subheader("Análise de Likes & Comments")
        st.text_area("Resumo da análise de interseção", texto_likes_comments, height=150)
        if tabela_likes_comments is not None and not tabela_likes_comments.empty:
            st.dataframe(tabela_likes_comments)

    elif selecao == "likes":
        st.subheader("Análise de Likes")
        st.text_area("Resumo da análise de likes", texto_likes, height=250)
        if tabela_likes is not None and not tabela_likes.empty:
            st.dataframe(tabela_likes)

    elif selecao == "seofernandes":
        st.subheader("Seo Fernandes – Curtidas e Comentários")
        st.text_area("Resumo da análise do Seo Fernandes", texto_seofernandes, height=250)
        if tabela_seofernandes is not None and not tabela_seofernandes.empty:
            st.dataframe(tabela_seofernandes)

    else:
        st.markdown("### Selecione uma análise à esquerda.")
