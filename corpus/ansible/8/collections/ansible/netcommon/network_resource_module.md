---
collection: ansible
version: "8"
title: "ansible.netcommon.network_resource module – Manage resource modules"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/netcommon/network_resource_module.html
fetched_at: 2026-07-28T01:09:11+00:00
---
# ansible.netcommon.network_resource module – Manage resource modules

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
> To use it in a playbook, specify: `ansible.netcommon.network_resource`.

New in ansible.netcommon 2.4.0

- [Synopsis](network_resource_module.md#synopsis)
- [Parameters](network_resource_module.md#parameters)
- [Notes](network_resource_module.md#notes)
- [Examples](network_resource_module.md#examples)
- [Return Values](network_resource_module.md#return-values)

## [Synopsis](network_resource_module.md#id1)

- Get list of available resource modules for given os name
- Retrieve given resource module configuration facts
- Push given resource module configuration

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](network_resource_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  any | The resource module configuration. For details on the type and structure of this option refer the individual resource module platform documentation. |
| **name**  string | The name of the resource module to manage.  The resource module should be supported for given *os_name*, if not supported it will result in error. |
| **os_name**  string | The name of the os to manage the resource modules.  The name should be fully qualified collection name format, that is *<namespace>.<collection-name>.<plugin-name>*.  If value of this option is not set the os value will be read from *ansible_network_os* variable.  If value of both *os_name* and *ansible_network_os* is not set it will result in error. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the host device by executing the cli command to get the resource configuration on host.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  For supported values refer the individual resource module platform documentation. |

## [Notes](network_resource_module.md#id3)

> **Note:**
>
> - Refer the individual module documentation for the valid inputs of *state* and *config* modules.

## [Examples](network_resource_module.md#id4)

```yaml+jinja
- name: get list of resource modules for given network_os
  ansible.netcommon.network_resource:
  register: result

- name: fetch acl config for
  ansible.netcommon.network_resource:
    os_name: cisco.ios.ios
    name: acls
    state: gathered

- name: manage acl config for cisco.ios.ios network os.
  ansible.netcommon.network_resource:
    name: acls
    config:
      - afi: ipv4
        acls:
          - name: test_acl
            acl_type: extended
            aces:
              - grant: deny
                protocol_options:
                  tcp:
                    fin: true
                source:
                  address: 192.0.2.0
                  wildcard_bits: 0.0.0.255
                destination:
                  address: 192.0.3.0
                  wildcard_bits: 0.0.0.255
                  port_protocol:
                    eq: www
                option:
                  traceroute: true
                ttl:
                  eq: 10
    state: merged
```

## [Return Values](network_resource_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  **Returned:** when changed and when *state* and/or *config* option is set  **Sample:** `["The configuration returned will always be in the same format of the parameters above."]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  **Returned:** When *state* and/or *config* option is set  **Sample:** `["The configuration returned will always be in the same format of the parameters above."]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device  **Returned:** When *state* and/or *config* option is set  **Sample:** `["ip access-list extended 110"]` |
| **modules**  list / elements=string | List of resource modules supported for given OS.  **Returned:** When only *os_name* or *ansible_network_os* is set  **Sample:** `["acl_interfaces", "acls", "bgp_global"]` |

### Authors

- Ganesh B. Nalawade (@ganeshrn)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
