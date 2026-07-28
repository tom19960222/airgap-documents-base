---
collection: ansible
version: "8"
title: "community.general.omapi_host module – Setup OMAPI hosts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/omapi_host_module.html
fetched_at: 2026-07-28T01:48:18+00:00
---
# community.general.omapi_host module – Setup OMAPI hosts

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
> see [Requirements](omapi_host_module.md#ansible-collections-community-general-omapi-host-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.omapi_host`.

- [Synopsis](omapi_host_module.md#synopsis)
- [Requirements](omapi_host_module.md#requirements)
- [Parameters](omapi_host_module.md#parameters)
- [Attributes](omapi_host_module.md#attributes)
- [Examples](omapi_host_module.md#examples)
- [Return Values](omapi_host_module.md#return-values)

## [Synopsis](omapi_host_module.md#id1)

- Manage OMAPI hosts into compatible DHCPd servers

Aliases: net_tools.omapi_host

## [Requirements](omapi_host_module.md#id2)

The below requirements are needed on the host that executes this module.

- pypureomapi

## [Parameters](omapi_host_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ddns**  boolean | Enable dynamic DNS updates for this host.  **Choices:**   - `false` ← (default) - `true` |
| **host**  string | Sets OMAPI server host to interact with.  **Default:** `"localhost"` |
| **hostname**  aliases: name  string | Sets the host lease hostname (mandatory if state=present). |
| **ip**  string | Sets the lease host IP address. |
| **key**  string / required | Sets the TSIG key content for authenticating against OMAPI server. |
| **key_name**  string / required | Sets the TSIG key name for authenticating against OMAPI server. |
| **macaddr**  string / required | Sets the lease host MAC address. |
| **port**  integer | Sets the OMAPI server port to interact with.  **Default:** `7911` |
| **state**  string / required | Create or remove OMAPI host.  **Choices:**   - `"absent"` - `"present"` |
| **statements**  list / elements=string | Attach a list of OMAPI DHCP statements with host lease (without ending semicolon).  **Default:** `[]` |

## [Attributes](omapi_host_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](omapi_host_module.md#id5)

```yaml+jinja
- name: Add a host using OMAPI
  community.general.omapi_host:
    key_name: defomapi
    key: +bFQtBCta6j2vWkjPkNFtgA==
    host: 10.98.4.55
    macaddr: 44:dd:ab:dd:11:44
    name: server01
    ip: 192.168.88.99
    ddns: true
    statements:
    - filename "pxelinux.0"
    - next-server 1.1.1.1
    state: present

- name: Remove a host using OMAPI
  community.general.omapi_host:
    key_name: defomapi
    key: +bFQtBCta6j2vWkjPkNFtgA==
    host: 10.1.1.1
    macaddr: 00:66:ab:dd:11:44
    state: absent
```

## [Return Values](omapi_host_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **lease**  complex | dictionary containing host information  **Returned:** success |
| **hardware-address**  string | MAC address  **Returned:** success  **Sample:** `"00:11:22:33:44:55"` |
| **hardware-type**  integer | hardware type, generally ‘1’  **Returned:** success  **Sample:** `1` |
| **ip-address**  string | IP address, if there is.  **Returned:** success  **Sample:** `"192.168.1.5"` |
| **name**  string | hostname  **Returned:** success  **Sample:** `"mydesktop"` |

### Authors

- Loic Blot (@nerzhul)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
