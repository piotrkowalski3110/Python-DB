def encode (znaki, lista):
    length = len(znaki)
    licznik = 0

    for n in range (length):
        if n < len(lista):
            ascii = ord(znaki[n])
            ascii = ascii + lista[n]
            if ascii > 90:
                ascii = ascii - 26
            znak = chr(ascii)
            print(znak, end="")

        if n >= len(lista):
            ascii = ord(znaki[n])
            ascii = ascii + lista[licznik]
            if ascii > 90:
                ascii = ascii - 26
            znak = chr(ascii)
            print(znak, end="")
            licznik = licznik +1

            if licznik >= len(lista):
                licznik = 0

encode("KOMPUTER", [50])

