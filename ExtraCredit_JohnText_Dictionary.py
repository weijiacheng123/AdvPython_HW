text = open('book_of_John_text.txt','r')
d = dict()
#d = { 1:'Father', 2:'God', 3:'Christ', 4:'Spirit', 5:'life', 6:'man' }

for line in text:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")

    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

for key in list(d.keys()):
    print(key, ":", d[key])

    