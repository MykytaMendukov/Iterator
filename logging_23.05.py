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

