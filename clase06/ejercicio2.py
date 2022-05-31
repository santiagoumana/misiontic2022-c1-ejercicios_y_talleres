from ejercicios_clase6 import nota_definitiva_2

def nota_definitiva_2(nota: float) -> str:  #biblioteca
    # validación de parametros
    if not isinstance(nota, float) and not isinstance(nota, float):
        return "la nota debe ser con numero decimal"

    # not (nota >= 0.0 and nota <= 5.0)
    if nota < 0.0 or nota > 5.0: # - (p and q) --> -p or
        return "la nota ingresada no es valida"

    # proceso
    if nota >= 3.0:
        mensaje = "gano la materia. ¡felicitaciones!"
    else:
        mensaje = "perdio la materia"

    #salida
    return f"su nota es: {nota} {mensaje}" #biblioteca

# prueba del algoritmo
#nota = float(input("ingrese la nota de 0.0 a 5.0: "))
nota = 5
print(nota_definitiva_2(nota))