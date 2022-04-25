import datetime
import hashlib
import time
import uuid
from collections.abc import MutableMapping
from logging import getLogger

logger = getLogger('app.function')


def com_batch_job(original_fn: object) -> object:
    def wrapper_fn(**kwargs):
        logger.debug('-' * 79)
        logger.debug('{}.{} started : {}'.format(original_fn.__module__, original_fn.__name__, kwargs))
        logger.debug('-' * 79)
        return original_fn(**kwargs)

    return wrapper_fn


def com_merge_dict(d, v):
    """
    Merge two dictionaries.

    Merge dict-like `v` into dict-like `d`. In case keys between them are the same, merge
    their sub-dictionaries where possible. Otherwise, values in `v` overwrite `d`.
    """
    for key in v:
        if key in d and isinstance(d[key], MutableMapping) and isinstance(v[key], MutableMapping):
            d[key] = com_merge_dict(d[key], v[key])
        else:
            d[key] = v[key]
    return d


def com_sort(objects: list, sort_field: str, is_descending: bool = False):
    result: list = objects

    if objects and sort_field:
        result = sorted(objects, key=lambda obj: obj[sort_field], reverse=is_descending)

    return result


def com_get_uuid():
    return str(uuid.uuid4())


def com_get_ts(digit: int = 13):
    ts: str = str(time.time())
    return int(ts.replace('.', '')[:digit])


def com_get_today(date_format: str = '%Y%m%d'):
    return datetime.datetime.now().strftime(date_format)


def com_get_yesterday(date_format: str = '%Y%m%d'):
    return (datetime.datetime.now() - datetime.timedelta(days=1)).strftime(date_format)


def com_get_one_month_ago(date_format: str = '%Y%m%d'):
    today = datetime.date.today()
    first = today.replace(day=1)
    last_month_today = (first - datetime.timedelta(days=1)).replace(day=today.day)
    return last_month_today.strftime(date_format)


def com_get_days_ago(days: int, date_format: str = '%Y%m%d'):
    return (datetime.datetime.now() - datetime.timedelta(days=days)).strftime(date_format)


def com_logging_obj(obj: object, text: str = ''):
    logger.debug('+' * 80)
    logger.debug('{0}: {1}'.format(text, obj.__class__.__name__))
    logger.debug(obj)
    logger.debug('+' * 80)


def com_local_to_utc(dt: datetime) -> datetime:
    return dt - datetime.timedelta(hours=9)


def com_utc_to_local(dt: datetime) -> datetime:
    return dt + datetime.timedelta(hours=9)


def com_get_hash_value(text, digest_size=64, return_type='hexdigest'):
    blake = hashlib.blake2b(text.encode('utf-8'), digest_size=digest_size)

    if return_type == 'hexdigest':
        return blake.hexdigest()
    elif return_type == 'number':
        return int(blake.hexdigest(), base=16)
    else:
        return blake.digest()


if __name__ == '__main__':
    now = datetime.datetime.now()
    utc_dt = com_local_to_utc(now)
    local_dt = com_utc_to_local(now)
    print(com_get_today('%Y-%m-%d %H:%M:%S'))
    print('-' * 80)
    print(f'''
    now : {now},
    local_to_utc : {utc_dt} / {utc_dt.timestamp()},
    utc_to_local : {local_dt} / {local_dt.timestamp()}''')

    s = 'hello psc'
    print(com_get_hash_value(text=s, digest_size=32, return_type='hexdigest'))
    print(com_get_hash_value(text=s, digest_size=32, return_type='number'))
