---
collection: ansible
version: "8"
title: "CNOS Platform Options"
source_url: https://docs.ansible.com/projects/ansible/8/network/user_guide/platform_cnos.html
fetched_at: 2026-07-28T01:00:59+00:00
---
# CNOS Platform Options

CNOS is part of the [community.network](https://galaxy.ansible.com/ui/repo/published/community/network) collection and supports Enable Mode (Privilege Escalation). This page offers details on how to use Enable Mode on CNOS in Ansible.

- [Connections available](platform_cnos.md#connections-available)
- [Using CLI in Ansible](platform_cnos.md#using-cli-in-ansible)

  - [Example CLI `group_vars/cnos.yml`](platform_cnos.md#example-cli-group-vars-cnos-yml)
  - [Example CLI task](platform_cnos.md#example-cli-task)

## [Connections available](platform_cnos.md#id2)

|  | CLI |
| --- | --- |
| Protocol | SSH |
| Credentials | uses SSH keys / SSH-agent if present  accepts `-u myuser -k` if using password |
| Indirect Access | by a bastion (jump host) |
| Connection Settings | `ansible_connection: ansible.netcommon.network_cli` |
| Enable Mode   (Privilege Escalation) | supported: use `ansible_become: true` with `ansible_become_method: enable` and `ansible_become_password:` |
| Returned Data Format | `stdout[0].` |

The `ansible_connection: local` has been deprecated. Please use `ansible_connection: ansible.netcommon.network_cli` instead.

## [Using CLI in Ansible](platform_cnos.md#id3)

### [Example CLI `group_vars/cnos.yml`](platform_cnos.md#id4)

```yaml
ansible_connection: ansible.netcommon.network_cli
ansible_network_os: community.network.cnos
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

### [Example CLI task](platform_cnos.md#id5)

```yaml
- name: Retrieve CNOS OS version
  community.network.cnos_command:
    commands: show version
  when: ansible_network_os == 'community.network.cnos'
```

> **Warning:**
>
> Never store passwords in plain text. We recommend using SSH keys to authenticate SSH connections. Ansible supports ssh-agent to manage your SSH keys. If you must use passwords to authenticate SSH connections, we recommend encrypting them with [Ansible Vault](../../vault_guide/vault_using_encrypted_content.md#playbooks-vault).

> **See also:**
>
> [Setting timeout options](../getting_started/network_connection_options.md#timeout-options)
