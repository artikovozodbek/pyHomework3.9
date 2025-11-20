f = open('asciLetters.txt', 'r')
matn = f.read()

matn_new = matn.title()

f2 = open('asciNumbers.txt', 'w')
f2.write(matn_new)
