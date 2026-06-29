# Escreva um programa que receba uma lsita de numeros do usuário e conte quantas vezes um numero especifico
# aparece na lista. Solicite ao usuário um número e exiba a contagem
# %%
lista = [1,2,3,4,5,3,5,8,9,5,4,7,5,1,2,5,4,8,9,4,1,2,5,1,5,1,2,3]
numero = input("entre com um numero: ")
numero = int(numero)

contador = 0
for i in lista: 
    if i == numero:
        contador += 1

print("Quantidade de vezes que o numero",numero, "apareceu na lista:" ,contador)

