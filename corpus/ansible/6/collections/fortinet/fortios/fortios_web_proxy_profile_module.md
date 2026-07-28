---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_web_proxy_profile module – Configure web proxy profiles in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_web_proxy_profile_module.html
fetched_at: 2026-07-27T17:46:42+00:00
---
# fortinet.fortios.fortios_web_proxy_profile module – Configure web proxy profiles in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_web_proxy_profile_module.md#ansible-collections-fortinet-fortios-fortios-web-proxy-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_web_proxy_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_web_proxy_profile_module.md#synopsis)
- [Requirements](fortios_web_proxy_profile_module.md#requirements)
- [Parameters](fortios_web_proxy_profile_module.md#parameters)
- [Notes](fortios_web_proxy_profile_module.md#notes)
- [Examples](fortios_web_proxy_profile_module.md#examples)
- [Return Values](fortios_web_proxy_profile_module.md#return-values)

## [Synopsis](fortios_web_proxy_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify web_proxy feature and profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_web_proxy_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_web_proxy_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |
| **web_proxy_profile**  dictionary | Configure web proxy profiles. |
| **header_client_ip**  string | Action to take on the HTTP client-IP header in forwarded requests: forwards (pass), adds, or removes the HTTP header.  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **header_front_end_https**  string | Action to take on the HTTP front-end-HTTPS header in forwarded requests: forwards (pass), adds, or removes the HTTP header.  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **header_via_request**  string | Action to take on the HTTP via header in forwarded requests: forwards (pass), adds, or removes the HTTP header.  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **header_via_response**  string | Action to take on the HTTP via header in forwarded responses: forwards (pass), adds, or removes the HTTP header.  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **header_x_authenticated_groups**  string | Action to take on the HTTP x-authenticated-groups header in forwarded requests: forwards (pass), adds, or removes the HTTP header.  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **header_x_authenticated_user**  string | Action to take on the HTTP x-authenticated-user header in forwarded requests: forwards (pass), adds, or removes the HTTP header.  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **header_x_forwarded_client_cert**  string | Action to take on the HTTP x-forwarded-client-cert header in forwarded requests: forwards (pass), adds, or removes the HTTP header.  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **header_x_forwarded_for**  string | Action to take on the HTTP x-forwarded-for header in forwarded requests: forwards (pass), adds, or removes the HTTP header.  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **headers**  list / elements=dictionary | Configure HTTP forwarded requests headers. |
| **action**  string | Action when the HTTP header is forwarded.  Choices:   - `"add-to-request"` - `"add-to-response"` - `"remove-from-request"` - `"remove-from-response"` |
| **add_option**  string | Configure options to append content to existing HTTP header or add new HTTP header.  Choices:   - `"append"` - `"new-on-not-found"` - `"new"` |
| **base64_encoding**  string | Enable/disable use of base64 encoding of HTTP content.  Choices:   - `"disable"` - `"enable"` |
| **content**  string | HTTP header content. |
| **dstaddr**  list / elements=dictionary | Destination address and address group names. |
| **name**  string | Address name. Source firewall.address.name firewall.addrgrp.name. |
| **dstaddr6**  list / elements=dictionary | Destination address and address group names (IPv6). |
| **name**  string | Address name. Source firewall.address6.name firewall.addrgrp6.name. |
| **id**  integer | HTTP forwarded header id. |
| **name**  string | HTTP forwarded header name. |
| **protocol**  list / elements=string | Configure protocol(s) to take add-option action on (HTTP, HTTPS, or both).  Choices:   - `"https"` - `"http"` |
| **log_header_change**  string | Enable/disable logging HTTP header changes.  Choices:   - `"enable"` - `"disable"` |
| **name**  string / required | Profile name. |
| **strip_encoding**  string | Enable/disable stripping unsupported encoding from the request header.  Choices:   - `"enable"` - `"disable"` |

## [Notes](fortios_web_proxy_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_web_proxy_profile_module.md#id5)

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
  - name: Configure web proxy profiles.
    fortios_web_proxy_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      web_proxy_profile:
        header_client_ip: "pass"
        header_front_end_https: "pass"
        header_via_request: "pass"
        header_via_response: "pass"
        header_x_authenticated_groups: "pass"
        header_x_authenticated_user: "pass"
        header_x_forwarded_client_cert: "pass"
        header_x_forwarded_for: "pass"
        headers:
         -
            action: "add-to-request"
            add_option: "append"
            base64_encoding: "disable"
            content: "<your_own_value>"
            dstaddr:
             -
                name: "default_name_17 (source firewall.address.name firewall.addrgrp.name)"
            dstaddr6:
             -
                name: "default_name_19 (source firewall.address6.name firewall.addrgrp6.name)"
            id:  "20"
            name: "default_name_21"
            protocol: "https"
        log_header_change: "enable"
        name: "default_name_24"
        strip_encoding: "enable"
```

## [Return Values](fortios_web_proxy_profile_module.md#id6)

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
