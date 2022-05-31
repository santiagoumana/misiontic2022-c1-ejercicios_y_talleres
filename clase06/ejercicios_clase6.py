def nota_definitiva_2(nota: float) -> str:
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
    return f"su nota es: {nota} {mensaje}"
    

def factura_acueducto(estrato: int, consumo: float, tarifas: dict):
    #validacion
    if estrato < 1 or estrato > 6:
        return "El estrato debe estar entre 1 y 6"
    if consumo < 0:
        return "el consumo debe ser 0 o superior"
   
   #proceso   
    valor_factura = tarifas[estrato]["cargo_fijo"]
    valor_factura += consumo * tarifas[estrato]["metro_cubico"]
    valor_factura += tarifas[estrato]["basuras"]
  
   # salida
    return valor_factura