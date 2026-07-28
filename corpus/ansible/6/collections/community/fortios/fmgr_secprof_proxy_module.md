---
collection: ansible
version: "6"
title: "community.fortios.fmgr_secprof_proxy module – Manage proxy security profiles in FortiManager"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/fortios/fmgr_secprof_proxy_module.html
fetched_at: 2026-07-27T17:07:51+00:00
---
# community.fortios.fmgr_secprof_proxy module – Manage proxy security profiles in FortiManager

> **Note:**
>
> This module is part of the [community.fortios collection](https://galaxy.ansible.com/community/fortios) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.fortios`.
>
> To use it in a playbook, specify: `community.fortios.fmgr_secprof_proxy`.

- [Synopsis](fmgr_secprof_proxy_module.md#synopsis)
- [Parameters](fmgr_secprof_proxy_module.md#parameters)
- [Notes](fmgr_secprof_proxy_module.md#notes)
- [Examples](fmgr_secprof_proxy_module.md#examples)
- [Return Values](fmgr_secprof_proxy_module.md#return-values)

## [Synopsis](fmgr_secprof_proxy_module.md#id1)

- Manage proxy security profiles for FortiGates via FortiManager using the FMG API with playbooks

## [Parameters](fmgr_secprof_proxy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string | The ADOM the configuration should belong to.  Default: `"root"` |
| **header_client_ip**  string | Actions to take on the HTTP client-IP header in forwarded requests| forwards (pass), adds, or removes the HTTP  header.  choice | pass | Forward the same HTTP header.  choice | add | Add the HTTP header.  choice | remove | Remove the HTTP header.  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **header_front_end_https**  string | Action to take on the HTTP front-end-HTTPS header in forwarded requests| forwards (pass), adds, or removes the  HTTP header.  choice | pass | Forward the same HTTP header.  choice | add | Add the HTTP header.  choice | remove | Remove the HTTP header.  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **header_via_request**  string | Action to take on the HTTP via header in forwarded requests| forwards (pass), adds, or removes the HTTP header  .  choice | pass | Forward the same HTTP header.  choice | add | Add the HTTP header.  choice | remove | Remove the HTTP header.  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **header_via_response**  string | Action to take on the HTTP via header in forwarded responses| forwards (pass), adds, or removes the HTTP heade      choice | pass | Forward the same HTTP header.  choice | add | Add the HTTP header.  choice | remove | Remove the HTTP header.  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **header_x_authenticated_groups**  string | Action to take on the HTTP x-authenticated-groups header in forwarded requests| forwards (pass), adds, or remo  ves the HTTP header.  choice | pass | Forward the same HTTP header.  choice | add | Add the HTTP header.  choice | remove | Remove the HTTP header.  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **header_x_authenticated_user**  string | Action to take on the HTTP x-authenticated-user header in forwarded requests| forwards (pass), adds, or remove  s the HTTP header.  choice | pass | Forward the same HTTP header.  choice | add | Add the HTTP header.  choice | remove | Remove the HTTP header.  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **header_x_forwarded_for**  string | Action to take on the HTTP x-forwarded-for header in forwarded requests| forwards (pass), adds, or removes the  HTTP header.  choice | pass | Forward the same HTTP header.  choice | add | Add the HTTP header.  choice | remove | Remove the HTTP header.  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **headers**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **headers_action**  string | Action when HTTP the header forwarded.  choice | add-to-request | Add the HTTP header to request.  choice | add-to-response | Add the HTTP header to response.  choice | remove-from-request | Remove the HTTP header from request.  choice | remove-from-response | Remove the HTTP header from response.  Choices:   - `"add-to-request"` - `"add-to-response"` - `"remove-from-request"` - `"remove-from-response"` |
| **headers_content**  string | HTTP header’s content. |
| **headers_name**  string | HTTP forwarded header name. |
| **log_header_change**  string | Enable/disable logging HTTP header changes.  choice | disable | Disable Enable/disable logging HTTP header changes.  choice | enable | Enable Enable/disable logging HTTP header changes.  Choices:   - `"disable"` - `"enable"` |
| **mode**  string | Sets one of three modes for managing the object.  Allows use of soft-adds instead of overwriting existing values  Choices:   - `"add"` ← (default) - `"set"` - `"delete"` - `"update"` |
| **name**  string | Profile name. |
| **strip_encoding**  string | Enable/disable stripping unsupported encoding from the request header.  choice | disable | Disable stripping of unsupported encoding from the request header.  choice | enable | Enable stripping of unsupported encoding from the request header.  Choices:   - `"disable"` - `"enable"` |

## [Notes](fmgr_secprof_proxy_module.md#id3)

> **Note:**
>
> - Full Documentation at <https://ftnt-ansible-docs.readthedocs.io/en/latest/>.

## [Examples](fmgr_secprof_proxy_module.md#id4)

```yaml+jinja
- name: DELETE Profile
  community.fortios.fmgr_secprof_proxy:
    name: "Ansible_Web_Proxy_Profile"
    mode: "delete"

- name: CREATE Profile
  community.fortios.fmgr_secprof_proxy:
    name: "Ansible_Web_Proxy_Profile"
    mode: "set"
    header_client_ip: "pass"
    header_front_end_https: "add"
    header_via_request: "remove"
    header_via_response: "pass"
    header_x_authenticated_groups: "add"
    header_x_authenticated_user: "remove"
    strip_encoding: "enable"
    log_header_change: "enable"
    header_x_forwarded_for: "pass"
    headers_action: "add-to-request"
    headers_content: "test"
    headers_name: "test_header"
```

## [Return Values](fmgr_secprof_proxy_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  Returned: always |

### Authors

- Luke Weighall (@lweighall)
- Andrew Welsh (@Ghilli3)
- Jim Huber (@p4r4n0y1ng)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.fortios)
