syote = input("Anna luku: ")
luku = float(syote)
pienin = luku
suurin = luku
while syote != "":
    if luku < pienin:
        pienin = luku
    if luku > suurin:
        suurin = luku
    syote = input("Anna luku: ")
    if syote != "":
            luku = float(syote)
print("Pienin: ", pienin)
print("Suurin: ", suurin)