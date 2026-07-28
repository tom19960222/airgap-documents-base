---
collection: ansible
version: "8"
title: "Pluribus NETVISOR Platform Options"
source_url: https://docs.ansible.com/projects/ansible/8/network/user_guide/platform_netvisor.html
fetched_at: 2026-07-28T01:01:09+00:00
---
# Pluribus NETVISOR Platform Options

Pluribus NETVISOR Ansible is part of the [community.network](https://galaxy.ansible.com/ui/repo/published/community/network) collection and only supports CLI connections today. `httpapi` modules may be added in future.
This page offers details on how to use `ansible.netcommon.network_cli` on NETVISOR in Ansible.

- [Connections available](platform_netvisor.md#connections-available)
- [Using CLI in Ansible](platform_netvisor.md#using-cli-in-ansible)

  - [Example CLI `group_vars/netvisor.yml`](platform_netvisor.md#example-cli-group-vars-netvisor-yml)
  - [Example CLI task](platform_netvisor.md#example-cli-task)

## [Connections available](platform_netvisor.md#id1)

|  | CLI |
| --- | --- |
| Protocol | SSH |
| Credentials | uses SSH keys / SSH-agent if present  accepts `-u myuser -k` if using password |
| Indirect Access | by a bastion (jump host) |
| Connection Settings | `ansible_connection: ansible.netcommon.network_cli` |
| Enable Mode   (Privilege Escalation) | not supported by NETVISOR |
| Returned Data Format | `stdout[0].` |

Pluribus NETVISOR does not support `ansible_connection: local`. You must use `ansible_connection: ansible.netcommon.network_cli`.

## [Using CLI in Ansible](platform_netvisor.md#id2)

### [Example CLI `group_vars/netvisor.yml`](platform_netvisor.md#id3)

```yaml
ansible_connection: ansible.netcommon.network_cli
ansible_network_os: community.netcommon.netvisor
ansible_user: myuser
ansible_password: !vault...
ansible_ssh_common_args: '-o ProxyCommand="ssh -W %h:%p -q bastion01"'
```

- If you are using SSH keys (including an ssh-agent) you can remove the `ansible_password` configuration.
- If you are accessing your host directly (not through a bastion/jump host) you can remove the `ansible_ssh_common_args` configuration.
- If you are accessing your host through a bastion/jump host, you cannot include your SSH password in the `ProxyCommand` directive. To prevent secrets from leaking out (for example in `ps` output), SSH does not support providing passwords through environment variables.

### [Example CLI task](platform_netvisor.md#id4)

```yaml
- name: Create access list
  community.network.pn_access_list:
    pn_name: "foo"
    pn_scope: "local"
    state: "present"
  register: acc_list
  when: ansible_network_os == 'community.network.netvisor'
```

> **Warning:**
>
> Never store passwords in plain text. We recommend using SSH keys to authenticate SSH connections. Ansible supports ssh-agent to manage your SSH keys. If you must use passwords to authenticate SSH connections, we recommend encrypting them with [Ansible Vault](../../vault_guide/vault_using_encrypted_content.md#playbooks-vault).

> **See also:**
>
> [Setting timeout options](../getting_started/network_connection_options.md#timeout-options)
