---
collection: ansible
version: "8"
title: "community.general.ibm_sa_domain module – Manages domains on IBM Spectrum Accelerate Family storage systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ibm_sa_domain_module.html
fetched_at: 2026-07-28T01:46:16+00:00
---
# community.general.ibm_sa_domain module – Manages domains on IBM Spectrum Accelerate Family storage systems

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
> see [Requirements](ibm_sa_domain_module.md#ansible-collections-community-general-ibm-sa-domain-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ibm_sa_domain`.

- [Synopsis](ibm_sa_domain_module.md#synopsis)
- [Requirements](ibm_sa_domain_module.md#requirements)
- [Parameters](ibm_sa_domain_module.md#parameters)
- [Attributes](ibm_sa_domain_module.md#attributes)
- [Notes](ibm_sa_domain_module.md#notes)
- [Examples](ibm_sa_domain_module.md#examples)
- [Return Values](ibm_sa_domain_module.md#return-values)

## [Synopsis](ibm_sa_domain_module.md#id1)

- This module can be used to add domains to or removes them from IBM Spectrum Accelerate Family storage systems.

Aliases: storage.ibm.ibm_sa_domain

## [Requirements](ibm_sa_domain_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- pyxcli

## [Parameters](ibm_sa_domain_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **domain**  string / required | Name of the domain to be managed. |
| **endpoints**  string / required | The hostname or management IP of Spectrum Accelerate storage system. |
| **hard_capacity**  string | Hard capacity of the domain. |
| **ldap_id**  string | ldap id to add to the domain. |
| **max_cgs**  string | Number of max cgs. |
| **max_dms**  string | Number of max dms. |
| **max_mirrors**  string | Number of max_mirrors. |
| **max_pools**  string | Number of max_pools. |
| **max_volumes**  string | Number of max_volumes. |
| **password**  string / required | Password for username on the spectrum accelerate storage system. |
| **perf_class**  string | Add the domain to a performance class. |
| **size**  string | Size of the domain. |
| **soft_capacity**  string | Soft capacity of the domain. |
| **state**  string | The desired state of the domain.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  string / required | Management user on the spectrum accelerate storage system. |

## [Attributes](ibm_sa_domain_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](ibm_sa_domain_module.md#id5)

> **Note:**
>
> - This module requires pyxcli python library. Use ‘pip install pyxcli’ in order to get pyxcli.

## [Examples](ibm_sa_domain_module.md#id6)

```yaml+jinja
- name: Define new domain.
  community.general.ibm_sa_domain:
    domain: domain_name
    size: domain_size
    state: present
    username: admin
    password: secret
    endpoints: hostdev-system

- name: Delete domain.
  community.general.ibm_sa_domain:
    domain: domain_name
    state: absent
    username: admin
    password: secret
    endpoints: hostdev-system
```

## [Return Values](ibm_sa_domain_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | module return status.  **Returned:** as needed  **Sample:** `"domain 'domain_name' created successfully."` |

### Authors

- Tzur Eliyahu (@tzure)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
