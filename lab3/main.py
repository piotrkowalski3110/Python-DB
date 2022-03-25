class zarowka:
    def __init__(self, name, moc, napiecie):
        self.name = name;
        print("Zarowka: "+name)
        print("Moc: "+moc)
        print("Napiecie: "+napiecie)

    def stan(self, stanzarowki):
        self.stanzarowki = stanzarowki

        if stanzarowki == 1:
            print("Włączona")
            return stanzarowki
        if stanzarowki == 0:
            print("Wyłączona")
            return stanzarowki

    def onoff(stanzarowki):
        if stanzarowki == 1:
            stan = 0
            print("Wyłączam...")
        if stanzarowki == 0:
            stan = 1
            print("Włączam...")

    def dzwiek(self):
        pass


class jazeniowka (zarowka):
    def dzwiek(self):
        print("Brrrrr...")


z1 = zarowka("zarowka1", "230V", "50W")
z1.stan(0)

print("\n")

j1 = jazeniowka("Jazeniowka", "100V", "250W")
j1.stan(1)
j1.dzwiek()



