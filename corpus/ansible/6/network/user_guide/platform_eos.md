---
collection: ansible
version: "6"
title: "EOS Platform Options"
source_url: https://docs.ansible.com/projects/ansible/6/network/user_guide/platform_eos.html
fetched_at: 2026-07-27T16:41:08+00:00
---
# EOS Platform Options

The [Arista EOS](https://galaxy.ansible.com/arista/eos) collection supports multiple connections. This page offers details on how each connection works in Ansible and how to use it.

- [Connections available](platform_eos.md#connections-available)
- [Using CLI in Ansible](platform_eos.md#using-cli-in-ansible)

  - [Example CLI `group_vars/eos.yml`](platform_eos.md#example-cli-group-vars-eos-yml)
  - [Example CLI task](platform_eos.md#example-cli-task)
- [Using eAPI in Ansible](platform_eos.md#using-eapi-in-ansible)

  - [Enabling eAPI](platform_eos.md#enabling-eapi)
  - [Example eAPI `group_vars/eos.yml`](platform_eos.md#example-eapi-group-vars-eos-yml)
  - [Example eAPI task](platform_eos.md#example-eapi-task)

## [Connections available](platform_eos.md#id2)

|  | CLI | eAPI |
| --- | --- | --- |
| Protocol | SSH | HTTP(S) |
| Credentials | uses SSH keys / SSH-agent if present  accepts `-u myuser -k` if using password | uses HTTPS certificates if present |
| Indirect Access | via a bastion (jump host) | via a web proxy |
| Connection Settings | `ansible_connection:` `ansible.netcommon.network_cli` | `ansible_connection:` `ansible.netcommon.httpapi` |
| Enable Mode   (Privilege Escalation) | supported:   - use `ansible_become: yes`   with `ansible_become_method: enable` | supported:   - `httpapi`   uses `ansible_become: yes`   with `ansible_become_method: enable` |
| Returned Data Format | `stdout[0].` | `stdout[0].messages[0].` |

The `ansible_connection: local` has been deprecated. Please use `ansible_connection: ansible.netcommon.network_cli` or `ansible_connection: ansible.netcommon.httpapi` instead.

## [Using CLI in Ansible](platform_eos.md#id3)

### [Example CLI `group_vars/eos.yml`](platform_eos.md#id4)

```yaml
ansible_connection: ansible.netcommon.network_cli
ansible_network_os: arista.eos.eos
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

### [Example CLI task](platform_eos.md#id5)

```yaml
- name: Backup current switch config (eos)
  arista.eos.eos_config:
    backup: yes
  register: backup_eos_location
  when: ansible_network_os == 'arista.eos.eos'
```

## [Using eAPI in Ansible](platform_eos.md#id6)

### [Enabling eAPI](platform_eos.md#id7)

Before you can use eAPI to connect to a switch, you must enable eAPI. To enable eAPI on a new switch with Ansible, use the `arista.eos.eos_eapi` module through the CLI connection. Set up `group_vars/eos.yml` just like in the CLI example above, then run a playbook task like this:

```yaml
- name: Enable eAPI
  arista.eos.eos_eapi:
    enable_http: yes
    enable_https: yes
  become: true
  become_method: enable
  when: ansible_network_os == 'arista.eos.eos'
```

You can find more options for enabling HTTP/HTTPS connections in the [arista.eos.eos_eapi](../../collections/arista/eos/eos_eapi_module.md#ansible-collections-arista-eos-eos-eapi-module) module documentation.

Once eAPI is enabled, change your `group_vars/eos.yml` to use the eAPI connection.

### [Example eAPI `group_vars/eos.yml`](platform_eos.md#id8)

```yaml
ansible_connection: ansible.netcommon.httpapi
ansible_network_os: arista.eos.eos
ansible_user: myuser
ansible_password: !vault...
ansible_become: yes
ansible_become_method: enable
proxy_env:
  http_proxy: http://proxy.example.com:8080
```

- If you are accessing your host directly (not through a web proxy) you can remove the `proxy_env` configuration.
- If you are accessing your host through a web proxy using `https`, change `http_proxy` to `https_proxy`.

### [Example eAPI task](platform_eos.md#id9)

```yaml
- name: Backup current switch config (eos)
  arista.eos.eos_config:
    backup: yes
  register: backup_eos_location
  environment: "{{ proxy_env }}"
  when: ansible_network_os == 'arista.eos.eos'
```

In this example the `proxy_env` variable defined in `group_vars` gets passed to the `environment` option of the module in the task.

> **Warning:**
>
> Never store passwords in plain text. We recommend using SSH keys to authenticate SSH connections. Ansible supports ssh-agent to manage your SSH keys. If you must use passwords to authenticate SSH connections, we recommend encrypting them with [Ansible Vault](../../user_guide/vault.md#playbooks-vault).

> **See also:**
>
> [Setting timeout options](../getting_started/network_connection_options.md#timeout-options)
