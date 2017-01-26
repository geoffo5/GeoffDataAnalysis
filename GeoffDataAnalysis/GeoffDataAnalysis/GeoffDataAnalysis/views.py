"""
Routes and views for the flask application.
"""
import re
from datetime import datetime
from flask import render_template, request, send_from_directory
from GeoffDataAnalysis import app

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
    fileString = fileBytes.decode("utf-8")
    print(type(fileString))
    wordList = wordSplit(fileString)
    return render_template('uploaded.html', file=file)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

def wordSplit(fileString):
    delimiters = [' ', ',', '.']
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

    print(wordList)
            
            
        