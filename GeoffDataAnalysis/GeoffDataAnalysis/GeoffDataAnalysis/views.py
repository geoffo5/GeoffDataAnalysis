"""
Routes and views for the flask application.
"""
import re
from datetime import datetime
from flask import render_template, request, send_from_directory
from GeoffDataAnalysis import app
import nltk
from analysis import analyse
import hashlib
import hmac
import GeoffDataAnalysis.database


@app.route('/')
@app.route('/home')
def home():
   return render_template('index.html')

@app.route('/upload', methods = ['POST', 'GET'])
def upload():
    file = request.files['file']
    fileBytes = file.read()
    fileString = fileBytes.decode("latin-1")
    id = sha_hash = hashlib.sha256(bytes(fileString, encoding='utf-8')).hexdigest()
    fileExists = GeoffDataAnalysis.database.checkFileExists(id)
    if fileExists:
        analysed = GeoffDataAnalysis.database.retrieveFile(id)
    else:
        fileString = toLower(fileString)
        wordList = wordSplit(fileString)
        analysed = analyse(wordList, id)
    #for k in analysed['file']:
    #    print(k)
    return render_template('uploaded.html', fullFile = analysed)


def wordSplit(fileString):
    delimiters = [' ', ',', '.', '"', '#','/',"\\"]
    wordList = ['']
    i = 0
    for char in fileString:
        if char in delimiters:
            i = i + 1
            wordList.append('')
        else:
            wordList[i] = wordList[i] + char
    for word in wordList:
        if word == '':
            wordList.remove('')
    return wordList
            
def toLower(fileString):
    for char in fileString:
        fileString = fileString.lower()
        return fileString
            
        