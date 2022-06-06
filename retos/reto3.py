def AutoPartes(ventas: list):
    return dict(zip(range(len(ventas)), ventas))

def consultaRegistro(ventas, idproducto):
    bandera = False
    for item in ventas.values():
        if item[0] == idproducto:
            print(f"Producto consultado : {item[0]}  Descripción  {item[1]}  #Parte  {item[2]}  Cantidad vendida  {item[3]}  Stock  {item[4]}  Comprador {item[5]}  Documento  {item[6]}  Fecha Venta  {item[7]}")
            bandera = True
    if bandera == False:
        print("No hay registro de venta de ese producto")