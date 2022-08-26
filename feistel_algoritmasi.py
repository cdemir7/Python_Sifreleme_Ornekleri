import random as rd

def keyOlustur(a):

    import random as rd
    key1 = ''
    for i in range(a):  
        gecici = rd.randint(0,1)
        gecici = str(gecici)
        key1 += gecici

    return(key1)

def gecisFonksiyonu(a,b):
    gecici = ''
    for i in range(uzunluk1):
        if(a[i] == 1 or b[i] ==1):
            gecici += 1

        else:
            gecici += 0

    return gecici

def xorFonksiyonu(a,b):
    gecici = ''
     
    for i in range(uzunluk1):
         
        if (a[i] == b[i]):
            gecici += "0"
             
        else:
            gecici += "1"
             
    return gecici

sayi = input("Binary Sayı Giriniz: ")
sayiDizisi = []

for i in sayi:
    sayiDizisi.append(i)

uzunluk = len(sayiDizisi)
uzunluk1 = int(uzunluk / 2)
l1 = sayiDizisi[0 : uzunluk1]
r1 = sayiDizisi[uzunluk1 :: ]

K1 = keyOlustur(uzunluk)
K2 = keyOlustur(uzunluk)

f1 = xorFonksiyonu(r1,K1)
r2 = xorFonksiyonu(f1,l1)
l2 = r1

f2 = xorFonksiyonu(r2,K2)
r3 = xorFonksiyonu(f2,l2)
l3 = r2

veri = l3 + r3
print(veri)