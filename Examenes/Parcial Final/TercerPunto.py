RepCiclos = 1

while (RepCiclos == 1):
    try:
        nombre = str(input('Ingresa tu nombre: '))
        assert (nombre.isalpha())
        RepCiclos = 2
    except AssertionError:
        print ('Has ingresado un dato no válido. Recuerda que no se admiten números en tu nombre')

while (RepCiclos == 2):
    try:
        dineroDolares = int(input('Ingresa tu dinero en dolares: '))
        RepCiclos = 3
    except ValueError:
        print ('ingresaste un dato no válido')

print (f'Nombre: {nombre}. Dinero en dolares: {dineroDolares}') 

dineroEuros = round(dineroDolares*0.82, 3)

print (f'Nombre: {nombre}. ahora tu dinero ha sido convertido de dolares a euros: {dineroEuros}')

