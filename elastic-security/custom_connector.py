"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

import requests
import json
from typing import Literal, Optional, Union


class CustomConnector:
    def __init__(self, url: str, api_key: str, verify_ssl: bool):
        self.url: str = url
        self.api_key: str = api_key
        self.verify_ssl: bool = verify_ssl
        self._check_url(url)

    def _check_url(self, url: str):
        if not (self.url.startswith("https://") or self.url.startswith("http://")):
            raise Exception("config url must start with 'https://' or 'http://'")

        if self.url.endswith("/"):
            raise Exception("config url must not end with '/'")

    def _check_api_endpoint(self, api_endpoint: str):
        if not api_endpoint.startswith("/"):
            raise Exception("param api_endpoint must startswith '/'")

    def _delete_none_dict(self, _d: Union[dict, list, None]) -> Union[dict, list, None]:
        if _d == None:
            return None
        elif isinstance(_d, list):
            return _d
        elif isinstance(_d, str):
            return None
        return {k: v for k, v in _d.items() if v is not None}

    def _check_health(self):
        return self.health_check()

    def generic_api_call(
            self,
            method: Literal["GET", "PUT", "POST", "DELETE", "PATCH", "HEAD", "OPTIONS", "TRACE"],
            api_endpoint: str,
            headers: Optional[dict] = None,
            params: Optional[dict] = None,
            json_data: Optional[dict] = None,
    ) -> dict:
        self._check_api_endpoint(api_endpoint)
        url = self.url + api_endpoint

        headers = headers if headers else {}
        headers["Accept"] = f"application/json"
        headers["Content-Type"] = f"application/json"
        headers["Authorization"] = f"ApiKey {self.api_key}"

        params_new = self._delete_none_dict(params)
        json_data_new = self._delete_none_dict(json_data)

        resp = requests.request(method, url, headers=headers, params=params_new, json=json_data_new,
                                verify=self.verify_ssl)
        return resp.json()

    def health_check(self) -> dict:
        return self.get_the_cluster_health_status("_all")

    def get_the_cluster_health_status(self, index: str) -> dict:
        """Get the cluster health status
        - API Documentation: <https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-health>
        """
        endpoint = f"/_cluster/health/{index}"
        return self.generic_api_call("GET", endpoint)

    def get_eql_search_results(self, index: str, query: dict) -> dict:
        """Get EQL search results
        - API Documentation: <https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-eql-search>
        """
        endpoint = f"/{index}/_eql/search"
        # json_data = {"query": query}

        return self.generic_api_call("POST", endpoint, json_data=query)

    def run_an_esql_query(
            self,
            query: dict,
            format: Optional[Literal["CSV", "JSON", "TSV", "TXT", "YAML", "CBOR", "Smile", "Arrow"]] = None,
            delimiter: Optional[str] = None,
            drop_null_columns: Optional[bool] = None,
            allow_partial_results: Optional[bool] = None,
    ) -> dict:
        """Run an ES|QL query
        - API Documentation: <https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-esql-query>
        """
        endpoint = f"/_query"
        params = {
            "format": format.lower() if format else '',
            "delimiter": delimiter if delimiter else '',
            "drop_null_columns": "true" if drop_null_columns else "false",
            "allow_partial_results": "true" if allow_partial_results else "false",
        }

        # json_data = {"query": query}
        params = {k: v for k, v in params.items() if v is not None and v != ''}
        return self.generic_api_call("POST", endpoint, params=params, json_data=query)

    # ------------------- Below functions are going to be deprecated in the newer version of connector. ------------------------------------------------------------------------------------------------
    # Will be deprecated in version 1.0.1

    # TODO Deprecation Warning: "This operation is going to be deprecated after version 1.0.1\nUse generic_api_call"
    def generic_action(
            self,
            method: Literal["GET", "PUT", "POST", "DELETE", "PATCH", "HEAD", "OPTIONS", "TRACE"],
            apiendpoint: str,
            params: dict,
            data: dict,
    ):
        return self.generic_api_call(method, apiendpoint, params=params, json_data=data)

    # TODO Deprecation Warning: This operation is going to be deprecated after version 1.0.1\nUse get_the_cluster_health_status
    def get_status(self) -> dict:
        return self.generic_api_call("GET", "/")

    # TODO Deprecation Warning: This operation is going to be deprecated after version 1.0.1\nUse get_eql_search_results
    def eql_search_api(self, target: str, data: dict) -> dict:
        return self.generic_api_call("GET", f"/{target}/_eql/search", json_data=data)

    # TODO Deprecation Warning: This operation is going to be deprecated after version 1.0.1\nUse run_an_esql_query
    def esql_search_api(self, data: dict) -> dict:
        return self.generic_api_call("POST", f"/_query", json_data=data)
