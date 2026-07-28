---
collection: ansible
version: "8"
title: "Start using Ansible"
source_url: https://docs.ansible.com/projects/ansible/8/getting_started/get_started_ansible.html
fetched_at: 2026-07-28T00:58:11+00:00
---
# Start using Ansible

Start automating with Ansible in a few easy steps.

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
> [Ansible Labs](https://www.ansible.com/products/ansible-training)
> :   Labs to provide further knowledge on different topics
>
> [Mailing List](https://groups.google.com/group/ansible-project)
> :   Questions? Help? Ideas? Stop by the list on Google Groups
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
