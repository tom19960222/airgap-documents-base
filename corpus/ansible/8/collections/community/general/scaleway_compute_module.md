---
collection: ansible
version: "8"
title: "community.general.scaleway_compute module – Scaleway compute management module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/scaleway_compute_module.html
fetched_at: 2026-07-28T01:50:08+00:00
---
# community.general.scaleway_compute module – Scaleway compute management module

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.scaleway_compute`.

- [Synopsis](scaleway_compute_module.md#synopsis)
- [Parameters](scaleway_compute_module.md#parameters)
- [Attributes](scaleway_compute_module.md#attributes)
- [Notes](scaleway_compute_module.md#notes)
- [Examples](scaleway_compute_module.md#examples)

## [Synopsis](scaleway_compute_module.md#id1)

- This module manages compute instances on Scaleway.

Aliases: cloud.scaleway.scaleway_compute

## [Parameters](scaleway_compute_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  aliases: timeout  integer | HTTP timeout to Scaleway API in seconds.  **Default:** `30` |
| **api_token**  aliases: oauth_token  string / required | Scaleway OAuth token. |
| **api_url**  aliases: base_url  string | Scaleway API URL.  **Default:** `"https://api.scaleway.com"` |
| **commercial_type**  string / required | Commercial name of the compute node |
| **enable_ipv6**  boolean | Enable public IPv6 connectivity on the instance  **Choices:**   - `false` ← (default) - `true` |
| **image**  string / required | Image identifier used to start the instance with |
| **name**  string | Name of the instance |
| **organization**  string | Organization identifier.  Exactly one of `project` and `organization` must be specified. |
| **project**  string  *added in community.general 4.3.0* | Project identifier.  Exactly one of `project` and `organization` must be specified. |
| **public_ip**  string | Manage public IP on a Scaleway server  Could be Scaleway IP address UUID  `dynamic` Means that IP is destroyed at the same time the host is destroyed  `absent` Means no public IP at all  **Default:** `"absent"` |
| **query_parameters**  dictionary | List of parameters passed to the query string.  **Default:** `{}` |
| **region**  string / required | Scaleway compute zone  **Choices:**   - `"ams1"` - `"EMEA-NL-EVS"` - `"par1"` - `"EMEA-FR-PAR1"` - `"par2"` - `"EMEA-FR-PAR2"` - `"waw1"` - `"EMEA-PL-WAW1"` |
| **security_group**  string | Security group unique identifier  If no value provided, the default security group or current security group will be used |
| **state**  string | Indicate desired state of the instance.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"running"` - `"restarted"` - `"stopped"` |
| **tags**  list / elements=string | List of tags to apply to the instance (5 max)  **Default:** `[]` |
| **validate_certs**  boolean | Validate SSL certs of the Scaleway API.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean | Wait for the instance to reach its desired state before returning.  **Choices:**   - `false` ← (default) - `true` |
| **wait_sleep_time**  integer | Time to wait before every attempt to check the state of the server  **Default:** `3` |
| **wait_timeout**  integer | Time to wait for the server to reach the expected state  **Default:** `300` |

## [Attributes](scaleway_compute_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](scaleway_compute_module.md#id4)

> **Note:**
>
> - Also see the API documentation on <https://developer.scaleway.com/>
> - If `api_token` is not set within the module, the following environment variables can be used in decreasing order of precedence [`SCW_TOKEN`](../../environment_variables.md#envvar-SCW_TOKEN), [`SCW_API_KEY`](../../environment_variables.md#envvar-SCW_API_KEY), [`SCW_OAUTH_TOKEN`](../../environment_variables.md#envvar-SCW_OAUTH_TOKEN) or `SCW_API_TOKEN`.
> - If one wants to use a different `api_url` one can also set the `SCW_API_URL` environment variable.

## [Examples](scaleway_compute_module.md#id5)

```yaml+jinja
- name: Create a server
  community.general.scaleway_compute:
    name: foobar
    state: present
    image: 89ee4018-f8c3-4dc4-a6b5-bca14f985ebe
    project: 951df375-e094-4d26-97c1-ba548eeb9c42
    region: ams1
    commercial_type: VC1S
    tags:
      - test
      - www

- name: Create a server attached to a security group
  community.general.scaleway_compute:
    name: foobar
    state: present
    image: 89ee4018-f8c3-4dc4-a6b5-bca14f985ebe
    project: 951df375-e094-4d26-97c1-ba548eeb9c42
    region: ams1
    commercial_type: VC1S
    security_group: 4a31b633-118e-4900-bd52-facf1085fc8d
    tags:
      - test
      - www

- name: Destroy it right after
  community.general.scaleway_compute:
    name: foobar
    state: absent
    image: 89ee4018-f8c3-4dc4-a6b5-bca14f985ebe
    project: 951df375-e094-4d26-97c1-ba548eeb9c42
    region: ams1
    commercial_type: VC1S
```

### Authors

- Remy Leone (@remyleone)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
