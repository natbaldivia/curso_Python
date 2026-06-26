# %%
idades = []

while True:
    idade = input("Entre com a idade: ")
    if idade =="":
        break
    idades.append(int(idade))

print(idades)
media = sum(idades) / len(idades)
print("A média das idades é: ",media)

