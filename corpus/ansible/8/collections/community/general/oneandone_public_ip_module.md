---
collection: ansible
version: "8"
title: "community.general.oneandone_public_ip module – Configure 1&1 public IPs"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/oneandone_public_ip_module.html
fetched_at: 2026-07-28T01:48:26+00:00
---
# community.general.oneandone_public_ip module – Configure 1&1 public IPs

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](oneandone_public_ip_module.md#ansible-collections-community-general-oneandone-public-ip-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.oneandone_public_ip`.

- [Synopsis](oneandone_public_ip_module.md#synopsis)
- [Requirements](oneandone_public_ip_module.md#requirements)
- [Parameters](oneandone_public_ip_module.md#parameters)
- [Attributes](oneandone_public_ip_module.md#attributes)
- [Examples](oneandone_public_ip_module.md#examples)
- [Return Values](oneandone_public_ip_module.md#return-values)

## [Synopsis](oneandone_public_ip_module.md#id1)

- Create, update, and remove public IPs. This module has a dependency on 1and1 >= 1.0.

Aliases: cloud.oneandone.oneandone_public_ip

## [Requirements](oneandone_public_ip_module.md#id2)

The below requirements are needed on the host that executes this module.

- 1and1
- python >= 2.6

## [Parameters](oneandone_public_ip_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_url**  string | Custom API URL. Overrides the ONEANDONE_API_URL environment variable. |
| **auth_token**  string | Authenticating API token provided by 1&1. |
| **datacenter**  string | ID of the datacenter where the IP will be created (only for unassigned IPs).  **Choices:**   - `"US"` ← (default) - `"ES"` - `"DE"` - `"GB"` |
| **public_ip_id**  string | The ID of the public IP used with update and delete states. |
| **reverse_dns**  string | Reverse DNS name. maxLength=256 |
| **state**  string | Define a public ip state to create, remove, or update.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"update"` |
| **type**  string | Type of IP. Currently, only IPV4 is available.  **Choices:**   - `"IPV4"` ← (default) - `"IPV6"` |
| **wait**  boolean | wait for the instance to be in state ‘running’ before returning  **Choices:**   - `false` - `true` ← (default) |
| **wait_interval**  integer | Defines the number of seconds to wait when using the _wait_for methods  **Default:** `5` |
| **wait_timeout**  integer | how long before wait gives up, in seconds  **Default:** `600` |

## [Attributes](oneandone_public_ip_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](oneandone_public_ip_module.md#id5)

```yaml+jinja
- name: Create a public IP
  community.general.oneandone_public_ip:
    auth_token: oneandone_private_api_key
    reverse_dns: example.com
    datacenter: US
    type: IPV4

- name: Update a public IP
  community.general.oneandone_public_ip:
    auth_token: oneandone_private_api_key
    public_ip_id: public ip id
    reverse_dns: secondexample.com
    state: update

- name: Delete a public IP
  community.general.oneandone_public_ip:
    auth_token: oneandone_private_api_key
    public_ip_id: public ip id
    state: absent
```

## [Return Values](oneandone_public_ip_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **public_ip**  dictionary | Information about the public ip that was processed  **Returned:** always  **Sample:** `{"id": "F77CC589EBC120905B4F4719217BFF6D", "ip": "10.5.132.106"}` |

### Authors

- Amel Ajdinovic (@aajdinov)
- Ethan Devenport (@edevenport)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
