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
        data = {'Affirmative': [], 'Negative': []}
        if adj[-2:] == 'いい':
            for value in self.rules['Affirmative']:
                if self.rules['Affirmative'].index(value) == 1:
                    data['Affirmative'].append(cutAdj + 'よ' + value)
                else:
                    data['Affirmative'].append(adj)
            for value in self.rules['Negative']:
                data['Negative'].append(cutAdj + value)
        else:
            for value in self.rules['Affirmative']:
                data['Affirmative'].append(cutAdj + value)
            for value in self.rules['Negative']:
                data['Negative'].append(cutAdj + value)
        return(data)

    def getForms(self, adj: str):
        '''
        Get the い-Adjective inflections

        @param adj - needs plain adjective
        '''
        results = self.useRules(adj)

        data = CreateDataFrame(results, 'い Adjective').createDataFrame()
        return data