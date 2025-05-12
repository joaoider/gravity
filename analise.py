import pandas as pd

# Caminho até o arquivo
caminho_arquivo_base = 'base/Base_Seofernandes.csv'
df_base = pd.read_csv(caminho_arquivo_base, sep=';')
print('_____________________________________________________________________________________')
print('base')
print(df_base)

# Caminho até o arquivo
caminho_arquivo_amostra = 'amostra/base_amostra.csv'
df_amostra = pd.read_csv(caminho_arquivo_amostra, sep=',')
print('_____________________________________________________________________________________')
print('amostra')
print(df_amostra)

# Caminho até o arquivo
caminho_arquivo_followers = 'Resultados/followers_dados_completos.csv'
df_followers = pd.read_csv(caminho_arquivo_followers, sep=';')
print('_____________________________________________________________________________________')
print('followers')
print(df_followers)

# Caminho até o arquivo
caminho_arquivo_following = 'Resultados/followings_dados_completos.csv'
df_following = pd.read_csv(caminho_arquivo_following, sep=';')
print('_____________________________________________________________________________________')
print('following')
print(df_following)

# Obtendo logins em comum nos dois dataframes
logins_comuns = df_base[df_base['login'].isin(df_amostra['login'])]
print('_____________________________________________________________________________________')
print(len(logins_comuns))
print('Logins comuns nas duas bases:')
print(logins_comuns)

# Obtendo logins em comum nos dois dataframes
logins_comuns = df_base[df_base['login'].isin(df_amostra['login'])]
print('_____________________________________________________________________________________')
print('login comum base e amostra')
print(len(logins_comuns))
print('Logins comuns nas duas bases:')
print(logins_comuns)

# Obtendo logins em comum nos dois dataframes
logins_comuns2 = df_amostra[df_amostra['login'].isin(df_followers['source'])]
print('_____________________________________________________________________________________')
print('login comum base e followers source')
print(len(logins_comuns2))
print('Logins comuns nas duas bases:')
print(logins_comuns2)

# Obtendo logins em comum nos dois dataframes
logins_comuns3 = df_amostra[df_amostra['login'].isin(df_following['source'])]
print('_____________________________________________________________________________________')
print('login comum base e following source')
print(len(logins_comuns3))
print('Logins comuns nas duas bases:')
print(logins_comuns3)

# Obtendo logins em comum nos dois dataframes
logins_comuns4 = df_amostra[df_amostra['login'].isin(df_followers['username'])]
print('_____________________________________________________________________________________')
print('login comum base e followers username')
print(len(logins_comuns4))
print('Logins comuns nas duas bases:')
print(logins_comuns4)

# Obtendo logins em comum nos dois dataframes
logins_comuns5 = df_amostra[df_amostra['login'].isin(df_following['username'])]
print('_____________________________________________________________________________________')
print('login comum base e following username')
print(len(logins_comuns5))
print('Logins comuns nas duas bases:')
print(logins_comuns5)