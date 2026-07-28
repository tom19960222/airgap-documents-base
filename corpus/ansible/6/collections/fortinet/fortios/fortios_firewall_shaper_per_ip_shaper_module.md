---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_firewall_shaper_per_ip_shaper module – Configure per-IP traffic shaper in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_firewall_shaper_per_ip_shaper_module.html
fetched_at: 2026-07-27T17:41:31+00:00
---
# fortinet.fortios.fortios_firewall_shaper_per_ip_shaper module – Configure per-IP traffic shaper in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/fortinet/fortios) (version 2.2.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_firewall_shaper_per_ip_shaper_module.md#ansible-collections-fortinet-fortios-fortios-firewall-shaper-per-ip-shaper-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_shaper_per_ip_shaper`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_shaper_per_ip_shaper_module.md#synopsis)
- [Requirements](fortios_firewall_shaper_per_ip_shaper_module.md#requirements)
- [Parameters](fortios_firewall_shaper_per_ip_shaper_module.md#parameters)
- [Notes](fortios_firewall_shaper_per_ip_shaper_module.md#notes)
- [Examples](fortios_firewall_shaper_per_ip_shaper_module.md#examples)
- [Return Values](fortios_firewall_shaper_per_ip_shaper_module.md#return-values)

## [Synopsis](fortios_firewall_shaper_per_ip_shaper_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall_shaper feature and per_ip_shaper category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_shaper_per_ip_shaper_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_firewall_shaper_per_ip_shaper_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **firewall_shaper_per_ip_shaper**  dictionary | Configure per-IP traffic shaper. |
| **bandwidth_unit**  string | Unit of measurement for maximum bandwidth for this shaper (Kbps, Mbps or Gbps).  Choices:   - `"kbps"` - `"mbps"` - `"gbps"` |
| **diffserv_forward**  string | Enable/disable changing the Forward (original) DiffServ setting applied to traffic accepted by this shaper.  Choices:   - `"enable"` - `"disable"` |
| **diffserv_reverse**  string | Enable/disable changing the Reverse (reply) DiffServ setting applied to traffic accepted by this shaper.  Choices:   - `"enable"` - `"disable"` |
| **diffservcode_forward**  string | Forward (original) DiffServ setting to be applied to traffic accepted by this shaper. |
| **diffservcode_rev**  string | Reverse (reply) DiffServ setting to be applied to traffic accepted by this shaper. |
| **max_bandwidth**  integer | Upper bandwidth limit enforced by this shaper (0 - 80000000). 0 means no limit. Units depend on the bandwidth-unit setting. |
| **max_concurrent_session**  integer | Maximum number of concurrent sessions allowed by this shaper (0 - 2097000). 0 means no limit. |
| **max_concurrent_tcp_session**  integer | Maximum number of concurrent TCP sessions allowed by this shaper (0 - 2097000). 0 means no limit. |
| **max_concurrent_udp_session**  integer | Maximum number of concurrent UDP sessions allowed by this shaper (0 - 2097000). 0 means no limit. |
| **name**  string / required | Traffic shaper name. |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_firewall_shaper_per_ip_shaper_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_shaper_per_ip_shaper_module.md#id5)

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
  - name: Configure per-IP traffic shaper.
    fortios_firewall_shaper_per_ip_shaper:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_shaper_per_ip_shaper:
        bandwidth_unit: "kbps"
        diffserv_forward: "enable"
        diffserv_reverse: "enable"
        diffservcode_forward: "<your_own_value>"
        diffservcode_rev: "<your_own_value>"
        max_bandwidth: "0"
        max_concurrent_session: "0"
        max_concurrent_tcp_session: "0"
        max_concurrent_udp_session: "0"
        name: "default_name_12"
```

## [Return Values](fortios_firewall_shaper_per_ip_shaper_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  Returned: always  Sample: `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  Returned: always  Sample: `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  Returned: always  Sample: `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  Returned: success  Sample: `"id"` |
| **name**  string | Name of the table used to fulfill the request  Returned: always  Sample: `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  Returned: always  Sample: `"webfilter"` |
| **revision**  string | Internal revision number  Returned: always  Sample: `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  Returned: always  Sample: `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  Returned: always  Sample: `"success"` |
| **vdom**  string | Virtual domain used  Returned: always  Sample: `"root"` |
| **version**  string | Version of the FortiGate  Returned: always  Sample: `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
[Homepage](https://www.fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
