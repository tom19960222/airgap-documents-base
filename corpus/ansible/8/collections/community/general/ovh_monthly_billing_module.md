---
collection: ansible
version: "8"
title: "community.general.ovh_monthly_billing module – Manage OVH monthly billing"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ovh_monthly_billing_module.html
fetched_at: 2026-07-28T01:48:47+00:00
---
# community.general.ovh_monthly_billing module – Manage OVH monthly billing

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
> see [Requirements](ovh_monthly_billing_module.md#ansible-collections-community-general-ovh-monthly-billing-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ovh_monthly_billing`.

New in community.general 0.2.0

- [Synopsis](ovh_monthly_billing_module.md#synopsis)
- [Requirements](ovh_monthly_billing_module.md#requirements)
- [Parameters](ovh_monthly_billing_module.md#parameters)
- [Attributes](ovh_monthly_billing_module.md#attributes)
- [Examples](ovh_monthly_billing_module.md#examples)

## [Synopsis](ovh_monthly_billing_module.md#id1)

- Enable monthly billing on OVH cloud instances (be aware OVH does not allow to disable it).

Aliases: cloud.ovh.ovh_monthly_billing

## [Requirements](ovh_monthly_billing_module.md#id2)

The below requirements are needed on the host that executes this module.

- ovh

## [Parameters](ovh_monthly_billing_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **application_key**  string | The applicationKey to use |
| **application_secret**  string | The application secret to use |
| **consumer_key**  string | The consumer key to use |
| **endpoint**  string | The endpoint to use (for instance ovh-eu) |
| **instance_id**  string / required | ID of the instance, get it with <https://api.ovh.com/console/#/cloud/project/%257BserviceName%257D>/instance#GET |
| **project_id**  string / required | ID of the project, get it with <https://api.ovh.com/console/#/cloud>/project#GET |

## [Attributes](ovh_monthly_billing_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](ovh_monthly_billing_module.md#id5)

```yaml+jinja
- name: Basic usage, using auth from /etc/ovh.conf
  community.general.ovh_monthly_billing:
    project_id: 0c727a20aa144485b70c44dee9123b46
    instance_id: 8fa89ad2-8f08-4220-9fa4-9695ea23e948

# Get openstack cloud ID and instance ID, OVH use them in its API
- name: Get openstack cloud ID and instance ID
  os_server_info:
    cloud: myProjectName
    region_name: myRegionName
    server: myServerName
  register: openstack_servers

- name: Use IDs
  community.general.ovh_monthly_billing:
    project_id: "{{ openstack_servers.0.tenant_id }}"
    instance_id: "{{ openstack_servers.0.id }}"
    application_key: yourkey
    application_secret: yoursecret
    consumer_key: yourconsumerkey
```

### Authors

- Francois Lallart (@fraff)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
