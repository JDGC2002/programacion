nombres = []
print (type(nombres))
print(nombres)   
nombres = ['Diego', 'Kaiser', 'Jhon']
print (nombres)
print (nombres[2])
nombres.append('Camilo')

edades = [15, 18, 19, 23, 1, 53, 28, 66]
print (edades)
print (edades [:2])
print (edades [2:5])
print (edades [:])
print (edades [3:])
edades.sort()
print(edades)
edades.sort(reverse=True)
print (edades)
mayor = max(edades)
print (mayor)
menor = min(edades)
print (menor)
##cuenta de elementos
LargoListaEdades = len(edades)
###operaciones
sumaEdades = sum(edades)
print (sumaEdades)
##calculo promedio
promedioEdades = sumaEdades/LargoListaEdades
print (promedioEdades)
##eliminar un elemento
edades.pop (2)
print (edades) 
print ("-------------------------------------------------------")

#ciclos for 
LargoListaEdades = len(edades)
for indice in range (LargoListaEdades):
    print ('estoy en la posición',
    indice, 'valgo',
    edades[indice])
print ("-------------------------------------------------------")

LargoListaNombres = len(nombres)
for indice in range (LargoListaNombres):
    print ('estoy en la posición',
    indice, 'y mi nombre es',
    nombres[indice])
print ("-------------------------------------------------------")

PosicionesConValoresPares = []
LargoListaEdades = len(edades)
for posicion in range (LargoListaEdades):
    if (edades[posicion]%2 == 0):
        PosicionesConValoresPares.append(posicion)

print (edades)
print (PosicionesConValoresPares)

#solo cuando interese mostrar la lista
posicion = 0
for edad in edades:
    print (edad)
for nombre in nombres:
    print (nombre)
    print (posicion)
    posicion+=1

posicion = 0
PosicionesPares = []
for edad in edades:
    if (edad%2 == 0):
        PosicionesPares.append (posicion)
    posicion+=1

print (PosicionesPares)


