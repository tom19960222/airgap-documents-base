---
collection: ansible
version: "8"
title: "community.general.ipmi_power module – Power management for machine"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ipmi_power_module.html
fetched_at: 2026-07-28T01:46:51+00:00
---
# community.general.ipmi_power module – Power management for machine

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
> see [Requirements](ipmi_power_module.md#ansible-collections-community-general-ipmi-power-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ipmi_power`.

- [Synopsis](ipmi_power_module.md#synopsis)
- [Requirements](ipmi_power_module.md#requirements)
- [Parameters](ipmi_power_module.md#parameters)
- [Attributes](ipmi_power_module.md#attributes)
- [Examples](ipmi_power_module.md#examples)
- [Return Values](ipmi_power_module.md#return-values)

## [Synopsis](ipmi_power_module.md#id1)

- Use this module for power management

Aliases: remote_management.ipmi.ipmi_power

## [Requirements](ipmi_power_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- pyghmi

## [Parameters](ipmi_power_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **key**  string  *added in community.general 4.1.0* | Encryption key to connect to the BMC in hex format. |
| **machine**  list / elements=dictionary  *added in community.general 4.3.0* | Provide a list of the remote target address for the bridge IPMI request, and the power status.  Either this option or `state` is required. |
| **state**  string | Whether to ensure that the machine specified by `machine[].targetAddress` in desired state.  If this option is not set, the power state is set by `state`.  If both this option and `state` are set, this option takes precedence over `state`.  **Choices:**   - `"on"` - `"off"` - `"shutdown"` - `"reset"` - `"boot"` |
| **targetAddress**  integer / required | Remote target address for the bridge IPMI request. |
| **name**  string / required | Hostname or ip address of the BMC. |
| **password**  string / required | Password to connect to the BMC. |
| **port**  integer | Remote RMCP port.  **Default:** `623` |
| **state**  string | Whether to ensure that the machine in desired state.  The choices for state are: - on – Request system turn on - off – Request system turn off without waiting for OS to shutdown - shutdown – Have system request OS proper shutdown - reset – Request system reset without waiting for OS - boot – If system is off, then ‘on’, else ‘reset’  Either this option or `machine` is required.  **Choices:**   - `"on"` - `"off"` - `"shutdown"` - `"reset"` - `"boot"` |
| **timeout**  integer | Maximum number of seconds before interrupt request.  **Default:** `300` |
| **user**  string / required | Username to use to connect to the BMC. |

## [Attributes](ipmi_power_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](ipmi_power_module.md#id5)

```yaml+jinja
- name: Ensure machine is powered on
  community.general.ipmi_power:
    name: test.testdomain.com
    user: admin
    password: password
    state: 'on'

- name: Ensure machines of which remote target address is 48 and 50 are powered off
  community.general.ipmi_power:
    name: test.testdomain.com
    user: admin
    password: password
    state: 'off'
    machine:
      - targetAddress: 48
      - targetAddress: 50

- name: Ensure machine of which remote target address is 48 is powered on, and 50 is powered off
  community.general.ipmi_power:
    name: test.testdomain.com
    user: admin
    password: password
    machine:
      - targetAddress: 48
        state: 'on'
      - targetAddress: 50
        state: 'off'
```

## [Return Values](ipmi_power_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **powerstate**  string | The current power state of the machine.  **Returned:** success and `machine` is not provided  **Sample:** `"on"` |
| **status**  list / elements=dictionary  *added in community.general 4.3.0* | The current power state of the machine when the machine option is set.  **Returned:** success and `machine` is provided  **Sample:** `[{"powerstate": "on", "targetAddress": 48}, {"powerstate": "on", "targetAddress": 50}]` |
| **powerstate**  string | The current power state of the machine specified by `status[].targetAddress`.  **Returned:** success |
| **targetAddress**  integer | The remote target address.  **Returned:** success |

### Authors

- Bulat Gaifullin (@bgaifullin)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
