def mcd(x, y):
    # Validar
    if y < 0:
        return "No puede buscar divisores si hay números negativos"
    # Algoritmo
    if y == 0:
        return x
    if x >= y:
        return mcd(y, x % y) 
    else:
        return mcd(y, x)

print(mcd(240, 12500))
