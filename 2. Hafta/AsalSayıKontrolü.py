sayi = int(input("Bir sayı giriniz: "))

def asalMi(sayi):
    for i in range(2, sayi):
        if sayi % i == 0:
            return False
    return True
            
sonuc = asalMi(sayi)


if sonuc == True:
    print(f"{sayi} bir asal sayıdır")
else:
    print(f"{sayi} bir asal sayı değildir")