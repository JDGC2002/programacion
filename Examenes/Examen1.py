#--------CONSTANTES-----#
MENSAJE_BIENVENIDA = "Hola, a continuación podrá ingresar los datos y se le brindará una valoración del paciente"
PREGUNTA_DATOS_TRI = "Ingrese el nivel de triglicéridos del paciente: "
PREGUNTA_DATOS_HOM = "Ingrese el nivel de homocisteína del paciente: "
MENSAJE_OPTIMO = "El valor del paciente es óptimo"
MENSAJE_SOBRE_LIMITE = "El valor del paciente está sobre el límite"
MENSAJE_SOBRE_ALTO = "El valor del paciente está alto"
MENSAJE_SOBRE__MUY_ALTO = "El valor del paciente está muy alto"
MENSAJE_DESPEDIDA = "Proceso Finalizado"

#------Entrada al código---------#
print (MENSAJE_BIENVENIDA)
TRIGLICERIDOS = int(input(PREGUNTA_DATOS_TRI))
isOptimoT = TRIGLICERIDOS < 150
isSobreLimiteOptimoT = TRIGLICERIDOS >= 150 and TRIGLICERIDOS <= 199
isAltoT = TRIGLICERIDOS >= 200 and TRIGLICERIDOS <= 499
resultado_tri = ""

if (isOptimoT):
    resultado_tri = MENSAJE_OPTIMO
elif (isSobreLimiteOptimoT):
    resultado_tri = MENSAJE_SOBRE_LIMITE
elif (isAltoT):
    resultado_tri = MENSAJE_SOBRE_ALTO
else:
    resultado_tri = MENSAJE_SOBRE__MUY_ALTO

print (resultado_tri)

HOMOCISTEINA = int(input(PREGUNTA_DATOS_HOM))
isOptimoH = HOMOCISTEINA > 2 and HOMOCISTEINA <= 15
isSobreLimiteOptimoH = HOMOCISTEINA > 15 and HOMOCISTEINA <= 30
isAltoH = HOMOCISTEINA > 30 and HOMOCISTEINA <= 100
resultadoH = ""

if (isOptimoH):
    resultadoH = MENSAJE_OPTIMO
elif (isSobreLimiteOptimoH):
    resultadoH = MENSAJE_SOBRE_LIMITE
elif (isAltoH):
    resultadoH = MENSAJE_SOBRE_ALTO
else:
    resultadoH = MENSAJE_SOBRE__MUY_ALTO

print (resultadoH)
print (MENSAJE_DESPEDIDA)

