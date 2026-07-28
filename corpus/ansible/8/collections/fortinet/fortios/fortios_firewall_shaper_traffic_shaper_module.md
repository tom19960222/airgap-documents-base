---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_firewall_shaper_traffic_shaper module – Configure shared traffic shaper in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_firewall_shaper_traffic_shaper_module.html
fetched_at: 2026-07-28T02:25:08+00:00
---
# fortinet.fortios.fortios_firewall_shaper_traffic_shaper module – Configure shared traffic shaper in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_shaper_traffic_shaper_module.md#ansible-collections-fortinet-fortios-fortios-firewall-shaper-traffic-shaper-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_shaper_traffic_shaper`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_shaper_traffic_shaper_module.md#synopsis)
- [Requirements](fortios_firewall_shaper_traffic_shaper_module.md#requirements)
- [Parameters](fortios_firewall_shaper_traffic_shaper_module.md#parameters)
- [Notes](fortios_firewall_shaper_traffic_shaper_module.md#notes)
- [Examples](fortios_firewall_shaper_traffic_shaper_module.md#examples)
- [Return Values](fortios_firewall_shaper_traffic_shaper_module.md#return-values)

## [Synopsis](fortios_firewall_shaper_traffic_shaper_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall_shaper feature and traffic_shaper category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_shaper_traffic_shaper_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_firewall_shaper_traffic_shaper_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_shaper_traffic_shaper**  dictionary | Configure shared traffic shaper. |
| **bandwidth_unit**  string | Unit of measurement for guaranteed and maximum bandwidth for this shaper (Kbps, Mbps or Gbps).  **Choices:**   - `"kbps"` - `"mbps"` - `"gbps"` |
| **cos**  string | VLAN CoS mark. |
| **cos_marking**  string | Enable/disable VLAN CoS marking.  **Choices:**   - `"enable"` - `"disable"` |
| **cos_marking_method**  string | Select VLAN CoS marking method.  **Choices:**   - `"multi-stage"` - `"static"` |
| **diffserv**  string | Enable/disable changing the DiffServ setting applied to traffic accepted by this shaper.  **Choices:**   - `"enable"` - `"disable"` |
| **diffservcode**  string | DiffServ setting to be applied to traffic accepted by this shaper. |
| **dscp_marking_method**  string | Select DSCP marking method.  **Choices:**   - `"multi-stage"` - `"static"` |
| **exceed_bandwidth**  integer | Exceed bandwidth used for DSCP/VLAN CoS multi-stage marking. Units depend on the bandwidth-unit setting. |
| **exceed_class_id**  integer | Class ID for traffic in guaranteed-bandwidth and maximum-bandwidth. Source firewall.traffic-class.class-id. |
| **exceed_cos**  string | VLAN CoS mark for traffic in [guaranteed-bandwidth, exceed-bandwidth]. |
| **exceed_dscp**  string | DSCP mark for traffic in guaranteed-bandwidth and exceed-bandwidth. |
| **guaranteed_bandwidth**  integer | Amount of bandwidth guaranteed for this shaper (0 - 80000000). Units depend on the bandwidth-unit setting. |
| **maximum_bandwidth**  integer | Upper bandwidth limit enforced by this shaper (0 - 80000000). 0 means no limit. Units depend on the bandwidth-unit setting. |
| **maximum_cos**  string | VLAN CoS mark for traffic in [exceed-bandwidth, maximum-bandwidth]. |
| **maximum_dscp**  string | DSCP mark for traffic in exceed-bandwidth and maximum-bandwidth. |
| **name**  string / required | Traffic shaper name. |
| **overhead**  integer | Per-packet size overhead used in rate computations. |
| **per_policy**  string | Enable/disable applying a separate shaper for each policy. For example, if enabled the guaranteed bandwidth is applied separately for each policy.  **Choices:**   - `"disable"` - `"enable"` |
| **priority**  string | Higher priority traffic is more likely to be forwarded without delays and without compromising the guaranteed bandwidth.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_firewall_shaper_traffic_shaper_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_shaper_traffic_shaper_module.md#id5)

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
  - name: Configure shared traffic shaper.
    fortios_firewall_shaper_traffic_shaper:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_shaper_traffic_shaper:
        bandwidth_unit: "kbps"
        cos: "<your_own_value>"
        cos_marking: "enable"
        cos_marking_method: "multi-stage"
        diffserv: "enable"
        diffservcode: "<your_own_value>"
        dscp_marking_method: "multi-stage"
        exceed_bandwidth: "0"
        exceed_class_id: "0"
        exceed_cos: "<your_own_value>"
        exceed_dscp: "<your_own_value>"
        guaranteed_bandwidth: "0"
        maximum_bandwidth: "0"
        maximum_cos: "<your_own_value>"
        maximum_dscp: "<your_own_value>"
        name: "default_name_18"
        overhead: "0"
        per_policy: "disable"
        priority: "low"
```

## [Return Values](fortios_firewall_shaper_traffic_shaper_module.md#id6)

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
