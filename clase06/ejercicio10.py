#10
from ejercicios_clase6 import factura_acueducto #biblioteca
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
    return valor_factura # biblioteca
#prueba
tarifas = {
        1: { "cargo_fijo": 2500, "metro_cubico": 2200, "basuras": 5500},                          
        2: { "cargo_fijo": 2800, "metro_cubico": 2350, "basuras": 6200},                   
        3: { "cargo_fijo": 3000, "metro_cubico": 2600, "basuras": 7400},                                    
        4: { "cargo_fijo": 3300, "metro_cubico": 3400, "basuras": 8600},    
        5: { "cargo_fijo": 3700, "metro_cubico": 3900, "basuras": 9700},
        6: { "cargo_fijo": 4400, "metro_cubico": 4800, "basuras": 11000}
}
print(factura_acueducto(2, 23.0, tarifas))
#print(2800 +  23.0 * 2350 + 6200)