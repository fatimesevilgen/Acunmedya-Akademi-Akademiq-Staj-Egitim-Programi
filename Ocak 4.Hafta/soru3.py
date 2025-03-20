liste = ["a" , "b" , "a" , "d" , "a" , "c" , "d"]
#print(set(liste))  tuple kullanılarak da yapılabilir

newList = []
for i in liste:
    if i not in newList:
        newList.append(i)
print(newList)