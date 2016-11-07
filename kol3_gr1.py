#testy wykonane dla uzytkownika o nazwie: ketmia0

import unittest
import math

import Nauczyciel
import Osoba
import Student

class Test_Nauczyciel(unittest.TestCase):

	def setUp(self):
		self.test_name="Test_imie"
		self.test_instance = Nauczyciel.Nauczyciel(self.test_name)

	def test_method_przypisz_sobie_przedmiot(self):
		test_przedmiot1="przedmiot1"
		test_przedmiot2="przedmiot2"
		self.test_instance.przypisz_sobie_przedmiot(test_przedmiot1)
		self.test_instance.przypisz_sobie_przedmiot(test_przedmiot2)
		test_przedmioty = []
		test_przedmioty.append(test_przedmiot1)
		test_przedmioty.append(test_przedmiot2)
		self.assertEqual(test_przedmioty, self.test_instance.przedmioty)

class Test_Osoba(unittest.TestCase):

	def setUp(self):
		self.test_name="Test_imie"
		self.test_instance = Osoba.Osoba(self.test_name)

	def test_method___str__(self):
		self.assertEqual(self.test_name, str(self.test_instance))


class Test_Student(unittest.TestCase):

	def setUp(self):
		self.test_name="Test_imie"
		self.test_instance = Student.Student(self.test_name)

	def test_method_przypisz_sobie_rok(self):
		test_rok=1999
		self.test_instance.przypisz_sobie_rok(test_rok)
		self.assertEqual(test_rok, self.test_instance.rok)

	def test_method_dodaj_przedmiot_do_dzienniczka(self):
		dzienniczek={}
		przedmioty=[1,2,3]
		for przedmiot in przedmioty:
            		dzienniczek[przedmiot] = []
		self.test_instance.dodaj_przedmiot_do_dzienniczka(przedmioty)
		self.assertEqual(dzienniczek, self.test_instance.dzienniczek)





















