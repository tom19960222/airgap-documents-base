---
collection: ansible
version: "8"
title: "hetzner.hcloud.hcloud_floating_ip_info module – Gather infos about the Hetzner Cloud Floating IPs."
source_url: https://docs.ansible.com/projects/ansible/8/collections/hetzner/hcloud/hcloud_floating_ip_info_module.html
fetched_at: 2026-07-28T02:33:57+00:00
---
# hetzner.hcloud.hcloud_floating_ip_info module – Gather infos about the Hetzner Cloud Floating IPs.

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
> see [Requirements](hcloud_floating_ip_info_module.md#ansible-collections-hetzner-hcloud-hcloud-floating-ip-info-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_floating_ip_info`.

- [Synopsis](hcloud_floating_ip_info_module.md#synopsis)
- [Requirements](hcloud_floating_ip_info_module.md#requirements)
- [Parameters](hcloud_floating_ip_info_module.md#parameters)
- [See Also](hcloud_floating_ip_info_module.md#see-also)
- [Examples](hcloud_floating_ip_info_module.md#examples)
- [Return Values](hcloud_floating_ip_info_module.md#return-values)

## [Synopsis](hcloud_floating_ip_info_module.md#id1)

- Gather facts about your Hetzner Cloud Floating IPs.
- This module was called `hcloud_floating_ip_facts` before Ansible 2.9, returning `ansible_facts` and `hcloud_floating_ip_facts`. Note that the [hetzner.hcloud.hcloud_floating_ip_info](hcloud_floating_ip_info_module.md#ansible-collections-hetzner-hcloud-hcloud-floating-ip-info-module) module no longer returns `ansible_facts` and the value was renamed to `hcloud_floating_ip_info`!

Aliases: hcloud_floating_ip_facts

## [Requirements](hcloud_floating_ip_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python-dateutil >= 2.7.5
- requests >=2.20

## [Parameters](hcloud_floating_ip_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  **Default:** `"https://api.hetzner.cloud/v1"` |
| **id**  integer | The ID of the Floating IP you want to get. |
| **label_selector**  string | The label selector for the Floating IP you want to get. |

## [See Also](hcloud_floating_ip_info_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_floating_ip_info_module.md#id5)

```yaml+jinja
- name: Gather hcloud Floating ip infos
  hcloud_floating_ip_info:
  register: output
- name: Print the gathered infos
  debug:
    var: output
```

## [Return Values](hcloud_floating_ip_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_floating_ip_info**  complex | The Floating ip infos as list  **Returned:** always |
| **delete_protection**  boolean  *added in hetzner.hcloud 0.1.0* | True if the Floating IP is protected for deletion  **Returned:** always |
| **description**  string | Description of the Floating IP  **Returned:** always  **Sample:** `"Falkenstein DC 8"` |
| **home_location**  string | Location the Floating IP was created in  **Returned:** always  **Sample:** `"fsn1"` |
| **id**  integer | Numeric identifier of the Floating IP  **Returned:** always  **Sample:** `1937415` |
| **ip**  string | IP address of the Floating IP  **Returned:** always  **Sample:** `"131.232.99.1"` |
| **labels**  dictionary | User-defined labels (key-value pairs)  **Returned:** always |
| **name**  string  *added in hetzner.hcloud 0.1.0* | Name of the Floating IP  **Returned:** Always  **Sample:** `"my-floating-ip"` |
| **server**  string | Name of the server where the Floating IP is assigned to.  **Returned:** always  **Sample:** `"my-server"` |
| **type**  string | Type of the Floating IP  **Returned:** always  **Sample:** `"ipv4"` |

### Authors

- Lukas Kaemmerling (@LKaemmerling)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
- [Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
