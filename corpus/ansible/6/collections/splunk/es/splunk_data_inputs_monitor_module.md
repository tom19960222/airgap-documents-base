---
collection: ansible
version: "6"
title: "splunk.es.splunk_data_inputs_monitor module – Splunk Data Inputs of type Monitor resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/splunk/es/splunk_data_inputs_monitor_module.html
fetched_at: 2026-07-28T00:20:00+00:00
---
# splunk.es.splunk_data_inputs_monitor module – Splunk Data Inputs of type Monitor resource module

> **Note:**
>
> This module is part of the [splunk.es collection](https://galaxy.ansible.com/splunk/es) (version 2.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install splunk.es`.
>
> To use it in a playbook, specify: `splunk.es.splunk_data_inputs_monitor`.

New in splunk.es 2.1.0

- [Synopsis](splunk_data_inputs_monitor_module.md#synopsis)
- [Parameters](splunk_data_inputs_monitor_module.md#parameters)
- [Examples](splunk_data_inputs_monitor_module.md#examples)
- [Return Values](splunk_data_inputs_monitor_module.md#return-values)

## [Synopsis](splunk_data_inputs_monitor_module.md#id1)

- Module to add/modify or delete, File and Directory Monitor Data Inputs in Splunk.
- Tested against Splunk Enterprise Server 8.2.3

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](splunk_data_inputs_monitor_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | Configure file and directory monitoring on the system |
| **blacklist**  string | Specify a regular expression for a file path. The file path that matches this regular expression is not indexed. |
| **check_index**  boolean | If set to `True`, the index value is checked to ensure that it is the name of a valid index.  This parameter is not returned back by Splunk while obtaining object information. It is therefore left out while performing idempotency checks  Choices:   - `false` - `true` |
| **check_path**  boolean | If set to `True`, the name value is checked to ensure that it exists.  This parameter is not returned back by Splunk while obtaining object information. It is therefore left out while performing idempotency checks  Choices:   - `false` - `true` |
| **crc_salt**  string | A string that modifies the file tracking identity for files in this input. The magic value <SOURCE> invokes special behavior (see admin documentation). |
| **disabled**  boolean | Indicates if input monitoring is disabled.  Choices:   - `false` ← (default) - `true` |
| **follow_tail**  boolean | If set to `True`, files that are seen for the first time is read from the end.  Choices:   - `false` - `true` |
| **host**  string | The value to populate in the host field for events from this data input.  Default: `"$decideOnStartup"` |
| **host_regex**  string | Specify a regular expression for a file path. If the path for a file matches this regular expression, the captured value is used to populate the host field for events from this data input. The regular expression must have one capture group. |
| **host_segment**  integer | Use the specified slash-separate segment of the filepath as the host field value. |
| **ignore_older_than**  string | Specify a time value. If the modification time of a file being monitored falls outside of this rolling time window, the file is no longer being monitored.  This parameter is not returned back by Splunk while obtaining object information. It is therefore left out while performing idempotency checks |
| **index**  string | Which index events from this input should be stored in. Defaults to default.  Default: `"default"` |
| **name**  string / required | The file or directory path to monitor on the system. |
| **recursive**  boolean | Setting this to False prevents monitoring of any subdirectories encountered within this data input.  Choices:   - `false` - `true` |
| **rename_source**  string | The value to populate in the source field for events from this data input. The same source should not be used for multiple data inputs.  This parameter is not returned back by Splunk while obtaining object information. It is therefore left out while performing idempotency checks |
| **sourcetype**  string | The value to populate in the sourcetype field for incoming events. |
| **time_before_close**  integer | When Splunk software reaches the end of a file that is being read, the file is kept open for a minimum of the number of seconds specified in this value. After this period has elapsed, the file is checked again for more data.  This parameter is not returned back by Splunk while obtaining object information. It is therefore left out while performing idempotency checks |
| **whitelist**  string | Specify a regular expression for a file path. Only file paths that match this regular expression are indexed. |
| **running_config**  string | The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-config for every task in a playbook. The *running_config* argument allows the implementer to pass in the configuration to use as the base config for comparison. This value of this option should be the output received from device by executing command. |
| **state**  string | The state the configuration should be left in  Choices:   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"gathered"` |

## [Examples](splunk_data_inputs_monitor_module.md#id3)

```yaml+jinja
# Using gathered
# --------------

- name: Gather config for specified Data inputs monitors
  splunk.es.splunk_data_inputs_monitor:
    config:
      - name: "/var/log"
      - name: "/var"
    state: gathered

# RUN output:
# -----------

# "gathered": [
#     {
#         "blacklist": "//var/log/[a-z0-9]/gm",
#         "crc_salt": "<SOURCE>",
#         "disabled": false,
#         "host": "$decideOnStartup",
#         "host_regex": "/(test_host)/gm",
#         "host_segment": 3,
#         "index": "default",
#         "name": "/var/log",
#         "recursive": true,
#         "sourcetype": "test_source",
#         "whitelist": "//var/log/[0-9]/gm"
#     }
# ]
#

# Using merged
# ------------

- name: Update Data inputs monitors config
  splunk.es.splunk_data_inputs_monitor:
    config:
      - name: "/var/log"
        blacklist: "//var/log/[a-z]/gm"
        check_index: True
        check_path: True
        crc_salt: <SOURCE>
        rename_source: "test"
        whitelist: "//var/log/[0-9]/gm"
    state: merged

# RUN output:
# -----------

# "after": [
#     {
#         "blacklist": "//var/log/[a-z]/gm",
#         "crc_salt": "<SOURCE>",
#         "disabled": false,
#         "host": "$decideOnStartup",
#         "host_regex": "/(test_host)/gm",
#         "host_segment": 3,
#         "index": "default",
#         "name": "/var/log",
#         "recursive": true,
#         "sourcetype": "test_source",
#         "whitelist": "//var/log/[0-9]/gm"
#     }
# ],
# "before": [
#     {
#         "blacklist": "//var/log/[a-z0-9]/gm",
#         "crc_salt": "<SOURCE>",
#         "disabled": false,
#         "host": "$decideOnStartup",
#         "host_regex": "/(test_host)/gm",
#         "host_segment": 3,
#         "index": "default",
#         "name": "/var/log",
#         "recursive": true,
#         "sourcetype": "test_source",
#         "whitelist": "//var/log/[0-9]/gm"
#     }
# ],

# Using replaced
# --------------

- name: To Replace Data inputs monitors config
  splunk.es.splunk_data_inputs_monitor:
    config:
      - name: "/var/log"
        blacklist: "//var/log/[a-z0-9]/gm"
        crc_salt: <SOURCE>
        index: default
    state: replaced

# RUN output:
# -----------

# "after": [
#     {
#         "blacklist": "//var/log/[a-z0-9]/gm",
#         "crc_salt": "<SOURCE>",
#         "disabled": false,
#         "host": "$decideOnStartup",
#         "index": "default",
#         "name": "/var/log"
#     }
# ],
# "before": [
#     {
#         "blacklist": "//var/log/[a-z0-9]/gm",
#         "crc_salt": "<SOURCE>",
#         "disabled": false,
#         "host": "$decideOnStartup",
#         "host_regex": "/(test_host)/gm",
#         "host_segment": 3,
#         "index": "default",
#         "name": "/var/log",
#         "recursive": true,
#         "sourcetype": "test_source",
#         "whitelist": "//var/log/[0-9]/gm"
#     }
# ],

# Using deleted
# -----------
- name: To Delete Data inpur monitor config
  splunk.es.splunk_data_inputs_monitor:
    config:
      - name: "/var/log"
    state: deleted

# RUN output:
# -----------
#
# "after": [],
# "before": [
#     {
#         "blacklist": "//var/log/[a-z0-9]/gm",
#         "crc_salt": "<SOURCE>",
#         "disabled": false,
#         "host": "$decideOnStartup",
#         "index": "default",
#         "name": "/var/log"
#     }
# ],
```

## [Return Values](splunk_data_inputs_monitor_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  Returned: when changed  Sample: `["The configuration returned will always be in the same format of the parameters above."]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format of the parameters above."]` |

### Authors

- Ansible Security Automation Team (@pranav-bhatt) <<https://github.com/ansible-security>>

### Collection links

[Issue Tracker](https://github.com/ansible-collections/splunk.es/issues)
[Repository (Sources)](https://github.com/ansible-collections/splunk.es)
