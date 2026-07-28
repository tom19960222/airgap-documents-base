---
collection: ansible
version: "6"
title: "community.general.cloud_init_data_facts module – Retrieve facts of cloud-init"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/cloud_init_data_facts_module.html
fetched_at: 2026-07-27T17:08:30+00:00
---
# community.general.cloud_init_data_facts module – Retrieve facts of cloud-init

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.cloud_init_data_facts`.

- [Synopsis](cloud_init_data_facts_module.md#synopsis)
- [Parameters](cloud_init_data_facts_module.md#parameters)
- [Notes](cloud_init_data_facts_module.md#notes)
- [Examples](cloud_init_data_facts_module.md#examples)
- [Return Values](cloud_init_data_facts_module.md#return-values)

## [Synopsis](cloud_init_data_facts_module.md#id1)

- Gathers facts by reading the status.json and result.json of cloud-init.

## [Parameters](cloud_init_data_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **filter**  string | Filter facts  Choices:   - `"status"` - `"result"` |

## [Notes](cloud_init_data_facts_module.md#id3)

> **Note:**
>
> - See <http://cloudinit.readthedocs.io/> for more information about cloud-init.

## [Examples](cloud_init_data_facts_module.md#id4)

```yaml+jinja
- name: Gather all facts of cloud init
  community.general.cloud_init_data_facts:
  register: result

- ansible.builtin.debug:
    var: result

- name: Wait for cloud init to finish
  community.general.cloud_init_data_facts:
    filter: status
  register: res
  until: "res.cloud_init_data_facts.status.v1.stage is defined and not res.cloud_init_data_facts.status.v1.stage"
  retries: 50
  delay: 5
```

## [Return Values](cloud_init_data_facts_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cloud_init_data_facts**  dictionary | Facts of result and status.  Returned: success  Sample: `"{ \"status\": { \"v1\": { \"datasource\": \"DataSourceCloudStack\", \"errors\": [] }, \"result\": { \"v1\": { \"datasource\": \"DataSourceCloudStack\", \"init\": { \"errors\": [], \"finished\": 1522066377.0185432, \"start\": 1522066375.2648022 }, \"init-local\": { \"errors\": [], \"finished\": 1522066373.70919, \"start\": 1522066373.4726632 }, \"modules-config\": { \"errors\": [], \"finished\": 1522066380.9097016, \"start\": 1522066379.0011985 }, \"modules-final\": { \"errors\": [], \"finished\": 1522066383.56594, \"start\": 1522066382.3449218 }, \"stage\": null } }"` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
