---
collection: ansible
version: "8"
title: "Building Ansible inventories"
source_url: https://docs.ansible.com/projects/ansible/8/inventory_guide/index.html
fetched_at: 2026-07-28T00:57:41+00:00
---
# Building Ansible inventories

> **Note:**
>
> **Making Open Source More Inclusive**
>
> Red Hat is committed to replacing problematic language in our code, documentation, and web properties. We are beginning with these four terms: master, slave, blacklist, and whitelist. We ask that you open an issue or pull request if you come upon a term that we have missed. For more details, see [our CTO Chris Wright’s message](https://www.redhat.com/en/blog/making-open-source-more-inclusive-eradicating-problematic-language).

Welcome to the guide to building Ansible inventories.
An inventory is a list of managed nodes, or hosts, that Ansible deploys and configures.
This guide introduces you to inventories and covers the following topics:

- Creating inventories to track a list of servers and devices that you want to automate.
- Using dynamic inventories to track cloud services with servers and devices that are constantly starting and stopping.
- Using patterns to automate specific sub-sets of an inventory.
- Expanding and refining the connection methods Ansible uses for your inventory.

- [How to build your inventory](intro_inventory.md)
  - [Inventory basics: formats, hosts, and groups](intro_inventory.md#inventory-basics-formats-hosts-and-groups)
  - [Passing multiple inventory sources](intro_inventory.md#passing-multiple-inventory-sources)
  - [Organizing inventory in a directory](intro_inventory.md#organizing-inventory-in-a-directory)
  - [Adding variables to inventory](intro_inventory.md#adding-variables-to-inventory)
  - [Assigning a variable to one machine: host variables](intro_inventory.md#assigning-a-variable-to-one-machine-host-variables)
  - [Defining variables in INI format](intro_inventory.md#defining-variables-in-ini-format)
  - [Assigning a variable to many machines: group variables](intro_inventory.md#assigning-a-variable-to-many-machines-group-variables)
  - [Organizing host and group variables](intro_inventory.md#organizing-host-and-group-variables)
  - [How variables are merged](intro_inventory.md#how-variables-are-merged)
  - [Connecting to hosts: behavioral inventory parameters](intro_inventory.md#connecting-to-hosts-behavioral-inventory-parameters)
  - [Inventory setup examples](intro_inventory.md#inventory-setup-examples)
- [Working with dynamic inventory](intro_dynamic_inventory.md)
  - [Inventory script example: Cobbler](intro_dynamic_inventory.md#inventory-script-example-cobbler)
  - [Inventory script example: OpenStack](intro_dynamic_inventory.md#inventory-script-example-openstack)
  - [Other inventory scripts](intro_dynamic_inventory.md#other-inventory-scripts)
  - [Using inventory directories and multiple inventory sources](intro_dynamic_inventory.md#using-inventory-directories-and-multiple-inventory-sources)
  - [Static groups of dynamic groups](intro_dynamic_inventory.md#static-groups-of-dynamic-groups)
- [Patterns: targeting hosts and groups](intro_patterns.md)
  - [Using patterns](intro_patterns.md#using-patterns)
  - [Common patterns](intro_patterns.md#common-patterns)
  - [Limitations of patterns](intro_patterns.md#limitations-of-patterns)
  - [Pattern processing order](intro_patterns.md#pattern-processing-order)
  - [Advanced pattern options](intro_patterns.md#advanced-pattern-options)
  - [Patterns and ad-hoc commands](intro_patterns.md#patterns-and-ad-hoc-commands)
  - [Patterns and ansible-playbook flags](intro_patterns.md#patterns-and-ansible-playbook-flags)
- [Connection methods and details](connection_details.md)
  - [ControlPersist and paramiko](connection_details.md#controlpersist-and-paramiko)
  - [Setting a remote user](connection_details.md#setting-a-remote-user)
  - [Setting up SSH keys](connection_details.md#setting-up-ssh-keys)
  - [Running against localhost](connection_details.md#running-against-localhost)
  - [Managing host key checking](connection_details.md#managing-host-key-checking)
  - [Other connection methods](connection_details.md#other-connection-methods)
