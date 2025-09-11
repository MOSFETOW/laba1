
intAndString = [5, 12, 3, 18,"patient", 7, 22, "neck",1, 9, 14, 30, 
           "writer","attitude","manage","video","source","laboratory","reservoir","modest"]

intList = []

for x in intAndString:
    if isinstance(x, int):
        intList.append(x)

intList.sort()

strList = []

for x in intAndString:
    if isinstance(x, str):
        strList.append(x)


strList.sort()


sortedList = intList + strList


evenList = []

for x in intList:
    if x % 2 == 0:
        evenList.append(x)
        

upperStrList = []

for x in strList:
        upperStrList.append(x.upper())

print("спочатку числа потім далі рядки:",sortedList)


print("список чисел кратних 2:",evenList)


print("список значень у капсі:",upperStrList)
