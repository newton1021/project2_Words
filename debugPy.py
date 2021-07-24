# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Dependencies
import requests
import json
import config
from random_word import RandomWords
import pandas as pd


# %%
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome_from_dict(json.loads(json_string))

from typing import Optional, Any, List, Union, TypeVar, Type, cast, Callable
from enum import Enum
from uuid import UUID


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


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


class Art:
    artid: Optional[str]
    capt: Optional[str]

    def __init__(self, artid: Optional[str], capt: Optional[str]) -> None:
        self.artid = artid
        self.capt = capt

    @staticmethod
    def from_dict(obj: Any) -> 'Art':
        assert isinstance(obj, dict)
        artid = from_union([from_str, from_none], obj.get("artid"))
        capt = from_union([from_str, from_none], obj.get("capt"))
        return Art(artid, capt)

    def to_dict(self) -> dict:
        result: dict = {}
        result["artid"] = from_union([from_str, from_none], self.artid)
        result["capt"] = from_union([from_str, from_none], self.capt)
        return result


class FL(Enum):
    GEOGRAPHICAL_NAME = "geographical name"
    NOUN = "noun"


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
    l: Optional[str]

    def __init__(self, mw: Optional[str], sound: Optional[Sound], l: Optional[str]) -> None:
        self.mw = mw
        self.sound = sound
        self.l = l

    @staticmethod
    def from_dict(obj: Any) -> 'PR':
        assert isinstance(obj, dict)
        mw = from_union([from_str, from_none], obj.get("mw"))
        sound = from_union([Sound.from_dict, from_none], obj.get("sound"))
        l = from_union([from_str, from_none], obj.get("l"))
        return PR(mw, sound, l)

    def to_dict(self) -> dict:
        result: dict = {}
        result["mw"] = from_union([from_str, from_none], self.mw)
        result["sound"] = from_union([lambda x: to_class(Sound, x), from_none], self.sound)
        result["l"] = from_union([from_str, from_none], self.l)
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


class In:
    in_if: Optional[str]
    il: Optional[str]

    def __init__(self, in_if: Optional[str], il: Optional[str]) -> None:
        self.in_if = in_if
        self.il = il

    @staticmethod
    def from_dict(obj: Any) -> 'In':
        assert isinstance(obj, dict)
        in_if = from_union([from_str, from_none], obj.get("if"))
        il = from_union([from_str, from_none], obj.get("il"))
        return In(in_if, il)

    def to_dict(self) -> dict:
        result: dict = {}
        result["if"] = from_union([from_str, from_none], self.in_if)
        result["il"] = from_union([from_str, from_none], self.il)
        return result


class Section(Enum):
    ALPHA = "alpha"
    GEOG = "geog"


class Src(Enum):
    COLLEGIATE = "collegiate"


class Meta:
    id: Optional[str]
    offensive: Optional[bool]
    section: Optional[Section]
    sort: Optional[str]
    src: Optional[Src]
    stems: Optional[List[str]]
    uuid: Optional[UUID]

    def __init__(self, id: Optional[str], offensive: Optional[bool], section: Optional[Section], sort: Optional[str], src: Optional[Src], stems: Optional[List[str]], uuid: Optional[UUID]) -> None:
        self.id = id
        self.offensive = offensive
        self.section = section
        self.sort = sort
        self.src = src
        self.stems = stems
        self.uuid = uuid

    @staticmethod
    def from_dict(obj: Any) -> 'Meta':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        offensive = from_union([from_bool, from_none], obj.get("offensive"))
        section = from_union([Section, from_none], obj.get("section"))
        sort = from_union([from_str, from_none], obj.get("sort"))
        src = from_union([Src, from_none], obj.get("src"))
        stems = from_union([lambda x: from_list(from_str, x), from_none], obj.get("stems"))
        uuid = from_union([lambda x: UUID(x), from_none], obj.get("uuid"))
        return Meta(id, offensive, section, sort, src, stems, uuid)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["offensive"] = from_union([from_bool, from_none], self.offensive)
        result["section"] = from_union([lambda x: to_enum(Section, x), from_none], self.section)
        result["sort"] = from_union([from_str, from_none], self.sort)
        result["src"] = from_union([lambda x: to_enum(Src, x), from_none], self.src)
        result["stems"] = from_union([lambda x: from_list(from_str, x), from_none], self.stems)
        result["uuid"] = from_union([lambda x: str(x), from_none], self.uuid)
        return result


class Aq:
    auth: Optional[str]

    def __init__(self, auth: Optional[str]) -> None:
        self.auth = auth

    @staticmethod
    def from_dict(obj: Any) -> 'Aq':
        assert isinstance(obj, dict)
        auth = from_union([from_str, from_none], obj.get("auth"))
        return Aq(auth)

    def to_dict(self) -> dict:
        result: dict = {}
        result["auth"] = from_union([from_str, from_none], self.auth)
        return result


class DtClass:
    t: Optional[str]
    aq: Optional[Aq]

    def __init__(self, t: Optional[str], aq: Optional[Aq]) -> None:
        self.t = t
        self.aq = aq

    @staticmethod
    def from_dict(obj: Any) -> 'DtClass':
        assert isinstance(obj, dict)
        t = from_union([from_str, from_none], obj.get("t"))
        aq = from_union([Aq.from_dict, from_none], obj.get("aq"))
        return DtClass(t, aq)

    def to_dict(self) -> dict:
        result: dict = {}
        result["t"] = from_union([from_str, from_none], self.t)
        result["aq"] = from_union([lambda x: to_class(Aq, x), from_none], self.aq)
        return result


class Sdsense:
    dt: Optional[List[List[str]]]
    sd: Optional[str]

    def __init__(self, dt: Optional[List[List[str]]], sd: Optional[str]) -> None:
        self.dt = dt
        self.sd = sd

    @staticmethod
    def from_dict(obj: Any) -> 'Sdsense':
        assert isinstance(obj, dict)
        dt = from_union([lambda x: from_list(lambda x: from_list(from_str, x), x), from_none], obj.get("dt"))
        sd = from_union([from_str, from_none], obj.get("sd"))
        return Sdsense(dt, sd)

    def to_dict(self) -> dict:
        result: dict = {}
        result["dt"] = from_union([lambda x: from_list(lambda x: from_list(from_str, x), x), from_none], self.dt)
        result["sd"] = from_union([from_str, from_none], self.sd)
        return result


class SseqClass:
    dt: Optional[List[List[Union[List[DtClass], str]]]]
    sn: Optional[int]
    sls: Optional[List[str]]
    sdsense: Optional[Sdsense]

    def __init__(self, dt: Optional[List[List[Union[List[DtClass], str]]]], sn: Optional[int], sls: Optional[List[str]], sdsense: Optional[Sdsense]) -> None:
        self.dt = dt
        self.sn = sn
        self.sls = sls
        self.sdsense = sdsense

    @staticmethod
    def from_dict(obj: Any) -> 'SseqClass':
        assert isinstance(obj, dict)
        dt = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: from_list(DtClass.from_dict, x), from_str], x), x), x), from_none], obj.get("dt"))
        sn = from_union([from_none, lambda x: int(from_str(x))], obj.get("sn"))
        sls = from_union([lambda x: from_list(from_str, x), from_none], obj.get("sls"))
        sdsense = from_union([Sdsense.from_dict, from_none], obj.get("sdsense"))
        return SseqClass(dt, sn, sls, sdsense)

    def to_dict(self) -> dict:
        result: dict = {}
        result["dt"] = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: from_list(lambda x: to_class(DtClass, x), x), from_str], x), x), x), from_none], self.dt)
        result["sn"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.sn)
        result["sls"] = from_union([lambda x: from_list(from_str, x), from_none], self.sls)
        result["sdsense"] = from_union([lambda x: to_class(Sdsense, x), from_none], self.sdsense)
        return result


class SseqEnum(Enum):
    SENSE = "sense"


class Def:
    sseq: Optional[List[List[List[Union[SseqClass, SseqEnum]]]]]

    def __init__(self, sseq: Optional[List[List[List[Union[SseqClass, SseqEnum]]]]]) -> None:
        self.sseq = sseq

    @staticmethod
    def from_dict(obj: Any) -> 'Def':
        assert isinstance(obj, dict)
        sseq = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_list(lambda x: from_union([SseqClass.from_dict, SseqEnum], x), x), x), x), from_none], obj.get("sseq"))
        return Def(sseq)

    def to_dict(self) -> dict:
        result: dict = {}
        result["sseq"] = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: to_class(SseqClass, x), lambda x: to_enum(SseqEnum, x)], x), x), x), x), from_none], self.sseq)
        return result


class WelcomeElement:
    art: Optional[Art]
    date: Optional[str]
    welcome_def: Optional[List[Def]]
    et: Optional[List[List[str]]]
    fl: Optional[FL]
    hwi: Optional[Hwi]
    meta: Optional[Meta]
    shortdef: Optional[List[str]]
    ins: Optional[List[In]]

    def __init__(self, art: Optional[Art], date: Optional[str], welcome_def: Optional[List[Def]], et: Optional[List[List[str]]], fl: Optional[FL], hwi: Optional[Hwi], meta: Optional[Meta], shortdef: Optional[List[str]], ins: Optional[List[In]]) -> None:
        self.art = art
        self.date = date
        self.welcome_def = welcome_def
        self.et = et
        self.fl = fl
        self.hwi = hwi
        self.meta = meta
        self.shortdef = shortdef
        self.ins = ins

    @staticmethod
    def from_dict(obj: Any) -> 'WelcomeElement':
        assert isinstance(obj, dict)
        art = from_union([Art.from_dict, from_none], obj.get("art"))
        date = from_union([from_str, from_none], obj.get("date"))
        welcome_def = from_union([lambda x: from_list(Def.from_dict, x), from_none], obj.get("def"))
        et = from_union([lambda x: from_list(lambda x: from_list(from_str, x), x), from_none], obj.get("et"))
        fl = from_union([FL, from_none], obj.get("fl"))
        hwi = from_union([Hwi.from_dict, from_none], obj.get("hwi"))
        meta = from_union([Meta.from_dict, from_none], obj.get("meta"))
        shortdef = from_union([lambda x: from_list(from_str, x), from_none], obj.get("shortdef"))
        ins = from_union([lambda x: from_list(In.from_dict, x), from_none], obj.get("ins"))
        return WelcomeElement(art, date, welcome_def, et, fl, hwi, meta, shortdef, ins)

    def to_dict(self) -> dict:
        result: dict = {}
        result["art"] = from_union([lambda x: to_class(Art, x), from_none], self.art)
        result["date"] = from_union([from_str, from_none], self.date)
        result["def"] = from_union([lambda x: from_list(lambda x: to_class(Def, x), x), from_none], self.welcome_def)
        result["et"] = from_union([lambda x: from_list(lambda x: from_list(from_str, x), x), from_none], self.et)
        result["fl"] = from_union([lambda x: to_enum(FL, x), from_none], self.fl)
        result["hwi"] = from_union([lambda x: to_class(Hwi, x), from_none], self.hwi)
        result["meta"] = from_union([lambda x: to_class(Meta, x), from_none], self.meta)
        result["shortdef"] = from_union([lambda x: from_list(from_str, x), from_none], self.shortdef)
        result["ins"] = from_union([lambda x: from_list(lambda x: to_class(In, x), x), from_none], self.ins)
        return result


def welcome_from_dict(s: Any) -> List[WelcomeElement]:
    return from_list(WelcomeElement.from_dict, s)


def welcome_to_dict(x: List[WelcomeElement]) -> Any:
    return from_list(lambda x: to_class(WelcomeElement, x), x)


# %%
words = set()
words_df = pd.DataFrame(columns=['Word','Definition', 'Etymology', 'Part_of_Speech', 'Date', 'Syllables', 'Phonetic', 'Offensive'])
words_df


# %%
word = RandomWords()

# Return a single random word
word.get_random_word()

for x in range(10):
    words.add(word.get_random_word())

print(words)


# %%
# URL for GET requests to retrieve vehicle data
url = "https://www.dictionaryapi.com/api/v3/references"

def dictionary(test_word):
    return (f'{url}/collegiate/json/{test_word}?key={config.API_KEY_Dictionary}')


dictionary ("Banana")


# %%
# Pretty print JSON for all launchpads

response = requests.get('https://www.dictionaryapi.com/api/v3/references/collegiate/json/Banana?key=cb663abf-5418-4831-8784-25c757c5b4ed').json()
# print(json.dumps(response, indent=4, sort_keys=True))
result = welcome_from_dict(json.loads(json.dumps(response, indent=4, sort_keys=True)))
result
# for word in list(words):
#     print(word)
#     word_url = dictionary('Banana')
#     print(word_url)
#     response = requests.get(word_url).json()
#     print(json.dumps(response, indent=4, sort_keys=True))


# %%
short_def = response[0]['shortdef']
print(short_def)
word_id = response[0]['meta']['id']
print(word_id)
ety = response[0]['et'][0][1]
print(ety)
pos = response[0]['fl']
print(pos)
date = response[0]['date']
print(date)
syl = response[0]['hwi']['hw']
print(syl)
phn = response[0]['hwi']['prs'][0]['mw']
print(phn)
offensive = response[0]['meta']['offensive']
print(offensive)


# %%
# Pretty print JSON for all launchpads

for word in list(words):
    print(word)
    word_url = dictionary(word)
        #print(word_url)
    response = requests.get(word_url).json()
        #print(json.dumps(response, indent=4, sort_keys=True))
    short_def = response[0]['shortdef']
    word_id = response[0]['meta']['id']
    pos = response[0]['fl']
    date = response[0]['date']
    syl = response[0]['hwi']['hw']
    phn = response[0]['hwi']['prs'][0]['mw']
    offensive = response[0]['meta']['offensive']
    words_df = words_df.append({'Word': word_id,'Definition': short_def, 'Etymology': ety, 'Part_of_Speech': pos, 'Date': date, 'Syllables': syl, 'Phonetic': phn , 'Offensive': offensive})
#     except(error):
#         print(f'{word} was skipped. Missing data.')
#         print(error)


# %%
words_df


# %%



# %%



