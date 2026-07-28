---
collection: ansible
version: "8"
title: "cisco.ise.personas_update_roles_services module – Update the roles and services of a node"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/personas_update_roles_services_module.html
fetched_at: 2026-07-28T01:30:03+00:00
---
# cisco.ise.personas_update_roles_services module – Update the roles and services of a node

> **Note:**
>
> This module is part of the [cisco.ise collection](https://galaxy.ansible.com/ui/repo/published/cisco/ise/) (version 2.6.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ise`.
> You need further requirements to be able to use this module,
> see [Requirements](personas_update_roles_services_module.md#ansible-collections-cisco-ise-personas-update-roles-services-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.personas_update_roles_services`.

New in cisco.ise 2.4.0

- [Synopsis](personas_update_roles_services_module.md#synopsis)
- [Requirements](personas_update_roles_services_module.md#requirements)
- [Parameters](personas_update_roles_services_module.md#parameters)
- [Notes](personas_update_roles_services_module.md#notes)
- [See Also](personas_update_roles_services_module.md#see-also)
- [Examples](personas_update_roles_services_module.md#examples)
- [Return Values](personas_update_roles_services_module.md#return-values)

## [Synopsis](personas_update_roles_services_module.md#id1)

- Update the roles and services of a node

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](personas_update_roles_services_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests >= 2.25.1
- python >= 3.5

## [Parameters](personas_update_roles_services_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostname**  string | The hostname of the node. |
| **ip**  string | The IP address of the node to be updated. |
| **ise_verify**  boolean | Whether or not to verify the identity of the node.  **Choices:**   - `false` - `true` |
| **ise_version**  string | The version of the ISE node. |
| **ise_wait_on_rate_limit**  boolean | Whether or not to wait on rate limit  **Choices:**   - `false` - `true` |
| **password**  string | The password to log into the node. |
| **roles**  list / elements=string | The roles to be fulfilled by this node. Possible roles are PrimaryAdmin, SecondaryAdmin, PrimaryMonitoring, SecondaryMonitoring, PrimaryDedicatedMonitoring, SecondaryDedicatedMonitoring, Standalone |
| **services**  list / elements=string | The services this node will run. Possible services are Session, Profiler, TC-NAC, SXP, DeviceAdmin, PassiveIdentity, pxGrid, pxGridCloud |
| **username**  string | The username to log into the node. |

## [Notes](personas_update_roles_services_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`

## [See Also](personas_update_roles_services_module.md#id5)

> **See also:**
>
> cisco.ise.plugins.modules.personas_update_roles_services
> :   The official documentation on the **cisco.ise.plugins.modules.personas_update_roles_services** module.

## [Examples](personas_update_roles_services_module.md#id6)

```yaml+jinja
- name: Remove the Primary Monitoring role and the Session and Profiler services from the primary node
  cisco.ise.personas_update_roles_services:
    ip: 10.1.1.1
    username: admin
    password: C1sco123
    hostname: ise-pan-server-1
    roles:
      - PrimaryAdmin
    services: []
```

## [Return Values](personas_update_roles_services_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  string | A string stating that the node was successfully updated  **Returned:** always  **Sample:** `"Node ise-pan-server-1 updated successfully"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
