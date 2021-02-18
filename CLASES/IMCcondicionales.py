#----------constantes---------#
PREGUNTA_PESO = "¿Cuánto pesas? en kg: "
PREGUNTA_ESTATURA = "¿Cuánto mides? en metros: "
MENSAJE_BIENVENIDA = "Hola, calcularé tu IMC"
MENSAJE_BAJO = "Estás delgado "
MENSAJE_NORMAL = "Estás bien "
MENSAJE_SOBREPESO = "Tienes sobrepeso "
MENSAJE_OBESIDAD = "Tienes obesidad "

#------entradas al código----------#
print (MENSAJE_BIENVENIDA)
peso = int (input(PREGUNTA_PESO))
estatura = float (input(PREGUNTA_ESTATURA))
imc = peso/(estatura**2)
print (imc, "%")
resultado = ""
isBajo = imc < 18.5
isNormal = imc >= 18.5 and imc < 25
isSobrepeso = imc >= 25 and imc < 30

if (isBajo):
    resultado = MENSAJE_BAJO
elif (isNormal):
    resultado = MENSAJE_NORMAL
elif (isSobrepeso):
    resultado = MENSAJE_SOBREPESO
else:
    resultado = MENSAJE_OBESIDAD

print (resultado)