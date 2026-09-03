def listan_summa(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa

def pääohjelma():
    luvut = [3, 7, 1, 9, 4]
    print("Summa:", listan_summa(luvut))

pääohjelma()