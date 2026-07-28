---
collection: ansible
version: "8"
title: "community.fortios.fmgr_secprof_waf module – FortiManager web application firewall security profile"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/fortios/fmgr_secprof_waf_module.html
fetched_at: 2026-07-28T01:44:25+00:00
---
# community.fortios.fmgr_secprof_waf module – FortiManager web application firewall security profile

> **Note:**
>
> This module is part of the [community.fortios collection](https://galaxy.ansible.com/ui/repo/published/community/fortios/) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.fortios`.
>
> To use it in a playbook, specify: `community.fortios.fmgr_secprof_waf`.

- [Synopsis](fmgr_secprof_waf_module.md#synopsis)
- [Parameters](fmgr_secprof_waf_module.md#parameters)
- [Notes](fmgr_secprof_waf_module.md#notes)
- [Examples](fmgr_secprof_waf_module.md#examples)
- [Return Values](fmgr_secprof_waf_module.md#return-values)

## [Synopsis](fmgr_secprof_waf_module.md#id1)

- Manage web application firewall security profiles for FGTs via FMG

## [Parameters](fmgr_secprof_waf_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address_list**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **address_list_blocked_address**  string | Blocked address. |
| **address_list_blocked_log**  string | Enable/disable logging on blocked addresses.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **address_list_severity**  string | Severity.  choice | low | Low severity.  choice | medium | Medium severity.  choice | high | High severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **address_list_status**  string | Status.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **address_list_trusted_address**  string | Trusted address. |
| **adom**  string | The ADOM the configuration should belong to.  **Default:** `"root"` |
| **comment**  string | Comment. |
| **constraint**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **constraint_content_length_action**  string | Action.  choice | allow | Allow.  choice | block | Block.  **Choices:**   - `"allow"` - `"block"` |
| **constraint_content_length_length**  string | Length of HTTP content in bytes (0 to 2147483647). |
| **constraint_content_length_log**  string | Enable/disable logging.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_content_length_severity**  string | Severity.  choice | low | Low severity.  choice | medium | Medium severity.  choice | high | High severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **constraint_content_length_status**  string | Enable/disable the constraint.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_exception_address**  string | Host address. |
| **constraint_exception_content_length**  string | HTTP content length in request.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_exception_header_length**  string | HTTP header length in request.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_exception_hostname**  string | Enable/disable hostname check.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_exception_line_length**  string | HTTP line length in request.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_exception_malformed**  string | Enable/disable malformed HTTP request check.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_exception_max_cookie**  string | Maximum number of cookies in HTTP request.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_exception_max_header_line**  string | Maximum number of HTTP header line.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_exception_max_range_segment**  string | Maximum number of range segments in HTTP range line.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_exception_max_url_param**  string | Maximum number of parameters in URL.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_exception_method**  string | Enable/disable HTTP method check.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_exception_param_length**  string | Maximum length of parameter in URL, HTTP POST request or HTTP body.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_exception_pattern**  string | URL pattern. |
| **constraint_exception_regex**  string | Enable/disable regular expression based pattern match.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_exception_url_param_length**  string | Maximum length of parameter in URL.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_exception_version**  string | Enable/disable HTTP version check.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_header_length_action**  string | Action.  choice | allow | Allow.  choice | block | Block.  **Choices:**   - `"allow"` - `"block"` |
| **constraint_header_length_length**  string | Length of HTTP header in bytes (0 to 2147483647). |
| **constraint_header_length_log**  string | Enable/disable logging.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_header_length_severity**  string | Severity.  choice | low | Low severity.  choice | medium | Medium severity.  choice | high | High severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **constraint_header_length_status**  string | Enable/disable the constraint.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_hostname_action**  string | Action for a hostname constraint.  choice | allow | Allow.  choice | block | Block.  **Choices:**   - `"allow"` - `"block"` |
| **constraint_hostname_log**  string | Enable/disable logging.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_hostname_severity**  string | Severity.  choice | low | Low severity.  choice | medium | Medium severity.  choice | high | High severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **constraint_hostname_status**  string | Enable/disable the constraint.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_line_length_action**  string | Action.  choice | allow | Allow.  choice | block | Block.  **Choices:**   - `"allow"` - `"block"` |
| **constraint_line_length_length**  string | Length of HTTP line in bytes (0 to 2147483647). |
| **constraint_line_length_log**  string | Enable/disable logging.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_line_length_severity**  string | Severity.  choice | low | Low severity.  choice | medium | Medium severity.  choice | high | High severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **constraint_line_length_status**  string | Enable/disable the constraint.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_malformed_action**  string | Action.  choice | allow | Allow.  choice | block | Block.  **Choices:**   - `"allow"` - `"block"` |
| **constraint_malformed_log**  string | Enable/disable logging.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_malformed_severity**  string | Severity.  choice | low | Low severity.  choice | medium | Medium severity.  choice | high | High severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **constraint_malformed_status**  string | Enable/disable the constraint.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_max_cookie_action**  string | Action.  choice | allow | Allow.  choice | block | Block.  **Choices:**   - `"allow"` - `"block"` |
| **constraint_max_cookie_log**  string | Enable/disable logging.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_max_cookie_max_cookie**  string | Maximum number of cookies in HTTP request (0 to 2147483647). |
| **constraint_max_cookie_severity**  string | Severity.  choice | low | Low severity.  choice | medium | Medium severity.  choice | high | High severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **constraint_max_cookie_status**  string | Enable/disable the constraint.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_max_header_line_action**  string | Action.  choice | allow | Allow.  choice | block | Block.  **Choices:**   - `"allow"` - `"block"` |
| **constraint_max_header_line_log**  string | Enable/disable logging.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_max_header_line_max_header_line**  string | Maximum number HTTP header lines (0 to 2147483647). |
| **constraint_max_header_line_severity**  string | Severity.  choice | low | Low severity.  choice | medium | Medium severity.  choice | high | High severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **constraint_max_header_line_status**  string | Enable/disable the constraint.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_max_range_segment_action**  string | Action.  choice | allow | Allow.  choice | block | Block.  **Choices:**   - `"allow"` - `"block"` |
| **constraint_max_range_segment_log**  string | Enable/disable logging.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_max_range_segment_max_range_segment**  string | Maximum number of range segments in HTTP range line (0 to 2147483647). |
| **constraint_max_range_segment_severity**  string | Severity.  choice | low | Low severity.  choice | medium | Medium severity.  choice | high | High severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **constraint_max_range_segment_status**  string | Enable/disable the constraint.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_max_url_param_action**  string | Action.  choice | allow | Allow.  choice | block | Block.  **Choices:**   - `"allow"` - `"block"` |
| **constraint_max_url_param_log**  string | Enable/disable logging.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_max_url_param_max_url_param**  string | Maximum number of parameters in URL (0 to 2147483647). |
| **constraint_max_url_param_severity**  string | Severity.  choice | low | Low severity.  choice | medium | Medium severity.  choice | high | High severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **constraint_max_url_param_status**  string | Enable/disable the constraint.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_method_action**  string | Action.  choice | allow | Allow.  choice | block | Block.  **Choices:**   - `"allow"` - `"block"` |
| **constraint_method_log**  string | Enable/disable logging.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_method_severity**  string | Severity.  choice | low | Low severity.  choice | medium | Medium severity.  choice | high | High severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **constraint_method_status**  string | Enable/disable the constraint.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_param_length_action**  string | Action.  choice | allow | Allow.  choice | block | Block.  **Choices:**   - `"allow"` - `"block"` |
| **constraint_param_length_length**  string | Maximum length of parameter in URL, HTTP POST request or HTTP body in bytes (0 to 2147483647). |
| **constraint_param_length_log**  string | Enable/disable logging.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_param_length_severity**  string | Severity.  choice | low | Low severity.  choice | medium | Medium severity.  choice | high | High severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **constraint_param_length_status**  string | Enable/disable the constraint.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_url_param_length_action**  string | Action.  choice | allow | Allow.  choice | block | Block.  **Choices:**   - `"allow"` - `"block"` |
| **constraint_url_param_length_length**  string | Maximum length of URL parameter in bytes (0 to 2147483647). |
| **constraint_url_param_length_log**  string | Enable/disable logging.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_url_param_length_severity**  string | Severity.  choice | low | Low severity.  choice | medium | Medium severity.  choice | high | High severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **constraint_url_param_length_status**  string | Enable/disable the constraint.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_version_action**  string | Action.  choice | allow | Allow.  choice | block | Block.  **Choices:**   - `"allow"` - `"block"` |
| **constraint_version_log**  string | Enable/disable logging.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **constraint_version_severity**  string | Severity.  choice | low | Low severity.  choice | medium | Medium severity.  choice | high | High severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **constraint_version_status**  string | Enable/disable the constraint.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **extended_log**  string | Enable/disable extended logging.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **external**  string | Disable/Enable external HTTP Inspection.  choice | disable | Disable external inspection.  choice | enable | Enable external inspection.  **Choices:**   - `"disable"` - `"enable"` |
| **method**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **method_default_allowed_methods**  string | Methods.  FLAG Based Options. Specify multiple in list form.  flag | delete | HTTP DELETE method.  flag | get | HTTP GET method.  flag | head | HTTP HEAD method.  flag | options | HTTP OPTIONS method.  flag | post | HTTP POST method.  flag | put | HTTP PUT method.  flag | trace | HTTP TRACE method.  flag | others | Other HTTP methods.  flag | connect | HTTP CONNECT method.  **Choices:**   - `"delete"` - `"get"` - `"head"` - `"options"` - `"post"` - `"put"` - `"trace"` - `"others"` - `"connect"` |
| **method_log**  string | Enable/disable logging.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **method_method_policy_address**  string | Host address. |
| **method_method_policy_allowed_methods**  string | Allowed Methods.  FLAG Based Options. Specify multiple in list form.  flag | delete | HTTP DELETE method.  flag | get | HTTP GET method.  flag | head | HTTP HEAD method.  flag | options | HTTP OPTIONS method.  flag | post | HTTP POST method.  flag | put | HTTP PUT method.  flag | trace | HTTP TRACE method.  flag | others | Other HTTP methods.  flag | connect | HTTP CONNECT method.  **Choices:**   - `"delete"` - `"get"` - `"head"` - `"options"` - `"post"` - `"put"` - `"trace"` - `"others"` - `"connect"` |
| **method_method_policy_pattern**  string | URL pattern. |
| **method_method_policy_regex**  string | Enable/disable regular expression based pattern match.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **method_severity**  string | Severity.  choice | low | low severity  choice | medium | medium severity  choice | high | High severity  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **method_status**  string | Status.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **mode**  string | Sets one of three modes for managing the object.  Allows use of soft-adds instead of overwriting existing values  **Choices:**   - `"add"` ← (default) - `"set"` - `"delete"` - `"update"` |
| **name**  string | WAF Profile name. |
| **signature**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **signature_credit_card_detection_threshold**  string | The minimum number of Credit cards to detect violation. |
| **signature_custom_signature_action**  string | Action.  choice | allow | Allow.  choice | block | Block.  choice | erase | Erase credit card numbers.  **Choices:**   - `"allow"` - `"block"` - `"erase"` |
| **signature_custom_signature_case_sensitivity**  string | Case sensitivity in pattern.  choice | disable | Case insensitive in pattern.  choice | enable | Case sensitive in pattern.  **Choices:**   - `"disable"` - `"enable"` |
| **signature_custom_signature_direction**  string | Traffic direction.  choice | request | Match HTTP request.  choice | response | Match HTTP response.  **Choices:**   - `"request"` - `"response"` |
| **signature_custom_signature_log**  string | Enable/disable logging.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **signature_custom_signature_name**  string | Signature name. |
| **signature_custom_signature_pattern**  string | Match pattern. |
| **signature_custom_signature_severity**  string | Severity.  choice | low | Low severity.  choice | medium | Medium severity.  choice | high | High severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **signature_custom_signature_status**  string | Status.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **signature_custom_signature_target**  string | Match HTTP target.  FLAG Based Options. Specify multiple in list form.  flag | arg | HTTP arguments.  flag | arg-name | Names of HTTP arguments.  flag | req-body | HTTP request body.  flag | req-cookie | HTTP request cookies.  flag | req-cookie-name | HTTP request cookie names.  flag | req-filename | HTTP request file name.  flag | req-header | HTTP request headers.  flag | req-header-name | HTTP request header names.  flag | req-raw-uri | Raw URI of HTTP request.  flag | req-uri | URI of HTTP request.  flag | resp-body | HTTP response body.  flag | resp-hdr | HTTP response headers.  flag | resp-status | HTTP response status.  **Choices:**   - `"arg"` - `"arg-name"` - `"req-body"` - `"req-cookie"` - `"req-cookie-name"` - `"req-filename"` - `"req-header"` - `"req-header-name"` - `"req-raw-uri"` - `"req-uri"` - `"resp-body"` - `"resp-hdr"` - `"resp-status"` |
| **signature_disabled_signature**  string | Disabled signatures |
| **signature_disabled_sub_class**  string | Disabled signature subclasses. |
| **signature_main_class_action**  string | Action.  choice | allow | Allow.  choice | block | Block.  choice | erase | Erase credit card numbers.  **Choices:**   - `"allow"` - `"block"` - `"erase"` |
| **signature_main_class_log**  string | Enable/disable logging.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **signature_main_class_severity**  string | Severity.  choice | low | Low severity.  choice | medium | Medium severity.  choice | high | High severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **signature_main_class_status**  string | Status.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **url_access**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **url_access_access_pattern_negate**  string | Enable/disable match negation.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **url_access_access_pattern_pattern**  string | URL pattern. |
| **url_access_access_pattern_regex**  string | Enable/disable regular expression based pattern match.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **url_access_access_pattern_srcaddr**  string | Source address. |
| **url_access_action**  string | Action.  choice | bypass | Allow the HTTP request, also bypass further WAF scanning.  choice | permit | Allow the HTTP request, and continue further WAF scanning.  choice | block | Block HTTP request.  **Choices:**   - `"bypass"` - `"permit"` - `"block"` |
| **url_access_address**  string | Host address. |
| **url_access_log**  string | Enable/disable logging.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **url_access_severity**  string | Severity.  choice | low | Low severity.  choice | medium | Medium severity.  choice | high | High severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |

## [Notes](fmgr_secprof_waf_module.md#id3)

> **Note:**
>
> - Full Documentation at <https://ftnt-ansible-docs.readthedocs.io/en/latest/>.

## [Examples](fmgr_secprof_waf_module.md#id4)

```yaml+jinja
- name: DELETE Profile
  community.fortios.fmgr_secprof_waf:
    name: "Ansible_WAF_Profile"
    comment: "Created by Ansible Module TEST"
    mode: "delete"

- name: CREATE Profile
  community.fortios.fmgr_secprof_waf:
    name: "Ansible_WAF_Profile"
    comment: "Created by Ansible Module TEST"
    mode: "set"
```

## [Return Values](fmgr_secprof_waf_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  **Returned:** always |

### Authors

- Luke Weighall (@lweighall)
- Andrew Welsh (@Ghilli3)
- Jim Huber (@p4r4n0y1ng)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.fortios)
