#CONSTANTES
MENSAJE_NUMERO = '''INGRESE ALGUNA DE LAS OPCIONES
    1- Hacer conversión de pesos a dolares o euros.
    2- Agregue un valor a la lista
    3- Obtenga el valor máximo, mínimo y el promedio de la lista
    4- Elimine un elemento de la lista
    5- Salir
    '''
MENSAJE_CONVERSION = '''¿Cuál es la conversión que deseas hacer?
    C- Mostrar la lista original (en cop)
    D- para dolares
    E- para euros
    '''
MENSAJE_PESOS = 'Mostrando la lista original'
MENSAJE_DOLARES = 'Mostrando la lista en dolares'
MENSAJE_EUROS = 'Mostrando la lista en euros'
MENSAJE_INVALIDO = 'Opción inválida'
PREGUNTA_NUMERO = 'Ingrese el valor que desea adicionar a la lista: '
MENSAJE_ELIMINAR = 'Se mostrará la lista, podrás elegir el número de la lista para eliminarlo. Elige: '

#LISTAS
listaPesos = [20000,30000,4000,2500,1000,7600]
listaEuros = []
for numero in listaPesos:
    conversor = round (numero*0.00023, 2)
    listaEuros.append (conversor)
listaDolares = []
for numero in listaPesos:
    conversor = round (numero*0.00027)
    listaDolares.append (conversor)


#CÓDIGO

opcionEscogida = int(input(MENSAJE_NUMERO))
while (opcionEscogida != 5):
    is1 = opcionEscogida == 1
    is2 = opcionEscogida == 2
    is3 = opcionEscogida == 3
    is4 = opcionEscogida == 4
    isInvalido = opcionEscogida != 5
    print ('------------------------')
    if (is1):
        print ('---------------------------')
        print ('escogiste 1')
        OpcionMoneda = str(input(MENSAJE_CONVERSION))
        if (OpcionMoneda == 'C'):
            print (MENSAJE_PESOS, listaPesos)
        elif (OpcionMoneda == 'D'):
            print (MENSAJE_DOLARES, listaDolares)
        elif (OpcionMoneda == 'E'):
            print (MENSAJE_EUROS, listaEuros)
        else:
            print (MENSAJE_INVALIDO)
        print ('---------------------------')
    elif (is2):
        print ('escogiste 2')
        ValorIngresado = float(input(PREGUNTA_NUMERO))
        listaPesos.append (ValorIngresado)
        print (listaPesos)
        print ('------------------------------')
    elif (is3):
        print ('escogiste 3')
        ValorAlto = max(listaPesos)
        print ('el mayor número de la lista es:', ValorAlto)
        ValorBajo = min(listaPesos)
        print ('el menor número de la lista es:', ValorBajo)
        ValorPromedio = sum(listaPesos)/len(listaPesos)
        print ('El promedio de la lista es:', ValorPromedio)
        print ('-----------------------------------')
    elif (is4):
        print ('escogiste 4')
        print (listaPesos)
        NumeroBorrar = int(input(MENSAJE_ELIMINAR)) - 1
        listaPesos.pop (NumeroBorrar)
        print (listaPesos)
        print ('-----------------------------------')
    else:  
        print (MENSAJE_INVALIDO)
        print ('-----------------------------------')
    opcionEscogida = int(input(MENSAJE_NUMERO))

print ('------------------------------')
print ('Feliz día')



