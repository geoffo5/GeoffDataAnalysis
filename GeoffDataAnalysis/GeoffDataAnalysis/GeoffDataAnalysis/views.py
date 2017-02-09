"""
Routes and views for the flask application.
"""
import re
from datetime import datetime
from flask import render_template, request, send_from_directory, session
from GeoffDataAnalysis import app
import nltk
import analysis
import hashlib
import hmac
import database
import operator
import json

app.secret_key = "MySecretKey"

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
    fileExists = database.checkFileExists(id)
    if fileExists:
        analysed = database.retrieveFile(id)
    else:
        fileString = toLower(fileString)
        wordList = wordSplit(fileString)
        analysed = analysis.analyse(wordList, id)
    session['file'] = id
    return render_template('uploaded.html', fullFile = analysed)

@app.route('/advanced', methods=['POST'])
def advanced():
    id = session['file']
    file = database.retrieveFile(id)
    assoc = request.form['assoc']
    assoc = int(assoc)
    file = analysis.advancedAnalysis(file, assoc, id)
    file = getCorrectAssociation(file['advanced'], assoc)
    print(file)
    return render_template('advanced.html', fullFile = file)


def wordSplit(fileString):
    delimiters = [' ', ',', '.', '"', '#','/',"\\"]
    specialChars = ['\r','\n']
    wordList = ['']
    i = 0
    for char in fileString:
        if char in delimiters:
            i = i + 1
            wordList.append('')
        elif char in specialChars:
            i
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

def getCorrectAssociation(file, assoc):
    for d in file:
        d['association'] = d['association'][assoc]     
    for d in file:
        d['rank'] = d['freq'] * d['association'][1]
    file = sorted(file, reverse = True, key = operator.itemgetter('rank'))
    return file

            
        