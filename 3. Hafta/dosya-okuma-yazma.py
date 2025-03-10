filename = "data.txt"
filename2 = "data2.txt"

text = input("Bir metin girin: ")
with open(filename, "w") as file:
    file.write(text)

with open(filename, "r") as file:
    print("\nDosya İçeriği:")
    print(file.read())


print("\n5 satır giriniz:")
with open(filename2, "w") as file:
    for _ in range(5):
        file.write(input() + "\n")

with open(filename2, "r", encoding="utf-8") as file:
    print("\nDosyadaki Satırlar:")
    line = file.readline()
    while line:
        print(line.strip())  
        line = file.readline()