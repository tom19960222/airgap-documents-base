---
collection: ansible
version: "6"
title: "community.general.shutdown module – Shut down a machine"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/shutdown_module.html
fetched_at: 2026-07-27T17:13:13+00:00
---
# community.general.shutdown module – Shut down a machine

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.shutdown`.

New in community.general 1.1.0

- [Synopsis](shutdown_module.md#synopsis)
- [Parameters](shutdown_module.md#parameters)
- [Notes](shutdown_module.md#notes)
- [See Also](shutdown_module.md#see-also)
- [Examples](shutdown_module.md#examples)
- [Return Values](shutdown_module.md#return-values)

## [Synopsis](shutdown_module.md#id1)

- Shut downs a machine.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](shutdown_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **delay**  integer | Seconds to wait before shutdown. Passed as a parameter to the shutdown command.  On Linux, macOS and OpenBSD, this is converted to minutes and rounded down. If less than 60, it will be set to 0.  On Solaris and FreeBSD, this will be seconds.  Default: `0` |
| **msg**  string | Message to display to users before shutdown.  Default: `"Shut down initiated by Ansible"` |
| **search_paths**  list / elements=path | Paths to search on the remote machine for the `shutdown` command.  *Only* these paths will be searched for the `shutdown` command. `PATH` is ignored in the remote node when searching for the `shutdown` command.  Default: `["/sbin", "/usr/sbin", "/usr/local/sbin"]` |

## [Notes](shutdown_module.md#id3)

> **Note:**
>
> - `PATH` is ignored on the remote node when searching for the `shutdown` command. Use *search_paths* to specify locations to search if the default paths do not work.

## [See Also](shutdown_module.md#id4)

> **See also:**
>
> [ansible.builtin.reboot](../../ansible/builtin/reboot_module.md#ansible-collections-ansible-builtin-reboot-module)
> :   Reboot a machine.

## [Examples](shutdown_module.md#id5)

```yaml+jinja
- name: Unconditionally shut down the machine with all defaults
  community.general.shutdown:

- name: Delay shutting down the remote node
  community.general.shutdown:
    delay: 60

- name: Shut down a machine with shutdown command in unusual place
  community.general.shutdown:
    search_paths:
     - '/lib/molly-guard'
```

## [Return Values](shutdown_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **shutdown**  boolean | `true` if the machine has been shut down.  Returned: always  Sample: `true` |

### Authors

- Matt Davis (@nitzmahone)
- Sam Doran (@samdoran)
- Amin Vakil (@aminvakil)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
