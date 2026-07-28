---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_volume_efficiency module – NetApp ONTAP enables, disables or modifies volume efficiency"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_volume_efficiency_module.html
fetched_at: 2026-07-28T02:43:35+00:00
---
# netapp.ontap.na_ontap_volume_efficiency module – NetApp ONTAP enables, disables or modifies volume efficiency

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
> see [Requirements](na_ontap_volume_efficiency_module.md#ansible-collections-netapp-ontap-na-ontap-volume-efficiency-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_volume_efficiency`.

New in netapp.ontap 21.2.0

- [Synopsis](na_ontap_volume_efficiency_module.md#synopsis)
- [Requirements](na_ontap_volume_efficiency_module.md#requirements)
- [Parameters](na_ontap_volume_efficiency_module.md#parameters)
- [Notes](na_ontap_volume_efficiency_module.md#notes)
- [Examples](na_ontap_volume_efficiency_module.md#examples)

## [Synopsis](na_ontap_volume_efficiency_module.md#id1)

- Enable, modify or disable volume efficiency.
- Either path or volume_name is required.
- Only admin user can modify volume efficiency.

## [Requirements](na_ontap_volume_efficiency_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_volume_efficiency_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **enable_compression**  boolean | Specifies if compression is to be enabled.  **Choices:**   - `false` - `true` |
| **enable_cross_volume_background_dedupe**  boolean | Specifies if cross volume background deduplication is to be enabled, this can only be enabled when inline deduplication is enabled.  **Choices:**   - `false` - `true` |
| **enable_cross_volume_inline_dedupe**  boolean | Specifies if in-line cross volume inline deduplication is to be enabled, this can only be enabled when inline deduplication is enabled.  **Choices:**   - `false` - `true` |
| **enable_data_compaction**  boolean | Specifies if compaction is to be enabled.  **Choices:**   - `false` - `true` |
| **enable_inline_compression**  boolean | Specifies if in-line compression is to be enabled.  **Choices:**   - `false` - `true` |
| **enable_inline_dedupe**  boolean | Specifies if in-line deduplication is to be enabled, only supported on AFF systems or hybrid aggregates.  **Choices:**   - `false` - `true` |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **path**  string | Specifies the path for the volume.  Either `path` or `volume_name` is required.  Requires ONTAP 9.9.1 or later with REST. |
| **policy**  string | Specifies the storage efficiency policy to use.  By default, the following names are available ‘auto’, ‘default’, ‘inline-only’, ‘-‘.  Requires ONTAP 9.7 or later with REST. |
| **schedule**  string | Specifies the storage efficiency schedule.  Only supported with ZAPI. |
| **start_ve_build_metadata**  boolean  *added in netapp.ontap 21.4.0* | Specifies the scanner to scan the entire and generate fingerprint database without attempting the sharing.  Only supported with ZAPI.  **Choices:**   - `false` - `true` |
| **start_ve_delete_checkpoint**  boolean  *added in netapp.ontap 21.4.0* | Specifies the scanner to delete existing checkpoint and start the operation from the begining.  Only supported with ZAPI.  **Choices:**   - `false` - `true` |
| **start_ve_qos_policy**  string  *added in netapp.ontap 21.4.0* | Specifies the QoS policy for the operation.  Default is best-effort in ZAPI.  Only supported with ZAPI.  **Choices:**   - `"background"` - `"best-effort"` |
| **start_ve_queue_operation**  boolean  *added in netapp.ontap 21.4.0* | Specifies the operation to queue if an exisitng operation is already running on the volume and in the fingerprint verification phase.  Only supported with ZAPI.  **Choices:**   - `false` - `true` |
| **start_ve_scan_all**  boolean  *added in netapp.ontap 21.4.0* | Specifies the scanner to scan the entire volume without applying share block optimization.  Only supported with ZAPI.  **Choices:**   - `false` - `true` |
| **start_ve_scan_old_data**  boolean  *added in netapp.ontap 21.4.0* | Specifies the operation to scan the file system to process all the existing data.  Requires ONTAP 9.11.1 or later with REST.  **Choices:**   - `false` - `true` |
| **state**  string | Whether the specified volume efficiency should be enabled or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **stop_ve_all_operations**  boolean  *added in netapp.ontap 21.4.0* | Specifies that all running and queued operations to be stopped.  Only supported with ZAPI.  **Choices:**   - `false` - `true` |
| **storage_efficiency_mode**  string  *added in netapp.ontap 21.14.0* | Storage efficiency mode used by volume. This parameter is only supported on AFF platforms.  Requires ONTAP 9.10.1 or later.  **Choices:**   - `"default"` - `"efficient"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **volume_efficiency**  string  *added in netapp.ontap 21.4.0* | Start or Stop a volume efficiency operation on a given volume path.  Requires ONTAP 9.11.1 or later with REST.  **Choices:**   - `"start"` - `"stop"` |
| **volume_name**  string  *added in netapp.ontap 22.3.0* | Specifies the volume name. |
| **vserver**  string / required | Specifies the vserver for the volume. |

## [Notes](na_ontap_volume_efficiency_module.md#id4)

> **Note:**
>
> - supports ZAPI and REST. REST requires ONTAP 9.6 or later.
> - supports check mode.
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_volume_efficiency_module.md#id5)

```yaml+jinja
- name: Enable Volume efficiency
  netapp.ontap.na_ontap_volume_efficiency:
    state: present
    vserver: "TESTSVM"
    path: "/vol/test_sis"
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    https: true
    validate_certs: false

- name: Disable Volume efficiency test
  netapp.ontap.na_ontap_volume_efficiency:
    state: absent
    vserver: "TESTSVM"
    path: "/vol/test_sis"
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    https: true
    validate_certs: false

- name: Modify storage efficiency schedule with ZAPI.
  netapp.ontap.na_ontap_volume_efficiency:
    state: present
    vserver: "TESTSVM"
    path: "/vol/test_sis"
    schedule: "mon-sun@0,1,23"
    enable_compression: true
    enable_inline_compression: true
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    https: true
    validate_certs: false

- name: Start volume efficiency
  netapp.ontap.na_ontap_volume_efficiency:
    state: present
    vserver: "TESTSVM"
    path: "/vol/test_sis"
    volume_efficiency: "start"
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    https: true
    validate_certs: false

- name: Stop volume efficiency
  netapp.ontap.na_ontap_volume_efficiency:
    state: present
    vserver: "TESTSVM"
    path: "/vol/test_sis"
    volume_efficiency: "stop"
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    https: true
    validate_certs: false

- name: modify volume efficiency with volume name in REST.
  netapp.ontap.na_ontap_volume_efficiency:
    state: present
    vserver: "TESTSVM"
    volume_name: "test_sis"
    volume_efficiency: "stop"
    enable_compression: True
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    https: true
    validate_certs: false
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
