# %%
print("Olá todo mundo!")

# %%
valor = input("Entre com um valor: ")
print(valor)

# %%
# quando eu re-declaro essa função ela é sobre-escrits
def f(x):
    resultado = 1 + x
    return resultado
# %%
f(10)