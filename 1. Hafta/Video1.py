print("Kodlama.io")

baslik = "Taşıt Kredisi"
print(baslik)

#string => metinsel ifade 
baslik = "İhtiyaç Kredisi"
print(baslik)

#int, integer => tam sayı 
vade = 36
ekVade = 6
vade2 = "36"

#float, decimal, double => ondalıklı sayı
aylikOdeme = 200.50

#bool, boolean => True, False
yukselisteMi = False

#matematiksel opeatörler

#  +
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)

#  -
print(5 - 5)
print(vade - 12)
print(vade - ekVade)
print(36 - 6)

#  *
print(5 * 5)
print(vade * 12)
print(vade * ekVade)
print(10 * 10)

#  /
print(5 / 5)
print(vade / 12)
print(vade / ekVade)
print(10 / 2)

yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % => mod operatörü
print(10 % 2)
print(vade % 5)
print(vade % ekVade)

# mantıksal operatörler
print(1 == 2)

# CTRL K + C => toplu yorum satırı
print(1 > 2)
print(3 > 1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)


print(1 != 1)
print(1 != 2)

# or and

# or => veya
print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)

print(1 > 2 and 5 > 2 and 3 > 2)

print(2 > 1 or 1 > 2 and 3 > 2)


# karar yapıları
# if - else
sayi1 = 10
sayi2 = 15

# sayi1 sayi2 den büyükse ekrana sayi1 daha büyük yazdır
# condition (durum, koşul)

# indent (girinti)

if sayi1 <= sayi2:
    print("Sayi1 Sayi2 den küçüktür")
elif sayi1 == sayi2:
    print("Sayi1 Sayi2 ye eşittir")
else:
    print("Sayi1 Sayi2 den büyüktür")


if sayi1 <= sayi2:
    print("Sayi1 Sayi2 den küçüktür")
if  sayi1 == sayi2:
    print("Sayi1 Sayi2 ye eşittir")
else:
    print("Sayi1 Sayi2 den büyüktür")