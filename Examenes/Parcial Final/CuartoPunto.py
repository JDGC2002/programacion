from os import fsdecode
import sys

nombreArchivo = 'pacientes.txt'
try:
    archivo = open(nombreArchivo)
except FileNotFoundError:
    archivo = open(nombreArchivo, 'w', encoding='UTF-8')
    descripcion = 'Archivo para manejo de clientes.'
    archivo.writelines(descripcion)
    sys.exit(1)

nombrePaciente = str(input('Ingrese el nombre del paciente: '))
descEnfermedad = str(input('Ingrese una descripción de la enfermedad del paciente: '))
precioConsulta = float(input('Ingrese el precio de la consulta del paciente: '))

archivo = open(nombreArchivo, 'a')
linea = '\nnombre:' + str(nombrePaciente) + ', descripción de la enfermedad:' + str(descEnfermedad) + ', Precio de la Consulta:' + str(precioConsulta)  
archivo.writelines(linea)
archivo.close