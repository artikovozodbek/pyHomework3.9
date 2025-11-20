soz = input("So'ni kiriting: ").lower()

f = open('asciNumbers.txt', 'r')

matn = f.read()

if soz in matn:
    print("Bor")
else:
    print("Yoq")