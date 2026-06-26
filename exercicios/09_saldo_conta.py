# %%
saldo_total = 0

while True:
    saldo = input("Insira seu saldo: ")
    if saldo == 0:
        break # esse break só pode existir dentro de laços de repetição, e ele sai do primeiro que ele se encontra
    saldo_total += float(saldo)

print("Seu saldo total é de: ",saldo_total)