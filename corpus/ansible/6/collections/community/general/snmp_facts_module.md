---
collection: ansible
version: "6"
title: "community.general.snmp_facts module – Retrieve facts for a device using SNMP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/snmp_facts_module.html
fetched_at: 2026-07-27T17:13:18+00:00
---
# community.general.snmp_facts module – Retrieve facts for a device using SNMP

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
> see [Requirements](snmp_facts_module.md#ansible-collections-community-general-snmp-facts-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.snmp_facts`.

- [Synopsis](snmp_facts_module.md#synopsis)
- [Requirements](snmp_facts_module.md#requirements)
- [Parameters](snmp_facts_module.md#parameters)
- [Examples](snmp_facts_module.md#examples)
- [Return Values](snmp_facts_module.md#return-values)

## [Synopsis](snmp_facts_module.md#id1)

- Retrieve facts for a device using SNMP, the facts will be inserted to the ansible_facts key.

## [Requirements](snmp_facts_module.md#id2)

The below requirements are needed on the host that executes this module.

- pysnmp

## [Parameters](snmp_facts_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **authkey**  string | Authentication key.  Required *version* is `v3`. |
| **community**  string | The SNMP community string, required if *version* is `v2` or `v2c`. |
| **host**  string / required | Set to target SNMP server (normally `{{ inventory_hostname }}`). |
| **integrity**  string | Hashing algorithm.  Required if *version* is `v3`.  Choices:   - `"md5"` - `"sha"` |
| **level**  string | Authentication level.  Required if *version* is `v3`.  Choices:   - `"authNoPriv"` - `"authPriv"` |
| **privacy**  string | Encryption algorithm.  Required if *level* is `authPriv`.  Choices:   - `"aes"` - `"des"` |
| **privkey**  string | Encryption key.  Required if *level* is `authPriv`. |
| **retries**  integer  added in community.general 2.3.0 | Maximum number of request retries, 0 retries means just a single request. |
| **timeout**  integer  added in community.general 2.3.0 | Response timeout in seconds. |
| **username**  string | Username for SNMPv3.  Required if *version* is `v3`. |
| **version**  string / required | SNMP Version to use, `v2`, `v2c` or `v3`.  Choices:   - `"v2"` - `"v2c"` - `"v3"` |

## [Examples](snmp_facts_module.md#id4)

```yaml+jinja
- name: Gather facts with SNMP version 2
  community.general.snmp_facts:
    host: '{{ inventory_hostname }}'
    version: v2c
    community: public
  delegate_to: local

- name: Gather facts using SNMP version 3
  community.general.snmp_facts:
    host: '{{ inventory_hostname }}'
    version: v3
    level: authPriv
    integrity: sha
    privacy: aes
    username: snmp-user
    authkey: abc12345
    privkey: def6789
  delegate_to: localhost
```

## [Return Values](snmp_facts_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ansible_all_ipv4_addresses**  list / elements=string | List of all IPv4 addresses.  Returned: success  Sample: `["127.0.0.1", "172.17.0.1"]` |
| **ansible_interfaces**  dictionary | Dictionary of each network interface and its metadata.  Returned: success  Sample: `{"1": {"adminstatus": "up", "description": "", "ifindex": "1", "ipv4": [{"address": "127.0.0.1", "netmask": "255.0.0.0"}], "mac": "", "mtu": "65536", "name": "lo", "operstatus": "up", "speed": "65536"}, "2": {"adminstatus": "up", "description": "", "ifindex": "2", "ipv4": [{"address": "192.168.213.128", "netmask": "255.255.255.0"}], "mac": "000a305a52a1", "mtu": "1500", "name": "Intel Corporation 82545EM Gigabit Ethernet Controller (Copper)", "operstatus": "up", "speed": "1500"}}` |
| **ansible_syscontact**  string | The textual identification of the contact person for this managed node, together with information on how to contact this person.  Returned: success  Sample: `"Me <me@example.org>"` |
| **ansible_sysdescr**  string | A textual description of the entity.  Returned: success  Sample: `"Linux ubuntu-user 4.4.0-93-generic"` |
| **ansible_syslocation**  string | The physical location of this node (e.g., `telephone closet, 3rd floor`).  Returned: success  Sample: `"Sitting on the Dock of the Bay"` |
| **ansible_sysname**  string | An administratively-assigned name for this managed node.  Returned: success  Sample: `"ubuntu-user"` |
| **ansible_sysobjectid**  string | The vendor’s authoritative identification of the network management subsystem contained in the entity.  Returned: success  Sample: `"1.3.6.1.4.1.8072.3.2.10"` |
| **ansible_sysuptime**  integer | The time (in hundredths of a second) since the network management portion of the system was last re-initialized.  Returned: success  Sample: `42388` |

### Authors

- Patrick Ogenstad (@ogenstad)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
