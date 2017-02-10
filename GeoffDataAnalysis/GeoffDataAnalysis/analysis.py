import json
import database
import operator

def analyse(wordList, id):
    scores = {}
    temp = {}
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
                    temp.update(file[word][i])
                scores[word] = [1, temp]
                temp = {}
  
    database.addToDatabase(scores,id)
    scores = database.retrieveFile(id)
    return scores

def advancedAnalysis(file, assoc, id):
    keys = []
    scores = []
    temp = {}

    for k in file['basic'].keys():
        if file['basic'][k][1] == 'Word not Found':
            keys.append(k)
    for k in keys:
        del file['basic'][k]

    file = intConvert(file)
    
    for k in file['basic']:
        temp['word'] = k
        temp['freq'] = file['basic'][k][0]
        sortedList = sorted(file['basic'][k][1].items(), key=operator.itemgetter(1))
        temp['association'] = sortedList
        scores.append(temp)
        temp = {}
    database.updateDatabase(scores,id)
    file = database.retrieveFile(id)
    return file


def intConvert(file):
    for k in file['basic']:  
        for key in file['basic'][k][1]:
            file['basic'][k][1][key] = int(file['basic'][k][1][key])

    return file
            

                
    
 #if word not in file and word in scores and scores[word][1] == 'Word not Found':
        #    scores[word][0] = scores[word][0] + 1
        #elif word not in file:
        #    scores[word] = [1, 'Word not Found']
        #else:
        #    if word in scores:
        #        scores[word][0] = scores[word][0] + 1
        #    else:
        #        for i in range(0,3):
        #            temp.update(file[word][i])
        #        scores[word] = [1, temp]
        #        temp = {}