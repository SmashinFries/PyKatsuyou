from .dataframes import CreateDataFrame

class Ichidan:
    '''
    Ichidan are the verbs that end in -る
    
    Available methods:
    @method getForms() - returns a dataframe or json with the forms
    @method getRules() - returns the rules of the verb

    Example:
    
    ichi = Ichidan()

    ichi.getForms('あそぶ')

    '''
    def __init__(self):
        self.rules = {
            'Affirmative': ['る', 'ます', 'た', 'ました', 'て', 'ろ', 'れば', 'よう'],
            'Negative': ['ない', 'ません', 'なかった', 'ませんでした', 'なくて', 'な', 'ｘ', 'ｘ']
        }

    def getRules(self):
        return self.rules

    def useRules(self, verb: str):
        cutVerb = verb.replace('る', '')
        data = {'Affirmative': [], 'Negative': []}
        for value in self.rules['Affirmative']:
            data['Affirmative'].append(cutVerb + value)
        for value in self.rules['Negative']:
            if value == 'ｘ':
                data['Negative'].append(value)
            else:
                if self.rules['Negative'].index(value) == 5:
                    data['Negative'].append(verb + value)
                else: 
                    data['Negative'].append(cutVerb + value)
            
        return data 

    def getForms(self, verb: str):
        '''
        Get the ru form

        @param verb - needs dictionary form
        '''
        results = self.useRules(verb)

        data = CreateDataFrame(results, 'Ichidan Verb').createDataFrame()
        return data