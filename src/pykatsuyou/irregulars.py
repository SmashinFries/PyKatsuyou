# INDEX_VERBS = ['Non-Past/Dict-Form', 'Non-Past Polite', 'Past Polite', 'Past', 'Te-Form', 'Imperative', 'Conditional', 'Volitional']
from .dataframes import CreateDataFrame

class IrregularVerb:
    def __init__(self) -> None:
        self.rulesSuru = {
            'Affirmative': ['する', 'します', 'した', 'しました', 'して', 'しろ', 'すれば', 'しよう'],
            'Negative': ['しない', 'しません', 'しなかった', 'しませんでした', 'しなくて', 'するな', 'しなければ', 'ｘ']
        }
        self.rulesKuru = {
            'Affirmative': ['くる', 'きます', 'きた', 'きました', 'きて', 'こい', 'くれば', 'こよう'],
            'Negative': ['こない', 'きません', 'こなかった', 'きませんでした', 'こなくて', 'くるな', 'こなければ', 'ｘ']
        }

    def getForms(self, verb:str) -> dict:
        data = {'Affirmative': [], 'Negative': []}
        if verb == 'する' or verb == '為る':
            data['Affirmative'] = self.rulesSuru['Affirmative']
            data['Negative'] = self.rulesSuru['Negative']
        elif verb == 'くる' or verb == '来る':
            data['Affirmative'] = self.rulesKuru['Affirmative']
            data['Negative'] = self.rulesKuru['Negative']
        
        return CreateDataFrame(data, 'Irregular Verb').createDataFrame()