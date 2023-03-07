class Pojisteny:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon
        self.je_pojisteny = True

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni} ({self.vek}), tel: {self.telefon}"

    def odejdi(self):
        self.je_poisteny = False
