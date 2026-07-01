# Construa um programa que realiza o sorteio de um numero entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute é maior ou menor que o numero sorteado.
# Caso o usuário acerte, dê os parabéns.

# %%
numero_sorteio = 7

for i in range(3):
    while True:
        try:
            numero_usuario = int(input("Qual numero você escolhe?"))

        except ValueError as err:
            print("Valor inválido! O valor deve ser um número.")
            continue

        if 1 <= numero_usuario <= 15:
            break
        print("Valor inválido. O numero deve ser entre 1 e 15.")

    if numero_sorteio == numero_usuario:
        print("Parabéns!")
        break
    elif numero_usuario > numero_sorteio:
        print("Muito alto, tente um numero menor.")
    else:
        print("Muito baixo, tente um numero maior.")
    
else:
    print("Você só tinha ",i+1,"tentativas. Sinto muito.")