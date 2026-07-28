---
collection: ansible
version: "6"
title: "community.general.manageiq_tags_info module – Retrieve resource tags in ManageIQ"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/manageiq_tags_info_module.html
fetched_at: 2026-07-27T17:10:49+00:00
---
# community.general.manageiq_tags_info module – Retrieve resource tags in ManageIQ

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](manageiq_tags_info_module.md#ansible-collections-community-general-manageiq-tags-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.manageiq_tags_info`.

New in community.general 5.8.0

- [Synopsis](manageiq_tags_info_module.md#synopsis)
- [Requirements](manageiq_tags_info_module.md#requirements)
- [Parameters](manageiq_tags_info_module.md#parameters)
- [Examples](manageiq_tags_info_module.md#examples)
- [Return Values](manageiq_tags_info_module.md#return-values)

## [Synopsis](manageiq_tags_info_module.md#id1)

- This module supports retrieving resource tags from ManageIQ.

## [Requirements](manageiq_tags_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- manageiq-client <https://github.com/ManageIQ/manageiq-api-client-python/>

## [Parameters](manageiq_tags_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **manageiq_connection**  dictionary | ManageIQ connection configuration information. |
| **ca_cert**  aliases: ca_bundle_path  string | The path to a CA bundle file or directory with certificates. defaults to None. |
| **password**  string | ManageIQ password. `MIQ_PASSWORD` env var if set. otherwise, required if no token is passed in. |
| **token**  string | ManageIQ token. `MIQ_TOKEN` env var if set. otherwise, required if no username or password is passed in. |
| **url**  string | ManageIQ environment url. `MIQ_URL` env var if set. otherwise, it is required to pass it. |
| **username**  string | ManageIQ username. `MIQ_USERNAME` env var if set. otherwise, required if no token is passed in. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether SSL certificates should be verified for HTTPS requests. defaults to True.  Choices:   - `false` - `true` ← (default) |
| **resource_id**  integer | The ID of the resource at which tags will be controlled.  Must be specified if *resource_name* is not set. Both options are mutually exclusive. |
| **resource_name**  string | The name of the resource at which tags will be controlled.  Must be specified if *resource_id* is not set. Both options are mutually exclusive. |
| **resource_type**  string / required | The relevant resource type in ManageIQ.  Choices:   - `"provider"` - `"host"` - `"vm"` - `"blueprint"` - `"category"` - `"cluster"` - `"data store"` - `"group"` - `"resource pool"` - `"service"` - `"service template"` - `"template"` - `"tenant"` - `"user"` |

## [Examples](manageiq_tags_info_module.md#id4)

```yaml+jinja
- name: List current tags for a provider in ManageIQ.
  community.general.manageiq_tags_info:
    resource_name: 'EngLab'
    resource_type: 'provider'
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
  register: result
```

## [Return Values](manageiq_tags_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **tags**  list / elements=dictionary | List of tags associated with the resource.  Returned: on success |

### Authors

- Alexei Znamensky (@russoz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
