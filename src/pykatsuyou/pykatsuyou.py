# -*- coding: utf-8 -*-

from pandas.core.frame import DataFrame
from igo.tagger import Tagger
from jaconv import kata2hira
from .godan import Godan
from .ichidan import Ichidan
from .iAdj import IAdj
from .irregulars import IrregularVerb

def getInflections(text: str, jsonIndent: int = 0, dataframe:bool = False):
    """
    Get the inflections of a verb or adjective.

    Parameters
    ----------
    text : string, required
        Requires dictionary form. Using only hiragana may provide inaccurate results.

    jsonIndent : int, default 0
        Indentation length of the JSON output. Default is 0.

    dataframe : bool, default False
        Whether or not to return a dataframe instead of object

    Returns
    -------
    An object containing JSON/List or a dataframe

    Example
    -------

    >>> result = getInflections('行く', dataframe:True)
    >>> print(tabulate(result, headers='keys', tablefmt='pretty'))

    """
    
    # Too many if statements?😅

    PAIRS = {
    # V     V    ka    ga    sa    za  　ta    da    na    ha    ba    ma    ya   ra    wa
    'あ': ['あ', 'か', 'が', 'さ', 'ざ', 'た', 'だ', 'な', 'は', 'ば', 'ま', 'や', 'ら', 'わ'], 
    'い': ['い', 'き', 'ぎ', 'し', 'じ', 'ち', 'ぢ', 'に', 'ひ', 'び', 'み', 'ー', 'り', 'ー'], 
    'う': ['う', 'く', 'ぐ', 'す', 'ず', 'つ', 'づ', 'ぬ', 'ふ', 'ぶ', 'む', 'ゆ', 'る', 'ー'], 
    'え': ['え', 'け', 'げ', 'せ', 'ぜ', 'て', 'で', 'ね', 'へ', 'べ', 'め', 'ー', 'れ', 'ー'],
    'お': ['お', 'こ', 'ご', 'そ', 'ぞ', 'と', 'ど', 'の', 'ほ', 'ぼ', 'も', 'よ', 'ろ', 'を'],
    }
    EXCEPTIONS = ['入る', '走る', '要る', '帰る', '限る', '切る', '喋る', '知る', '湿る', 'しゃべる', '減る', '焦る', '蹴る', '滑る', '握る', '練る', '参る', '交じる', '嘲る', '覆る', '遮る', '罵る', '捻る', '翻る', '滅入る', '蘇る']
    IRREGULARS = ['する', '為る', 'くる', '来る']

    tt = Tagger()
    check = tt.parse(text)
    temp = check[-1].feature.split(',')
    hira = kata2hira(temp[-1])
    
    go = Godan(hira)
    ichi = Ichidan()
    iadj = IAdj()
    irreg = IrregularVerb()
    data: DataFrame = {}

    def isVerb() -> bool:
        if '動詞' in check[-1].feature:
            return True
        else:
            return False

    def isAdj() -> bool:
        check = tt.parse(text)
        if '形容詞' in check[-1].feature:
            return True
        else:
            return False

    def ruDecider3000():
        if (hira[-2] in PAIRS['あ']) or (hira[-2] in PAIRS['う']) or (hira[-2] in PAIRS['お'] or (text in EXCEPTIONS)):
            # It is GODAN
            result = go.getForms(text)
            return result
        elif (hira[-2] in PAIRS['い'] or hira[-2] in PAIRS['え'] and text not in EXCEPTIONS):
            # It is ICHIDAN
            result = ichi.getForms(text)
            return result
        else:
            print('Failed:', hira[-2])

    def finalizeVerb(data):
        # Get Data
        if text not in IRREGULARS:
            if text[-1] == 'る':
                data = ruDecider3000()
            else:
                result = go.getForms(text)
                data = result
        else:
            data = irreg.getForms(text)
            pass
        
        # Finalize
        if dataframe:
            return data
        else:
            dataArr = []
            for item in list(data['Affirmative'].values[1:]):
                dataArr.append(item)
            for item in list(data['Negative'].values[1:]):
                if item == 'ｘ':
                    pass
                else:
                    dataArr.append(item)
            return {'json': data.to_json(force_ascii=False, indent=jsonIndent), 'list': dataArr}

    def finalizeAdj(data):
        result = iadj.getForms(text)
        data = result

        if dataframe:
            return data
        else:
            dataArr = []
            for item in list(data['Affirmative'].values[1:]):
                dataArr.append(item)
            for item in list(data['Negative'].values[1:]):
                if item == 'ｘ':
                    pass
                else:
                    dataArr.append(item)
            return {'json': data.to_json(force_ascii=False, indent=jsonIndent), 'list': dataArr}

    if isVerb():
        final = finalizeVerb(data)
        return final
    elif isAdj():
        final = finalizeAdj(data)
        return final
    else:
        return {'json': 'ⓧ', 'list': ['Not a verb/adjective']}
