class zarowka:
    def __init__(self, name, moc, napiecie, stan):
        self.name = name
        self.moc = moc
        self.napiecie = napiecie
        self.stan = stan

    def info(self):
        print("Zarowka: "+self.name)
        print("Moc: "+self.moc)
        print("Napiecie: "+self.napiecie)

    def state(self):
        print("Stan: ", end="")
        print(self.stan)

    def onoff(self):
        if self.stan == 1:
            self.stan = 0
            print("Wyłączam...")
            print("Stan: ",end="")
            print(self.stan)
        else:
            self.stan = 1
            print("Włączam...")
            print("Stan: ",end="")
            print(self.stan)

    def dzwiek(self):
        print("Bzzzzzz...")
        pass


class jazeniowka (zarowka):
    def dzwiek(self):
        print("Brrrrr...")


def swiatelka(obj):
    obj.info()
    obj.dzwiek()
    obj.state()
    obj.onoff()


zarowka = zarowka("zarowka1", "230V", "50W", 1)
swiatelka(zarowka)


print("\n")

jazeniowka = jazeniowka("Jazeniowka", "100V", "250W", 0)
swiatelka(jazeniowka)




