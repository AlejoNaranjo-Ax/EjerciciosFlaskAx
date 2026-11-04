class Proyecto:
    def __init__(self, Nombre, Fecha, Hora, Lugar, Responsable, ClaveDelPrograma=None):
        self.ClaveDelPrograma = ClaveDelPrograma
        self.Nombre = Nombre
        self.Fecha = Fecha
        self.Hora = Hora
        self.Lugar = Lugar
        self.Responsable = Responsable

    def mostrar_informacion(self):
        return f"Programa: {self.Nombre} | Fecha: {self.Fecha} a las {self.Hora} | Lugar: {self.Lugar} | Responsable: {self.Responsable}"

    def actualizar_proyecto(self, Nombre, Fecha, Hora, Lugar, Responsable):
        self.Nombre = Nombre
        self.Fecha = Fecha
        self.Hora = Hora
        self.Lugar = Lugar
        self.Responsable = Responsable