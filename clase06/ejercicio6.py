 #Diseñe un algoritmo que determine si un número real (x) se encuentra dentro de uno de los siguientes rangos: (3.5, 7.8], [9.3, 4.5) y [23.4, 45.3].

numero = float(input("ingrese el numero: "))

def rango(numero: float):


    mensaje = ""
    error_dato = True
    if numero > 3.5 and numero <= 7.8:
        error_dato = False
        mensaje += f"el numero {numero} esta dentro del rango (3.5, 7.8]\n"

    if numero > 4.5 and numero <= 9.3:
        mensaje += f"el numero {numero} esta en el rango [9.3, 4.5)\n"   
        error_dato = False

    if   numero >= 23.4 and numero < 45.3:
        mensaje += f"el numero {numero} esta en el rango [23.4, 45.3]\n"
        error_dato = False    

    if  error_dato:
        mensaje += f"el numero {numero} no esta en ningun rango\n"
    
    return mensaje

print(rango(numero))