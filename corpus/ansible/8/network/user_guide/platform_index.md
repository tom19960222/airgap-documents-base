---
collection: ansible
version: "8"
title: "Platform Options"
source_url: https://docs.ansible.com/projects/ansible/8/network/user_guide/platform_index.html
fetched_at: 2026-07-28T00:59:31+00:00
---
# Platform Options

Some Ansible Network platforms support multiple connection types, privilege escalation (`enable` mode), or other options. The pages in this section offer standardized guides to understanding available options on each network platform. We welcome contributions from community-maintained platforms to this section.

Platform Options

- [CloudEngine OS Platform Options](platform_ce.md)
  - [Connections available](platform_ce.md#connections-available)
  - [Using CLI in Ansible](platform_ce.md#using-cli-in-ansible)
  - [Using NETCONF in Ansible](platform_ce.md#using-netconf-in-ansible)
  - [Notes](platform_ce.md#notes)
- [CNOS Platform Options](platform_cnos.md)
  - [Connections available](platform_cnos.md#connections-available)
  - [Using CLI in Ansible](platform_cnos.md#using-cli-in-ansible)
- [Dell OS6 Platform Options](platform_dellos6.md)
  - [Connections available](platform_dellos6.md#connections-available)
  - [Using CLI in Ansible](platform_dellos6.md#using-cli-in-ansible)
- [Dell OS9 Platform Options](platform_dellos9.md)
  - [Connections available](platform_dellos9.md#connections-available)
  - [Using CLI in Ansible](platform_dellos9.md#using-cli-in-ansible)
- [Dell OS10 Platform Options](platform_dellos10.md)
  - [Connections available](platform_dellos10.md#connections-available)
  - [Using CLI in Ansible](platform_dellos10.md#using-cli-in-ansible)
- [ENOS Platform Options](platform_enos.md)
  - [Connections available](platform_enos.md#connections-available)
  - [Using CLI in Ansible](platform_enos.md#using-cli-in-ansible)
- [EOS Platform Options](platform_eos.md)
  - [Connections available](platform_eos.md#connections-available)
  - [Using CLI in Ansible](platform_eos.md#using-cli-in-ansible)
  - [Using eAPI in Ansible](platform_eos.md#using-eapi-in-ansible)
- [ERIC_ECCLI Platform Options](platform_eric_eccli.md)
  - [Connections available](platform_eric_eccli.md#connections-available)
  - [Using CLI in Ansible](platform_eric_eccli.md#using-cli-in-ansible)
- [EXOS Platform Options](platform_exos.md)
  - [Connections available](platform_exos.md#connections-available)
  - [Using CLI in Ansible](platform_exos.md#using-cli-in-ansible)
  - [Using EXOS-API in Ansible](platform_exos.md#using-exos-api-in-ansible)
- [FRR Platform Options](platform_frr.md)
  - [Connections available](platform_frr.md#connections-available)
  - [Using CLI in Ansible](platform_frr.md#using-cli-in-ansible)
- [ICX Platform Options](platform_icx.md)
  - [Connections available](platform_icx.md#connections-available)
  - [Using CLI in Ansible](platform_icx.md#using-cli-in-ansible)
- [IOS Platform Options](platform_ios.md)
  - [Connections available](platform_ios.md#connections-available)
  - [Using CLI in Ansible](platform_ios.md#using-cli-in-ansible)
- [IOS-XR Platform Options](platform_iosxr.md)
  - [Connections available](platform_iosxr.md#connections-available)
  - [Using CLI in Ansible](platform_iosxr.md#using-cli-in-ansible)
  - [Using NETCONF in Ansible](platform_iosxr.md#using-netconf-in-ansible)
- [IronWare Platform Options](platform_ironware.md)
  - [Connections available](platform_ironware.md#connections-available)
  - [Using CLI in Ansible](platform_ironware.md#using-cli-in-ansible)
- [Junos OS Platform Options](platform_junos.md)
  - [Connections available](platform_junos.md#connections-available)
  - [Using CLI in Ansible](platform_junos.md#using-cli-in-ansible)
  - [Using NETCONF in Ansible](platform_junos.md#using-netconf-in-ansible)
- [Meraki Platform Options](platform_meraki.md)
  - [Connections available](platform_meraki.md#connections-available)
- [Pluribus NETVISOR Platform Options](platform_netvisor.md)
  - [Connections available](platform_netvisor.md#connections-available)
  - [Using CLI in Ansible](platform_netvisor.md#using-cli-in-ansible)
- [NOS Platform Options](platform_nos.md)
  - [Connections available](platform_nos.md#connections-available)
  - [Using CLI in Ansible](platform_nos.md#using-cli-in-ansible)
- [NXOS Platform Options](platform_nxos.md)
  - [Connections available](platform_nxos.md#connections-available)
  - [Using CLI in Ansible](platform_nxos.md#using-cli-in-ansible)
  - [Using NX-API in Ansible](platform_nxos.md#using-nx-api-in-ansible)
  - [Cisco Nexus platform support matrix](platform_nxos.md#cisco-nexus-platform-support-matrix)
- [RouterOS Platform Options](platform_routeros.md)
  - [Connections available](platform_routeros.md#connections-available)
  - [Using CLI in Ansible](platform_routeros.md#using-cli-in-ansible)
- [SLX-OS Platform Options](platform_slxos.md)
  - [Connections available](platform_slxos.md#connections-available)
  - [Using CLI in Ansible](platform_slxos.md#using-cli-in-ansible)
- [VOSS Platform Options](platform_voss.md)
  - [Connections available](platform_voss.md#connections-available)
  - [Using CLI in Ansible](platform_voss.md#using-cli-in-ansible)
- [VyOS Platform Options](platform_vyos.md)
  - [Connections available](platform_vyos.md#connections-available)
  - [Using CLI in Ansible](platform_vyos.md#using-cli-in-ansible)
- [WeOS 4 Platform Options](platform_weos4.md)
  - [Connections available](platform_weos4.md#connections-available)
  - [Using CLI in Ansible](platform_weos4.md#using-cli-in-ansible)
- [Netconf enabled Platform Options](platform_netconf_enabled.md)
  - [Connections available](platform_netconf_enabled.md#connections-available)
  - [Using NETCONF in Ansible](platform_netconf_enabled.md#using-netconf-in-ansible)

## Settings by Platform

|  | | `ansible_connection:` settings available | | | |
| --- | --- | --- | --- | --- | --- |
| Network OS | `ansible_network_os:` | network_cli | netconf | httpapi | local |
| [Arista EOS](https://galaxy.ansible.com/ui/repo/published/arista/eos) [[†]](platform_index.md#id3) | `arista.eos.eos` | ✓ |  | ✓ | ✓ |
| [Ciena SAOS6](https://galaxy.ansible.com/ui/repo/published/ciena/saos6) | `ciena.saos6.saos6` | ✓ |  |  | ✓ |
| [Cisco ASA](https://galaxy.ansible.com/ui/repo/published/cisco/asa) [[†]](platform_index.md#id3) | `cisco.asa.asa` | ✓ |  |  | ✓ |
| [Cisco IOS](https://galaxy.ansible.com/ui/repo/published/cisco/ios) [[†]](platform_index.md#id3) | `cisco.ios.ios` | ✓ |  |  | ✓ |
| [Cisco IOS XR](https://galaxy.ansible.com/ui/repo/published/cisco/iosxr) [[†]](platform_index.md#id3) | `cisco.iosxr.iosxr` | ✓ |  |  | ✓ |
| [Cisco NX-OS](https://galaxy.ansible.com/ui/repo/published/cisco/nxos) [[†]](platform_index.md#id3) | `cisco.nxos.nxos` | ✓ |  | ✓ | ✓ |
| [Cloudengine OS](https://galaxy.ansible.com/ui/repo/published/community/network) | `community.network.ce` | ✓ | ✓ |  | ✓ |
| [Dell OS6](https://github.com/ansible-collections/dellemc.os6) | `dellemc.os6.os6` | ✓ |  |  | ✓ |
| [Dell OS9](https://github.com/ansible-collections/dellemc.os9) | `dellemc.os9.os9` | ✓ |  |  | ✓ |
| [Dell OS10](https://galaxy.ansible.com/ui/repo/published/dellemc/os10) | `dellemc.os10.os10` | ✓ |  |  | ✓ |
| [Ericsson ECCLI](https://galaxy.ansible.com/ui/repo/published/community/network) | `community.network.eric_eccli` | ✓ |  |  | ✓ |
| [Extreme EXOS](https://galaxy.ansible.com/ui/repo/published/community/network) | `community.network.exos` | ✓ |  | ✓ |  |
| [Extreme IronWare](https://galaxy.ansible.com/ui/repo/published/community/network) | `community.network.ironware` | ✓ |  |  | ✓ |
| [Extreme NOS](https://galaxy.ansible.com/ui/repo/published/community/network) | `community.network.nos` | ✓ |  |  |  |
| [Extreme SLX-OS](https://galaxy.ansible.com/ui/repo/published/community/network) | `community.network.slxos` | ✓ |  |  |  |
| [Extreme VOSS](https://galaxy.ansible.com/ui/repo/published/community/network) | `community.network.voss` | ✓ |  |  |  |
| [F5 BIG-IP](https://galaxy.ansible.com/ui/repo/published/f5networks/f5_modules) |  |  |  |  | ✓ |
| [F5 BIG-IQ](https://galaxy.ansible.com/ui/repo/published/f5networks/f5_modules) |  |  |  |  | ✓ |
| [Junos OS](https://galaxy.ansible.com/ui/repo/published/junipernetworks/junos) [[†]](platform_index.md#id3) | `junipernetworks.junos.junos` | ✓ | ✓ |  | ✓ |
| [Lenovo CNOS](https://galaxy.ansible.com/ui/repo/published/community/network) | `community.network.cnos` | ✓ |  |  | ✓ |
| [Lenovo ENOS](https://galaxy.ansible.com/ui/repo/published/community/network) | `community.network.enos` | ✓ |  |  | ✓ |
| [Meraki](https://galaxy.ansible.com/ui/repo/published/cisco/meraki) |  |  |  |  | ✓ |
| [MikroTik RouterOS](https://galaxy.ansible.com/ui/repo/published/community/network) | `community.network.routeros` | ✓ |  |  |  |
| [Nokia SR OS](https://galaxy.ansible.com/ui/repo/published/community/network) |  |  |  |  | ✓ |
| [Pluribus Netvisor](https://galaxy.ansible.com/ui/repo/published/community/network) | `community.network.netvisor` | ✓ |  |  |  |
| [Ruckus ICX](https://galaxy.ansible.com/ui/repo/published/community/network) | `community.network.icx` | ✓ |  |  |  |
| [VyOS](https://galaxy.ansible.com/ui/repo/published/vyos/vyos) [[†]](platform_index.md#id3) | `vyos.vyos.vyos` | ✓ |  |  | ✓ |
| [Westermo WeOS 4](https://galaxy.ansible.com/ui/repo/published/community/network) | `community.network.weos4` | ✓ |  |  |  |
| OS that supports Netconf [[†]](platform_index.md#id3) | `<network-os>` |  | ✓ |  | ✓ |

**[†]** Maintained by Ansible Network Team
