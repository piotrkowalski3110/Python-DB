def choinka(znak, wysokosc, ilosc):
    znaki = 1
    for n in range (ilosc):
        znaki = 1
        for m in range (wysokosc):
            print(' '*(wysokosc-1-m)+znak*(znaki)+' '*(wysokosc-1-m))
            znaki = znaki + 2

def tagi(tag, tekst):
    tag1 = ("<"+tag+">"+tekst+"</"+tag+">")
    return tag1

"""zad1"""
choinka("$",4,4);

"""zad2"""
taga = tagi("h1","test")
print(taga)

