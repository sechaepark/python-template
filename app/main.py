import logging.config
import os
from time import sleep

from core.app_conf import app_conf
from core.app_meta import app_meta

logger = logging.getLogger('app.root')


def set_log():
    if not os.path.exists(app_meta.log_dir):
        os.mkdir(app_meta.log_dir)

    logging.config.dictConfig(config=app_conf.log)


def print_info():
    logger.info('*' * 80)
    logger.info('*' * 80)
    logger.info(f'Application Name : {app_conf.application.name}')
    logger.info(f'Application Version : {app_conf.application.version}')
    logger.info(f'Application Environment Variable : {app_conf.application.os_env_var}')
    logger.info(f'Application Environment : {app_conf.application.environment}')
    logger.info('-' * 80)
    logger.info('*' * 80)
    logger.info('*' * 80)
    logger.info('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    for i in range(100):
        logger.debug(i)
        logger.info(i)
        sleep(1)


if __name__ == '__main__':
    set_log()
    print_info()
