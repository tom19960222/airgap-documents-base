---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_application_name module – Configure application signatures in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_application_name_module.html
fetched_at: 2026-07-28T02:23:23+00:00
---
# fortinet.fortios.fortios_application_name module – Configure application signatures in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_application_name_module.md#ansible-collections-fortinet-fortios-fortios-application-name-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_application_name`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_application_name_module.md#synopsis)
- [Requirements](fortios_application_name_module.md#requirements)
- [Parameters](fortios_application_name_module.md#parameters)
- [Notes](fortios_application_name_module.md#notes)
- [Examples](fortios_application_name_module.md#examples)
- [Return Values](fortios_application_name_module.md#return-values)

## [Synopsis](fortios_application_name_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify application feature and name category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_application_name_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_application_name_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **application_name**  dictionary | Configure application signatures. |
| **behavior**  string | Application behavior. |
| **category**  integer | Application category ID. |
| **id**  integer | Application ID. |
| **metadata**  list / elements=dictionary | Meta data. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **metaid**  integer | Meta ID. |
| **valueid**  integer | Value ID. |
| **name**  string / required | Application name. |
| **parameter**  string | Application parameter name. |
| **parameters**  list / elements=dictionary | Application parameters. |
| **default_value**  string | Parameter default value. |
| **name**  string / required | Parameter name. |
| **popularity**  integer | Application popularity. |
| **protocol**  string | Application protocol. |
| **risk**  integer | Application risk. |
| **sub_category**  integer | Application sub-category ID. |
| **technology**  string | Application technology. |
| **vendor**  string | Application vendor. |
| **weight**  integer | Application weight. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_application_name_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_application_name_module.md#id5)

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
  - name: Configure application signatures.
    fortios_application_name:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      application_name:
        behavior: "<your_own_value>"
        category: "0"
        id:  "5"
        metadata:
         -
            id:  "7"
            metaid: "0"
            valueid: "0"
        name: "default_name_10"
        parameter: "<your_own_value>"
        parameters:
         -
            default_value: "<your_own_value>"
            name: "default_name_14"
        popularity: "0"
        protocol: "<your_own_value>"
        risk: "0"
        sub_category: "127"
        technology: "<your_own_value>"
        vendor: "<your_own_value>"
        weight: "0"
```

## [Return Values](fortios_application_name_module.md#id6)

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
