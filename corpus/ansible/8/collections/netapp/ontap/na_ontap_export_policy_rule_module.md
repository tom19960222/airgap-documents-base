---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_export_policy_rule module – NetApp ONTAP manage export policy rules"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_export_policy_rule_module.html
fetched_at: 2026-07-28T02:41:59+00:00
---
# netapp.ontap.na_ontap_export_policy_rule module – NetApp ONTAP manage export policy rules

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
> see [Requirements](na_ontap_export_policy_rule_module.md#ansible-collections-netapp-ontap-na-ontap-export-policy-rule-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_export_policy_rule`.

New in netapp.ontap 2.6.0

- [Synopsis](na_ontap_export_policy_rule_module.md#synopsis)
- [Requirements](na_ontap_export_policy_rule_module.md#requirements)
- [Parameters](na_ontap_export_policy_rule_module.md#parameters)
- [Notes](na_ontap_export_policy_rule_module.md#notes)
- [Examples](na_ontap_export_policy_rule_module.md#examples)

## [Synopsis](na_ontap_export_policy_rule_module.md#id1)

- Create or delete or modify export rules in ONTAP

## [Requirements](na_ontap_export_policy_rule_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_export_policy_rule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_device_creation**  boolean  *added in netapp.ontap 22.0.0* | Specifies whether or not device creation is allowed.  default is true.  With REST, supported from ONTAP 9.9.1 version.  **Choices:**   - `false` - `true` |
| **allow_suid**  boolean | If ‘true’, NFS server will honor SetUID bits in SETATTR operation. Default value on creation is ‘true’  **Choices:**   - `false` - `true` |
| **anonymous_user_id**  string | User name or ID to which anonymous users are mapped. Default value is ‘65534’. |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **chown_mode**  string  *added in netapp.ontap 22.0.0* | Specifies who is authorized to change the ownership mode of a file.  With REST, supported from ONTAP 9.9.1 version.  **Choices:**   - `"restricted"` - `"unrestricted"` |
| **client_match**  list / elements=string | List of Client Match host names, IP Addresses, Netgroups, or Domains. |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_delete_on_first_match**  boolean  *added in netapp.ontap 21.23.0* | when rule_index is not set, the default is to report an error on multiple matches.  when this option is set, one of the rules with an exact match is deleted when state is absent.  ignored when state is present.  **Choices:**   - `false` ← (default) - `true` |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **from_rule_index**  integer  *added in netapp.ontap 21.20.0* | index of the export policy rule to be re-indexed |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **name**  aliases: policy_name  string / required | The name of the export policy this rule will be added to (or modified, or removed from). |
| **ntfs_unix_security**  string  *added in netapp.ontap 21.18.0* | NTFS export UNIX security options.  With REST, supported from ONTAP 9.9.1 version.  **Choices:**   - `"fail"` - `"ignore"` |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **protocol**  aliases: protocols  list / elements=string | List of Client access protocols.  Default value is set to ‘any’ during create.  **Choices:**   - `"any"` - `"nfs"` - `"nfs3"` - `"nfs4"` - `"cifs"` - `"flexcache"` |
| **ro_rule**  list / elements=string | List of Read only access specifications for the rule  **Choices:**   - `"any"` - `"none"` - `"never"` - `"krb5"` - `"krb5i"` - `"krb5p"` - `"ntlm"` - `"sys"` |
| **rule_index**  integer | Index of the export policy rule.  When rule_index is not set, we try to find a rule with an exact match. If found, no action is taken with state set to present, and the rule is deleted with state set to absent. An error is reported if more than one rule is found.  When rule_index is set and state is present, if a rule cannot be found with this index, we try to find a rule with an exact match and assign the index to this rule if found. If no match is found, a new rule is created.  All attributes that are set are used for an exact match. As a minimum, client_match, ro_rule, and rw_rule are required. |
| **rw_rule**  list / elements=string | List of Read Write access specifications for the rule  **Choices:**   - `"any"` - `"none"` - `"never"` - `"krb5"` - `"krb5i"` - `"krb5p"` - `"ntlm"` - `"sys"` |
| **state**  string | Whether the specified export policy rule should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **super_user_security**  list / elements=string | List of Read Write access specifications for the rule  **Choices:**   - `"any"` - `"none"` - `"never"` - `"krb5"` - `"krb5i"` - `"krb5p"` - `"ntlm"` - `"sys"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **vserver**  string / required | Name of the vserver to use. |

## [Notes](na_ontap_export_policy_rule_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_export_policy_rule_module.md#id5)

```yaml+jinja
- name: Create ExportPolicyRule
  netapp.ontap.na_ontap_export_policy_rule:
    state: present
    name: default123
    rule_index: 100
    vserver: ci_dev
    client_match: 0.0.0.0/0,1.1.1.0/24
    ro_rule: krb5,krb5i
    rw_rule: any
    protocol: nfs,nfs3
    super_user_security: any
    anonymous_user_id: 65534
    allow_suid: true
    ntfs_unix_security: ignore
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Modify ExportPolicyRule
  netapp.ontap.na_ontap_export_policy_rule:
    state: present
    name: default123
    rule_index: 100
    client_match: 0.0.0.0/0
    anonymous_user_id: 65521
    ro_rule: ntlm
    rw_rule: any
    protocol: any
    allow_suid: false
    ntfs_unix_security: fail
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: rename ExportPolicyRule index
  netapp.ontap.na_ontap_export_policy_rule:
    state: present
    name: default123
    from_rule_index: 100
    rule_index: 99
    client_match: 0.0.0.0/0
    anonymous_user_id: 65521
    ro_rule: ntlm
    rw_rule: any
    protocol: any
    allow_suid: false
    ntfs_unix_security: fail
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Delete ExportPolicyRule
  netapp.ontap.na_ontap_export_policy_rule:
    state: absent
    name: default123
    rule_index: 99
    vserver: ci_dev
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
