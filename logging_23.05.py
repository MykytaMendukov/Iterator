import logging

logging.basicConfig(level=logging.DEBUG,  #щоб визвати лог, який не є помилкою
                    filename= 'logs.log',
                    filemode= 'w',
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('debug')
logging.info('info')
logging.warning('warming')
logging.error('error')
logging.critical('critical')
try:
    print(10 / 0)
except Exception:
    logging.exception('We have a problem!')


#факторіал числа

def factorial(n):
    logging.info(f'Розпочато обчислення факторіалу числа {n}')
    result = 1
    for i in range(1, n + 1):
        result *= i
    logging.info(f'Обчислення факторіалу числа {n} завершено. Результат виконання: {result}')
    return result
logging.basicConfig(level=logging.INFO)
factorial(5)