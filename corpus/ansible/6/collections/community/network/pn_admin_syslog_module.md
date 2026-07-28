---
collection: ansible
version: "6"
title: "community.network.pn_admin_syslog module – CLI command to create/modify/delete admin-syslog"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/pn_admin_syslog_module.html
fetched_at: 2026-07-27T17:19:16+00:00
---
# community.network.pn_admin_syslog module – CLI command to create/modify/delete admin-syslog

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.pn_admin_syslog`.

- [Synopsis](pn_admin_syslog_module.md#synopsis)
- [Parameters](pn_admin_syslog_module.md#parameters)
- [Examples](pn_admin_syslog_module.md#examples)
- [Return Values](pn_admin_syslog_module.md#return-values)

## [Synopsis](pn_admin_syslog_module.md#id1)

- This module can be used to create the scope and other parameters of syslog event collection.
- This module can be used to modify parameters of syslog event collection.
- This module can be used to delete the scope and other parameters of syslog event collection.

## [Parameters](pn_admin_syslog_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_host**  string | Hostname to log system events. |
| **pn_message_format**  string | message-format for log events - structured or legacy.  Choices:   - `"structured"` - `"legacy"` |
| **pn_name**  string | name of the system log. |
| **pn_port**  string | Host port. |
| **pn_scope**  string | Scope of the system log.  Choices:   - `"local"` - `"fabric"` |
| **pn_transport**  string | Transport for log events - tcp/tls or udp.  Choices:   - `"tcp-tls"` - `"udp"` ← (default) |
| **state**  string / required | State the action to perform. Use `present` to create admin-syslog and `absent` to delete admin-syslog `update` to modify the admin-syslog.  Choices:   - `"present"` - `"absent"` - `"update"` |

## [Examples](pn_admin_syslog_module.md#id3)

```yaml+jinja
- name: Admin-syslog functionality
  community.network.pn_admin_syslog:
    pn_cliswitch: "sw01"
    state: "absent"
    pn_name: "foo"
    pn_scope: "local"

- name: Admin-syslog functionality
  community.network.pn_admin_syslog:
    pn_cliswitch: "sw01"
    state: "present"
    pn_name: "foo"
    pn_scope: "local"
    pn_host: "166.68.224.46"
    pn_message_format: "structured"

- name: Admin-syslog functionality
  community.network.pn_admin_syslog:
    pn_cliswitch: "sw01"
    state: "update"
    pn_name: "foo"
    pn_host: "166.68.224.10"
```

## [Return Values](pn_admin_syslog_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  Returned: always |
| **command**  string | the CLI command run on the target node.  Returned: always |
| **stderr**  list / elements=string | set of error responses from the admin-syslog command.  Returned: on error |
| **stdout**  list / elements=string | set of responses from the admin-syslog command.  Returned: always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
