def gallonit_litroiksi(gallonit):
    return gallonit * 3.785

def pääohjelma():
    gallonit = float(input("Anna gallonimäärä (negatiivinen lopettaa): "))
    while gallonit > 0:
        litrat = gallonit_litroiksi(gallonit)
        print(f"{gallonit} gallonii on {litrat:.2f} litrat")
        gallonit = float(input("Anna gallonimäärä (negatiivinen lopettaa): "))

pääohjelma()