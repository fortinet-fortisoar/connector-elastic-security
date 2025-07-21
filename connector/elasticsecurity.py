# %%
import json
import requests
from typing import Literal


class ElasticSecurity:
    def __init__(
        self,
        server_url: str,
        protocol: str,
        api_key: str = None,
        username: str = None,
        password: str = None,
        port: int = 9200,
        verify_ssl: bool = True,
    ):
        self.server_url = server_url
        self.protocol = protocol
        self.api_key = (api_key,)
        self.username = username
        self.password = password
        self.port = str(port)
        self.verify_ssl = False

        self.url = self.protocol + "://" + self.server_url + ":" + str(self.port)

    def get_status(self) -> requests.Response:
        return self.make_api_request("GET", "/")

    def eql_search_api(self, target: str, data: str) -> requests.Response:
        return self.make_api_request("GET", f"/{target}/_eql/search", data=data)

    def esql_search_api(self, data: str) -> requests.Response:
        return self.make_api_request("POST", f"/_query", data=data)

    def get_osquery_saved_queries(self) -> requests.Response:
        return self.make_api_request("GET", f"/api/osquery/saved_queries")

    def create_osquery_live_queries(self, data: str) -> requests.Response:
        return self.make_api_request("POST", f"/api/osquery/live_queries")

    def make_api_request(
        self,
        method: Literal["GET", "POST"],
        api_endpoint: str,
        params: str = None,
        data: str = None,
    ):
        if not api_endpoint.startswith("/"):
            api_endpoint = "/" + api_endpoint

        resp = None

        headers = {"Accept": "application/json", "Content-type": "application/json"}
        if isinstance(self.api_key, str):
            headers["Authorization"] = f"ApiKey {self.api_key}"
            if method == "GET":
                resp = requests.get(self.url + api_endpoint, headers=headers, data=data, params=params, verify=self.verify_ssl)
            elif method == "POST":
                resp = requests.post(self.url + api_endpoint, headers=headers, data=data, params=params, verify=self.verify_ssl)

        elif isinstance(self.username, str) and isinstance(self.password, str):
            if method == "GET":
                resp = requests.get(
                    self.url + api_endpoint,
                    auth=(self.username, self.password),
                    headers=headers,
                    data=data,
                    params=params,
                    verify=self.verify_ssl,
                )
            elif method == "POST":
                resp = requests.post(
                    self.url + api_endpoint,
                    auth=(self.username, self.password),
                    headers=headers,
                    data=data,
                    params=params,
                    verify=self.verify_ssl,
                )

        return resp