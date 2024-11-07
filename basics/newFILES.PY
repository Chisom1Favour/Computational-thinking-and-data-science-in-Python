nameHandle = open('kids', 'a')
nameHandle.write('Michael\n')
nameHandle.write('Zoba\n')
nameHandle.close()
nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line[:-1])
nameHandle.close()
