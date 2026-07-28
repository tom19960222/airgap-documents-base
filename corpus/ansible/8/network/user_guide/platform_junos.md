---
collection: ansible
version: "8"
title: "Junos OS Platform Options"
source_url: https://docs.ansible.com/projects/ansible/8/network/user_guide/platform_junos.html
fetched_at: 2026-07-28T01:01:08+00:00
---
# Junos OS Platform Options

The [Juniper Junos OS](https://galaxy.ansible.com/ui/repo/published/junipernetworks/junos) supports multiple connections. This page offers details on how each connection works in Ansible and how to use it.

- [Connections available](platform_junos.md#connections-available)
- [Using CLI in Ansible](platform_junos.md#using-cli-in-ansible)

  - [Example CLI inventory `[junos:vars]`](platform_junos.md#example-cli-inventory-junos-vars)
  - [Example CLI task](platform_junos.md#example-cli-task)
- [Using NETCONF in Ansible](platform_junos.md#using-netconf-in-ansible)

  - [Enabling NETCONF](platform_junos.md#enabling-netconf)
  - [Example NETCONF inventory `[junos:vars]`](platform_junos.md#example-netconf-inventory-junos-vars)
  - [Example NETCONF task](platform_junos.md#example-netconf-task)

## [Connections available](platform_junos.md#id1)

|  | CLI  `junos_netconf` & `junos_command` modules only | NETCONF  all modules except `junos_netconf`, which enables NETCONF |
| --- | --- | --- |
| Protocol | SSH | XML over SSH |
| Credentials | uses SSH keys / SSH-agent if present  accepts `-u myuser -k` if using password | uses SSH keys / SSH-agent if present  accepts `-u myuser -k` if using password |
| Indirect Access | by a bastion (jump host) | by a bastion (jump host) |
| Connection Settings | ``` ansible_connection: ``ansible.netcommon.network_cli ``` | ``` ansible_connection: ``ansible.netcommon.netconf ``` |
| Enable Mode   (Privilege Escalation) | not supported by Junos OS | not supported by Junos OS |
| Returned Data Format | `stdout[0].` | - json: `result[0]['software-information'][0]['host-name'][0]['data'] foo lo0` - text: `result[1].interface-information[0].physical-interface[0].name[0].data foo lo0` - xml: `result[1].rpc-reply.interface-information[0].physical-interface[0].name[0].data foo lo0` |

The `ansible_connection: local` has been deprecated. Please use `ansible_connection: ansible.netcommon.network_cli` or `ansible_connection: ansible.netcommon.netconf` instead.

## [Using CLI in Ansible](platform_junos.md#id2)

### [Example CLI inventory `[junos:vars]`](platform_junos.md#id3)

```yaml
[junos:vars]
ansible_connection=ansible.netcommon.network_cli
ansible_network_os=junipernetworks.junos.junos
ansible_user=myuser
ansible_password=!vault...
ansible_ssh_common_args='-o ProxyCommand="ssh -W %h:%p -q bastion01"'
```

- If you are using SSH keys (including an ssh-agent) you can remove the `ansible_password` configuration.
- If you are accessing your host directly (not through a bastion/jump host) you can remove the `ansible_ssh_common_args` configuration.
- If you are accessing your host through a bastion/jump host, you cannot include your SSH password in the `ProxyCommand` directive. To prevent secrets from leaking out (for example in `ps` output), SSH does not support providing passwords through environment variables.

### [Example CLI task](platform_junos.md#id4)

```yaml
- name: Retrieve Junos OS version
  junipernetworks.junos.junos_command:
    commands: show version
  when: ansible_network_os == 'junipernetworks.junos.junos'
```

## [Using NETCONF in Ansible](platform_junos.md#id5)

### [Enabling NETCONF](platform_junos.md#id6)

Before you can use NETCONF to connect to a switch, you must:

- install the `ncclient` python package on your control node(s) with `pip install ncclient`
- enable NETCONF on the Junos OS device(s)

To enable NETCONF on a new switch through Ansible, use the `junipernetworks.junos.junos_netconf` module through the CLI connection. Set up your platform-level variables just like in the CLI example above, then run a playbook task like this:

```yaml
- name: Enable NETCONF
  connection: ansible.netcommon.network_cli
  junipernetworks.junos.junos_netconf:
  when: ansible_network_os == 'junipernetworks.junos.junos'
```

Once NETCONF is enabled, change your variables to use the NETCONF connection.

### [Example NETCONF inventory `[junos:vars]`](platform_junos.md#id7)

```yaml
[junos:vars]
ansible_connection=ansible.netcommon.netconf
ansible_network_os=junipernetworks.junos.junos
ansible_user=myuser
ansible_password=!vault |
ansible_ssh_common_args='-o ProxyCommand="ssh -W %h:%p -q bastion01"'
```

### [Example NETCONF task](platform_junos.md#id8)

```yaml
- name: Backup current switch config (junos)
  junipernetworks.junos.junos_config:
    backup: yes
  register: backup_junos_location
  when: ansible_network_os == 'junipernetworks.junos.junos'
```

> **Warning:**
>
> Never store passwords in plain text. We recommend using SSH keys to authenticate SSH connections. Ansible supports ssh-agent to manage your SSH keys. If you must use passwords to authenticate SSH connections, we recommend encrypting them with [Ansible Vault](../../vault_guide/vault_using_encrypted_content.md#playbooks-vault).

> **See also:**
>
> [Setting timeout options](../getting_started/network_connection_options.md#timeout-options)
