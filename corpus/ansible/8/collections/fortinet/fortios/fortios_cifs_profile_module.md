---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_cifs_profile module – Configure CIFS profile in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_cifs_profile_module.html
fetched_at: 2026-07-28T02:23:33+00:00
---
# fortinet.fortios.fortios_cifs_profile module – Configure CIFS profile in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_cifs_profile_module.md#ansible-collections-fortinet-fortios-fortios-cifs-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_cifs_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_cifs_profile_module.md#synopsis)
- [Requirements](fortios_cifs_profile_module.md#requirements)
- [Parameters](fortios_cifs_profile_module.md#parameters)
- [Notes](fortios_cifs_profile_module.md#notes)
- [Examples](fortios_cifs_profile_module.md#examples)
- [Return Values](fortios_cifs_profile_module.md#return-values)

## [Synopsis](fortios_cifs_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify cifs feature and profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_cifs_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_cifs_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **cifs_profile**  dictionary | Configure CIFS profile. |
| **domain_controller**  string | Domain for which to decrypt CIFS traffic. Source credential-store.domain-controller.server-name. |
| **file_filter**  dictionary | File filter. |
| **entries**  list / elements=dictionary | File filter entries. |
| **action**  string | Action taken for matched file.  **Choices:**   - `"log"` - `"block"` |
| **comment**  string | Comment. |
| **direction**  string | Match files transmitted in the session”s originating or reply direction.  **Choices:**   - `"incoming"` - `"outgoing"` - `"any"` |
| **file_type**  list / elements=dictionary | Select file type. |
| **name**  string / required | File type name. Source antivirus.filetype.name. |
| **filter**  string / required | Add a file filter. |
| **protocol**  list / elements=string | Protocols to apply with.  **Choices:**   - `"cifs"` |
| **log**  string | Enable/disable file filter logging.  **Choices:**   - `"enable"` - `"disable"` |
| **status**  string | Enable/disable file filter.  **Choices:**   - `"enable"` - `"disable"` |
| **name**  string / required | Profile name. |
| **server_credential_type**  string | CIFS server credential type.  **Choices:**   - `"none"` - `"credential-replication"` - `"credential-keytab"` |
| **server_keytab**  list / elements=dictionary | Server keytab. |
| **keytab**  string | Base64 encoded keytab file containing credential of the server. |
| **password**  string | Password for keytab. |
| **principal**  string / required | Service principal. For example, “[host/cifsserver.example.com@example.com](mailto:host/cifsserver.example.com%40example.com)”. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_cifs_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_cifs_profile_module.md#id5)

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
  - name: Configure CIFS profile.
    fortios_cifs_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      cifs_profile:
        domain_controller: "<your_own_value> (source credential-store.domain-controller.server-name)"
        file_filter:
            entries:
             -
                action: "log"
                comment: "Comment."
                direction: "incoming"
                file_type:
                 -
                    name: "default_name_10 (source antivirus.filetype.name)"
                filter: "<your_own_value>"
                protocol: "cifs"
            log: "enable"
            status: "enable"
        name: "default_name_15"
        server_credential_type: "none"
        server_keytab:
         -
            keytab: "<your_own_value>"
            password: "<your_own_value>"
            principal: "<your_own_value>"
```

## [Return Values](fortios_cifs_profile_module.md#id6)

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
