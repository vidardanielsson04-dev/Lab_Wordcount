import wordfreq
import sys

def main():
    stopfile = sys.argv[1]
    textfile = sys.argv[2]
    n = int(sys.argv[3])

    stopwords = []
    for line in open(stopfile, encoding="utf-8"):
        stopwords.append(line.strip())

    words = wordfreq.tokenize(open(textfile, encoding="utf-8"))

    frequencies = wordfreq.countWords(words,stopwords)

    print(wordfreq.printTopMost(frequencies, n))


main()
        