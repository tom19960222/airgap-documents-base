---
collection: ansible
version: "8"
title: "theforeman.foreman.host_power module – Manage Power State of Hosts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/host_power_module.html
fetched_at: 2026-07-28T02:56:03+00:00
---
# theforeman.foreman.host_power module – Manage Power State of Hosts

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/ui/repo/published/theforeman/foreman/) (version 3.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](host_power_module.md#ansible-collections-theforeman-foreman-host-power-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.host_power`.

New in theforeman.foreman 1.0.0

- [Synopsis](host_power_module.md#synopsis)
- [Requirements](host_power_module.md#requirements)
- [Parameters](host_power_module.md#parameters)
- [Attributes](host_power_module.md#attributes)
- [Examples](host_power_module.md#examples)
- [Return Values](host_power_module.md#return-values)

## [Synopsis](host_power_module.md#id1)

- Manage power state of a host
- This beta version can start and stop an existing foreman host and question the current power state.

Aliases: foreman_host_power

## [Requirements](host_power_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](host_power_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **name**  aliases: hostname  string / required | Name (FQDN) of the host |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | Desired power state  **Choices:**   - `"on"` - `"start"` - `"off"` - `"stop"` - `"soft"` - `"reboot"` - `"cycle"` - `"reset"` - `"state"` ← (default) - `"status"` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](host_power_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](host_power_module.md#id5)

```yaml+jinja
- name: "Switch a host on"
  theforeman.foreman.host_power:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    hostname: "test-host.domain.test"
    state: on

- name: "Switch a host off"
  theforeman.foreman.host_power:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    hostname: "test-host.domain.test"
    state: off

- name: "Query host power state"
  theforeman.foreman.host_power:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    hostname: "test-host.domain.test"
    state: state
    register: result
- debug:
    msg: "Host power state is {{ result.power_state }}"
```

## [Return Values](host_power_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **power_state**  string | current power state of host  **Returned:** always  **Sample:** `"off"` |

### Authors

- Bernhard Hopfenmueller (@Fobhep) ATIX AG
- Baptiste Agasse (@bagasse)

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
