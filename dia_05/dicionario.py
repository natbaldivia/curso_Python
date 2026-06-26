# %%
dados_nat = {"Nome": "Natalia Baldivia Gomes",
             "idade":34,
             "filhos":False,
             "cargos":[
                 {"função":"Engenheira de dados","empresa":"Arbit"},
                 {"função":"Analista de performance","empresa":"Inmetrics"}
             ]}
print(dados_nat["cargos"][-1]["empresa"])

dados_nat["estado civil"] = "Solteira" # adicionando dado novo na lista

print(dados_nat)

print("Chaves: ",dados_nat.keys())
print("Valores: ",dados_nat.values())
print("Items: ",dados_nat.items()) # o .items vai trazer uma lista de tuplas onde cada tupla tem chave e valor

for i in dados_nat:
    print(i,"-->",dados_nat[i])

for item in dados_nat.items():
    print(item)

for chave,valor in dados_nat.items():
    print(chave," : ",valor)