---
collection: ansible
version: "6"
title: "community.vmware.vmware_portgroup_info module – Gathers info about an ESXi host’s Port Group configuration"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_portgroup_info_module.html
fetched_at: 2026-07-27T17:22:45+00:00
---
# community.vmware.vmware_portgroup_info module – Gathers info about an ESXi host’s Port Group configuration

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
> To use it in a playbook, specify: `community.vmware.vmware_portgroup_info`.

- [Synopsis](vmware_portgroup_info_module.md#synopsis)
- [Parameters](vmware_portgroup_info_module.md#parameters)
- [Notes](vmware_portgroup_info_module.md#notes)
- [Examples](vmware_portgroup_info_module.md#examples)
- [Return Values](vmware_portgroup_info_module.md#return-values)

## [Synopsis](vmware_portgroup_info_module.md#id1)

- This module can be used to gather information about an ESXi host’s Port Group configuration when ESXi hostname or Cluster name is given.

## [Parameters](vmware_portgroup_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string | Name of the cluster.  Info will be returned for all hostsystem belonging to this cluster name.  If `esxi_hostname` is not given, this parameter is required. |
| **esxi_hostname**  string | ESXi hostname to gather information from.  If `cluster_name` is not given, this parameter is required. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **policies**  boolean | Gather information about Security, Traffic Shaping, as well as Teaming and failover.  The property `ts` stands for Traffic Shaping and `lb` for Load Balancing.  Choices:   - `false` ← (default) - `true` |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_portgroup_info_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_portgroup_info_module.md#id4)

```yaml+jinja
- name: Gather portgroup info about all ESXi Host in given Cluster
  community.vmware.vmware_portgroup_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
  delegate_to: localhost

- name: Gather portgroup info about ESXi Host system
  community.vmware.vmware_portgroup_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
  delegate_to: localhost
```

## [Return Values](vmware_portgroup_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hosts_portgroup_info**  dictionary | metadata about host’s portgroup configuration  Returned: on success  Sample: `{"esx01": [{"failback": true, "failover_active": ["vmnic0", "vmnic1"], "failover_standby": [], "failure_detection": "link_status_only", "lb": "loadbalance_srcid", "notify": true, "portgroup": "Management Network", "security": [false, false, false], "ts": "No override", "vlan_id": 0, "vswitch": "vSwitch0"}, {"failback": true, "failover_active": ["vmnic2"], "failover_standby": ["vmnic3"], "failure_detection": "No override", "lb": "No override", "notify": true, "portgroup": "vMotion", "security": [false, false, false], "ts": "No override", "vlan_id": 33, "vswitch": "vSwitch1"}]}` |

### Authors

- Abhijeet Kasurde (@Akasurde)
- Christian Kotte (@ckotte)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
