sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: ")) 
islem = input("Yapmak istediğiniz işlemi giriniz (+, -, /, *): ")

def hesapMakinesi(sayi1, sayi2, islem):
    if islem == '+':
        return print(f"{sayi1} {islem} {sayi2} = {sayi1 + sayi2}")
    elif islem == '-':
        return print(f"{sayi1} {islem} {sayi2} = {sayi1 - sayi2}")
    elif islem == '/':
        if sayi2 == 0:
            return print("Bölme işlemi için ikinci sayı 0 olamaz!" )
        return print(f"{sayi1} {islem} {sayi2} = {sayi1 / sayi2}")
    elif islem == '*':
        return print(f"{sayi1} {islem} {sayi2} = {sayi1 * sayi2}")
    else:
        return print("Geçersiz işlem türü!")


hesapMakinesi(sayi1, sayi2, islem)
