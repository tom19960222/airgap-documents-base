---
collection: ansible
version: "6"
title: "netapp.ontap.na_ontap_wait_for_condition module – NetApp ONTAP wait_for_condition.  Loop over a get status request until a condition is met."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/ontap/na_ontap_wait_for_condition_module.html
fetched_at: 2026-07-28T00:13:33+00:00
---
# netapp.ontap.na_ontap_wait_for_condition module – NetApp ONTAP wait_for_condition. Loop over a get status request until a condition is met.

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
> see [Requirements](na_ontap_wait_for_condition_module.md#ansible-collections-netapp-ontap-na-ontap-wait-for-condition-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_wait_for_condition`.

New in netapp.ontap 20.8.0

- [Synopsis](na_ontap_wait_for_condition_module.md#synopsis)
- [Requirements](na_ontap_wait_for_condition_module.md#requirements)
- [Parameters](na_ontap_wait_for_condition_module.md#parameters)
- [Notes](na_ontap_wait_for_condition_module.md#notes)
- [Examples](na_ontap_wait_for_condition_module.md#examples)
- [Return Values](na_ontap_wait_for_condition_module.md#return-values)

## [Synopsis](na_ontap_wait_for_condition_module.md#id1)

- Loop over an ONTAP get status request until a condition is satisfied.
- Report a timeout error if `timeout` is exceeded while waiting for the condition.

## [Requirements](na_ontap_wait_for_condition_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_wait_for_condition_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  dictionary | a dictionary of custom attributes for the condition.  `sp_upgrade`, `sp_version` require `node`.  `sp_version` requires `expected_version`.  `snapmirror_relationship` requires `destination_path` and `expected_state` or `expected_transfer_state` to match the condition(s). |
| **cert_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **conditions**  list / elements=string / required | one or more conditions to match  `state` and/or `transfer_state` for `snapmirror_relationship`,  `is_in_progress` for `sp_upgrade`,  `firmware_version` for `sp_version`. |
| **feature_flags**  dictionary  added in netapp.ontap 20.5.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  added in netapp.ontap 21.23.0 | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  Choices:   - `false` ← (default) - `true` |
| **key_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client key file. |
| **name**  string / required | The name of the event to check for.  snapmirror_relationship was added in 21.22.0.  Choices:   - `"snapmirror_relationship"` - `"sp_upgrade"` - `"sp_version"` |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **polling_interval**  integer | how ofen to check for the conditions, in seconds.  Default: `5` |
| **state**  string | whether the conditions should be present or absent.  if `present`, the module exits when any of the conditions is observed.  if `absent`, the module exits with success when None of the conditions is observed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | how long to wait for the conditions, in seconds.  Default: `180` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  Default: `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](na_ontap_wait_for_condition_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_wait_for_condition_module.md#id5)

```yaml+jinja
- name: wait for sp_upgrade in progress
  netapp.ontap.na_ontap_wait_for_condition:
    hostname: "{{ ontap_admin_ip }}"
    username: "{{ ontap_admin_username }}"
    password: "{{ ontap_admin_password }}"
    https: true
    validate_certs: no
    name: sp_upgrade
    conditions: is_in_progress
    attributes:
      node: "{{ node }}"
    polling_interval: 30
    timeout: 1800

- name: wait for sp_upgrade not in progress
  netapp.ontap.na_ontap_wait_for_condition:
    hostname: "{{ ontap_admin_ip }}"
    username: "{{ ontap_admin_username }}"
    password: "{{ ontap_admin_password }}"
    https: true
    validate_certs: no
    name: sp_upgrade
    conditions: is_in_progress
    state: absent
    attributes:
      node: "{{ ontap_admin_ip }}"
    polling_interval: 30
    timeout: 1800

- name: wait for sp_version to match 3.9
  netapp.ontap.na_ontap_wait_for_condition:
    hostname: "{{ ontap_admin_ip }}"
    username: "{{ ontap_admin_username }}"
    password: "{{ ontap_admin_password }}"
    https: true
    validate_certs: no
    name: sp_version
    conditions: firmware_version
    state: present
    attributes:
      node: "{{ ontap_admin_ip }}"
      expected_version: 3.9
    polling_interval: 30
    timeout: 1800
```

## [Return Values](na_ontap_wait_for_condition_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **last_state**  string | last observed state for event  Returned: always |
| **states**  string | summarized list of observed states while waiting for completion  reported for success or timeout error  Returned: always |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
