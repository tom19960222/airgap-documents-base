---
collection: ansible
version: "6"
title: "community.fortios.fmgr_provisioning module – Provision devices via FortiMananger"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/fortios/fmgr_provisioning_module.html
fetched_at: 2026-07-27T17:07:45+00:00
---
# community.fortios.fmgr_provisioning module – Provision devices via FortiMananger

> **Note:**
>
> This module is part of the [community.fortios collection](https://galaxy.ansible.com/community/fortios) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.fortios`.
>
> To use it in a playbook, specify: `community.fortios.fmgr_provisioning`.

- [Synopsis](fmgr_provisioning_module.md#synopsis)
- [Parameters](fmgr_provisioning_module.md#parameters)
- [Examples](fmgr_provisioning_module.md#examples)
- [Return Values](fmgr_provisioning_module.md#return-values)

## [Synopsis](fmgr_provisioning_module.md#id1)

- Add model devices on the FortiManager using jsonrpc API and have them pre-configured, so when central management is configured, the configuration is pushed down to the registering devices

## [Parameters](fmgr_provisioning_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | The administrative domain (admon) the configuration belongs to |
| **description**  string | Description of the device to be provisioned. |
| **group**  string | The name of the device group the provisioned device can belong to. |
| **host**  string / required | The FortiManager’s Address. |
| **minor_release**  string | The minor release number such as 6.X.1, as X being the minor release. |
| **name**  string / required | The name of the device to be provisioned. |
| **os_type**  string / required | The Fortinet OS type to be pushed to the device, such as ‘FOS’ for FortiOS. |
| **os_version**  string / required | The Fortinet OS version to be used for the device, such as 5.0 or 6.0. |
| **password**  string | The password associated with the username account. |
| **patch_release**  string | The patch release number such as 6.0.X, as X being the patch release. |
| **platform**  string / required | The platform of the device, such as model number or VM. |
| **policy_package**  string / required | The name of the policy package to be assigned to the device. |
| **serial**  string / required | The serial number of the device that will be provisioned. |
| **username**  string / required | The username to log into the FortiManager |
| **vdom**  string | The virtual domain (vdom) the configuration belongs to |

## [Examples](fmgr_provisioning_module.md#id3)

```yaml+jinja
- name: Create FGT1 Model Device
  community.fortios.fmgr_provisioning:
    host: "{{ inventory_hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    adom: "root"
    vdom: "root"
    policy_package: "default"
    name: "FGT1"
    group: "Ansible"
    serial: "FGVM000000117994"
    platform: "FortiGate-VM64"
    description: "Provisioned by Ansible"
    os_version: '6.0'
    minor_release: 0
    patch_release: 0
    os_type: 'fos'

- name: Create FGT2 Model Device
  community.fortios.fmgr_provisioning:
    host: "{{ inventory_hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    adom: "root"
    vdom: "root"
    policy_package: "test_pp"
    name: "FGT2"
    group: "Ansible"
    serial: "FGVM000000117992"
    platform: "FortiGate-VM64"
    description: "Provisioned by Ansible"
    os_version: '5.0'
    minor_release: 6
    patch_release: 0
    os_type: 'fos'
```

## [Return Values](fmgr_provisioning_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  Returned: always |

### Authors

- Andrew Welsh (@Ghilli3)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.fortios)
