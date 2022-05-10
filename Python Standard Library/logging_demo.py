import logging

# https://docs.python.org/3/library/logging.html

def main():
    # logging.basicConfig(filename='logging_demo.log', filemode='a', level=logging.INFO)  # filemode: a, w
    # logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    # logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
    # logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', datefmt='%Y/%m/%d %H:%M:%S')

    # logger configuration to log to file and print to stdout
    logging.basicConfig(
    	level=logging.DEBUG,
    	datefmt='%Y.%m.%d %H:%M:%S',
    	format="%(asctime)s %(module)s:%(lineno)d [%(levelname)s]  %(message)s",
    	handlers=[logging.FileHandler("logging_demo.log", mode='w'), logging.StreamHandler()]
    	)

    logging.info('Started')
    logging.info('Finished')

    logging.warning('Watch out!')  # will print a message to the console
    logging.warning('%s before you %s', 'Look', 'leap!')

    logging.debug('This message should go to the log file')

    logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

if __name__ == '__main__':
    main()
