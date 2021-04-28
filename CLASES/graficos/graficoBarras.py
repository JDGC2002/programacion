import matplotlib.pyplot as plt

lenguajes = ['py', 'java', 'dart', 'ts', 'elixir']
encuesta = [50, 10, 20, 10, 10]

plt.bar(lenguajes, encuesta)
plt.title ('Lenguajes más usados')
plt.xlabel ('lenguajes de programación')    
plt.ylabel ('% de uso de lenguajes')
plt.show ()

