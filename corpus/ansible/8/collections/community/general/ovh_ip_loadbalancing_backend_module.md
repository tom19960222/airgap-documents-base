---
collection: ansible
version: "8"
title: "community.general.ovh_ip_loadbalancing_backend module – Manage OVH IP LoadBalancing backends"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ovh_ip_loadbalancing_backend_module.html
fetched_at: 2026-07-28T01:48:46+00:00
---
# community.general.ovh_ip_loadbalancing_backend module – Manage OVH IP LoadBalancing backends

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
> see [Requirements](ovh_ip_loadbalancing_backend_module.md#ansible-collections-community-general-ovh-ip-loadbalancing-backend-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ovh_ip_loadbalancing_backend`.

- [Synopsis](ovh_ip_loadbalancing_backend_module.md#synopsis)
- [Requirements](ovh_ip_loadbalancing_backend_module.md#requirements)
- [Parameters](ovh_ip_loadbalancing_backend_module.md#parameters)
- [Attributes](ovh_ip_loadbalancing_backend_module.md#attributes)
- [Notes](ovh_ip_loadbalancing_backend_module.md#notes)
- [Examples](ovh_ip_loadbalancing_backend_module.md#examples)

## [Synopsis](ovh_ip_loadbalancing_backend_module.md#id1)

- Manage OVH (French European hosting provider) LoadBalancing IP backends

Aliases: cloud.ovh.ovh_ip_loadbalancing_backend

## [Requirements](ovh_ip_loadbalancing_backend_module.md#id2)

The below requirements are needed on the host that executes this module.

- ovh > 0.3.5

## [Parameters](ovh_ip_loadbalancing_backend_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **application_key**  string / required | The applicationKey to use |
| **application_secret**  string / required | The application secret to use |
| **backend**  string / required | The IP address of the backend to update / modify / delete |
| **consumer_key**  string / required | The consumer key to use |
| **endpoint**  string / required | The endpoint to use ( for instance ovh-eu) |
| **name**  string / required | Name of the LoadBalancing internal name (ip-X.X.X.X) |
| **probe**  string | Determines the type of probe to use for this backend  **Choices:**   - `"none"` ← (default) - `"http"` - `"icmp"` - `"oco"` |
| **state**  string | Determines whether the backend is to be created/modified or deleted  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The timeout in seconds used to wait for a task to be completed.  **Default:** `120` |
| **weight**  integer | Determines the weight for this backend  **Default:** `8` |

## [Attributes](ovh_ip_loadbalancing_backend_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](ovh_ip_loadbalancing_backend_module.md#id5)

> **Note:**
>
> - Uses the python OVH Api <https://github.com/ovh/python-ovh>. You have to create an application (a key and secret) with a consumer key as described into <https://docs.ovh.com/gb/en/customer/first-steps-with-ovh-api/>

## [Examples](ovh_ip_loadbalancing_backend_module.md#id6)

```yaml+jinja
- name: Adds or modify the backend '212.1.1.1' to a loadbalancing 'ip-1.1.1.1'
  ovh_ip_loadbalancing:
    name: ip-1.1.1.1
    backend: 212.1.1.1
    state: present
    probe: none
    weight: 8
    endpoint: ovh-eu
    application_key: yourkey
    application_secret: yoursecret
    consumer_key: yourconsumerkey

- name: Removes a backend '212.1.1.1' from a loadbalancing 'ip-1.1.1.1'
  ovh_ip_loadbalancing:
    name: ip-1.1.1.1
    backend: 212.1.1.1
    state: absent
    endpoint: ovh-eu
    application_key: yourkey
    application_secret: yoursecret
    consumer_key: yourconsumerkey
```

### Authors

- Pascal Heraud (@pascalheraud)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
