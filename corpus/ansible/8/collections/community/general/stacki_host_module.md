---
collection: ansible
version: "8"
title: "community.general.stacki_host module – Add or remove host to stacki front-end"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/stacki_host_module.html
fetched_at: 2026-07-28T01:50:47+00:00
---
# community.general.stacki_host module – Add or remove host to stacki front-end

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.stacki_host`.

- [Synopsis](stacki_host_module.md#synopsis)
- [Parameters](stacki_host_module.md#parameters)
- [Attributes](stacki_host_module.md#attributes)
- [Examples](stacki_host_module.md#examples)
- [Return Values](stacki_host_module.md#return-values)

## [Synopsis](stacki_host_module.md#id1)

- Use this module to add or remove hosts to a stacki front-end via API.
- Information on stacki can be found at <https://github.com/StackIQ/stacki>.

Aliases: remote_management.stacki.stacki_host

## [Parameters](stacki_host_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **appliance**  string | Appliance to be used in host creation.  Required if `state=present` and host does not yet exist.  **Default:** `"backend"` |
| **force_install**  boolean | Set value to `true` to force node into install state if it already exists in stacki.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | Name of the host to be added to Stacki. |
| **network**  string | Network to be configured in the host.  Currently not used by the module.  **Default:** `"private"` |
| **prim_intf**  string | Name of the primary network interface.  Currently not used by the module. |
| **prim_intf_ip**  string | IP Address for the primary network interface.  Currently not used by the module. |
| **prim_intf_mac**  string | MAC Address for the primary PXE boot network interface.  Currently not used by the module. |
| **rack**  integer | Rack to be used in host creation.  Required if `state=present` and host does not yet exist.  **Default:** `0` |
| **rank**  integer | Rank to be used in host creation.  In Stacki terminology, the rank is the position of the machine in a rack.  Required if `state=present` and host does not yet exist.  **Default:** `0` |
| **stacki_endpoint**  string / required | URL for the Stacki API Endpoint. |
| **stacki_password**  string / required | Password for authenticating with Stacki API, but if not specified, the environment variable `stacki_password` is used instead. |
| **stacki_user**  string / required | Username for authenticating with Stacki API, but if not specified, the environment variable `stacki_user` is used instead. |
| **state**  string | Set value to the desired state for the specified host.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Attributes](stacki_host_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](stacki_host_module.md#id4)

```yaml+jinja
- name: Add a host named test-1
  community.general.stacki_host:
    name: test-1
    stacki_user: usr
    stacki_password: pwd
    stacki_endpoint: url
    prim_intf_mac: mac_addr
    prim_intf_ip: x.x.x.x
    prim_intf: eth0

- name: Remove a host named test-1
  community.general.stacki_host:
    name: test-1
    stacki_user: usr
    stacki_password: pwd
    stacki_endpoint: url
    state: absent
```

## [Return Values](stacki_host_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | response to whether or not the api call completed successfully  **Returned:** always  **Sample:** `true` |
| **stdout**  list / elements=string | the set of responses from the commands  **Returned:** always  **Sample:** `["...", "..."]` |
| **stdout_lines**  list / elements=string | the value of stdout split into a list  **Returned:** always  **Sample:** `[["...", "..."], ["..."], ["..."]]` |

### Authors

- Hugh Ma (@bbyhuy)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
