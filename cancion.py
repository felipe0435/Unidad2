class Cancion(object):
    def __init__(self):
        self.autor = None
        self.nombre = None
        self.genero = None
        self.anio = 0
        self.duracion = 0


    def set_autor(self, autor):
        self.autor = autor


    def set_nombre(self, nombre):
        self.nombre = nombre


    def set_genero(self, genero):
        self.genero = genero


    def set_anio(self, anio):
        self.anio = anio


    def set_duration(self, duration):
        self.duration = duration


    def get_autor(self):
        return self.autor


    def get_nombre(self):
        return self.nombre


    def get_genero(self):
        return self.genero


    def get_anio(self):
        return self.anio


    def get_duration(self):
        return self.duration
