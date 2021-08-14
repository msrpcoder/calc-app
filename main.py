"""
Module level docstring.
"""
import os
import time


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


def start_app(no_of_times, sleep_time):
    '''start_app() docstring'''
    for _ in range(no_of_times):
        print({
            'add': Calc('add', 21, 38).calculate(),
            'minus': Calc('minus', 4, 2).calculate()
        })
        time.sleep(sleep_time)


NO_OF_TIMES = int(os.environ.get('TIMES', 5))
SLEEP_TIME = int(os.environ.get('SLEEP_TIME', 5))

if __name__ == '__main__':
    start_app(NO_OF_TIMES, SLEEP_TIME)
