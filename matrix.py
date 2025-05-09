import numpy as np
import math
import pandas as pd
from google.colab import files
from google.colab import drive

# Conecto ao Google Drive pra pegar os arquivos, como se fosse abrir uma gaveta onde guardo meus livros.
drive.mount('/content/drive')

# Digo onde estão os dois arquivos de texto que vou usar, que estão na minha gaveta (Google Drive).
base_text_1 = "/content/drive/MyDrive/Colab/Ciencia_Dados/Problema 01/Base Text - Matrix Representation I.txt"
base_text_2 = "/content/drive/MyDrive/Colab/Ciencia_Dados/Problema 01/Base Text - Matrix Representation II.txt"

# Abro o primeiro arquivo e leio tudo que está dentro, como se fosse ler um livro.
file1 = open(base_text_1, "r")
# Abro o segundo arquivo e leio tudo que está dentro dele também.
file2 = open(base_text_2, "r")

# Pego todo o texto dos dois arquivos e guardo como uma grande história.
file_content1 = file1.read()
file_content2 = file2.read()
texto = file_content1 + file_content2

# Limpo o texto, tirando tudo que não é letra ou espaço (como pontos e números), como se eu estivesse apagando desenhos e deixando só as palavras.
pontuacoes = '!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~“”’‘—–\n'
texto_limpo = ''
for c in texto:
    if c not in pontuacoes:
        texto_limpo += c

# Crio uma lista com todas as letras únicas que sobraram, em ordem alfabética, como se fosse uma lista de personagens diferentes.
caracteres_unicos = sorted(set(texto_limpo))

# Transformo cada letra em um número usando a posição dela na lista (ex.: 'A' pode ser 0, 'B' pode ser 1).
# Isso é como dar um número secreto pra cada personagem.
tabela_inversa = caracteres_unicos  # O número vira de volta a letra usando essa lista.

# Transformo o texto limpo em uma lista de números, cada um representando uma letra.
matriz = []
for c in texto_limpo:
    numero = caracteres_unicos.index(c)
    matriz.append(numero)

# Calculo o tamanho de uma tabela quadrada pra guardar todos os números.
# Se eu tenho 10 números, a tabela pode ser 4x4 (16 espaços), porque 4 é o número mais próximo que faz um quadrado.
lado = math.ceil(math.sqrt(len(matriz)))
total = lado * lado
# Preencho os espaços vazios da tabela com zeros, como se fossem quadradinhos em branco.
matriz += [0] * (total - len(matriz))

# Transformo a lista de números numa tabela quadrada usando uma ferramenta mágica (numpy).
matriz_np = np.array(matriz).reshape((lado, lado))

# Reconstruo o texto original a partir da tabela, ignorando os zeros que coloquei pra preencher.
texto_reconstruido = ''
for n in matriz:
    if n < len(tabela_inversa):
        texto_reconstruido += tabela_inversa[n]

# Mostro a tabela com as primeiras 15 linhas na tela, pra gente ver como ficou.
print("Matriz (quadrada com padding):")
print()
print(matriz_np[:15, :])

# Mostro os primeiros 199 caracteres do texto que reconstruí, pra ver se deu certo.
print("\nTexto reconstruído:", texto_reconstruido[:199], "...")

# Mostro uma tabela que mostra quais números correspondem a quais letras, mas só as primeiras 11.
print("\nTabela (caractere -> índice):")
for i, c in enumerate(tabela_inversa):
    print(f"{c!r} -> {i}")
    if i > 11:
        break
print("...")

# Transformo a tabela de números numa planilha que posso salvar.
df = pd.DataFrame(matriz_np)

# Salvo a planilha num arquivo chamado "matriz_texto.xlsx".
df.to_excel("matriz_texto.xlsx", index=False, header=False)

# Faço o arquivo ser baixado automaticamente pro meu computador.
files.download("matriz_texto.xlsx")

# Digo que tudo deu certo e que o arquivo está sendo baixado.
print("\nMatriz salva e baixada! Verifique seu drive ou seus downloads.")
