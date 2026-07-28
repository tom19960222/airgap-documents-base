---
collection: ansible
version: "6"
title: "IronWare Platform Options"
source_url: https://docs.ansible.com/projects/ansible/6/network/user_guide/platform_ironware.html
fetched_at: 2026-07-27T16:41:11+00:00
---
# IronWare Platform Options

IronWare is part of the [community.network](https://galaxy.ansible.com/community/network) collection and supports Enable Mode (Privilege Escalation). This page offers details on how to use Enable Mode on IronWare in Ansible.

- [Connections available](platform_ironware.md#connections-available)
- [Using CLI in Ansible](platform_ironware.md#using-cli-in-ansible)

  - [Example CLI `group_vars/mlx.yml`](platform_ironware.md#example-cli-group-vars-mlx-yml)
  - [Example CLI task](platform_ironware.md#example-cli-task)

## [Connections available](platform_ironware.md#id2)

|  | CLI |
| --- | --- |
| Protocol | SSH |
| Credentials | uses SSH keys / SSH-agent if present  accepts `-u myuser -k` if using password |
| Indirect Access | via a bastion (jump host) |
| Connection Settings | `ansible_connection: ansible.netcommon.network_cli` |
| Enable Mode   (Privilege Escalation) | supported: use `ansible_become: yes` with `ansible_become_method: enable` and `ansible_become_password:` |
| Returned Data Format | `stdout[0].` |

The `ansible_connection: local` has been deprecated. Please use `ansible_connection: ansible.netcommon.network_cli` instead.

## [Using CLI in Ansible](platform_ironware.md#id3)

### [Example CLI `group_vars/mlx.yml`](platform_ironware.md#id4)

```yaml
ansible_connection: ansible.netcommon.network_cli
ansible_network_os: community.network.ironware
ansible_user: myuser
ansible_password: !vault...
ansible_become: yes
ansible_become_method: enable
ansible_become_password: !vault...
ansible_ssh_common_args: '-o ProxyCommand="ssh -W %h:%p -q bastion01"'
```

- If you are using SSH keys (including an ssh-agent) you can remove the `ansible_password` configuration.
- If you are accessing your host directly (not through a bastion/jump host) you can remove the `ansible_ssh_common_args` configuration.
- If you are accessing your host through a bastion/jump host, you cannot include your SSH password in the `ProxyCommand` directive. To prevent secrets from leaking out (for example in `ps` output), SSH does not support providing passwords via environment variables.

### [Example CLI task](platform_ironware.md#id5)

```yaml
- name: Backup current switch config (ironware)
  community.network.ironware_config:
    backup: yes
  register: backup_ironware_location
  when: ansible_network_os == 'community.network.ironware'
```

> **Warning:**
>
> Never store passwords in plain text. We recommend using SSH keys to authenticate SSH connections. Ansible supports ssh-agent to manage your SSH keys. If you must use passwords to authenticate SSH connections, we recommend encrypting them with [Ansible Vault](../../user_guide/vault.md#playbooks-vault).

> **See also:**
>
> [Setting timeout options](../getting_started/network_connection_options.md#timeout-options)
