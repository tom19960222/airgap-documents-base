---
collection: ansible
version: "6"
title: "community.network.pn_connection_stats_settings module – CLI command to modify connection-stats-settings"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/pn_connection_stats_settings_module.html
fetched_at: 2026-07-27T17:19:17+00:00
---
# community.network.pn_connection_stats_settings module – CLI command to modify connection-stats-settings

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
> To use it in a playbook, specify: `community.network.pn_connection_stats_settings`.

- [Synopsis](pn_connection_stats_settings_module.md#synopsis)
- [Parameters](pn_connection_stats_settings_module.md#parameters)
- [Examples](pn_connection_stats_settings_module.md#examples)
- [Return Values](pn_connection_stats_settings_module.md#return-values)

## [Synopsis](pn_connection_stats_settings_module.md#id1)

- This module can be used to modify the settings for collecting statistical data about connections.

## [Parameters](pn_connection_stats_settings_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_client_server_stats_log_disk_space**  string | disk-space allocated for statistics (including rotated log files). |
| **pn_client_server_stats_log_enable**  boolean | Enable or disable statistics.  Choices:   - `false` - `true` |
| **pn_client_server_stats_log_interval**  string | interval to collect statistics. |
| **pn_client_server_stats_max_memory**  string | maximum memory for client server statistics. |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_connection_backup_enable**  boolean | Enable backup for connection statistics collection.  Choices:   - `false` - `true` |
| **pn_connection_backup_interval**  string | backup interval for connection statistics collection. |
| **pn_connection_max_memory**  string | maximum memory allowed for connection statistics. |
| **pn_connection_stats_log_disk_space**  string | disk-space allocated for statistics (including rotated log files). |
| **pn_connection_stats_log_enable**  boolean | enable or disable statistics.  Choices:   - `false` - `true` |
| **pn_connection_stats_log_interval**  string | interval to collect statistics. |
| **pn_connection_stats_max_memory**  string | maximum memory allowed for connection statistics. |
| **pn_enable**  boolean | Enable or disable collecting connections statistics.  Choices:   - `false` - `true` |
| **pn_fabric_connection_backup_enable**  boolean | enable backup for fabric connection statistics collection.  Choices:   - `false` - `true` |
| **pn_fabric_connection_backup_interval**  string | backup interval for fabric connection statistics collection. |
| **pn_fabric_connection_max_memory**  string | maximum memory allowed for fabric connection statistics. |
| **pn_service_stat_max_memory**  string | maximum memory allowed for service statistics. |
| **state**  string / required | State the action to perform. Use `update` to modify the connection-stats-settings.  Choices:   - `"update"` |

## [Examples](pn_connection_stats_settings_module.md#id3)

```yaml+jinja
- name: "Modify connection stats settings"
  community.network.pn_connection_stats_settings:
    pn_cliswitch: "sw01"
    state: "update"
    pn_enable: False
    pn_fabric_connection_max_memory: "1000"

- name: "Modify connection stats settings"
  community.network.pn_connection_stats_settings:
    pn_cliswitch: "sw01"
    state: "update"
    pn_enable: True
```

## [Return Values](pn_connection_stats_settings_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  Returned: always |
| **command**  string | the CLI command run on the target node.  Returned: always |
| **stderr**  list / elements=string | set of error responses from the connection-stats-settings command.  Returned: on error |
| **stdout**  list / elements=string | set of responses from the connection-stats-settings command.  Returned: always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
