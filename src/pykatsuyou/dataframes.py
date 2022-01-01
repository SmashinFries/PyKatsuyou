import pandas as pd

INDEX_VERBS = ['Dict-Form', 'Non-Past Polite', 'Past', 'Past Polite', 'Te-Form', 'Imperative', 'Conditional', 'Volitional']
INDEX_ADJ = ['Non-Past', 'Past']

class CreateDataFrame:
    def __init__(self, data: dict, type:str) -> None:
        self.data = data
        self.type = type

    def checkIndex(self):
        splitted = self.type.split(' ')
        if splitted[-1] == 'Verb':
            return INDEX_VERBS
        else:
            return INDEX_ADJ
    
    def createDataFrame(self):

        df = pd.DataFrame(self.data, index=self.checkIndex())
        df.index.name = self.type
        return df