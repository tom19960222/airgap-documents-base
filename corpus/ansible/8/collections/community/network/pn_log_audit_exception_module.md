---
collection: ansible
version: "8"
title: "community.network.pn_log_audit_exception module – CLI command to create/delete an audit exception"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/pn_log_audit_exception_module.html
fetched_at: 2026-07-28T01:57:30+00:00
---
# community.network.pn_log_audit_exception module – CLI command to create/delete an audit exception

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.pn_log_audit_exception`.

- [Synopsis](pn_log_audit_exception_module.md#synopsis)
- [Parameters](pn_log_audit_exception_module.md#parameters)
- [Examples](pn_log_audit_exception_module.md#examples)
- [Return Values](pn_log_audit_exception_module.md#return-values)

## [Synopsis](pn_log_audit_exception_module.md#id1)

- This module can be used to create an audit exception and delete an audit exception.

Aliases: network.netvisor.pn_log_audit_exception

## [Parameters](pn_log_audit_exception_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_access**  string / required | Specify the access type to match exceptions.  **Choices:**   - `"any"` - `"read-only"` - `"read-write"` |
| **pn_audit_type**  string | Specify the type of audit exception.  **Choices:**   - `"cli"` - `"shell"` - `"vtysh"` |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_pattern**  string | Specify a regular expression to match exceptions. |
| **pn_scope**  string | scope - local or fabric.  **Choices:**   - `"local"` - `"fabric"` |
| **state**  string | State the action to perform. Use ‘present’ to create audit-exception and ‘absent’ to delete audit-exception.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Examples](pn_log_audit_exception_module.md#id3)

```yaml+jinja
- name: Create a log-audit-exception
  community.network.pn_log_audit_exception:
    pn_audit_type: "cli"
    pn_pattern: "test"
    state: "present"
    pn_access: "any"
    pn_scope: "local"

- name: Delete a log-audit-exception
  community.network.pn_log_audit_exception:
    pn_audit_type: "shell"
    pn_pattern: "test"
    state: "absent"
    pn_access: "any"
```

## [Return Values](pn_log_audit_exception_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  **Returned:** always |
| **command**  string | the CLI command run on the target node.  **Returned:** always |
| **stderr**  list / elements=string | set of error responses from the log_audit_exceptions command.  **Returned:** on error |
| **stdout**  list / elements=string | set of responses from the pn_log_audit_exceptions command.  **Returned:** always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
