# = förklaring av korden
### = förslag på ändring / tankar kring korden
document = ['''Francis Albert Sinatra, nicknamed the "Chairman of the Board" and "Ol' Blue Eyes", was an American singer and actor. He is regarded as one of the most popular entertainers of the 20th century. He is among the world's best-selling music artists, with an estimated 150 million record sales globally.''']
words = []
def tokenize(document):
    for line in document:
        line = line.lower()
        i = 0
        while i < len(line):
            ch = line[i]
            if ch.isalpha() or ch.isdigit():
                token = ch
                i += 1
                while i < len(line) and (line[i].isalpha() or line[i].isdigit() or (line[i] == "'" and line[i+1].isalpha())): #om bokstav, om nummer eller om ' följt av bokstav
                    token += line[i]
                    i += 1
                words.append(token)
            else:
                i += 1
    return words


def countWord(words):
    tokenize(document)
    i = 0
    n = 0
    nyLista = []
    vardeLista = []
    slutLista = [] ###går det att göra med mindre antal listor?
    while i < len(words):
        if words[i] not in nyLista: #om nytt ord >
            nyLista.append(words[i]) #lägg till ord i ny lista
            vardeLista.append(1) # lägg till nytt element med värde 1
        elif words[i] in nyLista: #om ordet redan finns >
            n = nyLista.index(words[i]) #finn platsen i nyLista där ordet finns
            vardeLista[n] += 1 #öka värdet i vardelista på den plats där orden befinner sig 
            ###finns count funktion som kanske hade varit snyggare
        i += 1
    i = 0
    while i < len(nyLista):
        slutLista.append(str(nyLista[i]) + ' : ' + str(vardeLista[i])) #lägger ihop orden med dess värden   ###nested list istället?
        i += 1
    return slutLista
print(countWord(words))