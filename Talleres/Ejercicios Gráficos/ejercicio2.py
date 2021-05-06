import matplotlib.pyplot as plt 

pieLabels = ['Medellín', 'Bogotá', 'Cali', 'Barranquilla', 'Cartagena']
sizes = [25, 40, 15, 10, 5]

pieExplode = [0, 0.2, 0, 0, 0]
plt.pie(sizes, labels=pieLabels, explode=pieExplode, shadow= True, startangle= 90)
plt.title ('Ciudades más pobladas de Colombia')
plt.show ()
