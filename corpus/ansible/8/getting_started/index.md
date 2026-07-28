---
collection: ansible
version: "8"
title: "Getting started with Ansible"
source_url: https://docs.ansible.com/projects/ansible/8/getting_started/index.html
fetched_at: 2026-07-28T00:57:39+00:00
---
# Getting started with Ansible

Ansible automates the management of remote systems and controls their desired state.
A basic Ansible environment has three main components:

Control node
:   A system on which Ansible is installed.
    You run Ansible commands such as `ansible` or `ansible-inventory` on a control node.

Managed node
:   A remote system, or host, that Ansible controls.

Inventory
:   A list of managed nodes that are logically organized.
    You create an inventory on the control node to describe host deployments to Ansible.

[![Basic components of an Ansible environment include a control node, an inventory of managed nodes, and a module copied to each managed node.](../_images/ansible_basic.svg)](https://docs.ansible.com/projects/ansible/8/_images/ansible_basic.svg)

- [Introduction to Ansible](introduction.md)
- [Start using Ansible](get_started_ansible.md)
- [Building an inventory](get_started_inventory.md)
- [Creating a playbook](get_started_playbook.md)
- [Ansible concepts](basic_concepts.md)
