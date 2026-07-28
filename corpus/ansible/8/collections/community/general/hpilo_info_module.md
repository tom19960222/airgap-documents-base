---
collection: ansible
version: "8"
title: "community.general.hpilo_info module – Gather information through an HP iLO interface"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/hpilo_info_module.html
fetched_at: 2026-07-28T01:46:05+00:00
---
# community.general.hpilo_info module – Gather information through an HP iLO interface

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
> see [Requirements](hpilo_info_module.md#ansible-collections-community-general-hpilo-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.hpilo_info`.

- [Synopsis](hpilo_info_module.md#synopsis)
- [Requirements](hpilo_info_module.md#requirements)
- [Parameters](hpilo_info_module.md#parameters)
- [Attributes](hpilo_info_module.md#attributes)
- [Notes](hpilo_info_module.md#notes)
- [Examples](hpilo_info_module.md#examples)
- [Return Values](hpilo_info_module.md#return-values)

## [Synopsis](hpilo_info_module.md#id1)

- This module gathers information on a specific system using its HP iLO interface. These information includes hardware and network related information useful for provisioning (e.g. macaddress, uuid).
- This module requires the `hpilo` python module.
- This module was called `hpilo_facts` before Ansible 2.9, returning `ansible_facts`. Note that the [community.general.hpilo_info](hpilo_info_module.md#ansible-collections-community-general-hpilo-info-module) module no longer returns `ansible_facts`!

Aliases: remote_management.hpilo.hpilo_info

## [Requirements](hpilo_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- hpilo

## [Parameters](hpilo_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **host**  string / required | The HP iLO hostname/address that is linked to the physical system. |
| **login**  string | The login name to authenticate to the HP iLO interface.  **Default:** `"Administrator"` |
| **password**  string | The password to authenticate to the HP iLO interface.  **Default:** `"admin"` |
| **ssl_version**  string | Change the ssl_version used.  **Choices:**   - `"SSLv3"` - `"SSLv23"` - `"TLSv1"` ← (default) - `"TLSv1_1"` - `"TLSv1_2"` |

## [Attributes](hpilo_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](hpilo_info_module.md#id5)

> **Note:**
>
> - This module ought to be run from a system that can access the HP iLO interface directly, either by using `local_action` or using `delegate_to`.

## [Examples](hpilo_info_module.md#id6)

```yaml+jinja
- name: Gather facts from a HP iLO interface only if the system is an HP server
  community.general.hpilo_info:
    host: YOUR_ILO_ADDRESS
    login: YOUR_ILO_LOGIN
    password: YOUR_ILO_PASSWORD
  when: cmdb_hwmodel.startswith('HP ')
  delegate_to: localhost
  register: results

- ansible.builtin.fail:
    msg: 'CMDB serial ({{ cmdb_serialno }}) does not match hardware serial ({{ results.hw_system_serial }}) !'
  when: cmdb_serialno != results.hw_system_serial
```

## [Return Values](hpilo_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **host_power_status**  string  *added in community.general 3.5.0* | Power status of host.  Will be one of `ON`, `OFF` and `UNKNOWN`.  **Returned:** always  **Sample:** `"ON"` |
| **hw_bios_date**  string | BIOS date  **Returned:** always  **Sample:** `"05/05/2011"` |
| **hw_bios_version**  string | BIOS version  **Returned:** always  **Sample:** `"P68"` |
| **hw_eth_ilo**  dictionary | Interface information (for the iLO network interface)  **Returned:** always  **Sample:** `[{"macaddress": "00:11:22:33:44:BA"}, {"macaddress_dash": "00-11-22-33-44-BA"}]` |
| **hw_ethX**  dictionary | Interface information (for each interface)  **Returned:** always  **Sample:** `[{"macaddress": "00:11:22:33:44:55", "macaddress_dash": "00-11-22-33-44-55"}]` |
| **hw_product_name**  string | Product name  **Returned:** always  **Sample:** `"ProLiant DL360 G7"` |
| **hw_product_uuid**  string | Product UUID  **Returned:** always  **Sample:** `"ef50bac8-2845-40ff-81d9-675315501dac"` |
| **hw_system_serial**  string | System serial number  **Returned:** always  **Sample:** `"ABC12345D6"` |
| **hw_uuid**  string | Hardware UUID  **Returned:** always  **Sample:** `"123456ABC78901D2"` |

### Authors

- Dag Wieers (@dagwieers)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
