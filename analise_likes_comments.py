import pandas as pd
import glob
import os

caminho_arquivo = 'base/Base_Seofernandes.csv'
df = pd.read_csv(caminho_arquivo, sep=';')
print('dataframe')
print(df)

import pandas as pd
import glob
import os

# -------------------- DataFrame de Likes --------------------
pasta_likes = r'C:\Users\joao.silva\Documents\GitHub\gravity\scrapegram\seofernandes\Resultados\Arquivos Individuais - Likes'
arquivos_likes = glob.glob(os.path.join(pasta_likes, "*.csv"))
lista_likes = []

for arquivo in arquivos_likes:
    try:
        df_temp = pd.read_csv(arquivo, sep=';', on_bad_lines='skip')
        lista_likes.append(df_temp)
    except pd.errors.ParserError as e:
        print(f"Erro no arquivo {arquivo}: {e}")

if lista_likes:
    df_likes = pd.concat(lista_likes, ignore_index=True)
    print("DataFrame de Likes:")
    print(df_likes.head())
else:
    print("Nenhum arquivo CSV válido encontrado para likes.")

# -------------------- DataFrame de Comments --------------------
pasta_comments = r'C:\Users\joao.silva\Documents\GitHub\gravity\scrapegram\seofernandes\Resultados\Arquivos Individuais - Comments'
arquivos_comments = glob.glob(os.path.join(pasta_comments, "*.csv"))
lista_comments = []

for arquivo in arquivos_comments:
    try:
        df_temp = pd.read_csv(arquivo, sep=';', on_bad_lines='skip')
        lista_comments.append(df_temp)
    except pd.errors.ParserError as e:
        print(f"Erro no arquivo {arquivo}: {e}")

if lista_comments:
    df_comments = pd.concat(lista_comments, ignore_index=True)
    print("DataFrame de Comments:")
    print(df_comments.head())
else:
    print("Nenhum arquivo CSV válido encontrado para comments.")





print('__________________________________________________________________________________________________________________')
# Obter os nomes únicos de cada DataFrame
usernames_likes = set(df_likes['username'].dropna().unique())
usernames_comments = set(df_comments['username'].dropna().unique())

# Verificar interseção
usernames_em_ambos = usernames_likes.intersection(usernames_comments)

# Exibir resultado
print(f"Quantidade de nomes que aparecem nas duas colunas 'username': {len(usernames_em_ambos)}")
print("Usernames em comum:")
print(len(usernames_em_ambos))
