---
collection: ansible
version: "8"
title: "hpe.nimble.hpe_nimble_partner module – Manage the HPE Nimble Storage Replication Partner"
source_url: https://docs.ansible.com/projects/ansible/8/collections/hpe/nimble/hpe_nimble_partner_module.html
fetched_at: 2026-07-28T02:34:23+00:00
---
# hpe.nimble.hpe_nimble_partner module – Manage the HPE Nimble Storage Replication Partner

> **Note:**
>
> This module is part of the [hpe.nimble collection](https://galaxy.ansible.com/ui/repo/published/hpe/nimble/) (version 1.1.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hpe.nimble`.
> You need further requirements to be able to use this module,
> see [Requirements](hpe_nimble_partner_module.md#ansible-collections-hpe-nimble-hpe-nimble-partner-module-requirements) for details.
>
> To use it in a playbook, specify: `hpe.nimble.hpe_nimble_partner`.

New in hpe.nimble 1.0.0

- [Synopsis](hpe_nimble_partner_module.md#synopsis)
- [Requirements](hpe_nimble_partner_module.md#requirements)
- [Parameters](hpe_nimble_partner_module.md#parameters)
- [Notes](hpe_nimble_partner_module.md#notes)
- [Examples](hpe_nimble_partner_module.md#examples)

## [Synopsis](hpe_nimble_partner_module.md#id1)

- Manage the replication partner on an HPE Nimble Storage group.

## [Requirements](hpe_nimble_partner_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later
- Python 3.6 or later
- HPE Nimble Storage SDK for Python
- HPE Nimble Storage arrays running NimbleOS 5.0 or later

## [Parameters](hpe_nimble_partner_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **control_port**  integer | Port number of partner control interface. Value -1 for an invalid port or a positive integer value up to 65535 representing the TCP/IP port. |
| **data_port**  integer | Port number of partner data interface. Value -1 for an invalid port or a positive integer value up to 65535 representing the TCP/IP port. |
| **description**  string | Description of replication partner. |
| **downstream_hostname**  string / required | IP address or hostname of partner interface. This must be the partner’s Group Management IP address. String of up to 64 alphanumeric characters, - and . and ‘:’ are allowed after first character. |
| **folder**  string | The Folder ID within the pool where volumes replicated from this partner will be created. This is not supported for pool partners. |
| **host**  string / required | HPE Nimble Storage IP address. |
| **match_folder**  boolean | Indicates whether to match the upstream volume’s folder on the downstream.  **Choices:**   - `false` - `true` |
| **name**  string | Name of replication partner. String of up to 64 alphanumeric characters, - and . and ‘:’ are allowed after first character. |
| **password**  string / required | HPE Nimble Storage password. |
| **pause**  boolean | Pause replication for the specified partner.  **Choices:**   - `false` - `true` |
| **pool**  string | The pool name where volumes replicated from this partner will be created. Replica volumes created as clones ignore this parameter and are always created in the same pool as their parent volume. |
| **repl_data_hostname**  string | IP address or hostname of partner data interface. String of up to 64 alphanumeric characters, - and . and ‘:’ are allowed after first character. |
| **resume**  boolean | Resume replication for the specified partner.  **Choices:**   - `false` - `true` |
| **secret**  string | Replication partner shared secret, used for mutual authentication of the partners. |
| **state**  string / required | The replication partner operation.  **Choices:**   - `"create"` - `"present"` - `"absent"` |
| **subnet_label**  string | Indicates whether to match the upstream volume’s folder on the downstream. |
| **subnet_type**  string | Type of the subnet used to replicate to this partner.  **Choices:**   - `"invalid"` - `"unconfigured"` - `"unconfigured"` - `"mgmt"` - `"data"` - `"mgmt_data"` |
| **test**  boolean | Test connectivity to the specified partner.  **Choices:**   - `false` - `true` |
| **throttles**  list / elements=dictionary | Throttles used while replicating from/to this partner. All the throttles for the partner. |
| **username**  string / required | HPE Nimble Storage user name. |

## [Notes](hpe_nimble_partner_module.md#id4)

> **Note:**
>
> - This module does not support `check_mode`.

## [Examples](hpe_nimble_partner_module.md#id5)

```yaml+jinja
# if state is create, then create partner, fails if it exist or cannot create
# if state is present, then create partner if not present ,else success
- name: Create Partner
  hpe.nimble.hpe_nimble_partner:
    host: "{{ host }}"  # upstream host
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name | mandatory }}"
    description: "{{ description }}"
    downstream_hostname: "{{ downstream_hostname | mandatory }}"
    secret: "{{ secret | mandatory }}"
    subnet_label: "{{ subnet_label | mandatory }}"
    state: "{{ state | default('present') }}"

- name: Delete Partner
  hpe.nimble.hpe_nimble_partner:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    downstream_hostname: "{{ downstream_hostname | mandatory }}"
    state: "absent"

- name: Test Partner
  hpe.nimble.hpe_nimble_partner:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    downstream_hostname: "{{ downstream_hostname | mandatory }}"
    state: "present"
    test: true

- name: Pause Partner
  hpe.nimble.hpe_nimble_partner:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    downstream_hostname: "{{ downstream_hostname | mandatory }}"
    state: "present"
    pause: true

- name: Resume Partner
  hpe.nimble.hpe_nimble_partner:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    downstream_hostname: "{{ downstream_hostname | mandatory }}"
    state: "present"
    resume: true
```

### Authors

- HPE Nimble Storage Ansible Team (@ar-india)

### Collection links

- [Issue Tracker](https://github.com/hpe-storage/nimble-ansible-modules/issues)
- [Homepage](http://hpe.com/storage/nimble)
- [Repository (Sources)](https://github.com/hpe-storage/nimble-ansible-modules)
