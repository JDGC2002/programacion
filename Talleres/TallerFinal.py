from os import fsdecode
import sys

# PUNTO 1

RepCiclos = 1

while (RepCiclos == 1):
    try:
        nombre = str(input('Ingresa tu nombre: '))
        assert (nombre.isalpha())
        RepCiclos = 2
    except AssertionError:
        print ('Ingresaste incorrectamente el nombre')


while (RepCiclos == 2):
    try:
        peso = int(input('¿Cuál es tu peso?: '))
        estatura = float(input('¿Cuál es tu estatura?: '))
        RepCiclos = 3
    except ValueError:
        print ('Ingresaste un dato inválido')

IMC = peso/(estatura**2)
print (f'Tu IMC es {IMC}.')

#PUNTO 2

RepCiclos = 1

while (RepCiclos == 1):
    try:
        parrafo = str(input('Ingresa tu parrafo: '))
        assert (parrafo.endswith('.'))
        RepCiclos = 2
    except AssertionError:
        print ('Recuerda que el parrafo debe terminar en "."')

palabras = parrafo.split(' ')
print(f'en el parrafo la palabra más grande es {max(palabras, key=len)}, y la más pequeña es {min(palabras, key=len)}')

#PUNTO 3

nombreArchivo = 'mantenimientos.txt'
try:
    archivo = open(nombreArchivo)
except FileNotFoundError:
    archivo = open(nombreArchivo, 'w', encoding='UTF-8')
    descripcion = 'Archivo para manejo el mantenimiento de equipos biomédicos.'
    archivo.writelines(descripcion)
    sys.exit(1)

nombrePaciente = str(input('Ingrese el nombre del equipo biomédico: '))
descEnfermedad = str(input('Ingrese una descripción del equipo: '))
precioConsulta = float(input('Ingrese el precio para el mantenimiento: '))

archivo = open(nombreArchivo, 'a')
linea = '\nnombre del equipo:' + str(nombrePaciente) + ', Descripción del equipo:' + str(descEnfermedad) + ', Precio del mantenimiento:' + str(precioConsulta)  
archivo.writelines(linea)
archivo.close