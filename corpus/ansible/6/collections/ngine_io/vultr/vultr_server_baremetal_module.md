---
collection: ansible
version: "6"
title: "ngine_io.vultr.vultr_server_baremetal module – Manages baremetal servers on Vultr."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/vultr/vultr_server_baremetal_module.html
fetched_at: 2026-07-28T00:16:12+00:00
---
# ngine_io.vultr.vultr_server_baremetal module – Manages baremetal servers on Vultr.

> **Note:**
>
> This module is part of the [ngine_io.vultr collection](https://galaxy.ansible.com/ngine_io/vultr) (version 1.1.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.vultr`.
> You need further requirements to be able to use this module,
> see [Requirements](vultr_server_baremetal_module.md#ansible-collections-ngine-io-vultr-vultr-server-baremetal-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.vultr.vultr_server_baremetal`.

New in ngine_io.vultr 0.3.0

- [Synopsis](vultr_server_baremetal_module.md#synopsis)
- [Requirements](vultr_server_baremetal_module.md#requirements)
- [Parameters](vultr_server_baremetal_module.md#parameters)
- [Notes](vultr_server_baremetal_module.md#notes)
- [Examples](vultr_server_baremetal_module.md#examples)
- [Return Values](vultr_server_baremetal_module.md#return-values)

## [Synopsis](vultr_server_baremetal_module.md#id1)

- Deploy and destroy servers.

## [Requirements](vultr_server_baremetal_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](vultr_server_baremetal_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_account**  string | Name of the ini section in the `vultr.ini` file.  The ENV variable `VULTR_API_ACCOUNT` is used as default, when defined.  Default: `"default"` |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  The ENV variable `VULTR_API_ENDPOINT` is used as default, when defined.  Fallback value is <https://api.vultr.com> if not specified. |
| **api_key**  string | API key of the Vultr API.  The ENV variable `VULTR_API_KEY` is used as default, when defined. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  The ENV variable `VULTR_API_RETRIES` is used as default, when defined.  Fallback value is 5 retries if not specified. |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  The ENV variable `VULTR_API_RETRY_MAX_DELAY` is used as default, when defined.  Fallback value is 12 seconds. |
| **api_timeout**  integer | HTTP timeout to Vultr API.  The ENV variable `VULTR_API_TIMEOUT` is used as default, when defined.  Fallback value is 60 seconds if not specified. |
| **hostname**  string | The hostname to assign to this server. |
| **ipv6_enabled**  boolean | Whether to enable IPv6 or not.  Choices:   - `false` - `true` |
| **name**  aliases: label  string / required | Name of the server. |
| **notify_activate**  boolean | Whether to send an activation email when the server is ready or not.  Only considered on creation.  Choices:   - `false` ← (default) - `true` |
| **os**  string | The operating system name or ID.  Required if the server does not yet exist and is not restoring from a snapshot. |
| **plan**  string | Plan name or ID to use for the server.  Required if the server does not yet exist. |
| **region**  string | Region name or ID the server is deployed into.  Required if the server does not yet exist. |
| **reserved_ip_v4**  string | IP address of the floating IP to use as the main IP of this server.  Only considered on creation. |
| **ssh_keys**  aliases: ssh_key  list / elements=string | List of SSH key names or IDs passed to the server on creation. |
| **startup_script**  string | Name or ID of the startup script to execute on boot.  Only considered while creating the server. |
| **state**  string | State of the server.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tag**  string | Tag for the server. |
| **user_data**  string | User data to be passed to the server. |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  Choices:   - `false` - `true` ← (default) |

## [Notes](vultr_server_baremetal_module.md#id4)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](vultr_server_baremetal_module.md#id5)

```yaml+jinja
- name: create server
  ngine_io.vultr.vultr_server_baremetal:
    name: "{{ vultr_server_baremetal_name }}"
    os: Debian 9 x64 (stretch)
    plan: 32768 MB RAM,2x 240 GB SSD,5.00 TB BW
    region: Amsterdam

- name: ensure a server is absent
  ngine_io.vultr.vultr_server_baremetal:
    name: "{{ vultr_server_baremetal_name }}"
    state: absent
```

## [Return Values](vultr_server_baremetal_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  complex | Response from Vultr API with a few additions/modification  Returned: success |
| **api_account**  string | Account used in the ini file to select the key  Returned: success  Sample: `"default"` |
| **api_endpoint**  string | Endpoint used for the API requests  Returned: success  Sample: `"https://api.vultr.com"` |
| **api_retries**  integer | Amount of max retries for the API requests  Returned: success  Sample: `5` |
| **api_timeout**  integer | Timeout used for the API requests  Returned: success  Sample: `60` |
| **vultr_server_baremetal**  complex | Response from Vultr API with a few additions/modification  Returned: success |
| **allowed_bandwidth_gb**  integer | Allowed bandwidth to use in GB  Returned: success  Sample: `1000` |
| **cost_per_month**  float | Cost per month for the server  Returned: success  Sample: `120.0` |
| **current_bandwidth_gb**  integer | Current bandwidth used for the server  Returned: success  Sample: `0` |
| **date_created**  string | Date when the server was created  Returned: success  Sample: `"2017-04-12 18:45:41"` |
| **default_password**  string | Password to login as root into the server  Returned: success  Sample: `"ab81u!ryranq"` |
| **disk**  string | Information about the disk  Returned: success  Sample: `"SSD 250 GB"` |
| **id**  string | ID of the server  Returned: success  Sample: `"900000"` |
| **internal_ip**  string | Internal IP  Returned: success  Sample: `""` |
| **name**  string | Name (label) of the server  Returned: success  Sample: `"ansible-test-baremetal"` |
| **os**  string | Operating system used for the server  Returned: success  Sample: `"Debian 9 x64"` |
| **pending_charges**  float | Pending charges  Returned: success  Sample: `0.18` |
| **plan**  string | Plan used for the server  Returned: success  Sample: `"32768 MB RAM,2x 240 GB SSD,5.00 TB BW"` |
| **ram**  string | Information about the RAM size  Returned: success  Sample: `"32768 MB"` |
| **region**  string | Region the server was deployed into  Returned: success  Sample: `"Amsterdam"` |
| **status**  string | Status about the deployment of the server  Returned: success  Sample: `"active"` |
| **tag**  string | Server tag  Returned: success  Sample: `"my tag"` |
| **v4_gateway**  string | IPv4 gateway  Returned: success  Sample: `"203.0.113.1"` |
| **v4_main_ip**  string | Main IPv4  Returned: success  Sample: `"203.0.113.10"` |
| **v4_netmask**  string | Netmask IPv4  Returned: success  Sample: `"255.255.255.0"` |
| **v6_main_ip**  string | Main IPv6  Returned: success  Sample: `"2001:DB8:9000::100"` |
| **v6_network**  string | Network IPv6  Returned: success  Sample: `"2001:DB8:9000::"` |
| **v6_network_size**  integer | Network size IPv6  Returned: success  Sample: `64` |
| **v6_networks**  list / elements=string | Networks IPv6  Returned: success  Sample: `[]` |

### Authors

- Nate River (@vitikc)
- Simon Baerlocher (@sbaerlocher)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-vultr/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-vultr)
