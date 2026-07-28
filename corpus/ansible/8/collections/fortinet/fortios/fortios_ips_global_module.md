---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_ips_global module – Configure IPS global parameter in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_ips_global_module.html
fetched_at: 2026-07-28T02:25:40+00:00
---
# fortinet.fortios.fortios_ips_global module – Configure IPS global parameter in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_ips_global_module.md#ansible-collections-fortinet-fortios-fortios-ips-global-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_ips_global`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_ips_global_module.md#synopsis)
- [Requirements](fortios_ips_global_module.md#requirements)
- [Parameters](fortios_ips_global_module.md#parameters)
- [Notes](fortios_ips_global_module.md#notes)
- [Examples](fortios_ips_global_module.md#examples)
- [Return Values](fortios_ips_global_module.md#return-values)

## [Synopsis](fortios_ips_global_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify ips feature and global category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_ips_global_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_ips_global_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **ips_global**  dictionary | Configure IPS global parameter. |
| **anomaly_mode**  string | Global blocking mode for rate-based anomalies.  **Choices:**   - `"periodical"` - `"continuous"` |
| **cp_accel_mode**  string | IPS Pattern matching acceleration/offloading to CPx processors.  **Choices:**   - `"none"` - `"basic"` - `"advanced"` |
| **database**  string | Regular or extended IPS database. Regular protects against the latest common and in-the-wild attacks. Extended includes protection from legacy attacks.  **Choices:**   - `"regular"` - `"extended"` |
| **deep_app_insp_db_limit**  integer | Limit on number of entries in deep application inspection database (1 - 2147483647, use recommended setting = 0). |
| **deep_app_insp_timeout**  integer | Timeout for Deep application inspection (1 - 2147483647 sec., 0 = use recommended setting). |
| **engine_count**  integer | Number of IPS engines running. If set to the default value of 0, FortiOS sets the number to optimize performance depending on the number of CPU cores. |
| **exclude_signatures**  string | Excluded signatures.  **Choices:**   - `"none"` - `"ot"` - `"industrial"` |
| **fail_open**  string | Enable to allow traffic if the IPS buffer is full. Default is disable and IPS traffic is blocked when the IPS buffer is full.  **Choices:**   - `"enable"` - `"disable"` |
| **intelligent_mode**  string | Enable/disable IPS adaptive scanning (intelligent mode). Intelligent mode optimizes the scanning method for the type of traffic.  **Choices:**   - `"enable"` - `"disable"` |
| **ips_reserve_cpu**  string | Enable/disable IPS daemon”s use of CPUs other than CPU 0.  **Choices:**   - `"disable"` - `"enable"` |
| **ngfw_max_scan_range**  integer | NGFW policy-mode app detection threshold. |
| **np_accel_mode**  string | Acceleration mode for IPS processing by NPx processors.  **Choices:**   - `"none"` - `"basic"` |
| **packet_log_queue_depth**  integer | Packet/pcap log queue depth per IPS engine. |
| **session_limit_mode**  string | Method of counting concurrent sessions used by session limit anomalies. Choose between greater accuracy (accurate) or improved performance (heuristics).  **Choices:**   - `"accurate"` - `"heuristic"` |
| **skype_client_public_ipaddr**  string | Public IP addresses of your network that receive Skype sessions. Helps identify Skype sessions. Separate IP addresses with commas. |
| **socket_size**  integer | IPS socket buffer size. Max and default value depend on available memory. Can be changed to tune performance. |
| **sync_session_ttl**  string | Enable/disable use of kernel session TTL for IPS sessions.  **Choices:**   - `"enable"` - `"disable"` |
| **tls_active_probe**  dictionary | TLS active probe configuration. |
| **interface**  string | Specify outgoing interface to reach server. Source system.interface.name. |
| **interface_select_method**  string | Specify how to select outgoing interface to reach server.  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **source_ip**  string | Source IP address used for TLS active probe. |
| **source_ip6**  string | Source IPv6 address used for TLS active probe. |
| **vdom**  string | Virtual domain name for TLS active probe. Source system.vdom.name. |
| **traffic_submit**  string | Enable/disable submitting attack data found by this FortiGate to FortiGuard.  **Choices:**   - `"enable"` - `"disable"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_ips_global_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_ips_global_module.md#id5)

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
  - name: Configure IPS global parameter.
    fortios_ips_global:
      vdom:  "{{ vdom }}"
      ips_global:
        anomaly_mode: "periodical"
        cp_accel_mode: "none"
        database: "regular"
        deep_app_insp_db_limit: "0"
        deep_app_insp_timeout: "0"
        engine_count: "0"
        exclude_signatures: "none"
        fail_open: "enable"
        intelligent_mode: "enable"
        ips_reserve_cpu: "disable"
        ngfw_max_scan_range: "4096"
        np_accel_mode: "none"
        packet_log_queue_depth: "128"
        session_limit_mode: "accurate"
        skype_client_public_ipaddr: "<your_own_value>"
        socket_size: "256"
        sync_session_ttl: "enable"
        tls_active_probe:
            interface: "<your_own_value> (source system.interface.name)"
            interface_select_method: "auto"
            source_ip: "84.230.14.43"
            source_ip6: "<your_own_value>"
            vdom: "<your_own_value> (source system.vdom.name)"
        traffic_submit: "enable"
```

## [Return Values](fortios_ips_global_module.md#id6)

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
