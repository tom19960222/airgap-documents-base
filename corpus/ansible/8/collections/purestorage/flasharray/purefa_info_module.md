---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_info module – Collect information from Pure Storage FlashArray"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_info_module.html
fetched_at: 2026-07-28T02:51:01+00:00
---
# purestorage.flasharray.purefa_info module – Collect information from Pure Storage FlashArray

> **Note:**
>
> This module is part of the [purestorage.flasharray collection](https://galaxy.ansible.com/ui/repo/published/purestorage/flasharray/) (version 1.24.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flasharray`.
> You need further requirements to be able to use this module,
> see [Requirements](purefa_info_module.md#ansible-collections-purestorage-flasharray-purefa-info-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_info`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_info_module.md#synopsis)
- [Requirements](purefa_info_module.md#requirements)
- [Parameters](purefa_info_module.md#parameters)
- [Notes](purefa_info_module.md#notes)
- [Examples](purefa_info_module.md#examples)
- [Return Values](purefa_info_module.md#return-values)

## [Synopsis](purefa_info_module.md#id1)

- Collect information from a Pure Storage Flasharray running the Purity//FA operating system. By default, the module will collect basic information including hosts, host groups, protection groups and volume counts. Additional information can be collected based on the configured set of arguments.

## [Requirements](purefa_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **gather_subset**  list / elements=string | When supplied, this argument will define the information to be collected. Possible values for this include all, minimum, config, performance, capacity, network, subnet, interfaces, hgroups, pgroups, hosts, admins, volumes, snapshots, pods, replication, vgroups, offload, apps, arrays, certs, kmip, clients, policies, dir_snaps, filesystems, alerts, virtual_machines, hosts_balance and subscriptions.  **Default:** `["minimum"]` |

## [Notes](purefa_info_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_info_module.md#id5)

```yaml+jinja
- name: collect default set of information
  purestorage.flasharray.purefa_info:
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
  register: array_info
- name: show default information
  debug:
    msg: "{{ array_info['purefa_info']['default'] }}"

- name: collect configuration and capacity information
  purestorage.flasharray.purefa_info:
    gather_subset:
      - config
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
  register: array_info
- name: show configuration information
  debug:
    msg: "{{ array_info['purefa_info']['config'] }}"

- name: collect all information
  purestorage.flasharray.purefa_info:
    gather_subset:
      - all
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
- name: show all information
  debug:
    msg: "{{ array_info['purefa_info'] }}"
```

## [Return Values](purefa_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **purefa_info**  dictionary | Returns the information collected from the FlashArray  **Returned:** always |

### Authors

- Pure Storage ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
- [Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
- [Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
- [Communication](index.md#communication-for-purestorage-flasharray)
