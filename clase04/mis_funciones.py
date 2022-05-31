def ejercicio1():
    calculo = 6 / 2 * (1 + 2)
    print(calculo)

def ejercicio2(producto_gramos, precio_producto, peso_gramos = 1000):
     precio_conversion = precio_producto * peso_gramos / producto_gramos
     return precio_conversion

precio_otra_presentacion(producto_gramos: int, precio_producto: float, peso_gramos: int):
    """"Retorna la conversion del precio de un producto en dierentes presentaciones
    """
    precio_conversion = precio_producto * peso_gramos / producto_gramos

  import math as m
