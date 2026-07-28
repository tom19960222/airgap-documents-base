---
collection: ansible
version: "6"
title: "ERIC_ECCLI Platform Options"
source_url: https://docs.ansible.com/projects/ansible/6/network/user_guide/platform_eric_eccli.html
fetched_at: 2026-07-27T16:41:09+00:00
---
# ERIC_ECCLI Platform Options

Extreme ERIC_ECCLI is part of the [community.network](https://galaxy.ansible.com/community/network) collection and only supports CLI connections today. This page offers details on how to use `ansible.netcommon.network_cli` on ERIC_ECCLI in Ansible.

- [Connections available](platform_eric_eccli.md#connections-available)
- [Using CLI in Ansible](platform_eric_eccli.md#using-cli-in-ansible)

  - [Example CLI `group_vars/eric_eccli.yml`](platform_eric_eccli.md#example-cli-group-vars-eric-eccli-yml)
  - [Example CLI task](platform_eric_eccli.md#example-cli-task)

## [Connections available](platform_eric_eccli.md#id1)

|  | CLI |
| --- | --- |
| Protocol | SSH |
| Credentials | uses SSH keys / SSH-agent if present  accepts `-u myuser -k` if using password |
| Indirect Access | via a bastion (jump host) |
| Connection Settings | `ansible_connection: ansible.netcommon.network_cli` |
| Enable Mode   (Privilege Escalation) | not supported by ERIC_ECCLI |
| Returned Data Format | `stdout[0].` |

ERIC_ECCLI does not support `ansible_connection: local`. You must use `ansible_connection: ansible.netcommon.network_cli`.

## [Using CLI in Ansible](platform_eric_eccli.md#id2)

### [Example CLI `group_vars/eric_eccli.yml`](platform_eric_eccli.md#id3)

```yaml
ansible_connection: ansible.netcommon.network_cli
ansible_network_os: community.network.eric_eccli
ansible_user: myuser
ansible_password: !vault...
ansible_ssh_common_args: '-o ProxyCommand="ssh -W %h:%p -q bastion01"'
```

- If you are using SSH keys (including an ssh-agent) you can remove the `ansible_password` configuration.
- If you are accessing your host directly (not through a bastion/jump host) you can remove the `ansible_ssh_common_args` configuration.
- If you are accessing your host through a bastion/jump host, you cannot include your SSH password in the `ProxyCommand` directive. To prevent secrets from leaking out (for example in `ps` output), SSH does not support providing passwords via environment variables.

### [Example CLI task](platform_eric_eccli.md#id4)

```yaml
- name: run show version on remote devices (eric_eccli)
  community.network.eric_eccli_command:
     commands: show version
  when: ansible_network_os == 'community.network.eric_eccli'
```

> **Warning:**
>
> Never store passwords in plain text. We recommend using SSH keys to authenticate SSH connections. Ansible supports ssh-agent to manage your SSH keys. If you must use passwords to authenticate SSH connections, we recommend encrypting them with [Ansible Vault](../../user_guide/vault.md#playbooks-vault).

> **See also:**
>
> [Setting timeout options](../getting_started/network_connection_options.md#timeout-options)
