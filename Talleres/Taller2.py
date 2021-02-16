#------CONSTANTES-----#
MENSAJE_BIENVENIDA = "Hola, a continuación haremos una comparación y una serie de operaciones con 2 números que desees"
DEFINE_NUMEROA = "Ingresa el número A: "
DEFINE_NUMEROB = "Ingresa el número B: "
MENSAJE_DESPEDIDA = "El proceso ha finalizado"

#-----Entrada al código-----#
print (MENSAJE_BIENVENIDA)
NumeroA = int (input (DEFINE_NUMEROA))
NumeroB = int (input (DEFINE_NUMEROB))
areIguales = NumeroA == NumeroB
isMayor = NumeroA > NumeroB
SumaNumeros = NumeroA + NumeroB
RestaNumerosAB = NumeroA - NumeroB
RestaNumerosBA = NumeroB - NumeroA
MultiplicacionNumeros = NumeroA * NumeroB
DivisionNumerosAB = NumeroA / NumeroB
DivisionNumerosBA = NumeroB / NumeroA
print ("¿los números son iguales?", areIguales)
print ("La suma de los numeros es igual a", SumaNumeros)
print ("La resta de números A - B es igual a", RestaNumerosAB, ". La resta de números B - A es igual a ", RestaNumerosBA)
print ("La multiplicación de los numeros es igual a", MultiplicacionNumeros)
print ("La división A/B es igual a", DivisionNumerosAB, ". La división B/A es igual a", DivisionNumerosBA)
print (MENSAJE_DESPEDIDA)