---
collection: ansible
version: "6"
title: "cisco.asa.asa_og module – (deprecated, removed after 2022-06-01) Manage object groups on a Cisco ASA"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/asa/asa_og_module.html
fetched_at: 2026-07-27T16:50:48+00:00
---
# cisco.asa.asa_og module – (deprecated, removed after 2022-06-01) Manage object groups on a Cisco ASA

> **Note:**
>
> This module is part of the [cisco.asa collection](https://galaxy.ansible.com/cisco/asa) (version 3.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.asa`.
>
> To use it in a playbook, specify: `cisco.asa.asa_og`.

New in cisco.asa 1.0.0

- [DEPRECATED](asa_og_module.md#deprecated)
- [Synopsis](asa_og_module.md#synopsis)
- [Parameters](asa_og_module.md#parameters)
- [Examples](asa_og_module.md#examples)
- [Return Values](asa_og_module.md#return-values)
- [Status](asa_og_module.md#status)

## [DEPRECATED](asa_og_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Newer and updated modules released with more functionality in Ansible 2.10

Alternative:
:   asa_ogs

## [Synopsis](asa_og_module.md#id2)

- This module allows you to create and update object-group network/service on Cisco ASA device.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](asa_og_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | The description for the object-group. |
| **group_object**  list / elements=string | The group-object for network object-group. |
| **group_type**  string / required | The object group type.  Choices:   - `"network-object"` - `"service-object"` - `"port-object"` |
| **host_ip**  list / elements=string | The host IP address for object-group network. |
| **ip_mask**  list / elements=string | The IP address and mask for network object-group. |
| **name**  string / required | Name of the object group. |
| **port_eq**  list / elements=string | The single port for port-object. |
| **port_range**  list / elements=string | The port range for port-object. |
| **protocol**  string | The protocol for object-group service with port-object.  Choices:   - `"udp"` - `"tcp"` - `"tcp-udp"` |
| **service_cfg**  list / elements=string | The service-object configuration protocol, direction, range or port. |
| **state**  string | Manage the state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` - `"replace"` |

## [Examples](asa_og_module.md#id4)

```yaml+jinja
- name: configure network object-group
  cisco.asa.asa_og:
    name: ansible_test_0
    group_type: network-object
    state: present
    description: ansible_test object-group description
    host_ip:
    - 8.8.8.8
    - 8.8.4.4
    ip_mask:
    - 10.0.0.0 255.255.255.0
    - 192.168.0.0 255.255.0.0
    group_object:
    - awx_lon
    - awx_ams

- name: configure port-object object-group
  cisco.asa.asa_og:
    name: ansible_test_1
    group_type: port-object
    state: replace
    description: ansible_test object-group description
    protocol: tcp-udp
    port_eq:
    - 1025
    - kerberos
    port_range:
    - 1025 5201
    - 0 1024

- name: configure service-object object-group
  cisco.asa.asa_og:
    name: ansible_test_2
    group_type: service-object
    state: absent
    description: ansible_test object-group description
    service_cfg:
    - tcp destination eq 8080
    - tcp destination eq www
```

## [Return Values](asa_og_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | command sent to the device  Returned: always  Sample: `["object-group network ansible_test_0", "description ansible_test object-group description", "network-object host 8.8.8.8", "network-object host 8.8.4.4", "network-object 10.0.0.0 255.255.255.0", "network-object 192.168.0.0 255.255.0.0", "network-object 192.168.0.0 255.255.0.0", "group-object awx_lon", "group-object awx_ams"]` |

## [Status](asa_og_module.md#id6)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](asa_og_module.md#deprecated).

### Authors

- Federico Olivieri (@Federico87)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.asa/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.asa)
