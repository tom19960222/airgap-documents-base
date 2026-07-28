---
collection: ansible
version: "6"
title: "FRR Platform Options"
source_url: https://docs.ansible.com/projects/ansible/6/network/user_guide/platform_frr.html
fetched_at: 2026-07-27T16:41:09+00:00
---
# FRR Platform Options

The [FRR](https://galaxy.ansible.com/frr/frr) collection supports the `ansible.netcommon.network_cli` connection. This section provides details on how to use this connection for Free Range Routing (FRR).

- [Connections available](platform_frr.md#connections-available)
- [Using CLI in Ansible](platform_frr.md#using-cli-in-ansible)

  - [Example CLI `group_vars/frr.yml`](platform_frr.md#example-cli-group-vars-frr-yml)
  - [Example CLI task](platform_frr.md#example-cli-task)

## [Connections available](platform_frr.md#id2)

|  | CLI |
| --- | --- |
| Protocol | SSH |
| Credentials | uses SSH keys / SSH-agent if present  accepts `-u myuser -k` if using password |
| Indirect Access | via a bastion (jump host) |
| Connection Settings | `ansible_connection: ansible.netcommon.network_cli` |
| Enable Mode   (Privilege Escalation) | not supported |
| Returned Data Format | `stdout[0].` |

## [Using CLI in Ansible](platform_frr.md#id3)

### [Example CLI `group_vars/frr.yml`](platform_frr.md#id4)

```yaml
ansible_connection: ansible.netcommon.network_cli
ansible_network_os: frr.frr.frr
ansible_user: frruser
ansible_password: !vault...
ansible_ssh_common_args: '-o ProxyCommand="ssh -W %h:%p -q bastion01"'
```

- The `ansible_user` should be a part of the `frrvty` group and should have the default shell set to `/bin/vtysh`.
- If you are using SSH keys (including an ssh-agent) you can remove the `ansible_password` configuration.
- If you are accessing your host directly (not through a bastion/jump host) you can remove the `ansible_ssh_common_args` configuration.
- If you are accessing your host through a bastion/jump host, you cannot include your SSH password in the `ProxyCommand` directive. To prevent secrets from leaking out (for example in `ps` output), SSH does not support providing passwords via environment variables.

### [Example CLI task](platform_frr.md#id5)

```yaml
- name: Gather FRR facts
  frr.frr.frr_facts:
    gather_subset:
     - config
     - hardware
```

> **Warning:**
>
> Never store passwords in plain text. We recommend using SSH keys to authenticate SSH connections. Ansible supports ssh-agent to manage your SSH keys. If you must use passwords to authenticate SSH connections, we recommend encrypting them with [Ansible Vault](../../user_guide/vault.md#playbooks-vault).

> **See also:**
>
> [Setting timeout options](../getting_started/network_connection_options.md#timeout-options)
