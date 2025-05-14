"""
Autor: Jan Richter  
Email: JanRichter.jr@seznam.cz
Datum: 14. 5. 2025
Popis: Hra Bulls and Cows s měřením času a statistikami o počtu odhadů v jednotlivých hrách.
"""

import random
import time

def pozdrav():
    print("Vítej ve hře Bulls and Cows!")
    print("Musíš uhodnout čtyřmístné číslo s unikátními číslicemi, které nezačíná nulou.")
    print("Za každou správnou číslici na správné pozici získáš 'bull'.")
    print("Za správnou číslici na špatné pozici získáš 'cow'.")
    print("Například: 1234 je tajné číslo a tvůj tip je 1243, dostaneš 2 bulls a 2 cows.")
    print("Hra končí, když uhodneš tajné číslo.")
    print("Hodně štěstí!\n")

def generuj_tajne_cislo():
    cislice = list('123456789')  # první číslice nesmí být 0
    prvni = random.choice(cislice)
    cislice = list(set('0123456789') - set(prvni))
    zbytek = random.sample(cislice, 3)
    return prvni + ''.join(zbytek)

def je_validni_vstup(vstup):
    if not vstup.isdigit():
        print("Chyba: Vstup musí obsahovat pouze číslice.")
        return False
    if len(vstup) != 4:
        print("Chyba: Vstup musí být přesně 4 číslice.")
        return False
    if vstup[0] == '0':
        print("Chyba: Číslo nesmí začínat nulou.")
        return False
    if len(set(vstup)) != 4:
        print("Chyba: Všechny číslice musí být unikátní.")
        return False
    return True

def vyhodnot_tip(tajne_cislo, tip):
    bulls = sum(1 for i in range(4) if tip[i] == tajne_cislo[i])
    cows = sum(1 for i in range(4) if tip[i] in tajne_cislo and tip[i] != tajne_cislo[i])
    return bulls, cows

def vypis_vysledek(bulls, cows):
    bull_str = "bull" if bulls == 1 else "bulls"
    cow_str = "cow" if cows == 1 else "cows"
    print(f"{bulls} {bull_str}, {cows} {cow_str}")

def hraj_jednu_hru():
    tajne = generuj_tajne_cislo()
    pokusy = 0
    start_cas = time.time()

    while True:
        tip = input("Zadej svůj tip: ")
        if not je_validni_vstup(tip):
            continue
        pokusy += 1
        bulls, cows = vyhodnot_tip(tajne, tip)
        vypis_vysledek(bulls, cows)
        if bulls == 4:
            end_cas = time.time()
            trvani = round(end_cas - start_cas, 2)
            print(f"\nGratuluji! Uhodl(a) jsi číslo {tajne} na {pokusy}. pokus za {trvani} sekund.\n")
            return pokusy, trvani

def zobraz_statistiky(statistiky):
    print("📊 Statistiky her:")
    for i, (pokusy, cas) in enumerate(statistiky, 1):
        print(f"Hra {i}: {pokusy} pokusů, {cas} s")

def hraj_hry():
    pozdrav()
    statistiky = []

    while True:
        pokusy, cas = hraj_jednu_hru()
        statistiky.append((pokusy, cas))

        odpoved = input("Chceš hrát znovu? (a/n): ").strip().lower()
        if odpoved != 'a':
            break

    zobraz_statistiky(statistiky)
    print("\nDěkujeme za hru!")

# Spuštění hry
if __name__ == "__main__":
    hraj_hry()
