---
collection: ansible
version: "6"
title: "cisco.dnac.discovery_job_info module – Information module for Discovery Job"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/discovery_job_info_module.html
fetched_at: 2026-07-27T16:51:44+00:00
---
# cisco.dnac.discovery_job_info module – Information module for Discovery Job

> **Note:**
>
> This module is part of the [cisco.dnac collection](https://galaxy.ansible.com/cisco/dnac) (version 6.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.dnac`.
> You need further requirements to be able to use this module,
> see [Requirements](discovery_job_info_module.md#ansible-collections-cisco-dnac-discovery-job-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.discovery_job_info`.

New in cisco.dnac 3.1.0

- [Synopsis](discovery_job_info_module.md#synopsis)
- [Requirements](discovery_job_info_module.md#requirements)
- [Parameters](discovery_job_info_module.md#parameters)
- [Notes](discovery_job_info_module.md#notes)
- [See Also](discovery_job_info_module.md#see-also)
- [Examples](discovery_job_info_module.md#examples)
- [Return Values](discovery_job_info_module.md#return-values)

## [Synopsis](discovery_job_info_module.md#id1)

- Get all Discovery Job.
- Get Discovery Job by id.
- Returns the list of discovery jobs for the given Discovery ID. The results can be optionally filtered based on IP. Discovery ID can be obtained using the “Get Discoveries by range” API.
- Returns the list of discovery jobs for the given IP.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](discovery_job_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](discovery_job_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **headers**  dictionary | Additional headers. |
| **id**  string | Id path parameter. Discovery ID. |
| **ipAddress**  string | IpAddress query parameter. |
| **limit**  integer | Limit query parameter. |
| **name**  string | Name query parameter. |
| **offset**  integer | Offset query parameter. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](discovery_job_info_module.md#id4)

> **Note:**
>
> - SDK Method used are discovery.Discovery.get_discovery_jobs_by_ip, discovery.Discovery.get_list_of_discoveries_by_discovery_id,
> - Paths used are get /dna/intent/api/v1/discovery/job, get /dna/intent/api/v1/discovery/{id}/job,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](discovery_job_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Discovery GetDiscoveryJobsByIP](https://developer.cisco.com/docs/dna-center/#!get-discovery-jobs-by-ip)
> :   Complete reference of the GetDiscoveryJobsByIP API.
>
> [Cisco DNA Center documentation for Discovery GetListOfDiscoveriesByDiscoveryId](https://developer.cisco.com/docs/dna-center/#!get-list-of-discoveries-by-discovery-id)
> :   Complete reference of the GetListOfDiscoveriesByDiscoveryId API.

## [Examples](discovery_job_info_module.md#id6)

```yaml+jinja
- name: Get all Discovery Job
  cisco.dnac.discovery_job_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    offset: 0
    limit: 0
    ipAddress: string
    name: string
  register: result

- name: Get Discovery Job by id
  cisco.dnac.discovery_job_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    offset: 0
    limit: 0
    ipAddress: string
    id: string
  register: result
```

## [Return Values](discovery_job_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": [{"attributeInfo": {}, "cliStatus": "string", "discoveryStatus": "string", "endTime": "string", "httpStatus": "string", "id": "string", "inventoryCollectionStatus": "string", "inventoryReachabilityStatus": "string", "ipAddress": "string", "jobStatus": "string", "name": "string", "netconfStatus": "string", "pingStatus": "string", "snmpStatus": "string", "startTime": "string", "taskId": "string"}], "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
