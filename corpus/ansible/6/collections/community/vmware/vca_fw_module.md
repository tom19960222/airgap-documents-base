---
collection: ansible
version: "6"
title: "community.vmware.vca_fw module – add remove firewall rules in a gateway  in a vca"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vca_fw_module.html
fetched_at: 2026-07-27T16:43:15+00:00
---
# community.vmware.vca_fw module – add remove firewall rules in a gateway in a vca

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/community/vmware) (version 2.10.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
>
> To use it in a playbook, specify: `community.vmware.vca_fw`.

- [DEPRECATED](vca_fw_module.md#deprecated)
- [Synopsis](vca_fw_module.md#synopsis)
- [Parameters](vca_fw_module.md#parameters)
- [Examples](vca_fw_module.md#examples)
- [Status](vca_fw_module.md#status)

## [DEPRECATED](vca_fw_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Module depends upon deprecated version of Pyvcloud library.

Alternative:
:   Use <https://github.com/vmware/ansible-module-vcloud-director> instead.

## [Synopsis](vca_fw_module.md#id2)

- Adds or removes firewall rules from a gateway in a vca environment

## [Parameters](vca_fw_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  string | The API version to be used with the vca.  Default: `"5.7"` |
| **fw_rules**  string / required | A list of firewall rules to be added to the gateway, Please see examples on valid entries  Default: `false` |
| **gateway_name**  string | The name of the gateway of the vdc where the rule should be added.  Default: `"gateway"` |
| **host**  string | The authentication host to be used when service type is vcd. |
| **instance_id**  string | The instance ID in a vchs environment to be used for creating the vapp. |
| **org**  string | The org to login to for creating vapp.  This option is required when the `service_type` is *vdc*. |
| **password**  aliases: pass, passwd  string | The vca password, if not set the environment variable `VCA_PASS` is checked for the password. |
| **service_type**  string | The type of service we are authenticating against.  Choices:   - `"vca"` ← (default) - `"vcd"` - `"vchs"` |
| **state**  string | Whether the object should be added or removed.  Choices:   - `"absent"` - `"present"` ← (default) |
| **username**  aliases: user  string | The vca username or email address, if not set the environment variable `VCA_USER` is checked for the username. |
| **validate_certs**  aliases: verify_certs  boolean | If the certificates of the authentication is to be verified.  Choices:   - `false` - `true` ← (default) |
| **vdc_name**  string | The name of the vdc where the gateway is located. |

## [Examples](vca_fw_module.md#id4)

```yaml+jinja
#Add a set of firewall rules

- hosts: localhost
  connection: local
  tasks:
   - community.vmware.vca_fw:
       instance_id: 'b15ff1e5-1024-4f55-889f-ea0209726282'
       vdc_name: 'benz_ansible'
       fw_rules:
         - description: "ben testing"
           source_ip: "Any"
           dest_ip: 192.0.2.23
         - description: "ben testing 2"
           source_ip: 192.0.2.50
           source_port: "Any"
           dest_port: "22"
           dest_ip: 192.0.2.101
           is_enable: "true"
           enable_logging: "false"
           protocol: "Tcp"
           policy: "allow"
```

## [Status](vca_fw_module.md#id5)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](vca_fw_module.md#deprecated).

### Authors

- Peter Sprygada (@privateip)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
