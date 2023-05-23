#1
import logging

class Calculator:
    def __init__(self):
        self.logger = logging.getLogger('Calculator')
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(logging.StreamHandler())
    def add(self, a, b):
        result =  a + b
        self.logger.info(f'{a} + {b} = {result}')
        return result
    def sub(self, a ,b):
        result = a - b
        self.logger.info(f'{a} - {b} = {result}')
        return result
    def mult(self, a, b):
        result = a * b
        self.logger.info(f'{a} * {b} = {result}')
        return result
    def div(self, a ,b):
        if b != 0:
            result = a / b
            result = int(result)
            self.logger.info(f'{a} / {b} = {result}')
            return result
        else:
            raise ValueError('Не можна ділити на нуль!')

c = Calculator()
c.add(2, 3)
c.sub(10, 9)
c.mult(5, 6)
c.div(8, 2)

#2

logging.basicConfig(level=logging.INFO,
                    filename= 'ex2.log',
                    filemode= 'w',
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('debug')
logging.info('info')
logging.warning('warming')
logging.error('error')
logging.critical('critical')
a = input('Введіть текст: ')

class log_:
    def __init__(self):
        self.logger = logging.getLogger('Log_')
        self.logger.setLevel(logging.DEBUG)
    def text(self, a):
        if 'bad_words' in a:
            raise ValueError('У тексті присутні заборонені слова')
        try:
            self.logger.info(f'{a}')
            print('Текст був доданий до txt-файлу')
        except Exception as e:
            print(f"Error: {e}")
l = log_()
l.text(a)

#3

import random

logging.basicConfig(level=logging.INFO,
                    filename= 'ex3.log',
                    filemode= 'w',
                    format='%(asctime)s - %(levelname)s - %(message)s')
class loggg():
    def __init__(self):
        self.logger = logging.getLogger('LOG')
        self.logger.setLevel(logging.DEBUG)
    def add_to_log(self):
        for i in range(10):
            i = random.randint(1, 100)
            if i != int(i):
                raise TypeError(f'{i} не є цілим числом!')
            try:
                self.logger.info(i)
                print(f'Число "{i}" було додано до Log')
            except Exception as e:
                print(f'Error: {e}')

l = loggg()
l.add_to_log()


