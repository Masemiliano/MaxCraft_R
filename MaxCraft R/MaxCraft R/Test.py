hej = "hej"

ny = bytes(hej, "utf-8")

lista = []

for var in ny:
    lista.append(bin(var))
    
print(lista)
