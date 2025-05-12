
import pandas as pd

# URL exportando como CSV
url = "https://docs.google.com/spreadsheets/d/1BUvrDgLYDPsKMcK5nNeJGtzRJDZPFFd9HkQHT1eLesI/export?format=csv"

# Carregar direto no pandas
df_following = pd.read_csv(url)

# Visualizar
print('_____________________________________________________________________________________')
print('following')
print(df_following.head())
