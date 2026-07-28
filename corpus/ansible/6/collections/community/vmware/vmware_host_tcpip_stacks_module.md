---
collection: ansible
version: "6"
title: "community.vmware.vmware_host_tcpip_stacks module – Manage the TCP/IP Stacks configuration of ESXi host"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_host_tcpip_stacks_module.html
fetched_at: 2026-07-27T17:22:35+00:00
---
# community.vmware.vmware_host_tcpip_stacks module – Manage the TCP/IP Stacks configuration of ESXi host

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
> To use it in a playbook, specify: `community.vmware.vmware_host_tcpip_stacks`.

New in community.vmware 1.10.0

- [Synopsis](vmware_host_tcpip_stacks_module.md#synopsis)
- [Parameters](vmware_host_tcpip_stacks_module.md#parameters)
- [Notes](vmware_host_tcpip_stacks_module.md#notes)
- [Examples](vmware_host_tcpip_stacks_module.md#examples)
- [Return Values](vmware_host_tcpip_stacks_module.md#return-values)

## [Synopsis](vmware_host_tcpip_stacks_module.md#id1)

- This module can be used to modify the TCP/IP stacks configuration.

## [Parameters](vmware_host_tcpip_stacks_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **default**  dictionary | The TCP/IP stacks configuration of the *default*. |
| **alternate_dns**  string | The IP address of the alternate dns server. |
| **congestion_algorithm**  string | The TCP congest control algorithm.  Choices:   - `"newreno"` ← (default) - `"cubic"` |
| **domain**  string / required | The domain name portion of the DNS name. |
| **gateway**  string | The ipv4 gateway address. |
| **hostname**  string / required | The host name of the ESXi host. |
| **ipv6_gateway**  string  added in community.vmware 1.11.0 | The ipv6 gateway address. |
| **max_num_connections**  integer | The maximum number of socket connection that are requested.  Default: `11000` |
| **preferred_dns**  string | The IP address of the preferred dns server. |
| **search_domains**  list / elements=string | The domain in which to search for hosts, placed in order of preference.  Default: `[]` |
| **esxi_hostname**  string / required | Name of the ESXi host. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **provisioning**  dictionary | The TCP/IP stacks configuration of the *provisioning*. |
| **congestion_algorithm**  string | The TCP congest control algorithm.  Choices:   - `"newreno"` ← (default) - `"cubic"` |
| **gateway**  string | The ipv4 gateway address. |
| **ipv6_gateway**  string  added in community.vmware 1.11.0 | The ipv6 gateway address. |
| **max_num_connections**  integer | The maximum number of socket connection that are requested.  Default: `11000` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |
| **vmotion**  dictionary | The TCP/IP stacks configuration of the *vmotion*. |
| **congestion_algorithm**  string | The TCP congest control algorithm.  Choices:   - `"newreno"` ← (default) - `"cubic"` |
| **gateway**  string | The ipv4 gateway address. |
| **ipv6_gateway**  string  added in community.vmware 1.11.0 | The ipv6 gateway address. |
| **max_num_connections**  integer | The maximum number of socket connection that are requested.  Default: `11000` |
| **vxlan**  aliases: nsx_overlay  dictionary | The TCP/IP stacks configuration of the *vxlan*. |
| **congestion_algorithm**  string | The TCP congest control algorithm.  Choices:   - `"newreno"` ← (default) - `"cubic"` |
| **gateway**  string | The ipv4 gateway address. |
| **ipv6_gateway**  string  added in community.vmware 1.11.0 | The ipv6 gateway address. |
| **max_num_connections**  integer | The maximum number of socket connection that are requested.  Default: `11000` |

## [Notes](vmware_host_tcpip_stacks_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_tcpip_stacks_module.md#id4)

```yaml+jinja
- name: Update the TCP/IP stack configuration of the default
  community.vmware.vmware_host_tcpip_stacks:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    esxi_hostname: "{{ esxi_hostname }}"
    default:
      hostname: "{{ esxi_hostname }}"
      domain: example.com
      preferred_dns: 192.168.10.1
      alternate_dns: 192.168.20.1
      search_domains:
        - hoge.com
        - fuga.com
      gateway: 192.168.10.1
      congestion_algorithm: cubic
      max_num_connections: 12000

- name: Update the TCP/IP stack configuration of the provisioning
  community.vmware.vmware_host_tcpip_stacks:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    esxi_hostname: "{{ esxi_hostname }}"
    provisioning:
      congestion_algorithm: newreno
      max_num_connections: 12000
      gateway: 10.10.10.254

- name: Update the TCP/IP stack configuration of the default and provisioning
  community.vmware.vmware_host_tcpip_stacks:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    esxi_hostname: "{{ esxi_hostname }}"
    default:
      hostname: "{{ esxi_hostname }}"
      domain: example.com
      preferred_dns: 192.168.10.1
      alternate_dns: 192.168.20.1
      search_domains:
        - hoge.com
        - fuga.com
      gateway: 192.168.10.1
      congestion_algorithm: cubic
      max_num_connections: 12000
    provisioning:
      congestion_algorithm: newreno
      max_num_connections: 12000
      gateway: 10.10.10.254

- name: Update the ipv6 gateway of the provisioning TCP/IP stack
  community.vmware.vmware_host_tcpip_stacks:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    esxi_hostname: "{{ esxi_hostname }}"
    provisioning:
      ipv6_gateway: ::ffff:6440:301
```

## [Return Values](vmware_host_tcpip_stacks_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **default**  dictionary | dict of the TCP/IP stack configuration of the default.  Returned: always  Sample: `"{\n    \"alternate_dns\": \"192.168.20.1\",\n    \"congestion_algorithm\": \"cubic\",\n    \"domain\": \"example.com\",\n    \"gateway\": \"192.168.10.1\",\n    \"ipv6_gateway\", null,\n    \"hostname\": \"esxi-test03\",\n    \"max_num_connections\": 12000,\n    \"preferred_dns\": \"192.168.10.1\",\n    \"search_domains\": [\n        \"hoge.com\",\n        \"fuga.com\"\n    ]\n}"` |
| **provisioning**  dictionary | dict of the TCP/IP stack configuration of the provisioning.  Returned: always  Sample: `{"congestion_algorithm": "newreno", "gateway": "10.10.10.254", "ipv6_gateway": null, "max_num_connections": 12000}` |
| **vmotion**  dictionary | dict of the TCP/IP stack configuration of the vmotion.  Returned: always  Sample: `{"congestion_algorithm": "newreno", "gateway": null, "ipv6_gateway": null, "max_num_connections": 11000}` |
| **vxlan**  dictionary | dict of the TCP/IP stack configuration of the vxlan.  Returned: always  Sample: `{"congestion_algorithm": "newreno", "gateway": null, "ipv6_gateway": null, "max_num_connections": 11000}` |

### Authors

- sky-joker (@sky-joker)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
