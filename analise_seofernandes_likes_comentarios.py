import pandas as pd

caminho_arquivo = 'curtidas_comentarios_seo/flavio_50k_seofernandes_dados_completos.csv'
df = pd.read_csv(caminho_arquivo, sep=';')
print('dataframe')
print(df)

print('tamanho da base')
print(len(df))

num_unicos = df['username'].nunique()
print(f"Quantidade de nomes únicos na coluna 'username': {num_unicos}")

print('média de seguidores: ', df['seguidores'].mean())
print('seguindo, em média: ', df['seguindo'].mean())
print('média de posts: ', df['posts'].mean())

caminho_arquivo2 = 'base/Base_Seofernandes.csv'
df2 = pd.read_csv(caminho_arquivo2, sep=';')
print('dataframe2')
print(df2)


print('________________________________________________________________________________________________')
# Verificar quais usernames estão também na coluna login
usernames_em_ambos = df[df['username'].isin(df2['login'])]
# Exibir quantidade de correspondências e os nomes únicos encontrados
print(f"Quantidade de usernames que também estão na coluna 'login': {len(usernames_em_ambos)}")
#print(f"Nomes únicos em comum: {usernames_em_ambos['username'].nunique()}")
#print("Usernames em comum:")
#print(usernames_em_ambos['username'].unique())