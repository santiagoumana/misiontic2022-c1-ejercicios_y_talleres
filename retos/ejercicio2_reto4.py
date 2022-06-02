def ordenes(rutinacontable):
    from functools import reduce
    facturas = list(map(lambda l: l.pop(0), rutinacontable))
    totales = list(map(lambda x: reduce(lambda v, w: v + w, map(lambda y: y[1]*y[2], x)), rutinacontable))
    totales = list(map(lambda x: x if x > 600000 else x, totales))
    renglones = list(zip(facturas, totales))

    print('----------------- Inicio Registro diario --------------------------')
    for numero, total in renglones:
        print(f"la factura {numero} tiene un total en pesos de {total:,.2f}")
    print('----------------- Fin Registro diario --------------------------')
     

ventas = [
    [6589, ("9874", 1, 125698.20), ("88112", 2, 135645.20), ("3218", 4, 13645.20)],
    [6590, ("5236", 8, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)],
    [6591, ("7812", 2, 11.99), ("9652",11,18.99)],
]
ordenes(ventas)
