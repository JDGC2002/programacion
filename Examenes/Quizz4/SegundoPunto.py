import matplotlib.pyplot as plt

ciudades = []
poblaciones = []

NumeroRepe = 5

for ciudad in range(NumeroRepe):
    ciudadd = str(input('Ingrese la ciudad: '))
    ciudades.append (ciudadd)
    Pob = float(input('Ingrese la población de la ciudad: '))
    poblaciones.append(Pob)


ubicacion = poblaciones.index(max(poblaciones))
pieExplode = [0,0,0,0,0]
pieExplode[ubicacion] = 0.2

plt.pie (poblaciones, labels=ciudades, explode=pieExplode, shadow= True)
plt.title ('Ciudades favoritas y su poblacion')
plt.show ()