

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
    frequencies = {}
    i = 0
    while i < len(words):
        if words[i] in stopWords:
            i += 1
        elif words[i] not in frequencies:
            frequencies[words[i]] = 1
            i += 1
        elif words[i] in frequencies:
            frequencies[words[i]] += 1
            i += 1

    return frequencies


def printTopMost(frequencies,n):
    sorted_dic = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    i = 0
    while i < n and i < len(sorted_dic):
        key, value = sorted_dic[i]
        print(key.ljust(20) + str(value).rjust(5))
        i += 1
    
        



    



