import json

def analyse(wordList, id):
    scores = {}
    temp = []
    file = {}
    with open("ea-thesaurus-lower.json") as fileLoad:
        file = json.load(fileLoad)

   
    for word in wordList:
        if word not in file and word in scores and scores[word][1] == 'Word not Found':
            scores[word][0] = scores[word][0] + 1
        elif word not in file:
            scores[word] = [1, 'Word not Found']
        else:
            if word in scores:
                scores[word][0] = scores[word][0] + 1
            else:
                for i in range(0,3):
                    temp.append(file[word][i])
                scores[word] = [1, temp]
                temp = []
    print(scores)