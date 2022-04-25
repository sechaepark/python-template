from dataclasses import dataclass
from typing import List

from core.app_meta import app_meta


@dataclass
class SchedulerConfig(object):
    job_stores: dict
    executors: dict
    job_defaults: dict


@dataclass
class ComServerDto(object):
    host: str
    port: str
    username: str
    password: str


@dataclass
class RedisServerDto(ComServerDto):
    decode_responses: bool
    db: int
    charset: str


@dataclass
class RedisServer(object):
    main: RedisServerDto


@dataclass
class DataSourceDto(ComServerDto):
    db: str
    charset: str


@dataclass
class DataSource(object):
    main_write: DataSourceDto
    main_read: DataSourceDto


@dataclass
class Proxies(object):
    http: str
    https: str


@dataclass
class SlackChannel:
    monitoring: List[str]


@dataclass
class SlackConfig(object):
    proxies: Proxies
    bot_user_oauth_access_token: str
    channels: SlackChannel


@dataclass
class ApplicationConfig(object):
    name: str
    version: str
    os_env_var: str
    environment: str
    slack: SlackConfig
    redis: RedisServer
    datasource: DataSource


@dataclass
class AppConfig(object):
    application: ApplicationConfig
    log: dict

    def is_local(self):
        return self.application.environment == app_meta.environment.local

    def is_dev(self):
        return self.application.environment == app_meta.environment.development

    def is_prod(self):
        return self.application.environment == app_meta.environment.production
