import matplotlib.pyplot as plt

mangas = ['One piece', 'Berserk', 'Monster']
encuesta2 = [35, 53, 32]

plt.bar (mangas, encuesta2)
plt.title ('Mangas favoritos')
plt.xlabel ('Mangas')
plt.ylabel ('Numero de personas')
plt.show ()