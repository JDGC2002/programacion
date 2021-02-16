#---------Constantes-------#
PREGUNTA_NOMBRE = "¿Cómo te llamas?: "
PREGUNTA_EDAD = "¿Cuántos años tienes?: "
PREGUNTA_ESTATURA = "¿Cuál es tu estatura?: "
PREGUNTA_PESO = "¿Cuánto pesas?"
MENSAJE_SALUDO = "Un gusto conocerte"
#---------Entradas al código-----#
Nombre = input (PREGUNTA_NOMBRE)
Edad = int (input (PREGUNTA_EDAD))
Estatura = float (input (PREGUNTA_ESTATURA))
Peso = int (input (PREGUNTA_PESO))
print (MENSAJE_SALUDO, Nombre)
print ("tu edad en 5 años será:", Edad + 5)
print ("tu estatura es: ", Estatura)
print ("tu peso es: ", Peso, "kg")