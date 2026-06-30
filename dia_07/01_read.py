# %%
nome_arquivo = "historia.txt"

# abre o arquivo em formato de leitura
open_file = open(nome_arquivo)

# lê os dados do arquivo
conteudo = open_file.read()

print(conteudo)

# fecha o arquivo
open_file.close()

# %%
# para não ter q abrir e fechar o arquivo, o mais usual é o seguinte:
nome_arquivo = "historia.txt"

with open(nome_arquivo) as open_file:
    conteudo = open_file.read()

