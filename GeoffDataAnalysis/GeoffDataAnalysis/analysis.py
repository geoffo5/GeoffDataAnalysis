import json

def analyse(wordList):
    scores = {}
    with open("ea-thesaurus-lower.json") as fileLoad:
        file = json.load(fileLoad)
    for word in wordList:
        if word not in file:
            scores[word] = 'Word not Found'
        else:
            scores[word] = file[word][:3]
    print(scores)