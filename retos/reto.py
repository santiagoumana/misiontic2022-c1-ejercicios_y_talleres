

def CDT (usuario:str, capital:int, tiempo:int):
    intereses = (capital * 0.03 * tiempo) / 12
    perdida = capital * 0.02
    if tiempo > 2:
        valor_total = intereses + capital
    else:
        valor_total = capital - perdida
    return (f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}")

print (CDT("AB1012", 1000000, 3))
print (CDT("ER3366", 650000, 2))

def CDT(usuario: str, capital: int, tiempo: int):
    intereses = (capital * 0.03 + tiempo) / 12
    valor_intereses = int(intereses)
    perdida = capital * 0.02
    valor_a_perder = int(perdida)
    if tiempo > 2:
        valor_total = valor_intereses + capital
    else:
        valor_total = capital - valor_a_perder
    return (f"Para el usuario {usuario} La cantidad de dinero a recibir, segun el monto incial {capital} para un tiempo de {tiempo} meses es: {valor_total}")

print (CDT("AB1012", 1000000, 3))
print (CDT("ER3366", 650000, 2))
