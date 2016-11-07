from Osoba import Osoba
from datetime import date

class Student(Osoba):
    """Klasa przedstawiajaca osobe studenta."""


    def __init__(self, imie):
        super(Student, self).__init__(imie)
        self.rok = ""
        self.dzienniczek = {}
        self.obecnosci = {}

    def przypisz_sobie_rok(self, rok):
        self.rok = rok
    
    def dodaj_przedmiot_do_dzienniczka(self, przedmioty=[]):
        for przedmiot in przedmioty:
            self.dzienniczek[przedmiot] = []

    def wpisz_obecnosc(self, dzien=date.today(), obecnosc=True):
        if obecnosc:
            self.obecnosci[dzien] = "obecny"
        else:
            self.obecnosci[dzien] = "nieobecny"

    def sprawdz_obecnosci(self):
        print "\nLista obecnosci studenta %s:" % self.nazwa
        for dzien, obecnosc in self.obecnosci.iteritems():
            print "%s\t%s" % (dzien, obecnosc)

    def wpisz_ocene(self, przedmiot, ocena):
        if przedmiot in self.dzienniczek.keys():
            self.dzienniczek[przedmiot].append(ocena)

    def srednia(self, oceny):
        return sum(oceny)/len(oceny)

    def sprawdz_srednia_z_przedmiotu(self, przedmiot):
        print "\nStudent %s ma z przedmiotu %s oceny: %s" % (self.nazwa, przedmiot, self.dzienniczek[przedmiot])
        print "Srednia ocen z przedmiotu: %.2f." % self.srednia(self.dzienniczek[przedmiot])

    def sprawdz_srednia_z_semestru(self):
        print "\nStudent %s ma w tym semestrze oceny:" % self.nazwa
        oceny_z_semestru = []
        for przedmiot, oceny in self.dzienniczek.iteritems():
            print "%s:\t%s" % (przedmiot, str(oceny)[1:-1])
            oceny_z_semestru.extend(oceny)
        print "Srednia ocen z calego semestu: %.2f." % self.srednia(oceny_z_semestru)