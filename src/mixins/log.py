from logging import basicConfig, getLogger, INFO, DEBUG

basicConfig(
    level=INFO,
    filename = 'logfile.log',
    filemode='a',
    encoding='utf-8',
    format='%(levelname)s:-:%(asctime)s:-:%(module)s:-:%(funcName)s:-:%(message)s'
)

logger = getLogger()