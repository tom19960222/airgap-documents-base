---
collection: ansible
version: "8"
title: "netapp.elementsw.na_elementsw_info module – NetApp Element Software Info"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/elementsw/na_elementsw_info_module.html
fetched_at: 2026-07-28T02:41:24+00:00
---
# netapp.elementsw.na_elementsw_info module – NetApp Element Software Info

> **Note:**
>
> This module is part of the [netapp.elementsw collection](https://galaxy.ansible.com/ui/repo/published/netapp/elementsw/) (version 21.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.elementsw`.
> You need further requirements to be able to use this module,
> see [Requirements](na_elementsw_info_module.md#ansible-collections-netapp-elementsw-na-elementsw-info-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.elementsw.na_elementsw_info`.

New in netapp.elementsw 20.10.0

- [Synopsis](na_elementsw_info_module.md#synopsis)
- [Requirements](na_elementsw_info_module.md#requirements)
- [Parameters](na_elementsw_info_module.md#parameters)
- [Notes](na_elementsw_info_module.md#notes)
- [Examples](na_elementsw_info_module.md#examples)
- [Return Values](na_elementsw_info_module.md#return-values)

## [Synopsis](na_elementsw_info_module.md#id1)

- Collect cluster and node information.
- Use a MVIP as hostname for cluster and node scope.
- Use a MIP as hostname for node scope.
- When using MIPs, cluster APIs are expected to fail with ‘xUnknownAPIMethod method=ListAccounts’

## [Requirements](na_elementsw_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- The modules were developed with SolidFire 10.1
- solidfire-sdk-python (1.1.0.92) or greater. Install using ‘pip install solidfire-sdk-python’

## [Parameters](na_elementsw_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **fail_on_error**  boolean | by default, errors are not fatal when collecting a subset. The subset will show on error in the info output.  if set to True, the module fails on the first error.  **Choices:**   - `false` ← (default) - `true` |
| **fail_on_key_not_found**  boolean | force an error when filter is used and a key is not present in records.  **Choices:**   - `false` - `true` ← (default) |
| **fail_on_record_not_found**  boolean | force an error when filter is used and no record is matched.  **Choices:**   - `false` ← (default) - `true` |
| **filter**  dictionary | When a list of records is returned, this can be used to limit the records to be returned.  If more than one key is used, all keys must match. |
| **gather_subsets**  aliases: gather_subset  list / elements=string | list of subsets to gather from target cluster or node  supported values  node_config, cluster_accounts, cluster_nodes, cluster_drives.  additional values  all - for all subsets,  all_clusters - all subsets at cluster scope,  all_nodes - all subsets at node scope  **Default:** `["all"]` |
| **hostname**  string / required | The hostname or IP address of the SolidFire cluster.  For na_elementsw_cluster, the Management IP (MIP) or hostname of the node to initiate the cluster creation from. |
| **password**  aliases: pass  string / required | Password for the specified user. |
| **username**  aliases: user  string / required | Please ensure that the user has the adequate permissions. For more information, please read the official documentation <https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US>. |

## [Notes](na_elementsw_info_module.md#id4)

> **Note:**
>
> - The modules prefixed with na\\_elementsw are built to support the SolidFire storage platform.

## [Examples](na_elementsw_info_module.md#id5)

```yaml+jinja
- name: get all available subsets
  na_elementsw_info:
    hostname: "{{ elementsw_mvip }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    gather_subsets: all
  register: result

- name: collect data for elementsw accounts using a filter
  na_elementsw_info:
    hostname: "{{ elementsw_mvip }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    gather_subsets: 'cluster_accounts'
    filter:
      username: "{{ username_to_find }}"
  register: result
```

## [Return Values](na_elementsw_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **debug**  list / elements=string | a list of detailed error messages if some subsets cannot be collected  **Returned:** success |
| **info**  dictionary | a dictionary of collected subsets  each subset if in JSON format  **Returned:** success |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.elementsw/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.elementsw)
