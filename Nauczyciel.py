from Osoba import Osoba

class Nauczyciel(Osoba):
    """Klasa przedstawiajaca osobe nauczyciela."""


    def __init__(self, nazwisko):
        super(Nauczyciel, self).__init__(nazwisko)
        self.przedmioty = []

    def przypisz_sobie_przedmiot(self, przedmiot):
        self.przedmioty.append(przedmiot)
    