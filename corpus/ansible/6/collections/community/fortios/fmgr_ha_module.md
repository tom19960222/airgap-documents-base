---
collection: ansible
version: "6"
title: "community.fortios.fmgr_ha module – Manages the High-Availability State of FortiManager Clusters and Nodes."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/fortios/fmgr_ha_module.html
fetched_at: 2026-07-27T17:07:44+00:00
---
# community.fortios.fmgr_ha module – Manages the High-Availability State of FortiManager Clusters and Nodes.

> **Note:**
>
> This module is part of the [community.fortios collection](https://galaxy.ansible.com/community/fortios) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.fortios`.
>
> To use it in a playbook, specify: `community.fortios.fmgr_ha`.

- [Synopsis](fmgr_ha_module.md#synopsis)
- [Parameters](fmgr_ha_module.md#parameters)
- [Notes](fmgr_ha_module.md#notes)
- [Examples](fmgr_ha_module.md#examples)
- [Return Values](fmgr_ha_module.md#return-values)

## [Synopsis](fmgr_ha_module.md#id1)

- Change HA state or settings of FortiManager nodes (Standalone/Master/Slave).

## [Parameters](fmgr_ha_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **fmgr_ha_cluster_id**  string | Sets the ID number of the HA cluster. Defaults to 1.  Default: `1` |
| **fmgr_ha_cluster_pw**  string | Sets the password for the HA cluster. Only required once. System remembers between HA mode switches. |
| **fmgr_ha_file_quota**  string | Sets the File quota in MB (2048-20480).  Default: `4096` |
| **fmgr_ha_hb_interval**  string | Sets the heartbeat interval (1-255).  Default: `5` |
| **fmgr_ha_hb_threshold**  string | Sets heartbeat lost threshold (1-255).  Default: `3` |
| **fmgr_ha_mode**  string | Sets the role of the FortiManager host for HA.  Choices:   - `"standalone"` - `"master"` - `"slave"` |
| **fmgr_ha_peer_ipv4**  string | Sets the IPv4 address of a HA peer. |
| **fmgr_ha_peer_ipv6**  string | Sets the IPv6 address of a HA peer. |
| **fmgr_ha_peer_sn**  string | Sets the HA Peer Serial Number. |
| **fmgr_ha_peer_status**  string | Sets the peer status to enable or disable.  Choices:   - `"enable"` - `"disable"` |

## [Notes](fmgr_ha_module.md#id3)

> **Note:**
>
> - Full Documentation at <https://ftnt-ansible-docs.readthedocs.io/en/latest/>.

## [Examples](fmgr_ha_module.md#id4)

```yaml+jinja
- name: SET FORTIMANAGER HA NODE TO MASTER
  community.fortios.fmgr_ha:
    fmgr_ha_mode: "master"
    fmgr_ha_cluster_pw: "fortinet"
    fmgr_ha_cluster_id: "1"

- name: SET FORTIMANAGER HA NODE TO SLAVE
  community.fortios.fmgr_ha:
    fmgr_ha_mode: "slave"
    fmgr_ha_cluster_pw: "fortinet"
    fmgr_ha_cluster_id: "1"

- name: SET FORTIMANAGER HA NODE TO STANDALONE
  community.fortios.fmgr_ha:
    fmgr_ha_mode: "standalone"

- name: ADD FORTIMANAGER HA PEER
  community.fortios.fmgr_ha:
    fmgr_ha_peer_ipv4: "192.168.1.254"
    fmgr_ha_peer_sn: "FMG-VM1234567890"
    fmgr_ha_peer_status: "enable"

- name: CREATE CLUSTER ON MASTER
  community.fortios.fmgr_ha:
    fmgr_ha_mode: "master"
    fmgr_ha_cluster_pw: "fortinet"
    fmgr_ha_cluster_id: "1"
    fmgr_ha_hb_threshold: "10"
    fmgr_ha_hb_interval: "15"
    fmgr_ha_file_quota: "2048"
```

## [Return Values](fmgr_ha_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  Returned: always |

### Authors

- Luke Weighall (@lweighall)
- Andrew Welsh (@Ghilli3)
- Jim Huber (@p4r4n0y1ng)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.fortios)
