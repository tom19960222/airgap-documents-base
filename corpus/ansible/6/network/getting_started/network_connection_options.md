---
collection: ansible
version: "6"
title: "Working with network connection options"
source_url: https://docs.ansible.com/projects/ansible/6/network/getting_started/network_connection_options.html
fetched_at: 2026-07-27T16:40:04+00:00
---
# Working with network connection options

Network modules can support multiple connection protocols, such as `ansible.netcommon.network_cli`, `ansible.netcommon.netconf`, and `ansible.netcommon.httpapi`. These connections include some common options you can set to control how the connection to your network device behaves.

Common options are:

- `become` and `become_method` as described in [Privilege Escalation: enable mode, become, and authorize](network_differences.md#privilege-escalation).
- `network_os` - set to match your network platform you are communicating with. See the [platform-specific](../user_guide/platform_index.md#platform-options) pages.
- `remote_user` as described in [Setting a remote user](../../user_guide/connection_details.md#connection-set-user).
- Timeout options - `persistent_command_timeout`, `persistent_connect_timeout`, and `timeout`.

## Setting timeout options

When communicating with a remote device, you have control over how long Ansible maintains the connection to that device, as well as how long Ansible waits for a command to complete on that device. Each of these options can be set as variables in your playbook files, environment variables, or settings in your [ansible.cfg file](../../reference_appendices/config.md#ansible-configuration-settings).

For example, the three options for controlling the connection timeout are as follows.

Using vars (per task):

```yaml
- name: save running-config
  cisco.ios.ios_command:
    commands: copy running-config startup-config
    vars:
      ansible_command_timeout: 30
```

Using the environment variable:

```bash
$export ANSIBLE_PERSISTENT_COMMAND_TIMEOUT=30
```

Using the global configuration (in `ansible.cfg`)

```ini
[persistent_connection ]
command_timeout = 30
```

See [Variable precedence: Where should I put a variable?](../../user_guide/playbooks_variables.md#ansible-variable-precedence) for details on the relative precedence of each of these variables. See the individual connection type to understand each option.
