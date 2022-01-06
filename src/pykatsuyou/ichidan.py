from .dataframes import CreateDataFrame

class Ichidan:
    '''
    Ichidan are the verbs that end in -る
    
    Available methods:
    @method getForms() - returns a dataframe or json with the forms
    @method getRules() - returns the rules of the verb

    Example:
    
    ichi = Ichidan()

    ichi.getForms('上げる')

    '''
    def __init__(self):
        self.rules = {
            'Affirmative': ['る', 'ます', 'た', 'ました', 'て', 'ろ', 'れば', 'よう'],
            'Negative': ['ない', 'ません', 'なかった', 'ませんでした', 'なくて', 'な', 'ｘ', 'ｘ']
        }

    def getRules(self):
        return self.rules

    def applyRules(self, verb: str):
        cutVerb = verb.replace('る', '')
        affirmative = []
        negative = []
        for value in self.rules['Affirmative']:
            affirmative.append(cutVerb + value)
        for value in self.rules['Negative']:
            if value == 'ｘ':
                negative.append(value)
            else:
                if self.rules['Negative'].index(value) == 5:
                    negative.append(verb + value)
                else: 
                    negative.append(cutVerb + value)
            
        return affirmative, negative

    def getForms(self, verb: str):
        '''
        Get the ru form

        @param verb - needs dictionary form
        '''
        affirmative, negative = self.applyRules(verb)

        data = CreateDataFrame({'Affirmative': affirmative, 'Negative': negative}, 'Ichidan Verb').createDataFrame()
        return data