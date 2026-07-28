---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_fpolicy_event module – NetApp ONTAP FPolicy policy event configuration"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_fpolicy_event_module.html
fetched_at: 2026-07-28T02:42:13+00:00
---
# netapp.ontap.na_ontap_fpolicy_event module – NetApp ONTAP FPolicy policy event configuration

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
> see [Requirements](na_ontap_fpolicy_event_module.md#ansible-collections-netapp-ontap-na-ontap-fpolicy-event-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_fpolicy_event`.

New in netapp.ontap 21.4.0

- [Synopsis](na_ontap_fpolicy_event_module.md#synopsis)
- [Requirements](na_ontap_fpolicy_event_module.md#requirements)
- [Parameters](na_ontap_fpolicy_event_module.md#parameters)
- [Notes](na_ontap_fpolicy_event_module.md#notes)
- [Examples](na_ontap_fpolicy_event_module.md#examples)

## [Synopsis](na_ontap_fpolicy_event_module.md#id1)

- Create, delete or modify an FPolicy policy event.

## [Requirements](na_ontap_fpolicy_event_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_fpolicy_event_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **file_operations**  list / elements=string | Name of file operations to be applied to the event. By default no operations are monitored.  **Choices:**   - `"close"` - `"create"` - `"create_dir"` - `"delete"` - `"delete_dir"` - `"getattr"` - `"link"` - `"lookup"` - `"open"` - `"read"` - `"write"` - `"rename"` - `"rename_dir"` - `"setattr"` - `"symlink"` |
| **filters**  list / elements=string | Name of filters to be applied to the event. It is notification filtering parameters. By default no filters are selected.  **Choices:**   - `"monitor_ads"` - `"close_with_modification"` - `"close_without_modification"` - `"first_read"` - `"first_write"` - `"offline_bit"` - `"open_with_delete_intent"` - `"open_with_write_intent"` - `"write_with_size_change"` - `"close_with_read"` - `"setattr_with_owner_change"` - `"setattr_with_group_change"` - `"setattr_with_sacl_change"` - `"setattr_with_dacl_change"` - `"setattr_with_modify_time_change"` - `"setattr_with_access_time_change"` - `"setattr_with_creation_time_change"` - `"setattr_with_mode_change"` - `"setattr_with_size_change"` - `"setattr_with_allocation_size_change"` - `"exclude_directory"` |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **name**  string / required | Name of the Event. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **protocol**  string | Name of protocol for which event is created. By default no protocol is selected.  **Choices:**   - `"cifs"` - `"nfsv3"` - `"nfsv4"` |
| **state**  string | Whether the FPolicy policy event is present or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **volume_monitoring**  boolean | Indicator if the volume operation required for the event. If not specified the default Value is false.  **Choices:**   - `false` - `true` |
| **vserver**  string / required | The name of the vserver to create the event on. |

## [Notes](na_ontap_fpolicy_event_module.md#id4)

> **Note:**
>
> - Support check_mode.
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_fpolicy_event_module.md#id5)

```yaml+jinja
- name: Create FPolicy Event
  na_ontap_fpolicy_event:
    state: present
    vserver: svm1
    name: fpolicy_event
    file_operations: ['create', 'create_dir', 'delete', 'delete_dir', 'read', 'close', 'rename', 'rename_dir']
    filters: ['first_read', 'close_with_modification']
    protocol: cifs
    volume_monitoring: false
    username: "{{ username }}"
    password: "{{ password }}"
    hostname: "{{ hostname }}"

- name: Modify FPolicy Event
  na_ontap_fpolicy_event:
    state: present
    vserver: svm1
    name: fpolicy_event
    volume_monitoring: true
    username: "{{ username }}"
    password: "{{ password }}"
    hostname: "{{ hostname }}"

- name: Delete FPolicy Event
  na_ontap_fpolicy_event:
    state: absent
    vserver: svm1
    name: fpolicy_event
    username: "{{ username }}"
    password: "{{ password }}"
    hostname: "{{ hostname }}"
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
