import random
class Instrumento:
    pass

class Guitarra(Intrumento):
    


class Musico:
    def __init__(self, ins):
        self.instrumento = ins

    def afinar_instrumento(self):
        self.instrumento.afinar()


    def tocar_instrumento(self):
        self.instrumento.tocar()
