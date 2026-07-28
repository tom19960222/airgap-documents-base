---
collection: ansible
version: "8"
title: "hetzner.hcloud.hcloud_load_balancer_type_info module – Gather infos about the Hetzner Cloud Load Balancer types."
source_url: https://docs.ansible.com/projects/ansible/8/collections/hetzner/hcloud/hcloud_load_balancer_type_info_module.html
fetched_at: 2026-07-28T02:34:04+00:00
---
# hetzner.hcloud.hcloud_load_balancer_type_info module – Gather infos about the Hetzner Cloud Load Balancer types.

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
> see [Requirements](hcloud_load_balancer_type_info_module.md#ansible-collections-hetzner-hcloud-hcloud-load-balancer-type-info-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_load_balancer_type_info`.

New in hetzner.hcloud 0.1.0

- [Synopsis](hcloud_load_balancer_type_info_module.md#synopsis)
- [Requirements](hcloud_load_balancer_type_info_module.md#requirements)
- [Parameters](hcloud_load_balancer_type_info_module.md#parameters)
- [See Also](hcloud_load_balancer_type_info_module.md#see-also)
- [Examples](hcloud_load_balancer_type_info_module.md#examples)
- [Return Values](hcloud_load_balancer_type_info_module.md#return-values)

## [Synopsis](hcloud_load_balancer_type_info_module.md#id1)

- Gather infos about your Hetzner Cloud Load Balancer types.

## [Requirements](hcloud_load_balancer_type_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python-dateutil >= 2.7.5
- requests >=2.20

## [Parameters](hcloud_load_balancer_type_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  **Default:** `"https://api.hetzner.cloud/v1"` |
| **id**  integer | The ID of the Load Balancer type you want to get. |
| **name**  string | The name of the Load Balancer type you want to get. |

## [See Also](hcloud_load_balancer_type_info_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_load_balancer_type_info_module.md#id5)

```yaml+jinja
- name: Gather hcloud Load Balancer type infos
  hcloud_load_balancer_type_info:
  register: output

- name: Print the gathered infos
  debug:
    var: output.hcloud_load_balancer_type_info
```

## [Return Values](hcloud_load_balancer_type_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_load_balancer_type_info**  complex | The Load Balancer type infos as list  **Returned:** always |
| **description**  string | Description of the Load Balancer type  **Returned:** always  **Sample:** `"LB11"` |
| **id**  integer | Numeric identifier of the Load Balancer type  **Returned:** always  **Sample:** `1937415` |
| **max_assigned_certificates**  integer | Number of SSL Certificates that can be assigned to a single Load Balancer  **Returned:** always  **Sample:** `5` |
| **max_connections**  integer | Number of maximum simultaneous open connections  **Returned:** always  **Sample:** `1` |
| **max_services**  integer | Number of services a Load Balancer of this type can have  **Returned:** always  **Sample:** `1` |
| **max_targets**  integer | Number of targets a single Load Balancer can have  **Returned:** always  **Sample:** `25` |
| **name**  string | Name of the Load Balancer type  **Returned:** always  **Sample:** `"lb11"` |

### Authors

- Lukas Kaemmerling (@LKaemmerling)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
- [Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
