# %%
idades = [28, 42, 43, 35, 39, 28, 38]
mix = ["natalia", 1, 1.5, "nome", idades]

print(mix[1])

# %%
print("Soma das idades: ",sum(idades))
print("quantidade de idades: ",len(idades))
print("média de idades:",sum(idades)/len(idades))
print("menor idade: ",min(idades))
print("maior idade: ",max(idades))

# %%
nat = ["Natalia Baldivia",34, True,"Solteira", ["café", "parque", "lamen", "hamburgueria", "cinema"],[2000,3500,5000,4000,10000,12000,13000]]
print("Tamanho da lista da nat: ",len(nat))
print("Ultimo rolê: ",nat[-1][-1]) # -1 é a última posição
print("primeiros 3 dados: ",nat[0:3])
print("últimos 2 rolês: ",nat[4][-2:])
roles = nat[4]
salarios = nat[5]
print("rolês: ",roles)
print("Salários: ",salarios)
print("salarios por ordem decrescente: ",salarios[::-1]) # [ start : stop : step ] 
