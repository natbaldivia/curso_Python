# %%
soma = 0 # valor final
qtd_entradas = 4 # contador de entradas

while qtd_entradas > 0:
    altura = input("Informe sua altura: ")
    altura = float(altura)
    soma += altura
    qtd_entradas -= 1

print("Soma das alturas: ",soma)