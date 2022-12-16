def vigenere_sifreleme(duz_metin, anahtar):
    anahtar_uzunluk = len(anahtar)
    anahtar_int = [ord(i) for i in anahtar]
    duz_metin_int = [ord(i) for i in duz_metin]
    sifreli_metin = ''
    for i in range(len(duz_metin_int)):
        deger = (duz_metin_int[i] + anahtar_int[i % anahtar_uzunluk]) % 26
        sifreli_metin += chr(deger + 65)
    return sifreli_metin

def vigenere_cozme(sifreli_metin, anahtar):
    anahtar_uzunluk = len(anahtar)
    anahtar_int = [ord(i) for i in anahtar]
    sifreli_metin_int = [ord(i) for i in sifreli_metin]
    duz_metin = ''
    for i in range(len(sifreli_metin_int)):
        deger = (sifreli_metin_int[i] - anahtar_int[i % anahtar_uzunluk]) % 26
        duz_metin += chr(deger + 65)
    return duz_metin

if __name__ == '__main__':
    print('Şifreleme için : 1')
    print('Çözme için : 2')
    sayi = int(input("Değer giriniz: "))
    if sayi == 1:
        duz_metin = input("Metin(Lütfen büyük harf kullanın) : ")
        anahtar = input("Anahtar(Lütfen büyük harf kullanın) : ")
        sifreli_metin = vigenere_sifreleme(duz_metin, anahtar)
        print('Sonuc: ',sifreli_metin)

    elif sayi == 2:
        sifreli_metin = input("Şifreli Metin(Lütfen büyük harf kullanın) : ")
        anahtar = input("Anahtar(Lütfen büyük harf kullanın) : ")
        cozulen_duz_metin = vigenere_cozme(sifreli_metin, anahtar)
        print('Sonuc:',cozulen_duz_metin)

