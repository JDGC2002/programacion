import matplotlib.pyplot as plt

Snacks = []
PreciosSnacks = []
NumeroRepeticiones = 8


for i in range(NumeroRepeticiones):
    Snackk = str(input('Introduzca el nombre del snack: '))
    Snacks.append (Snackk)
    Precios = float(input('Introduzca el precio: '))
    PreciosSnacks.append (Precios)


plt.bar (Snacks, PreciosSnacks)
plt.title ('Snacks favoritos vs su precio')
plt.xlabel ('Snack')
plt.ylabel ('Precio')
plt.savefig ('graficoDeSnacks.png')
plt.show ()


