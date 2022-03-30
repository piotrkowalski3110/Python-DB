class zarowka:
    def __init__(self, name, moc, napiecie):
        print("Zarowka: "+name)
        print("Moc: "+moc)
        print("Napiecie: "+napiecie)

    def stan(self, stan):
        print(stan)

    def onoff(self, stan1):
        if self.stan == 1:
            self.stan1 = 0
            print("Wyłączam...")
        if self.stan == 0:
            self.stan1 = 1
            print("Włączam...")

    def dzwiek(self):
        pass


class jazeniowka (zarowka):
    def dzwiek(self):
        print("Brrrrr...")


z1 = zarowka("zarowka1", "230V", "50W")
z1.stan(0)
z1.onoff(1)

print("\n")

j1 = jazeniowka("Jazeniowka", "100V", "250W")
j1.stan(0)
j1.dzwiek()



