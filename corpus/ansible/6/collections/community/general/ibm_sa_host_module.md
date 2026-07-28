---
collection: ansible
version: "6"
title: "community.general.ibm_sa_host module – Adds hosts to or removes them from IBM Spectrum Accelerate Family storage systems"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/ibm_sa_host_module.html
fetched_at: 2026-07-27T17:09:34+00:00
---
# community.general.ibm_sa_host module – Adds hosts to or removes them from IBM Spectrum Accelerate Family storage systems

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
> see [Requirements](ibm_sa_host_module.md#ansible-collections-community-general-ibm-sa-host-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ibm_sa_host`.

- [Synopsis](ibm_sa_host_module.md#synopsis)
- [Requirements](ibm_sa_host_module.md#requirements)
- [Parameters](ibm_sa_host_module.md#parameters)
- [Notes](ibm_sa_host_module.md#notes)
- [Examples](ibm_sa_host_module.md#examples)

## [Synopsis](ibm_sa_host_module.md#id1)

- This module adds hosts to or removes them from IBM Spectrum Accelerate Family storage systems.

## [Requirements](ibm_sa_host_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- pyxcli

## [Parameters](ibm_sa_host_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cluster**  string | The name of the cluster to include the host. |
| **domain**  string | The domains the cluster will be attached to. To include more than one domain, separate domain names with commas. To include all existing domains, use an asterisk (”\*”). |
| **endpoints**  string / required | The hostname or management IP of Spectrum Accelerate storage system. |
| **host**  string / required | Host name. |
| **iscsi_chap_name**  string | The host’s CHAP name identifier |
| **iscsi_chap_secret**  string | The password of the initiator used to authenticate to the system when CHAP is enable |
| **password**  string / required | Password for username on the spectrum accelerate storage system. |
| **state**  string | Host state.  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  string / required | Management user on the spectrum accelerate storage system. |

## [Notes](ibm_sa_host_module.md#id4)

> **Note:**
>
> - This module requires pyxcli python library. Use ‘pip install pyxcli’ in order to get pyxcli.

## [Examples](ibm_sa_host_module.md#id5)

```yaml+jinja
- name: Define new host.
  community.general.ibm_sa_host:
    host: host_name
    state: present
    username: admin
    password: secret
    endpoints: hostdev-system

- name: Delete host.
  community.general.ibm_sa_host:
    host: host_name
    state: absent
    username: admin
    password: secret
    endpoints: hostdev-system
```

### Authors

- Tzur Eliyahu (@tzure)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
