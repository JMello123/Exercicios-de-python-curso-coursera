class Triangulo():
    def __init__(self,lado_a,lado_b,lado_c):
        self.a = lado_a
        self.b = lado_b
        self.c = lado_c

    def calcula_perimetro(self):
        per = self.a + self.b + self.c
        return per

    def tipo_lado(self):
        if self.a == self.b == self.c == self.a:
            return 'equilátero'
        if self.a != self.b != self.c != self.a:
            return 'escaleno'
        else:
            return 'isósceles'

