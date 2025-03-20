asal = True

for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            asal = False
            break
    if asal:
        print(i)
    asal = True
