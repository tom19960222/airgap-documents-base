---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_flexcache module – NetApp ONTAP FlexCache - create/delete relationship"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_flexcache_module.html
fetched_at: 2026-07-28T02:42:12+00:00
---
# netapp.ontap.na_ontap_flexcache module – NetApp ONTAP FlexCache - create/delete relationship

> **Note:**
>
> This module is part of the [netapp.ontap collection](https://galaxy.ansible.com/ui/repo/published/netapp/ontap/) (version 22.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.ontap`.
> You need further requirements to be able to use this module,
> see [Requirements](na_ontap_flexcache_module.md#ansible-collections-netapp-ontap-na-ontap-flexcache-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_flexcache`.

New in netapp.ontap 2.8.0

- [Synopsis](na_ontap_flexcache_module.md#synopsis)
- [Requirements](na_ontap_flexcache_module.md#requirements)
- [Parameters](na_ontap_flexcache_module.md#parameters)
- [Notes](na_ontap_flexcache_module.md#notes)
- [Examples](na_ontap_flexcache_module.md#examples)

## [Synopsis](na_ontap_flexcache_module.md#id1)

- Create/Delete FlexCache volume relationships.
- This module does not modify an existing FlexCache volume with two exceptions.
- When using REST, a prepopulate can be started on an exising FlexCache volume.
- When using REST, the volume can be mounted or unmounted. Set path to ‘’ to unmount it.
- It is required the volume is mounted to prepopulate it.
- Some actions are also available through the na_ontap_volume.

## [Requirements](na_ontap_flexcache_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_flexcache_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aggr_list**  aliases: aggregates  list / elements=string | List of aggregates to host target FlexCache volume. |
| **aggr_list_multiplier**  aliases: constituents_per_aggregate  integer | Aggregate list repeat count.  REST - Number of FlexCache constituents per aggregate when the `aggregates` field is mentioned. |
| **auto_provision_as**  string | Use this parameter to automatically select existing aggregates for volume provisioning. Eg flexgroup  Note that the fastest aggregate type with at least one aggregate on each node of the cluster will be selected.  Ignored when using REST - omit aggr_list for automatic selection. |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_offline**  boolean | Offline FlexCache volume before deleting the FlexCache relationship.  The volume will be destroyed and data can be lost.  **Choices:**   - `false` ← (default) - `true` |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **force_unmount**  boolean | Unmount FlexCache volume. Delete the junction path at which the volume is mounted before deleting the FlexCache relationship.  **Choices:**   - `false` ← (default) - `true` |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **junction_path**  aliases: path  string | Junction path of the cache volume. |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **name**  aliases: volume  string / required  *added in netapp.ontap 21.3.0* | Name of the target volume for the FlexCache. |
| **ontapi**  integer | The ontap api version to use |
| **origin_cluster**  string | Name of the origin cluster for the FlexCache.  Defaults to cluster associated with target vserver if absent.  Not used for creation. |
| **origin_volume**  string | Name of the origin volume for the FlexCache.  Required for creation. |
| **origin_vserver**  string | Name of the origin vserver for the FlexCache.  Required for creation. |
| **password**  aliases: pass  string | Password for the specified user. |
| **prepopulate**  dictionary  *added in netapp.ontap 21.3.0* | prepopulate FlexCache with data from origin volume.  requires ONTAP 9.8 or later, and REST support.  dir_paths must be set for this option to be effective. |
| **dir_paths**  list / elements=string / required | List of directory paths in the owning SVM’s namespace at which the FlexCache volume is mounted.  Path must begin with ‘/’. |
| **exclude_dir_paths**  list / elements=string | Directory path which needs to be excluded from prepopulation.  Path must begin with ‘/’.  Requires ONTAP 9.9 or later. |
| **force_prepopulate_if_already_created**  boolean | by default, this module will start a prepopulate task each time it is called, and is not idempotent.  if set to false, the prepopulate task is not started if the FlexCache already exists.  **Choices:**   - `false` - `true` ← (default) |
| **recurse**  boolean | Specifies whether or not the prepopulate action should search through the directory-path recursively.  If not set, the default value ‘true’ is used.  **Choices:**   - `false` - `true` |
| **size**  integer | Size of cache volume. |
| **size_unit**  string | The unit used to interpret the size parameter.  **Choices:**   - `"bytes"` - `"b"` - `"kb"` - `"mb"` - `"gb"` ← (default) - `"tb"` - `"pb"` - `"eb"` - `"zb"` - `"yb"` |
| **state**  string | Whether the specified relationship should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **time_out**  integer | time to wait for flexcache creation or deletion in seconds  if 0, the request is asynchronous  default is set to 3 minutes  **Default:** `180` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **vserver**  string / required | Name of the target vserver for the FlexCache.  Note that hostname, username, password are intended for the target vserver. |

## [Notes](na_ontap_flexcache_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_flexcache_module.md#id5)

```yaml+jinja
- name: Create FlexCache
  netapp.ontap.na_ontap_flexcache:
    state: present
    origin_volume: test_src
    name: test_dest
    origin_vserver: ansible_src
    vserver: ansible_dest
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Delete FlexCache
  netapp.ontap.na_ontap_flexcache:
    state: absent
    name: test_dest
    vserver: ansible_dest
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
