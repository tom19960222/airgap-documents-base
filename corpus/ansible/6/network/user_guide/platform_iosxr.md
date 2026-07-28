---
collection: ansible
version: "6"
title: "IOS-XR Platform Options"
source_url: https://docs.ansible.com/projects/ansible/6/network/user_guide/platform_iosxr.html
fetched_at: 2026-07-27T16:41:11+00:00
---
# IOS-XR Platform Options

The [Cisco IOS-XR collection](https://galaxy.ansible.com/cisco/iosxr) supports multiple connections. This page offers details on how each connection works in Ansible and how to use it.

- [Connections available](platform_iosxr.md#connections-available)
- [Using CLI in Ansible](platform_iosxr.md#using-cli-in-ansible)

  - [Example CLI inventory `[iosxr:vars]`](platform_iosxr.md#example-cli-inventory-iosxr-vars)
  - [Example CLI task](platform_iosxr.md#example-cli-task)
- [Using NETCONF in Ansible](platform_iosxr.md#using-netconf-in-ansible)

  - [Enabling NETCONF](platform_iosxr.md#enabling-netconf)
  - [Example NETCONF inventory `[iosxr:vars]`](platform_iosxr.md#example-netconf-inventory-iosxr-vars)
  - [Example NETCONF task](platform_iosxr.md#example-netconf-task)

## [Connections available](platform_iosxr.md#id1)

|  | CLI | NETCONF  only for modules `iosxr_banner`, `iosxr_interface`, `iosxr_logging`, `iosxr_system`, `iosxr_user` |
| --- | --- | --- |
| Protocol | SSH | XML over SSH |
| Credentials | uses SSH keys / SSH-agent if present  accepts `-u myuser -k` if using password | uses SSH keys / SSH-agent if present  accepts `-u myuser -k` if using password |
| Indirect Access | via a bastion (jump host) | via a bastion (jump host) |
| Connection Settings | `ansible_connection:`  `ansible.netcommon.network_cli` | `ansible_connection:`  `ansible.netcommon.netconf` |
| Enable Mode   (Privilege Escalation) | not supported | not supported |
| Returned Data Format | Refer to individual module documentation | Refer to individual module documentation |

The `ansible_connection: local` has been deprecated. Please use `ansible_connection: ansible.netcommon.network_cli` or `ansible_connection: ansible.netcommon.netconf` instead.

## [Using CLI in Ansible](platform_iosxr.md#id2)

### [Example CLI inventory `[iosxr:vars]`](platform_iosxr.md#id3)

```yaml
[iosxr:vars]
ansible_connection=ansible.netcommon.network_cli
ansible_network_os=cisco.iosxr.iosxr
ansible_user=myuser
ansible_password=!vault...
ansible_ssh_common_args='-o ProxyCommand="ssh -W %h:%p -q bastion01"'
```

- If you are using SSH keys (including an ssh-agent) you can remove the `ansible_password` configuration.
- If you are accessing your host directly (not through a bastion/jump host) you can remove the `ansible_ssh_common_args` configuration.
- If you are accessing your host through a bastion/jump host, you cannot include your SSH password in the `ProxyCommand` directive. To prevent secrets from leaking out (for example in `ps` output), SSH does not support providing passwords via environment variables.

### [Example CLI task](platform_iosxr.md#id4)

```yaml
- name: Retrieve IOS-XR version
  cisco.iosxr.iosxr_command:
    commands: show version
  when: ansible_network_os == 'cisco.iosxr.iosxr'
```

## [Using NETCONF in Ansible](platform_iosxr.md#id5)

### [Enabling NETCONF](platform_iosxr.md#id6)

Before you can use NETCONF to connect to a switch, you must:

- install the `ncclient` python package on your control node(s) with `pip install ncclient`
- enable NETCONF on the Cisco IOS-XR device(s)

To enable NETCONF on a new switch via Ansible, use the `cisco.iosxr.iosxr_netconf` module through the CLI connection. Set up your platform-level variables just like in the CLI example above, then run a playbook task like this:

```yaml
- name: Enable NETCONF
  connection: ansible.netcommon.network_cli
  cisco.iosxr.iosxr_netconf:
  when: ansible_network_os == 'cisco.iosxr.iosxr'
```

Once NETCONF is enabled, change your variables to use the NETCONF connection.

### [Example NETCONF inventory `[iosxr:vars]`](platform_iosxr.md#id7)

```yaml
[iosxr:vars]
ansible_connection=ansible.netcommon.netconf
ansible_network_os=cisco.iosxr.iosxr
ansible_user=myuser
ansible_password=!vault |
ansible_ssh_common_args='-o ProxyCommand="ssh -W %h:%p -q bastion01"'
```

### [Example NETCONF task](platform_iosxr.md#id8)

```yaml
- name: Configure hostname and domain-name
  cisco.iosxr.iosxr_system:
    hostname: iosxr01
    domain_name: test.example.com
    domain_search:
      - ansible.com
      - redhat.com
      - cisco.com
```

> **Warning:**
>
> Never store passwords in plain text. We recommend using SSH keys to authenticate SSH connections. Ansible supports ssh-agent to manage your SSH keys. If you must use passwords to authenticate SSH connections, we recommend encrypting them with [Ansible Vault](../../user_guide/vault.md#playbooks-vault).

> **See also:**
>
> [Setting timeout options](../getting_started/network_connection_options.md#timeout-options)
