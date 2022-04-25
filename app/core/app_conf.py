import logging
import os
import jsons

from core.app_conf_dto import AppConfig
from core.app_meta import app_meta
from core.com_function import com_merge_dict
from conf.application import default_config
from conf.application_dev import dev_config
from conf.application_local import local_config
from conf.application_prod import prod_config

logger = logging.getLogger('app.root')

config_dict: dict = default_config

env_var: str = config_dict.get('application', {}).get('os_env_var', '')

if not env_var:
    print('-' * 80)
    print('not found OS Environment Variable (os_env_var) in config files')
    print('-' * 80)
    exit(1)

environment: str = os.environ.get(env_var) or app_meta.environment.local

merge_config: dict

if environment == app_meta.environment.production:
    merge_config = prod_config
elif environment == app_meta.environment.development:
    merge_config = dev_config
else:
    merge_config = local_config

com_merge_dict(config_dict, merge_config)

app_conf: AppConfig = jsons.load(config_dict, AppConfig)
