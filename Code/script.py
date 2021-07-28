import numpy as np

import sqlalchemy
#from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, String, Boolean, Column

from flask import Flask, jsonify, render_template, redirect





connection_String = "postgres:drwho@localhost:5432/words"
engine = create_engine(f'postgresql://{connection_String}')
print(engine.table_names())

#Base = automap_base()

Base = declarative_base()
#Base.prepare(engine, reflect=True)

class WordObj(Base):
	__tablename__ = 'word_list'
	Word = Column(String(50), primary_key=True)
	Date = Column(String(50))
	Definition = Column(String(150))
	Etymology = Column(String(50))
	Syllables = Column(String(50))
	Phonetic = Column(String(50))
	Offensive = Column(Boolean)
	
	def __init__(self, word, date, definition, ety, syl, pho, offensive):
		self.Word = word
		self.date = date
		self.Definition = definition
		self.Etymology = ety
		self.Syllables = syl
		self.Phonetic = pho
		self.Offensive = offensive

#	def __init__(self, newWord):
#		self.Word = newWord.Word
#		self.date = date
#		self.Definition = definition
#		self.Etymology = ety
#		self.Syllables = syl
#		self.Phonetic = pho
#		self.Offensive = offensive
	





app = Flask(__name__)


@app.route('/')
def get_data():
	print("Hello")
	
	allwords = []
	session = Session(engine)
	for row in  session.query(WordObj):
		allwords.append(row)
				
	session.close()
	
	
	
	return render_template("index.html" ,words = allwords)



@app.route("/newWord")
def addWord(word):
	print(word)
# %%





if __name__ == "__main__":
	app.run(debug=True)