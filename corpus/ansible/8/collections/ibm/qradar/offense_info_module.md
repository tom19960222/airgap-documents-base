---
collection: ansible
version: "8"
title: "ibm.qradar.offense_info module – Obtain information about one or many QRadar Offenses, with filter options"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/qradar/offense_info_module.html
fetched_at: 2026-07-28T02:34:33+00:00
---
# ibm.qradar.offense_info module – Obtain information about one or many QRadar Offenses, with filter options

> **Note:**
>
> This module is part of the [ibm.qradar collection](https://galaxy.ansible.com/ui/repo/published/ibm/qradar/) (version 2.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ibm.qradar`.
>
> To use it in a playbook, specify: `ibm.qradar.offense_info`.

New in ibm.qradar 1.0.0

- [Synopsis](offense_info_module.md#synopsis)
- [Parameters](offense_info_module.md#parameters)
- [Notes](offense_info_module.md#notes)
- [Examples](offense_info_module.md#examples)
- [Return Values](offense_info_module.md#return-values)

## [Synopsis](offense_info_module.md#id1)

- This module allows to obtain information about one or many QRadar Offenses, with filter options

Aliases: qradar_offense_info

## [Parameters](offense_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **assigned_to**  string | Obtain only information of Offenses assigned to a certain user |
| **closing_reason**  string | Obtain only information of Offenses that were closed by a specific closing reason |
| **closing_reason_id**  integer | Obtain only information of Offenses that were closed by a specific closing reason ID |
| **follow_up**  boolean | Obtain only information of Offenses that are marked with the follow up flag  **Choices:**   - `false` - `true` |
| **id**  integer | Obtain only information of the Offense with provided ID |
| **name**  string | Obtain only information of the Offense that matches the provided name |
| **protected**  boolean | Obtain only information of Offenses that are protected  **Choices:**   - `false` - `true` |
| **status**  string | Obtain only information of Offenses of a certain status  **Choices:**   - `"open"` ← (default) - `"OPEN"` - `"hidden"` - `"HIDDEN"` - `"closed"` - `"CLOSED"` |

## [Notes](offense_info_module.md#id3)

> **Note:**
>
> - You may provide many filters and they will all be applied, except for `id` as that will return only

## [Examples](offense_info_module.md#id4)

```yaml+jinja
- name: Get list of all currently OPEN IBM QRadar Offenses
  ibm.qradar.offense_info:
    status: OPEN
  register: offense_list

- name: display offense information for debug purposes
  debug:
    var: offense_list
```

## [Return Values](offense_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **offenses**  list / elements=dictionary | Information  **Returned:** always |
| **qradar_offenses**  complex | IBM QRadar Offenses found based on provided filters  **Returned:** always |
| **name**  string | Name of the service.  **Returned:** always  **Sample:** `"arp-ethers.service"` |
| **source**  string | Init system of the service. One of `systemd`, `sysv`, `upstart`.  **Returned:** always  **Sample:** `"sysv"` |
| **state**  string | State of the service. Either `running`, `stopped`, or `unknown`.  **Returned:** always  **Sample:** `"running"` |
| **status**  string | State of the service. Either `enabled`, `disabled`, or `unknown`.  **Returned:** systemd systems or RedHat/SUSE flavored sysvinit/upstart  **Sample:** `"enabled"` |

### Authors

- Ansible Security Automation Team (@maxamillion) <<https://github.com/ansible-security>>

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.qradar/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.qradar)
