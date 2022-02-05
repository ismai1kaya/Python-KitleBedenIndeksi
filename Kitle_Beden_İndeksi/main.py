print("<<<Kitle Beden İndeksi Hesaplama>>>")

kilo = int(input(("Kilonuzu Giriniz(Örn. 75Kg):")))
boy = float(input("Boyunuzu Giriniz(Örn. 1.81m):"))
indeks = kilo / (boy ** 2)

if (indeks < 18.5):
    print("Zayıf\nİndeksiniz= {}".format(indeks))
elif (indeks>= 18.5 and indeks < 25):
    print("Normal\nİndeksiniz= {}".format(indeks))
elif (indeks >= 25 and indeks < 30):
    print("Fazla Kilolu\nİndeksiniz= {}".format(indeks))
else:
    print("Obez\nİndeksiniz= {}".format(indeks))