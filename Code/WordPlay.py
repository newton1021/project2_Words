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

# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome_from_dict(json.loads(json_string))

from typing import Optional, Any, List, Union, TypeVar, Type, cast, Callable
from uuid import UUID
from enum import Enum


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            print(f'PASS: {f}')
            return f(x)
        except:
            print(f'FAIL: {f}')
            pass
    assert False
    
    
def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


class Sound:
    audio: Optional[str]
    ref: Optional[str]
    stat: Optional[int]
    
    def __init__(self, audio: Optional[str], ref: Optional[str], stat: Optional[int]) -> None:
        self.audio = audio
        self.ref = ref
        self.stat = stat
        
    @staticmethod
    def from_dict(obj: Any) -> 'Sound':
        assert isinstance(obj, dict)
        audio = from_union([from_str, from_none], obj.get("audio"))
        ref = from_union([from_str, from_none], obj.get("ref"))
        stat = from_union([from_none, lambda x: int(from_str(x))], obj.get("stat"))
        return Sound(audio, ref, stat)
    
    def to_dict(self) -> dict:
        result: dict = {}
        result["audio"] = from_union([from_str, from_none], self.audio)
        result["ref"] = from_union([from_str, from_none], self.ref)
        result["stat"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.stat)
        return result
    
    
class PR:
    mw: Optional[str]
    sound: Optional[Sound]
    
    def __init__(self, mw: Optional[str], sound: Optional[Sound]) -> None:
        self.mw = mw
        self.sound = sound
        
    @staticmethod
    def from_dict(obj: Any) -> 'PR':
        assert isinstance(obj, dict)
        mw = from_union([from_str, from_none], obj.get("mw"))
        sound = from_union([Sound.from_dict, from_none], obj.get("sound"))
        return PR(mw, sound)
    
    def to_dict(self) -> dict:
        result: dict = {}
        result["mw"] = from_union([from_str, from_none], self.mw)
        result["sound"] = from_union([lambda x: to_class(Sound, x), from_none], self.sound)
        return result
    
    
class Hwi:
    hw: Optional[str]
    prs: Optional[List[PR]]
    
    def __init__(self, hw: Optional[str], prs: Optional[List[PR]]) -> None:
        self.hw = hw
        self.prs = prs
        
    @staticmethod
    def from_dict(obj: Any) -> 'Hwi':
        assert isinstance(obj, dict)
        hw = from_union([from_str, from_none], obj.get("hw"))
        prs = from_union([lambda x: from_list(PR.from_dict, x), from_none], obj.get("prs"))
        return Hwi(hw, prs)
    
    def to_dict(self) -> dict:
        result: dict = {}
        result["hw"] = from_union([from_str, from_none], self.hw)
        result["prs"] = from_union([lambda x: from_list(lambda x: to_class(PR, x), x), from_none], self.prs)
        return result
    
    
class Meta:
    id: Optional[str]
    uuid: Optional[UUID]
    sort: Optional[str]
    src: Optional[str]
    section: Optional[str]
    stems: Optional[List[str]]
    offensive: Optional[bool]
    
    def __init__(self, id: Optional[str], uuid: Optional[UUID], sort: Optional[str], src: Optional[str], section: Optional[str], stems: Optional[List[str]], offensive: Optional[bool]) -> None:
        self.id = id
        self.uuid = uuid
        self.sort = sort
        self.src = src
        self.section = section
        self.stems = stems
        self.offensive = offensive
        
    @staticmethod
    def from_dict(obj: Any) -> 'Meta':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        uuid = from_union([lambda x: UUID(x), from_none], obj.get("uuid"))
        sort = from_union([from_str, from_none], obj.get("sort"))
        src = from_union([from_str, from_none], obj.get("src"))
        section = from_union([from_str, from_none], obj.get("section"))
        stems = from_union([lambda x: from_list(from_str, x), from_none], obj.get("stems"))
        offensive = from_union([from_bool, from_none], obj.get("offensive"))
        return Meta(id, uuid, sort, src, section, stems, offensive)
    
    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["uuid"] = from_union([lambda x: str(x), from_none], self.uuid)
        result["sort"] = from_union([from_str, from_none], self.sort)
        result["src"] = from_union([from_str, from_none], self.src)
        result["section"] = from_union([from_str, from_none], self.section)
        result["stems"] = from_union([lambda x: from_list(from_str, x), from_none], self.stems)
        result["offensive"] = from_union([from_bool, from_none], self.offensive)
        return result
    
    
class Aq:
    auth: Optional[str]
    source: Optional[str]
    aqdate: Optional[str]
    
    def __init__(self, auth: Optional[str], source: Optional[str], aqdate: Optional[str]) -> None:
        self.auth = auth
        self.source = source
        self.aqdate = aqdate
        
    @staticmethod
    def from_dict(obj: Any) -> 'Aq':
        assert isinstance(obj, dict)
        auth = from_union([from_str, from_none], obj.get("auth"))
        source = from_union([from_str, from_none], obj.get("source"))
        aqdate = from_union([from_str, from_none], obj.get("aqdate"))
        return Aq(auth, source, aqdate)
    
    def to_dict(self) -> dict:
        result: dict = {}
        result["auth"] = from_union([from_str, from_none], self.auth)
        result["source"] = from_union([from_str, from_none], self.source)
        result["aqdate"] = from_union([from_str, from_none], self.aqdate)
        return result
    
    
class Quote:
    t: Optional[str]
    aq: Optional[Aq]
    
    def __init__(self, t: Optional[str], aq: Optional[Aq]) -> None:
        self.t = t
        self.aq = aq
        
    @staticmethod
    def from_dict(obj: Any) -> 'Quote':
        assert isinstance(obj, dict)
        t = from_union([from_str, from_none], obj.get("t"))
        aq = from_union([Aq.from_dict, from_none], obj.get("aq"))
        return Quote(t, aq)
    
    def to_dict(self) -> dict:
        result: dict = {}
        result["t"] = from_union([from_str, from_none], self.t)
        result["aq"] = from_union([lambda x: to_class(Aq, x), from_none], self.aq)
        return result
    
    
class UtxtClass:
    t: Optional[str]
    
    def __init__(self, t: Optional[str]) -> None:
        self.t = t
        
    @staticmethod
    def from_dict(obj: Any) -> 'UtxtClass':
        assert isinstance(obj, dict)
        t = from_union([from_str, from_none], obj.get("t"))
        return UtxtClass(t)
    
    def to_dict(self) -> dict:
        result: dict = {}
        result["t"] = from_union([from_str, from_none], self.t)
        return result
    
    
class Uro:
    ure: Optional[str]
    prs: Optional[List[PR]]
    fl: Optional[str]
    utxt: Optional[List[List[Union[List[UtxtClass], str]]]]
    
    def __init__(self, ure: Optional[str], prs: Optional[List[PR]], fl: Optional[str], utxt: Optional[List[List[Union[List[UtxtClass], str]]]]) -> None:
        self.ure = ure
        self.prs = prs
        self.fl = fl
        self.utxt = utxt
        
    @staticmethod
    def from_dict(obj: Any) -> 'Uro':
        assert isinstance(obj, dict)
        ure = from_union([from_str, from_none], obj.get("ure"))
        prs = from_union([lambda x: from_list(PR.from_dict, x), from_none], obj.get("prs"))
        fl = from_union([from_str, from_none], obj.get("fl"))
        utxt = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: from_list(UtxtClass.from_dict, x), from_str], x), x), x), from_none], obj.get("utxt"))
        return Uro(ure, prs, fl, utxt)
    
    def to_dict(self) -> dict:
        result: dict = {}
        result["ure"] = from_union([from_str, from_none], self.ure)
        result["prs"] = from_union([lambda x: from_list(lambda x: to_class(PR, x), x), from_none], self.prs)
        result["fl"] = from_union([from_str, from_none], self.fl)
        result["utxt"] = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: from_list(lambda x: to_class(UtxtClass, x), x), from_str], x), x), x), from_none], self.utxt)
        return result
    
    
class PurpleSseq:
    sn: Optional[str]
    dt: Optional[List[List[Union[List[UtxtClass], str]]]]
    
    def __init__(self, sn: Optional[str], dt: Optional[List[List[Union[List[UtxtClass], str]]]]) -> None:
        self.sn = sn
        self.dt = dt
        
    @staticmethod
    def from_dict(obj: Any) -> 'PurpleSseq':
        assert isinstance(obj, dict)
        sn = from_union([from_str, from_none], obj.get("sn"))
        dt = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: from_list(UtxtClass.from_dict, x), from_str], x), x), x), from_none], obj.get("dt"))
        return PurpleSseq(sn, dt)
    
    def to_dict(self) -> dict:
        result: dict = {}
        result["sn"] = from_union([from_str, from_none], self.sn)
        result["dt"] = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: from_list(lambda x: to_class(UtxtClass, x), x), from_str], x), x), x), from_none], self.dt)
        return result
    
    
class SseqEnum(Enum):
    PSEQ = "pseq"
    SENSE = "sense"
    
    
class Sdsense:
    sd: Optional[str]
    dt: Optional[List[List[str]]]
    
    def __init__(self, sd: Optional[str], dt: Optional[List[List[str]]]) -> None:
        self.sd = sd
        self.dt = dt
        
    @staticmethod
    def from_dict(obj: Any) -> 'Sdsense':
        assert isinstance(obj, dict)
        sd = from_union([from_str, from_none], obj.get("sd"))
        dt = from_union([lambda x: from_list(lambda x: from_list(from_str, x), x), from_none], obj.get("dt"))
        return Sdsense(sd, dt)
    
    def to_dict(self) -> dict:
        result: dict = {}
        result["sd"] = from_union([from_str, from_none], self.sd)
        result["dt"] = from_union([lambda x: from_list(lambda x: from_list(from_str, x), x), from_none], self.dt)
        return result
    
    
class FluffySseq:
    sn: Optional[str]
    dt: Optional[List[List[Union[List[UtxtClass], str]]]]
    sdsense: Optional[Sdsense]
    
    def __init__(self, sn: Optional[str], dt: Optional[List[List[Union[List[UtxtClass], str]]]], sdsense: Optional[Sdsense]) -> None:
        self.sn = sn
        self.dt = dt
        self.sdsense = sdsense
        
    @staticmethod
    def from_dict(obj: Any) -> 'FluffySseq':
        assert isinstance(obj, dict)
        sn = from_union([from_str, from_none], obj.get("sn"))
        dt = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: from_list(UtxtClass.from_dict, x), from_str], x), x), x), from_none], obj.get("dt"))
        sdsense = from_union([Sdsense.from_dict, from_none], obj.get("sdsense"))
        return FluffySseq(sn, dt, sdsense)
    
    def to_dict(self) -> dict:
        result: dict = {}
        result["sn"] = from_union([from_str, from_none], self.sn)
        result["dt"] = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: from_list(lambda x: to_class(UtxtClass, x), x), from_str], x), x), x), from_none], self.dt)
        result["sdsense"] = from_union([lambda x: to_class(Sdsense, x), from_none], self.sdsense)
        return result
    
    
class Def:
    sseq: Optional[List[List[List[Union[List[List[Union[PurpleSseq, SseqEnum]]], FluffySseq, SseqEnum]]]]]
    
    def __init__(self, sseq: Optional[List[List[List[Union[List[List[Union[PurpleSseq, SseqEnum]]], FluffySseq, SseqEnum]]]]]) -> None:
        self.sseq = sseq
        
    @staticmethod
    def from_dict(obj: Any) -> 'Def':
        assert isinstance(obj, dict)
        sseq = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_list(lambda x: from_union([FluffySseq.from_dict, lambda x: from_list(lambda x: from_list(lambda x: from_union([PurpleSseq.from_dict, SseqEnum], x), x), x), SseqEnum], x), x), x), x), from_none], obj.get("sseq"))
        return Def(sseq)
    
    def to_dict(self) -> dict:
        result: dict = {}
        result["sseq"] = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: to_class(FluffySseq, x), lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: to_class(PurpleSseq, x), lambda x: to_enum(SseqEnum, x)], x), x), x), lambda x: to_enum(SseqEnum, x)], x), x), x), x), from_none], self.sseq)
        return result
    
    
class WelcomeElement:
    meta: Optional[Meta]
    hwi: Optional[Hwi]
    fl: Optional[str]
    welcome_def: Optional[List[Def]]
    uros: Optional[List[Uro]]
    quotes: Optional[List[Quote]]
    et: Optional[List[List[str]]]
    date: Optional[str]
    shortdef: Optional[List[str]]
    
    def __init__(self, meta: Optional[Meta], hwi: Optional[Hwi], fl: Optional[str], welcome_def: Optional[List[Def]], uros: Optional[List[Uro]], quotes: Optional[List[Quote]], et: Optional[List[List[str]]], date: Optional[str], shortdef: Optional[List[str]]) -> None:
        self.meta = meta
        self.hwi = hwi
        self.fl = fl
        self.welcome_def = welcome_def
        self.uros = uros
        self.quotes = quotes
        self.et = et
        self.date = date
        self.shortdef = shortdef
        
    @staticmethod
    def from_dict(obj: Any) -> 'WelcomeElement':
        assert isinstance(obj, dict)
        meta = from_union([Meta.from_dict, from_none], obj.get("meta"))
        hwi = from_union([Hwi.from_dict, from_none], obj.get("hwi"))
        fl = from_union([from_str, from_none], obj.get("fl"))
        welcome_def = from_union([lambda x: from_list(Def.from_dict, x), from_none], obj.get("def"))
        uros = from_union([lambda x: from_list(Uro.from_dict, x), from_none], obj.get("uros"))
        quotes = from_union([lambda x: from_list(Quote.from_dict, x), from_none], obj.get("quotes"))
        et = from_union([lambda x: from_list(lambda x: from_list(from_str, x), x), from_none], obj.get("et"))
        date = from_union([from_str, from_none], obj.get("date"))
        shortdef = from_union([lambda x: from_list(from_str, x), from_none], obj.get("shortdef"))
        return WelcomeElement(meta, hwi, fl, welcome_def, uros, quotes, et, date, shortdef)
    
    def to_dict(self) -> dict:
        result: dict = {}
        result["meta"] = from_union([lambda x: to_class(Meta, x), from_none], self.meta)
        result["hwi"] = from_union([lambda x: to_class(Hwi, x), from_none], self.hwi)
        result["fl"] = from_union([from_str, from_none], self.fl)
        result["def"] = from_union([lambda x: from_list(lambda x: to_class(Def, x), x), from_none], self.welcome_def)
        result["uros"] = from_union([lambda x: from_list(lambda x: to_class(Uro, x), x), from_none], self.uros)
        result["quotes"] = from_union([lambda x: from_list(lambda x: to_class(Quote, x), x), from_none], self.quotes)
        result["et"] = from_union([lambda x: from_list(lambda x: from_list(from_str, x), x), from_none], self.et)
        result["date"] = from_union([from_str, from_none], self.date)
        result["shortdef"] = from_union([lambda x: from_list(from_str, x), from_none], self.shortdef)
        return result
    
    
def welcome_from_dict(s: Any) -> List[WelcomeElement]:
    return from_list(WelcomeElement.from_dict, s)


def welcome_to_dict(x: List[WelcomeElement]) -> Any:
    return from_list(lambda x: to_class(WelcomeElement, x), x)





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
        self.date = date
        self.Part_of_Speech
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
    print(response)
    try: 
        newWordObj = welcome_from_dict(json.loads(response))
    except:
        print("the json failed")
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
        ety = newWordObj[0].et[0][1]
        print(ety)
    except:
        ety = "unknown"
    try: 
        pos = newWordObj[0].fl
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
    
    word_df = pd.DataFrame(allwords)
    
    

def saveDatabase(df):
    connection_String = "postgres:drwho@localhost:5432/words"
    engine = create_engine(f'postgresql://{connection_String}')
    print(engine.table_names())
    
    df.to_sql(name="word_list", con=engine, if_exists="append", index=False)
    
    

def initalizeDB():
    words = []
    while len(words) < 500:
        words.add(wordGenerator.get_random_word())
    for word in words:
        wordObj = lookupWord(word)
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


def addWordToDB(word):
    global words_df
    
    getDatabase()
    wordObj = lookupWord(word)
    
    if wordObj != None:
        print(f'Saving word {word}')
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
    
    
        
        
        
    
    