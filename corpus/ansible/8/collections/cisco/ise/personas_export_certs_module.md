---
collection: ansible
version: "8"
title: "cisco.ise.personas_export_certs module – Export certificate into primary node"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/personas_export_certs_module.html
fetched_at: 2026-07-28T01:30:01+00:00
---
# cisco.ise.personas_export_certs module – Export certificate into primary node

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
> see [Requirements](personas_export_certs_module.md#ansible-collections-cisco-ise-personas-export-certs-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.personas_export_certs`.

New in cisco.ise 0.0.8

- [Synopsis](personas_export_certs_module.md#synopsis)
- [Requirements](personas_export_certs_module.md#requirements)
- [Parameters](personas_export_certs_module.md#parameters)
- [Notes](personas_export_certs_module.md#notes)
- [See Also](personas_export_certs_module.md#see-also)
- [Examples](personas_export_certs_module.md#examples)
- [Return Values](personas_export_certs_module.md#return-values)

## [Synopsis](personas_export_certs_module.md#id1)

- Export certificate into primary node

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](personas_export_certs_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests >= 2.25.1
- python >= 3.5

## [Parameters](personas_export_certs_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostname**  string | The hostname for the node for which the certificate will be exported. |
| **ip**  string | The IP address of the node for which the certificate will be exported. |
| **ise_verify**  boolean | Whether or not to verify the identity of the node.  **Choices:**   - `false` - `true` |
| **ise_version**  string | The version of the ISE node. |
| **ise_wait_on_rate_limit**  boolean | Whether or not to wait on rate limit  **Choices:**   - `false` - `true` |
| **name**  string | The name of the node for which the certificate will be exported. |
| **password**  string | The password for the node for which the certificate will be exported. |
| **primary_ip**  string | The IP address of the primary node. |
| **primary_password**  string | The password for the primary node. |
| **primary_username**  string | The username for the primary node. |
| **username**  string | The username for the node for which the certificate will be exported. |

## [Notes](personas_export_certs_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`

## [See Also](personas_export_certs_module.md#id5)

> **See also:**
>
> cisco.ise.plugins.modules.personas_export_certs
> :   The official documentation on the **cisco.ise.plugins.modules.personas_export_certs** module.

## [Examples](personas_export_certs_module.md#id6)

```yaml+jinja
- name: Export trusted certificates into primary node
  cisco.ise.personas_export_certs:
    primary_ip: 10.1.1.1
    primary_username: admin
    primary_password: cisco123
    name: "{{ item.name }}"
    ip: "{{ item.ip }}"
    hostname: "{{ item.hostname }}"
    username: admin
    password: cisco123
  loop:
    - name: ISE PAN Server 2
      ip: 10.1.1.2
      hostname: ise-pan-server-2
    - name: ISE PSN Server 1
      ip: 10.1.1.3
      hostname: ise-psn-server-1
    - name: ISE PSN Server 2
      ip: 10.1.1.4
      hostname: ise-psn-server-2
```

## [Return Values](personas_export_certs_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  string | A text string stating that the certificate was exported successfully.  **Returned:** always  **Sample:** `"The certificate for ISE PAN Server 2 was exported successfully to the primary node"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
