pituus = float(input("Kuhan pituus :"))

if pituus <= 37:
    # Kuha onalamittainen. Lasketaan kuinka paljon.
    alamittaisuus = 37 - pituus
    print(f"Kalasi on {alamittaisuus}cm liian lyhyt!")


else:
    print("Voit syödä kalan")