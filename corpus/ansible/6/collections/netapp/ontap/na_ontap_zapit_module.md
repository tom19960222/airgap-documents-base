---
collection: ansible
version: "6"
title: "netapp.ontap.na_ontap_zapit module – NetApp ONTAP Run any ZAPI on ONTAP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/ontap/na_ontap_zapit_module.html
fetched_at: 2026-07-28T00:13:35+00:00
---
# netapp.ontap.na_ontap_zapit module – NetApp ONTAP Run any ZAPI on ONTAP

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
> see [Requirements](na_ontap_zapit_module.md#ansible-collections-netapp-ontap-na-ontap-zapit-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_zapit`.

New in netapp.ontap 20.4.0

- [Synopsis](na_ontap_zapit_module.md#synopsis)
- [Requirements](na_ontap_zapit_module.md#requirements)
- [Parameters](na_ontap_zapit_module.md#parameters)
- [Notes](na_ontap_zapit_module.md#notes)
- [Examples](na_ontap_zapit_module.md#examples)
- [Return Values](na_ontap_zapit_module.md#return-values)

## [Synopsis](na_ontap_zapit_module.md#id1)

- Call a ZAPI on ONTAP.
- Cluster ZAPIs are run using a cluster admin account.
- Vserver ZAPIs can be run using a vsadmin account or using vserver tunneling (cluster admin with *vserver option*).
- In case of success, a json dictionary is returned as `response`.
- In case of a ZAPI error, `status`, `errno`, `reason` are set to help with diagnosing the issue,
- and the call is reported as an error (‘failed’).
- Other errors (eg connection issues) are reported as Ansible error.

## [Requirements](na_ontap_zapit_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_zapit_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **feature_flags**  dictionary  added in netapp.ontap 20.5.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  added in netapp.ontap 21.23.0 | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  Choices:   - `false` ← (default) - `true` |
| **key_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client key file. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  Default: `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **vserver**  string | if provided, forces vserver tunneling. username identifies a cluster admin account. |
| **zapi**  dictionary / required | A dictionary for the zapi and arguments.  An XML tag *<tag>value</tag>* is a dictionary with tag as the key.  Value can be another dictionary, a list of dictionaries, a string, or nothing.  eg *<tag/>* is represented as *tag:*  A single zapi can be called at a time. Ansible warns if duplicate keys are found and only uses the last entry. |

## [Notes](na_ontap_zapit_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_zapit_module.md#id5)

```yaml+jinja
-
  name: Ontap ZAPI
  hosts: localhost
  gather_facts: False
  collections:
    - netapp.ontap
  vars:
    login: &login
      hostname: "{{ admin_ip }}"
      username: "{{ admin_username }}"
      password: "{{ admin_password }}"
      https: true
      validate_certs: false
    svm_login: &svm_login
      hostname: "{{ svm_admin_ip }}"
      username: "{{ svm_admin_username }}"
      password: "{{ svm_admin_password }}"
      https: true
      validate_certs: false

  tasks:
    - name: run ontap ZAPI command as cluster admin
      netapp.ontap.na_ontap_zapit:
        <<: *login
        zapi:
          system-get-version:
      register: output
    - debug: var=output

    - name: run ontap ZAPI command as cluster admin
      netapp.ontap.na_ontap_zapit:
        <<: *login
        zapi:
          vserver-get-iter:
      register: output
    - debug: var=output

    - name: run ontap ZAPI command as cluster admin
      netapp.ontap.na_ontap_zapit:
        <<: *login
        zapi:
          vserver-get-iter:
            desired-attributes:
              vserver-info:
                - aggr-list:
                    - aggr-name
                - allowed-protocols:
                    - protocols
                - vserver-aggr-info-list:
                    - vserser-aggr-info
                - uuid
            query:
              vserver-info:
                vserver-name: trident_svm
      register: output
    - debug: var=output

    - name: run ontap ZAPI command as vsadmin
      netapp.ontap.na_ontap_zapit:
        <<: *svm_login
        zapi:
          vserver-get-iter:
            desired-attributes:
              vserver-info:
                - uuid
      register: output
    - debug: var=output

    - name: run ontap ZAPI command as vserver tunneling
      netapp.ontap.na_ontap_zapit:
        <<: *login
        vserver: trident_svm
        zapi:
          vserver-get-iter:
            desired-attributes:
              vserver-info:
                - uuid
      register: output
    - debug: var=output

    - name: run ontap active-directory ZAPI command
      netapp.ontap.na_ontap_zapit:
        <<: *login
        vserver: trident_svm
        zapi:
          active-directory-account-create:
            account-name: testaccount
            admin-username: testuser
            admin-password: testpass
            domain: testdomain
            organizational-unit: testou
      register: output
      ignore_errors: True
    - debug: var=output
```

## [Return Values](na_ontap_zapit_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **errno**  string | If the ZAPI was executed but failed, the error code set by the ZAPI.  Not present if successful, or if the ZAPI call cannot be performed.  Returned: On error |
| **reason**  string | If the ZAPI was executed but failed, the error reason set by the ZAPI.  Not present if successful, or if the ZAPI call cannot be performed.  Returned: On error |
| **response**  dictionary | If successful, a json dictionary representing the data returned by the ZAPI.  If the ZAPI was executed but failed, an empty dictionary.  Not present if the ZAPI call cannot be performed.  Returned: On success |
| **status**  string | If the ZAPI was executed but failed, the status set by the ZAPI.  Not present if successful, or if the ZAPI call cannot be performed.  Returned: On error |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
