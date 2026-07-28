---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_system_replacemsg_mm7 module – Replacement messages in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_system_replacemsg_mm7_module.html
fetched_at: 2026-07-27T17:45:16+00:00
---
# fortinet.fortios.fortios_system_replacemsg_mm7 module – Replacement messages in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_replacemsg_mm7_module.md#ansible-collections-fortinet-fortios-fortios-system-replacemsg-mm7-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_replacemsg_mm7`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_replacemsg_mm7_module.md#synopsis)
- [Requirements](fortios_system_replacemsg_mm7_module.md#requirements)
- [Parameters](fortios_system_replacemsg_mm7_module.md#parameters)
- [Notes](fortios_system_replacemsg_mm7_module.md#notes)
- [Examples](fortios_system_replacemsg_mm7_module.md#examples)
- [Return Values](fortios_system_replacemsg_mm7_module.md#return-values)

## [Synopsis](fortios_system_replacemsg_mm7_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system_replacemsg feature and mm7 category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_replacemsg_mm7_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_system_replacemsg_mm7_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **system_replacemsg_mm7**  dictionary | Replacement messages. |
| **add_smil**  string | add message encapsulation  Choices:   - `"enable"` - `"disable"` |
| **addr_type**  string | from address type  Choices:   - `"rfc2822-addr"` - `"number"` - `"short-code"` |
| **allow_content_adaptation**  string | allow content adaptations  Choices:   - `"enable"` - `"disable"` |
| **charset**  string | character encoding used for replacement message  Choices:   - `"utf-8"` - `"us-ascii"` |
| **class**  string | message class  Choices:   - `"not-included"` - `"personal"` - `"informational"` - `"advertisement"` - `"auto"` |
| **format**  string | Format flag.  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **fos_message**  string | message text |
| **from**  string | from address |
| **from_sender**  string | notification message sent from recipient  Choices:   - `"enable"` - `"disable"` |
| **header**  string | Header flag.  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **image**  string | Message string. Source system.replacemsg-image.name. |
| **msg_type**  string | Message type. |
| **priority**  string | message priority  Choices:   - `"not-included"` - `"low"` - `"normal"` - `"high"` |
| **rsp_status**  string | response status  Choices:   - `"success"` - `"partial-success"` - `"client-err"` - `"oper-restrict"` - `"addr-err"` - `"addr-not-found"` - `"content-refused"` - `"msg-id-not-found"` - `"link-id-not-found"` - `"msg-fmt-corrupt"` - `"app-id-not-found"` - `"repl-app-id-not-found"` - `"srv-err"` - `"not-possible"` - `"msg-rejected"` - `"multiple-addr-not-supp"` - `"app-addr-not-supp"` - `"gen-service-err"` - `"improper-ident"` - `"unsupp-ver"` - `"unsupp-oper"` - `"validation-err"` - `"service-err"` - `"service-unavail"` - `"service-denied"` - `"app-denied"` |
| **smil_part**  string | message encapsulation text |
| **subject**  string | subject text string |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_system_replacemsg_mm7_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_replacemsg_mm7_module.md#id5)

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
  - name: Replacement messages.
    fortios_system_replacemsg_mm7:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_replacemsg_mm7:
        add_smil: "enable"
        addr_type: "rfc2822-addr"
        allow_content_adaptation: "enable"
        charset: "utf-8"
        class: "not-included"
        format: "none"
        fos_message: "<your_own_value>"
        from: "<your_own_value>"
        from_sender: "enable"
        header: "none"
        image: "<your_own_value> (source system.replacemsg-image.name)"
        msg_type: "<your_own_value>"
        priority: "not-included"
        rsp_status: "success"
        smil_part: "<your_own_value>"
        subject: "<your_own_value>"
```

## [Return Values](fortios_system_replacemsg_mm7_module.md#id6)

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
