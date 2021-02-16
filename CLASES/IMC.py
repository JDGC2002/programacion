#----------constantes---------#
PREGUNTA_PESO = "¿Cuánto pesas? en kg: "
PREGUNTA_ESTATURA = "¿Cuánto mides? en metros: "
MENSAJE_BIENVENIDA = "Hola, calcularé tu IMC"
MENSAJE_DESPEDIDA = "Tu IMC es: "

#------entradas al código----------#
print (MENSAJE_BIENVENIDA)
peso = int (input(PREGUNTA_PESO))
estatura = float (input(PREGUNTA_ESTATURA))
imc = peso/(estatura**2)
print (MENSAJE_DESPEDIDA, imc, "%")
isObeso = imc >= 30
print ("el resultado de la prueba de obesidad es:", isObeso)