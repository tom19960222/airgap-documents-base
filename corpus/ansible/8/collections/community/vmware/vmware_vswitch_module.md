---
collection: ansible
version: "8"
title: "community.vmware.vmware_vswitch module – Manage a VMware Standard Switch to an ESXi host."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_vswitch_module.html
fetched_at: 2026-07-28T02:01:29+00:00
---
# community.vmware.vmware_vswitch module – Manage a VMware Standard Switch to an ESXi host.

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
> To use it in a playbook, specify: `community.vmware.vmware_vswitch`.

- [Synopsis](vmware_vswitch_module.md#synopsis)
- [Parameters](vmware_vswitch_module.md#parameters)
- [Notes](vmware_vswitch_module.md#notes)
- [Examples](vmware_vswitch_module.md#examples)
- [Return Values](vmware_vswitch_module.md#return-values)

## [Synopsis](vmware_vswitch_module.md#id1)

- This module can be used to add, remove and update a VMware Standard Switch to an ESXi host.

## [Parameters](vmware_vswitch_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **esxi_hostname**  aliases: host  string | Manage the vSwitch using this ESXi host system. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **mtu**  integer | MTU to configure on vSwitch.  **Default:** `1500` |
| **nics**  aliases: nic_name  list / elements=string | A list of vmnic names or vmnic name to attach to vSwitch.  Alias `nics` is added in version 2.4.  **Default:** `[]` |
| **number_of_ports**  integer | Number of port to configure on vSwitch.  **Default:** `128` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **security**  aliases: security_policy, network_policy  dictionary  *added in community.vmware 2.4.0* | Network policy specifies layer 2 security settings for a portgroup such as promiscuous mode, where guest adapter listens to all the packets, MAC address changes and forged transmits.  Dict which configures the different security values for portgroup. |
| **forged_transmits**  boolean | Indicates whether forged transmits are allowed.  **Choices:**   - `false` - `true` |
| **mac_changes**  boolean | Indicates whether mac changes are allowed.  **Choices:**   - `false` - `true` |
| **promiscuous_mode**  boolean | Indicates whether promiscuous mode is allowed.  **Choices:**   - `false` - `true` |
| **state**  string | Add or remove the switch.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **switch**  aliases: switch_name  string / required | vSwitch name to add.  Alias `switch` is added in version 2.4. |
| **teaming**  aliases: teaming_policy  dictionary  *added in community.vmware 2.4.0* | Dictionary which configures the different teaming values for portgroup. |
| **active_adapters**  list / elements=string | List of active adapters used for load balancing.  All vmnics are used as active adapters if `active_adapters` and `standby_adapters` are not defined. |
| **failback**  boolean | Indicate whether or not to use a failback when restoring links.  **Choices:**   - `false` - `true` |
| **load_balancing**  aliases: load_balance_policy  string | Network adapter teaming policy.  **Choices:**   - `"loadbalance_ip"` - `"loadbalance_srcmac"` - `"loadbalance_srcid"` - `"failover_explicit"` |
| **network_failure_detection**  string | Network failure detection.  **Choices:**   - `"link_status_only"` - `"beacon_probing"` |
| **notify_switches**  boolean | Indicate whether or not to notify the physical switch if a link fails.  **Choices:**   - `false` - `true` |
| **standby_adapters**  list / elements=string | List of standby adapters used for failover.  All vmnics are used as active adapters if `active_adapters` and `standby_adapters` are not defined. |
| **traffic_shaping**  dictionary  *added in community.vmware 2.4.0* | Dictionary which configures traffic shaping for the switch. |
| **average_bandwidth**  integer | Average bandwidth (kbit/s). |
| **burst_size**  integer | Burst size (KB). |
| **enabled**  boolean | Status of Traffic Shaping Policy.  **Choices:**   - `false` - `true` |
| **peak_bandwidth**  integer | Peak bandwidth (kbit/s). |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_vswitch_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_vswitch_module.md#id4)

```yaml+jinja
- name: Add a VMware vSwitch
  community.vmware.vmware_vswitch:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    switch: vswitch_name
    nics: vmnic_name
    mtu: 9000
  delegate_to: localhost

- name: Add a VMware vSwitch without any physical NIC attached
  community.vmware.vmware_vswitch:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    switch: vswitch_0001
    mtu: 9000
  delegate_to: localhost

- name: Add a VMware vSwitch with multiple NICs
  community.vmware.vmware_vswitch:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    switch: vmware_vswitch_0004
    nics:
    - vmnic1
    - vmnic2
    mtu: 9000
  delegate_to: localhost

- name: Add a VMware vSwitch to a specific host system
  community.vmware.vmware_vswitch:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    esxi_hostname: DC0_H0
    switch_name: vswitch_001
    nic_name: vmnic0
    mtu: 9000
  delegate_to: localhost

- name: Add a VMware vSwitch to a specific host system with Promiscuous Mode Enabled
  community.vmware.vmware_vswitch:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    esxi_hostname: DC0_H0
    switch_name: vswitch_001
    nic_name: vmnic0
    mtu: 9000
    security:
        promiscuous_mode: true
  delegate_to: localhost

- name: Add a VMware vSwitch to a specific host system with active/standby teaming
  community.vmware.vmware_vswitch:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    esxi_hostname: DC0_H0
    switch_name: vswitch_001
    nic_name:
      - vmnic0
      - vmnic1
    teaming:
      active_adapters:
        - vmnic0
      standby_adapters:
        - vmnic1
  delegate_to: localhost

- name: Add a VMware vSwitch to a specific host system with traffic shaping
  community.vmware.vmware_vswitch:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    esxi_hostname: DC0_H0
    switch_name: vswitch_001
    nic_name:
      - vmnic0
      - vmnic1
    traffic_shaping:
        enabled: true
        average_bandwidth: 100000
        peak_bandwidth: 100000
        burst_size: 102400
  delegate_to: localhost

- name: Delete a VMware vSwitch in a specific host system
  community.vmware.vmware_vswitch:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    esxi_hostname: DC0_H0
    switch_name: vswitch_001
    state: absent
  delegate_to: localhost
```

## [Return Values](vmware_vswitch_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  string | information about performed operation  **Returned:** always  **Sample:** `"vSwitch 'vSwitch_1002' is created successfully"` |

### Authors

- Joseph Callen (@jcpowermac)
- Russell Teague (@mtnbikenc)
- Abhijeet Kasurde (@Akasurde)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
