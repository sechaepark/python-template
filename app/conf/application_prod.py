from typing import Dict

from core.app_meta import app_meta

prod_config: Dict = {
    'application': {
        'environment': app_meta.environment.production,
        'redis': {
            'main': {
                'host': '127.0.0.1',
                'port': '6379',
                'username': '',
                'password': '',
                'db': 0,
                'charset': 'utf-8',
                'decode_responses': True,
            },
        },
        'datasource': {
            'main_write': {
                'host': '',
                'port': '',
                'username': '',
                'password': '',
                'db': '',
                'charset': 'utf-8',
            },
            'main_read': {
                'host': '',
                'port': '',
                'username': '',
                'password': '',
                'db': '',
                'charset': 'utf-8',
            },
        },
    },
    'log': {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            },
            'detail': {
                'format': '%(asctime)s [%(levelname)s] %(pathname)s %(funcName)s() : %(lineno)d - %(message)s'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
                'formatter': 'simple',
                'stream': 'ext://sys.stdout'
            },
            'app_log_file_handler': {
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'level': 'INFO',
                'formatter': 'simple',
                'filename': f'{app_meta.log_dir}/app.log',
                'when': 'midnight',
                'interval': 1,
                'backupCount': 30,
                'encoding': 'utf8'
            },
            'err_log_file_handler': {
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'level': 'ERROR',
                'formatter': 'detail',
                'filename': f'{app_meta.log_dir}/error.log',
                'when': 'midnight',
                'interval': 1,
                'backupCount': 30,
                'encoding': 'utf8'
            }
        },
        'loggers': {
            'apscheduler': {
                'level': 'ERROR'
            },
            'urllib3': {
                'level': 'INFO'
            },
            'slack': {
                'level': 'INFO'
            },
            'app.root': {
                'level': 'INFO',
            },
            'app.job': {
                'level': 'INFO',
            },
            'app.function': {
                'level': 'INFO',
            }
        },
        'root': {
            'level': 'INFO',
            'handlers': [
                'console',
                'app_log_file_handler',
                'err_log_file_handler'
            ]
        },
    }
}
