metin = input('Şifrelenecek Metni Giriniz: ')
ilerleme_sayisi = int(input('İlerleme Sayısını Giriniz: '))


def sifrele(metin,ilerleme_sayisi):
    sonuc = ''
    for i in range(len(metin)):
        karakter = metin[i]

        if(karakter.isupper()):
            sonuc += chr((ord(karakter) + ilerleme_sayisi - 65) % 26 + 65)

        else:
            sonuc += chr((ord(karakter) + ilerleme_sayisi - 97) % 26 + 97)
        
    return sonuc

print("Girilen Metin : " + metin)
print("İlerleme Sayısı : " + str(ilerleme_sayisi))
print("Şifrelenmiş Metin : " + sifrele(metin,ilerleme_sayisi))

