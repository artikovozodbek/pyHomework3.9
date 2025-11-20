f = open('asciNumbers.txt', 'r')
sonlar = f.read().split()

for i in range(len(sonlar)):
    sonlar[i] = int(sonlar[i])

or1 = sum(sonlar) / len(sonlar)

print(or1)
