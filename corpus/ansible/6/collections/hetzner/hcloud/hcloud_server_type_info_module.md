---
collection: ansible
version: "6"
title: "hetzner.hcloud.hcloud_server_type_info module – Gather infos about the Hetzner Cloud server types."
source_url: https://docs.ansible.com/projects/ansible/6/collections/hetzner/hcloud/hcloud_server_type_info_module.html
fetched_at: 2026-07-27T17:49:52+00:00
---
# hetzner.hcloud.hcloud_server_type_info module – Gather infos about the Hetzner Cloud server types.

> **Note:**
>
> This module is part of the [hetzner.hcloud collection](https://galaxy.ansible.com/hetzner/hcloud) (version 1.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hetzner.hcloud`.
> You need further requirements to be able to use this module,
> see [Requirements](hcloud_server_type_info_module.md#ansible-collections-hetzner-hcloud-hcloud-server-type-info-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_server_type_info`.

- [Synopsis](hcloud_server_type_info_module.md#synopsis)
- [Requirements](hcloud_server_type_info_module.md#requirements)
- [Parameters](hcloud_server_type_info_module.md#parameters)
- [See Also](hcloud_server_type_info_module.md#see-also)
- [Examples](hcloud_server_type_info_module.md#examples)
- [Return Values](hcloud_server_type_info_module.md#return-values)

## [Synopsis](hcloud_server_type_info_module.md#id1)

- Gather infos about your Hetzner Cloud server types.
- This module was called `hcloud_server_type_facts` before Ansible 2.9, returning `ansible_facts` and `hcloud_server_type_facts`. Note that the [hetzner.hcloud.hcloud_server_type_info](hcloud_server_type_info_module.md#ansible-collections-hetzner-hcloud-hcloud-server-type-info-module) module no longer returns `ansible_facts` and the value was renamed to `hcloud_server_type_info`!

## [Requirements](hcloud_server_type_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- hcloud-python >= 1.0.0

## [Parameters](hcloud_server_type_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  Default: `"https://api.hetzner.cloud/v1"` |
| **id**  integer | The ID of the server type you want to get. |
| **name**  string | The name of the server type you want to get. |

## [See Also](hcloud_server_type_info_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_server_type_info_module.md#id5)

```yaml+jinja
- name: Gather hcloud server type infos
  hcloud_server_type_info:
  register: output

- name: Print the gathered infos
  debug:
    var: output.hcloud_server_type_info
```

## [Return Values](hcloud_server_type_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_server_type_info**  complex | The server type infos as list  Returned: always |
| **cores**  integer | Number of cpu cores a server of this type will have  Returned: always  Sample: `1` |
| **cpu_type**  string | Type of cpu  Returned: always  Sample: `"shared"` |
| **description**  string | Detail description of the server type  Returned: always  Sample: `"Falkenstein DC Park 1"` |
| **disk**  integer | Disk size a server of this type will have in GB  Returned: always  Sample: `25` |
| **id**  integer | Numeric identifier of the server type  Returned: always  Sample: `1937415` |
| **memory**  integer | Memory a server of this type will have in GB  Returned: always  Sample: `1` |
| **name**  string | Name of the server type  Returned: always  Sample: `"fsn1"` |
| **storage_type**  string | Type of server boot drive  Returned: always  Sample: `"local"` |

### Authors

- Lukas Kaemmerling (@LKaemmerling)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
[Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
