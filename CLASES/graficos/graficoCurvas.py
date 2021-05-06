import matplotlib.pyplot as plt

tiempo = [0,1,2,3,4,5]
sensor = [4,5,6,8,9,10]
plt.plot(tiempo,sensor,'--,r')
############
plt.title('Gráfico Sensor contra el tiempo')
plt.xlabel('Tiempo(s)')
plt.ylabel('Voltaje(mV)')
############
plt.show()

diccionario = {}
diccionario['NombresEstudiantes'] = ['Jacobo', 'Dani', 'Maria', 'Elena']
diccionario['EdadEstudiantes'] = [18, 17, 24, 32]
diccionario['peso'] = [84, 56, 64, 57]
print(diccionario)
print (diccionario['NombresEstudiantes'][-1], diccionario['EdadEstudiantes'][-1], diccionario['peso'][-1])

import pandas as pd 

ecgData = pd.read_csv('ecg.csv', encoding='UTF-8', header=0, delimiter=';').to_dict()
muestras = list(ecgData['muestra'].values())
print (muestras[:5])
voltaje = list(ecgData['valor'].values())
print (voltaje[-10:])

plt.plot(muestras, voltaje, 'c')
plt.title ('Frecuencia cardiaca')
plt.xlabel ('Tiempo (microsegundos)')
plt.ylabel ('Voltaje (microvoltios)')

plt.show()


