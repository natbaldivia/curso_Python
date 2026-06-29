
# %%
def juros_compostos(aporte:int, taxa:float, prazo:int)->float:

    return aporte * (1 + taxa) ** prazo

# %%
print(juros_compostos(1000,0.13,4)) # se você ocultar o nome do argumento, cuidado para não mudar a ordem
print(juros_compostos(aporte=1000,taxa=0.13,prazo=4)) # dessa forma, nomeando o argumento, não importa a ordem

# ao implementar uma função, é interessante documentá-la na doc-string
# %%
juros_compostos.__doc__ = """juros_compostos serve para calcular o retorno financeiro a partir de um aporte.
Deve-se considerar o valor aportado, a taxa de juros atual e o prazo (em anos)
para cálculo do valor a ser retornado.
aporte: um numero inteiro que represente o valor em reais
taxa: um numero float que represente o valor da taxa
prazo: um numero inteiro >= 1 que represents o tempo que o investimento terá liquidez"""


# %%
print(juros_compostos.__doc__)

# %%
print(help(juros_compostos))