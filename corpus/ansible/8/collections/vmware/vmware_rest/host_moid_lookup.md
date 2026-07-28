---
collection: ansible
version: "8"
title: "vmware.vmware_rest.host_moid lookup – Look up MoID for vSphere host objects using vCenter REST API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vmware/vmware_rest/host_moid_lookup.html
fetched_at: 2026-07-28T02:58:42+00:00
---
# vmware.vmware_rest.host_moid lookup – Look up MoID for vSphere host objects using vCenter REST API

> **Note:**
>
> This lookup plugin is part of the [vmware.vmware_rest collection](https://galaxy.ansible.com/ui/repo/published/vmware/vmware_rest/) (version 2.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vmware.vmware_rest`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](host_moid_lookup.md#ansible-collections-vmware-vmware-rest-host-moid-lookup-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.host_moid`.

New in vmware.vmware_rest 2.1.0

- [Synopsis](host_moid_lookup.md#synopsis)
- [Requirements](host_moid_lookup.md#requirements)
- [Terms](host_moid_lookup.md#terms)
- [Keyword parameters](host_moid_lookup.md#keyword-parameters)
- [Notes](host_moid_lookup.md#notes)
- [Examples](host_moid_lookup.md#examples)
- [Return Value](host_moid_lookup.md#return-value)

## [Synopsis](host_moid_lookup.md#id1)

- Returns Managed Object Reference (MoID) of the vSphere host object contained in the specified path.

## [Requirements](host_moid_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Terms](host_moid_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | Path to query. |

## [Keyword parameters](host_moid_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('vmware.vmware_rest.host_moid', key1=value1, key2=value2, ...)` and `query('vmware.vmware_rest.host_moid', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](host_moid_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('vmware.vmware_rest.host_moid', term1, term2, key1=value1, key2=value2)` and `query('vmware.vmware_rest.host_moid', term1, term2, key1=value1, key2=value2)`

## [Examples](host_moid_lookup.md#id6)

```yaml+jinja
# lookup sample
- name: set connection info
  ansible.builtin.set_fact:
    connection_args:
        vcenter_hostname: "vcenter.test"
        vcenter_username: "administrator@vsphere.local"
        vcenter_password: "1234"

- name: lookup MoID of the object
  ansible.builtin.debug: msg="{{ lookup('vmware.vmware_rest.host_moid', '/my_dc/host/my_cluster/esxi1.test', **connection_args) }}"

- name: lookup MoID of the object inside the path
  ansible.builtin.debug: msg="{{ lookup('vmware.vmware_rest.host_moid', '/my_dc/host/my_cluster/') }}"
```

## [Return Value](host_moid_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  string | MoID of the vSphere host object  **Returned:** success  **Sample:** `"host-1014"` |

### Authors

- Alina Buzachis (@alinabuzachis)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
- [Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
