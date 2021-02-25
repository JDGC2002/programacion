#---------CONSTANTES-----#
PREGUNTA_A = "¿Cuál es el número A?: "
PREGUNTA_B = "¿Cuál es el número B?: "
MENSAJE_A_MAYOR = "El número A es mayor al número B"
MENSAJE_B_MAYOR = "El número B es mayor al número A"
MENSAJE_IGUALES = "Los números son iguales"

#---------ENTRADA AL CÓDIGO-----#
NumeroA = int(input(PREGUNTA_A))
NumeroB = int(input(PREGUNTA_B))
AreIguales = NumeroA == NumeroB
isMayorA = NumeroA > NumeroB
isMayorB = NumeroB > NumeroA
resultado = ""

if (AreIguales):
    resultado = MENSAJE_IGUALES
elif (isMayorA):
    resultado = MENSAJE_A_MAYOR
else:
    resultado = MENSAJE_B_MAYOR

print (resultado)


