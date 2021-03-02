#---CONSTANTES----#
MENSAJE_BIENVENIDA = "oe, le voy a colaborar pa que ahorre"
PREGUNTA_AHORRO = "¿Cuánto tiene ahorrado?: "
PREGUNTA_CPU = "¿Cuánto vale el pc que tienes presupuestado?: "
MENSAJE_AHORRADO = "LLEVAS AHORRADO: "

#----Entrada al código---#
print(MENSAJE_BIENVENIDA)
valor = float(input(PREGUNTA_CPU))
ahorro = float(input(PREGUNTA_AHORRO))

while (valor > ahorro):
    print (MENSAJE_AHORRADO, ahorro, "Te faltan:", valor - ahorro)
    ahorro = ahorro + 1000

