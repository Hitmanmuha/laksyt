import random
oikea_luku = random.randint(1, 10)
arvaus = int(input("Arvaa luku 1-10: "))

while arvaus != oikea_luku:
    if arvaus > oikea_luku:
        print("Liian suuri arvaus")
    else:
        print("Liian suuri oikea arvaus")
    arvaus = int(input("Arvaa luku 1-10: "))

print("oikea_luku")