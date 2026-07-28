---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_system_standalone_cluster module – Configure FortiGate Session Life Support Protocol (FGSP) cluster attributes in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_system_standalone_cluster_module.html
fetched_at: 2026-07-28T02:29:33+00:00
---
# fortinet.fortios.fortios_system_standalone_cluster module – Configure FortiGate Session Life Support Protocol (FGSP) cluster attributes in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortios/) (version 2.3.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_system_standalone_cluster_module.md#ansible-collections-fortinet-fortios-fortios-system-standalone-cluster-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_standalone_cluster`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_standalone_cluster_module.md#synopsis)
- [Requirements](fortios_system_standalone_cluster_module.md#requirements)
- [Parameters](fortios_system_standalone_cluster_module.md#parameters)
- [Notes](fortios_system_standalone_cluster_module.md#notes)
- [Examples](fortios_system_standalone_cluster_module.md#examples)
- [Return Values](fortios_system_standalone_cluster_module.md#return-values)

## [Synopsis](fortios_system_standalone_cluster_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and standalone_cluster category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_standalone_cluster_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_system_standalone_cluster_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **system_standalone_cluster**  dictionary | Configure FortiGate Session Life Support Protocol (FGSP) cluster attributes. |
| **cluster_peer**  list / elements=dictionary | Configure FortiGate Session Life Support Protocol (FGSP) session synchronization. |
| **down_intfs_before_sess_sync**  list / elements=dictionary | List of interfaces to be turned down before session synchronization is complete. |
| **name**  string / required | Interface name. Source system.interface.name. |
| **hb_interval**  integer | Heartbeat interval (1 - 20 (100\*ms). Increase to reduce false positives. |
| **hb_lost_threshold**  integer | Lost heartbeat threshold (1 - 60). Increase to reduce false positives. |
| **ipsec_tunnel_sync**  string | Enable/disable IPsec tunnel synchronization.  **Choices:**   - `"enable"` - `"disable"` |
| **peerip**  string | IP address of the interface on the peer unit that is used for the session synchronization link. |
| **peervd**  string | VDOM that contains the session synchronization link interface on the peer unit. Usually both peers would have the same peervd. Source system.vdom.name. |
| **secondary_add_ipsec_routes**  string | Enable/disable IKE route announcement on the backup unit.  **Choices:**   - `"enable"` - `"disable"` |
| **session_sync_filter**  dictionary | Add one or more filters if you only want to synchronize some sessions. Use the filter to configure the types of sessions to synchronize. |
| **custom_service**  list / elements=dictionary | Only sessions using these custom services are synchronized. Use source and destination port ranges to define these custom services. |
| **dst_port_range**  string | Custom service destination port range. |
| **id**  integer / required | Custom service ID. see <a href=’#notes’>Notes</a>. |
| **src_port_range**  string | Custom service source port range. |
| **dstaddr**  string | Only sessions to this IPv4 address are synchronized. |
| **dstaddr6**  string | Only sessions to this IPv6 address are synchronized. |
| **dstintf**  string | Only sessions to this interface are synchronized. Source system.interface.name. |
| **srcaddr**  string | Only sessions from this IPv4 address are synchronized. |
| **srcaddr6**  string | Only sessions from this IPv6 address are synchronized. |
| **srcintf**  string | Only sessions from this interface are synchronized. Source system.interface.name. |
| **sync_id**  integer / required | Sync ID. see <a href=’#notes’>Notes</a>. |
| **syncvd**  list / elements=dictionary | Sessions from these VDOMs are synchronized using this session synchronization configuration. |
| **name**  string / required | VDOM name. Source system.vdom.name. |
| **encryption**  string | Enable/disable encryption when synchronizing sessions.  **Choices:**   - `"enable"` - `"disable"` |
| **group_member_id**  integer | Cluster member ID (0 - 15). |
| **layer2_connection**  string | Indicate whether layer 2 connections are present among FGSP members.  **Choices:**   - `"available"` - `"unavailable"` |
| **psksecret**  string | Pre-shared secret for session synchronization (ASCII string or hexadecimal encoded with a leading 0x). |
| **session_sync_dev**  list / elements=string | Offload session-sync process to kernel and sync sessions using connected interface(s) directly. Source system.interface.name. |
| **standalone_group_id**  integer | Cluster group ID (0 - 255). Must be the same for all members. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_system_standalone_cluster_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_standalone_cluster_module.md#id5)

```yaml+jinja
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Configure FortiGate Session Life Support Protocol (FGSP) cluster attributes.
    fortios_system_standalone_cluster:
      vdom:  "{{ vdom }}"
      system_standalone_cluster:
        cluster_peer:
         -
            down_intfs_before_sess_sync:
             -
                name: "default_name_5 (source system.interface.name)"
            hb_interval: "2"
            hb_lost_threshold: "10"
            ipsec_tunnel_sync: "enable"
            peerip: "<your_own_value>"
            peervd: "<your_own_value> (source system.vdom.name)"
            secondary_add_ipsec_routes: "enable"
            session_sync_filter:
                custom_service:
                 -
                    dst_port_range: "<your_own_value>"
                    id:  "15"
                    src_port_range: "<your_own_value>"
                dstaddr: "<your_own_value>"
                dstaddr6: "<your_own_value>"
                dstintf: "<your_own_value> (source system.interface.name)"
                srcaddr: "<your_own_value>"
                srcaddr6: "<your_own_value>"
                srcintf: "<your_own_value> (source system.interface.name)"
            sync_id: "<you_own_value>"
            syncvd:
             -
                name: "default_name_25 (source system.vdom.name)"
        encryption: "enable"
        group_member_id: "0"
        layer2_connection: "available"
        psksecret: "<your_own_value>"
        session_sync_dev: "<your_own_value> (source system.interface.name)"
        standalone_group_id: "0"
```

## [Return Values](fortios_system_standalone_cluster_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  **Returned:** always  **Sample:** `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  **Returned:** always  **Sample:** `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  **Returned:** always  **Sample:** `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  **Returned:** success  **Sample:** `"id"` |
| **name**  string | Name of the table used to fulfill the request  **Returned:** always  **Sample:** `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  **Returned:** always  **Sample:** `"webfilter"` |
| **revision**  string | Internal revision number  **Returned:** always  **Sample:** `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  **Returned:** always  **Sample:** `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  **Returned:** always  **Sample:** `"success"` |
| **vdom**  string | Virtual domain used  **Returned:** always  **Sample:** `"root"` |
| **version**  string | Version of the FortiGate  **Returned:** always  **Sample:** `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
- [Homepage](https://www.fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
