import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título da aplicação
st.title("Gravity")

# Layout com duas colunas
col1, col2 = st.columns([1, 3])  # col1 é mais estreita (imagem à esquerda)

# Coluna 1: imagem
with col1:
    st.image("seofernandes.PNG", width=150, caption="Seo Fernandes")

# Coluna 2: conteúdo principal (pode ficar vazio ou com outro conteúdo se desejar)
with col2:
    st.write("Bem-vindo à análise!")

# Espaço horizontal
st.markdown("---")

# Botões de análise abaixo
if st.button("Análise 1"):
    st.write("Executando análise 1...")

if st.button("Análise 2"):
    st.write("Executando análise 2...")

if st.button("Análise 3"):
    st.write("Executando análise 3...")