from .dataframes import CreateDataFrame

class IAdj:
    # 良い or いい・よい always uses よい when conjugated
    # Any adj ending in -いい is always treated as よい
    # Kawaii does not conjugate to よい and is treated normally
    def __init__(self) -> None:
        self.rules = {
            # [Present, Past]
            'Affirmative': ['い', 'かった'],
            'Negative': ['くない', 'くなかった']
        }
    
    def useRules(self, adj: str):
        cutAdj = adj.replace('い', '')
        affirmative = []
        negative = []
        if adj[-2:] == 'いい':
            for value in self.rules['Affirmative']:
                if self.rules['Affirmative'].index(value) == 1:
                    affirmative.append(cutAdj + 'よ' + value)
                else:
                    affirmative.append(adj)
            for value in self.rules['Negative']:
                negative.append(cutAdj + value)
        else:
            for value in self.rules['Affirmative']:
                affirmative.append(cutAdj + value)
            for value in self.rules['Negative']:
                negative.append(cutAdj + value)
        return affirmative, negative

    def getForms(self, adj: str):
        '''
        Get the い-Adjective inflections

        @param adj - needs plain adjective
        '''
        affirmative, negative = self.useRules(adj)

        data = CreateDataFrame({'Affirmative': affirmative, 'Negative': negative}, 'い Adjective').createDataFrame()
        return data