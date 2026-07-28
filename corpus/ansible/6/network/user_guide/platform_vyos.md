---
collection: ansible
version: "6"
title: "VyOS Platform Options"
source_url: https://docs.ansible.com/projects/ansible/6/network/user_guide/platform_vyos.html
fetched_at: 2026-07-27T16:41:14+00:00
---
# VyOS Platform Options

The [VyOS](https://galaxy.ansible.com/vyos/vyos) collection supports the `ansible.netcommon.network_cli` connection type. This page offers details on connection options to manage VyOS using Ansible.

- [Connections available](platform_vyos.md#connections-available)
- [Using CLI in Ansible](platform_vyos.md#using-cli-in-ansible)

  - [Example CLI `group_vars/vyos.yml`](platform_vyos.md#example-cli-group-vars-vyos-yml)
  - [Example CLI task](platform_vyos.md#example-cli-task)

## [Connections available](platform_vyos.md#id2)

|  | CLI |
| --- | --- |
| Protocol | SSH |
| Credentials | uses SSH keys / SSH-agent if present  accepts `-u myuser -k` if using password |
| Indirect Access | via a bastion (jump host) |
| Connection Settings | `ansible_connection: ansible.netcommon.network_cli` |
| Enable Mode   (Privilege Escalation) | not supported |
| Returned Data Format | Refer to individual module documentation |

The `ansible_connection: local` has been deprecated. Please use `ansible_connection: ansible.netcommon.network_cli` instead.

## [Using CLI in Ansible](platform_vyos.md#id3)

### [Example CLI `group_vars/vyos.yml`](platform_vyos.md#id4)

```yaml
ansible_connection: ansible.netcommon.network_cli
ansible_network_os: vyos.vyos.vyos
ansible_user: myuser
ansible_password: !vault...
ansible_ssh_common_args: '-o ProxyCommand="ssh -W %h:%p -q bastion01"'
```

- If you are using SSH keys (including an ssh-agent) you can remove the `ansible_password` configuration.
- If you are accessing your host directly (not through a bastion/jump host) you can remove the `ansible_ssh_common_args` configuration.
- If you are accessing your host through a bastion/jump host, you cannot include your SSH password in the `ProxyCommand` directive. To prevent secrets from leaking out (for example in `ps` output), SSH does not support providing passwords via environment variables.

### [Example CLI task](platform_vyos.md#id5)

```yaml
- name: Retrieve VyOS version info
  vyos.vyos.vyos_command:
    commands: show version
  when: ansible_network_os == 'vyos.vyos.vyos'
```

> **Warning:**
>
> Never store passwords in plain text. We recommend using SSH keys to authenticate SSH connections. Ansible supports ssh-agent to manage your SSH keys. If you must use passwords to authenticate SSH connections, we recommend encrypting them with [Ansible Vault](../../user_guide/vault.md#playbooks-vault).

> **See also:**
>
> [Setting timeout options](../getting_started/network_connection_options.md#timeout-options)
