import matplotlib.pyplot as plt

pieLabels = ['py', 'java', 'dart', 'js']
sizes = [30, 25, 15, 10]

def etiquetarElementosPorcentuales (sizes, labels, indicador= '->'):
    acumulador = 0
    for elemento in sizes:
        acumulador += elemento

    for i in range (len(labels)):
        pieLabels [i] += indicador+str(sizes[i]/acumulador*100) + '%'

etiquetarElementosPorcentuales(sizes, pieLabels)
pieExplode = [0, 0, 0.2, 0]
plt.pie(sizes, labels=pieLabels, explode=pieExplode, shadow= True, startangle=45)
plt.title ("Uso de lenguajes de programación en el 2021")
plt.show()

