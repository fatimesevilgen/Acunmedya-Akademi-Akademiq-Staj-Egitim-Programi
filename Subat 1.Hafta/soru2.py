kelime = input("Bir kelime giriniz : ")
tersi = kelime[::-1]
if kelime == tersi:
    print("Bu kelime palindromik bir kelimedir.")

else:
    print("Bu kelime palindromik bir kelime değildir.")