---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_system_replacemsg_group module – Configure replacement message groups in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_system_replacemsg_group_module.html
fetched_at: 2026-07-27T17:45:11+00:00
---
# fortinet.fortios.fortios_system_replacemsg_group module – Configure replacement message groups in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_replacemsg_group_module.md#ansible-collections-fortinet-fortios-fortios-system-replacemsg-group-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_replacemsg_group`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_replacemsg_group_module.md#synopsis)
- [Requirements](fortios_system_replacemsg_group_module.md#requirements)
- [Parameters](fortios_system_replacemsg_group_module.md#parameters)
- [Notes](fortios_system_replacemsg_group_module.md#notes)
- [Examples](fortios_system_replacemsg_group_module.md#examples)
- [Return Values](fortios_system_replacemsg_group_module.md#return-values)

## [Synopsis](fortios_system_replacemsg_group_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and replacemsg_group category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_replacemsg_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_system_replacemsg_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **system_replacemsg_group**  dictionary | Configure replacement message groups. |
| **admin**  list / elements=dictionary | Replacement message table entries. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg_type**  string | Message type. |
| **alertmail**  list / elements=dictionary | Replacement message table entries. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg_type**  string | Message type. |
| **auth**  list / elements=dictionary | Replacement message table entries. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg_type**  string | Message type. |
| **automation**  list / elements=dictionary | Replacement message table entries. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  Choices:   - `"none"` - `"text"` - `"html"` |
| **header**  string | Header flag.  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg_type**  string | Message type. |
| **comment**  string | Comment. |
| **custom_message**  list / elements=dictionary | Replacement message table entries. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg_type**  string | Message type. |
| **device_detection_portal**  list / elements=dictionary | Replacement message table entries. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg_type**  string | Message type. |
| **ec**  list / elements=dictionary | Replacement message table entries. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg_type**  string | Message type. |
| **fortiguard_wf**  list / elements=dictionary | Replacement message table entries. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg_type**  string | Message type. |
| **ftp**  list / elements=dictionary | Replacement message table entries. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg_type**  string | Message type. |
| **group_type**  string | Group type.  Choices:   - `"default"` - `"utm"` - `"auth"` - `"ec"` |
| **http**  list / elements=dictionary | Replacement message table entries. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg_type**  string | Message type. |
| **icap**  list / elements=dictionary | Replacement message table entries. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg_type**  string | Message type. |
| **mail**  list / elements=dictionary | Replacement message table entries. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg_type**  string | Message type. |
| **mm1**  list / elements=dictionary | Replacement message table entries. |
| **add_smil**  string | add message encapsulation  Choices:   - `"enable"` - `"disable"` |
| **charset**  string | character encoding used for replacement message  Choices:   - `"utf-8"` - `"us-ascii"` |
| **class**  string | message class  Choices:   - `"not-included"` - `"personal"` - `"advertisement"` - `"information"` - `"automatic"` |
| **format**  string | Format flag.  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **fos_message**  string | message text |
| **from**  string | from address |
| **from_sender**  string | notification message sent from recipient  Choices:   - `"enable"` - `"disable"` |
| **header**  string | Header flag.  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **image**  string | Message string. Source system.replacemsg-image.name. |
| **msg_type**  string | Message type. |
| **priority**  string | message priority  Choices:   - `"not-included"` - `"low"` - `"normal"` - `"high"` |
| **rsp_status**  string | response status code  Choices:   - `"ok"` - `"err-unspecified"` - `"err-srv-denied"` - `"err-msg-fmt-corrupt"` - `"err-snd-addr-unresolv"` - `"err-msg-not-found"` - `"err-net-prob"` - `"err-content-not-accept"` - `"err-unsupp-msg"` |
| **rsp_text**  string | response text |
| **sender_visibility**  string | sender visibility  Choices:   - `"not-specified"` - `"show"` - `"hide"` |
| **smil_part**  string | message encapsulation text |
| **subject**  string | subject text string |
| **mm3**  list / elements=dictionary | Replacement message table entries. |
| **add_html**  string | add message encapsulation  Choices:   - `"enable"` - `"disable"` |
| **charset**  string | character encoding used for replacement message  Choices:   - `"utf-8"` - `"us-ascii"` |
| **format**  string | Format flag.  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **fos_message**  string | message text |
| **from**  string | from address |
| **from_sender**  string | notification message sent from recipient  Choices:   - `"enable"` - `"disable"` |
| **header**  string | Header flag.  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **html_part**  string | message encapsulation text |
| **image**  string | Message string. Source system.replacemsg-image.name. |
| **msg_type**  string | Message type. |
| **priority**  string | message priority  Choices:   - `"not-included"` - `"low"` - `"normal"` - `"high"` |
| **subject**  string | subject text string |
| **mm4**  list / elements=dictionary | Replacement message table entries. |
| **add_smil**  string | add message encapsulation  Choices:   - `"enable"` - `"disable"` |
| **charset**  string | character encoding used for replacement message  Choices:   - `"utf-8"` - `"us-ascii"` |
| **class**  string | message class  Choices:   - `"not-included"` - `"personal"` - `"informational"` - `"advertisement"` - `"auto"` |
| **domain**  string | from address domain |
| **format**  string | Format flag.  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **fos_message**  string | message text |
| **from**  string | from address |
| **from_sender**  string | notification message sent from recipient  Choices:   - `"enable"` - `"disable"` |
| **header**  string | Header flag.  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **image**  string | Message string. Source system.replacemsg-image.name. |
| **msg_type**  string | Message type. |
| **priority**  string | message priority  Choices:   - `"not-included"` - `"low"` - `"normal"` - `"high"` |
| **rsp_status**  string | response status  Choices:   - `"ok"` - `"err-unspecified"` - `"err-srv-denied"` - `"err-msg-fmt-corrupt"` - `"err-snd-addr-unresolv"` - `"err-net-prob"` - `"err-content-not-accept"` - `"err-unsupp-msg"` |
| **smil_part**  string | message encapsulation text |
| **subject**  string | subject text string |
| **mm7**  list / elements=dictionary | Replacement message table entries. |
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
| **mms**  list / elements=dictionary | Replacement message table entries. |
| **buffer**  string | Message string. |
| **charset**  string | character encoding used for replacement message  Choices:   - `"utf-8"` - `"us-ascii"` |
| **format**  string | Format flag.  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **image**  string | Message string. Source system.replacemsg-image.name. |
| **msg_type**  string | Message type. |
| **nac_quar**  list / elements=dictionary | Replacement message table entries. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg_type**  string | Message type. |
| **name**  string / required | Group name. |
| **nntp**  list / elements=dictionary | Replacement message table entries. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg_type**  string | Message type. |
| **spam**  list / elements=dictionary | Replacement message table entries. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg_type**  string | Message type. |
| **sslvpn**  list / elements=dictionary | Replacement message table entries. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg_type**  string | Message type. |
| **traffic_quota**  list / elements=dictionary | Replacement message table entries. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg_type**  string | Message type. |
| **utm**  list / elements=dictionary | Replacement message table entries. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg_type**  string | Message type. |
| **webproxy**  list / elements=dictionary | Replacement message table entries. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg_type**  string | Message type. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_system_replacemsg_group_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_replacemsg_group_module.md#id5)

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
  - name: Configure replacement message groups.
    fortios_system_replacemsg_group:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_replacemsg_group:
        admin:
         -
            buffer: "<your_own_value>"
            format: "none"
            header: "none"
            msg_type: "<your_own_value>"
        alertmail:
         -
            buffer: "<your_own_value>"
            format: "none"
            header: "none"
            msg_type: "<your_own_value>"
        auth:
         -
            buffer: "<your_own_value>"
            format: "none"
            header: "none"
            msg_type: "<your_own_value>"
        automation:
         -
            buffer: "<your_own_value>"
            format: "none"
            header: "none"
            msg_type: "<your_own_value>"
        comment: "Comment."
        custom_message:
         -
            buffer: "<your_own_value>"
            format: "none"
            header: "none"
            msg_type: "<your_own_value>"
        device_detection_portal:
         -
            buffer: "<your_own_value>"
            format: "none"
            header: "none"
            msg_type: "<your_own_value>"
        ec:
         -
            buffer: "<your_own_value>"
            format: "none"
            header: "none"
            msg_type: "<your_own_value>"
        fortiguard_wf:
         -
            buffer: "<your_own_value>"
            format: "none"
            header: "none"
            msg_type: "<your_own_value>"
        ftp:
         -
            buffer: "<your_own_value>"
            format: "none"
            header: "none"
            msg_type: "<your_own_value>"
        group_type: "default"
        http:
         -
            buffer: "<your_own_value>"
            format: "none"
            header: "none"
            msg_type: "<your_own_value>"
        icap:
         -
            buffer: "<your_own_value>"
            format: "none"
            header: "none"
            msg_type: "<your_own_value>"
        mail:
         -
            buffer: "<your_own_value>"
            format: "none"
            header: "none"
            msg_type: "<your_own_value>"
        mm1:
         -
            add_smil: "enable"
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
            rsp_status: "ok"
            rsp_text: "<your_own_value>"
            sender_visibility: "not-specified"
            smil_part: "<your_own_value>"
            subject: "<your_own_value>"
        mm3:
         -
            add_html: "enable"
            charset: "utf-8"
            format: "none"
            fos_message: "<your_own_value>"
            from: "<your_own_value>"
            from_sender: "enable"
            header: "none"
            html_part: "<your_own_value>"
            image: "<your_own_value> (source system.replacemsg-image.name)"
            msg_type: "<your_own_value>"
            priority: "not-included"
            subject: "<your_own_value>"
        mm4:
         -
            add_smil: "enable"
            charset: "utf-8"
            class: "not-included"
            domain: "<your_own_value>"
            format: "none"
            fos_message: "<your_own_value>"
            from: "<your_own_value>"
            from_sender: "enable"
            header: "none"
            image: "<your_own_value> (source system.replacemsg-image.name)"
            msg_type: "<your_own_value>"
            priority: "not-included"
            rsp_status: "ok"
            smil_part: "<your_own_value>"
            subject: "<your_own_value>"
        mm7:
         -
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
        mms:
         -
            buffer: "<your_own_value>"
            charset: "utf-8"
            format: "none"
            header: "none"
            image: "<your_own_value> (source system.replacemsg-image.name)"
            msg_type: "<your_own_value>"
        nac_quar:
         -
            buffer: "<your_own_value>"
            format: "none"
            header: "none"
            msg_type: "<your_own_value>"
        name: "default_name_140"
        nntp:
         -
            buffer: "<your_own_value>"
            format: "none"
            header: "none"
            msg_type: "<your_own_value>"
        spam:
         -
            buffer: "<your_own_value>"
            format: "none"
            header: "none"
            msg_type: "<your_own_value>"
        sslvpn:
         -
            buffer: "<your_own_value>"
            format: "none"
            header: "none"
            msg_type: "<your_own_value>"
        traffic_quota:
         -
            buffer: "<your_own_value>"
            format: "none"
            header: "none"
            msg_type: "<your_own_value>"
        utm:
         -
            buffer: "<your_own_value>"
            format: "none"
            header: "none"
            msg_type: "<your_own_value>"
        webproxy:
         -
            buffer: "<your_own_value>"
            format: "none"
            header: "none"
            msg_type: "<your_own_value>"
```

## [Return Values](fortios_system_replacemsg_group_module.md#id6)

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
