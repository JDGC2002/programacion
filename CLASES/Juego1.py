#----CONSTANTES---#
MENSAJE_BIENVENIDA ='''¡JUGUEMOS!!!
    ADIVINA EL NÚMERO DEL 1 AL 10'''

PREGUNTA_NUMERO = "¿Cuál es el número????: "
PREGUNTA_FALLIDA_UNO = "Nop, ese no es, pon otro: "
PREGUNTA_FALLIDA_DOS = "tampoco es, de nuevo:  "
PREGUNTA_FALLIDA_TRES = "Nea real? otro intento:  "
PREGUNTA_FALLIDA_CUATRO = "ùltimo intento: "
MENSAJE_GANASTE = 'Felicidades, acertaste.'
MENSAJE_PERDISTE = 'Has perdido :C'

#----entrada al código----#
NumeroGanador = 8
vidas = 5
isGanadorNormal = vidas 
print(MENSAJE_BIENVENIDA)
NumeroIngresado = int(input(PREGUNTA_NUMERO))
if (NumeroIngresado != NumeroGanador):
    vidas = vidas - 1
while (NumeroGanador != NumeroIngresado and vidas > 0):
    if (vidas == 4):
        NumeroIngresado = int(input(PREGUNTA_FALLIDA_UNO))
    elif (vidas == 3):
        NumeroIngresado = int(input(PREGUNTA_FALLIDA_DOS))
    elif (vidas == 2):
        NumeroIngresado = int(input(PREGUNTA_FALLIDA_TRES))
    else:
        NumeroIngresado = int(input(PREGUNTA_FALLIDA_CUATRO))
    if (NumeroIngresado != NumeroGanador):
        vidas = vidas - 1
        print ('te quedan', vidas, 'vidas')

if (vidas > 1 and NumeroGanador == NumeroIngresado):
    print (MENSAJE_GANASTE, "terminaste con", vidas, "vidas")
elif (vidas == 1):
    print ("UFFF, en la última ganaste c:")
else: 
    print (MENSAJE_PERDISTE)




