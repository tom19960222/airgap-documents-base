---
collection: ansible
version: "8"
title: "openstack.cloud.config module – Get OpenStack Client config"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/config_module.html
fetched_at: 2026-07-28T02:47:37+00:00
---
# openstack.cloud.config module – Get OpenStack Client config

> **Note:**
>
> This module is part of the [openstack.cloud collection](https://galaxy.ansible.com/ui/repo/published/openstack/cloud/) (version 2.2.0).
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
- [Examples](config_module.md#examples)
- [Return Values](config_module.md#return-values)

## [Synopsis](config_module.md#id1)

- Get OpenStack cloud credentials and configuration, e.g. from clouds.yaml and environment variables.

## [Requirements](config_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](config_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **clouds**  list / elements=string | List of clouds to limit the return list to.  When *clouds* is not defined, then data is returned for all configured clouds.  **Default:** `[]` |

## [Examples](config_module.md#id4)

```yaml+jinja
- name: Read configuration of all defined clouds
  openstack.cloud.config:
  register: config

- name: Print clouds which do not support security groups
  loop: "{{ config.clouds }}"
  when: item.config.secgroup_source|default(None) != None
  debug:
    var: item

- name: Read configuration of a two specific clouds
  openstack.cloud.config:
    clouds:
      - devstack
      - mordred
```

## [Return Values](config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **clouds**  list / elements=dictionary | List of OpenStack cloud configurations.  **Returned:** always |
| **config**  dictionary | A dict of configuration values for the CloudRegion and its services. The key for a ${config_option} for a specific ${service} should be ${service}_${config_option}.  **Returned:** success |
| **name**  string | Name of the cloud.  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
