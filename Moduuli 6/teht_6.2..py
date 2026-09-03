import random

def heitä_noppaa(tahkot):
    return random.randint(1, tahkot)

def pääohjelma():
    tahkot = int(input("Anna nopan tahkojen määrä: "))
    silmäluku = 0
    while silmäluku != tahkot:
        silmäluku = heitä_noppaa(tahkot)
        print(silmäluku)

pääohjelma()