#----CONSTANTES-----#
MENSAJE_BIENVENIDA = "Hola, a continuación podrás ingresar una distancia en centímetros y calcularemos su equivalente en metros y kilometros"
PREGUNTA_DISTANCIA_CM = "¿Cuál es la distancia que deseas calcular?: "

#-----Entrada al código-------#
print (MENSAJE_BIENVENIDA)
DistanciaCM = float(input(PREGUNTA_DISTANCIA_CM))
DistanciaM = DistanciaCM / 100
DistanciaKM = DistanciaCM / 100000
print ("La distancia ingresada fue", DistanciaCM, "Cm,", "su equivalente en metros es:", DistanciaM, "M", "y en Kilometros es:", DistanciaKM, "Km")
