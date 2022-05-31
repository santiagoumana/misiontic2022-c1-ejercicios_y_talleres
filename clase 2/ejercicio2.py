peso_producto_en_gramos= 100
precio_producto = 5.95
peso_kilo_en_gramos = 1000

precio_por_gramo = precio_producto / peso_producto_en_gramos
precio_por_kilo = precio_por_gramo * peso_kilo_en_gramos
precio_por_kilo = round(precio_por_kilo, 2)

print(round(precio_por_kilo, 2))
