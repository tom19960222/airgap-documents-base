---
collection: ansible
version: "6"
title: "WeOS 4 Platform Options"
source_url: https://docs.ansible.com/projects/ansible/6/network/user_guide/platform_weos4.html
fetched_at: 2026-07-27T16:41:15+00:00
---
# WeOS 4 Platform Options

Westermo WeOS 4 is part of the [community.network](https://galaxy.ansible.com/community/network) collection and only supports CLI connections.
This page offers details on how to use `ansible.netcommon.network_cli` on WeOS 4 in Ansible.

- [Connections available](platform_weos4.md#connections-available)
- [Using CLI in Ansible](platform_weos4.md#using-cli-in-ansible)

  - [Example CLI `group_vars/weos4.yml`](platform_weos4.md#example-cli-group-vars-weos4-yml)
  - [Example CLI task](platform_weos4.md#example-cli-task)
  - [Example Configuration task](platform_weos4.md#example-configuration-task)

## [Connections available](platform_weos4.md#id1)

|  | CLI |
| --- | --- |
| Protocol | SSH |
| Credentials | uses SSH keys / SSH-agent if present  accepts `-u myuser -k` if using password |
| Indirect Access | via a bastion (jump host) |
| Connection Settings | `ansible_connection: community.netcommon.network_cli` |
| Enable Mode   (Privilege Escalation) | not supported by WeOS 4 |
| Returned Data Format | `stdout[0].` |

WeOS 4 does not support `ansible_connection: local`. You must use `ansible_connection: ansible.netcommon.network_cli`.

## [Using CLI in Ansible](platform_weos4.md#id2)

### [Example CLI `group_vars/weos4.yml`](platform_weos4.md#id3)

```yaml
ansible_connection: ansible.netcommon.network_cli
ansible_network_os: community.network.weos4
ansible_user: myuser
ansible_password: !vault...
ansible_ssh_common_args: '-o ProxyCommand="ssh -W %h:%p -q bastion01"'
```

- If you are using SSH keys (including an ssh-agent) you can remove the `ansible_password` configuration.
- If you are accessing your host directly (not through a bastion/jump host) you can remove the `ansible_ssh_common_args` configuration.
- If you are accessing your host through a bastion/jump host, you cannot include your SSH password in the `ProxyCommand` directive. To prevent secrets from leaking out (for example in `ps` output), SSH does not support providing passwords via environment variables.

### [Example CLI task](platform_weos4.md#id4)

```yaml
- name: Get version information (WeOS 4)
  ansible.netcommon.cli_command:
    commands: "show version"
  register: show_ver
  when: ansible_network_os == 'community.network.weos4'
```

### [Example Configuration task](platform_weos4.md#id5)

```yaml
- name: Replace configuration with file on ansible host (WeOS 4)
  ansible.netcommon.cli_config:
    config: "{{ lookup('file', 'westermo.conf') }}"
    replace: "yes"
    diff_match: exact
    diff_replace: config
  when: ansible_network_os == 'community.network.weos4'
```

> **Warning:**
>
> Never store passwords in plain text. We recommend using SSH keys to authenticate SSH connections. Ansible supports ssh-agent to manage your SSH keys. If you must use passwords to authenticate SSH connections, we recommend encrypting them with [Ansible Vault](../../user_guide/vault.md#playbooks-vault).

> **See also:**
>
> [Setting timeout options](../getting_started/network_connection_options.md#timeout-options)
