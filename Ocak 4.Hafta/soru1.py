# 1. yol
liste = []

for i in range(5):
    num = int(input("Bir sayı giriniz : "))
    liste.append(num)

print(f"Toplam : {sum(liste)}")
print(f"Ortalama : {sum(liste) / len(liste)}")
print(f"En büyük sayı : {max(liste)}")
print(f"En küçük sayı : {min(liste)}")


#----------------------------------------------------------
# 2. yol

toplam = 0
for i in liste:
    toplam += i

en_buyuk = liste[0]
en_kucuk = liste[0]

for i in liste:
    if i > en_buyuk:
        en_buyuk = i
    if i < en_kucuk:
        en_kucuk = i


print(f"Toplam : {toplam}")
print(f"Ortalama : {toplam / len(liste)}")
print(f"En büyük sayı : {en_buyuk}")
print(f"En küçük sayı : {en_kucuk}")