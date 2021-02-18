#---------CONSTANTES------------#
MENSAJE_BIENVENIDA = "Hola, espero que estés bien"
MENSAJE_MAYOR = "El número A es mayor que el B"
MENSAJE_MENOR = "El número B es mayor que el A"
MENSAJE_IGUAL = "Los números son iguales"
PREGUNTA_NUMA = "Ingrese el número A: "
PREGUNTA_NUMB = "Ingrese el número B: "


#---------ENTRADA AL CÓDIGO----------#
print (MENSAJE_BIENVENIDA)
NumeroA = int(input(PREGUNTA_NUMA))
NumeroB = int(input(PREGUNTA_NUMB))
isMayor = NumeroA > NumeroB
isMenor = NumeroA < NumeroB
resultado = ""

if (isMayor):
    resultado = MENSAJE_MAYOR
elif (isMenor):
    resultado = MENSAJE_MENOR
else:
    resultado = MENSAJE_IGUAL

print (resultado)


