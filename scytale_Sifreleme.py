cevrilecek_metin = input("Şifrelenecek Metni Giriniz(Metindeki Karakter Sayısı 4'ün Katı Olmalı): ")

def sifreleme(cevrilecek_metin):
    gecici_dizi = []
    for i in range(0,len(cevrilecek_metin),4):
        parcalanmis_metin = cevrilecek_metin[i : i + 4]
        a,b,c,d = parcalanmis_metin
        gecici_dizi.append(d+c+a+b)
    print("Şifrelenmiş Metin:")
    gecici_dizi = "".join(gecici_dizi).split()[-1]
    print(gecici_dizi)
    # for i in gecici_dizi:
    #     print(i)

sifreleme(cevrilecek_metin)