---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_volume_autosize module – NetApp ONTAP manage volume autosize"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_volume_autosize_module.html
fetched_at: 2026-07-28T02:43:34+00:00
---
# netapp.ontap.na_ontap_volume_autosize module – NetApp ONTAP manage volume autosize

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
> see [Requirements](na_ontap_volume_autosize_module.md#ansible-collections-netapp-ontap-na-ontap-volume-autosize-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_volume_autosize`.

New in netapp.ontap 2.9.0

- [Synopsis](na_ontap_volume_autosize_module.md#synopsis)
- [Requirements](na_ontap_volume_autosize_module.md#requirements)
- [Parameters](na_ontap_volume_autosize_module.md#parameters)
- [Notes](na_ontap_volume_autosize_module.md#notes)
- [Examples](na_ontap_volume_autosize_module.md#examples)

## [Synopsis](na_ontap_volume_autosize_module.md#id1)

- Modify Volume AutoSize

## [Requirements](na_ontap_volume_autosize_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_volume_autosize_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **grow_threshold_percent**  integer | Specifies the percentage of the flexible volume’s capacity at which autogrow is initiated.  The default grow threshold varies from 85% to 98%, depending on the volume size.  It is an error for the grow threshold to be less than or equal to the shrink threshold.  Range between 0 and 100 |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **increment_size**  string | Specify the flexible volume’s increment size using the following format < number > [k|m|g|t]  The amount is the absolute size to set.  The trailing ‘k’, ‘m’, ‘g’, and ‘t’ indicates the desired units, namely ‘kilobytes’, ‘megabytes’, ‘gigabytes’, and ‘terabytes’ (respectively). |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **maximum_size**  string | Specify the flexible volume’s maximum allowed size using the following format < number > [k|m|g|t]  The amount is the absolute size to set.  The trailing ‘k’, ‘m’, ‘g’, and ‘t’ indicates the desired units, namely ‘kilobytes’, ‘megabytes’, ‘gigabytes’, and ‘terabytes’ (respectively).  The default value is 20% greater than the volume size at the time autosize was enabled.  It is an error for the maximum volume size to be less than the current volume size.  It is also an error for the maximum size to be less than or equal to the minimum size. |
| **minimum_size**  string | Specify the flexible volume’s minimum allowed size using the following format < number > [k|m|g|t] The amount is the absolute size to set.  The trailing ‘k’, ‘m’, ‘g’, and ‘t’ indicates the desired units, namely ‘kilobytes’, ‘megabytes’, ‘gigabytes’, and ‘terabytes’ (respectively).  The default value is the size of the volume at the time the ‘grow_shrink’ mode was enabled.  It is an error for the minimum size to be greater than or equal to the maximum size. |
| **mode**  string | Specify the flexible volume’s autosize mode of operation.  **Choices:**   - `"grow"` - `"grow_shrink"` - `"off"` |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **reset**  boolean | Sets the values of maximum_size, increment_size, minimum_size, grow_threshold_percent, shrink_threshold_percent and mode to their defaults  If reset paramater is present system will always perform reset action, so idempotency is not supported.  **Choices:**   - `false` - `true` |
| **shrink_threshold_percent**  integer | Specifies the percentage of the flexible volume’s capacity at which autoshrink is initiated.  The default shrink theshold is 50%. It is an error for the shrink threshold to be greater than or equal to the grow threshold.  Range between 0 and 100 |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **volume**  string / required | The name of the flexible volume for which we want to set autosize. |
| **vserver**  string / required | Name of the vserver to use. |

## [Notes](na_ontap_volume_autosize_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_volume_autosize_module.md#id5)

```yaml+jinja
- name: Modify volume autosize
  netapp.ontap.na_ontap_volume_autosize:
    hostname: 10.193.79.189
    username: admin
    password: netapp1!
    volume: ansibleVolumesize12
    mode: grow
    grow_threshold_percent: 99
    increment_size: 50m
    maximum_size: 10g
    minimum_size: 21m
    shrink_threshold_percent: 40
    vserver: ansible_vserver

- name: Reset volume autosize
  netapp.ontap.na_ontap_volume_autosize:
    hostname: 10.193.79.189
    username: admin
    password: netapp1!
    volume: ansibleVolumesize12
    reset: true
    vserver: ansible_vserver
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
