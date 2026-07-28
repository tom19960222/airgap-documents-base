---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_ntp_servers_peers module – Configures NTP peers and servers parameters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_ntp_servers_peers_module.html
fetched_at: 2026-07-27T17:55:35+00:00
---
# mellanox.onyx.onyx_ntp_servers_peers module – Configures NTP peers and servers parameters

> **Note:**
>
> This module is part of the [mellanox.onyx collection](https://galaxy.ansible.com/mellanox/onyx) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install mellanox.onyx`.
>
> To use it in a playbook, specify: `mellanox.onyx.onyx_ntp_servers_peers`.

New in mellanox.onyx 0.2.0

- [Synopsis](onyx_ntp_servers_peers_module.md#synopsis)
- [Parameters](onyx_ntp_servers_peers_module.md#parameters)
- [Examples](onyx_ntp_servers_peers_module.md#examples)
- [Return Values](onyx_ntp_servers_peers_module.md#return-values)

## [Synopsis](onyx_ntp_servers_peers_module.md#id1)

- This module provides declarative management of NTP peers and servers configuration on Mellanox ONYX network devices.

## [Parameters](onyx_ntp_servers_peers_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **ntpdate**  string | Sets system clock once from a remote server using NTP. |
| **peer**  list / elements=string | List of ntp peers. |
| **enabled**  boolean | Disables/Enables ntp peer state  Choices:   - `false` - `true` |
| **ip_or_name**  string / required | Configures ntp peer name or ip. |
| **key_id**  integer | Used to configure the key-id for the ntp peer |
| **state**  string | Indicates if the ntp peer exists or should be deleted  Choices:   - `"present"` - `"absent"` |
| **version**  integer | version number for the ntp peer  Choices:   - `3` - `4` |
| **server**  list / elements=string | List of ntp servers. |
| **enabled**  boolean | Disables/Enables ntp server  Choices:   - `false` - `true` |
| **ip_or_name**  string / required | Configures ntp server name or ip. |
| **key_id**  integer | Used to configure the key-id for the ntp server |
| **state**  string | Indicates if the ntp peer exists or should be deleted.  Choices:   - `"present"` - `"absent"` |
| **trusted_enable**  boolean | Disables/Enables the trusted state for the ntp server.  Choices:   - `false` - `true` |
| **version**  integer | version number for the ntp server  Choices:   - `3` - `4` |

## [Examples](onyx_ntp_servers_peers_module.md#id3)

```yaml+jinja
- name: Configure NTP peers and servers
  onyx_ntp_peers_servers:
    peer:
       - ip_or_name: 1.1.1.1
         enabled: yes
         version: 4
         key_id: 6
         state: present
    server:
       - ip_or_name: 2.2.2.2
         enabled: true
         version: 3
         key_id: 8
         trusted_enable: no
         state: present
    ntpdate: 192.168.10.10
```

## [Return Values](onyx_ntp_servers_peers_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always.  Sample: `["ntp peer 1.1.1.1 disable no ntp peer 1.1.1.1 disable ntp peer 1.1.1.1 keyId 6 ntp peer 1.1.1.1 version 4 no ntp peer 1.1.1.1 ntp server 2.2.2.2 disable no ntp server 2.2.2.2 disable ntp server 2.2.2.2 keyID 8 ntp server 2.2.2.2 version 3 ntp server 2.2.2.2 trusted-enable no ntp server 2.2.2.2 ntp server 192.168.10.10 ntpdate 192.168.10.10"]` |

### Authors

- Sara-Touqan (@sarato)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
