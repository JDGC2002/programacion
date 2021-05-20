from os import fsdecode
import sys

nombreArchivo = 'estudiantes.txt'
try:
    archivo = open(nombreArchivo)
except FileNotFoundError:
    archivo = open(nombreArchivo, 'w', encoding='UTF-8')
    descripcion = 'Archivo de datos de estudiantes'
    archivo.writelines(descripcion)
    sys.exit(1)

nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))
estatura = float(input('Ingrese su estatura: '))

archivo = open(nombreArchivo, 'a')
linea = '\nnombre:' + nombre + ' edad:' + str(edad) + ' estatura:' + str(estatura)  
archivo.writelines(linea)
archivo.close

#Leer
with open (nombreArchivo) as reader:
    for line in reader:
        print (line)