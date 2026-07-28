---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_waf_profile module – Configure Web application firewall configuration in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_waf_profile_module.html
fetched_at: 2026-07-27T17:46:31+00:00
---
# fortinet.fortios.fortios_waf_profile module – Configure Web application firewall configuration in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_waf_profile_module.md#ansible-collections-fortinet-fortios-fortios-waf-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_waf_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_waf_profile_module.md#synopsis)
- [Requirements](fortios_waf_profile_module.md#requirements)
- [Parameters](fortios_waf_profile_module.md#parameters)
- [Notes](fortios_waf_profile_module.md#notes)
- [Examples](fortios_waf_profile_module.md#examples)
- [Return Values](fortios_waf_profile_module.md#return-values)

## [Synopsis](fortios_waf_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify waf feature and profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_waf_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_waf_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |
| **waf_profile**  dictionary | Configure Web application firewall configuration. |
| **address_list**  dictionary | Address block and allow lists. |
| **blocked_address**  list / elements=dictionary | Blocked address. |
| **name**  string | Address name. Source firewall.address.name firewall.addrgrp.name. |
| **blocked_log**  string | Enable/disable logging on blocked addresses.  Choices:   - `"enable"` - `"disable"` |
| **severity**  string | Severity.  Choices:   - `"high"` - `"medium"` - `"low"` |
| **status**  string | Status.  Choices:   - `"enable"` - `"disable"` |
| **trusted_address**  list / elements=dictionary | Trusted address. |
| **name**  string | Address name. Source firewall.address.name firewall.addrgrp.name. |
| **comment**  string | Comment. |
| **constraint**  dictionary | WAF HTTP protocol restrictions. |
| **content_length**  dictionary | HTTP content length in request. |
| **action**  string | Action.  Choices:   - `"allow"` - `"block"` |
| **length**  integer | Length of HTTP content in bytes (0 to 2147483647). |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **severity**  string | Severity.  Choices:   - `"high"` - `"medium"` - `"low"` |
| **status**  string | Enable/disable the constraint.  Choices:   - `"enable"` - `"disable"` |
| **exception**  list / elements=dictionary | HTTP constraint exception. |
| **address**  string | Host address. Source firewall.address.name firewall.addrgrp.name. |
| **content_length**  string | HTTP content length in request.  Choices:   - `"enable"` - `"disable"` |
| **header_length**  string | HTTP header length in request.  Choices:   - `"enable"` - `"disable"` |
| **hostname**  string | Enable/disable hostname check.  Choices:   - `"enable"` - `"disable"` |
| **id**  integer | Exception ID. |
| **line_length**  string | HTTP line length in request.  Choices:   - `"enable"` - `"disable"` |
| **malformed**  string | Enable/disable malformed HTTP request check.  Choices:   - `"enable"` - `"disable"` |
| **max_cookie**  string | Maximum number of cookies in HTTP request.  Choices:   - `"enable"` - `"disable"` |
| **max_header_line**  string | Maximum number of HTTP header line.  Choices:   - `"enable"` - `"disable"` |
| **max_range_segment**  string | Maximum number of range segments in HTTP range line.  Choices:   - `"enable"` - `"disable"` |
| **max_url_param**  string | Maximum number of parameters in URL.  Choices:   - `"enable"` - `"disable"` |
| **method**  string | Enable/disable HTTP method check.  Choices:   - `"enable"` - `"disable"` |
| **param_length**  string | Maximum length of parameter in URL, HTTP POST request or HTTP body.  Choices:   - `"enable"` - `"disable"` |
| **pattern**  string | URL pattern. |
| **regex**  string | Enable/disable regular expression based pattern match.  Choices:   - `"enable"` - `"disable"` |
| **url_param_length**  string | Maximum length of parameter in URL.  Choices:   - `"enable"` - `"disable"` |
| **version**  string | Enable/disable HTTP version check.  Choices:   - `"enable"` - `"disable"` |
| **header_length**  dictionary | HTTP header length in request. |
| **action**  string | Action.  Choices:   - `"allow"` - `"block"` |
| **length**  integer | Length of HTTP header in bytes (0 to 2147483647). |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **severity**  string | Severity.  Choices:   - `"high"` - `"medium"` - `"low"` |
| **status**  string | Enable/disable the constraint.  Choices:   - `"enable"` - `"disable"` |
| **hostname**  dictionary | Enable/disable hostname check. |
| **action**  string | Action.  Choices:   - `"allow"` - `"block"` |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **severity**  string | Severity.  Choices:   - `"high"` - `"medium"` - `"low"` |
| **status**  string | Enable/disable the constraint.  Choices:   - `"enable"` - `"disable"` |
| **line_length**  dictionary | HTTP line length in request. |
| **action**  string | Action.  Choices:   - `"allow"` - `"block"` |
| **length**  integer | Length of HTTP line in bytes (0 to 2147483647). |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **severity**  string | Severity.  Choices:   - `"high"` - `"medium"` - `"low"` |
| **status**  string | Enable/disable the constraint.  Choices:   - `"enable"` - `"disable"` |
| **malformed**  dictionary | Enable/disable malformed HTTP request check. |
| **action**  string | Action.  Choices:   - `"allow"` - `"block"` |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **severity**  string | Severity.  Choices:   - `"high"` - `"medium"` - `"low"` |
| **status**  string | Enable/disable the constraint.  Choices:   - `"enable"` - `"disable"` |
| **max_cookie**  dictionary | Maximum number of cookies in HTTP request. |
| **action**  string | Action.  Choices:   - `"allow"` - `"block"` |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **max_cookie**  integer | Maximum number of cookies in HTTP request (0 to 2147483647). |
| **severity**  string | Severity.  Choices:   - `"high"` - `"medium"` - `"low"` |
| **status**  string | Enable/disable the constraint.  Choices:   - `"enable"` - `"disable"` |
| **max_header_line**  dictionary | Maximum number of HTTP header line. |
| **action**  string | Action.  Choices:   - `"allow"` - `"block"` |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **max_header_line**  integer | Maximum number HTTP header lines (0 to 2147483647). |
| **severity**  string | Severity.  Choices:   - `"high"` - `"medium"` - `"low"` |
| **status**  string | Enable/disable the constraint.  Choices:   - `"enable"` - `"disable"` |
| **max_range_segment**  dictionary | Maximum number of range segments in HTTP range line. |
| **action**  string | Action.  Choices:   - `"allow"` - `"block"` |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **max_range_segment**  integer | Maximum number of range segments in HTTP range line (0 to 2147483647). |
| **severity**  string | Severity.  Choices:   - `"high"` - `"medium"` - `"low"` |
| **status**  string | Enable/disable the constraint.  Choices:   - `"enable"` - `"disable"` |
| **max_url_param**  dictionary | Maximum number of parameters in URL. |
| **action**  string | Action.  Choices:   - `"allow"` - `"block"` |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **max_url_param**  integer | Maximum number of parameters in URL (0 to 2147483647). |
| **severity**  string | Severity.  Choices:   - `"high"` - `"medium"` - `"low"` |
| **status**  string | Enable/disable the constraint.  Choices:   - `"enable"` - `"disable"` |
| **method**  dictionary | Enable/disable HTTP method check. |
| **action**  string | Action.  Choices:   - `"allow"` - `"block"` |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **severity**  string | Severity.  Choices:   - `"high"` - `"medium"` - `"low"` |
| **status**  string | Enable/disable the constraint.  Choices:   - `"enable"` - `"disable"` |
| **param_length**  dictionary | Maximum length of parameter in URL, HTTP POST request or HTTP body. |
| **action**  string | Action.  Choices:   - `"allow"` - `"block"` |
| **length**  integer | Maximum length of parameter in URL, HTTP POST request or HTTP body in bytes (0 to 2147483647). |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **severity**  string | Severity.  Choices:   - `"high"` - `"medium"` - `"low"` |
| **status**  string | Enable/disable the constraint.  Choices:   - `"enable"` - `"disable"` |
| **url_param_length**  dictionary | Maximum length of parameter in URL. |
| **action**  string | Action.  Choices:   - `"allow"` - `"block"` |
| **length**  integer | Maximum length of URL parameter in bytes (0 to 2147483647). |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **severity**  string | Severity.  Choices:   - `"high"` - `"medium"` - `"low"` |
| **status**  string | Enable/disable the constraint.  Choices:   - `"enable"` - `"disable"` |
| **version**  dictionary | Enable/disable HTTP version check. |
| **action**  string | Action.  Choices:   - `"allow"` - `"block"` |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **severity**  string | Severity.  Choices:   - `"high"` - `"medium"` - `"low"` |
| **status**  string | Enable/disable the constraint.  Choices:   - `"enable"` - `"disable"` |
| **extended_log**  string | Enable/disable extended logging.  Choices:   - `"enable"` - `"disable"` |
| **external**  string | Disable/Enable external HTTP Inspection.  Choices:   - `"disable"` - `"enable"` |
| **method**  dictionary | Method restriction. |
| **default_allowed_methods**  list / elements=string | Methods.  Choices:   - `"get"` - `"post"` - `"put"` - `"head"` - `"connect"` - `"trace"` - `"options"` - `"delete"` - `"others"` |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **method_policy**  list / elements=dictionary | HTTP method policy. |
| **address**  string | Host address. Source firewall.address.name firewall.addrgrp.name. |
| **allowed_methods**  list / elements=string | Allowed Methods.  Choices:   - `"get"` - `"post"` - `"put"` - `"head"` - `"connect"` - `"trace"` - `"options"` - `"delete"` - `"others"` |
| **id**  integer | HTTP method policy ID. |
| **pattern**  string | URL pattern. |
| **regex**  string | Enable/disable regular expression based pattern match.  Choices:   - `"enable"` - `"disable"` |
| **severity**  string | Severity.  Choices:   - `"high"` - `"medium"` - `"low"` |
| **status**  string | Status.  Choices:   - `"enable"` - `"disable"` |
| **name**  string / required | WAF Profile name. |
| **signature**  dictionary | WAF signatures. |
| **credit_card_detection_threshold**  integer | The minimum number of Credit cards to detect violation. |
| **custom_signature**  list / elements=dictionary | Custom signature. |
| **action**  string | Action.  Choices:   - `"allow"` - `"block"` - `"erase"` |
| **case_sensitivity**  string | Case sensitivity in pattern.  Choices:   - `"disable"` - `"enable"` |
| **direction**  string | Traffic direction.  Choices:   - `"request"` - `"response"` |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **name**  string | Signature name. |
| **pattern**  string | Match pattern. |
| **severity**  string | Severity.  Choices:   - `"high"` - `"medium"` - `"low"` |
| **status**  string | Status.  Choices:   - `"enable"` - `"disable"` |
| **target**  list / elements=string | Match HTTP target.  Choices:   - `"arg"` - `"arg-name"` - `"req-body"` - `"req-cookie"` - `"req-cookie-name"` - `"req-filename"` - `"req-header"` - `"req-header-name"` - `"req-raw-uri"` - `"req-uri"` - `"resp-body"` - `"resp-hdr"` - `"resp-status"` |
| **disabled_signature**  list / elements=dictionary | Disabled signatures. |
| **id**  integer | Signature ID. Source waf.signature.id. |
| **disabled_sub_class**  list / elements=dictionary | Disabled signature subclasses. |
| **id**  integer | Signature subclass ID. Source waf.sub-class.id. |
| **main_class**  list / elements=dictionary | Main signature class. |
| **action**  string | Action.  Choices:   - `"allow"` - `"block"` - `"erase"` |
| **id**  integer | Main signature class ID. Source waf.main-class.id. |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **severity**  string | Severity.  Choices:   - `"high"` - `"medium"` - `"low"` |
| **status**  string | Status.  Choices:   - `"enable"` - `"disable"` |
| **url_access**  list / elements=dictionary | URL access list. |
| **access_pattern**  list / elements=dictionary | URL access pattern. |
| **id**  integer | URL access pattern ID. |
| **negate**  string | Enable/disable match negation.  Choices:   - `"enable"` - `"disable"` |
| **pattern**  string | URL pattern. |
| **regex**  string | Enable/disable regular expression based pattern match.  Choices:   - `"enable"` - `"disable"` |
| **srcaddr**  string | Source address. Source firewall.address.name firewall.addrgrp.name. |
| **action**  string | Action.  Choices:   - `"bypass"` - `"permit"` - `"block"` |
| **address**  string | Host address. Source firewall.address.name firewall.addrgrp.name. |
| **id**  integer | URL access ID. |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **severity**  string | Severity.  Choices:   - `"high"` - `"medium"` - `"low"` |

## [Notes](fortios_waf_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_waf_profile_module.md#id5)

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
  - name: Configure Web application firewall configuration.
    fortios_waf_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      waf_profile:
        address_list:
            blocked_address:
             -
                name: "default_name_5 (source firewall.address.name firewall.addrgrp.name)"
            blocked_log: "enable"
            severity: "high"
            status: "enable"
            trusted_address:
             -
                name: "default_name_10 (source firewall.address.name firewall.addrgrp.name)"
        comment: "Comment."
        constraint:
            content_length:
                action: "allow"
                length: "67108864"
                log: "enable"
                severity: "high"
                status: "enable"
            exception:
             -
                address: "<your_own_value> (source firewall.address.name firewall.addrgrp.name)"
                content_length: "enable"
                header_length: "enable"
                hostname: "enable"
                id:  "24"
                line_length: "enable"
                malformed: "enable"
                max_cookie: "enable"
                max_header_line: "enable"
                max_range_segment: "enable"
                max_url_param: "enable"
                method: "enable"
                param_length: "enable"
                pattern: "<your_own_value>"
                regex: "enable"
                url_param_length: "enable"
                version: "enable"
            header_length:
                action: "allow"
                length: "8192"
                log: "enable"
                severity: "high"
                status: "enable"
            hostname:
                action: "allow"
                log: "enable"
                severity: "high"
                status: "enable"
            line_length:
                action: "allow"
                length: "1024"
                log: "enable"
                severity: "high"
                status: "enable"
            malformed:
                action: "allow"
                log: "enable"
                severity: "high"
                status: "enable"
            max_cookie:
                action: "allow"
                log: "enable"
                max_cookie: "16"
                severity: "high"
                status: "enable"
            max_header_line:
                action: "allow"
                log: "enable"
                max_header_line: "32"
                severity: "high"
                status: "enable"
            max_range_segment:
                action: "allow"
                log: "enable"
                max_range_segment: "5"
                severity: "high"
                status: "enable"
            max_url_param:
                action: "allow"
                log: "enable"
                max_url_param: "16"
                severity: "high"
                status: "enable"
            method:
                action: "allow"
                log: "enable"
                severity: "high"
                status: "enable"
            param_length:
                action: "allow"
                length: "8192"
                log: "enable"
                severity: "high"
                status: "enable"
            url_param_length:
                action: "allow"
                length: "8192"
                log: "enable"
                severity: "high"
                status: "enable"
            version:
                action: "allow"
                log: "enable"
                severity: "high"
                status: "enable"
        extended_log: "enable"
        external: "disable"
        method:
            default_allowed_methods: "get"
            log: "enable"
            method_policy:
             -
                address: "<your_own_value> (source firewall.address.name firewall.addrgrp.name)"
                allowed_methods: "get"
                id:  "113"
                pattern: "<your_own_value>"
                regex: "enable"
            severity: "high"
            status: "enable"
        name: "default_name_118"
        signature:
            credit_card_detection_threshold: "3"
            custom_signature:
             -
                action: "allow"
                case_sensitivity: "disable"
                direction: "request"
                log: "enable"
                name: "default_name_126"
                pattern: "<your_own_value>"
                severity: "high"
                status: "enable"
                target: "arg"
            disabled_signature:
             -
                id:  "132 (source waf.signature.id)"
            disabled_sub_class:
             -
                id:  "134 (source waf.sub-class.id)"
            main_class:
             -
                action: "allow"
                id:  "137 (source waf.main-class.id)"
                log: "enable"
                severity: "high"
                status: "enable"
        url_access:
         -
            access_pattern:
             -
                id:  "143"
                negate: "enable"
                pattern: "<your_own_value>"
                regex: "enable"
                srcaddr: "<your_own_value> (source firewall.address.name firewall.addrgrp.name)"
            action: "bypass"
            address: "<your_own_value> (source firewall.address.name firewall.addrgrp.name)"
            id:  "150"
            log: "enable"
            severity: "high"
```

## [Return Values](fortios_waf_profile_module.md#id6)

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
