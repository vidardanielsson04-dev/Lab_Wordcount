document = ["He is in the room, she said."]

def tokenize(document):
    words = []
    for line in document:
        line = line.lower()
        i = 0
        while i < len(line):
            if line[i].isalpha():
                token = ""
                while i < len(line) and line[i].isalpha():
                    token += line[i]
                    i += 1
                words.append(token)

            elif line[i].isdigit():
                token = ""
                while i < len(line) and line[i].isdigit():
                    token += line[i]
                    i += 1
                words.append(token)

            elif line[i].isspace():
                i += 1

            else:  # skiljetecken
                words.append(line[i])
                i += 1

    return words


def countWords(words,stopWords):
    sorteradDic = {}
    i = 0
    while i < len(words):
        if words[i] in stopWords:
            i += 1
        elif words[i] not in sorteradDic:
            sorteradDic[words[i]] = 1
            i += 1
        elif words[i] in sorteradDic:
            i += 1

    return sorteradDic

    




print(tokenize(document))