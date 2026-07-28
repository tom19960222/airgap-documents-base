---
collection: ansible
version: "8"
title: "ansible.builtin.service module – Manage services"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/service_module.html
fetched_at: 2026-07-28T01:07:41+00:00
---
# ansible.builtin.service module – Manage services

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `service` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.service` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](service_module.md#synopsis)
- [Parameters](service_module.md#parameters)
- [Attributes](service_module.md#attributes)
- [Notes](service_module.md#notes)
- [See Also](service_module.md#see-also)
- [Examples](service_module.md#examples)

## [Synopsis](service_module.md#id1)

- Controls services on remote hosts. Supported init systems include BSD init, OpenRC, SysV, Solaris SMF, systemd, upstart.
- This module acts as a proxy to the underlying service manager module. While all arguments will be passed to the underlying module, not all modules support the same arguments. This documentation only covers the minimum intersection of module arguments that all service manager modules support.
- This module is a proxy for multiple more specific service manager modules (such as [ansible.builtin.systemd](systemd_module.md#ansible-collections-ansible-builtin-systemd-module) and [ansible.builtin.sysvinit](sysvinit_module.md#ansible-collections-ansible-builtin-sysvinit-module)). This allows management of a heterogeneous environment of machines without creating a specific task for each service manager. The module to be executed is determined by the *use* option, which defaults to the service manager discovered by [ansible.builtin.setup](setup_module.md#ansible-collections-ansible-builtin-setup-module). If `setup` was not yet run, this module may run it.
- For Windows targets, use the [ansible.windows.win_service](../windows/win_service_module.md#ansible-collections-ansible-windows-win-service-module) module instead.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](service_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **arguments**  aliases: args  string | Additional arguments provided on the command line.  While using remote hosts with systemd this setting will be ignored.  **Default:** `""` |
| **enabled**  boolean | Whether the service should start on boot.  **At least one of state and enabled are required.**  **Choices:**   - `false` - `true` |
| **name**  string / required | Name of the service. |
| **pattern**  string | If the service does not respond to the status command, name a substring to look for as would be found in the output of the *ps* command as a stand-in for a status result.  If the string is found, the service will be assumed to be started.  While using remote hosts with systemd this setting will be ignored. |
| **runlevel**  string | For OpenRC init scripts (e.g. Gentoo) only.  The runlevel that this service belongs to.  While using remote hosts with systemd this setting will be ignored.  **Default:** `"default"` |
| **sleep**  integer | If the service is being `restarted` then sleep this many seconds between the stop and start command.  This helps to work around badly-behaving init scripts that exit immediately after signaling a process to stop.  Not all service managers support sleep, i.e when using systemd this setting will be ignored. |
| **state**  string | `started`/`stopped` are idempotent actions that will not run commands unless necessary.  `restarted` will always bounce the service.  `reloaded` will always reload.  **At least one of state and enabled are required.**  Note that reloaded will start the service if it is not already started, even if your chosen init system wouldn’t normally.  **Choices:**   - `"reloaded"` - `"restarted"` - `"started"` - `"stopped"` |
| **use**  string | The service module actually uses system specific modules, normally through auto detection, this setting can force a specific module.  Normally it uses the value of the ‘ansible_service_mgr’ fact and falls back to the old ‘service’ module when none matching is found.  **Default:** `"auto"` |

## [Attributes](service_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | **Support:** **full** | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | **Support:** **full** | Supports being used with the `async` keyword |
| **bypass_host_loop** | **Support:** **none** | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **check_mode** | **Support:**  N/A  support depends on the underlying plugin invoked | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:**  N/A  support depends on the underlying plugin invoked | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platforms:** **all**  The support depends on the availability for the specific plugin for each platform and if fact gathering is able to detect it | Target OS/families that can be operated against |

## [Notes](service_module.md#id4)

> **Note:**
>
> - For AIX, group subsystem names can be used.

## [See Also](service_module.md#id5)

> **See also:**
>
> [ansible.windows.win_service](../windows/win_service_module.md#ansible-collections-ansible-windows-win-service-module)
> :   Manage and query Windows services.

## [Examples](service_module.md#id6)

```yaml+jinja
- name: Start service httpd, if not started
  ansible.builtin.service:
    name: httpd
    state: started

- name: Stop service httpd, if started
  ansible.builtin.service:
    name: httpd
    state: stopped

- name: Restart service httpd, in all cases
  ansible.builtin.service:
    name: httpd
    state: restarted

- name: Reload service httpd, in all cases
  ansible.builtin.service:
    name: httpd
    state: reloaded

- name: Enable service httpd, and not touch the state
  ansible.builtin.service:
    name: httpd
    enabled: yes

- name: Start service foo, based on running process /usr/bin/foo
  ansible.builtin.service:
    name: foo
    pattern: /usr/bin/foo
    state: started

- name: Restart network service for interface eth0
  ansible.builtin.service:
    name: network
    state: restarted
    args: eth0
```

### Authors

- Ansible Core Team
- Michael DeHaan

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
