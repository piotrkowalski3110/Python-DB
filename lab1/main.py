def palindrom(liczba):
    dl = len(str(liczba))
    for n in range (dl):
        if n==0:
            pierwsza = str(liczba)[0]
        if n==dl-1:
            ostatnia = str(liczba)[dl-1]

    if pierwsza == ostatnia:
        print("palindrom")
    else:
        print("nie palindrom")

def nowatablica(A, B):
    x = len(A)
    y = len(B)

    for n in range(x):
        if A[n]%2 != 0:
            Wynik.append(A[n])

    for m in range(y):
        if B[m]%2 == 0:
            Wynik.append(B[m])

    z = len(Wynik)

    for o in range(z):
        print("Wynik = ", end=" ")
        print(Wynik[o])

def listacyfr(liczba):
    for n in range(len(str(liczba))):
        T.append(liczba%10)
        liczba = (liczba - (liczba%10))//10
        print(T[n], end=" ")


def tabliczka():
    for n in range(10):
        for m in range(10):
            print((m+1)*(n+1), end=" ")
        print("\n")

def wyrazy(zdanie):
    if len(zdanie)>0:
        wyrazy = 1
    else:
        wyrazy = 0
    dlzdania = len(zdanie)
    for n in range(dlzdania):
        if zdanie[n] == " ":
            wyrazy = wyrazy + 1
    print(wyrazy)

def czestosc(zdanie):
    for n in range (len(zdanie)):

"""
###################### ZAD 1
liczba = 2562
palindrom(liczba)
"""

"""
###################### ZAD 2
A = []
B = []

A.append(20)
A.append(82)
A.append(5)
A.append(24)
A.append(25)

B.append(64)
B.append(25)
B.append(35)
B.append(80)
B.append(92)

Wynik = []

nowatablica(A,B)
"""

"""
####################### ZAD 3
liczba = 24698
T = []
listacyfr(liczba)
"""

"""
####################### ZAD 4
tabliczka()
"""

####################### ZAD 5
zdanie = "Rather than building all of its functionality into its core, Python was designed to be highly extensible via modules, its compact modularity has made it particularly popular as a means of adding programmable interfaces to existing applications."
wyrazy(zdanie)
czestosc(zdanie)








