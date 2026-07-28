---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_dlp_fp_doc_source module – Create a DLP fingerprint database by allowing the FortiGate to access a file server containing files from which to create fingerprints in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_dlp_fp_doc_source_module.html
fetched_at: 2026-07-28T02:23:37+00:00
---
# fortinet.fortios.fortios_dlp_fp_doc_source module – Create a DLP fingerprint database by allowing the FortiGate to access a file server containing files from which to create fingerprints in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_dlp_fp_doc_source_module.md#ansible-collections-fortinet-fortios-fortios-dlp-fp-doc-source-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_dlp_fp_doc_source`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_dlp_fp_doc_source_module.md#synopsis)
- [Requirements](fortios_dlp_fp_doc_source_module.md#requirements)
- [Parameters](fortios_dlp_fp_doc_source_module.md#parameters)
- [Notes](fortios_dlp_fp_doc_source_module.md#notes)
- [Examples](fortios_dlp_fp_doc_source_module.md#examples)
- [Return Values](fortios_dlp_fp_doc_source_module.md#return-values)

## [Synopsis](fortios_dlp_fp_doc_source_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify dlp feature and fp_doc_source category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_dlp_fp_doc_source_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_dlp_fp_doc_source_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **dlp_fp_doc_source**  dictionary | Create a DLP fingerprint database by allowing the FortiGate to access a file server containing files from which to create fingerprints. |
| **date**  integer | Day of the month on which to scan the server (1 - 31). |
| **file_path**  string | Path on the server to the fingerprint files (max 119 characters). |
| **file_pattern**  string | Files matching this pattern on the server are fingerprinted. Optionally use the \* and ? wildcards. |
| **keep_modified**  string | Enable so that when a file is changed on the server the FortiGate keeps the old fingerprint and adds a new fingerprint to the database.  **Choices:**   - `"enable"` - `"disable"` |
| **name**  string / required | Name of the DLP fingerprint database. |
| **password**  string | Password required to log into the file server. |
| **period**  string | Frequency for which the FortiGate checks the server for new or changed files.  **Choices:**   - `"none"` - `"daily"` - `"weekly"` - `"monthly"` |
| **remove_deleted**  string | Enable to keep the fingerprint database up to date when a file is deleted from the server.  **Choices:**   - `"enable"` - `"disable"` |
| **scan_on_creation**  string | Enable to keep the fingerprint database up to date when a file is added or changed on the server.  **Choices:**   - `"enable"` - `"disable"` |
| **scan_subdirectories**  string | Enable/disable scanning subdirectories to find files to create fingerprints from.  **Choices:**   - `"enable"` - `"disable"` |
| **sensitivity**  string | Select a sensitivity or threat level for matches with this fingerprint database. Add sensitivities using sensitivity. Source dlp .sensitivity.name. |
| **server**  string | IPv4 or IPv6 address of the server. |
| **server_type**  string | Protocol used to communicate with the file server. Currently only Samba (SMB) servers are supported.  **Choices:**   - `"samba"` |
| **tod_hour**  integer | Hour of the day on which to scan the server (0 - 23). |
| **tod_min**  integer | Minute of the hour on which to scan the server (0 - 59). |
| **username**  string | User name required to log into the file server. |
| **vdom**  string | Select the VDOM that can communicate with the file server.  **Choices:**   - `"mgmt"` - `"current"` |
| **weekday**  string | Day of the week on which to scan the server.  **Choices:**   - `"sunday"` - `"monday"` - `"tuesday"` - `"wednesday"` - `"thursday"` - `"friday"` - `"saturday"` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_dlp_fp_doc_source_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_dlp_fp_doc_source_module.md#id5)

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
  - name: Create a DLP fingerprint database by allowing the FortiGate to access a file server containing files from which to create fingerprints.
    fortios_dlp_fp_doc_source:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      dlp_fp_doc_source:
        date: "1"
        file_path: "<your_own_value>"
        file_pattern: "<your_own_value>"
        keep_modified: "enable"
        name: "default_name_7"
        password: "<your_own_value>"
        period: "none"
        remove_deleted: "enable"
        scan_on_creation: "enable"
        scan_subdirectories: "enable"
        sensitivity: "<your_own_value> (source dlp.sensitivity.name)"
        server: "192.168.100.40"
        server_type: "samba"
        tod_hour: "1"
        tod_min: "0"
        username: "<your_own_value>"
        vdom: "mgmt"
        weekday: "sunday"
```

## [Return Values](fortios_dlp_fp_doc_source_module.md#id6)

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
