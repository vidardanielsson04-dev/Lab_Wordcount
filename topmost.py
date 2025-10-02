import wordfreq
import sys
import urllib.request


def main():
    
    stopfile = sys.argv[1]
    link = sys.argv[2]
    n = int(sys.argv[3])

    stopwords = []
    for line in open(stopfile, encoding="utf-8"):
        stopwords.append(line.strip())

    if link.startswith("http://") or link.startswith("https://"):
        response = urllib.request.urlopen(link)
        text = response.read().decode("utf8")
    else:
        with open(link, encoding="utf-8") as f:
            text = ""
            for line in f:
                text += line

    
    dokument = text.splitlines()
    words = wordfreq.tokenize(dokument)

    frequencies = wordfreq.countWords(words,stopwords)

    print(wordfreq.printTopMost(frequencies, n))


main()
        