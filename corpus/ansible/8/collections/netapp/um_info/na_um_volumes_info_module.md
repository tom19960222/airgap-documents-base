---
collection: ansible
version: "8"
title: "netapp.um_info.na_um_volumes_info module – NetApp Unified Manager list volumes."
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/um_info/na_um_volumes_info_module.html
fetched_at: 2026-07-28T01:05:52+00:00
---
# netapp.um_info.na_um_volumes_info module – NetApp Unified Manager list volumes.

> **Note:**
>
> This module is part of the [netapp.um_info collection](https://galaxy.ansible.com/ui/repo/published/netapp/um_info/) (version 21.8.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.um_info`.
> You need further requirements to be able to use this module,
> see [Requirements](na_um_volumes_info_module.md#ansible-collections-netapp-um-info-na-um-volumes-info-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.um_info.na_um_volumes_info`.

New in netapp.um_info 20.6.0

- [Synopsis](na_um_volumes_info_module.md#synopsis)
- [Requirements](na_um_volumes_info_module.md#requirements)
- [Parameters](na_um_volumes_info_module.md#parameters)
- [Notes](na_um_volumes_info_module.md#notes)
- [Examples](na_um_volumes_info_module.md#examples)
- [Return Values](na_um_volumes_info_module.md#return-values)

## [Synopsis](na_um_volumes_info_module.md#id1)

- List Volumes on AIQUM.

Aliases: na_um_list_volumes

## [Requirements](na_um_volumes_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- A AIQUM 9.7 system.
- Ansible 2.9 or later.

## [Parameters](na_um_volumes_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **feature_flags**  dictionary  *added in netapp.um_info 21.7.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored.  trace_apis can be set to true to enable tracing, data is written to /tmp/um_apis.log. |
| **hostname**  string / required | The hostname or IP address of the Unified Manager instance. |
| **http_port**  integer | Override the default port (443) with this port |
| **max_records**  integer  *added in netapp.um_info 21.7.0* | Maximum number of records retrieved in a single GET request.  This module loops on GET requests until all available records are fetched.  If absent, AIQUM uses 1000. |
| **password**  string / required | Password for the specified user. |
| **username**  string / required | username of the Unified Manager instance. |
| **validate_certs**  boolean | If set to `False`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](na_um_volumes_info_module.md#id4)

> **Note:**
>
> - With the 21.6.0 release, all modules have been renamed to na_um_<module>_info. The old ones will continue to work but will be depecrated in the future.
> - The modules prefixed with na_um are built to support the AIQUM 9.7 platform.
> - Supports check_mode.

## [Examples](na_um_volumes_info_module.md#id5)

```yaml+jinja
- name: List Volumes
  netapp.um_info.na_um_volumes_info:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
```

## [Return Values](na_um_volumes_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **records**  list / elements=string | Returns list of Volumes information  **Returned:** always  **Sample:** `[{"_links": {"self": {"href": "..."}}, "aggregates": [{"...": null}], "autosize": {"...": null}, "cluster": {"...": null}, "create_time": "...", "key": "...", "language": "...", "name": "...", "qos": {"...": null}, "snapmirror": {"...": null}, "snapshot_policy": {"...": null}, "space": {"...": null}, "state": "...", "style": "...", "svm": {"...": null, "_links": {"self": {"...": null}}}, "tiering": {"...": null}, "type": "...", "uuid": "..."}]` |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.um_info/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.um_info)
