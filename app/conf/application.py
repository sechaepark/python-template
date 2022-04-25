from typing import Dict

default_config: Dict = {
    'application': {
        'name': 'xxx-application',
        'version': '1.0',
        'os_env_var': 'PYTHON_TEMPLATE_ENV',
        'slack': {
            'proxies': {
                'http': '',
                'https': '',
            },
            'bot_user_oauth_access_token': '',
            'channels': {
                'monitoring': [''],
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
    }
}
