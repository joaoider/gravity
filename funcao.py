import pandas as pd
import os

def analisar_csv(caminho_arquivo, salvar_em_txt=False, caminho_saida_txt='analise_resultado.txt'):
    # Leitura do arquivo CSV como DataFrame
    df = pd.read_csv(caminho_arquivo, sep=';')
    
    # String para armazenar os resultados
    resultados = []
    
    def adicionar_resultado(titulo, conteudo):
        resultados.append('\n' + '_'*90)
        resultados.append(f'\n{titulo}:\n')
        resultados.append(str(conteudo))
    
    # Análise
    adicionar_resultado('DataFrame', df)
    adicionar_resultado('DataFrame Info', df.info(verbose=True))
    adicionar_resultado('DataFrame Describe', df.describe())
    adicionar_resultado('DataFrame Length', len(df))
    
    adicionar_resultado('Quantidade de usuários distintos (source)', len(df['source'].value_counts()))
    adicionar_resultado('Contagem de source', df['source'].value_counts())
    adicionar_resultado('Percentual de source', df['source'].value_counts(normalize=True) * 100)
    
    adicionar_resultado('Entries where source = "seofernandes"', df.loc[df['source'] == 'seofernandes'])
    
    adicionar_resultado('Username analysis - Contagem', len(df['username'].value_counts()))
    adicionar_resultado('Username analysis - Frequência', df['username'].value_counts())
    adicionar_resultado('Username analysis - Percentual', df['username'].value_counts(normalize=True) * 100)
    
    adicionar_resultado('Entries where username = "seofernandes"', df.loc[df['username'] == 'seofernandes'])
    
    adicionar_resultado('Seguidores (followers) - Média', df['seguidores'].mean())
    adicionar_resultado('Seguindo (following) - Média', df['seguindo'].mean())
    adicionar_resultado('Posts - Média', df['posts'].mean())
    
    adicionar_resultado('Privado - Contagem', df['privado'].value_counts())
    adicionar_resultado('Privado - Percentual', df['privado'].value_counts(normalize=True) * 100)
    
    adicionar_resultado('Profissional - Contagem', df['profissional'].value_counts())
    adicionar_resultado('Profissional - Percentual', df['profissional'].value_counts(normalize=True) * 100)
    
    adicionar_resultado('Verificado - Contagem', df['verificado'].value_counts())
    adicionar_resultado('Verificado - Percentual', df['verificado'].value_counts(normalize=True) * 100)
    
    adicionar_resultado('Celular - Contagem', df['celular'].value_counts())
    adicionar_resultado('Celular - Percentual', df['celular'].value_counts(normalize=True) * 100)
    
    adicionar_resultado('Email - Contagem', df['email'].value_counts())
    adicionar_resultado('Email - Percentual', df['email'].value_counts(normalize=True) * 100)
    
    adicionar_resultado('Cidade - Contagem', df['cidade'].value_counts())
    adicionar_resultado('Cidade - Percentual', df['cidade'].value_counts(normalize=True) * 100)
    
    adicionar_resultado('Linguagem - Contagem', df['linguagem'].value_counts())
    adicionar_resultado('Linguagem - Percentual', df['linguagem'].value_counts(normalize=True) * 100)
    
    adicionar_resultado('Taxa de engajamento - Likes - Média', df['txengajamento_likes'].mean())
    adicionar_resultado('Taxa de engajamento - Comentários - Média', df['txengajamento_comentarios'].mean())

    # Juntar todos os resultados
    texto_final = '\n'.join(map(str, resultados))
    
    # Exibir no console
    print(texto_final)
    
    # Juntar todos os resultados
    texto_final = '\n'.join(map(str, resultados))

    # Exibir no console (opcional)
    print(texto_final)

    # Se quiser salvar
    if salvar_em_txt:
        with open(caminho_saida_txt, 'w', encoding='utf-8') as f:
            f.write(texto_final)
        print(f'\nResultados salvos em: {os.path.abspath(caminho_saida_txt)}')

    return texto_final  # <--- Adicionado
