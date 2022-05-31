menu = """"
| Carácter | Mensaje a imprimir |
|----------|--------------------|
|   'a'    | Android            |
|   'i'    | IOS                |
|   otro   | Opcion inválida    |

elige una opcion: """

opcion = input(menu)

def seleccion_so (opcion):

    if opcion == 'a' or opcion == 'A':
        return ' Android '
    elif opcion == 'i' or opcion == 'I':
        return' IOS '
    else:
        return'opcion invalida'


print(seleccion_so(opcion))           