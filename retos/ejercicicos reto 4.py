

factura = ventas[0]
salida = "la factura 1201 tiene un total en pesos de 962,529.33"

def imprimir_factura(datos: list):
    from functools import reduce
    numero = datos.pop(0)
    lineas = list(map(lambda x[1]*x[2], datos))
    total = reduce(lambda x, y: x + y, lineas)
    return numero, total
   
    renglones = list(map(imprimir_factura, rutinacontable))
    renglones = list(map(lambda x: (x[0], x[1] if x[1] > 600000 else x[1] + 25000), renglones))

    print('----------------- Inicio Registro diario --------------------------')
    for numero, total in renglones:
        print(f"la factura {numero} tiene un total en pesos de {total:,.2f}")
    print('----------------- Fin Registro diario --------------------------')

    
ventas = [
[1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],
 [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
 [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
 [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]    
]

   

    
if total < 600000:
        total += 25000
    return f"la factura {numero} tiene un total en pesos de {total:,.2f}"