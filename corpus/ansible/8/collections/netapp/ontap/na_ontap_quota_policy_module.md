---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_quota_policy module – NetApp Ontap create, assign, rename or delete quota policy"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_quota_policy_module.html
fetched_at: 2026-07-28T02:43:02+00:00
---
# netapp.ontap.na_ontap_quota_policy module – NetApp Ontap create, assign, rename or delete quota policy

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
> see [Requirements](na_ontap_quota_policy_module.md#ansible-collections-netapp-ontap-na-ontap-quota-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_quota_policy`.

New in netapp.ontap 19.11.0

- [Synopsis](na_ontap_quota_policy_module.md#synopsis)
- [Requirements](na_ontap_quota_policy_module.md#requirements)
- [Parameters](na_ontap_quota_policy_module.md#parameters)
- [Notes](na_ontap_quota_policy_module.md#notes)
- [Examples](na_ontap_quota_policy_module.md#examples)

## [Synopsis](na_ontap_quota_policy_module.md#id1)

- Create, assign, rename or delete the quota policy
- This module only supports ZAPI and is deprecated.
- The final version of ONTAP to support ZAPI is 9.12.1.

## [Requirements](na_ontap_quota_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_quota_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auto_assign**  boolean  *added in netapp.ontap 20.12.0* | when true, assign the policy to the vserver, whether it is newly created, renamed, or already exists.  when true, the policy identified by name replaces the already assigned policy.  when false, the policy is created if it does not already exist but is not assigned.  **Choices:**   - `false` - `true` ← (default) |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **from_name**  string | Name of the existing quota policy to be renamed to name. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **name**  string / required | Specifies the quota policy name to create or rename to. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **state**  string | Whether the specified quota policy should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **use_rest**  string | This module only support ZAPI and will can not be swtich to REST  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will always use ZAPI.  **Default:** `"never"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **vserver**  string / required | Specifies the vserver for the quota policy. |

## [Notes](na_ontap_quota_policy_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_quota_policy_module.md#id5)

```yaml+jinja
- name: Create quota policy
  na_ontap_quota_policy:
    state: present
    vserver: SVM1
    name: ansible_policy
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Rename quota policy
  na_ontap_quota_policy:
    state: present
    vserver: SVM1
    name: new_ansible
    from_name: ansible
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Delete quota policy
  na_ontap_quota_policy:
    state: absent
    vserver: SVM1
    name: ansible_policy
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
