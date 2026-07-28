---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_publickey module – NetApp ONTAP publickey configuration"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_publickey_module.html
fetched_at: 2026-07-28T02:42:59+00:00
---
# netapp.ontap.na_ontap_publickey module – NetApp ONTAP publickey configuration

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
> see [Requirements](na_ontap_publickey_module.md#ansible-collections-netapp-ontap-na-ontap-publickey-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_publickey`.

New in netapp.ontap 21.7.0

- [Synopsis](na_ontap_publickey_module.md#synopsis)
- [Requirements](na_ontap_publickey_module.md#requirements)
- [Parameters](na_ontap_publickey_module.md#parameters)
- [Notes](na_ontap_publickey_module.md#notes)
- [Examples](na_ontap_publickey_module.md#examples)
- [Return Values](na_ontap_publickey_module.md#return-values)

## [Synopsis](na_ontap_publickey_module.md#id1)

- Add, modify, or remove publickeys.
- Requires ONTAP 9.7 or later, and only supports REST.

## [Requirements](na_ontap_publickey_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_publickey_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string / required | The name of the user account. |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **comment**  string | Optional comment for the public key. |
| **delete_all**  boolean | If index is not present, with state=absent, delete all public key for this user account.  **Choices:**   - `false` ← (default) - `true` |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **index**  integer | Index number for the public key.  If index is not present, with state=present, the public key is always added, using the next available index.  If index is not present, with state=present, the module is not idempotent.  If index is not present, with state=absent, if only one key is found, it is deleted. Otherwise an error is reported.  See also `delete_all` option. |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **public_key**  string | The public key. |
| **state**  string | Whether the specified publickey should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **vserver**  string | The name of the vserver to use.  Omit this option for cluster scoped user accounts. |

## [Notes](na_ontap_publickey_module.md#id4)

> **Note:**
>
> - This module supports check_mode.
> - This module is not idempotent if index is omitted.
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_publickey_module.md#id5)

```yaml+jinja
- name: Create publickey
  netapp.ontap.na_ontap_publickey:
    state: present
    account: SampleUser
    index: 0
    public_key: "{{ netapp_publickey }}"
    vserver: ansibleVServer
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Delete single publickey
  netapp.ontap.na_ontap_publickey:
    state: absent
    account: SampleUser
    vserver: ansibleVServer
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Modify single publickey
  netapp.ontap.na_ontap_publickey:
    state: present
    account: SampleUser
    comment: ssh key for XXXX
    index: 0
    vserver: ansibleVServer
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
```

## [Return Values](na_ontap_publickey_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cd_action**  string | whether a public key is created or deleted.  **Returned:** success |
| **modify**  dictionary | attributes that were modified if the key already exists.  **Returned:** success |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
