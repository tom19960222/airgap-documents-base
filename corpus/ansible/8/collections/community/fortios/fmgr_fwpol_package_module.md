---
collection: ansible
version: "8"
title: "community.fortios.fmgr_fwpol_package module – Manages FortiManager Firewall Policies Packages."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/fortios/fmgr_fwpol_package_module.html
fetched_at: 2026-07-28T01:44:14+00:00
---
# community.fortios.fmgr_fwpol_package module – Manages FortiManager Firewall Policies Packages.

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
> To use it in a playbook, specify: `community.fortios.fmgr_fwpol_package`.

- [Synopsis](fmgr_fwpol_package_module.md#synopsis)
- [Parameters](fmgr_fwpol_package_module.md#parameters)
- [Notes](fmgr_fwpol_package_module.md#notes)
- [Examples](fmgr_fwpol_package_module.md#examples)
- [Return Values](fmgr_fwpol_package_module.md#return-values)

## [Synopsis](fmgr_fwpol_package_module.md#id1)

- Manages FortiManager Firewall Policies Packages. Policy Packages contain one or more Firewall Policies/Rules and are distritbuted via FortiManager to Fortigates.
- This module controls the creation/edit/delete/assign of these packages.

## [Parameters](fmgr_fwpol_package_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string | The ADOM the configuration should belong to.  **Default:** `"root"` |
| **central_nat**  string | Central NAT setting.  **Choices:**   - `"enable"` - `"disable"` ← (default) |
| **fwpolicy6_implicit_log**  string | Implicit Log setting for all IPv6 policies in package.  **Choices:**   - `"enable"` - `"disable"` ← (default) |
| **fwpolicy_implicit_log**  string | Implicit Log setting for all IPv4 policies in package.  **Choices:**   - `"enable"` - `"disable"` ← (default) |
| **inspection_mode**  string | Inspection mode setting for the policies flow or proxy.  **Choices:**   - `"flow"` ← (default) - `"proxy"` |
| **mode**  string | Sets one of three modes for managing the object.  **Choices:**   - `"add"` ← (default) - `"set"` - `"delete"` |
| **name**  string / required | Name of the FortiManager package or folder. |
| **ngfw_mode**  string | NGFW mode setting for the policies flow or proxy.  **Choices:**   - `"profile-based"` ← (default) - `"policy-based"` |
| **object_type**  string / required | Are we managing packages or folders, or installing packages?  **Choices:**   - `"pkg"` - `"folder"` - `"install"` |
| **package_folder**  string | Name of the folder you want to put the package into. |
| **parent_folder**  string | The parent folder name you want to add this object under. |
| **scope_members**  string | The devices or scope that you want to assign this policy package to. |
| **scope_members_vdom**  string | The members VDOM you want to assign the package to.  **Default:** `"root"` |
| **ssl_ssh_profile**  string | if policy-based ngfw-mode, refer to firewall ssl-ssh-profile. |

## [Notes](fmgr_fwpol_package_module.md#id3)

> **Note:**
>
> - Full Documentation at <https://ftnt-ansible-docs.readthedocs.io/en/latest/>.

## [Examples](fmgr_fwpol_package_module.md#id4)

```yaml+jinja
- name: CREATE BASIC POLICY PACKAGE
  community.fortios.fmgr_fwpol_package:
    adom: "ansible"
    mode: "add"
    name: "testPackage"
    object_type: "pkg"

- name: ADD PACKAGE WITH TARGETS
  community.fortios.fmgr_fwpol_package:
    mode: "add"
    adom: "ansible"
    name: "ansibleTestPackage1"
    object_type: "pkg"
    inspection_mode: "flow"
    ngfw_mode: "profile-based"
    scope_members: "seattle-fgt02, seattle-fgt03"

- name: ADD FOLDER
  community.fortios.fmgr_fwpol_package:
    mode: "add"
    adom: "ansible"
    name: "ansibleTestFolder1"
    object_type: "folder"

- name: ADD PACKAGE INTO PARENT FOLDER
  community.fortios.fmgr_fwpol_package:
    mode: "set"
    adom: "ansible"
    name: "ansibleTestPackage2"
    object_type: "pkg"
    parent_folder: "ansibleTestFolder1"

- name: ADD FOLDER INTO PARENT FOLDER
  community.fortios.fmgr_fwpol_package:
    mode: "set"
    adom: "ansible"
    name: "ansibleTestFolder2"
    object_type: "folder"
    parent_folder: "ansibleTestFolder1"

- name: INSTALL PACKAGE
  community.fortios.fmgr_fwpol_package:
    mode: "set"
    adom: "ansible"
    name: "ansibleTestPackage1"
    object_type: "install"
    scope_members: "seattle-fgt03, seattle-fgt02"

- name: REMOVE PACKAGE
  community.fortios.fmgr_fwpol_package:
    mode: "delete"
    adom: "ansible"
    name: "ansibleTestPackage1"
    object_type: "pkg"

- name: REMOVE NESTED PACKAGE
  community.fortios.fmgr_fwpol_package:
    mode: "delete"
    adom: "ansible"
    name: "ansibleTestPackage2"
    object_type: "pkg"
    parent_folder: "ansibleTestFolder1"

- name: REMOVE NESTED FOLDER
  community.fortios.fmgr_fwpol_package:
    mode: "delete"
    adom: "ansible"
    name: "ansibleTestFolder2"
    object_type: "folder"
    parent_folder: "ansibleTestFolder1"

- name: REMOVE FOLDER
  community.fortios.fmgr_fwpol_package:
    mode: "delete"
    adom: "ansible"
    name: "ansibleTestFolder1"
    object_type: "folder"
```

## [Return Values](fmgr_fwpol_package_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  **Returned:** always |

### Authors

- Luke Weighall (@lweighall)
- Andrew Welsh (@Ghilli3)
- Jim Huber (@p4r4n0y1ng)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.fortios)
