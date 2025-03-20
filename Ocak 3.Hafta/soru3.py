num = int(input("Bir sayı giriniz : "))

faktoriyel = 1
for i in range(1, num + 1):
    faktoriyel *= i

print(f"{num}! = {faktoriyel}")
