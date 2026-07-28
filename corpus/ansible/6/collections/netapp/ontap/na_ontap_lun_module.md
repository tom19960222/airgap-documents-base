---
collection: ansible
version: "6"
title: "netapp.ontap.na_ontap_lun module – NetApp ONTAP manage LUNs"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/ontap/na_ontap_lun_module.html
fetched_at: 2026-07-28T00:12:38+00:00
---
# netapp.ontap.na_ontap_lun module – NetApp ONTAP manage LUNs

> **Note:**
>
> This module is part of the [netapp.ontap collection](https://galaxy.ansible.com/netapp/ontap) (version 21.24.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.ontap`.
> You need further requirements to be able to use this module,
> see [Requirements](na_ontap_lun_module.md#ansible-collections-netapp-ontap-na-ontap-lun-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_lun`.

New in netapp.ontap 2.6.0

- [Synopsis](na_ontap_lun_module.md#synopsis)
- [Requirements](na_ontap_lun_module.md#requirements)
- [Parameters](na_ontap_lun_module.md#parameters)
- [Notes](na_ontap_lun_module.md#notes)
- [Examples](na_ontap_lun_module.md#examples)

## [Synopsis](na_ontap_lun_module.md#id1)

- Create, destroy, resize LUNs on NetApp ONTAP.

## [Requirements](na_ontap_lun_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_lun_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **comment**  string  added in netapp.ontap 21.2.0 | Optional descriptive comment for the LUN. |
| **feature_flags**  dictionary  added in netapp.ontap 20.5.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **flexvol_name**  string | The name of the FlexVol the LUN should exist on.  Required if san_application_template is not present.  Not allowed if san_application_template is present. |
| **force_ontap_version**  string  added in netapp.ontap 21.23.0 | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **force_remove**  boolean | If “true”, override checks that prevent a LUN from being destroyed if it is online and mapped.  If “false”, destroying an online and mapped LUN will fail.  Choices:   - `false` ← (default) - `true` |
| **force_remove_fenced**  boolean | If “true”, override checks that prevent a LUN from being destroyed while it is fenced.  If “false”, attempting to destroy a fenced LUN will fail.  The default if not specified is “false”. This field is available in Data ONTAP 8.2 and later.  Choices:   - `false` - `true` |
| **force_resize**  boolean | Forcibly reduce the size. This is required for reducing the size of the LUN to avoid accidentally reducing the LUN size.  Choices:   - `false` - `true` |
| **from_name**  string  added in netapp.ontap 20.12.0 | The name of the LUN to be renamed. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  Choices:   - `false` ← (default) - `true` |
| **key_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client key file. |
| **name**  string / required | The name of the LUN to manage.  Or LUN group name (volume name) when san_application_template is used. |
| **ontapi**  integer | The ontap api version to use |
| **os_type**  aliases: ostype  string | The os type for the LUN. |
| **password**  aliases: pass  string | Password for the specified user. |
| **qos_adaptive_policy_group**  string  added in netapp.ontap 21.2.0 | The adaptive QoS policy group to be set on the LUN.  Defines measurable service level objectives (SLOs) and service level agreements (SLAs) that adjust based on the LUN’s allocated space or used space.  Requires ONTAP 9.4 or later.  With REST, qos_policy_group and qos_adaptive_policy_group are handled as QOS policy. |
| **qos_policy_group**  string  added in netapp.ontap 20.12.0 | The QoS policy group to be set on the LUN.  With REST, qos_policy_group and qos_adaptive_policy_group are handled as QOS policy. |
| **san_application_template**  dictionary  added in netapp.ontap 20.12.0 | additional options when using the application/applications REST API to create LUNs.  the module is using ZAPI by default, and switches to REST if san_application_template is present.  create one or more LUNs (and the associated volume as needed).  operations at the LUN level are supported, they require to know the LUN short name.  this requires ONTAP 9.8 or higher.  The module partially supports ONTAP 9.7 for create and delete operations, but not for modify (API limitations). |
| **exclude_aggregates**  list / elements=string  added in netapp.ontap 21.7.0 | The list of aggregate names to exclude when creating a volume.  Requires ONTAP 9.9.1 GA or better. |
| **igroup_name**  string | name of the initiator group through which the contents of this application will be accessed. |
| **lun_count**  integer | number of LUNs in the application component (1 to 32). |
| **name**  string / required | name of the SAN application. |
| **protection_type**  dictionary | The snasphot policy for the volume supporting the LUNs. |
| **local_policy**  string | The snapshot copy policy for the volume. |
| **scope**  string  added in netapp.ontap 21.2.0 | whether the top level name identifies a single LUN or a LUN group (application).  By default, the module will try to make the right choice, but can report extra warnings.  Setting scope to ‘application’ is required to convert an existing volume to a smart container.  The module reports an error when ‘lun’ or ‘application’ is used and the desired action cannot be completed.  The module issues warnings when the default ‘auto’ is used, and there is ambiguity regarding the desired actions.  Choices:   - `"application"` - `"auto"` ← (default) - `"lun"` |
| **storage_service**  string | The performance service level (PSL) for this volume  Choices:   - `"value"` - `"performance"` - `"extreme"` |
| **tiering**  dictionary | Cloud tiering policy. |
| **control**  string | Storage tiering placement rules for the container.  Choices:   - `"required"` - `"best_effort"` - `"disallowed"` |
| **object_stores**  list / elements=string | list of object store names for tiering. |
| **policy**  string | Cloud tiering policy.  Choices:   - `"all"` - `"auto"` - `"none"` - `"snapshot-only"` |
| **total_size**  integer  added in netapp.ontap 21.1.0 | The total size of the application component, split across the member LUNs in `total_size_unit`.  Recommended when `lun_count` is present.  Required when `lun_count` is present and greater than 1.  Note - if lun_count is equal to 1, and total_size is not present, size is used to maintain backward compatibility. |
| **total_size_unit**  string  added in netapp.ontap 21.1.0 | The unit used to interpret the total_size parameter.  Defaults to size_unit if not present.  Choices:   - `"bytes"` - `"b"` - `"kb"` - `"mb"` - `"gb"` - `"tb"` - `"pb"` - `"eb"` - `"zb"` - `"yb"` |
| **use_san_application**  boolean | Whether to use the application/applications REST/API to create LUNs.  This will default to true if any other suboption is present.  Choices:   - `false` - `true` ← (default) |
| **size**  integer | The size of the LUN in `size_unit`.  Required when creating a single LUN if application template is not used. |
| **size_unit**  string | The unit used to interpret the size parameter.  Choices:   - `"bytes"` - `"b"` - `"kb"` - `"mb"` - `"gb"` ← (default) - `"tb"` - `"pb"` - `"eb"` - `"zb"` - `"yb"` |
| **space_allocation**  boolean  added in netapp.ontap 2.7.0 | This enables support for the SCSI Thin Provisioning features. If the Host and file system do not support this do not enable it.  Choices:   - `false` - `true` |
| **space_reserve**  boolean | This can be set to “false” which will create a LUN without any space being reserved.  Choices:   - `false` - `true` ← (default) |
| **state**  string | Whether the specified LUN should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **use_exact_size**  boolean  added in netapp.ontap 20.11.0 | This can be set to “false” which will round the LUN >= 450g.  Choices:   - `false` - `true` ← (default) |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  Default: `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **vserver**  string / required | The name of the vserver to use. |

## [Notes](na_ontap_lun_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_lun_module.md#id5)

```yaml+jinja
- name: Create LUN
  netapp.ontap.na_ontap_lun:
    state: present
    name: ansibleLUN
    flexvol_name: ansibleVolume
    vserver: ansibleVServer
    size: 5
    size_unit: mb
    os_type: linux
    space_reserve: true
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Resize LUN
  netapp.ontap.na_ontap_lun:
    state: present
    name: ansibleLUN
    force_resize: true
    flexvol_name: ansibleVolume
    vserver: ansibleVServer
    size: 5
    size_unit: gb
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Create LUNs using SAN application
  tags: create
  netapp.ontap.na_ontap_lun:
    state: present
    name: ansibleLUN
    size: 15
    size_unit: mb
    os_type: linux
    space_reserve: false
    san_application_template:
      name: san-ansibleLUN
      igroup_name: testme_igroup
      lun_count: 3
      protection_type:
      local_policy: default
      exclude_aggregates: aggr0
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Convert existing volume to SAN application
  tags: create
  netapp.ontap.na_ontap_lun:
    state: present
    name: someVolume
    size: 22
    size_unit: mb
    os_type: linux
    space_reserve: false
    san_application_template:
      name: san-ansibleLUN
      igroup_name: testme_igroup
      lun_count: 3
      protection_type:
      local_policy: default
      scope: application
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
