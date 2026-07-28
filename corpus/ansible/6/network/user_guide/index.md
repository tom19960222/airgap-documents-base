---
collection: ansible
version: "6"
title: "Network Advanced Topics"
source_url: https://docs.ansible.com/projects/ansible/6/network/user_guide/index.html
fetched_at: 2026-07-27T16:39:27+00:00
---
# Network Advanced Topics

Once you have mastered the basics of network automation with Ansible, as presented in [Network Getting Started](../getting_started/index.md#network-getting-started), use this guide understand platform-specific details, optimization, and troubleshooting tips for Ansible for network automation.

**Who should use this guide?**

This guide is intended for network engineers using Ansible for automation. It covers advanced topics. If you understand networks and Ansible, this guide is for you. You may read through the entire guide if you choose, or use the links below to find the specific information you need.

If you’re new to Ansible, or new to using Ansible for network automation, start with the [Network Getting Started](../getting_started/index.md#network-getting-started).

Advanced Topics

- [Network Resource Modules](network_resource_modules.md)
  - [Network resource module states](network_resource_modules.md#network-resource-module-states)
  - [Using network resource modules](network_resource_modules.md#using-network-resource-modules)
  - [Example: Verifying the network device configuration has not changed](network_resource_modules.md#example-verifying-the-network-device-configuration-has-not-changed)
  - [Example: Acquiring and updating VLANs on a network device](network_resource_modules.md#example-acquiring-and-updating-vlans-on-a-network-device)
- [Ansible Network Examples](network_best_practices_2.5.md)
  - [Prerequisites](network_best_practices_2.5.md#prerequisites)
  - [Groups and variables in an inventory file](network_best_practices_2.5.md#groups-and-variables-in-an-inventory-file)
  - [Example 1: collecting facts and creating backup files with a playbook](network_best_practices_2.5.md#example-1-collecting-facts-and-creating-backup-files-with-a-playbook)
  - [Example 2: simplifying playbooks with platform-independent modules](network_best_practices_2.5.md#example-2-simplifying-playbooks-with-platform-independent-modules)
  - [Implementation Notes](network_best_practices_2.5.md#implementation-notes)
  - [Troubleshooting](network_best_practices_2.5.md#troubleshooting)
- [Parsing semi-structured text with Ansible](cli_parsing.md)
  - [Understanding the CLI parser](cli_parsing.md#understanding-the-cli-parser)
  - [Parsing the CLI](cli_parsing.md#parsing-the-cli)
  - [Advanced use cases](cli_parsing.md#advanced-use-cases)
- [Validate data against set criteria with Ansible](validate.md)
  - [Understanding the validate plugin](validate.md#understanding-the-validate-plugin)
  - [Structuring the data](validate.md#structuring-the-data)
  - [Defining the criteria to validate against](validate.md#defining-the-criteria-to-validate-against)
  - [Validating the data](validate.md#validating-the-data)
- [Network Debug and Troubleshooting Guide](network_debug_troubleshooting.md)
  - [How to troubleshoot](network_debug_troubleshooting.md#how-to-troubleshoot)
  - [Troubleshooting socket path issues](network_debug_troubleshooting.md#troubleshooting-socket-path-issues)
  - [Category “Unable to open shell”](network_debug_troubleshooting.md#category-unable-to-open-shell)
  - [Timeout issues](network_debug_troubleshooting.md#timeout-issues)
  - [Playbook issues](network_debug_troubleshooting.md#playbook-issues)
  - [Proxy Issues](network_debug_troubleshooting.md#proxy-issues)
  - [Miscellaneous Issues](network_debug_troubleshooting.md#miscellaneous-issues)
- [Working with command output and prompts in network modules](network_working_with_command_output.md)
  - [Conditionals in networking modules](network_working_with_command_output.md#conditionals-in-networking-modules)
  - [Handling prompts in network modules](network_working_with_command_output.md#handling-prompts-in-network-modules)
- [Ansible Network FAQ](faq.md)
  - [How can I improve performance for network playbooks?](faq.md#how-can-i-improve-performance-for-network-playbooks)
  - [Why is my output sometimes replaced with `********`?](faq.md#why-is-my-output-sometimes-replaced-with)
  - [Why do the `*_config` modules always return `changed=true` with abbreviated commands?](faq.md#why-do-the-config-modules-always-return-changed-true-with-abbreviated-commands)
- [Platform Options](platform_index.md)
  - [CloudEngine OS Platform Options](platform_ce.md)
  - [CNOS Platform Options](platform_cnos.md)
  - [Dell OS6 Platform Options](platform_dellos6.md)
  - [Dell OS9 Platform Options](platform_dellos9.md)
  - [Dell OS10 Platform Options](platform_dellos10.md)
  - [ENOS Platform Options](platform_enos.md)
  - [EOS Platform Options](platform_eos.md)
  - [ERIC_ECCLI Platform Options](platform_eric_eccli.md)
  - [EXOS Platform Options](platform_exos.md)
  - [FRR Platform Options](platform_frr.md)
  - [ICX Platform Options](platform_icx.md)
  - [IOS Platform Options](platform_ios.md)
  - [IOS-XR Platform Options](platform_iosxr.md)
  - [IronWare Platform Options](platform_ironware.md)
  - [Junos OS Platform Options](platform_junos.md)
  - [Meraki Platform Options](platform_meraki.md)
  - [Pluribus NETVISOR Platform Options](platform_netvisor.md)
  - [NOS Platform Options](platform_nos.md)
  - [NXOS Platform Options](platform_nxos.md)
  - [RouterOS Platform Options](platform_routeros.md)
  - [SLX-OS Platform Options](platform_slxos.md)
  - [VOSS Platform Options](platform_voss.md)
  - [VyOS Platform Options](platform_vyos.md)
  - [WeOS 4 Platform Options](platform_weos4.md)
  - [Netconf enabled Platform Options](platform_netconf_enabled.md)
  - [Settings by Platform](platform_index.md#settings-by-platform)
