import numpy as np

import sqlalchemy
#from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, String, Boolean, Column

from flask import Flask, jsonify, render_template, redirect, request
from  WordPlay import addWordToDB, WordObj
import re



connection_String = "postgres:drwho@localhost:5432/words"
engine = create_engine(f'postgresql://{connection_String}')
print(engine.table_names())

#Base = automap_base()

Base = declarative_base()
#Base.prepare(engine, reflect=True)


#	def __init__(self, newWord):
#		self.Word = newWord.Word
#		self.date = date
#		self.Definition = definition
#		self.Etymology = ety
#		self.Syllables = syl
#		self.Phonetic = pho
#		self.Offensive = offensive
	

def wordSearch(testWord):
	session = Session(engine)
	allwords =   session.query(WordObj).order_by(WordObj.Word).all()
	session.close()
	
	found = [row for row in allwords if row.Word.upper() == testWord.upper()]
	
	if len(found) == 0:
		result = None
		print("The word was not found")
		
	else:
		result = found[0]
		print("word was found in the list already")
	
	return result



app = Flask(__name__)


@app.route('/')
def get_data():
	
	
	allwords = []
	session = Session(engine)
	allwords =   session.query(WordObj).all()
	session.close()
	
	
	
	return render_template("index.html" ,words = allwords)



@app.route("/word_def/<newWord>")
def addWord(newWord):
	
	
	count = 0
	found = None
	print(newWord)
	
	while (count < 2) & (found == None):
		found = wordSearch(newWord)
		if found == None:
			print(f'Trying to add {newWord} to the database count - {count}')
			addWordToDB(newWord)
			count += 1
		

	allwords = []
	session = Session(engine)
	allwords =   session.query(WordObj).order_by(WordObj.Word).all()
	session.close()
	if found == None:
		return  render_template("index.html", words = allwords, msg = "Unable to add word")
	
	
	# need to look up the word see if it is in the current database or else look up from MW
	return render_template("word_def.html", word = found, words = allwords)
# %%

@app.route("/bubble")
def makeBubble():
	allwords = []
	session = Session(engine)
	allwords =   session.query(WordObj).order_by(WordObj.Word).all()
	
	
	etyWords = session.query(WordObj.Etymology, func.count(WordObj.Word)).group_by(WordObj.Etymology).all()
	
	results = []
	for row in etyWords:
		if row[0] is not None:
			if row[0] != "unknown":
				results.append([row[0],row[1]])
	session.close()
	
	return render_template("bubble.html", words = allwords, ety = results)






if __name__ == "__main__":
	app.run(debug=True)