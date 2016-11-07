class Osoba(object):
    """Klasa przedstawiajaca osobe."""

    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __str__(self):
        return self.nazwa