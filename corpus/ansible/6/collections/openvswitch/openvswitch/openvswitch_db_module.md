---
collection: ansible
version: "6"
title: "openvswitch.openvswitch.openvswitch_db module – Configure open vswitch database."
source_url: https://docs.ansible.com/projects/ansible/6/collections/openvswitch/openvswitch/openvswitch_db_module.html
fetched_at: 2026-07-28T00:17:19+00:00
---
# openvswitch.openvswitch.openvswitch_db module – Configure open vswitch database.

> **Note:**
>
> This module is part of the [openvswitch.openvswitch collection](https://galaxy.ansible.com/openvswitch/openvswitch) (version 2.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install openvswitch.openvswitch`.
> You need further requirements to be able to use this module,
> see [Requirements](openvswitch_db_module.md#ansible-collections-openvswitch-openvswitch-openvswitch-db-module-requirements) for details.
>
> To use it in a playbook, specify: `openvswitch.openvswitch.openvswitch_db`.

New in openvswitch.openvswitch 1.0.0

- [Synopsis](openvswitch_db_module.md#synopsis)
- [Requirements](openvswitch_db_module.md#requirements)
- [Parameters](openvswitch_db_module.md#parameters)
- [Examples](openvswitch_db_module.md#examples)
- [Return Values](openvswitch_db_module.md#return-values)

## [Synopsis](openvswitch_db_module.md#id1)

- Set column values in record in database table.

## [Requirements](openvswitch_db_module.md#id2)

The below requirements are needed on the host that executes this module.

- ovs-vsctl >= 2.3.3

## [Parameters](openvswitch_db_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **col**  string / required | Identifies the column in the record. |
| **database_socket**  string | Path/ip to datbase socket to use  Default path is used if not specified  Path should start with ‘unix:’ prefix |
| **key**  string | Identifies the key in the record column, when the column is a map type. |
| **record**  string / required | Identifies the record in the table. |
| **state**  string | Configures the state of the key. When set to *present*, the *key* and *value* pair will be set on the *record* and when set to *absent* the *key* will not be set.  Choices:   - `"present"` ← (default) - `"absent"` - `"read"` |
| **table**  string / required | Identifies the table in the database. |
| **timeout**  integer | How long to wait for ovs-vswitchd to respond  Default: `5` |
| **value**  string | Expected value for the table, record, column and key. |

## [Examples](openvswitch_db_module.md#id4)

```yaml+jinja
# Increase the maximum idle time to 50 seconds before pruning unused kernel
# rules.
- openvswitch.openvswitch.openvswitch_db:
    table: open_vswitch
    record: .
    col: other_config
    key: max-idle
    value: 50000

# Disable in band copy
- openvswitch.openvswitch.openvswitch_db:
    table: Bridge
    record: br-int
    col: other_config
    key: disable-in-band
    value: true

# Remove in band key
- openvswitch.openvswitch.openvswitch_db:
    state: present
    table: Bridge
    record: br-int
    col: other_config
    key: disable-in-band

# Mark port with tag 10
- openvswitch.openvswitch.openvswitch_db:
    table: Port
    record: port0
    col: tag
    value: 10

# Mark port with tag 10 for OVSDB with socket in /opt/second.sock
- openvswitch.openvswitch.openvswitch_db:
    table: Port
    record: port0
    col: tag
    value: 10
    database_socket: unix:/opt/second.sock

# Get interface statistics
- openvswitch.openvswitch.openvswitch_db:
    state: read
    table: interface
    record: ifname
    col: statistics

# Get tx_packets value
- openvswitch.openvswitch.openvswitch_db:
    state: read
    table: interface
    record: ifname
    col: statistics
    key: tx_packets

# Get mtu value
- openvswitch.openvswitch.openvswitch_db:
    state: read
    table: interface
    record: ifname
    col: mtu
```

## [Return Values](openvswitch_db_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | List of commands sent  Returned: when state is read  Sample: `["/usr/local/bin/ovs-vsctl -t 5 get interface vhuclient1 statistics:tx_packets"]` |
| **output**  dictionary | Output of the commands  Returned: when state is read  Sample: `{"tx_packets": "0"}` |

### Authors

- Mark Hamilton (@markleehamilton)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/openvswitch.openvswitch/issues)
[Repository (Sources)](https://github.com/ansible-collections/openvswitch.openvswitch)
