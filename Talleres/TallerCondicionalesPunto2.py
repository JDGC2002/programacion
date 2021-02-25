#-------CONSTANTES-----#
MENSAJE_BIENVENIDA  = "Hola, el programa ha iniciado"
PREGUNTA_EDAD = "¿Cuál es tu edad?: "
MENSAJE_MENOR = "Eres menor de edad"
MENSAJE_JOVEN = "Eres joven"
MENSAJE_ADULTO = "Eres adulto"
MENSAJE_ADULTO_MAYOR = "Eres adulto mayor"

#------INTRODUCIR------#

print (MENSAJE_BIENVENIDA)
Edad = int(input(PREGUNTA_EDAD))
isMenor = Edad < 18
isJoven = Edad >= 18 and Edad < 25
isAdulto = Edad >= 26 and Edad < 60
isAdultoMayor = Edad >= 60 
resultado = ""

if (isMenor):
    resultado = MENSAJE_MENOR
elif (isJoven):
    resultado = MENSAJE_JOVEN
elif (isAdulto):
    resultado = MENSAJE_ADULTO
else:
    resultado = MENSAJE_ADULTO_MAYOR

print (resultado)
print ("el proceso ha finalizado, hasta luego")