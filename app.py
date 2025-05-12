import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard de Vendas")

# Exemplo de dados
dados = {
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr'],
    'Vendas': [100, 150, 130, 170]
}
df = pd.DataFrame(dados)

# Visualização
st.subheader("Tabela de Vendas")
st.dataframe(df)

st.subheader("Gráfico de Linha")
st.line_chart(df.set_index('Mês'))
