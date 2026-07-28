---
collection: ansible
version: "8"
title: "cisco.nso.nso_show module – Displays data from Cisco NSO."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nso/nso_show_module.html
fetched_at: 2026-07-28T01:38:24+00:00
---
# cisco.nso.nso_show module – Displays data from Cisco NSO.

> **Note:**
>
> This module is part of the [cisco.nso collection](https://galaxy.ansible.com/ui/repo/published/cisco/nso/) (version 1.0.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nso`.
> You need further requirements to be able to use this module,
> see [Requirements](nso_show_module.md#ansible-collections-cisco-nso-nso-show-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.nso.nso_show`.

- [Synopsis](nso_show_module.md#synopsis)
- [Requirements](nso_show_module.md#requirements)
- [Parameters](nso_show_module.md#parameters)
- [See Also](nso_show_module.md#see-also)
- [Examples](nso_show_module.md#examples)
- [Return Values](nso_show_module.md#return-values)

## [Synopsis](nso_show_module.md#id1)

- This module provides support for displaying data from Cisco NSO.

## [Requirements](nso_show_module.md#id2)

The below requirements are needed on the host that executes this module.

- Cisco NSO version 3.4.12 or higher, 4.1.9 or higher, 4.2.6 or higher, 4.3.7 or higher, 4.4.5 or higher, 4.5 or higher.

## [Parameters](nso_show_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **operational**  boolean | Controls whether or not operational data is included in the result.  **Choices:**   - `false` ← (default) - `true` |
| **password**  string / required | NSO password |
| **path**  string / required | Path to NSO data. |
| **timeout**  integer | JSON-RPC request timeout in seconds  **Default:** `300` |
| **url**  string / required | NSO JSON-RPC URL, <http://localhost:8080/jsonrpc> |
| **username**  string / required | NSO username |
| **validate_certs**  boolean | When set to true, validates the SSL certificate of NSO when using SSL  **Choices:**   - `false` ← (default) - `true` |

## [See Also](nso_show_module.md#id4)

> **See also:**
>
> [Cisco DevNet NSO Sandbox](https://blogs.cisco.com/developer/nso-learning-lab-and-sandbox)
> :   Provides a reservable pod with NSO, virtual network topology simulated with Cisco CML and a Linux host running Ansible
>
> [NSO Developer Resources on DevNet](https://developer.cisco.com/docs/nso/)
> :   Documentation for getting started using NSO
>
> [NSO Developer Hub](https://community.cisco.com/t5/nso-developer-hub/ct-p/5672j-dev-nso)
> :   Collaboration community portal for NSO developers
>
> [NSO Developer Github](https://github.com/NSO-developer/)
> :   Code for NSO on Github

## [Examples](nso_show_module.md#id5)

```yaml+jinja
- name: DISPLAY DEVICE INCLUDING OPERATIONAL DATA
  cisco.nso.nso_show:
    url: https://10.10.20.49/jsonrpc
    username: developer
    password: C1sco12345
    path: /ncs:devices/device{dist-rtr01}
    operational: true
  register: result

- name: Display the result
  debug:
    var: result

- name: DISPLAY INTERFACES
  cisco.nso.nso_show:
    url: "https://10.10.20.49/jsonrpc"
    username: developer
    password: C1sco12345
    path: /ncs:devices/device{dist-rtr01}/config/interface
    operational: true
  register: result

- name: Display the result
  debug:
    var: result
```

## [Return Values](nso_show_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **output**  dictionary | Configuration  **Returned:** success |

### Authors

- Claes Nästén (@cnasten)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-nso/issues)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-nso)
