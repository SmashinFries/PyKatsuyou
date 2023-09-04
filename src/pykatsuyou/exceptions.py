class UnknownVerbError(Exception):

    def __init__(self, verb, *args):
        super().__init__(args)
        self.verb = verb

    def __str__(self):
        return f'Unable to get inflections of {self.verb}. \nTake a look at this issue for more information: https://github.com/SmashinFries/PyKatsuyou/issues/2'