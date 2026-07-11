import math
import random

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

def predictNextWord(vocab: dict, currentWord: str) -> dict:
    if currentWord not in vocab:
        return None
    values = vocab[currentWord]
    totalValue = 0
    for v in values.values():
        totalValue += v
    probs = {}
    for k in values:
        probs[k] = values[k]/totalValue
    return probs

def sampleNextWord(probs: dict):
    rn = random.random()
    cummProb = 0
    for k in probs:
        val = probs[k]
        cummProb += val
        if rn <= cummProb:
            return k
    return None

def sampling():
    fileToRead = 'data/doc.txt'
    vocab = buildVocabulary(fileToRead)
    print(vocab)
    nextPredictedWord = 'I'
    print(nextPredictedWord, end = ' ')
    while True:
        nextValueProbs = predictNextWord(vocab, nextPredictedWord)
        # print(nextValueProbs)
        if nextValueProbs is not None:
            nextPredictedWord = sampleNextWord(nextValueProbs)
            print(nextPredictedWord, end = ' ')
        else:
            break
    

if __name__ == "__main__":
    sampling()
