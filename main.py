from evidence_pojistenych import EvidencePojistenych
from pojisteny import Pojisteny

evidence = EvidencePojistenych()

while True:
    print("Evidence pojistěných")
    print("Vyberte si akci:")
    print("1. Přidat nového pojistného")
    print("2. Vypsat všechny pojistné")
    print("3. Vyhledat pojistného")
    print("4. Odebrat pojistného")
    print("5. Konec")

    volba = input()

    if volba == "1":
        jmeno = input("Jméno: ")
        prijmeni = input("Příjmení: ")
        vek = None
        while not vek:
            try:
                vek = int(input("Věk: "))
            except ValueError:
                print("Neplatný věk. Zadejte celé číslo.")
        telefon = None
        while not telefon or len(telefon) != 9:
            telefon = input("Telefonní číslo (9 číslic): ")
            if not telefon.isdigit():
                print("Telefonní číslo může obsahovat pouze číslice.")
            elif len(telefon) != 9:
                print("Telefonní číslo musí mít délku 9 číslic.")
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        evidence.pridej_pojisteneho(pojisteny)
        print("Pojistný byl přidán.")
    elif volba == "2":
        evidence.vypis_vsechny_pojistene()
    elif volba == "3":
        jmeno = input("Jméno: ")
        prijmeni = input("Příjmení: ")
        pojisteny = evidence.najdi_pojisteneho(jmeno, prijmeni)
        if pojisteny:
            print(pojisteny)
        else:
            print("Pojistný nebyl nalezen.")
    elif volba == "4":
        jmeno = input("Jméno: ")
        prijmeni = input("Příjmení: ")
        pojisteny = evidence.najdi_pojisteneho(jmeno, prijmeni)
        if pojisteny:
            evidence.odeber_pojisteneho(pojisteny)
            print("Pojistný byl odebrán.")
        else:
            print("Pojistný nebyl nalezen.")
    elif volba == "5":
        break
    else:
        print("Neplatná volba.")
