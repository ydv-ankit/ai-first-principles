def buildVocabulary(f: str) -> dict:
    # read file
    # split words by <space> and put them in a dictionary 
    # with value as next word with a counter
    voc = dict()
    with open('data/doc.txt') as file:
        content = file.read()
        nl = content.split('\n')
        for l in nl:
            words = l.split(' ')
            for i in range(len(words) - 1):
                if words[i] not in voc.keys():
                    voc[words[i]] = dict()
                if words[i + 1] not in voc[words[i]].keys():
                    voc[words[i]][words[i + 1]] = 1
                else:
                    voc[words[i]][words[i + 1]] += 1

    return voc

def predictNextWord(vocab: dict, currentWord: str) -> str:
    if currentWord not in vocab:
        return None
    values = vocab[currentWord]
    nextWord = ''
    maxValue = 0
    for k in values:
        if values[k] > maxValue:
            nextWord = k
            maxValue = values[k]
    return nextWord

def sampling():
    fileToRead = 'data/doc.txt'
    vocab = buildVocabulary(fileToRead)
    print(vocab)
    nextWord = 'I'
    while True:
        print(nextWord, end=' ')
        nextWord = predictNextWord(vocab, nextWord)
        if nextWord is None:
            break
    

if __name__ == "__main__":
    sampling()
