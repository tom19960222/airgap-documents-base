---
collection: ansible
version: "6"
title: "community.network.bcf_switch module – Create and remove a bcf switch."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/bcf_switch_module.html
fetched_at: 2026-07-27T17:17:10+00:00
---
# community.network.bcf_switch module – Create and remove a bcf switch.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.bcf_switch`.

- [Synopsis](bcf_switch_module.md#synopsis)
- [Parameters](bcf_switch_module.md#parameters)
- [Examples](bcf_switch_module.md#examples)

## [Synopsis](bcf_switch_module.md#id1)

- Create and remove a Big Cloud Fabric switch.

## [Parameters](bcf_switch_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Big Cloud Fabric access token. If this isn’t set then the environment variable `BIGSWITCH_ACCESS_TOKEN` is used. |
| **controller**  string / required | The controller IP address. |
| **fabric_role**  string / required | Fabric role of the switch.  Choices:   - `"spine"` - `"leaf"` |
| **leaf_group**  string | The leaf group of the switch if the switch is a leaf. |
| **mac**  string / required | The MAC address of the switch. |
| **name**  string / required | The name of the switch. |
| **state**  string | Whether the switch should be present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated. This should only be used on personally controlled devices using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](bcf_switch_module.md#id3)

```yaml+jinja
- name: Bcf leaf switch
  community.network.bcf_switch:
    name: Rack1Leaf1
    fabric_role: leaf
    leaf_group: R1
    mac: 00:00:00:02:00:02
    controller: '{{ inventory_hostname }}'
    state: present
    validate_certs: false
```

### Authors

- Ted (@tedelhourani)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
