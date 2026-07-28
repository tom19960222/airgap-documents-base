---
collection: ansible
version: "8"
title: "hetzner.hcloud.hcloud_primary_ip_info module – Gather infos about the Hetzner Cloud Primary IPs."
source_url: https://docs.ansible.com/projects/ansible/8/collections/hetzner/hcloud/hcloud_primary_ip_info_module.html
fetched_at: 2026-07-28T02:34:08+00:00
---
# hetzner.hcloud.hcloud_primary_ip_info module – Gather infos about the Hetzner Cloud Primary IPs.

> **Note:**
>
> This module is part of the [hetzner.hcloud collection](https://galaxy.ansible.com/ui/repo/published/hetzner/hcloud/) (version 1.16.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hetzner.hcloud`.
> You need further requirements to be able to use this module,
> see [Requirements](hcloud_primary_ip_info_module.md#ansible-collections-hetzner-hcloud-hcloud-primary-ip-info-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_primary_ip_info`.

- [Synopsis](hcloud_primary_ip_info_module.md#synopsis)
- [Requirements](hcloud_primary_ip_info_module.md#requirements)
- [Parameters](hcloud_primary_ip_info_module.md#parameters)
- [See Also](hcloud_primary_ip_info_module.md#see-also)
- [Examples](hcloud_primary_ip_info_module.md#examples)
- [Return Values](hcloud_primary_ip_info_module.md#return-values)

## [Synopsis](hcloud_primary_ip_info_module.md#id1)

- Gather facts about your Hetzner Cloud Primary IPs.

## [Requirements](hcloud_primary_ip_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python-dateutil >= 2.7.5
- requests >=2.20

## [Parameters](hcloud_primary_ip_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  **Default:** `"https://api.hetzner.cloud/v1"` |
| **id**  integer | The ID of the Primary IP you want to get. |
| **label_selector**  string | The label selector for the Primary IP you want to get. |
| **name**  string | The name for the Primary IP you want to get. |

## [See Also](hcloud_primary_ip_info_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_primary_ip_info_module.md#id5)

```yaml+jinja
- name: Gather hcloud Primary IP infos
  hcloud_primary_ip_info:
  register: output

- name: Gather hcloud Primary IP infos by id
  hcloud_primary_ip_info:
    id: 673954
  register: output

- name: Gather hcloud Primary IP infos by name
  hcloud_primary_ip_info:
    name: srv1-v4
  register: output

- name: Gather hcloud Primary IP infos by label
  hcloud_primary_ip_info:
    label_selector: srv03-ips
  register: output

- name: Print the gathered infos
  debug:
    var: output
```

## [Return Values](hcloud_primary_ip_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_primary_ip_info**  complex | The Primary IP infos as list  **Returned:** always |
| **assignee_id**  integer | Numeric identifier of the ressource where the Primary IP is assigned to.  **Returned:** always  **Sample:** `19584637` |
| **assignee_type**  string | Name of the type where the Primary IP is assigned to.  **Returned:** always  **Sample:** `"server"` |
| **delete_protection**  boolean | True if the Primary IP is protected for deletion  **Returned:** always |
| **dns_ptr**  string | Shows the DNS PTR Record for Primary IP.  **Returned:** always  **Sample:** `"srv01.example.com"` |
| **home_location**  string | Location with datacenter where the Primary IP was created in  **Returned:** always  **Sample:** `"fsn1-dc1"` |
| **id**  integer | Numeric identifier of the Primary IP  **Returned:** always  **Sample:** `1937415` |
| **ip**  string | IP address of the Primary IP  **Returned:** always  **Sample:** `"131.232.99.1"` |
| **labels**  dictionary | User-defined labels (key-value pairs)  **Returned:** always |
| **name**  string | Name of the Primary IP  **Returned:** always  **Sample:** `"my-primary-ip"` |
| **type**  string | Type of the Primary IP  **Returned:** always  **Sample:** `"ipv4"` |

### Authors

- Lukas Kaemmerling (@LKaemmerling)
- Kevin Castner (@kcastner)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
- [Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
