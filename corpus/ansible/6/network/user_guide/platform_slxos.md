---
collection: ansible
version: "6"
title: "SLX-OS Platform Options"
source_url: https://docs.ansible.com/projects/ansible/6/network/user_guide/platform_slxos.html
fetched_at: 2026-07-27T16:41:14+00:00
---
# SLX-OS Platform Options

Extreme SLX-OS is part of the [community.network](https://galaxy.ansible.com/community/network) collection and only supports CLI connections today. `httpapi` modules may be added in future.
This page offers details on how to use `ansible.netcommon.network_cli` on SLX-OS in Ansible.

- [Connections available](platform_slxos.md#connections-available)
- [Using CLI in Ansible](platform_slxos.md#using-cli-in-ansible)

  - [Example CLI `group_vars/slxos.yml`](platform_slxos.md#example-cli-group-vars-slxos-yml)
  - [Example CLI task](platform_slxos.md#example-cli-task)

## [Connections available](platform_slxos.md#id1)

|  | CLI |
| --- | --- |
| Protocol | SSH |
| Credentials | uses SSH keys / SSH-agent if present  accepts `-u myuser -k` if using password |
| Indirect Access | via a bastion (jump host) |
| Connection Settings | `ansible_connection: ansible.netcommon.network_cli` |
| Enable Mode   (Privilege Escalation) | not supported by SLX-OS |
| Returned Data Format | `stdout[0].` |

SLX-OS does not support `ansible_connection: local`. You must use `ansible_connection: ansible.netcommon.network_cli`.

## [Using CLI in Ansible](platform_slxos.md#id2)

### [Example CLI `group_vars/slxos.yml`](platform_slxos.md#id3)

```yaml
ansible_connection: ansible.netcommon.network_cli
ansible_network_os: community.network.slxos
ansible_user: myuser
ansible_password: !vault...
ansible_ssh_common_args: '-o ProxyCommand="ssh -W %h:%p -q bastion01"'
```

- If you are using SSH keys (including an ssh-agent) you can remove the `ansible_password` configuration.
- If you are accessing your host directly (not through a bastion/jump host) you can remove the `ansible_ssh_common_args` configuration.
- If you are accessing your host through a bastion/jump host, you cannot include your SSH password in the `ProxyCommand` directive. To prevent secrets from leaking out (for example in `ps` output), SSH does not support providing passwords via environment variables.

### [Example CLI task](platform_slxos.md#id4)

```yaml
- name: Backup current switch config (slxos)
  community.network.slxos_config:
    backup: yes
  register: backup_slxos_location
  when: ansible_network_os == 'community.network.slxos'
```

> **Warning:**
>
> Never store passwords in plain text. We recommend using SSH keys to authenticate SSH connections. Ansible supports ssh-agent to manage your SSH keys. If you must use passwords to authenticate SSH connections, we recommend encrypting them with [Ansible Vault](../../user_guide/vault.md#playbooks-vault).

> **See also:**
>
> [Setting timeout options](../getting_started/network_connection_options.md#timeout-options)
