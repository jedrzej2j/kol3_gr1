from Student import Student
from Nauczyciel import Nauczyciel
from datetime import date

class Uczelnia(object):
    """Klasa przedstawiajaca uczelnie."""

    __lista_dostepnych_przedmiotow = ["Matematyka", "Fizyka", "C++", "Java", "Python", "Wf"]
    __maksymalna_ilosc_przedmiotow_na_roku = 2

    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.nauczyciele = {}
        self.studenci = {}
        self.plan_zajec = {"I": [], "II": [], "III": [], "IV": [], "V": []}
        self.data = date.today()
        
    def ustaw_dzien(self, dzien):
        if isinstance(dzien, date):
            self.data = dzien
        
    def dodaj_studenta(self, student, rok="I"):
        if isinstance(student, Student):
            if rok in self.plan_zajec.keys():
                student.przypisz_sobie_rok(rok)
                self.studenci[student] = student
                print "Do uczelni %s do klasy %s zapisano studenta o imieniu %s." % (self.nazwa, rok, student)
            else:
                print "Student o imieniu %s istnieje, ale w uczelni %s nie ma roku %s." % (student, self.nazwa, rok)
        else:
            print "Nie mozna dodac %s, obiekt nie jest studentem." % student

    def dodaj_nauczyciela(self, nauczyciel, przedmioty=[]):
        if isinstance(nauczyciel, Nauczyciel):
            for przedmiot in przedmioty:
                if przedmiot in self.__lista_dostepnych_przedmiotow:
                    nauczyciel.przypisz_sobie_przedmiot(przedmiot)
            self.nauczyciele[nauczyciel] = nauczyciel
            print "Do uczelni %s zapisano nauczyciela o imieniu %s." % (self.nazwa, nauczyciel)
            print "%s uczy przedmiotow: " % nauczyciel + str(self.nauczyciele[nauczyciel].przedmioty)[1:-1]
        else:
            print "Nie mozna dodac %s, obiekt nie jest nauczycielem." % nauczyciel

    def ustal_plan_zajec(self, rok, przedmioty=[]):
        print "Ustalam plan zajec %s dla roku %s" % (rok, str(przedmioty)[1:-1])
        if rok in self.plan_zajec.keys():
            for przedmiot in przedmioty:
                if przedmiot in self.__lista_dostepnych_przedmiotow and len(self.plan_zajec[rok])<self.__maksymalna_ilosc_przedmiotow_na_roku:
                    self.plan_zajec[rok].append(przedmiot)
            print "Plan zajec dla roku %s: " % rok + str(self.plan_zajec[rok])[1:-1]
        else:
            print "W uczelni %s nie ma klasy %s, nie mozna ustalic planu zajec." % (self.nazwa, rok)

    def sprawdz_plan_zajec(self):
        status = True
        for student in self.studenci.itervalues():
            if not self.plan_zajec[student.rok]:
                print "Student %s zapisal sie na rok %s, ale nie ma ustalonego planu zajec!" % (student, student.rok)
                status = False
            else:
                print "Student %s zapisal sie na rok %s i dostal plan zajec: %s."  %  (student, student.rok, str(self.plan_zajec[student.rok])[1:-1])
                student.dodaj_przedmiot_do_dzienniczka(self.plan_zajec[student.rok])
        przedmioty = list(set([przedmiot for lista_przedmiotow in self.plan_zajec.itervalues() for przedmiot in lista_przedmiotow]))
        for przedmiot in przedmioty:
            for nauczyciel in self.nauczyciele.itervalues():
                if przedmiot in nauczyciel.przedmioty:
                    print "Nauczyciel %s bedzie w tym roku uczyl przedmiotu %s." % (nauczyciel, przedmiot)
                    break
            else:
                print "Nie ma przypisanego nauczyciela do przedmiotu %s!" % przedmiot
                status = False
        return status

    def zacznij_nowy_semestr(self):
        print "\n\nSprawdzam, czy mozna zaczac nowy semestr...\n"
        if not self.sprawdz_plan_zajec():
            print "\nNie mozemy zaczac nowego semestru, nie wszystko jeszcze gotowe!"
        else:
            print "\nZACZYNAMY NOWY SEMESTR!!! %s" % self.data

    def sprawdz_obecnosc(self, lista_obecnosci):
        print "\nDzien %s, sprawdzam obecnosc..." % self.data
        for student, obecnosc in lista_obecnosci:
            print "Student %s jest %s." % (student, "obecny" if obecnosc else "nieobecny")
            self.studenci[student].wpisz_obecnosc(self.data, obecnosc)

    def wpisz_ocene(self, student, nauczyciel, przedmiot, ocena):
        if student.obecnosci[self.data] == "nieobecny":
            print "Student %s jest dzis nieobecny, nie mozna wpisac oceny!" % student
        elif przedmiot not in student.dzienniczek.keys():
            print "Student %s nie jest zapisany na przedmiot %s, nie mozna wpisac oceny!" % (student, przedmiot)
        elif przedmiot not in nauczyciel.przedmioty:
            print "Nauczyciel %s nie uczy przedmiotu %s, wiec nie moze wpisac oceny studentowi %s!" % (nauczyciel, przedmiot, student)
        elif ocena not in [2.0, 3.0, 3.5, 4.0, 4.5,  5.0]:
            print "Nie mozna wpisac oceny %s!" % ocena
        else:
            print "Nauczyciel %s wpisal studentowi %s ocene %.1f z przedmiotu %s" % (nauczyciel, student, ocena, przedmiot)
            student.wpisz_ocene(przedmiot, ocena)