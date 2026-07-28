---
collection: ansible
version: "8"
title: "ansible.netcommon.restconf_config module – Handles create, update, read and delete of configuration data on RESTCONF enabled devices."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/netcommon/restconf_config_module.html
fetched_at: 2026-07-28T01:09:12+00:00
---
# ansible.netcommon.restconf_config module – Handles create, update, read and delete of configuration data on RESTCONF enabled devices.

> **Note:**
>
> This module is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ui/repo/published/ansible/netcommon/) (version 5.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
>
> To use it in a playbook, specify: `ansible.netcommon.restconf_config`.

New in ansible.netcommon 1.0.0

- [Synopsis](restconf_config_module.md#synopsis)
- [Parameters](restconf_config_module.md#parameters)
- [Notes](restconf_config_module.md#notes)
- [Examples](restconf_config_module.md#examples)
- [Return Values](restconf_config_module.md#return-values)

## [Synopsis](restconf_config_module.md#id1)

- RESTCONF is a standard mechanisms to allow web applications to configure and manage data. RESTCONF is a IETF standard and documented on RFC 8040.
- This module allows the user to configure data on RESTCONF enabled devices.

## [Parameters](restconf_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **content**  string | The configuration data in format as specififed in `format` option. Required unless `method` is *delete*. |
| **format**  string | The format of the configuration provided as value of `content`. Accepted values are *xml* and *json* and the given configuration format should be supported by remote RESTCONF server.  **Choices:**   - `"json"` ← (default) - `"xml"` |
| **method**  string | The RESTCONF method to manage the configuration change on device. The value *post* is used to create a data resource or invoke an operation resource, *put* is used to replace the target data resource, *patch* is used to modify the target resource, and *delete* is used to delete the target resource.  **Choices:**   - `"post"` ← (default) - `"put"` - `"patch"` - `"delete"` |
| **path**  string / required | URI being used to execute API calls. |

## [Notes](restconf_config_module.md#id3)

> **Note:**
>
> - This module requires the RESTCONF system service be enabled on the remote device being managed.
> - This module is supported with *ansible_connection* value of *ansible.netcommon.httpapi* and *ansible_network_os* value of *ansible.netcommon.restconf*.
> - This module is tested against Cisco IOSXE 16.12.02 version.

## [Examples](restconf_config_module.md#id4)

```yaml+jinja
- name: create l3vpn services
  ansible.netcommon.restconf_config:
    path: /config/ietf-l3vpn-svc:l3vpn-svc/vpn-services
    content: |
      {
        "vpn-service":[
                        {
                          "vpn-id": "red_vpn2",
                          "customer-name": "blue",
                          "vpn-service-topology": "ietf-l3vpn-svc:any-to-any"
                        },
                        {
                          "vpn-id": "blue_vpn1",
                          "customer-name": "red",
                          "vpn-service-topology": "ietf-l3vpn-svc:any-to-any"
                        }
                      ]
       }
```

## [Return Values](restconf_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **candidate**  dictionary | The configuration sent to the device.  **Returned:** When the method is not delete  **Sample:** `{"vpn-service": [{"customer-name": "red", "vpn-id": "blue_vpn1", "vpn-service-topology": "ietf-l3vpn-svc:any-to-any"}]}` |
| **running**  dictionary | The current running configuration on the device.  **Returned:** When the method is not delete  **Sample:** `{"vpn-service": [{"customer-name": "blue", "vpn-id": "red_vpn2", "vpn-service-topology": "ietf-l3vpn-svc:any-to-any"}, {"customer-name": "red", "vpn-id": "blue_vpn1", "vpn-service-topology": "ietf-l3vpn-svc:any-to-any"}]}` |

### Authors

- Ganesh Nalawade (@ganeshrn)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
