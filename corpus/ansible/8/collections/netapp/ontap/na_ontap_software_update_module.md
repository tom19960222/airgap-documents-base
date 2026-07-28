---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_software_update module – NetApp ONTAP Update Software"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_software_update_module.html
fetched_at: 2026-07-28T02:43:23+00:00
---
# netapp.ontap.na_ontap_software_update module – NetApp ONTAP Update Software

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
> see [Requirements](na_ontap_software_update_module.md#ansible-collections-netapp-ontap-na-ontap-software-update-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_software_update`.

New in netapp.ontap 2.7.0

- [Synopsis](na_ontap_software_update_module.md#synopsis)
- [Requirements](na_ontap_software_update_module.md#requirements)
- [Parameters](na_ontap_software_update_module.md#parameters)
- [Notes](na_ontap_software_update_module.md#notes)
- [Examples](na_ontap_software_update_module.md#examples)
- [Return Values](na_ontap_software_update_module.md#return-values)

## [Synopsis](na_ontap_software_update_module.md#id1)

- Update ONTAP software
- Requires an https connection and is not supported over http

## [Requirements](na_ontap_software_update_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_software_update_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **download_only**  boolean  *added in netapp.ontap 20.4.0* | Allows to download image without update.  **Choices:**   - `false` ← (default) - `true` |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **force_update**  boolean  *added in netapp.ontap 20.11.0* | force an update, even if package_version matches what is reported as installed.  **Choices:**   - `false` ← (default) - `true` |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **ignore_validation_warning**  aliases: skip_warnings  boolean | Allows the update to continue if warnings are encountered during the validation phase.  **Choices:**   - `false` ← (default) - `true` |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **nodes**  aliases: node, nodes_to_update  list / elements=string | List of nodes to be updated, the nodes have to be a part of a HA Pair.  Requires ONTAP 9.9 with REST. |
| **ontapi**  integer | The ontap api version to use |
| **package_url**  string | Specifies the package URL to download the package.  Required when state is present unless the package is already present on disk. |
| **package_version**  string / required | Specifies the package version to update ONTAP software to, or to be deleted. |
| **password**  aliases: pass  string | Password for the specified user. |
| **stabilize_minutes**  integer  *added in netapp.ontap 20.6.0* | Number of minutes that the update should wait after a takeover or giveback is completed.  Requires ONTAP 9.8 with REST. |
| **state**  string | This module downloads and optionally installs ONTAP software on a cluster.  The software package is deleted after a successful installation.  If the software package is already present, it is not downloaded and not replaced.  When state is absent, the package is deleted from disk.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | how long to wait for the update to complete, in seconds.  **Default:** `1800` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_after_download**  boolean  *added in netapp.ontap 21.11.0* | By default validation is not run after download, as it is already done in the update step.  This option is useful when using `download_only`, for instance when updating a MetroCluster system.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](na_ontap_software_update_module.md#id4)

> **Note:**
>
> - ONTAP expects the nodes to be in HA pairs to perform non disruptive updates.
> - In a single node setup, the node is updated, and rebooted.
> - Supports ZAPI and REST.
> - Support check_mode.
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_software_update_module.md#id5)

```yaml+jinja
- name: ONTAP software update
  netapp.ontap.na_ontap_software_update:
    state: present
    nodes: vsim1
    package_url: "{{ url }}"
    package_version: "{{ version_name }}"
    ignore_validation_warning: True
    download_only: True
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
```

## [Return Values](na_ontap_software_update_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **validation_reports**  string | `validation_reports_after_update` as a string, for backward compatibility.  **Returned:** always |
| **validation_reports_after_download**  list / elements=string | List of validation reports, after downloading the software package.  Note that it is different from the validation checks reported after attempting an update.  **Returned:** always |
| **validation_reports_after_updates**  list / elements=string | List of validation reports, after attemting to update the software package.  **Returned:** always |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
