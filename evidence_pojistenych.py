class EvidencePojistenych:

    def __init__(self):
        self.pojisteni = []

    def pridej_pojisteneho(self, pojisteny):
        self.pojisteni.append(pojisteny)

    def vypis_vsechny_pojistene(self):
        for pojisteny in self.pojisteni:
            if pojisteny.je_pojisteny:
                print(pojisteny)
            else:
                self.pojisteni.remove(pojisteny)

    def najdi_pojisteneho(self, jmeno, prijmeni):
        for pojisteny in self.pojisteni:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni and pojisteny.je_pojisteny:
                return pojisteny
        return None

    def odeber_pojisteneho(self, pojisteny):
        pojisteny.odejdi()
