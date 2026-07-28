---
collection: ansible
version: "6"
title: "ansible.netcommon.restconf_get module – Fetch configuration/state data from RESTCONF enabled devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/netcommon/restconf_get_module.html
fetched_at: 2026-07-27T16:44:36+00:00
---
# ansible.netcommon.restconf_get module – Fetch configuration/state data from RESTCONF enabled devices.

> **Note:**
>
> This module is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ansible/netcommon) (version 3.1.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
>
> To use it in a playbook, specify: `ansible.netcommon.restconf_get`.

New in ansible.netcommon 1.0.0

- [Synopsis](restconf_get_module.md#synopsis)
- [Parameters](restconf_get_module.md#parameters)
- [Notes](restconf_get_module.md#notes)
- [Examples](restconf_get_module.md#examples)
- [Return Values](restconf_get_module.md#return-values)

## [Synopsis](restconf_get_module.md#id1)

- RESTCONF is a standard mechanisms to allow web applications to access the configuration data and state data developed and standardized by the IETF. It is documented in RFC 8040.
- This module allows the user to fetch configuration and state data from RESTCONF enabled devices.

## [Parameters](restconf_get_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **content**  string | The `content` is a query parameter that controls how descendant nodes of the requested data nodes in `path` will be processed in the reply. If value is *config* return only configuration descendant data nodes of value in `path`. If value is *nonconfig* return only non-configuration descendant data nodes of value in `path`. If value is *all* return all descendant data nodes of value in `path`  Choices:   - `"config"` - `"nonconfig"` - `"all"` |
| **output**  string | The output of response received.  Choices:   - `"json"` ← (default) - `"xml"` |
| **path**  string / required | URI being used to execute API calls. |

## [Notes](restconf_get_module.md#id3)

> **Note:**
>
> - This module requires the RESTCONF system service be enabled on the remote device being managed.
> - This module is supported with *ansible_connection* value of *ansible.netcommon.httpapi* and *ansible_network_os* value of *ansible.netcommon.restconf*.
> - This module is tested against Cisco IOSXE 16.12.02 version.

## [Examples](restconf_get_module.md#id4)

```yaml+jinja
- name: get l3vpn services
  ansible.netcommon.restconf_get:
    path: /config/ietf-l3vpn-svc:l3vpn-svc/vpn-services
```

## [Return Values](restconf_get_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **response**  dictionary | A dictionary representing a JSON-formatted response  Returned: when the device response is valid JSON  Sample: `{"vpn-services": {"vpn-service": [{"customer-name": "red", "vpn-id": "blue_vpn1", "vpn-service-topology": "ietf-l3vpn-svc:any-to-any"}]}}` |

### Authors

- Ganesh Nalawade (@ganeshrn)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
