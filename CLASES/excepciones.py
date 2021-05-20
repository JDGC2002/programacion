isCorrectoInfo = False

while (isCorrectoInfo == False):
    try:
        edad = int(input('¿Cuál es tu edad?: '))
        isCorrectoInfo = True
    except ValueError:
        print ('ingresaste un dato no válido')

nombreArchivo = str(input("Ingrese el nombre del archivo que desea encontrar: "))
try:
    archivo = open(nombreArchivo)
except FileNotFoundError:
    print (f'El archivo {nombreArchivo} no se ha encontrado')

isCorrectoInfo = False 

while (isCorrectoInfo == False):
    try:
        nombre = str(input('Ingresa tu nombre: '))
        assert (nombre.isalpha())
        isCorrectoInfo = True
    except AssertionError:
        print ('Has ingresado un dato inválido')

