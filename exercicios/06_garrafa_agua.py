# %%
texto = """
Escolha sua água para comprar:
(1)água mineral natural
(2)água mineral com gás"""

opcao = input(texto)

conta = 0
if opcao == "1":
    conta = 1.50
elif opcao == "2":
    conta = 2.50
if conta == 0:
    print("Escolha 1 ou 2")
else:
    print("Pague o valor de R$",conta)
