import random

def heitä_noppaa(tahkot):
    return random.randint(1, tahkot)

tahkot = int(input("Anna tahkojen määrä: "))
    silmäluku = 0
    while silmäluku != tahkot:
        silmäluku = heitä_noppaa(tahkot)
        print(silmäluku)

