import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')  #щоб визвати лог, як пріоритетний
logging.debug('debug')
logging.info('info')
logging.warning('warming')
logging.error('error')
logging.critical('critical')

