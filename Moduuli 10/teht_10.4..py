import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Rekisteritunnus':<16}{'Huippunopeus':>14}{'Nopeus':>10}{'Matka':>12}")
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<16}{auto.huippunopeus:>10} km/h{auto.nopeus:>6} km/h{auto.kuljettu_matka:>8.0f} km")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False


autot = []
for numero in range(1, 11):
    autot.append(Auto(f"ABC-{numero}", random.randint(100, 200)))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1
    if tunnit % 10 == 0:
        print(f"\nTunti {tunnit}:")
        kilpailu.tulosta_tilanne()

print(f"\nKilpailu {kilpailu.nimi} päättyi, tunteja kului {tunnit}:")
kilpailu.tulosta_tilanne()