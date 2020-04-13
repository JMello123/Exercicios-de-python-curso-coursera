class Triangulo():
    def __init__(self,lado_a,lado_b,lado_c):
        self.a = lado_a
        self.b = lado_b
        self.c = lado_c
        self.lados = sorted([self.a,self.b,self.c])

    def perimetro(self):
        per = self.a + self.b + self.c
        return per

    def tipo_lado(self):
        if self.a == self.b == self.c == self.a:
            return 'equilátero'
        if self.a != self.b != self.c != self.a:
            return 'escaleno'
        else:
            return 'isósceles'

    def retangulo(self):
        if self.lados[0]/3 == self.lados[1]/4 == self.lados[2]/5 == self.lados[0]/3:
            return True
        else:
            return False

    def semelhantes(self, triangulo):
        a = triangulo.a
        b = triangulo.b
        c = triangulo.c
        lados = sorted([a,b,c])
        if self.lados[0]/lados[0] == self.lados[1]/lados[1] == self.lados[2]/lados[2] == self.lados[0]/lados[0]:
            return True
        else:
            return False



class Carro():
    def __init__(self):
        self.ano = 2000

    def __getattribute__():
        return self.ano

mercedao = Carro()
print(mercedao.ano)