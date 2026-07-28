---
collection: ansible
version: "6"
title: "community.network.pn_cpu_class module – CLI command to create/modify/delete cpu-class"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/pn_cpu_class_module.html
fetched_at: 2026-07-27T17:19:18+00:00
---
# community.network.pn_cpu_class module – CLI command to create/modify/delete cpu-class

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.pn_cpu_class`.

- [Synopsis](pn_cpu_class_module.md#synopsis)
- [Parameters](pn_cpu_class_module.md#parameters)
- [Examples](pn_cpu_class_module.md#examples)
- [Return Values](pn_cpu_class_module.md#return-values)

## [Synopsis](pn_cpu_class_module.md#id1)

- This module can be used to create, modify and delete CPU class information.

## [Parameters](pn_cpu_class_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_hog_protect**  string | enable host-based hog protection.  Choices:   - `"disable"` - `"enable"` - `"enable-and-drop"` |
| **pn_name**  string | name for the CPU class. |
| **pn_rate_limit**  string | rate-limit for CPU class. |
| **pn_scope**  string | scope for CPU class.  Choices:   - `"local"` - `"fabric"` |
| **state**  string / required | State the action to perform. Use `present` to create cpu-class and `absent` to delete cpu-class `update` to modify the cpu-class.  Choices:   - `"present"` - `"absent"` - `"update"` |

## [Examples](pn_cpu_class_module.md#id3)

```yaml+jinja
- name: Create cpu class
  community.network.pn_cpu_class:
    pn_cliswitch: 'sw01'
    state: 'present'
    pn_name: 'icmp'
    pn_rate_limit: '1000'
    pn_scope: 'local'

- name: Delete cpu class
  community.network.pn_cpu_class:
    pn_cliswitch: 'sw01'
    state: 'absent'
    pn_name: 'icmp'

- name: Modify cpu class
  community.network.pn_cpu_class:
    pn_cliswitch: 'sw01'
    state: 'update'
    pn_name: 'icmp'
    pn_rate_limit: '2000'
```

## [Return Values](pn_cpu_class_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  Returned: always |
| **command**  string | the CLI command run on the target node.  Returned: always |
| **stderr**  list / elements=string | set of error responses from the cpu-class command.  Returned: on error |
| **stdout**  list / elements=string | set of responses from the cpu-class command.  Returned: always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
