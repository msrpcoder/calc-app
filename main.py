"""
Module level docstring.
"""


class Calc:
    '''class-level docstring.'''

    def __init__(self, operator, param1, param2):
        '''
        constructor method

        :param operator <operator docs>
        :param param1 <param1 docs>
        :param param2 <param2 docs>
        '''
        self.operator = operator
        self.param1 = param1
        self.param2 = param2

    def calculate(self):
        '''calculate docstring'''
        method = getattr(self, self.operator, None)
        if not method:
            raise Exception(f'Invalid operator: {self.operator}')

        return method()

    def add(self):
        '''add docstring'''
        return self.param1 + self.param2

    def minus(self):
        '''minus docstring'''
        return self.param1 - self.param2


def start_app():
    '''start_app() docstring'''
    return {
        'add': Calc('add', 21, 38).calculate(),
        'minus': Calc('minus', 4, 2).calculate()
    }

if __name__ == '__main__':
    print(start_app())
