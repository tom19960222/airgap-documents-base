---
collection: ansible
version: "6"
title: "netapp.ontap.na_ontap_fpolicy_ext_engine module – NetApp ONTAP fPolicy external engine configuration."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/ontap/na_ontap_fpolicy_ext_engine_module.html
fetched_at: 2026-07-28T00:12:25+00:00
---
# netapp.ontap.na_ontap_fpolicy_ext_engine module – NetApp ONTAP fPolicy external engine configuration.

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
> see [Requirements](na_ontap_fpolicy_ext_engine_module.md#ansible-collections-netapp-ontap-na-ontap-fpolicy-ext-engine-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_fpolicy_ext_engine`.

New in netapp.ontap 21.4.0

- [Synopsis](na_ontap_fpolicy_ext_engine_module.md#synopsis)
- [Requirements](na_ontap_fpolicy_ext_engine_module.md#requirements)
- [Parameters](na_ontap_fpolicy_ext_engine_module.md#parameters)
- [Notes](na_ontap_fpolicy_ext_engine_module.md#notes)
- [Examples](na_ontap_fpolicy_ext_engine_module.md#examples)

## [Synopsis](na_ontap_fpolicy_ext_engine_module.md#id1)

- Create, delete or modify fpolicy external engine.

## [Requirements](na_ontap_fpolicy_ext_engine_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_fpolicy_ext_engine_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **certificate_ca**  string | Certificate authority name. No default value is set for this field. |
| **certificate_common_name**  string | FQDN or custom common name of certificate. No default value is set for this field. |
| **certificate_serial**  string | Serial number of certificate. No default value is set for this field. |
| **extern_engine_type**  string | External engine type. If the engine is asynchronous, no reply is sent from FPolicy servers. Default value set for this field is synchronous.  Choices:   - `"synchronous"` - `"asynchronous"` |
| **feature_flags**  dictionary  added in netapp.ontap 20.5.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  added in netapp.ontap 21.23.0 | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  Choices:   - `false` ← (default) - `true` |
| **is_resiliency_enabled**  boolean | Indicates if the resiliency with this engine is required.  If set to true, the notifications will be stored in a path as resiliency_directory_path  If it is false, the notifications will not be stored. Default value is false.  Choices:   - `false` - `true` |
| **key_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client key file. |
| **max_connection_retries**  integer | Number of times storage appliance will attempt to establish a broken connection to FPolicy server. Default value set for this field is 5. |
| **max_server_reqs**  integer | Maximum number of outstanding screen requests that will be queued for an FPolicy Server. Default value set for this field is 50. |
| **name**  string / required | Name of the external engine. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **port**  integer | Port number of the FPolicy server application. |
| **primary_servers**  list / elements=string | Primary FPolicy servers. |
| **recv_buffer_size**  integer | Receive buffer size of connected socket for FPolicy Server. Default value set for this field is 256 kilobytes (256Kb). |
| **resiliency_directory_path**  string | Directory path under Vserver for storing file access notifications. File access notifications will be stored in a generated file during the outage time.  The path is the full, user visible path relative to the Vserver root, and it might be crossing junction mount points. |
| **secondary_servers**  list / elements=string | Secondary FPolicy servers. No default value is set for this field. |
| **send_buffer_size**  integer | Send buffer size of connected socket for FPolicy Server. Default value set for this field is 256 kilobytes (256Kb). |
| **ssl_option**  string | SSL option for external communication. No default value is set for this field  Choices:   - `"no_auth"` - `"server_auth"` - `"mutual_auth"` |
| **state**  string | Whether the fPolicy external engine is present or not  Choices:   - `"present"` ← (default) - `"absent"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  Default: `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **vserver**  string / required | the name of the vserver to create the external engine on |

## [Notes](na_ontap_fpolicy_ext_engine_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_fpolicy_ext_engine_module.md#id5)

```yaml+jinja
- name: Create fPolicy external engine
  na_ontap_fpolicy_ext_engine:
    state: present
    vserver: svm1
    name: fpolicy_ext_engine
    port: 8787
    extern_engine_type: asynchronous
    primary_servers: ['10.11.12.13', '10.11.12.14']
    ssl_option: no_auth
    username: "{{ username }}"
    password: "{{ password }}"
    hostname: "{{ hostname }}"

- name: Modify fPolicy external engine
  na_ontap_fpolicy_ext_engine:
    state: present
    vserver: svm1
    name: fpolicy_ext_engine
    port: 7878
    extern_engine_type: synchronous
    primary_servers: ['10.11.12.15', '10.11.12.16']
    ssl_option: server_auth
    username: "{{ username }}"
    password: "{{ password }}"
    hostname: "{{ hostname }}"

- name: Delete fPolicy external engine
  na_ontap_fpolicy_ext_engine:
    state: absent
    vserver: svm1
    name: fpolicy_engine
    username: "{{ username }}"
    password: "{{ password }}"
    hostname: "{{ hostname }}"
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
