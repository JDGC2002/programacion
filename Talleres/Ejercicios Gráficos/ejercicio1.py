import matplotlib.pyplot as plt 

Meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
IngresosMes = [6.2, 6.2, 6.2, 6.2, 6.2, 7.8, 6.2, 6.2, 6.2, 6.2, 6.2, 8.5]

plt.bar (Meses, IngresosMes, width=0.7, )
plt.title ('Ingresos por mes de pablo')
plt.xlabel ('Meses del año')
plt.ylabel ('Ingresos')
plt.show()