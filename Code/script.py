import numpy as np

import sqlalchemy
#from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, String, Boolean, Column

from flask import Flask, jsonify, render_template, redirect, request
from  WordPlay import addWordToDB, WordObj




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
	allwords =   session.query(WordObj).all()
	session.close()
	
	found = [row for row in allwords if row.Word == testWord]
	
	if len(found) == 0:
		result = None
		
	else:
		result = found[0]
	
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
		if found != None:
			addWordToDB(newWord)
			count += 1
		

	allwords = []
	session = Session(engine)
	allwords =   session.query(WordObj).all()
	session.close()
	
	# need to look up the word see if it is in the current database or else look up from MW
	return render_template("word_def.html", word = found, words = allwords)
# %%





if __name__ == "__main__":
	app.run(debug=True)