---
collection: ansible
version: "8"
title: "community.general.manageiq_tags module – Management of resource tags in ManageIQ"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/manageiq_tags_module.html
fetched_at: 2026-07-28T01:47:50+00:00
---
# community.general.manageiq_tags module – Management of resource tags in ManageIQ

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
> see [Requirements](manageiq_tags_module.md#ansible-collections-community-general-manageiq-tags-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.manageiq_tags`.

- [Synopsis](manageiq_tags_module.md#synopsis)
- [Requirements](manageiq_tags_module.md#requirements)
- [Parameters](manageiq_tags_module.md#parameters)
- [Attributes](manageiq_tags_module.md#attributes)
- [Examples](manageiq_tags_module.md#examples)

## [Synopsis](manageiq_tags_module.md#id1)

- The manageiq_tags module supports adding, updating and deleting tags in ManageIQ.

Aliases: remote_management.manageiq.manageiq_tags

## [Requirements](manageiq_tags_module.md#id2)

The below requirements are needed on the host that executes this module.

- manageiq-client <https://github.com/ManageIQ/manageiq-api-client-python/>

## [Parameters](manageiq_tags_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **manageiq_connection**  dictionary | ManageIQ connection configuration information. |
| **ca_cert**  aliases: ca_bundle_path  string | The path to a CA bundle file or directory with certificates. |
| **password**  string | ManageIQ password. `MIQ_PASSWORD` environment variable if set. Otherwise, required if no token is passed in. |
| **token**  string | ManageIQ token. `MIQ_TOKEN` environment variable if set. Otherwise, required if no username or password is passed in. |
| **url**  string | ManageIQ environment URL. `MIQ_URL` environment variable if set. Otherwise, it is required to pass it. |
| **username**  string | ManageIQ username. `MIQ_USERNAME` environment variable if set. Otherwise, required if no token is passed in. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether SSL certificates should be verified for HTTPS requests.  **Choices:**   - `false` - `true` ← (default) |
| **resource_id**  integer  *added in community.general 2.2.0* | The ID of the resource at which tags will be controlled.  Must be specified if `resource_name` is not set. Both options are mutually exclusive. |
| **resource_name**  string | The name of the resource at which tags will be controlled.  Must be specified if `resource_id` is not set. Both options are mutually exclusive. |
| **resource_type**  string / required | The relevant resource type in manageiq.  **Choices:**   - `"provider"` - `"host"` - `"vm"` - `"blueprint"` - `"category"` - `"cluster"` - `"data store"` - `"group"` - `"resource pool"` - `"service"` - `"service template"` - `"template"` - `"tenant"` - `"user"` |
| **state**  string | `absent` - tags should not exist.  `present` - tags should exist.  `list` - list current tags. This state is deprecated and will be removed 8.0.0. Please use the module [community.general.manageiq_tags_info](manageiq_tags_info_module.md#ansible-collections-community-general-manageiq-tags-info-module) instead.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"list"` |
| **tags**  list / elements=dictionary | `tags` - list of dictionaries, each includes `name` and `category` keys.  Required if `state` is `present` or `absent`. |

## [Attributes](manageiq_tags_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](manageiq_tags_module.md#id5)

```yaml+jinja
- name: Create new tags for a provider in ManageIQ.
  community.general.manageiq_tags:
    resource_name: 'EngLab'
    resource_type: 'provider'
    tags:
    - category: environment
      name: prod
    - category: owner
      name: prod_ops
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      validate_certs: false

- name: Create new tags for a provider in ManageIQ.
  community.general.manageiq_tags:
    resource_id: 23000000790497
    resource_type: 'provider'
    tags:
    - category: environment
      name: prod
    - category: owner
      name: prod_ops
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      validate_certs: false

- name: Remove tags for a provider in ManageIQ.
  community.general.manageiq_tags:
    state: absent
    resource_name: 'EngLab'
    resource_type: 'provider'
    tags:
    - category: environment
      name: prod
    - category: owner
      name: prod_ops
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      validate_certs: false
```

### Authors

- Daniel Korn (@dkorn)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
