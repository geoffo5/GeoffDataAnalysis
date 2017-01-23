"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from GeoffDataAnalysis import app

@app.route('/')
@app.route('/home')
def home():
   