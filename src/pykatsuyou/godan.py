from .dataframes import CreateDataFrame

PAIRS = {
    # V     V    ka    ga    sa    zo  　ta    da    na    ha    ba    ma    ya   ra    wa
    'あ': ['あ', 'か', 'が', 'さ', 'ざ', 'た', 'だ', 'な', 'は', 'ば', 'ま', 'や', 'ら', 'わ'], 
    'い': ['い', 'き', 'ぎ', 'し', 'じ', 'ち', 'ぢ', 'に', 'ひ', 'び', 'み', 'ー', 'り', 'ー'], 
    'う': ['う', 'く', 'ぐ', 'す', 'ず', 'つ', 'づ', 'ぬ', 'ふ', 'ぶ', 'む', 'ゆ', 'る', 'ー'], 
    'え': ['え', 'け', 'げ', 'せ', 'ぜ', 'て', 'で', 'ね', 'へ', 'べ', 'め', 'ー', 'れ', 'ー'],
    'お': ['お', 'こ', 'ご', 'そ', 'ぞ', 'と', 'ど', 'の', 'ほ', 'ぼ', 'も', 'よ', 'ろ', 'を'],
    }

class Godan:
    # あ - negative
    # い - infinitive
    # う - dictionary
    # え - conditional
    # お - volitional

    def __init__(self, hira:str) -> None:
        # ['Non-Past/Dict-Form', 'Non-Past Polite', 'Past Polite', 'Past', 'Te-Form', 'Imperative', 'Conditional', 'Volitional']
        # If う then use わ (NEGATIVE)
        # まい for neg volitional?
        self.rules = {
            'Affirmative': ['う', 'います', 'いた', 'いました', 'いて', 'え', 'えば', 'おう'],
            'Negative': ['あない', 'いません', 'あなかった', 'いませんでした', 'あなくて', 'うな', 'あなければ', 'ｘ']
        }
        self.hira = hira
        self.checkIndex = [2, 4]
        self.uIndexNeg = [0, 2, 4, 6]
        self.mnbStems = ['ま', 'む', 'も', 'な', 'ぬ', 'の', 'ば', 'ぶ', 'ぼ']
        self.wtrStems = ['わ', 'を', 'た', 'つ', 'と', 'ら', 'る', 'ろ']
        self.gStems = ['が', 'ぐ', 'ご']
        self.kStems = ['か', 'く', 'こ']
    
    def checkVerbType(self, verb:str) -> int:
        loc = -1
        for key in PAIRS.keys():
            if verb[-1] in PAIRS[key]:
                loc = PAIRS[key].index(verb[-1])
                break
        
        return loc

    def nonU(self, verb:str, loc:int, data:dict):
        for value in self.rules['Affirmative']:
            if self.rules['Affirmative'].index(value) in self.checkIndex:
                # If iku then...
                if self.hira[-2:] == 'いく':
                    data['Affirmative'].append(verb[:-1] + (value[:0] + 'っ' + value[1:]))
                # If has m~, n~, b~ then...
                elif self.hira[-1] in self.mnbStems:
                    if self.rules['Affirmative'].index(value) == 3:
                        data['Affirmative'].append(verb[:-1] + 'んだ')
                    elif self.rules['Affirmative'].index(value) == 4:
                        data['Affirmative'].append(verb[:-1] + 'んで')
                    else:
                        data['Affirmative'].append(verb[:-1] + value)
                # If has w~, t~, r~ then...
                elif self.hira[-1] in self.wtrStems:
                    if self.rules['Affirmative'].index(value) == 3 or self.rules['Affirmative'].index(value) == 4:
                        data['Affirmative'].append(verb[:-1] + (value[:0] + 'っ' + value[1:]))
                    else:
                        data['Affirmative'].append(verb[:-1] + value)
                # If has k~ then...
                elif self.hira[-1] in self.kStems:
                    if self.rules['Affirmative'].index(value) == 3:
                        data['Affirmative'].append(verb[:-1] + 'いた')
                    elif self.rules['Affirmative'].index(value) == 4:
                        data['Affirmative'].append(verb[:-1] + 'いて')
                # If has g~ then...
                elif self.hira[-1] in self.gStems:
                    if self.rules['Affirmative'].index(value) == 3:
                        data['Affirmative'].append(verb[:-1] + 'いだ')
                    elif self.rules['Affirmative'].index(value) == 4:
                        data['Affirmative'].append(verb[:-1] + 'いで')
                else:
                    data['Affirmative'].append(verb[:-1] + PAIRS[value[0]][loc] + value[1:])
            else: 
                data['Affirmative'].append(verb[:-1] + PAIRS[value[0]][loc] + value[1:])
        for value in self.rules['Negative']:
            if value == 'ｘ':
                data['Negative'].append(value)
            else: 
                data['Negative'].append(verb[:-1] + PAIRS[value[0]][loc] + value[1:])

    def isU(self, verb:str, loc:int, data:dict):
        for value in self.rules['Affirmative']:
            if self.rules['Affirmative'].index(value) in self.checkIndex:
                data['Affirmative'].append(verb[:-1] + (value[:0] + 'っ' + value[1:]))
            else: 
                data['Affirmative'].append(verb[:-1] + PAIRS[value[0]][loc] + value[1:])
        for value in self.rules['Negative']:
            if value == 'ｘ':
                data['Negative'].append(value)
            elif (self.rules['Negative'].index(value) in self.uIndexNeg):
                data['Negative'].append(verb[:-1] + (value[:0] + 'わ' + value[1:]))
            else: 
                data['Negative'].append(verb[:-1] + PAIRS[value[0]][loc] + value[1:])

    def getForms(self, verb):
        def useRules():
            loc = self.checkVerbType(verb)
            data = {'Affirmative': [], 'Negative': []}
            if loc != -1:
                if verb[-1] != 'う':
                    self.nonU(verb, loc, data)
                elif verb[-1] == 'う':
                    self.isU(verb, loc, data)
            return data
        result = useRules()
        data = CreateDataFrame(result, 'Godan Verb').createDataFrame()
        return data