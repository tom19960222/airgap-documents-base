---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_icap_profile module – Configure ICAP profiles in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_icap_profile_module.html
fetched_at: 2026-07-28T02:25:37+00:00
---
# fortinet.fortios.fortios_icap_profile module – Configure ICAP profiles in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_icap_profile_module.md#ansible-collections-fortinet-fortios-fortios-icap-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_icap_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_icap_profile_module.md#synopsis)
- [Requirements](fortios_icap_profile_module.md#requirements)
- [Parameters](fortios_icap_profile_module.md#parameters)
- [Notes](fortios_icap_profile_module.md#notes)
- [Examples](fortios_icap_profile_module.md#examples)
- [Return Values](fortios_icap_profile_module.md#return-values)

## [Synopsis](fortios_icap_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify icap feature and profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_icap_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_icap_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **icap_profile**  dictionary | Configure ICAP profiles. |
| **chunk_encap**  string | Enable/disable chunked encapsulation .  **Choices:**   - `"disable"` - `"enable"` |
| **comment**  string | Comment. |
| **extension_feature**  list / elements=string | Enable/disable ICAP extension features.  **Choices:**   - `"scan-progress"` |
| **file_transfer**  list / elements=string | Configure the file transfer protocols to pass transferred files to an ICAP server as REQMOD.  **Choices:**   - `"ssh"` - `"ftp"` |
| **file_transfer_failure**  string | Action to take if the ICAP server cannot be contacted when processing a file transfer.  **Choices:**   - `"error"` - `"bypass"` |
| **file_transfer_path**  string | Path component of the ICAP URI that identifies the file transfer processing service. |
| **file_transfer_server**  string | ICAP server to use for a file transfer. Source icap.server.name icap.server-group.name. |
| **icap_block_log**  string | Enable/disable UTM log when infection found .  **Choices:**   - `"disable"` - `"enable"` |
| **icap_headers**  list / elements=dictionary | Configure ICAP forwarded request headers. |
| **base64_encoding**  string | Enable/disable use of base64 encoding of HTTP content.  **Choices:**   - `"disable"` - `"enable"` |
| **content**  string | HTTP header content. |
| **id**  integer / required | HTTP forwarded header ID. see <a href=’#notes’>Notes</a>. |
| **name**  string | HTTP forwarded header name. |
| **methods**  list / elements=string | The allowed HTTP methods that will be sent to ICAP server for further processing.  **Choices:**   - `"delete"` - `"get"` - `"head"` - `"options"` - `"post"` - `"put"` - `"trace"` - `"connect"` - `"other"` |
| **name**  string / required | ICAP profile name. |
| **preview**  string | Enable/disable preview of data to ICAP server.  **Choices:**   - `"disable"` - `"enable"` |
| **preview_data_length**  integer | Preview data length to be sent to ICAP server. |
| **replacemsg_group**  string | Replacement message group. Source system.replacemsg-group.name. |
| **request**  string | Enable/disable whether an HTTP request is passed to an ICAP server.  **Choices:**   - `"disable"` - `"enable"` |
| **request_failure**  string | Action to take if the ICAP server cannot be contacted when processing an HTTP request.  **Choices:**   - `"error"` - `"bypass"` |
| **request_path**  string | Path component of the ICAP URI that identifies the HTTP request processing service. |
| **request_server**  string | ICAP server to use for an HTTP request. Source icap.server.name icap.server-group.name. |
| **respmod_default_action**  string | Default action to ICAP response modification (respmod) processing.  **Choices:**   - `"forward"` - `"bypass"` |
| **respmod_forward_rules**  list / elements=dictionary | ICAP response mode forward rules. |
| **action**  string | Action to be taken for ICAP server.  **Choices:**   - `"forward"` - `"bypass"` |
| **header_group**  list / elements=dictionary | HTTP header group. |
| **case_sensitivity**  string | Enable/disable case sensitivity when matching header.  **Choices:**   - `"disable"` - `"enable"` |
| **header**  string | HTTP header regular expression. |
| **header_name**  string | HTTP header. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **host**  string | Address object for the host. Source firewall.address.name firewall.addrgrp.name firewall.proxy-address.name. |
| **http_resp_status_code**  list / elements=dictionary | HTTP response status code. |
| **code**  integer / required | HTTP response status code. see <a href=’#notes’>Notes</a>. |
| **name**  string / required | Address name. |
| **response**  string | Enable/disable whether an HTTP response is passed to an ICAP server.  **Choices:**   - `"disable"` - `"enable"` |
| **response_204**  string | Enable/disable allowance of 204 response from ICAP server.  **Choices:**   - `"disable"` - `"enable"` |
| **response_failure**  string | Action to take if the ICAP server cannot be contacted when processing an HTTP response.  **Choices:**   - `"error"` - `"bypass"` |
| **response_path**  string | Path component of the ICAP URI that identifies the HTTP response processing service. |
| **response_req_hdr**  string | Enable/disable addition of req-hdr for ICAP response modification (respmod) processing.  **Choices:**   - `"disable"` - `"enable"` |
| **response_server**  string | ICAP server to use for an HTTP response. Source icap.server.name icap.server-group.name. |
| **scan_progress_interval**  integer | Scan progress interval value. |
| **size_limit_204**  integer | 204 response size limit to be saved by ICAP client in megabytes (1 - 10). |
| **streaming_content_bypass**  string | Enable/disable bypassing of ICAP server for streaming content.  **Choices:**   - `"disable"` - `"enable"` |
| **timeout**  integer | Time (in seconds) that ICAP client waits for the response from ICAP server. |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_icap_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_icap_profile_module.md#id5)

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
  - name: Configure ICAP profiles.
    fortios_icap_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      icap_profile:
        response_204: "disable"
        size_limit_204: "1"
        chunk_encap: "disable"
        comment: "Comment."
        extension_feature: "scan-progress"
        file_transfer: "ssh"
        file_transfer_failure: "error"
        file_transfer_path: "<your_own_value>"
        file_transfer_server: "<your_own_value> (source icap.server.name icap.server-group.name)"
        icap_block_log: "disable"
        icap_headers:
         -
            base64_encoding: "disable"
            content: "<your_own_value>"
            id:  "16"
            name: "default_name_17"
        methods: "delete"
        name: "default_name_19"
        preview: "disable"
        preview_data_length: "0"
        replacemsg_group: "<your_own_value> (source system.replacemsg-group.name)"
        request: "disable"
        request_failure: "error"
        request_path: "<your_own_value>"
        request_server: "<your_own_value> (source icap.server.name icap.server-group.name)"
        respmod_default_action: "forward"
        respmod_forward_rules:
         -
            action: "forward"
            header_group:
             -
                case_sensitivity: "disable"
                header: "<your_own_value>"
                header_name: "<your_own_value>"
                id:  "34"
            host: "myhostname (source firewall.address.name firewall.addrgrp.name firewall.proxy-address.name)"
            http_resp_status_code:
             -
                code: "<you_own_value>"
            name: "default_name_38"
        response: "disable"
        response_failure: "error"
        response_path: "<your_own_value>"
        response_req_hdr: "disable"
        response_server: "<your_own_value> (source icap.server.name icap.server-group.name)"
        scan_progress_interval: "10"
        streaming_content_bypass: "disable"
        timeout: "30"
```

## [Return Values](fortios_icap_profile_module.md#id6)

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
