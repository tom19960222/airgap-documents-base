---
collection: ansible
version: "8"
title: "RouterOS Platform Options"
source_url: https://docs.ansible.com/projects/ansible/8/network/user_guide/platform_routeros.html
fetched_at: 2026-07-28T01:01:11+00:00
---
# RouterOS Platform Options

RouterOS is part of the [community.network](https://galaxy.ansible.com/ui/repo/published/community/network) collection and only supports CLI connections and direct API access.
This page offers details on how to use `ansible.netcommon.network_cli` on RouterOS in Ansible.
Further information can be found in [the community.routeros collection’s SSH guide](../../collections/community/routeros/docsite/ssh-guide.md#ansible-collections-community-routeros-docsite-ssh-guide).

Information on how to use the RouterOS API can be found in [the community.routeros collection’s API guide](../../collections/community/routeros/docsite/api-guide.md#ansible-collections-community-routeros-docsite-api-guide).

- [Connections available](platform_routeros.md#connections-available)
- [Using CLI in Ansible](platform_routeros.md#using-cli-in-ansible)

  - [Example CLI `group_vars/routeros.yml`](platform_routeros.md#example-cli-group-vars-routeros-yml)
  - [Example CLI task](platform_routeros.md#example-cli-task)

## [Connections available](platform_routeros.md#id2)

|  | CLI |
| --- | --- |
| Protocol | SSH |
| Credentials | uses SSH keys / SSH-agent if present  accepts `-u myuser -k` if using password |
| Indirect Access | by a bastion (jump host) |
| Connection Settings | `ansible_connection: ansible.network.network_cli` |
| Enable Mode   (Privilege Escalation) | not supported by RouterOS |
| Returned Data Format | `stdout[0].` |

The RouterOS SSH modules do not support `ansible_connection: local`. You must use `ansible_connection: ansible.netcommon.network_cli`.

The RouterOS API modules require `ansible_connection: local`. See the [the community.routeros collection’s API guide](../../collections/community/routeros/docsite/api-guide.md#ansible-collections-community-routeros-docsite-api-guide) for more information.

## [Using CLI in Ansible](platform_routeros.md#id3)

### [Example CLI `group_vars/routeros.yml`](platform_routeros.md#id4)

```yaml
ansible_connection: ansible.netcommon.network_cli
ansible_network_os: community.network.routeros
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
- If you are getting timeout errors you may want to add `+cet1024w` suffix to your username which will disable console colors, enable “dumb” mode, tell RouterOS not to try detecting terminal capabilities and set terminal width to 1024 columns. See article [Console login process](https://wiki.mikrotik.com/wiki/Manual:Console_login_process) in MikroTik wiki for more information.
- More notes can be found in the [the community.routeros collection’s SSH guide](../../collections/community/routeros/docsite/ssh-guide.md#ansible-collections-community-routeros-docsite-ssh-guide).

### [Example CLI task](platform_routeros.md#id5)

```yaml
- name: Display resource statistics (routeros)
  community.network.routeros_command:
    commands: /system resource print
  register: routeros_resources
  when: ansible_network_os == 'community.network.routeros'
```

> **Warning:**
>
> Never store passwords in plain text. We recommend using SSH keys to authenticate SSH connections. Ansible supports ssh-agent to manage your SSH keys. If you must use passwords to authenticate SSH connections, we recommend encrypting them with [Ansible Vault](../../vault_guide/vault_using_encrypted_content.md#playbooks-vault).

> **See also:**
>
> [Setting timeout options](../getting_started/network_connection_options.md#timeout-options)
