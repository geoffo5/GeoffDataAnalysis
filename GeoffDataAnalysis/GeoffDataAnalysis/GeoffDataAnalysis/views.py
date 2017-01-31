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

app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'rtf'])
app.config['UPLOAD_FOLDER'] = 'C:\ServerFiles'


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
    
    fileString = toLower(fileString)
    wordList = wordSplit(fileString)
    analyse(wordList, id)
    return render_template('uploaded.html')


def wordSplit(fileString):
    delimiters = [' ', ',', '.', '"', '#']
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
            
        