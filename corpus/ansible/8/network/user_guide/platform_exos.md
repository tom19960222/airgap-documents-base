---
collection: ansible
version: "8"
title: "EXOS Platform Options"
source_url: https://docs.ansible.com/projects/ansible/8/network/user_guide/platform_exos.html
fetched_at: 2026-07-28T01:01:04+00:00
---
# EXOS Platform Options

Extreme EXOS is part of the [community.network](https://galaxy.ansible.com/ui/repo/published/community/network) collection and supports multiple connections. This page offers details on how each connection works in Ansible and how to use it.

- [Connections available](platform_exos.md#connections-available)
- [Using CLI in Ansible](platform_exos.md#using-cli-in-ansible)

  - [Example CLI `group_vars/exos.yml`](platform_exos.md#example-cli-group-vars-exos-yml)
  - [Example CLI task](platform_exos.md#example-cli-task)
- [Using EXOS-API in Ansible](platform_exos.md#using-exos-api-in-ansible)

  - [Example EXOS-API `group_vars/exos.yml`](platform_exos.md#example-exos-api-group-vars-exos-yml)
  - [Example EXOS-API task](platform_exos.md#example-exos-api-task)

## [Connections available](platform_exos.md#id2)

|  | CLI | EXOS-API |
| --- | --- | --- |
| Protocol | SSH | HTTP(S) |
| Credentials | uses SSH keys / SSH-agent if present  accepts `-u myuser -k` if using password | uses HTTPS certificates if present |
| Indirect Access | by a bastion (jump host) | through a web proxy |
| Connection Settings | `ansible_connection:`  `ansible.netcommon.network_cli` | `ansible_connection:`  `ansible.netcommon.httpapi` |
| Enable Mode   (Privilege Escalation) | not supported by EXOS | not supported by EXOS |
| Returned Data Format | `stdout[0].` | `stdout[0].messages[0].` |

EXOS does not support `ansible_connection: local`. You must use `ansible_connection: ansible.netcommon.network_cli` or `ansible_connection: ansible.netcommon.httpapi`.

## [Using CLI in Ansible](platform_exos.md#id3)

### [Example CLI `group_vars/exos.yml`](platform_exos.md#id4)

```yaml
ansible_connection: ansible.netcommon.network_cli
ansible_network_os: community.network.exos
ansible_user: myuser
ansible_password: !vault...
ansible_ssh_common_args: '-o ProxyCommand="ssh -W %h:%p -q bastion01"'
```

- If you are using SSH keys (including an ssh-agent) you can remove the `ansible_password` configuration.
- If you are accessing your host directly (not through a bastion/jump host) you can remove the `ansible_ssh_common_args` configuration.
- If you are accessing your host through a bastion/jump host, you cannot include your SSH password in the `ProxyCommand` directive. To prevent secrets from leaking out (for example in `ps` output), SSH does not support providing passwords through environment variables.

### [Example CLI task](platform_exos.md#id5)

```yaml
- name: Retrieve EXOS OS version
  community.network.exos_command:
    commands: show version
  when: ansible_network_os == 'community.network.exos'
```

## [Using EXOS-API in Ansible](platform_exos.md#id6)

### [Example EXOS-API `group_vars/exos.yml`](platform_exos.md#id7)

```yaml
ansible_connection: ansible.netcommon.httpapi
ansible_network_os: community.network.exos
ansible_user: myuser
ansible_password: !vault...
proxy_env:
  http_proxy: http://proxy.example.com:8080
```

- If you are accessing your host directly (not through a web proxy) you can remove the `proxy_env` configuration.
- If you are accessing your host through a web proxy using `https`, change `http_proxy` to `https_proxy`.

### [Example EXOS-API task](platform_exos.md#id8)

```yaml
- name: Retrieve EXOS OS version
  community.network.exos_command:
    commands: show version
  when: ansible_network_os == 'community.network.exos'
```

In this example the `proxy_env` variable defined in `group_vars` gets passed to the `environment` option of the module used in the task.

> **Warning:**
>
> Never store passwords in plain text. We recommend using SSH keys to authenticate SSH connections. Ansible supports ssh-agent to manage your SSH keys. If you must use passwords to authenticate SSH connections, we recommend encrypting them with [Ansible Vault](../../vault_guide/vault_using_encrypted_content.md#playbooks-vault).

> **See also:**
>
> [Setting timeout options](../getting_started/network_connection_options.md#timeout-options)
