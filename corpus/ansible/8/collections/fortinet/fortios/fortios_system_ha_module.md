---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_system_ha module – Configure HA in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_system_ha_module.html
fetched_at: 2026-07-28T02:28:30+00:00
---
# fortinet.fortios.fortios_system_ha module – Configure HA in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_ha_module.md#ansible-collections-fortinet-fortios-fortios-system-ha-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_ha`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_ha_module.md#synopsis)
- [Requirements](fortios_system_ha_module.md#requirements)
- [Parameters](fortios_system_ha_module.md#parameters)
- [Notes](fortios_system_ha_module.md#notes)
- [Examples](fortios_system_ha_module.md#examples)
- [Return Values](fortios_system_ha_module.md#return-values)

## [Synopsis](fortios_system_ha_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and ha category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_ha_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_system_ha_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **system_ha**  dictionary | Configure HA. |
| **arps**  integer | Number of gratuitous ARPs (1 - 60). Lower to reduce traffic. Higher to reduce failover time. |
| **arps_interval**  integer | Time between gratuitous ARPs (1 - 20 sec). Lower to reduce failover time. Higher to reduce traffic. |
| **authentication**  string | Enable/disable heartbeat message authentication.  **Choices:**   - `"enable"` - `"disable"` |
| **cpu_threshold**  string | Dynamic weighted load balancing CPU usage weight and high and low thresholds. |
| **encryption**  string | Enable/disable heartbeat message encryption.  **Choices:**   - `"enable"` - `"disable"` |
| **evpn_ttl**  integer | HA EVPN FDB TTL on primary box (5 - 3600 sec). |
| **failover_hold_time**  integer | Time to wait before failover (0 - 300 sec), to avoid flip. |
| **ftp_proxy_threshold**  string | Dynamic weighted load balancing weight and high and low number of FTP proxy sessions. |
| **gratuitous_arps**  string | Enable/disable gratuitous ARPs. Disable if link-failed-signal enabled.  **Choices:**   - `"enable"` - `"disable"` |
| **group_id**  integer | HA group ID (0 - 1023; or 0 - 7 when there are more than 2 vclusters). Must be the same for all members. |
| **group_name**  string | Cluster group name. Must be the same for all members. |
| **ha_direct**  string | Enable/disable using ha-mgmt interface for syslog, remote authentication (RADIUS), FortiAnalyzer, FortiSandbox, sFlow, and Netflow.  **Choices:**   - `"enable"` - `"disable"` |
| **ha_eth_type**  string | HA heartbeat packet Ethertype (4-digit hex). |
| **ha_mgmt_interfaces**  list / elements=dictionary | Reserve interfaces to manage individual cluster units. |
| **dst**  string | Default route destination for reserved HA management interface. |
| **gateway**  string | Default route gateway for reserved HA management interface. |
| **gateway6**  string | Default IPv6 gateway for reserved HA management interface. |
| **id**  integer / required | Table ID. see <a href=’#notes’>Notes</a>. |
| **interface**  string | Interface to reserve for HA management. Source system.interface.name. |
| **ha_mgmt_status**  string | Enable to reserve interfaces to manage individual cluster units.  **Choices:**   - `"enable"` - `"disable"` |
| **ha_uptime_diff_margin**  integer | Normally you would only reduce this value for failover testing. |
| **hb_interval**  integer | Time between sending heartbeat packets (1 - 20). Increase to reduce false positives. |
| **hb_interval_in_milliseconds**  string | Units of heartbeat interval time between sending heartbeat packets. Default is 100ms.  **Choices:**   - `"100ms"` - `"10ms"` |
| **hb_lost_threshold**  integer | Number of lost heartbeats to signal a failure (1 - 60). Increase to reduce false positives. |
| **hbdev**  list / elements=string | Heartbeat interfaces. Must be the same for all members. |
| **hc_eth_type**  string | Transparent mode HA heartbeat packet Ethertype (4-digit hex). |
| **hello_holddown**  integer | Time to wait before changing from hello to work state (5 - 300 sec). |
| **http_proxy_threshold**  string | Dynamic weighted load balancing weight and high and low number of HTTP proxy sessions. |
| **imap_proxy_threshold**  string | Dynamic weighted load balancing weight and high and low number of IMAP proxy sessions. |
| **inter_cluster_session_sync**  string | Enable/disable synchronization of sessions among HA clusters.  **Choices:**   - `"enable"` - `"disable"` |
| **key**  string | Key. |
| **l2ep_eth_type**  string | Telnet session HA heartbeat packet Ethertype (4-digit hex). |
| **link_failed_signal**  string | Enable to shut down all interfaces for 1 sec after a failover. Use if gratuitous ARPs do not update network.  **Choices:**   - `"enable"` - `"disable"` |
| **load_balance_all**  string | Enable to load balance TCP sessions. Disable to load balance proxy sessions only.  **Choices:**   - `"enable"` - `"disable"` |
| **logical_sn**  string | Enable/disable usage of the logical serial number.  **Choices:**   - `"enable"` - `"disable"` |
| **memory_based_failover**  string | Enable/disable memory based failover.  **Choices:**   - `"enable"` - `"disable"` |
| **memory_compatible_mode**  string | Enable/disable memory compatible mode.  **Choices:**   - `"enable"` - `"disable"` |
| **memory_failover_flip_timeout**  integer | Time to wait between subsequent memory based failovers in minutes (6 - 2147483647). |
| **memory_failover_monitor_period**  integer | Duration of high memory usage before memory based failover is triggered in seconds (1 - 300). |
| **memory_failover_sample_rate**  integer | Rate at which memory usage is sampled in order to measure memory usage in seconds (1 - 60). |
| **memory_failover_threshold**  integer | Memory usage threshold to trigger memory based failover (0 means using conserve mode threshold in system.global). |
| **memory_threshold**  string | Dynamic weighted load balancing memory usage weight and high and low thresholds. |
| **mode**  string | HA mode. Must be the same for all members. FGSP requires standalone.  **Choices:**   - `"standalone"` - `"a-a"` - `"a-p"` |
| **monitor**  list / elements=string | Interfaces to check for port monitoring (or link failure). Source system.interface.name. |
| **multicast_ttl**  integer | HA multicast TTL on primary (5 - 3600 sec). |
| **nntp_proxy_threshold**  string | Dynamic weighted load balancing weight and high and low number of NNTP proxy sessions. |
| **override**  string | Enable and increase the priority of the unit that should always be primary (master).  **Choices:**   - `"enable"` - `"disable"` |
| **override_wait_time**  integer | Delay negotiating if override is enabled (0 - 3600 sec). Reduces how often the cluster negotiates. |
| **password**  string | Cluster password. Must be the same for all members. |
| **pingserver_failover_threshold**  integer | Remote IP monitoring failover threshold (0 - 50). |
| **pingserver_flip_timeout**  integer | Time to wait in minutes before renegotiating after a remote IP monitoring failover. |
| **pingserver_monitor_interface**  list / elements=string | Interfaces to check for remote IP monitoring. Source system.interface.name. |
| **pingserver_secondary_force_reset**  string | Enable to force the cluster to negotiate after a remote IP monitoring failover.  **Choices:**   - `"enable"` - `"disable"` |
| **pingserver_slave_force_reset**  string | Enable to force the cluster to negotiate after a remote IP monitoring failover.  **Choices:**   - `"enable"` - `"disable"` |
| **pop3_proxy_threshold**  string | Dynamic weighted load balancing weight and high and low number of POP3 proxy sessions. |
| **priority**  integer | Increase the priority to select the primary unit (0 - 255). |
| **route_hold**  integer | Time to wait between routing table updates to the cluster (0 - 3600 sec). |
| **route_ttl**  integer | TTL for primary unit routes (5 - 3600 sec). Increase to maintain active routes during failover. |
| **route_wait**  integer | Time to wait before sending new routes to the cluster (0 - 3600 sec). |
| **schedule**  string | Type of A-A load balancing. Use none if you have external load balancers.  **Choices:**   - `"none"` - `"leastconnection"` - `"round-robin"` - `"weight-round-robin"` - `"random"` - `"ip"` - `"ipport"` - `"hub"` |
| **secondary_vcluster**  dictionary | Configure virtual cluster 2. |
| **monitor**  list / elements=string | Interfaces to check for port monitoring (or link failure). Source system.interface.name. |
| **override**  string | Enable and increase the priority of the unit that should always be primary.  **Choices:**   - `"enable"` - `"disable"` |
| **override_wait_time**  integer | Delay negotiating if override is enabled (0 - 3600 sec). Reduces how often the cluster negotiates. |
| **pingserver_failover_threshold**  integer | Remote IP monitoring failover threshold (0 - 50). |
| **pingserver_monitor_interface**  list / elements=string | Interfaces to check for remote IP monitoring. Source system.interface.name. |
| **pingserver_secondary_force_reset**  string | Enable to force the cluster to negotiate after a remote IP monitoring failover.  **Choices:**   - `"enable"` - `"disable"` |
| **pingserver_slave_force_reset**  string | Enable to force the cluster to negotiate after a remote IP monitoring failover.  **Choices:**   - `"enable"` - `"disable"` |
| **priority**  integer | Increase the priority to select the primary unit (0 - 255). |
| **vcluster_id**  integer | Cluster ID. |
| **vdom**  string | VDOMs in virtual cluster 2. |
| **session_pickup**  string | Enable/disable session pickup. Enabling it can reduce session down time when fail over happens.  **Choices:**   - `"enable"` - `"disable"` |
| **session_pickup_connectionless**  string | Enable/disable UDP and ICMP session sync.  **Choices:**   - `"enable"` - `"disable"` |
| **session_pickup_delay**  string | Enable to sync sessions longer than 30 sec. Only longer lived sessions need to be synced.  **Choices:**   - `"enable"` - `"disable"` |
| **session_pickup_expectation**  string | Enable/disable session helper expectation session sync for FGSP.  **Choices:**   - `"enable"` - `"disable"` |
| **session_pickup_nat**  string | Enable/disable NAT session sync for FGSP.  **Choices:**   - `"enable"` - `"disable"` |
| **session_sync_dev**  list / elements=string | Offload session-sync process to kernel and sync sessions using connected interface(s) directly. Source system.interface.name. |
| **smtp_proxy_threshold**  string | Dynamic weighted load balancing weight and high and low number of SMTP proxy sessions. |
| **ssd_failover**  string | Enable/disable automatic HA failover on SSD disk failure.  **Choices:**   - `"enable"` - `"disable"` |
| **standalone_config_sync**  string | Enable/disable FGSP configuration synchronization.  **Choices:**   - `"enable"` - `"disable"` |
| **standalone_mgmt_vdom**  string | Enable/disable standalone management VDOM.  **Choices:**   - `"enable"` - `"disable"` |
| **sync_config**  string | Enable/disable configuration synchronization.  **Choices:**   - `"enable"` - `"disable"` |
| **sync_packet_balance**  string | Enable/disable HA packet distribution to multiple CPUs.  **Choices:**   - `"enable"` - `"disable"` |
| **unicast_gateway**  string | Default route gateway for unicast interface. |
| **unicast_hb**  string | Enable/disable unicast heartbeat.  **Choices:**   - `"enable"` - `"disable"` |
| **unicast_hb_netmask**  string | Unicast heartbeat netmask. |
| **unicast_hb_peerip**  string | Unicast heartbeat peer IP. |
| **unicast_peers**  list / elements=dictionary | Number of unicast peers. |
| **id**  integer / required | Table ID. see <a href=’#notes’>Notes</a>. |
| **peer_ip**  string | Unicast peer IP. |
| **unicast_status**  string | Enable/disable unicast connection.  **Choices:**   - `"enable"` - `"disable"` |
| **uninterruptible_primary_wait**  integer | Number of minutes the primary HA unit waits before the secondary HA unit is considered upgraded and the system is started before starting its own upgrade (15 - 300). |
| **uninterruptible_upgrade**  string | Enable to upgrade a cluster without blocking network traffic.  **Choices:**   - `"enable"` - `"disable"` |
| **upgrade_mode**  string | The mode to upgrade a cluster.  **Choices:**   - `"simultaneous"` - `"uninterruptible"` - `"local-only"` - `"secondary-only"` |
| **vcluster**  list / elements=dictionary | Virtual cluster table. |
| **monitor**  list / elements=string | Interfaces to check for port monitoring (or link failure). Source system.interface.name. |
| **override**  string | Enable and increase the priority of the unit that should always be primary (master).  **Choices:**   - `"enable"` - `"disable"` |
| **override_wait_time**  integer | Delay negotiating if override is enabled (0 - 3600 sec). Reduces how often the cluster negotiates. |
| **pingserver_failover_threshold**  integer | Remote IP monitoring failover threshold (0 - 50). |
| **pingserver_monitor_interface**  list / elements=string | Interfaces to check for remote IP monitoring. Source system.interface.name. |
| **pingserver_secondary_force_reset**  string | Enable to force the cluster to negotiate after a remote IP monitoring failover.  **Choices:**   - `"enable"` - `"disable"` |
| **pingserver_slave_force_reset**  string | Enable to force the cluster to negotiate after a remote IP monitoring failover.  **Choices:**   - `"enable"` - `"disable"` |
| **priority**  integer | Increase the priority to select the primary unit (0 - 255). |
| **vcluster_id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **vdom**  list / elements=dictionary | Virtual domain(s) in the virtual cluster. |
| **name**  string / required | Virtual domain name. Source system.vdom.name. |
| **vcluster2**  string | Enable/disable virtual cluster 2 for virtual clustering.  **Choices:**   - `"enable"` - `"disable"` |
| **vcluster_id**  integer | Cluster ID. |
| **vcluster_status**  string | Enable/disable virtual cluster for virtual clustering.  **Choices:**   - `"enable"` - `"disable"` |
| **vdom**  string | VDOMs in virtual cluster 1. |
| **weight**  string | Weight-round-robin weight for each cluster unit. Syntax <priority> <weight>. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_system_ha_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_ha_module.md#id5)

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
  - name: Configure HA.
    fortios_system_ha:
      vdom:  "{{ vdom }}"
      system_ha:
        arps: "5"
        arps_interval: "8"
        authentication: "enable"
        cpu_threshold: "<your_own_value>"
        encryption: "enable"
        evpn_ttl: "60"
        failover_hold_time: "0"
        ftp_proxy_threshold: "<your_own_value>"
        gratuitous_arps: "enable"
        group_id: "0"
        group_name: "<your_own_value>"
        ha_direct: "enable"
        ha_eth_type: "<your_own_value>"
        ha_mgmt_interfaces:
         -
            dst: "<your_own_value>"
            gateway: "<your_own_value>"
            gateway6: "<your_own_value>"
            id:  "20"
            interface: "<your_own_value> (source system.interface.name)"
        ha_mgmt_status: "enable"
        ha_uptime_diff_margin: "300"
        hb_interval: "2"
        hb_interval_in_milliseconds: "100ms"
        hb_lost_threshold: "20"
        hbdev: "<your_own_value>"
        hc_eth_type: "<your_own_value>"
        hello_holddown: "20"
        http_proxy_threshold: "<your_own_value>"
        imap_proxy_threshold: "<your_own_value>"
        inter_cluster_session_sync: "enable"
        key: "<your_own_value>"
        l2ep_eth_type: "<your_own_value>"
        link_failed_signal: "enable"
        load_balance_all: "enable"
        logical_sn: "enable"
        memory_based_failover: "enable"
        memory_compatible_mode: "enable"
        memory_failover_flip_timeout: "6"
        memory_failover_monitor_period: "60"
        memory_failover_sample_rate: "1"
        memory_failover_threshold: "0"
        memory_threshold: "<your_own_value>"
        mode: "standalone"
        monitor: "<your_own_value> (source system.interface.name)"
        multicast_ttl: "600"
        nntp_proxy_threshold: "<your_own_value>"
        override: "enable"
        override_wait_time: "0"
        password: "<your_own_value>"
        pingserver_failover_threshold: "0"
        pingserver_flip_timeout: "60"
        pingserver_monitor_interface: "<your_own_value> (source system.interface.name)"
        pingserver_secondary_force_reset: "enable"
        pingserver_slave_force_reset: "enable"
        pop3_proxy_threshold: "<your_own_value>"
        priority: "128"
        route_hold: "10"
        route_ttl: "10"
        route_wait: "0"
        schedule: "none"
        secondary_vcluster:
            monitor: "<your_own_value> (source system.interface.name)"
            override: "enable"
            override_wait_time: "0"
            pingserver_failover_threshold: "0"
            pingserver_monitor_interface: "<your_own_value> (source system.interface.name)"
            pingserver_secondary_force_reset: "enable"
            pingserver_slave_force_reset: "enable"
            priority: "128"
            vcluster_id: "1"
            vdom: "<your_own_value>"
        session_pickup: "enable"
        session_pickup_connectionless: "enable"
        session_pickup_delay: "enable"
        session_pickup_expectation: "enable"
        session_pickup_nat: "enable"
        session_sync_dev: "<your_own_value> (source system.interface.name)"
        smtp_proxy_threshold: "<your_own_value>"
        ssd_failover: "enable"
        standalone_config_sync: "enable"
        standalone_mgmt_vdom: "enable"
        sync_config: "enable"
        sync_packet_balance: "enable"
        unicast_gateway: "<your_own_value>"
        unicast_hb: "enable"
        unicast_hb_netmask: "<your_own_value>"
        unicast_hb_peerip: "<your_own_value>"
        unicast_peers:
         -
            id:  "91"
            peer_ip: "<your_own_value>"
        unicast_status: "enable"
        uninterruptible_primary_wait: "30"
        uninterruptible_upgrade: "enable"
        upgrade_mode: "simultaneous"
        vcluster:
         -
            monitor: "<your_own_value> (source system.interface.name)"
            override: "enable"
            override_wait_time: "0"
            pingserver_failover_threshold: "0"
            pingserver_monitor_interface: "<your_own_value> (source system.interface.name)"
            pingserver_secondary_force_reset: "enable"
            pingserver_slave_force_reset: "enable"
            priority: "128"
            vcluster_id: "<you_own_value>"
            vdom:
             -
                name: "default_name_108 (source system.vdom.name)"
        vcluster_id: "0"
        vcluster_status: "enable"
        vcluster2: "enable"
        vdom: "<your_own_value>"
        weight: "<your_own_value>"
```

## [Return Values](fortios_system_ha_module.md#id6)

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
