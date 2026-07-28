---
collection: ansible
version: "8"
title: "Network Getting Started"
source_url: https://docs.ansible.com/projects/ansible/8/network/getting_started/index.html
fetched_at: 2026-07-28T00:57:52+00:00
---
# Network Getting Started

Ansible collections support a wide range of vendors, device types, and actions, so you can manage your entire network with a single automation tool. With Ansible, you can:

- Automate repetitive tasks to speed routine network changes and free up your time for more strategic work
- Leverage the same simple, powerful, and agentless automation tool for network tasks that operations and development use
- Separate the data model (in a playbook or role) from the execution layer (through Ansible modules) to manage heterogeneous network devices
- Benefit from community and vendor-generated sample playbooks and roles to help accelerate network automation projects
- Communicate securely with network hardware over SSH or HTTPS

**Who should use this guide?**

This guide is intended for network engineers using Ansible for the first time. If you understand networks but have never used Ansible, work through the guide from start to finish.

This guide is also useful for experienced Ansible users automating network tasks for the first time. You can use Ansible commands, playbooks and modules to configure hubs, switches, routers, bridges and other network devices. But network modules are different from Linux/Unix and Windows modules, and you must understand some network-specific concepts to succeed. If you understand Ansible but have never automated a network task, start with the second section.

This guide introduces basic Ansible concepts and guides you through your first Ansible commands, playbooks and inventory entries.

Getting Started Guide

- [Basic Concepts](basic_concepts.md)
  - [Control node](basic_concepts.md#control-node)
  - [Managed nodes](basic_concepts.md#managed-nodes)
  - [Inventory](basic_concepts.md#inventory)
  - [Playbooks](basic_concepts.md#playbooks)
  - [Modules](basic_concepts.md#modules)
  - [Plugins](basic_concepts.md#plugins)
  - [Collections](basic_concepts.md#collections)
  - [AAP](basic_concepts.md#aap)
- [How Network Automation is Different](network_differences.md)
  - [Execution on the control node](network_differences.md#execution-on-the-control-node)
  - [Multiple communication protocols](network_differences.md#multiple-communication-protocols)
  - [Collections organized by network platform](network_differences.md#collections-organized-by-network-platform)
  - [Privilege Escalation: `enable` mode, `become`, and `authorize`](network_differences.md#privilege-escalation-enable-mode-become-and-authorize)
- [Run Your First Command and Playbook](first_playbook.md)
  - [Prerequisites](first_playbook.md#prerequisites)
  - [Install Ansible](first_playbook.md#install-ansible)
  - [Establish a manual connection to a managed node](first_playbook.md#establish-a-manual-connection-to-a-managed-node)
  - [Run your first network Ansible command](first_playbook.md#run-your-first-network-ansible-command)
  - [Create and run your first network Ansible Playbook](first_playbook.md#create-and-run-your-first-network-ansible-playbook)
  - [Gathering facts from network devices](first_playbook.md#gathering-facts-from-network-devices)
- [Build Your Inventory](first_inventory.md)
  - [Basic inventory](first_inventory.md#basic-inventory)
  - [Add variables to the inventory](first_inventory.md#add-variables-to-the-inventory)
  - [Group variables within inventory](first_inventory.md#group-variables-within-inventory)
  - [Variable syntax](first_inventory.md#variable-syntax)
  - [Group inventory by platform](first_inventory.md#group-inventory-by-platform)
  - [Verifying the inventory](first_inventory.md#verifying-the-inventory)
  - [Protecting sensitive variables with `ansible-vault`](first_inventory.md#protecting-sensitive-variables-with-ansible-vault)
- [Use Ansible network roles](network_roles.md)
  - [Understanding roles](network_roles.md#understanding-roles)
- [Beyond the basics](intermediate_concepts.md)
  - [A typical Ansible filetree](intermediate_concepts.md#a-typical-ansible-filetree)
  - [Tracking changes to inventory and playbooks: source control with git](intermediate_concepts.md#tracking-changes-to-inventory-and-playbooks-source-control-with-git)
- [Working with network connection options](network_connection_options.md)
  - [Setting timeout options](network_connection_options.md#setting-timeout-options)
- [Resources and next steps](network_resources.md)
  - [Documents](network_resources.md#documents)
  - [Events (on video and in person)](network_resources.md#events-on-video-and-in-person)
  - [GitHub repos](network_resources.md#github-repos)
  - [Chat channels](network_resources.md#chat-channels)
