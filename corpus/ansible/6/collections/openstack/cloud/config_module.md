---
collection: ansible
version: "6"
title: "openstack.cloud.config module – Get OpenStack Client config"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/config_module.html
fetched_at: 2026-07-28T00:16:29+00:00
---
# openstack.cloud.config module – Get OpenStack Client config

> **Note:**
>
> This module is part of the [openstack.cloud collection](https://galaxy.ansible.com/openstack/cloud) (version 1.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install openstack.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](config_module.md#ansible-collections-openstack-cloud-config-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.config`.

- [Synopsis](config_module.md#synopsis)
- [Requirements](config_module.md#requirements)
- [Parameters](config_module.md#parameters)
- [Notes](config_module.md#notes)
- [Examples](config_module.md#examples)

## [Synopsis](config_module.md#id1)

- Get *openstack* client config data from clouds.yaml or environment

## [Requirements](config_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk

## [Parameters](config_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **clouds**  list / elements=string | List of clouds to limit the return list to. No value means return information on all configured clouds  Default: `[]` |

## [Notes](config_module.md#id4)

> **Note:**
>
> - Facts are placed in the `openstack.clouds` variable.

## [Examples](config_module.md#id5)

```yaml+jinja
- name: Get list of clouds that do not support security groups
  openstack.cloud.config:

- debug:
    var: "{{ item }}"
  with_items: "{{ openstack.clouds | rejectattr('secgroup_source', 'none') | list }}"

- name: Get the information back just about the mordred cloud
  openstack.cloud.config:
    clouds:
      - mordred
```

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
