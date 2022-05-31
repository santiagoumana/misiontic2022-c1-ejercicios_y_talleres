def CDT (usuario:str, capital:int, tiempo:int):
    if tiempo < 2:
        perdida = capital * 0.02
        valor_total = capital - perdida
    else :
      intereses = (capital * 0.03 * tiempo) / 12
      valor_total = intereses + capital
      return (f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}")

print (CDT("AB1012", 1000000, 3))
print (CDT("ER3366", 650000, 2))
