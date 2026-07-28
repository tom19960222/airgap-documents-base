---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_ssh_filter_profile module – Configure SSH filter profile in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_ssh_filter_profile_module.html
fetched_at: 2026-07-27T17:43:21+00:00
---
# fortinet.fortios.fortios_ssh_filter_profile module – Configure SSH filter profile in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_ssh_filter_profile_module.md#ansible-collections-fortinet-fortios-fortios-ssh-filter-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_ssh_filter_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_ssh_filter_profile_module.md#synopsis)
- [Requirements](fortios_ssh_filter_profile_module.md#requirements)
- [Parameters](fortios_ssh_filter_profile_module.md#parameters)
- [Notes](fortios_ssh_filter_profile_module.md#notes)
- [Examples](fortios_ssh_filter_profile_module.md#examples)
- [Return Values](fortios_ssh_filter_profile_module.md#return-values)

## [Synopsis](fortios_ssh_filter_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify ssh_filter feature and profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_ssh_filter_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_ssh_filter_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **ssh_filter_profile**  dictionary | Configure SSH filter profile. |
| **block**  list / elements=string | SSH blocking options.  Choices:   - `"x11"` - `"shell"` - `"exec"` - `"port-forward"` - `"tun-forward"` - `"sftp"` - `"scp"` - `"unknown"` |
| **default_command_log**  string | Enable/disable logging unmatched shell commands.  Choices:   - `"enable"` - `"disable"` |
| **file_filter**  dictionary | File filter. |
| **entries**  list / elements=dictionary | File filter entries. |
| **action**  string | Action taken for matched file.  Choices:   - `"log"` - `"block"` |
| **comment**  string | Comment. |
| **direction**  string | Match files transmitted in the session”s originating or reply direction.  Choices:   - `"incoming"` - `"outgoing"` - `"any"` |
| **file_type**  list / elements=dictionary | Select file type. |
| **name**  string | File type name. Source antivirus.filetype.name. |
| **filter**  string | Add a file filter. |
| **password_protected**  string | Match password-protected files.  Choices:   - `"yes"` - `"any"` |
| **protocol**  list / elements=string | Protocols to apply with.  Choices:   - `"ssh"` |
| **log**  string | Enable/disable file filter logging.  Choices:   - `"enable"` - `"disable"` |
| **scan_archive_contents**  string | Enable/disable file filter archive contents scan.  Choices:   - `"enable"` - `"disable"` |
| **status**  string | Enable/disable file filter.  Choices:   - `"enable"` - `"disable"` |
| **log**  list / elements=string | SSH logging options.  Choices:   - `"x11"` - `"shell"` - `"exec"` - `"port-forward"` - `"tun-forward"` - `"sftp"` - `"scp"` - `"unknown"` |
| **name**  string / required | SSH filter profile name. |
| **shell_commands**  list / elements=dictionary | SSH command filter. |
| **action**  string | Action to take for SSH shell command matches.  Choices:   - `"block"` - `"allow"` |
| **alert**  string | Enable/disable alert.  Choices:   - `"enable"` - `"disable"` |
| **id**  integer | Id. |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **pattern**  string | SSH shell command pattern. |
| **severity**  string | Log severity.  Choices:   - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **type**  string | Matching type.  Choices:   - `"simple"` - `"regex"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_ssh_filter_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_ssh_filter_profile_module.md#id5)

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
  - name: Configure SSH filter profile.
    fortios_ssh_filter_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      ssh_filter_profile:
        block: "x11"
        default_command_log: "enable"
        file_filter:
            entries:
             -
                action: "log"
                comment: "Comment."
                direction: "incoming"
                file_type:
                 -
                    name: "default_name_11 (source antivirus.filetype.name)"
                filter: "<your_own_value>"
                password_protected: "yes"
                protocol: "ssh"
            log: "enable"
            scan_archive_contents: "enable"
            status: "enable"
        log: "x11"
        name: "default_name_19"
        shell_commands:
         -
            action: "block"
            alert: "enable"
            id:  "23"
            log: "enable"
            pattern: "<your_own_value>"
            severity: "low"
            type: "simple"
```

## [Return Values](fortios_ssh_filter_profile_module.md#id6)

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
