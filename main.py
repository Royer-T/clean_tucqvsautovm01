import logging

# constants
import constants


#  create and configure logger
log_file = constants.LOG_FILE
log_path = f'{constants.LOGDIRECTORY}/{log_file}'

logging.basicConfig(filename=log_path,
                    level=logging.DEBUG,
                    filemode='a',
                    force=True,
                    format='%(asctime)s - %(levelname)s - '
                           '%(name)s:%(message)s')