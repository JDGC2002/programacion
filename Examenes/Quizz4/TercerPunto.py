import matplotlib.pyplot as plt
import pandas as pd 

print ('Se mostrará un ECG en pantalla, ECG son las siglas de electrocardiograma. un electrocardiograma es la representación visual de las pulsaciones')
ecgData = pd.read_csv('ecg.csv', encoding='UTF-8', header=0, delimiter=';').to_dict()
muestras = list(ecgData['muestra'].values())
voltaje = list(ecgData['valor'].values())

plt.plot(muestras, voltaje, 'c')
plt.title ('Frecuencia cardiaca')
plt.xlabel ('Tiempo (microsegundos)')
plt.ylabel ('Voltaje (microvoltios)')
plt.savefig ('ECGgrafico.png')
plt.show()

print ('se mostrará en pantalla una PPG, estas siglas significan photoplethysmography es una representación visual de, dependendiendo del caso: Ciclo cardiaco, flujo sanguíneo, respiración.')

ppgData = pd.read_csv('ppg.csv', encoding='UTF-8', header=0, delimiter=';').to_dict()
muestras = list(ppgData['muestra'].values())
pulsaciones = list(ppgData['valor'].values())

plt.plot(muestras, pulsaciones, 'c')
plt.title ('Fotopletismografía')
plt.xlabel ('Tiempo (segundos)')
plt.ylabel ('Volúmen sanguíneo')
plt.savefig ('PPGgrafico.png')
plt.show()
