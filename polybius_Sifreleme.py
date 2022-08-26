alfabe1 = {
    'A' : '11','B' : '12', 'C' : '13', 'D' : '14', 'E' : '15',
    'F' : '21','G' : '22', 'H' : '23', 'I' : '24', 'J' : '24', 'K' : '25',
    'L' : '31','M' : '32', 'N' : '33', 'O' : '34', 'P' : '35',
    'Q' : '41','R' : '42', 'S' : '43', 'T' : '44', 'U' : '45',
    'V' : '51','W' : '52', 'X' : '53', 'Y' : '54', 'Z' : '55'
}

metin = input('Şifrelemek İstediğiniz Cümleyi Giriniz: ')
print("Girilen Metin : " + metin)
metin = metin.upper()

harfListesi = list(metin)
uzunluk = len(harfListesi)
sonuc = ''

i = 0
while(i < uzunluk):
    if(harfListesi[i] == " "):
        i += 1
    
    sonuc += alfabe1[harfListesi[i]]    
    i += 1

print("Şifrelenmiş Metin : "+ sonuc)

    