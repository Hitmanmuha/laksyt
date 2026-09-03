import random

def heitä_noppaa():
    return random.randint(1, 6)

def pääohjelma():
    silmäluku = 0
    while silmäluku != 6:
        silmäluku = heitä_noppaa()
        print(silmäluku)

pääohjelma()