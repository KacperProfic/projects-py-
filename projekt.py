import re


alphabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźżqxv"


def przesun_o_klucz(znak, key):
    if znak in alphabet:
        index = alphabet.index(znak)
        new_index = (index + key) % len(alphabet)
        return alphabet[new_index]
    else:
        return znak

def cofnij_o_klucz(znak, key):
    if znak in alphabet:
        index = alphabet.index(znak)
        new_index = (index - key) % len(alphabet)
        return alphabet[new_index]
    else:
        return znak

def caesar_encrypt(text, key):
    text = re.sub(r'[!?,.\s]', '', text.lower())
    return ''.join(przesun_o_klucz(char, key) for char in text)

def caesar_decrypt(text, key):
    text = re.sub(r'[!?,.\s]', '', text.lower())
    return ''.join(cofnij_o_klucz(char, key) for char in text)


def vigenere_encrypt(text, key):
    text = re.sub(r'[!?,.\s]', '', text.lower())
    key = re.sub(r'[!?,.\s]', '', key.lower())
    encrypted_text = []
    key_length = len(key)
    key_indices = [alphabet.index(k) for k in key]

    for i, char in enumerate(text):
        if char in alphabet:
            text_index = alphabet.index(char)
            key_index = key_indices[i % key_length]
            new_index = (text_index + key_index) % len(alphabet)
            encrypted_text.append(alphabet[new_index])
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text)

def vigenere_decrypt(text, key):
    text = re.sub(r'[!?,.\s]', '', text.lower())
    key = re.sub(r'[!?,.\s]', '', key.lower())
    decrypted_text = []
    key_length = len(key)
    key_indices = [alphabet.index(k) for k in key]

    for i, char in enumerate(text):
        if char in alphabet:
            text_index = alphabet.index(char)
            key_index = key_indices[i % key_length]
            new_index = (text_index - key_index) % len(alphabet)
            decrypted_text.append(alphabet[new_index])
        else:
            decrypted_text.append(char)

    return ''.join(decrypted_text)


def generuj_tablice_klucza(klucz):
    klucz_unikalny = ''.join(dict.fromkeys(klucz))
    tablica = klucz_unikalny + ''.join([c for c in alphabet if c not in klucz_unikalny])
    tablica2D = [list(tablica[i:i + 7]) for i in range(0, len(tablica), 7)]
    return tablica2D

def znajdz_pozycje(znak, tablica):
    for i, row in enumerate(tablica):
        if znak in row:
            return i, row.index(znak)
    return -1, -1

def przygotuj_tekst_playfair(tekst):
    tekst = re.sub(r'[^' + alphabet + r']', '', tekst.lower())
    return tekst

def szyfruj_playfair(tekst, klucz):
    tablica = generuj_tablice_klucza(klucz)
    tekst = przygotuj_tekst_playfair(tekst)
    szyfrowany = []

    i = 0
    while i < len(tekst):
        l1 = tekst[i]
        l2 = tekst[i + 1] if i + 1 < len(tekst) else 'x'

        if l1 == l2:
            l2 = 'y' if l1 == 'x' else 'x'

        r1, k1 = znajdz_pozycje(l1, tablica)
        r2, k2 = znajdz_pozycje(l2, tablica)

        if r1 == r2:  
            szyfrowany.append(tablica[r1][(k1 + 1) % 7])
            szyfrowany.append(tablica[r2][(k2 + 1) % 7])
        elif k1 == k2:  
            szyfrowany.append(tablica[(r1 + 1) % 5][k1])
            szyfrowany.append(tablica[(r2 + 1) % 5][k2])
        else:  
            szyfrowany.append(tablica[r1][k2])
            szyfrowany.append(tablica[r2][k1])

        i += 2

    return ''.join(szyfrowany)

def deszyfruj_playfair(tekst, klucz):
    tablica = generuj_tablice_klucza(klucz)
    odszyfrowany = []

    i = 0
    while i < len(tekst):
        l1 = tekst[i]
        l2 = tekst[i + 1] if i + 1 < len(tekst) else 'x'

        r1, k1 = znajdz_pozycje(l1, tablica)
        r2, k2 = znajdz_pozycje(l2, tablica)

        if r1 == r2:  
            odszyfrowany.append(tablica[r1][(k1 - 1) % 7])
            odszyfrowany.append(tablica[r2][(k2 - 1) % 7])
        elif k1 == k2:  
            odszyfrowany.append(tablica[(r1 - 1) % 5][k1])
            odszyfrowany.append(tablica[(r2 - 1) % 5][k2])
        else:  
            odszyfrowany.append(tablica[r1][k2])
            odszyfrowany.append(tablica[r2][k1])

        i += 2

    return ''.join(odszyfrowany)


def main():
    while True:
        print("\nWybierz szyfr:")
        print("1. Szyfr Cezara")
        print("2. Szyfr Vigenère'a")
        print("3. Szyfr Playfair")
        print("4. Wyjście")
        choice = input("Wybierz opcję (1-4): ").strip()

        if choice == '1':
            action = input("Wybierz: 'szyfruj' lub 'deszyfruj': ").strip().lower()
            text = input("Podaj tekst: ")
            key = int(input("Podaj klucz (liczba całkowita): "))
            if action == 'szyfruj':
                print("Zaszyfrowany tekst:", caesar_encrypt(text, key))
            elif action == 'deszyfruj':
                print("Odszyfrowany tekst:", caesar_decrypt(text, key))
            else:
                print("Nieprawidłowa opcja.")

        elif choice == '2':
            action = input("Wybierz: 'szyfruj' lub 'deszyfruj': ").strip().lower()
            text = input("Podaj tekst: ")
            key = input("Podaj klucz (ciąg znaków): ")
            if action == 'szyfruj':
                print("Zaszyfrowany tekst:", vigenere_encrypt(text, key))
            elif action == 'deszyfruj':
                print("Odszyfrowany tekst:", vigenere_decrypt(text, key))
            else:
                print("Nieprawidłowa opcja.")

        elif choice == '3':
            action = input("Wybierz: 'szyfruj' lub 'deszyfruj': ").strip().lower()
            text = input("Podaj tekst: ")
            key = input("Podaj klucz (ciąg znaków): ")
            if action == 'szyfruj':
                print("Zaszyfrowany tekst:", szyfruj_playfair(text, key))
            elif action == 'deszyfruj':
                print("Odszyfrowany tekst:", deszyfruj_playfair(text, key))
            else:
                print("Nieprawidłowa opcja.")

        elif choice == '4':
            
            break

        else:
            print("Nieprawidłowa opcja. Wybierz ponownie.")

if __name__ == "__main__":
    main()