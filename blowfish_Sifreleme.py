from Crypto.Cipher import Blowfish

cipher = Blowfish.new("(Anahtar boyutu 4 ile 56 bayt aralığında olmalı: ")
duz_metin = input("Şifrelenecek metni Giriniz:")
sifreli_veri = cipher.encrypt(duz_metin)
print("Düz Metin: {} ".format(duz_metin))
print("Şifrelenmiş Metin: {} ".format(sifreli_veri))