class Hissi:

    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylös(self):
        self.kerros += 1
        print(f"YLÖS => {self.kerros}")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"ALAS => {self.kerros}")

    def siirry_kerrokseen(self, kerros):
        while self.kerros < kerros and self.kerros < self.ylin:
            self.kerros_ylös()
        while self.kerros > kerros and self.kerros > self.alin:
            self.kerros_alas()


class Talo:

    def __init__(self, alin, ylin, hissien_maara):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []
        for i in range(hissien_maara):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissiä(self, numero, kerros):
        print(f"Hissi {numero}:")
        self.hissit[numero - 1].siirry_kerrokseen(kerros)

    def palohälytys(self):
        print("PALOHÄLYTYS!")
        numero = 1
        for hissi in self.hissit:
            print(f"Hissi {numero}:")
            hissi.siirry_kerrokseen(self.alin)
            numero += 1


talo = Talo(1, 10, 3)
talo.aja_hissiä(1, 6)
talo.aja_hissiä(2, 3)
talo.palohälytys()