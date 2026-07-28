---
collection: ansible
version: "8"
title: "community.fortios.fmgr_script module – Add/Edit/Delete and execute scripts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/fortios/fmgr_script_module.html
fetched_at: 2026-07-28T01:44:17+00:00
---
# community.fortios.fmgr_script module – Add/Edit/Delete and execute scripts

> **Note:**
>
> This module is part of the [community.fortios collection](https://galaxy.ansible.com/ui/repo/published/community/fortios/) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.fortios`.
>
> To use it in a playbook, specify: `community.fortios.fmgr_script`.

- [Synopsis](fmgr_script_module.md#synopsis)
- [Parameters](fmgr_script_module.md#parameters)
- [Notes](fmgr_script_module.md#notes)
- [Examples](fmgr_script_module.md#examples)
- [Return Values](fmgr_script_module.md#return-values)

## [Synopsis](fmgr_script_module.md#id1)

- Create/edit/delete scripts and execute the scripts on the FortiManager using jsonrpc API

## [Parameters](fmgr_script_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | The administrative domain (admon) the configuration belongs to |
| **mode**  string | The desired mode of the specified object. Execute will run the script.  **Choices:**   - `"add"` ← (default) - `"delete"` - `"execute"` - `"set"` |
| **script_content**  string | The script content that will be executed. |
| **script_description**  string | The description of the script. |
| **script_name**  string / required | The name of the script. |
| **script_package**  string | (datasource) Policy package object to run the script against |
| **script_scope**  string | (datasource) The devices that the script will run on, can have both device member and device group member. |
| **script_target**  string | The target of the script to be run. |
| **script_type**  string | The type of script (CLI or TCL). |
| **vdom**  string | The virtual domain (vdom) the configuration belongs to |

## [Notes](fmgr_script_module.md#id3)

> **Note:**
>
> - Full Documentation at <https://ftnt-ansible-docs.readthedocs.io/en/latest/>.

## [Examples](fmgr_script_module.md#id4)

```yaml+jinja
- name: CREATE SCRIPT
  community.fortios.fmgr_script:
    adom: "root"
    script_name: "TestScript"
    script_type: "cli"
    script_target: "remote_device"
    script_description: "Create by Ansible"
    script_content: "get system status"

- name: EXECUTE SCRIPT
  community.fortios.fmgr_script:
    adom: "root"
    script_name: "TestScript"
    mode: "execute"
    script_scope: "FGT1,FGT2"

- name: DELETE SCRIPT
  community.fortios.fmgr_script:
    adom: "root"
    script_name: "TestScript"
    mode: "delete"
```

## [Return Values](fmgr_script_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  **Returned:** always |

### Authors

- Andrew Welsh (@Ghilli3)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.fortios)
