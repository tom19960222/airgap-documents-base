---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_svm module – NetApp ONTAP SVM"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_svm_module.html
fetched_at: 2026-07-28T02:43:27+00:00
---
# netapp.ontap.na_ontap_svm module – NetApp ONTAP SVM

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
> see [Requirements](na_ontap_svm_module.md#ansible-collections-netapp-ontap-na-ontap-svm-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_svm`.

New in netapp.ontap 2.6.0

- [Synopsis](na_ontap_svm_module.md#synopsis)
- [Requirements](na_ontap_svm_module.md#requirements)
- [Parameters](na_ontap_svm_module.md#parameters)
- [Notes](na_ontap_svm_module.md#notes)
- [Examples](na_ontap_svm_module.md#examples)

## [Synopsis](na_ontap_svm_module.md#id1)

- Create, modify or delete SVM on NetApp ONTAP

## [Requirements](na_ontap_svm_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_svm_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **admin_state**  string  *added in netapp.ontap 21.15.0* | when the SVM is created, it will be in the running state, unless specified otherwise.  This is ignored with ZAPI.  **Choices:**   - `"running"` - `"stopped"` |
| **aggr_list**  list / elements=string | List of aggregates assigned for volume operations.  These aggregates could be shared for use with other Vservers.  When specified as part of a vserver-create, this field represents the list of aggregates that are assigned to the Vserver for volume operations.  When part of vserver-get-iter call, this will return the list of Vservers which have any of the aggregates specified as part of the aggr list. |
| **allowed_protocols**  list / elements=string | Allowed Protocols.  This field represent the list of protocols allowed on the Vserver.  When part of modify, this field should include the existing list along with new protocol list to be added to prevent data disruptions.  Possible values  nfs NFS protocol,  cifs CIFS protocol,  fcp FCP protocol,  iscsi iSCSI protocol,  ndmp NDMP protocol,  http HTTP protocol - ZAPI only,  nvme NVMe protocol |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **comment**  string  *added in netapp.ontap 2.8.0* | When specified as part of a vserver-create, this field represents the comment associated with the Vserver.  When part of vserver-get-iter call, this will return the list of matching Vservers. |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **from_name**  string  *added in netapp.ontap 2.7.0* | Name of the SVM to be renamed |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **ignore_rest_unsupported_options**  boolean  *added in netapp.ontap 21.10.0* | When true, ignore `root_volume`, `root_volume_aggregate`, `root_volume_security_style` options if target supports REST.  Ignored when `use_rest` is set to never.  **Choices:**   - `false` ← (default) - `true` |
| **ipspace**  string  *added in netapp.ontap 2.7.0* | IPSpace name  Cannot be modified after creation. |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **language**  string  *added in netapp.ontap 2.7.0* | Language to use for the SVM  Default to C.UTF-8  Possible values Language  c POSIX  ar Arabic  cs Czech  da Danish  de German  en English  en_us English (US)  es Spanish  fi Finnish  fr French  he Hebrew  hr Croatian  hu Hungarian  it Italian  ja Japanese euc-j  ja_v1 Japanese euc-j  ja_jp.pck Japanese PCK (sjis)  ja_jp.932 Japanese cp932  ja_jp.pck_v2 Japanese PCK (sjis)  ko Korean  no Norwegian  nl Dutch  pl Polish  pt Portuguese  ro Romanian  ru Russian  sk Slovak  sl Slovenian  sv Swedish  tr Turkish  zh Simplified Chinese  zh.gbk Simplified Chinese (GBK)  zh_tw Traditional Chinese euc-tw  zh_tw.big5 Traditional Chinese Big 5  utf8mb4  Most of the values accept a .utf_8 suffix, e.g. fr.utf_8 |
| **max_volumes**  string  *added in netapp.ontap 21.12.0* | Maximum number of volumes that can be created on the vserver.  Expects an integer or `unlimited`. |
| **name**  aliases: vserver  string / required | The name of the SVM to manage.  vserver is a convenient alias when using module_defaults. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **root_volume**  string | Root volume of the SVM.  Cannot be modified after creation. |
| **root_volume_aggregate**  string | The aggregate on which the root volume will be created.  Cannot be modified after creation. |
| **root_volume_security_style**  string | Security Style of the root volume.  When specified as part of the vserver-create, this field represents the security style for the Vserver root volume.  When specified as part of vserver-get-iter call, this will return the list of matching Vservers.  The ‘unified’ security style, which applies only to Infinite Volumes, cannot be applied to a Vserver’s root volume.  Cannot be modified after creation.  **Choices:**   - `"unix"` - `"ntfs"` - `"mixed"` - `"unified"` |
| **services**  dictionary  *added in netapp.ontap 21.10.0* | Enabled Protocols, only available with REST.  The service will be started if needed. A valid license may be required.  `enabled` is not supported for CIFS, to enable it use na_ontap_cifs_server.  If a service is not present, it is left unchanged. |
| **cifs**  dictionary | CIFS protocol service |
| **allowed**  boolean | If true, an SVM administrator can manage the CIFS service. If false, only the cluster administrator can manage the service.  **Choices:**   - `false` - `true` |
| **fcp**  dictionary | FCP protocol service |
| **allowed**  boolean | If true, an SVM administrator can manage the FCP service. If false, only the cluster administrator can manage the service.  **Choices:**   - `false` - `true` |
| **enabled**  boolean | If allowed, setting to true enables the FCP service.  **Choices:**   - `false` - `true` |
| **iscsi**  dictionary | iSCSI protocol service |
| **allowed**  boolean | If true, an SVM administrator can manage the iSCSI service. If false, only the cluster administrator can manage the service.  **Choices:**   - `false` - `true` |
| **enabled**  boolean | If allowed, setting to true enables the iSCSI service.  **Choices:**   - `false` - `true` |
| **ndmp**  dictionary  *added in netapp.ontap 21.24.0* | Network Data Management Protocol service |
| **allowed**  boolean | If this is set to true, an SVM administrator can manage the NDMP service  If it is false, only the cluster administrator can manage the service.  Requires ONTAP 9.10.1 or later.  **Choices:**   - `false` - `true` |
| **nfs**  dictionary | NFS protocol service |
| **allowed**  boolean | If true, an SVM administrator can manage the NFS service. If false, only the cluster administrator can manage the service.  **Choices:**   - `false` - `true` |
| **enabled**  boolean | If allowed, setting to true enables the NFS service.  **Choices:**   - `false` - `true` |
| **nvme**  dictionary | nvme protocol service |
| **allowed**  boolean | If true, an SVM administrator can manage the NVMe service. If false, only the cluster administrator can manage the service.  **Choices:**   - `false` - `true` |
| **enabled**  boolean | If allowed, setting to true enables the NVMe service.  **Choices:**   - `false` - `true` |
| **snapshot_policy**  string  *added in netapp.ontap 2.7.0* | Default snapshot policy setting for all volumes of the Vserver. This policy will be assigned to all volumes created in this Vserver unless the volume create request explicitly provides a snapshot policy or volume is modified later with a specific snapshot policy. A volume-level snapshot policy always overrides the default Vserver-wide snapshot policy. |
| **state**  string | Whether the specified SVM should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subtype**  string  *added in netapp.ontap 2.7.0* | The subtype for vserver to be created.  Cannot be modified after creation.  **Choices:**   - `"default"` - `"dp_destination"` - `"sync_source"` - `"sync_destination"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **web**  dictionary | web services security configuration.  requires ONTAP 9.8 or later for certificate name.  requires ONTAP 9.10.1 or later for the other options. |
| **certificate**  string | name of certificate used by cluster and node management interfaces for TLS connection requests.  The certificate must be of type “server”. |
| **client_enabled**  boolean | whether client authentication is enabled.  **Choices:**   - `false` - `true` |
| **ocsp_enabled**  boolean | whether online certificate status protocol verification is enabled.  **Choices:**   - `false` - `true` |

## [Notes](na_ontap_svm_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_svm_module.md#id5)

```yaml+jinja
- name: Create SVM
  netapp.ontap.na_ontap_svm:
    state: present
    name: ansibleVServer
    root_volume: vol1
    root_volume_aggregate: aggr1
    root_volume_security_style: mixed
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Create SVM
  netapp.ontap.na_ontap_svm:
    state: present
    services:
      cifs:
        allowed: true
      fcp:
        allowed: true
      nfs:
        allowed: true
        enabled: true
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    https: true
    validate_certs: false

- name: Stop SVM REST
  netapp.ontap.na_ontap_svm:
    state: present
    name: ansibleVServer
    admin_state: stopped
    use_rest: always
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
