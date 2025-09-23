# = förklaring av korden
### = förslag på ändring / tankar kring korden
document = ['''x-ray Francis Albert Sinatra, nicknamed the "Chairman of the Board" and "Ol' Blue Eyes", was an American singer and actor. He is regarded as one of the most popular entertainers of the 20th century. He is among the world's best-selling music artists, with an estimated 150 million record sales globally.''']
words = []
def tokenize(document): #metod för att definera vad som är ett ord och skapa en lista med alla ord
    for line in document:
        line = line.lower()
        i = 0
        while i < len(line):
            ch = line[i]
            if ch.isalpha() or ch.isdigit():
                token = ch
                i += 1
                while i < len(line) and (line[i].isalpha() or line[i].isdigit() or (line[i] == "'" and line[i+1].isalpha()) or (line[i] == "-" and line[i+1].isalpha())): #om bokstav, om nummer eller om ' eller - följt av bokstav, så att även don't och x-ray räknas som ord
                    token += line[i]
                    i += 1
                words.append(token)
            else:
                i += 1
    return words


def countWord(words): #metod för att räkna och sortera orden
    tokenize(document)
    i = 0
    n = 0
    nyLista = []
    vardeLista = []
    slutDic = {} #skapar en dictionary
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
    while i < len(nyLista): #lägger ihop ord och värde listan i en gemensam dictionary
        slutDic[nyLista[i]] = vardeLista[i] #ord [i] får värdet av värdelista[i]
        i += 1 
    sorteradDic = sorted(slutDic.items(), key=lambda x:x[1], reverse=True) #sorterar dictionary, (x:x[1]) innebär att vi sorterar efter det andra elementet dvs int, x:x[0] hade sorterat efter bokstav istället.
    return sorteradDic #reverse=True ovan är för att den annars sorterar efter minsta värde först
print(countWord(words))

### vi bör kanske sortera efter bokstav på de ord som finns lika många gånger, fråga läraren. isåfall förslagsvis i första metoden alltså innan counting
### vi behöver också ta bort ord "stopwords" förslagsvis vid början av counting
### fråga om vi behöver ha med nummer som ord

### sedan ska vi skapa en snyggare print i en ny metod
