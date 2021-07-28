# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Dependencies
import requests
import json
import config
from random_word import RandomWords
import pandas as pd


# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome_from_dict(json.loads(json_string))

from typing import Optional, Any, List, Union, TypeVar, Type, cast, Callable
from uuid import UUID


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
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
    
    
class Uro:
    ure: Optional[str]
    fl: Optional[str]
    
    def __init__(self, ure: Optional[str], fl: Optional[str]) -> None:
        self.ure = ure
        self.fl = fl
        
    @staticmethod
    def from_dict(obj: Any) -> 'Uro':
        assert isinstance(obj, dict)
        ure = from_union([from_str, from_none], obj.get("ure"))
        fl = from_union([from_str, from_none], obj.get("fl"))
        return Uro(ure, fl)
    
    def to_dict(self) -> dict:
        result: dict = {}
        result["ure"] = from_union([from_str, from_none], self.ure)
        result["fl"] = from_union([from_str, from_none], self.fl)
        return result
    
    
class DtClass:
    t: Optional[str]
    
    def __init__(self, t: Optional[str]) -> None:
        self.t = t
        
    @staticmethod
    def from_dict(obj: Any) -> 'DtClass':
        assert isinstance(obj, dict)
        t = from_union([from_str, from_none], obj.get("t"))
        return DtClass(t)
    
    def to_dict(self) -> dict:
        result: dict = {}
        result["t"] = from_union([from_str, from_none], self.t)
        return result
    
    
class SseqClass:
    dt: Optional[List[List[Union[List[DtClass], str]]]]
    
    def __init__(self, dt: Optional[List[List[Union[List[DtClass], str]]]]) -> None:
        self.dt = dt
        
    @staticmethod
    def from_dict(obj: Any) -> 'SseqClass':
        assert isinstance(obj, dict)
        dt = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: from_list(DtClass.from_dict, x), from_str], x), x), x), from_none], obj.get("dt"))
        return SseqClass(dt)
    
    def to_dict(self) -> dict:
        result: dict = {}
        result["dt"] = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: from_list(lambda x: to_class(DtClass, x), x), from_str], x), x), x), from_none], self.dt)
        return result
    
    
class Def:
    sls: Optional[List[str]]
    sseq: Optional[List[List[List[Union[SseqClass, str]]]]]
    
    def __init__(self, sls: Optional[List[str]], sseq: Optional[List[List[List[Union[SseqClass, str]]]]]) -> None:
        self.sls = sls
        self.sseq = sseq
        
    @staticmethod
    def from_dict(obj: Any) -> 'Def':
        assert isinstance(obj, dict)
        sls = from_union([lambda x: from_list(from_str, x), from_none], obj.get("sls"))
        sseq = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_list(lambda x: from_union([SseqClass.from_dict, from_str], x), x), x), x), from_none], obj.get("sseq"))
        return Def(sls, sseq)
    
    def to_dict(self) -> dict:
        result: dict = {}
        result["sls"] = from_union([lambda x: from_list(from_str, x), from_none], self.sls)
        result["sseq"] = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: to_class(SseqClass, x), from_str], x), x), x), x), from_none], self.sseq)
        return result
    
    
class WelcomeElement:
    meta: Optional[Meta]
    hwi: Optional[Hwi]
    fl: Optional[str]
    welcome_def: Optional[List[Def]]
    uros: Optional[List[Uro]]
    et: Optional[List[List[str]]]
    date: Optional[str]
    shortdef: Optional[List[str]]
    
    def __init__(self, meta: Optional[Meta], hwi: Optional[Hwi], fl: Optional[str], welcome_def: Optional[List[Def]], uros: Optional[List[Uro]], et: Optional[List[List[str]]], date: Optional[str], shortdef: Optional[List[str]]) -> None:
        self.meta = meta
        self.hwi = hwi
        self.fl = fl
        self.welcome_def = welcome_def
        self.uros = uros
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
        et = from_union([lambda x: from_list(lambda x: from_list(from_str, x), x), from_none], obj.get("et"))
        date = from_union([from_str, from_none], obj.get("date"))
        shortdef = from_union([lambda x: from_list(from_str, x), from_none], obj.get("shortdef"))
        return WelcomeElement(meta, hwi, fl, welcome_def, uros, et, date, shortdef)
    
    def to_dict(self) -> dict:
        result: dict = {}
        result["meta"] = from_union([lambda x: to_class(Meta, x), from_none], self.meta)
        result["hwi"] = from_union([lambda x: to_class(Hwi, x), from_none], self.hwi)
        result["fl"] = from_union([from_str, from_none], self.fl)
        result["def"] = from_union([lambda x: from_list(lambda x: to_class(Def, x), x), from_none], self.welcome_def)
        result["uros"] = from_union([lambda x: from_list(lambda x: to_class(Uro, x), x), from_none], self.uros)
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
words_df


# %%
word = RandomWords()

# Return a single random word
word.get_random_word()

while len(words) < 500:
    words.add(word.get_random_word())




# %%
# URL for GET requests to retrieve vehicle datawor
url = "https://www.dictionaryapi.com/api/v3/references"

def dictionary(test_word):
    return (f'{url}/collegiate/json/{test_word}?key={config.API_KEY_Dictionary}')





# %%
# Pretty print JSON for all launchpads



# for word in list(words):
#     print(word)
#     word_url = dictionary('Banana')
#     print(word_url)
#     response = requests.get(word_url).json()
#     print(json.dumps(response, indent=4, sort_keys=True))


# %%
#short_def = response[0]['shortdef']
#print(short_def)
#word_id = response[0]['meta']['id']
#print(word_id)
#ety = response[0]['et'][0][1]
#print(ety)
#pos = response[0]['fl']
#print(pos)
#date = response[0]['date']
#print(date)
#syl = response[0]['hwi']['hw']
#print(syl)
#phn = response[0]['hwi']['prs'][0]['mw']
#print(phn)
#offensive = response[0]['meta']['offensive']
#print(offensive)


# %%
# Pretty print JSON for all launchpads

for word in list(words):
    print(word)
    word_url = dictionary(word)
        #print(word_url)
    response = requests.get(word_url).text
        #print(json.dumps(response, indent=4, sort_keys=True))
    try: 
        newWordObj = welcome_from_dict(json.loads(response))
    except:
        print("the json failed")
        continue
    
    
    try:
                
        short_def = newWordObj[0].shortdef[0]
    except:
        short_def = "no definition"
    try: 
        word_id = newWordObj[0].meta.id
    except:
        word_id = ""
        
        
    try: 
        ety = newWordObj[0].et
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

    words_df = words_df.append({'Word': word_id,'Definition': short_def, 'Etymology': ety, 'Part_of_Speech': pos, 'Date': date, 'Syllables': syl, 'Phonetic': phn , 'Offensive': offensive}, ignore_index=True)
#    except: 
#        print('word was skipped')
        
#     except(error):
#         print(f'{word} was skipped. Missing data.')
#         print(error)
    print(f'{word_id}: {short_def}' )

# %%
print(words_df.head())



# %%



# %%
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


def loadDatabase(df):
    connection_String = "postgres:drwho@localhost:5432/words"
    engine = create_engine(f'postgresql://{connection_String}')
    print(engine.table_names())
    
    df.to_sql(name="word_list", con=engine, if_exists="replace", index=False)


loadDatabase(words_df)