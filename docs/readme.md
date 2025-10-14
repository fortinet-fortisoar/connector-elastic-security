## About the connector

Elastic Security provides threat prevention, detection, and response capabilities built on the Elastic Stack. It unifies
SIEM, endpoint security, and cloud security in a single solution.
<p>This document provides information about the Elastic Security Connector, which facilitates automated interactions, with a Elastic Security server using FortiSOAR&trade; playbooks. Add the Elastic Security Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Elastic Security.</p>

### Version information

Connector Version: 1.0.0

Authored By: Fortinet CSE

Contributor: Daehyeob Kim

Certified: No

## Installing the connector

<p>From FortiSOAR&trade; 6.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-elastic-security`

## Prerequisites to configuring the connector

- You must have the URL of Elastic Security server to which you will connect and perform automated operations and
  credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Elastic Security server.

## Minimum Permissions Required

- N/A

## Configuring the connector

For the procedure to configure a connector,
click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)

### Configuration parameters

<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Elastic Security</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>Specify the server URL of the Elastic server to connect and perform automated operations.<br>
<tr><td>API Key<br></td><td>Specify the API Key to connect to the endpoint and perform automated operations<br>
<tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get Cluster Health Status<br></td><td>Retrieve the cluster health status based on the index parameter that you have specified.<br></td><td>get_the_cluster_health_status <br/>Investigation<br></td></tr>
<tr><td>Get EQL Search Results<br></td><td>Retrieve a search results for an Event Query Language (EQL) query based on the index and query parameters you have specified.<br></td><td>get_eql_search_results <br/>Investigation<br></td></tr>
<tr><td>Run an ES|QL Query<br></td><td>Retrieve a search results for an ES|QL (Elasticsearch query language) query from Elastic based on the query and other input parameters you have specified.<br></td><td>run_an_esql_query <br/>Investigation<br></td></tr>
<tr><td>Execute an API Request<br></td><td>Sends an API request to an API endpoint based on specified HTTP method, endpoint, and other input parameters that you have specified, enabling flexible API interactions tailored to user needs.<br></td><td>generic_api_call <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Get Cluster Health Status
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Index<br></td><td>Specify the index to retrieve all data streams and indices in a cluster. Possible values are _all or *<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "timed_out": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "cluster_name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "active_shards": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "number_of_nodes": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "relocating_shards": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "unassigned_shards": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "initializing_shards": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "number_of_data_nodes": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "active_primary_shards": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "number_of_pending_tasks": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "delayed_unassigned_shards": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "number_of_in_flight_fetch": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "unassigned_primary_shards": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "active_shards_percent_as_number": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "task_max_waiting_in_queue_millis": ""
</code><code><br>}</code>
### operation: Get EQL Search Results
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Index<br></td><td>Specify the index to search results for an Event Query Language (EQL) query from Elastic. Possible values are _all or *<br>
</td></tr><tr><td>Query<br></td><td>Specify the EQL query to search results from Elastic.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "hits": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "total": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "value": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "relation": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "events": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "_id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "_index": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "_source": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "user.name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "@timestamp": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "process.pid": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "event.action": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "process.name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "event.category": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "process.parent.name": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ]
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "took": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "timed_out": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "is_partial": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "is_running": ""
</code><code><br>}</code>
### operation: Run an ES|QL Query
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Query<br></td><td>Specify the ES|QL query to search results from Elastic.<br>
</td></tr><tr><td>Format<br></td><td>Select the format by which to search results. You can choose from the following options: CSV, JSON, TSV, TXT, YAML, CBOR, Smile, or Arrow.<br>
</td></tr><tr><td>Delimiter<br></td><td>Specify the delimiter to use between values within a CSV row. Note: Only valid for the CSV format.<br>
</td></tr><tr><td>Remove Empty Columns<br></td><td>If enabled, columns that contain only null values are excluded from the results. By default, this is false. When true, the response also includes an all_columns section listing every column name.<br>
</td></tr><tr><td>Allow Partial Results<br></td><td>If true, partial results will be returned if there are shard failures, but the query can continue to execute on other clusters and shards. If false, the query will fail if there are any failures. By default, this is false.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "took": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "values": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "columns": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "type": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "is_partial": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "values_loaded": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "documents_found": ""
</code><code><br>}</code>
### operation: Execute an API Request
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>HTTP Method<br></td><td>Select an HTTP action for the request. You can select from the following options: 

GET

PUT

POST

DELETE

PATCH

HEAD

OPTIONS

TRACE<br>
</td></tr><tr><td>Endpoint<br></td><td>Specify the target API URL path for the request. For example, if the website is https://example.com and URL path is https://example.com/images/pic.jpg, the endpoint would be /images/pic.jpg.<br>
</td></tr><tr><td>Query Parameters<br></td><td>(Optional) Specify any optional parameters to add to the URL and refine the request.<br>
</td></tr><tr><td>Request Payload<br></td><td>(Optional) Specify data, as JSON, to be sent as the request payload (typically for POST or PUT requests).<br>
</td></tr></tbody></table>

#### Output

The output contains a non-dictionary value.

## Included playbooks

The `Sample - Elastic Security - 1.0.0` playbook collection comes bundled with the Elastic Security connector. These
playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the *
*Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the Elastic Security connector.

- Execute an API Request
- Get Cluster Health Status
- Get EQL Search Results
- Run an ES|QL Query

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those
playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector
upgrade and delete.
