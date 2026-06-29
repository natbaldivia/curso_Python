# Solicite ao usuário o nome de uma fruta e exiba o preço correspondente
# %%
frutas = {"maçã": 1.50,
          "banana": 2.75,
          "uva": 1.90,
          "pera":1.25,
          "laranja":0.65,
          "limão": 1.25,
          "goiaba": 2.15,
          "abacaxi": 3.20,
          "jaca": 5.80}

opcao = input("Escolha sua fruta: ")
if opcao in frutas:
    print(frutas[opcao])
else:
    print("Escolha uma fruta do nosso menu")