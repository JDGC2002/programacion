#datos
PruebaV = True
PruebaF = False     
print ("-"*10,"Datos", "-"*10)
edad = 18
estatura = 1.75
peso = 90
NOMBRE = "Jhon Diego Gómez Cifuentes"
#Linea para mostra en pantalla los datos
print ("Nombre:", NOMBRE)
print ("Edad:", edad, ",", "Estatura:", estatura, ",", "Peso", peso)
# Linea para la edad
print ("-"*10,"¿Mayor de edad?", "-"*10)
isMayorEdad = edad >= 18
print (isMayorEdad)
# Linea para la estatura
print ("-"*10,"¿Menor a la estatura promedio mundial?", "-"*10)
isMayorEstatura = estatura < 1.70
print (isMayorEstatura)
# linea para el peso
print ("-"*10,"¿Peso diferente a 90?", "-"*10)
isPesoDiferente = peso != 90
print (isPesoDiferente)
# Linea sobre el apellido
print ("-"*10,"¿Está el apellido", "Cifuentes", "en el nombre?", "-"*10)
apellido = "Cifuentes"
isApellido = apellido in NOMBRE
print (isApellido)