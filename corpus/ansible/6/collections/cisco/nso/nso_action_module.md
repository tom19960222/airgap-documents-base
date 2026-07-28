---
collection: ansible
version: "6"
title: "cisco.nso.nso_action module – Executes Cisco NSO actions and verifies output."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nso/nso_action_module.html
fetched_at: 2026-07-27T17:01:29+00:00
---
# cisco.nso.nso_action module – Executes Cisco NSO actions and verifies output.

> **Note:**
>
> This module is part of the [cisco.nso collection](https://galaxy.ansible.com/cisco/nso) (version 1.0.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nso`.
> You need further requirements to be able to use this module,
> see [Requirements](nso_action_module.md#ansible-collections-cisco-nso-nso-action-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.nso.nso_action`.

- [Synopsis](nso_action_module.md#synopsis)
- [Requirements](nso_action_module.md#requirements)
- [Parameters](nso_action_module.md#parameters)
- [See Also](nso_action_module.md#see-also)
- [Examples](nso_action_module.md#examples)
- [Return Values](nso_action_module.md#return-values)

## [Synopsis](nso_action_module.md#id1)

- This module provides support for executing Cisco NSO actions and then verifying that the output is as expected.

## [Requirements](nso_action_module.md#id2)

The below requirements are needed on the host that executes this module.

- Cisco NSO version 3.4 or higher.

## [Parameters](nso_action_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **input**  dictionary | NSO action parameters. |
| **output_invalid**  dictionary | List of result parameter names that will cause the task to fail if they are present. |
| **output_required**  dictionary | Required output parameters. |
| **password**  string / required | NSO password |
| **path**  string / required | Path to NSO action. |
| **timeout**  integer | JSON-RPC request timeout in seconds  Default: `300` |
| **url**  string / required | NSO JSON-RPC URL, <http://localhost:8080/jsonrpc> |
| **username**  string / required | NSO username |
| **validate_certs**  boolean | When set to true, validates the SSL certificate of NSO when using SSL  Choices:   - `false` ← (default) - `true` |
| **validate_strict**  boolean | If set to true, the task will fail if any output parameters not in output_required is present in the output.  Choices:   - `false` ← (default) - `true` |

## [See Also](nso_action_module.md#id4)

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

## [Examples](nso_action_module.md#id5)

```yaml+jinja
- name: Sync NSO device
  cisco.nso.nso_action:
    url: https://10.10.20.49/jsonrpc
    username: developer
    password: C1sco12345
    path: /ncs:devices/device{dist-rtr01}/sync-from
    input: {}

- name: Check device sync
  cisco.nso.nso_action:
    url: https://10.10.20.49/jsonrpc
    username: developer
    password: C1sco12345
    path: /ncs:devices/check-sync
    input: {}

- name: Load Native Config
  cisco.nso.nso_action:
    url: "https://10.10.20.49/jsonrpc"
    username: developer
    password: C1sco12345
    path: /ncs:devices/ncs:device{dist-rtr01}/load-native-config
    input: { file: "/home/developer/test.cfg" , verbose: true, mode: "merge"}
  register: result
```

## [Return Values](nso_action_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **output**  dictionary | Action output  Returned: success  Sample: `{"result": true}` |

### Authors

- Claes Nästén (@cnasten)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-nso/issues)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-nso)
