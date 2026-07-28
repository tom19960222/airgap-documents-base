---
collection: ansible
version: "8"
title: "ansible.builtin.wait_for_connection module – Waits until remote system is reachable/usable"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/wait_for_connection_module.html
fetched_at: 2026-07-28T01:07:49+00:00
---
# ansible.builtin.wait_for_connection module – Waits until remote system is reachable/usable

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `wait_for_connection` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.wait_for_connection` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](wait_for_connection_module.md#synopsis)
- [Parameters](wait_for_connection_module.md#parameters)
- [Attributes](wait_for_connection_module.md#attributes)
- [See Also](wait_for_connection_module.md#see-also)
- [Examples](wait_for_connection_module.md#examples)
- [Return Values](wait_for_connection_module.md#return-values)

## [Synopsis](wait_for_connection_module.md#id1)

- Waits for a total of `timeout` seconds.
- Retries the transport connection after a timeout of `connect_timeout`.
- Tests the transport connection every `sleep` seconds.
- This module makes use of internal ansible transport (and configuration) and the ping/win_ping module to guarantee correct end-to-end functioning.
- This module is also supported for Windows targets.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](wait_for_connection_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **connect_timeout**  integer | Maximum number of seconds to wait for a connection to happen before closing and retrying.  **Default:** `5` |
| **delay**  integer | Number of seconds to wait before starting to poll.  **Default:** `0` |
| **sleep**  integer | Number of seconds to sleep between checks.  **Default:** `1` |
| **timeout**  integer | Maximum number of seconds to wait for.  **Default:** `600` |

## [Attributes](wait_for_connection_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | **Support:** **full** | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | **Support:** **none** | Supports being used with the `async` keyword |
| **bypass_host_loop** | **Support:** **none** | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **check_mode** | **Support:** **none** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platforms:** **all**  As long as there is a connection plugin | Target OS/families that can be operated against |

## [See Also](wait_for_connection_module.md#id4)

> **See also:**
>
> [ansible.builtin.wait_for](wait_for_module.md#ansible-collections-ansible-builtin-wait-for-module)
> :   Waits for a condition before continuing.
>
> [ansible.windows.win_wait_for](../windows/win_wait_for_module.md#ansible-collections-ansible-windows-win-wait-for-module)
> :   Waits for a condition before continuing.
>
> [community.windows.win_wait_for_process](../../community/windows/win_wait_for_process_module.md#ansible-collections-community-windows-win-wait-for-process-module)
> :   Waits for a process to exist or not exist before continuing.

## [Examples](wait_for_connection_module.md#id5)

```yaml+jinja
- name: Wait 600 seconds for target connection to become reachable/usable
  ansible.builtin.wait_for_connection:

- name: Wait 300 seconds, but only start checking after 60 seconds
  ansible.builtin.wait_for_connection:
    delay: 60
    timeout: 300

# Wake desktops, wait for them to become ready and continue playbook
- hosts: all
  gather_facts: no
  tasks:
  - name: Send magic Wake-On-Lan packet to turn on individual systems
    community.general.wakeonlan:
      mac: '{{ mac }}'
      broadcast: 192.168.0.255
    delegate_to: localhost

  - name: Wait for system to become reachable
    ansible.builtin.wait_for_connection:

  - name: Gather facts for first time
    ansible.builtin.setup:

# Build a new VM, wait for it to become ready and continue playbook
- hosts: all
  gather_facts: no
  tasks:
  - name: Clone new VM, if missing
    community.vmware.vmware_guest:
      hostname: '{{ vcenter_ipaddress }}'
      name: '{{ inventory_hostname_short }}'
      template: Windows 2012R2
      customization:
        hostname: '{{ vm_shortname }}'
        runonce:
        - powershell.exe -ExecutionPolicy Unrestricted -File C:\Windows\Temp\ConfigureRemotingForAnsible.ps1 -ForceNewSSLCert -EnableCredSSP
    delegate_to: localhost

  - name: Wait for system to become reachable over WinRM
    ansible.builtin.wait_for_connection:
      timeout: 900

  - name: Gather facts for first time
    ansible.builtin.setup:
```

## [Return Values](wait_for_connection_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **elapsed**  float | The number of seconds that elapsed waiting for the connection to appear.  **Returned:** always  **Sample:** `23.1` |

### Authors

- Dag Wieers (@dagwieers)

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
