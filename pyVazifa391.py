
f = open("asciNumbers.txt", "r")
numbers = f.read().split()

sentence = ""

for i in numbers:
    sentence += chr(int(i))


f2 = open("asciLetters.txt", "w")
f2.write(sentence)
