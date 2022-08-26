alfabe1 = {
    '0' : 'AA', 'Y' : 'AD', 'P' : 'AF', 'E' : 'AG', '3' : 'AV', 'J' : 'AX',
    'N' : 'DA', 'W' : 'DD', 'A' : 'DF', 'X' : 'DG', 'I' : 'DV', 'C' : 'DX',
    'Q' : 'FA', '2' : 'FD', '6' : 'FF', 'Z' : 'FG', 'G' : 'FV', 'L' : 'FX',
    '1' : 'GA', '7' : 'GD', 'S' : 'GF', 'D' : 'GG', 'F' : 'GV', '9' : 'GX',
    'V' : 'VA', 'U' : 'VD', '4' : 'VF', 'R' : 'VG', '8' : 'VV', 'T' : 'VX',
    'B' : 'XA', '5' : 'XD', 'H' : 'XF', 'M' : 'XG', 'K' : 'XV', 'O' : 'XX',
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