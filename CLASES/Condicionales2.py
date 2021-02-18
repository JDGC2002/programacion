#------CONSTANTES-----#
MENSAJE_BIENVENIDA = "Bienvenido al prostibulo, necesitaremos confirmar tu edad"
MENSAJE_MAYOR_EDAD = "Confirmado señor, que lo disfrute"
MENSAJE_MENOR_EDAD = "Largo de aquí"
PREGUNTA_EDAD = "¿Qué edad tienes?: "

#------ENTRADA AL CÓDIGO-------#
print (MENSAJE_BIENVENIDA)
edad = int(input(PREGUNTA_EDAD))
isMayorEdad = edad >= 18
resultado = ""
if (isMayorEdad):
    resultado = MENSAJE_MAYOR_EDAD
else:
    resultado = MENSAJE_MENOR_EDAD

print (resultado)