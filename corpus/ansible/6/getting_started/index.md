---
collection: ansible
version: "6"
title: "Getting started with Ansible"
source_url: https://docs.ansible.com/projects/ansible/6/getting_started/index.html
fetched_at: 2026-07-27T16:39:22+00:00
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

[![Basic components of an Ansible environment include a control node, an inventory of managed nodes, and a module copied to each managed node.](../_images/ansible_basic.svg)](https://docs.ansible.com/projects/ansible/6/_images/ansible_basic.svg)

Ready to start using Ansible?
Complete the following steps to get up and running:

1. Install Ansible. Visit the [installation guide](../installation_guide/intro_installation.md#installation-guide) for complete details.

   ```bash
   python3 -m pip install --user ansible
   ```
2. Create an inventory by adding the IP address or fully qualified domain name (FQDN) of one or more remote systems to `/etc/ansible/hosts`.
   The following example adds the IP addresses of three virtual machines in KVM:

   ```ini
   [myvirtualmachines]
   192.0.2.50
   192.0.2.51
   192.0.2.52
   ```
3. Verify the hosts in your inventory.

   ```bash
   ansible all --list-hosts
   ```

   ```ansible-output
   hosts (1):
     192.0.2.50
     192.0.2.51
     192.0.2.52
   ```
4. Set up SSH connections so Ansible can connect to the managed nodes.

   1. Add your public SSH key to the `authorized_keys` file on each remote system.
   2. Test the SSH connections, for example:

   ```bash
   ssh username@192.0.2.50
   ```

   If the username on the control node is different on the host, you need to pass the `-u` option with the `ansible` command.
5. Ping the managed nodes.

   ```bash
   ansible all -m ping
   ```

   ```
   192.0.2.50 | SUCCESS => {
     "ansible_facts": {
       "discovered_interpreter_python": "/usr/bin/python3"
       },
       "changed": false,
       "ping": "pong"
       }
   192.0.2.51 | SUCCESS => {
     "ansible_facts": {
       "discovered_interpreter_python": "/usr/bin/python3"
       },
       "changed": false,
       "ping": "pong"
       }
   192.0.2.52 | SUCCESS => {
     "ansible_facts": {
       "discovered_interpreter_python": "/usr/bin/python3"
       },
       "changed": false,
       "ping": "pong"
       }
   ```

Congratulations! You are now using Ansible.
Continue by [learning how to build an inventory](get_started_inventory.md#get-started-inventory).

> **See also:**
>
> [Ansible Demos](https://github.com/ansible/product-demos)
> :   Demonstrations of different Ansible usecases
>
> [RHEL Labs](https://katacoda.com/rhel-labs)
> :   Labs to provide further knowledge on different topics
>
> [Mailing List](https://groups.google.com/group/ansible-project)
> :   Questions? Help? Ideas? Stop by the list on Google Groups
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels

- [Building an inventory](get_started_inventory.md)
- [Creating a playbook](get_started_playbook.md)
