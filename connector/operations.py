"""
This file will be auto-generated on each "new operation action", so avoid editing in this file.
"""
import json

from .elasticsecurity import ElasticSecurity


def parse_configs(config):
    info_keys = [
        "server_url",
        "protocol",
        "username",
        "password",
        "port",
        "verify_ssl"
    ]
    return {_key: config[_key] for _key in info_keys}


def generic_action(config, params):
    es = ElasticSecurity(**parse_configs(config))
    resp = es.make_api_request(
        params.get('method'),
        params.get('apiendpoint'),
        params.get('params'),
        json.dumps(params.get('data'))
    )
    return resp.json()


def get_status(config, params):
    es = ElasticSecurity(**parse_configs(config))
    resp = es.get_status()
    return resp.json()


def eql_search_api(config, params):
    es = ElasticSecurity(**parse_configs(config))
    resp = es.eql_search_api(
        params.get("target"), 
        json.dumps(params.get("data"))
    )
    return resp.json()


def esql_search_api(config, params):
    es = ElasticSecurity(**parse_configs(config))
    resp = es.esql_search_api(
        json.dumps(params.get("data"))
    )
    return resp.json()





operations = {
    "generic_action": generic_action,
    "get_status": get_status,
    "eql_search_api": eql_search_api,
    "esql_search_api": esql_search_api,
    # "os_query_get_saved_query": os_query_get_saved_query,
    # "os_query_create_live_query": os_query_create_live_query,
    # "os_query_get_live_query_results": os_query_get_live_query_results,
}
