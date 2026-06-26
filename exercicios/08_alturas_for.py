# %%
soma = 0 # valor final
qtd_entradas = 4 # contador de entradas

for i in range(qtd_entradas): # se a gente não determinar o valor inicial do range, ele começa com 0, vai ser a mesma coisa que (0,4)
    altura = input("Informe sua altura: ")
    altura = float(altura)
    soma += altura

print("Soma das alturas: ",soma)