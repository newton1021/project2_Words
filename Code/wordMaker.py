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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


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


class PurpleAq:
    auth: Optional[str]

    def __init__(self, auth: Optional[str]) -> None:
        self.auth = auth

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleAq':
        assert isinstance(obj, dict)
        auth = from_union([from_str, from_none], obj.get("auth"))
        return PurpleAq(auth)

    def to_dict(self) -> dict:
        result: dict = {}
        result["auth"] = from_union([from_str, from_none], self.auth)
        return result


class PurpleDt:
    t: Optional[str]
    aq: Optional[PurpleAq]

    def __init__(self, t: Optional[str], aq: Optional[PurpleAq]) -> None:
        self.t = t
        self.aq = aq

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleDt':
        assert isinstance(obj, dict)
        t = from_union([from_str, from_none], obj.get("t"))
        aq = from_union([PurpleAq.from_dict, from_none], obj.get("aq"))
        return PurpleDt(t, aq)

    def to_dict(self) -> dict:
        result: dict = {}
        result["t"] = from_union([from_str, from_none], self.t)
        result["aq"] = from_union([lambda x: to_class(PurpleAq, x), from_none], self.aq)
        return result


class TentacledSseq:
    dt: Optional[List[List[Union[List[Union[List[List[str]], PurpleDt]], str]]]]
    sls: Optional[List[str]]

    def __init__(self, dt: Optional[List[List[Union[List[Union[List[List[str]], PurpleDt]], str]]]], sls: Optional[List[str]]) -> None:
        self.dt = dt
        self.sls = sls

    @staticmethod
    def from_dict(obj: Any) -> 'TentacledSseq':
        assert isinstance(obj, dict)
        dt = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: from_list(lambda x: from_union([PurpleDt.from_dict, lambda x: from_list(lambda x: from_list(from_str, x), x)], x), x), from_str], x), x), x), from_none], obj.get("dt"))
        sls = from_union([lambda x: from_list(from_str, x), from_none], obj.get("sls"))
        return TentacledSseq(dt, sls)

    def to_dict(self) -> dict:
        result: dict = {}
        result["dt"] = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: from_list(lambda x: from_union([lambda x: to_class(PurpleDt, x), lambda x: from_list(lambda x: from_list(from_str, x), x)], x), x), from_str], x), x), x), from_none], self.dt)
        result["sls"] = from_union([lambda x: from_list(from_str, x), from_none], self.sls)
        return result


class SseqEnum(Enum):
    BS = "bs"
    PSEQ = "pseq"
    SEN = "sen"
    SENSE = "sense"


class DroDef:
    sseq: Optional[List[List[List[Union[TentacledSseq, SseqEnum]]]]]

    def __init__(self, sseq: Optional[List[List[List[Union[TentacledSseq, SseqEnum]]]]]) -> None:
        self.sseq = sseq

    @staticmethod
    def from_dict(obj: Any) -> 'DroDef':
        assert isinstance(obj, dict)
        sseq = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_list(lambda x: from_union([TentacledSseq.from_dict, SseqEnum], x), x), x), x), from_none], obj.get("sseq"))
        return DroDef(sseq)

    def to_dict(self) -> dict:
        result: dict = {}
        result["sseq"] = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: to_class(TentacledSseq, x), lambda x: to_enum(SseqEnum, x)], x), x), x), x), from_none], self.sseq)
        return result


class VR:
    vl: Optional[str]
    va: Optional[str]

    def __init__(self, vl: Optional[str], va: Optional[str]) -> None:
        self.vl = vl
        self.va = va

    @staticmethod
    def from_dict(obj: Any) -> 'VR':
        assert isinstance(obj, dict)
        vl = from_union([from_str, from_none], obj.get("vl"))
        va = from_union([from_str, from_none], obj.get("va"))
        return VR(vl, va)

    def to_dict(self) -> dict:
        result: dict = {}
        result["vl"] = from_union([from_str, from_none], self.vl)
        result["va"] = from_union([from_str, from_none], self.va)
        return result


class Dro:
    drp: Optional[str]
    vrs: Optional[List[VR]]
    dro_def: Optional[List[DroDef]]

    def __init__(self, drp: Optional[str], vrs: Optional[List[VR]], dro_def: Optional[List[DroDef]]) -> None:
        self.drp = drp
        self.vrs = vrs
        self.dro_def = dro_def

    @staticmethod
    def from_dict(obj: Any) -> 'Dro':
        assert isinstance(obj, dict)
        drp = from_union([from_str, from_none], obj.get("drp"))
        vrs = from_union([lambda x: from_list(VR.from_dict, x), from_none], obj.get("vrs"))
        dro_def = from_union([lambda x: from_list(DroDef.from_dict, x), from_none], obj.get("def"))
        return Dro(drp, vrs, dro_def)

    def to_dict(self) -> dict:
        result: dict = {}
        result["drp"] = from_union([from_str, from_none], self.drp)
        result["vrs"] = from_union([lambda x: from_list(lambda x: to_class(VR, x), x), from_none], self.vrs)
        result["def"] = from_union([lambda x: from_list(lambda x: to_class(DroDef, x), x), from_none], self.dro_def)
        return result


class FL(Enum):
    ADJECTIVE = "adjective"
    ADVERB = "adverb"
    BIOGRAPHICAL_NAME = "biographical name"
    GEOGRAPHICAL_NAME = "geographical name"
    IDIOM = "idiom"
    NOUN = "noun"
    PHRASAL_VERB = "phrasal verb"
    TRANSITIVE_VERB = "transitive verb"
    VERB = "verb"


class Ref(Enum):
    C = "c"
    LD = "ld"
    OWL = "owl"


class Sound:
    audio: Optional[str]
    ref: Optional[Ref]
    stat: Optional[int]

    def __init__(self, audio: Optional[str], ref: Optional[Ref], stat: Optional[int]) -> None:
        self.audio = audio
        self.ref = ref
        self.stat = stat

    @staticmethod
    def from_dict(obj: Any) -> 'Sound':
        assert isinstance(obj, dict)
        audio = from_union([from_str, from_none], obj.get("audio"))
        ref = from_union([Ref, from_none], obj.get("ref"))
        stat = from_union([from_none, lambda x: int(from_str(x))], obj.get("stat"))
        return Sound(audio, ref, stat)

    def to_dict(self) -> dict:
        result: dict = {}
        result["audio"] = from_union([from_str, from_none], self.audio)
        result["ref"] = from_union([lambda x: to_enum(Ref, x), from_none], self.ref)
        result["stat"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.stat)
        return result


class HwiPR:
    mw: Optional[str]
    sound: Optional[Sound]
    l: Optional[str]
    pun: Optional[str]

    def __init__(self, mw: Optional[str], sound: Optional[Sound], l: Optional[str], pun: Optional[str]) -> None:
        self.mw = mw
        self.sound = sound
        self.l = l
        self.pun = pun

    @staticmethod
    def from_dict(obj: Any) -> 'HwiPR':
        assert isinstance(obj, dict)
        mw = from_union([from_str, from_none], obj.get("mw"))
        sound = from_union([Sound.from_dict, from_none], obj.get("sound"))
        l = from_union([from_str, from_none], obj.get("l"))
        pun = from_union([from_str, from_none], obj.get("pun"))
        return HwiPR(mw, sound, l, pun)

    def to_dict(self) -> dict:
        result: dict = {}
        result["mw"] = from_union([from_str, from_none], self.mw)
        result["sound"] = from_union([lambda x: to_class(Sound, x), from_none], self.sound)
        result["l"] = from_union([from_str, from_none], self.l)
        result["pun"] = from_union([from_str, from_none], self.pun)
        return result


class Hwi:
    hw: Optional[str]
    prs: Optional[List[HwiPR]]

    def __init__(self, hw: Optional[str], prs: Optional[List[HwiPR]]) -> None:
        self.hw = hw
        self.prs = prs

    @staticmethod
    def from_dict(obj: Any) -> 'Hwi':
        assert isinstance(obj, dict)
        hw = from_union([from_str, from_none], obj.get("hw"))
        prs = from_union([lambda x: from_list(HwiPR.from_dict, x), from_none], obj.get("prs"))
        return Hwi(hw, prs)

    def to_dict(self) -> dict:
        result: dict = {}
        result["hw"] = from_union([from_str, from_none], self.hw)
        result["prs"] = from_union([lambda x: from_list(lambda x: to_class(HwiPR, x), x), from_none], self.prs)
        return result


class InPR:
    mw: Optional[str]
    sound: Optional[Sound]

    def __init__(self, mw: Optional[str], sound: Optional[Sound]) -> None:
        self.mw = mw
        self.sound = sound

    @staticmethod
    def from_dict(obj: Any) -> 'InPR':
        assert isinstance(obj, dict)
        mw = from_union([from_str, from_none], obj.get("mw"))
        sound = from_union([Sound.from_dict, from_none], obj.get("sound"))
        return InPR(mw, sound)

    def to_dict(self) -> dict:
        result: dict = {}
        result["mw"] = from_union([from_str, from_none], self.mw)
        result["sound"] = from_union([lambda x: to_class(Sound, x), from_none], self.sound)
        return result


class In:
    in_if: Optional[str]
    il: Optional[str]
    ifc: Optional[str]
    prs: Optional[List[InPR]]

    def __init__(self, in_if: Optional[str], il: Optional[str], ifc: Optional[str], prs: Optional[List[InPR]]) -> None:
        self.in_if = in_if
        self.il = il
        self.ifc = ifc
        self.prs = prs

    @staticmethod
    def from_dict(obj: Any) -> 'In':
        assert isinstance(obj, dict)
        in_if = from_union([from_str, from_none], obj.get("if"))
        il = from_union([from_str, from_none], obj.get("il"))
        ifc = from_union([from_str, from_none], obj.get("ifc"))
        prs = from_union([lambda x: from_list(InPR.from_dict, x), from_none], obj.get("prs"))
        return In(in_if, il, ifc, prs)

    def to_dict(self) -> dict:
        result: dict = {}
        result["if"] = from_union([from_str, from_none], self.in_if)
        result["il"] = from_union([from_str, from_none], self.il)
        result["ifc"] = from_union([from_str, from_none], self.ifc)
        result["prs"] = from_union([lambda x: from_list(lambda x: to_class(InPR, x), x), from_none], self.prs)
        return result


class Section(Enum):
    ALPHA = "alpha"
    BIOG = "biog"
    GEOG = "geog"
    IDIOMS = "idioms"


class Src(Enum):
    COLLEGIATE = "collegiate"
    LD = "ld"


class Meta:
    id: Optional[str]
    uuid: Optional[UUID]
    sort: Optional[str]
    src: Optional[Src]
    section: Optional[Section]
    stems: Optional[List[str]]
    offensive: Optional[bool]

    def __init__(self, id: Optional[str], uuid: Optional[UUID], sort: Optional[str], src: Optional[Src], section: Optional[Section], stems: Optional[List[str]], offensive: Optional[bool]) -> None:
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
        src = from_union([Src, from_none], obj.get("src"))
        section = from_union([Section, from_none], obj.get("section"))
        stems = from_union([lambda x: from_list(from_str, x), from_none], obj.get("stems"))
        offensive = from_union([from_bool, from_none], obj.get("offensive"))
        return Meta(id, uuid, sort, src, section, stems, offensive)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["uuid"] = from_union([lambda x: str(x), from_none], self.uuid)
        result["sort"] = from_union([from_str, from_none], self.sort)
        result["src"] = from_union([lambda x: to_enum(Src, x), from_none], self.src)
        result["section"] = from_union([lambda x: to_enum(Section, x), from_none], self.section)
        result["stems"] = from_union([lambda x: from_list(from_str, x), from_none], self.stems)
        result["offensive"] = from_union([from_bool, from_none], self.offensive)
        return result


class PtClass:
    t: Optional[str]

    def __init__(self, t: Optional[str]) -> None:
        self.t = t

    @staticmethod
    def from_dict(obj: Any) -> 'PtClass':
        assert isinstance(obj, dict)
        t = from_union([from_str, from_none], obj.get("t"))
        return PtClass(t)

    def to_dict(self) -> dict:
        result: dict = {}
        result["t"] = from_union([from_str, from_none], self.t)
        return result


class Syn:
    pl: Optional[str]
    pt: Optional[List[List[Union[List[PtClass], str]]]]

    def __init__(self, pl: Optional[str], pt: Optional[List[List[Union[List[PtClass], str]]]]) -> None:
        self.pl = pl
        self.pt = pt

    @staticmethod
    def from_dict(obj: Any) -> 'Syn':
        assert isinstance(obj, dict)
        pl = from_union([from_str, from_none], obj.get("pl"))
        pt = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: from_list(PtClass.from_dict, x), from_str], x), x), x), from_none], obj.get("pt"))
        return Syn(pl, pt)

    def to_dict(self) -> dict:
        result: dict = {}
        result["pl"] = from_union([from_str, from_none], self.pl)
        result["pt"] = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: from_list(lambda x: to_class(PtClass, x), x), from_str], x), x), x), from_none], self.pt)
        return result


class Uro:
    ure: Optional[str]
    fl: Optional[FL]
    prs: Optional[List[InPR]]

    def __init__(self, ure: Optional[str], fl: Optional[FL], prs: Optional[List[InPR]]) -> None:
        self.ure = ure
        self.fl = fl
        self.prs = prs

    @staticmethod
    def from_dict(obj: Any) -> 'Uro':
        assert isinstance(obj, dict)
        ure = from_union([from_str, from_none], obj.get("ure"))
        fl = from_union([FL, from_none], obj.get("fl"))
        prs = from_union([lambda x: from_list(InPR.from_dict, x), from_none], obj.get("prs"))
        return Uro(ure, fl, prs)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ure"] = from_union([from_str, from_none], self.ure)
        result["fl"] = from_union([lambda x: to_enum(FL, x), from_none], self.fl)
        result["prs"] = from_union([lambda x: from_list(lambda x: to_class(InPR, x), x), from_none], self.prs)
        return result


class SD(Enum):
    ALSO = "also"
    ESPECIALLY = "especially"


class PurpleSdsense:
    sd: Optional[SD]
    dt: Optional[List[List[str]]]

    def __init__(self, sd: Optional[SD], dt: Optional[List[List[str]]]) -> None:
        self.sd = sd
        self.dt = dt

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleSdsense':
        assert isinstance(obj, dict)
        sd = from_union([SD, from_none], obj.get("sd"))
        dt = from_union([lambda x: from_list(lambda x: from_list(from_str, x), x), from_none], obj.get("dt"))
        return PurpleSdsense(sd, dt)

    def to_dict(self) -> dict:
        result: dict = {}
        result["sd"] = from_union([lambda x: to_enum(SD, x), from_none], self.sd)
        result["dt"] = from_union([lambda x: from_list(lambda x: from_list(from_str, x), x), from_none], self.dt)
        return result


class Sense:
    sn: Union[Ref, int, None]
    dt: Optional[List[List[str]]]

    def __init__(self, sn: Union[Ref, int, None], dt: Optional[List[List[str]]]) -> None:
        self.sn = sn
        self.dt = dt

    @staticmethod
    def from_dict(obj: Any) -> 'Sense':
        assert isinstance(obj, dict)
        sn = from_union([from_none, lambda x: from_union([Ref, lambda x: int(x)], from_str(x))], obj.get("sn"))
        dt = from_union([lambda x: from_list(lambda x: from_list(from_str, x), x), from_none], obj.get("dt"))
        return Sense(sn, dt)

    def to_dict(self) -> dict:
        result: dict = {}
        result["sn"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: to_enum(Ref, (lambda x: is_type(Ref, x))(x)))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.sn)
        result["dt"] = from_union([lambda x: from_list(lambda x: from_list(from_str, x), x), from_none], self.dt)
        return result


class PurpleSseq:
    sn: Optional[str]
    dt: Optional[List[List[Union[List[PtClass], str]]]]
    sdsense: Optional[PurpleSdsense]
    sense: Optional[Sense]

    def __init__(self, sn: Optional[str], dt: Optional[List[List[Union[List[PtClass], str]]]], sdsense: Optional[PurpleSdsense], sense: Optional[Sense]) -> None:
        self.sn = sn
        self.dt = dt
        self.sdsense = sdsense
        self.sense = sense

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleSseq':
        assert isinstance(obj, dict)
        sn = from_union([from_str, from_none], obj.get("sn"))
        dt = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: from_list(PtClass.from_dict, x), from_str], x), x), x), from_none], obj.get("dt"))
        sdsense = from_union([PurpleSdsense.from_dict, from_none], obj.get("sdsense"))
        sense = from_union([Sense.from_dict, from_none], obj.get("sense"))
        return PurpleSseq(sn, dt, sdsense, sense)

    def to_dict(self) -> dict:
        result: dict = {}
        result["sn"] = from_union([from_str, from_none], self.sn)
        result["dt"] = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: from_list(lambda x: to_class(PtClass, x), x), from_str], x), x), x), from_none], self.dt)
        result["sdsense"] = from_union([lambda x: to_class(PurpleSdsense, x), from_none], self.sdsense)
        result["sense"] = from_union([lambda x: to_class(Sense, x), from_none], self.sense)
        return result


class FluffyAq:
    auth: Optional[str]
    source: Optional[str]

    def __init__(self, auth: Optional[str], source: Optional[str]) -> None:
        self.auth = auth
        self.source = source

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyAq':
        assert isinstance(obj, dict)
        auth = from_union([from_str, from_none], obj.get("auth"))
        source = from_union([from_str, from_none], obj.get("source"))
        return FluffyAq(auth, source)

    def to_dict(self) -> dict:
        result: dict = {}
        result["auth"] = from_union([from_str, from_none], self.auth)
        result["source"] = from_union([from_str, from_none], self.source)
        return result


class FluffyDt:
    t: Optional[str]
    aq: Optional[FluffyAq]

    def __init__(self, t: Optional[str], aq: Optional[FluffyAq]) -> None:
        self.t = t
        self.aq = aq

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyDt':
        assert isinstance(obj, dict)
        t = from_union([from_str, from_none], obj.get("t"))
        aq = from_union([FluffyAq.from_dict, from_none], obj.get("aq"))
        return FluffyDt(t, aq)

    def to_dict(self) -> dict:
        result: dict = {}
        result["t"] = from_union([from_str, from_none], self.t)
        result["aq"] = from_union([lambda x: to_class(FluffyAq, x), from_none], self.aq)
        return result


class Cat:
    cat: Optional[str]

    def __init__(self, cat: Optional[str]) -> None:
        self.cat = cat

    @staticmethod
    def from_dict(obj: Any) -> 'Cat':
        assert isinstance(obj, dict)
        cat = from_union([from_str, from_none], obj.get("cat"))
        return Cat(cat)

    def to_dict(self) -> dict:
        result: dict = {}
        result["cat"] = from_union([from_str, from_none], self.cat)
        return result


class TentacledDt:
    intro: Optional[str]
    cats: Optional[List[Cat]]

    def __init__(self, intro: Optional[str], cats: Optional[List[Cat]]) -> None:
        self.intro = intro
        self.cats = cats

    @staticmethod
    def from_dict(obj: Any) -> 'TentacledDt':
        assert isinstance(obj, dict)
        intro = from_union([from_str, from_none], obj.get("intro"))
        cats = from_union([lambda x: from_list(Cat.from_dict, x), from_none], obj.get("cats"))
        return TentacledDt(intro, cats)

    def to_dict(self) -> dict:
        result: dict = {}
        result["intro"] = from_union([from_str, from_none], self.intro)
        result["cats"] = from_union([lambda x: from_list(lambda x: to_class(Cat, x), x), from_none], self.cats)
        return result


class FluffySdsense:
    sd: Optional[SD]
    dt: Optional[List[List[Union[List[Union[List[List[str]], PtClass]], str]]]]

    def __init__(self, sd: Optional[SD], dt: Optional[List[List[Union[List[Union[List[List[str]], PtClass]], str]]]]) -> None:
        self.sd = sd
        self.dt = dt

    @staticmethod
    def from_dict(obj: Any) -> 'FluffySdsense':
        assert isinstance(obj, dict)
        sd = from_union([SD, from_none], obj.get("sd"))
        dt = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: from_list(lambda x: from_union([PtClass.from_dict, lambda x: from_list(lambda x: from_list(from_str, x), x)], x), x), from_str], x), x), x), from_none], obj.get("dt"))
        return FluffySdsense(sd, dt)

    def to_dict(self) -> dict:
        result: dict = {}
        result["sd"] = from_union([lambda x: to_enum(SD, x), from_none], self.sd)
        result["dt"] = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: from_list(lambda x: from_union([lambda x: to_class(PtClass, x), lambda x: from_list(lambda x: from_list(from_str, x), x)], x), x), from_str], x), x), x), from_none], self.dt)
        return result


class FluffySseq:
    sense: Optional[Sense]
    sn: Optional[str]
    dt: Optional[List[List[Union[List[Union[List[Union[List[Union[List[Union[PurpleDt, str]], str]], str]], FluffyDt]], TentacledDt, str]]]]
    sdsense: Optional[FluffySdsense]
    sls: Optional[List[str]]

    def __init__(self, sense: Optional[Sense], sn: Optional[str], dt: Optional[List[List[Union[List[Union[List[Union[List[Union[List[Union[PurpleDt, str]], str]], str]], FluffyDt]], TentacledDt, str]]]], sdsense: Optional[FluffySdsense], sls: Optional[List[str]]) -> None:
        self.sense = sense
        self.sn = sn
        self.dt = dt
        self.sdsense = sdsense
        self.sls = sls

    @staticmethod
    def from_dict(obj: Any) -> 'FluffySseq':
        assert isinstance(obj, dict)
        sense = from_union([Sense.from_dict, from_none], obj.get("sense"))
        sn = from_union([from_str, from_none], obj.get("sn"))
        dt = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: from_list(lambda x: from_union([FluffyDt.from_dict, lambda x: from_list(lambda x: from_union([lambda x: from_list(lambda x: from_union([lambda x: from_list(lambda x: from_union([PurpleDt.from_dict, from_str], x), x), from_str], x), x), from_str], x), x)], x), x), TentacledDt.from_dict, from_str], x), x), x), from_none], obj.get("dt"))
        sdsense = from_union([FluffySdsense.from_dict, from_none], obj.get("sdsense"))
        sls = from_union([lambda x: from_list(from_str, x), from_none], obj.get("sls"))
        return FluffySseq(sense, sn, dt, sdsense, sls)

    def to_dict(self) -> dict:
        result: dict = {}
        result["sense"] = from_union([lambda x: to_class(Sense, x), from_none], self.sense)
        result["sn"] = from_union([from_str, from_none], self.sn)
        result["dt"] = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: from_list(lambda x: from_union([lambda x: to_class(FluffyDt, x), lambda x: from_list(lambda x: from_union([lambda x: from_list(lambda x: from_union([lambda x: from_list(lambda x: from_union([lambda x: to_class(PurpleDt, x), from_str], x), x), from_str], x), x), from_str], x), x)], x), x), lambda x: to_class(TentacledDt, x), from_str], x), x), x), from_none], self.dt)
        result["sdsense"] = from_union([lambda x: to_class(FluffySdsense, x), from_none], self.sdsense)
        result["sls"] = from_union([lambda x: from_list(from_str, x), from_none], self.sls)
        return result


class Vd(Enum):
    INTRANSITIVE_VERB = "intransitive verb"
    TRANSITIVE_VERB = "transitive verb"


class WelcomeDef:
    sseq: Optional[List[List[List[Union[List[List[Union[PurpleSseq, SseqEnum]]], FluffySseq, SseqEnum]]]]]
    vd: Optional[Vd]
    sls: Optional[List[str]]

    def __init__(self, sseq: Optional[List[List[List[Union[List[List[Union[PurpleSseq, SseqEnum]]], FluffySseq, SseqEnum]]]]], vd: Optional[Vd], sls: Optional[List[str]]) -> None:
        self.sseq = sseq
        self.vd = vd
        self.sls = sls

    @staticmethod
    def from_dict(obj: Any) -> 'WelcomeDef':
        assert isinstance(obj, dict)
        sseq = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_list(lambda x: from_union([FluffySseq.from_dict, lambda x: from_list(lambda x: from_list(lambda x: from_union([PurpleSseq.from_dict, SseqEnum], x), x), x), SseqEnum], x), x), x), x), from_none], obj.get("sseq"))
        vd = from_union([Vd, from_none], obj.get("vd"))
        sls = from_union([lambda x: from_list(from_str, x), from_none], obj.get("sls"))
        return WelcomeDef(sseq, vd, sls)

    def to_dict(self) -> dict:
        result: dict = {}
        result["sseq"] = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: to_class(FluffySseq, x), lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: to_class(PurpleSseq, x), lambda x: to_enum(SseqEnum, x)], x), x), x), lambda x: to_enum(SseqEnum, x)], x), x), x), x), from_none], self.sseq)
        result["vd"] = from_union([lambda x: to_enum(Vd, x), from_none], self.vd)
        result["sls"] = from_union([lambda x: from_list(from_str, x), from_none], self.sls)
        return result


class WelcomeElement:
    meta: Optional[Meta]
    hom: Optional[int]
    hwi: Optional[Hwi]
    fl: Optional[FL]
    welcome_def: Optional[List[WelcomeDef]]
    et: Optional[List[List[Union[List[List[str]], str]]]]
    date: Optional[str]
    shortdef: Optional[List[str]]
    ins: Optional[List[In]]
    uros: Optional[List[Uro]]
    lbs: Optional[List[str]]
    art: Optional[Art]
    vrs: Optional[List[VR]]
    syns: Optional[List[Syn]]
    dros: Optional[List[Dro]]

    def __init__(self, meta: Optional[Meta], hom: Optional[int], hwi: Optional[Hwi], fl: Optional[FL], welcome_def: Optional[List[WelcomeDef]], et: Optional[List[List[Union[List[List[str]], str]]]], date: Optional[str], shortdef: Optional[List[str]], ins: Optional[List[In]], uros: Optional[List[Uro]], lbs: Optional[List[str]], art: Optional[Art], vrs: Optional[List[VR]], syns: Optional[List[Syn]], dros: Optional[List[Dro]]) -> None:
        self.meta = meta
        self.hom = hom
        self.hwi = hwi
        self.fl = fl
        self.welcome_def = welcome_def
        self.et = et
        self.date = date
        self.shortdef = shortdef
        self.ins = ins
        self.uros = uros
        self.lbs = lbs
        self.art = art
        self.vrs = vrs
        self.syns = syns
        self.dros = dros

    @staticmethod
    def from_dict(obj: Any) -> 'WelcomeElement':
        assert isinstance(obj, dict)
        meta = from_union([Meta.from_dict, from_none], obj.get("meta"))
        hom = from_union([from_int, from_none], obj.get("hom"))
        hwi = from_union([Hwi.from_dict, from_none], obj.get("hwi"))
        fl = from_union([FL, from_none], obj.get("fl"))
        welcome_def = from_union([lambda x: from_list(WelcomeDef.from_dict, x), from_none], obj.get("def"))
        et = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: from_list(lambda x: from_list(from_str, x), x), from_str], x), x), x), from_none], obj.get("et"))
        date = from_union([from_str, from_none], obj.get("date"))
        shortdef = from_union([lambda x: from_list(from_str, x), from_none], obj.get("shortdef"))
        ins = from_union([lambda x: from_list(In.from_dict, x), from_none], obj.get("ins"))
        uros = from_union([lambda x: from_list(Uro.from_dict, x), from_none], obj.get("uros"))
        lbs = from_union([lambda x: from_list(from_str, x), from_none], obj.get("lbs"))
        art = from_union([Art.from_dict, from_none], obj.get("art"))
        vrs = from_union([lambda x: from_list(VR.from_dict, x), from_none], obj.get("vrs"))
        syns = from_union([lambda x: from_list(Syn.from_dict, x), from_none], obj.get("syns"))
        dros = from_union([lambda x: from_list(Dro.from_dict, x), from_none], obj.get("dros"))
        return WelcomeElement(meta, hom, hwi, fl, welcome_def, et, date, shortdef, ins, uros, lbs, art, vrs, syns, dros)

    def to_dict(self) -> dict:
        result: dict = {}
        result["meta"] = from_union([lambda x: to_class(Meta, x), from_none], self.meta)
        result["hom"] = from_union([from_int, from_none], self.hom)
        result["hwi"] = from_union([lambda x: to_class(Hwi, x), from_none], self.hwi)
        result["fl"] = from_union([lambda x: to_enum(FL, x), from_none], self.fl)
        result["def"] = from_union([lambda x: from_list(lambda x: to_class(WelcomeDef, x), x), from_none], self.welcome_def)
        result["et"] = from_union([lambda x: from_list(lambda x: from_list(lambda x: from_union([lambda x: from_list(lambda x: from_list(from_str, x), x), from_str], x), x), x), from_none], self.et)
        result["date"] = from_union([from_str, from_none], self.date)
        result["shortdef"] = from_union([lambda x: from_list(from_str, x), from_none], self.shortdef)
        result["ins"] = from_union([lambda x: from_list(lambda x: to_class(In, x), x), from_none], self.ins)
        result["uros"] = from_union([lambda x: from_list(lambda x: to_class(Uro, x), x), from_none], self.uros)
        result["lbs"] = from_union([lambda x: from_list(from_str, x), from_none], self.lbs)
        result["art"] = from_union([lambda x: to_class(Art, x), from_none], self.art)
        result["vrs"] = from_union([lambda x: from_list(lambda x: to_class(VR, x), x), from_none], self.vrs)
        result["syns"] = from_union([lambda x: from_list(lambda x: to_class(Syn, x), x), from_none], self.syns)
        result["dros"] = from_union([lambda x: from_list(lambda x: to_class(Dro, x), x), from_none], self.dros)
        return result


def welcome_from_dict(s: Any) -> List[WelcomeElement]:
    return from_list(WelcomeElement.from_dict, s)


def welcome_to_dict(x: List[WelcomeElement]) -> Any:
    return from_list(lambda x: to_class(WelcomeElement, x), x)
