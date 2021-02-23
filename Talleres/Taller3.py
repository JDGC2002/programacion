#-----------CONSTANTES-----#
MENSAJE_BIENVENIDA = "Oe"
PREGUNTA_DESEO = "¿Va a comprar bareta? "
MENSAJE_NEGACION = "¿No? Entonces ábrase marica"
MENSAJE_SI = "Hágale pues, pille."
MENSAJE_DESPEDIDA_BUENA = "Cuando quiere vuelve pai"

#---------ENTRADA AL CÓDIGO-------#
print (MENSAJE_BIENVENIDA)
print ("escriba SI, si desea comprar el producto, de lo contrario escriba NO")
respuesta = (input(PREGUNTA_DESEO))
isAfirmacion = respuesta == "SI"
LoQueResponde = ""

if (isAfirmacion):
    LoQueResponde = MENSAJE_SI
else:
    LoQueResponde = MENSAJE_NEGACION

print (LoQueResponde)

BuenaGente = LoQueResponde == MENSAJE_SI

if (BuenaGente):
    print (MENSAJE_DESPEDIDA_BUENA)



