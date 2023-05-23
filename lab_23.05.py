#1
import logging
#
# class Calculator:
#     def __init__(self):
#         self.logger = logging.getLogger('Calculator')
#         self.logger.setLevel(logging.DEBUG)
#         self.logger.addHandler(logging.StreamHandler())
#     def add(self, a, b):
#         result =  a + b
#         self.logger.info(f'{a} + {b} = {result}')
#         return result
#     def sub(self, a ,b):
#         result = a - b
#         self.logger.info(f'{a} - {b} = {result}')
#         return result
#     def mult(self, a, b):
#         result = a * b
#         self.logger.info(f'{a} * {b} = {result}')
#         return result
#     def div(self, a ,b):
#         if b != 0:
#             result = a / b
#             result = int(result)
#             self.logger.info(f'{a} / {b} = {result}')
#             return result
#         else:
#             raise ValueError('Не можна ділити на нуль!')
#
# c = Calculator()
# c.add(2, 3)
# c.sub(10, 9)
# c.mult(5, 6)
# c.div(8, 2)

#2

logging.basicConfig(level=logging.INFO,
                    filename= 'ex2.log',
                    filemode= 'w',
                    format='%(asctime)s - %(levelname)s - %(message)s')
a = input('Введіть текст: ')
class log_:
    def __init__(self):
        self.logger = logging.getLogger('Log_')
        self.logger.setLevel(logging.DEBUG)
    def text(self, a):
        self.logger.info(f'{a}')
l = log_()
l.text(a)

#3
