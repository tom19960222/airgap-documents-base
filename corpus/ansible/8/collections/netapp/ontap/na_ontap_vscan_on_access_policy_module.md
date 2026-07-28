---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_vscan_on_access_policy module – NetApp ONTAP Vscan on access policy configuration."
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_vscan_on_access_policy_module.html
fetched_at: 2026-07-28T02:43:38+00:00
---
# netapp.ontap.na_ontap_vscan_on_access_policy module – NetApp ONTAP Vscan on access policy configuration.

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
> see [Requirements](na_ontap_vscan_on_access_policy_module.md#ansible-collections-netapp-ontap-na-ontap-vscan-on-access-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_vscan_on_access_policy`.

New in netapp.ontap 2.8.0

- [Synopsis](na_ontap_vscan_on_access_policy_module.md#synopsis)
- [Requirements](na_ontap_vscan_on_access_policy_module.md#requirements)
- [Parameters](na_ontap_vscan_on_access_policy_module.md#parameters)
- [Notes](na_ontap_vscan_on_access_policy_module.md#notes)
- [Examples](na_ontap_vscan_on_access_policy_module.md#examples)

## [Synopsis](na_ontap_vscan_on_access_policy_module.md#id1)

- Configure on access policy for Vscan (virus scan)

## [Requirements](na_ontap_vscan_on_access_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_vscan_on_access_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **file_ext_to_exclude**  list / elements=string | File extensions for which On-Access scanning must not be performed. |
| **file_ext_to_include**  list / elements=string | File extensions for which On-Access scanning is considered. The default value is ‘\*’, which means that all files are considered for scanning except  those which are excluded from scanning. |
| **filters**  list / elements=string | A list of filters which can be used to define the scope of the On-Access policy more precisely. The filters can be added in any order. Possible values  scan_ro_volume Enable scans for read-only volume,  scan_execute_access Scan only files opened with execute-access (CIFS only).  deprecated with REST, use `scan_readonly_volumes` or `only_execute_access`. |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **is_scan_mandatory**  boolean | Specifies whether access to a file is allowed if there are no external virus-scanning servers available for virus scanning.  If not specified, default value is False in ZAPI.  **Choices:**   - `false` - `true` |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **max_file_size**  integer | Max file-size (in bytes) allowed for scanning. The default value of 2147483648 (2GB) is taken if not provided at the time of creating a policy. |
| **only_execute_access**  boolean  *added in netapp.ontap 21.20.0* | Scan only files opened with execute-access.  If not specified, default value is False in creating policy.  **Choices:**   - `false` - `true` |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **paths_to_exclude**  list / elements=string | File paths for which On-Access scanning must not be performed. |
| **policy_name**  string / required | The name of the policy |
| **policy_status**  boolean  *added in netapp.ontap 20.8.0* | Status for the created policy  **Choices:**   - `false` - `true` |
| **scan_files_with_no_ext**  boolean | Specifies whether files without any extension are considered for scanning or not.  If not specified, default value is True in ZAPI.  **Choices:**   - `false` - `true` |
| **scan_readonly_volumes**  boolean  *added in netapp.ontap 21.20.0* | Specifies whether or not read-only volume can be scanned.  If not specified, default value is False in creating policy.  **Choices:**   - `false` - `true` |
| **state**  string | Whether a Vscan on Access policy is present or not  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **vserver**  string / required | the name of the data vserver to use. |

## [Notes](na_ontap_vscan_on_access_policy_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_vscan_on_access_policy_module.md#id5)

```yaml+jinja
- name: Create Vscan On Access Policy
  netapp.ontap.na_ontap_vscan_on_access_policy:
    state: present
    username: '{{ netapp_username }}'
    password: '{{ netapp_password }}'
    hostname: '{{ netapp_hostname }}'
    vserver: carchi-vsim2
    policy_name: carchi_policy
    file_ext_to_exclude: ['exe', 'yml']
- name: Create Vscan On Access Policy with Policy Status enabled
  netapp.ontap.na_ontap_vscan_on_access_policy:
    state: present
    username: '{{ netapp_username }}'
    password: '{{ netapp_password }}'
    hostname: '{{ netapp_hostname }}'
    vserver: carchi-vsim2
    policy_name: carchi_policy
    file_ext_to_exclude: ['exe', 'yml']
    policy_status: True
- name: modify Vscan on Access Policy
  netapp.ontap.na_ontap_vscan_on_access_policy:
    state: present
    username: '{{ netapp_username }}'
    password: '{{ netapp_password }}'
    hostname: '{{ netapp_hostname }}'
    vserver: carchi-vsim2
    policy_name: carchi_policy
    file_ext_to_exclude: ['exe', 'yml', 'py']
- name: Delete On Access Policy
  netapp.ontap.na_ontap_vscan_on_access_policy:
    state: absent
    username: '{{ netapp_username }}'
    password: '{{ netapp_password }}'
    hostname: '{{ netapp_hostname }}'
    vserver: carchi-vsim2
    policy_name: carchi_policy
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
