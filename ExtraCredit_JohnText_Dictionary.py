text = open('book_of_John_text.txt','r')
#d = dict()
d = {'Father':0, 'God':0, 'Christ':0, 'Spirit':0, 'life':0, 'man':0}

for line in text:
    line = line.strip()
    words = line.split(" ")

    for word in words:
        #print(word)
        if word in d:
            d[word] += 1

for key in list(d.keys()):
    print(key, ":", d[key])