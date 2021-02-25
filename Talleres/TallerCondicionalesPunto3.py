#-------CONSTANTES-------#
MENSAJE_BIENVENIDA = "Hola, a continuación solicitaremos el año actual y un año que usted desee, calcularemos cuantos años faltan o cuantos han pasado"
MENSAJE_AÑOS_FALTAN = "Los años que faltan para llegar al año son"
MENSAJE_AÑOS_PASADOS = "Los años que han pasado son"
PREGUNTA_AÑO_ACTUAL = "¿Cuál es el año actual?: "
PREGUNTA_AÑO_DESEADO = "¿Cuál es el año al que deseas saber cuanto faltan o han pasado?: "

#----Entrada al código----#
print (MENSAJE_BIENVENIDA)
AñoActual = int(input(PREGUNTA_AÑO_ACTUAL))
AñoDeseado = int(input(PREGUNTA_AÑO_DESEADO))
AñosQueFaltan = AñoDeseado - AñoActual
AñosQueHanPasado = AñoActual - AñoDeseado
isFaltan = AñoDeseado > AñoActual
isPasado = AñoActual > AñoDeseado
resultadoNumerico = 0
resultadoMensaje = ""

if (isFaltan):
    resultadoMensaje = MENSAJE_AÑOS_FALTAN
else:
    resultadoMensaje = MENSAJE_AÑOS_PASADOS

if (isFaltan):
    resultadoNumerico = AñosQueFaltan
else:
    resultadoNumerico = AñosQueHanPasado

print (resultadoMensaje, resultadoNumerico)
