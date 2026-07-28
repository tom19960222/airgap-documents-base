---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_antivirus_quarantine module – Configure quarantine options in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_antivirus_quarantine_module.html
fetched_at: 2026-07-27T17:39:52+00:00
---
# fortinet.fortios.fortios_antivirus_quarantine module – Configure quarantine options in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/fortinet/fortios) (version 2.2.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_antivirus_quarantine_module.md#ansible-collections-fortinet-fortios-fortios-antivirus-quarantine-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_antivirus_quarantine`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_antivirus_quarantine_module.md#synopsis)
- [Requirements](fortios_antivirus_quarantine_module.md#requirements)
- [Parameters](fortios_antivirus_quarantine_module.md#parameters)
- [Notes](fortios_antivirus_quarantine_module.md#notes)
- [Examples](fortios_antivirus_quarantine_module.md#examples)
- [Return Values](fortios_antivirus_quarantine_module.md#return-values)

## [Synopsis](fortios_antivirus_quarantine_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify antivirus feature and quarantine category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_antivirus_quarantine_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_antivirus_quarantine_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **antivirus_quarantine**  dictionary | Configure quarantine options. |
| **agelimit**  integer | Age limit for quarantined files (0 - 479 hours, 0 means forever). |
| **destination**  string | Choose whether to quarantine files to the FortiGate disk or to FortiAnalyzer or to delete them instead of quarantining them.  Choices:   - `"NULL"` - `"disk"` - `"FortiAnalyzer"` |
| **drop_blocked**  list / elements=string | Do not quarantine dropped files found in sessions using the selected protocols. Dropped files are deleted instead of being quarantined.  Choices:   - `"imap"` - `"smtp"` - `"pop3"` - `"http"` - `"ftp"` - `"nntp"` - `"imaps"` - `"smtps"` - `"pop3s"` - `"ftps"` - `"mapi"` - `"cifs"` - `"ssh"` - `"mm1"` - `"mm3"` - `"mm4"` - `"mm7"` |
| **drop_heuristic**  list / elements=string | Do not quarantine files detected by heuristics found in sessions using the selected protocols. Dropped files are deleted instead of being quarantined.  Choices:   - `"imap"` - `"smtp"` - `"pop3"` - `"http"` - `"ftp"` - `"nntp"` - `"imaps"` - `"smtps"` - `"pop3s"` - `"https"` - `"ftps"` - `"mapi"` - `"cifs"` - `"ssh"` - `"mm1"` - `"mm3"` - `"mm4"` - `"mm7"` |
| **drop_infected**  list / elements=string | Do not quarantine infected files found in sessions using the selected protocols. Dropped files are deleted instead of being quarantined.  Choices:   - `"imap"` - `"smtp"` - `"pop3"` - `"http"` - `"ftp"` - `"nntp"` - `"imaps"` - `"smtps"` - `"pop3s"` - `"https"` - `"ftps"` - `"mapi"` - `"cifs"` - `"ssh"` - `"mm1"` - `"mm3"` - `"mm4"` - `"mm7"` |
| **drop_intercepted**  list / elements=string | drop intercepted from a protocol  Choices:   - `"imap"` - `"smtp"` - `"pop3"` - `"http"` - `"ftp"` - `"imaps"` - `"smtps"` - `"pop3s"` - `"https"` - `"ftps"` - `"mapi"` - `"mm1"` - `"mm3"` - `"mm4"` - `"mm7"` |
| **drop_machine_learning**  list / elements=string | Do not quarantine files detected by machine learning found in sessions using the selected protocols. Dropped files are deleted instead of being quarantined.  Choices:   - `"imap"` - `"smtp"` - `"pop3"` - `"http"` - `"ftp"` - `"nntp"` - `"imaps"` - `"smtps"` - `"pop3s"` - `"https"` - `"ftps"` - `"mapi"` - `"cifs"` - `"ssh"` |
| **lowspace**  string | Select the method for handling additional files when running low on disk space.  Choices:   - `"drop-new"` - `"ovrw-old"` |
| **maxfilesize**  integer | Maximum file size to quarantine (0 - 500 Mbytes, 0 means unlimited). |
| **quarantine_quota**  integer | The amount of disk space to reserve for quarantining files (0 - 4294967295 Mbytes, depends on disk space). |
| **store_blocked**  list / elements=string | Quarantine blocked files found in sessions using the selected protocols.  Choices:   - `"imap"` - `"smtp"` - `"pop3"` - `"http"` - `"ftp"` - `"nntp"` - `"imaps"` - `"smtps"` - `"pop3s"` - `"ftps"` - `"mapi"` - `"cifs"` - `"ssh"` - `"mm1"` - `"mm3"` - `"mm4"` - `"mm7"` |
| **store_heuristic**  list / elements=string | Quarantine files detected by heuristics found in sessions using the selected protocols.  Choices:   - `"imap"` - `"smtp"` - `"pop3"` - `"http"` - `"ftp"` - `"nntp"` - `"imaps"` - `"smtps"` - `"pop3s"` - `"https"` - `"ftps"` - `"mapi"` - `"cifs"` - `"ssh"` - `"mm1"` - `"mm3"` - `"mm4"` - `"mm7"` |
| **store_infected**  list / elements=string | Quarantine infected files found in sessions using the selected protocols.  Choices:   - `"imap"` - `"smtp"` - `"pop3"` - `"http"` - `"ftp"` - `"nntp"` - `"imaps"` - `"smtps"` - `"pop3s"` - `"https"` - `"ftps"` - `"mapi"` - `"cifs"` - `"ssh"` - `"mm1"` - `"mm3"` - `"mm4"` - `"mm7"` |
| **store_intercepted**  list / elements=string | quarantine intercepted from a protocol  Choices:   - `"imap"` - `"smtp"` - `"pop3"` - `"http"` - `"ftp"` - `"imaps"` - `"smtps"` - `"pop3s"` - `"https"` - `"ftps"` - `"mapi"` - `"mm1"` - `"mm3"` - `"mm4"` - `"mm7"` |
| **store_machine_learning**  list / elements=string | Quarantine files detected by machine learning found in sessions using the selected protocols.  Choices:   - `"imap"` - `"smtp"` - `"pop3"` - `"http"` - `"ftp"` - `"nntp"` - `"imaps"` - `"smtps"` - `"pop3s"` - `"https"` - `"ftps"` - `"mapi"` - `"cifs"` - `"ssh"` |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_antivirus_quarantine_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_antivirus_quarantine_module.md#id5)

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
  - name: Configure quarantine options.
    fortios_antivirus_quarantine:
      vdom:  "{{ vdom }}"
      antivirus_quarantine:
        agelimit: "0"
        destination: "NULL"
        drop_blocked: "imap"
        drop_heuristic: "imap"
        drop_infected: "imap"
        drop_intercepted: "imap"
        drop_machine_learning: "imap"
        lowspace: "drop-new"
        maxfilesize: "0"
        quarantine_quota: "0"
        store_blocked: "imap"
        store_heuristic: "imap"
        store_infected: "imap"
        store_intercepted: "imap"
        store_machine_learning: "imap"
```

## [Return Values](fortios_antivirus_quarantine_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  Returned: always  Sample: `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  Returned: always  Sample: `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  Returned: always  Sample: `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  Returned: success  Sample: `"id"` |
| **name**  string | Name of the table used to fulfill the request  Returned: always  Sample: `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  Returned: always  Sample: `"webfilter"` |
| **revision**  string | Internal revision number  Returned: always  Sample: `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  Returned: always  Sample: `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  Returned: always  Sample: `"success"` |
| **vdom**  string | Virtual domain used  Returned: always  Sample: `"root"` |
| **version**  string | Version of the FortiGate  Returned: always  Sample: `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
[Homepage](https://www.fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
