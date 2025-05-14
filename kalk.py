import math

def kalkulacka():
    print("🧮 Pokročilá textová kalkulačka")
    print("Zadej matematický výraz (např. 2 + 3 * (4 - 1))")
    print("Podporované funkce: +  -  *  /  **  (), sin, cos, sqrt, log, atd.")
    print("Napiš 'konec' pro ukončení.\n")

    # Povolené funkce a konstanty
    povolene = {
        'sqrt': math.sqrt,
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'log': math.log,       # přirozený logaritmus
        'log10': math.log10,
        'pi': math.pi,
        'e': math.e,
        '__builtins__': None   # zákaz přístupu k vestavěným funkcím
    }

    while True:
        vstup = input("Zadej výraz: ")

        if vstup.lower() == "konec":
            print("Kalkulačka ukončena.")
            break

        try:
            vysledek = eval(vstup, povolene)
            print(f"Výsledek: {vysledek}\n")
        except Exception as e:
            print(f"Chyba: {e}\n")


# Spuštění kalkulačky
kalkulacka()
