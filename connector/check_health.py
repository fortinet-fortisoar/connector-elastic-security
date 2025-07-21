from .elasticsecurity import ElasticSecurity
from .operations import parse_configs

def _check_health(config: dict) -> bool:
    try:
        es = ElasticSecurity(**parse_configs(config))
        resp = es.get_status()
        if resp.status_code == 200:
            return True
    except Exception as e:
        raise Exception(e)