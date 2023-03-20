def ciclos(nume, numero):
    if numero == nume:
        return nume
    else:
        nume += 1
        return ciclos(nume, numero)


hola = ciclos(0, 7)


print(hola)
