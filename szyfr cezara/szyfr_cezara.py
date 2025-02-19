import re

chars = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i' ,'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż']


choice = input("Chcesz szyfrować(szyfruj) czy deszyfrować(deszyfruj) ciąg znaków?").strip().lower()



def przesun_o_klucz(znak, key):
    if znak in chars:
        index = chars.index(znak)
        new_index = (index + key) % len(chars)
        return chars[new_index]
    else:
        return znak
    
def cofnij_o_klucz(znak, key):
    if znak in chars:
        index1 = chars.index(znak)
        new_index1 = (index1 - key) % len(chars)
        return chars[new_index1]
    else:
        return znak
    

if choice == 'szyfruj':
    tekst = input("Podaj tekst do zaszyfrowania")
    key = int(input("Podaj wartość klucza (liczba całkowita)"))
    tekst = tekst.lower()
    cleaned_tekst = re.sub(r'[!?,.\s]', '', tekst)
    zaszyfruj = ''.join(przesun_o_klucz(znak, key) for znak in cleaned_tekst)
    print("Ciąg znaków po zaszyfrowaniu:", zaszyfruj)
elif choice == 'deszyfruj':
    tekst = input("Podaj tekst do deszyfrowania")
    key = int(input("Podaj wartość klucza (liczba całkowita)"))
    tekst = tekst.lower()
    cleaned_tekst = re.sub(r'[!?,.\s]', '', tekst)
    odszyfruj = ''.join(cofnij_o_klucz(znak, key) for znak in cleaned_tekst)
    print("Odszyfrowany tekst:", odszyfruj)
else:
    print("Nieprawidłowa opcja. Wybierz 'szyfruj' lub 'deszyfruj'.")