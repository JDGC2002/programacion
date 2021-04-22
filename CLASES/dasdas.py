class  Artista(Usuario):
    def _init_(self, nombreEntrada, edadEntrada, sexoEntrada, nacionalidadEntrada, generomusicalEntrada, numerocancionesEntrada, numeroalbumEntrada):
        Usuario._init_(self, nombreEntrada, edadEntrada, sexoEntrada, nacionalidadEntrada)
        self.generomusical = generomusicalEntrada
        self.numerocanciones = numerocancionesEntrada
        self.numeroalbum = numeroalbumEntrada

    def mostrarAtributos (self):
        print(f''' Mi nombre es {self.nombre}, 
        soy cantante del genero {self.generomusical}. 
        Hasta la fecha tengo {self.numerocanciones}
        canciones en {self.numeroalbum} albumes
        ''')

    def ubicacion (self, ciudad):
        print(f''' El día de mañana 
        dare un concierto en {ciudad},
        los espero.
    ''')

artista = Artista('Bad Bunny', 'trap', 83, 5)

artista.mostrarAtributos()
artista.ubicacion('Medellín')