from os import path


class Environment(object):
    local: str = 'local'
    development: str = 'development'
    production: str = 'production'


class SlackConfig(object):
    text_max_size: int = 3000
    block_max_size: int = 50
    accessory_text_max_size: int = 2000


class AppMeta(object):
    base_dir: str = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))
    log_dir: str = f'{base_dir}/logs'
    environment: Environment = Environment()
    slack_config: SlackConfig = SlackConfig()
