def cargo_fijo(estrato: float):
    if estrato == 1:
        return 2500
    if estrato == 2:
        return 2800
    if estrato == 3:
        return 3000
    if estrato == 4:
        return 3300  
    if estrato == 5:
        return 3700   
    if estrato == 6:
        return 4400  

def consumo_m3(estrato:float):
    if estrato == 1:
        return 2200
    if estrato == 2:
        return 2350
    if estrato == 3:
        return 2600
    if estrato == 4:
        return 3400  
    if estrato == 5:
        return 3900   
    if estrato == 6:
        return 4800 

def basura_alcantarillado(estrato:float):
    if estrato == 1:
        return 5500
    if estrato == 2:
        return 6200
    if estrato == 3:
        return 7400
    if estrato == 4:
        return 8600
    if estrato == 5:
        return 9700 
    if estrato == 6:
        return 11000


def cobro(estrato:int, consumo_de_agua_en_el_periodo: float):
    if estrato >= 1 and estrato <= 6:
        cobro_factura = cargo_fijo(estrato) + (consumo_de_agua_en_el_periodo * consumo_m3 (estrato)) + basura_alcantarillado(estrato)
        return  cobro_factura 
    else: 
        return "ingrese un estrato valido"


estrato = int(input("estrato"))
consumo_agua = float(input("consumo de agua"))   
print(cobro(estrato, consumo_agua))