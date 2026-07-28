---
collection: ansible
version: "8"
title: "community.vmware.vmware_host_vmnic_info module – Gathers info about vmnics available on the given ESXi host"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_host_vmnic_info_module.html
fetched_at: 2026-07-28T02:00:59+00:00
---
# community.vmware.vmware_host_vmnic_info module – Gathers info about vmnics available on the given ESXi host

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/ui/repo/published/community/vmware/) (version 3.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
>
> To use it in a playbook, specify: `community.vmware.vmware_host_vmnic_info`.

- [Synopsis](vmware_host_vmnic_info_module.md#synopsis)
- [Parameters](vmware_host_vmnic_info_module.md#parameters)
- [Notes](vmware_host_vmnic_info_module.md#notes)
- [Examples](vmware_host_vmnic_info_module.md#examples)
- [Return Values](vmware_host_vmnic_info_module.md#return-values)

## [Synopsis](vmware_host_vmnic_info_module.md#id1)

- This module can be used to gather information about vmnics available on the given ESXi host.
- If `cluster_name` is provided, then vmnic information about all hosts from given cluster will be returned.
- If `esxi_hostname` is provided, then vmnic information about given host system will be returned.
- Additional details about vswitch and dvswitch with respective vmnic is also provided which is added in 2.7 version.
- Additional details about lldp added in 1.11.0

## [Parameters](vmware_host_vmnic_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **capabilities**  boolean | Gather information about general capabilities (Auto negotiation, Wake On LAN, and Network I/O Control).  **Choices:**   - `false` ← (default) - `true` |
| **cluster_name**  string | Name of the cluster from which all host systems will be used.  Vmnic information about each ESXi server will be returned for the given cluster.  This parameter is required if `esxi_hostname` is not specified. |
| **directpath_io**  boolean | Gather information about DirectPath I/O capabilities and configuration.  **Choices:**   - `false` ← (default) - `true` |
| **esxi_hostname**  string | Name of the host system to work with.  Vmnic information about this ESXi server will be returned.  This parameter is required if `cluster_name` is not specified. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **sriov**  boolean | Gather information about SR-IOV capabilities and configuration.  **Choices:**   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_host_vmnic_info_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_vmnic_info_module.md#id4)

```yaml+jinja
- name: Gather info about vmnics of all ESXi Host in the given Cluster
  community.vmware.vmware_host_vmnic_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
  delegate_to: localhost
  register: cluster_host_vmnics

- name: Gather info about vmnics of an ESXi Host
  community.vmware.vmware_host_vmnic_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
  delegate_to: localhost
  register: host_vmnics
```

## [Return Values](vmware_host_vmnic_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hosts_vmnics_info**  dictionary | dict with hostname as key and dict with vmnics information as value.  for `num_vmnics`, only NICs starting with vmnic are counted. NICs like vusb\* are not counted.  details about vswitch and dvswitch was added in version 2.7.  details about vmnics was added in version 2.8.  details about lldp was added in version 1.11.0  **Returned:** hosts_vmnics_info  **Sample:** `{"10.76.33.204": {"all": ["vmnic0", "vmnic1"], "available": [], "dvswitch": {"dvs_0002": ["vmnic1"]}, "num_vmnics": 2, "used": ["vmnic1", "vmnic0"], "vmnic_details": [{"actual_duplex": "Full Duplex", "actual_speed": 10000, "adapter": "Intel(R) 82599 10 Gigabit Dual Port Network Connection", "configured_duplex": "Auto negotiate", "configured_speed": "Auto negotiate", "device": "vmnic0", "driver": "ixgbe", "lldp_info": {"Aggregated Port ID": "0", "Aggregation Status": "1", "Enabled Capabilities": {"_vimtype": "vim.host.PhysicalNic.CdpDeviceCapability", "host": false, "igmpEnabled": false, "networkSwitch": false, "repeater": false, "router": true, "sourceRouteBridge": false, "transparentBridge": true}, "MTU": "9216", "Port Description": "switch port description", "Samples": 18814, "System Description": "omitted from output", "System Name": "sw1", "TimeOut": 30, "Vlan ID": "1"}, "location": "0000:01:00.0", "mac": "aa:bb:cc:dd:ee:ff", "status": "Connected"}, {"actual_duplex": "Full Duplex", "actual_speed": 10000, "adapter": "Intel(R) 82599 10 Gigabit Dual Port Network Connection", "configured_duplex": "Auto negotiate", "configured_speed": "Auto negotiate", "device": "vmnic1", "driver": "ixgbe", "lldp_info": "N/A", "location": "0000:01:00.1", "mac": "ab:ba:cc:dd:ee:ff", "status": "Connected"}], "vswitch": {"vSwitch0": ["vmnic0"]}}}` |

### Authors

- Abhijeet Kasurde (@Akasurde)
- Christian Kotte (@ckotte)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
