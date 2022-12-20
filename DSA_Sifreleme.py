import hashlib
import secrets
import decimal

def anahtar_uret():
    q = secrets.randbelow(250)
    p = secrets.randbelow(125)
    h = secrets.randbelow(249) + 1
    g = ((h * (p - 1)) / q) % p
    x = secrets.randbelow(q)
    y = (g * x) % p
    dizi = []
    dizi.append(p)
    dizi.append(q)
    dizi.append(g)
    dizi.append(x)
    dizi.append(y)

    return  dizi
    #Açık anahtar: 0:p 1:q 2:g 3:x 4:y
    #Özel anahtar: x


def imzala(mesaj='string', p=1 ,q=1 ,g=1 ,y=1, x=1):
    k = secrets.randbelow(q)
    r = ((g * k) % p) % q
    hashlenmis_mesaj = int(hashlib.sha1(mesaj.encode()).hexdigest(), 16)
    s = ((k -1) * ((hashlenmis_mesaj + (x * r)))) % q
    return s, r, hashlenmis_mesaj

def dogrula(r=1,s=1,q=1,hashlenmis_mesaj=123456,g=1, y=1, p=1):
    if 0<r<q or 0<s<q:
        while True:
            break

    w = decimal.Decimal(decimal.Decimal(pow(s, -1)) % q)
    u1 = decimal.Decimal(decimal.Decimal(hashlenmis_mesaj * w) % q)
    u2 = decimal.Decimal(r * w)
    v = decimal.Decimal((decimal.Decimal((pow(g, u1)) * decimal.Decimal(pow(y, u2))) % p) % q)
    if v == r:
        print('İmza kabul edildi')


a = anahtar_uret()
b = imzala('hello', a[0], a[1], a[2], a[3], a[4])
print(dogrula(b[1], b[0], a[1], b[2], a[2], a[4], a[0]))



'''
Sayıların ve hashlenmiş mesajın çok büyük olmasından dolayı python bu işlemi gerçekleştiremiyor
'''









