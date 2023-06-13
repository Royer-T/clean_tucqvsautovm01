import logging

#  set the logging behaviour
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s '
                                               '- %(name)s:%(message)s')
logger = logging.getLogger(__name__)