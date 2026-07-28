---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_certificate_ca module – CA certificate in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_certificate_ca_module.html
fetched_at: 2026-07-28T02:23:29+00:00
---
# fortinet.fortios.fortios_certificate_ca module – CA certificate in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortios/) (version 2.3.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_certificate_ca_module.md#ansible-collections-fortinet-fortios-fortios-certificate-ca-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_certificate_ca`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_certificate_ca_module.md#synopsis)
- [Requirements](fortios_certificate_ca_module.md#requirements)
- [Parameters](fortios_certificate_ca_module.md#parameters)
- [Notes](fortios_certificate_ca_module.md#notes)
- [Examples](fortios_certificate_ca_module.md#examples)
- [Return Values](fortios_certificate_ca_module.md#return-values)

## [Synopsis](fortios_certificate_ca_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify certificate feature and ca category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_certificate_ca_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_certificate_ca_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **certificate_ca**  dictionary | CA certificate. |
| **auto_update_days**  integer | Number of days to wait before requesting an updated CA certificate (0 - 4294967295, 0 = disabled). |
| **auto_update_days_warning**  integer | Number of days before an expiry-warning message is generated (0 - 4294967295, 0 = disabled). |
| **ca**  string | CA certificate as a PEM file. |
| **ca_identifier**  string | CA identifier of the SCEP server. |
| **est_url**  string | URL of the EST server. |
| **last_updated**  integer | Time at which CA was last updated. |
| **name**  string / required | Name. |
| **obsolete**  string | Enable/disable this CA as obsoleted.  **Choices:**   - `"disable"` - `"enable"` |
| **range**  string | Either global or VDOM IP address range for the CA certificate.  **Choices:**   - `"global"` - `"vdom"` |
| **scep_url**  string | URL of the SCEP server. |
| **source**  string | CA certificate source type.  **Choices:**   - `"factory"` - `"user"` - `"bundle"` |
| **source_ip**  string | Source IP address for communications to the SCEP server. |
| **ssl_inspection_trusted**  string | Enable/disable this CA as a trusted CA for SSL inspection.  **Choices:**   - `"enable"` - `"disable"` |
| **trusted**  string | Enable/disable as a trusted CA.  **Choices:**   - `"enable"` - `"disable"` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_certificate_ca_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_certificate_ca_module.md#id5)

```yaml+jinja
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: CA certificate.
    fortios_certificate_ca:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      certificate_ca:
        auto_update_days: "0"
        auto_update_days_warning: "0"
        ca: "<your_own_value>"
        ca_identifier:  "myId_6"
        est_url: "<your_own_value>"
        last_updated: "2147483647"
        name: "default_name_9"
        obsolete: "disable"
        range: "global"
        scep_url: "<your_own_value>"
        source: "factory"
        source_ip: "84.230.14.43"
        ssl_inspection_trusted: "enable"
        trusted: "enable"
```

## [Return Values](fortios_certificate_ca_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  **Returned:** always  **Sample:** `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  **Returned:** always  **Sample:** `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  **Returned:** always  **Sample:** `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  **Returned:** success  **Sample:** `"id"` |
| **name**  string | Name of the table used to fulfill the request  **Returned:** always  **Sample:** `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  **Returned:** always  **Sample:** `"webfilter"` |
| **revision**  string | Internal revision number  **Returned:** always  **Sample:** `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  **Returned:** always  **Sample:** `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  **Returned:** always  **Sample:** `"success"` |
| **vdom**  string | Virtual domain used  **Returned:** always  **Sample:** `"root"` |
| **version**  string | Version of the FortiGate  **Returned:** always  **Sample:** `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
- [Homepage](https://www.fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
