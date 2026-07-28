---
collection: ansible
version: "8"
title: "Dell OS10 Platform Options"
source_url: https://docs.ansible.com/projects/ansible/8/network/user_guide/platform_dellos10.html
fetched_at: 2026-07-28T01:01:01+00:00
---
# Dell OS10 Platform Options

The [dellemc.os10](https://galaxy.ansible.com/ui/repo/published/dellemc_networking/os10) collection supports Enable Mode (Privilege Escalation). This page offers details on how to use Enable Mode on OS10 in Ansible.

- [Connections available](platform_dellos10.md#connections-available)
- [Using CLI in Ansible](platform_dellos10.md#using-cli-in-ansible)

  - [Example CLI `group_vars/dellos10.yml`](platform_dellos10.md#example-cli-group-vars-dellos10-yml)
  - [Example CLI task](platform_dellos10.md#example-cli-task)

## [Connections available](platform_dellos10.md#id1)

|  | CLI |
| --- | --- |
| Protocol | SSH |
| Credentials | uses SSH keys / SSH-agent if present  accepts `-u myuser -k` if using password |
| Indirect Access | through a bastion (jump host) |
| Connection Settings | `ansible_connection: ansible.netcommon.network_cli` |
| Enable Mode   (Privilege Escalation) | supported: use `ansible_become: true` with `ansible_become_method: enable` and `ansible_become_password:` |
| Returned Data Format | `stdout[0].` |

The `ansible_connection: local` has been deprecated. Please use `ansible_connection: ansible.netcommon.network_cli` instead.

## [Using CLI in Ansible](platform_dellos10.md#id2)

### [Example CLI `group_vars/dellos10.yml`](platform_dellos10.md#id3)

```yaml
ansible_connection: ansible.netcommon.network_cli
ansible_network_os: dellemc.os10.os10
ansible_user: myuser
ansible_password: !vault...
ansible_become: true
ansible_become_method: enable
ansible_become_password: !vault...
ansible_ssh_common_args: '-o ProxyCommand="ssh -W %h:%p -q bastion01"'
```

- If you are using SSH keys (including an ssh-agent) you can remove the `ansible_password` configuration.
- If you are accessing your host directly (not through a bastion/jump host) you can remove the `ansible_ssh_common_args` configuration.
- If you are accessing your host through a bastion/jump host, you cannot include your SSH password in the `ProxyCommand` directive. To prevent secrets from leaking out (for example in `ps` output), SSH does not support providing passwords through environment variables.

### [Example CLI task](platform_dellos10.md#id4)

```yaml
- name: Backup current switch config (dellos10)
  dellemc.os10.os10_config:
    backup: yes
  register: backup_dellos10_location
  when: ansible_network_os == 'dellemc.os10.os10'
```

> **Warning:**
>
> Never store passwords in plain text. We recommend using SSH keys to authenticate SSH connections. Ansible supports ssh-agent to manage your SSH keys. If you must use passwords to authenticate SSH connections, we recommend encrypting them with [Ansible Vault](../../vault_guide/vault_using_encrypted_content.md#playbooks-vault).

> **See also:**
>
> [Setting timeout options](../getting_started/network_connection_options.md#timeout-options)
