---
collection: ansible
version: "8"
title: "vultr.cloud.instance_info module – Get information about the Vultr instances"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vultr/cloud/instance_info_module.html
fetched_at: 2026-07-28T02:58:54+00:00
---
# vultr.cloud.instance_info module – Get information about the Vultr instances

> **Note:**
>
> This module is part of the [vultr.cloud collection](https://galaxy.ansible.com/ui/repo/published/vultr/cloud/) (version 1.11.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vultr.cloud`.
>
> To use it in a playbook, specify: `vultr.cloud.instance_info`.

New in vultr.cloud 1.5.0

- [Synopsis](instance_info_module.md#synopsis)
- [Parameters](instance_info_module.md#parameters)
- [Notes](instance_info_module.md#notes)
- [Examples](instance_info_module.md#examples)
- [Return Values](instance_info_module.md#return-values)

## [Synopsis](instance_info_module.md#id1)

- Get infos about available instances.

## [Parameters](instance_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  Fallback environment variable `VULTR_API_ENDPOINT`.  **Default:** `"https://api.vultr.com/v2"` |
| **api_key**  string / required | API key of the Vultr API.  Fallback environment variable `VULTR_API_KEY`. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  Fallback environment variable `VULTR_API_RETRIES`.  **Default:** `5` |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  Fallback environment variable `VULTR_API_RETRY_MAX_DELAY`.  **Default:** `12` |
| **api_timeout**  integer | HTTP timeout to Vultr API.  Fallback environment variable `VULTR_API_TIMEOUT`.  **Default:** `180` |
| **label**  aliases: name  string | Name of the instance. |
| **region**  string | Filter instances by region. |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](instance_info_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](instance_info_module.md#id4)

```yaml+jinja
- name: Get Vultr instance infos of region ams
  vultr.cloud.instance_info:
    region: ams

- name: Get Vultr instance infos of a single host
  vultr.cloud.instance_info:
    label: myhost

- name: Get all Vultr instance infos
  vultr.cloud.instance_info:
  register: results

- name: Print the gathered infos
  ansible.builtin.debug:
    var: results.vultr_instance_info
```

## [Return Values](instance_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  dictionary | Response from Vultr API with a few additions/modification.  **Returned:** success |
| **api_endpoint**  string | Endpoint used for the API requests.  **Returned:** success  **Sample:** `"https://api.vultr.com/v2"` |
| **api_retries**  integer | Amount of max retries for the API requests.  **Returned:** success  **Sample:** `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  **Returned:** success  **Sample:** `12` |
| **api_timeout**  integer | Timeout used for the API requests.  **Returned:** success  **Sample:** `60` |
| **vultr_instance_info**  list / elements=string | Response from Vultr API as list.  **Returned:** available |
| **allowed_bandwidth**  integer | Allowed bandwidth of the instance.  **Returned:** success  **Sample:** `1000` |
| **app_id**  integer | App ID of the instance.  **Returned:** success  **Sample:** `37` |
| **date_created**  string | Date when the instance was created.  **Returned:** success  **Sample:** `"2020-10-10T01:56:20+00:00"` |
| **disk**  integer | Disk size of the instance.  **Returned:** success  **Sample:** `25` |
| **features**  list / elements=string | Features of the instance.  **Returned:** success  **Sample:** `["ddos_protection", "ipv6", "auto_backups"]` |
| **firewall_group_id**  string | Firewall group ID of the instance.  **Returned:** success  **Sample:** `""` |
| **gateway_v4**  string | Gateway IPv4.  **Returned:** success  **Sample:** `"95.179.188.1"` |
| **hostname**  string | Hostname of the instance.  **Returned:** success  **Sample:** `"vultr.guest"` |
| **id**  string | ID of the instance.  **Returned:** success  **Sample:** `"cb676a46-66fd-4dfb-b839-443f2e6c0b60"` |
| **image_id**  string | Image ID of the instance.  **Returned:** success  **Sample:** `""` |
| **internal_ip**  string | Internal IP of the instance.  **Returned:** success  **Sample:** `""` |
| **kvm**  string | KVM of the instance.  **Returned:** success  **Sample:** `"https://my.vultr.com/subs/vps/novnc/api.php?data=..."` |
| **label**  string | Label of the instance.  **Returned:** success  **Sample:** `"my instance"` |
| **main_ip**  string | IPv4 of the instance.  **Returned:** success  **Sample:** `"95.179.189.95"` |
| **netmask_v4**  string | Netmask IPv4 of the instance.  **Returned:** success  **Sample:** `"255.255.254.0"` |
| **os**  string | OS of the instance.  **Returned:** success  **Sample:** `"Application"` |
| **os_id**  integer | OS ID of the instance.  **Returned:** success  **Sample:** `186` |
| **plan**  string | Plan of the instance.  **Returned:** success  **Sample:** `"vc2-1c-1gb"` |
| **power_status**  string | Power status of the instance.  **Returned:** success  **Sample:** `"running"` |
| **ram**  integer | RAM in MB of the instance.  **Returned:** success  **Sample:** `1024` |
| **region**  string | Region the instance was deployed into.  **Returned:** success  **Sample:** `"ews"` |
| **server_status**  string | Server status of the instance.  **Returned:** success  **Sample:** `"installingbooting"` |
| **status**  string | Status about the deployment of the instance.  **Returned:** success  **Sample:** `"active"` |
| **tags**  list / elements=string | Tags of the instance.  **Returned:** success  **Sample:** `["my-tag"]` |
| **user_data**  string | Base64 encoded user data (cloud init) of the instance.  **Returned:** success  **Sample:** `"I2Nsb3VkLWNvbmZpZwpwYWNrYWdlczoKICAtIGh0b3AK"` |
| **v6_main_ip**  string | IPv6 of the instance.  **Returned:** success  **Sample:** `""` |
| **v6_network**  string | IPv6 network of the instance.  **Returned:** success  **Sample:** `""` |
| **v6_network_size**  integer | IPv6 network size of the instance.  **Returned:** success  **Sample:** `0` |
| **vcpu_count**  integer | vCPUs of the instance.  **Returned:** success  **Sample:** `1` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/vultr/ansible-collection-vultr/issues)
- [Repository (Sources)](https://github.com/vultr/ansible-collection-vultr)
