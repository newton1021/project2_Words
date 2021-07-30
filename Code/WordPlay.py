# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Dependencies

import requests
import json
from random_word import RandomWords
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

import config

Base = declarative_base()

from wordMaker import welcome_to_dict, welcome_from_dict

#======================
words = set()
words_df = pd.DataFrame(columns=['Word','Definition', 'Etymology', 'Part_of_Speech', 'Date', 'Syllables', 'Phonetic', 'Offensive'])



# %%
wordGenerator = RandomWords()


class WordObj(Base):
    __tablename__ = 'word_list'
    Word = Column(String(50), primary_key=True)
    Date = Column(String(50))
    Definition = Column(String(150))
    Part_of_Speech = Column(String(50))
    Etymology = Column(String(50))
    Syllables = Column(String(50))
    Phonetic = Column(String(50))
    Offensive = Column(Boolean)
    
    def __init__(self, word, date, definition, pos, ety, syl, pho, offensive):
        self.Word = word
        self.Date = date
        self.Part_of_Speech = pos
        self.Definition = definition
        self.Etymology = ety
        self.Syllables = syl
        self.Phonetic = pho
        self.Offensive = offensive
        


# %%
# URL for GET requests to retrieve vehicle datawor


def dictionary(test_word):
    url = "https://www.dictionaryapi.com/api/v3/references"
    return (f'{url}/collegiate/json/{test_word}?key={config.API_KEY_Dictionary}')



# %%
# Pretty print JSON for all launchpads
def lookupWord(word):
        
    result = None
    
    word_url = dictionary(word)
#    print(word_url)
    response = requests.get(word_url).text
#    newWordObj = welcome_from_dict(json.loads(response))
    try: 
        newWordObj = welcome_from_dict(json.loads(response))
    except Exception as e:
        print(e)
        print(response)
        return result
    
    
    try:
        short_def = newWordObj[0].shortdef[0]
    except:
        short_def = "no definition"
    try: 
        temp = newWordObj[0].meta.id
        temps = temp.split(":")
        word_id = temps[0]
    except:
        word_id = ""
        return result
        
        
    try: 
        temp = newWordObj[0].et[0][1]
        tempL = temp.split(" {it}")
        ety = tempL[0]
    except:
        ety = "unknown"
    try: 
        pos = str(newWordObj[0].fl.value)
    except:
        pos = ""
    try: 
        date = newWordObj[0].date
    except:
        date = ""
    try: 
        syl = newWordObj[0].hwi.hw #['hwi']['hw']
    except: 
        syl =""
    try: 
        phn = newWordObj[0].hwi.prs[0].mw #['hwi']['prs'][0]['mw']
    except:
        phn = ""
    try:
        offensive = newWordObj[0].meta.offensive #response[0]['meta']['offensive']
    except:
        offensive = False
    try:
#        self, word, date, definition, pos, ety, syl, pho, offensive
#        print(f'date: {date}')
        newWord = WordObj(word_id, date, short_def, pos, ety, syl, phn, offensive)
        
    except:
        return result
    return newWord


def getDatabase():
    connection_String = "postgres:drwho@localhost:5432/words"
    engine = create_engine(f'postgresql://{connection_String}')
    session = Session(engine)
    allwords =   session.query(WordObj).all()
    session.close()    
    
    
    newData = []
    dirty = False
    for (i,word) in enumerate( allwords):
        temp = word.Word.split(":")
        if len(temp) > 0:
            dirty = True
            word = temp[0]
            allwords[i].Word = word
            
    word_df = pd.DataFrame(allwords)
    
    if dirty:
        saveDatabase(word_df)
    
    
    

def saveDatabase(df):
    connection_String = "postgres:drwho@localhost:5432/words"
    engine = create_engine(f'postgresql://{connection_String}')
    
    
    df.to_sql(name="word_list", con=engine, if_exists="append", index=False)
    
    

def initalizeDB():
    global words_df;
    words = []
    count = 0
    while len(words) < 100:
        print(len(words))
        words.append(wordGenerator.get_random_word())
    for word in words:
        try:
            wordObj = lookupWord(word)
#            self, word, date, definition, pos, ety, syl, pho, offensive
#            words_df = pd.DataFrame(columns=['Word','Definition', 'Etymology', 'Part_of_Speech', 'Date', 'Syllables', 'Phonetic', 'Offensive'])
            
            words_df = words_df.append({
                'Word': wordObj.Word,
                'Definition': wordObj.Definition, 
                'Etymology': wordObj.Etymology, 
                'Part_of_Speech': wordObj.Part_of_Speech, 
                'Date': wordObj.Date, 
                'Syllables': wordObj.Syllables, 
                'Phonetic': wordObj.Phonetic , 
                'Offensive': wordObj.Offensive}, ignore_index=True)
            
        except: 
            continue
            

    saveDatabase(words_df)


def addWordToDB(word):
    global words_df
    
    getDatabase()
    wordObj = lookupWord(word)
    
    if wordObj != None:
#        print(f'Saving word {word}')
#        words_df = pd.DataFrame(columns=['Word','Definition', 'Etymology', 'Part_of_Speech', 'Date', 'Syllables', 'Phonetic', 'Offensive'])
        
        
        words_df = words_df.append({
            'Word': wordObj.Word,
            'Definition': wordObj.Definition, 
            'Etymology': wordObj.Etymology, 
            'Part_of_Speech': wordObj.Part_of_Speech, 
            'Date': wordObj.Date, 
            'Syllables': wordObj.Syllables, 
            'Phonetic': wordObj.Phonetic , 
            'Offensive': wordObj.Offensive}, ignore_index=True)
        saveDatabase(words_df)
    
    
        

if __name__ == "__main__":
#    initalizeDB()
    lookupWord("penultimate")
        
    
    