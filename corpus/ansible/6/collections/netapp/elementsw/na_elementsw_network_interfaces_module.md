---
collection: ansible
version: "6"
title: "netapp.elementsw.na_elementsw_network_interfaces module – NetApp Element Software Configure Node Network Interfaces"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/elementsw/na_elementsw_network_interfaces_module.html
fetched_at: 2026-07-28T00:11:51+00:00
---
# netapp.elementsw.na_elementsw_network_interfaces module – NetApp Element Software Configure Node Network Interfaces

> **Note:**
>
> This module is part of the [netapp.elementsw collection](https://galaxy.ansible.com/netapp/elementsw) (version 21.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.elementsw`.
> You need further requirements to be able to use this module,
> see [Requirements](na_elementsw_network_interfaces_module.md#ansible-collections-netapp-elementsw-na-elementsw-network-interfaces-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.elementsw.na_elementsw_network_interfaces`.

New in netapp.elementsw 2.7.0

- [Synopsis](na_elementsw_network_interfaces_module.md#synopsis)
- [Requirements](na_elementsw_network_interfaces_module.md#requirements)
- [Parameters](na_elementsw_network_interfaces_module.md#parameters)
- [Notes](na_elementsw_network_interfaces_module.md#notes)
- [Examples](na_elementsw_network_interfaces_module.md#examples)
- [Return Values](na_elementsw_network_interfaces_module.md#return-values)

## [Synopsis](na_elementsw_network_interfaces_module.md#id1)

- Configure Element SW Node Network Interfaces for Bond 1G and 10G IP addresses.
- This module does not create interfaces, it expects the interfaces to already exists and can only modify them.
- This module cannot set or modify the method (Loopback, manual, dhcp, static).
- This module is not idempotent and does not support check_mode.

## [Requirements](na_elementsw_network_interfaces_module.md#id2)

The below requirements are needed on the host that executes this module.

- The modules were developed with SolidFire 10.1
- solidfire-sdk-python (1.1.0.92) or greater. Install using ‘pip install solidfire-sdk-python’

## [Parameters](na_elementsw_network_interfaces_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **bond_10g**  dictionary | settings for the Bond10G interface. |
| **address**  string | IP address for the interface. |
| **bond_lacp_rate**  string | Link Aggregation Control Protocol - useful only if LACP is selected as the Bond Mode.  Slow - Packets are transmitted at 30 second intervals.  Fast - Packets are transmitted in 1 second intervals.  Choices:   - `"Fast"` - `"Slow"` |
| **bond_mode**  string | Bonding mode.  Choices:   - `"ActivePassive"` - `"ALB"` - `"LACP"` |
| **dns_nameservers**  list / elements=string | List of addresses for domain name servers. |
| **dns_search**  list / elements=string | List of DNS search domains. |
| **gateway**  string | IP router network address to send packets out of the local network. |
| **mtu**  string | The largest packet size (in bytes) that the interface can transmit..  Must be greater than or equal to 1500 bytes. |
| **netmask**  string | subnet mask for the interface. |
| **virtual_network_tag**  string | The virtual network identifier of the interface (VLAN tag). |
| **bond_1g**  dictionary | settings for the Bond1G interface. |
| **address**  string | IP address for the interface. |
| **bond_lacp_rate**  string | Link Aggregation Control Protocol - useful only if LACP is selected as the Bond Mode.  Slow - Packets are transmitted at 30 second intervals.  Fast - Packets are transmitted in 1 second intervals.  Choices:   - `"Fast"` - `"Slow"` |
| **bond_mode**  string | Bonding mode.  Choices:   - `"ActivePassive"` - `"ALB"` - `"LACP"` |
| **dns_nameservers**  list / elements=string | List of addresses for domain name servers. |
| **dns_search**  list / elements=string | List of DNS search domains. |
| **gateway**  string | IP router network address to send packets out of the local network. |
| **mtu**  string | The largest packet size (in bytes) that the interface can transmit..  Must be greater than or equal to 1500 bytes. |
| **netmask**  string | subnet mask for the interface. |
| **virtual_network_tag**  string | The virtual network identifier of the interface (VLAN tag). |
| **bond_mode_10g**  string | deprecated, use bond_10g option. |
| **bond_mode_1g**  string | deprecated, use bond_1g option. |
| **dns_nameservers**  list / elements=string | deprecated, use bond_1g and bond_10g options. |
| **dns_search_domains**  list / elements=string | deprecated, use bond_1g and bond_10g options. |
| **gateway_address_10g**  string | deprecated, use bond_10g option. |
| **gateway_address_1g**  string | deprecated, use bond_1g option. |
| **hostname**  string / required | The hostname or IP address of the SolidFire cluster.  For na_elementsw_cluster, the Management IP (MIP) or hostname of the node to initiate the cluster creation from. |
| **ip_address_10g**  string | deprecated, use bond_10g option. |
| **ip_address_1g**  string | deprecated, use bond_1g option. |
| **lacp_10g**  string | deprecated, use bond_10g option. |
| **lacp_1g**  string | deprecated, use bond_1g option. |
| **method**  string | deprecated, this option would trigger a ‘updated failed’ error |
| **mtu_10g**  string | deprecated, use bond_10g option. |
| **mtu_1g**  string | deprecated, use bond_1g option. |
| **password**  aliases: pass  string / required | Password for the specified user. |
| **subnet_10g**  string | deprecated, use bond_10g option. |
| **subnet_1g**  string | deprecated, use bond_1g option. |
| **username**  aliases: user  string / required | Please ensure that the user has the adequate permissions. For more information, please read the official documentation <https://mysupport.netapp.com/documentation/docweb/index.html?productID%3D62636%26language%3Den-US>. |
| **virtual_network_tag**  string | deprecated, use bond_1g and bond_10g options. |

## [Notes](na_elementsw_network_interfaces_module.md#id4)

> **Note:**
>
> - The modules prefixed with na\\_elementsw are built to support the SolidFire storage platform.

## [Examples](na_elementsw_network_interfaces_module.md#id5)

```yaml+jinja
- name: Set Node network interfaces configuration for Bond 1G and 10G properties
  tags:
  - elementsw_network_interfaces
  na_elementsw_network_interfaces:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    bond_1g:
      address: 10.253.168.131
      netmask: 255.255.248.0
      gateway: 10.253.168.1
      mtu: '1500'
      bond_mode: ActivePassive
      dns_nameservers: dns1,dns2
      dns_search: domain1,domain2
    bond_10g:
      address: 10.253.1.202
      netmask: 255.255.255.192
      gateway: 10.253.1.193
      mtu: '9000'
      bond_mode: LACP
      bond_lacp_rate: Fast
      virtual_network_tag: vnet_tag
```

## [Return Values](na_elementsw_network_interfaces_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success message  Returned: success |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.elementsw/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.elementsw)
