---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_dpdk_global module – Configure global DPDK options in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_dpdk_global_module.html
fetched_at: 2026-07-27T17:40:14+00:00
---
# fortinet.fortios.fortios_dpdk_global module – Configure global DPDK options in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_dpdk_global_module.md#ansible-collections-fortinet-fortios-fortios-dpdk-global-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_dpdk_global`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_dpdk_global_module.md#synopsis)
- [Requirements](fortios_dpdk_global_module.md#requirements)
- [Parameters](fortios_dpdk_global_module.md#parameters)
- [Notes](fortios_dpdk_global_module.md#notes)
- [Examples](fortios_dpdk_global_module.md#examples)
- [Return Values](fortios_dpdk_global_module.md#return-values)

## [Synopsis](fortios_dpdk_global_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify dpdk feature and global category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_dpdk_global_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_dpdk_global_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **dpdk_global**  dictionary | Configure global DPDK options. |
| **elasticbuffer**  string | Enable/disable elasticbuffer support for all DPDK ports.  Choices:   - `"disable"` - `"enable"` |
| **hugepage_percentage**  integer | Percentage of main memory allocated to hugepages, which are available for DPDK operation. |
| **interface**  list / elements=dictionary | Physical interfaces that enable DPDK. |
| **interface_name**  string | Physical interface name. Source system.interface.name. |
| **ipsec_offload**  string | Enable/disable DPDK IPsec phase 2 offloading.  Choices:   - `"disable"` - `"enable"` |
| **mbufpool_percentage**  integer | Percentage of main memory allocated to DPDK packet buffer. |
| **multiqueue**  string | Enable/disable multi-queue RX/TX support for all DPDK ports.  Choices:   - `"disable"` - `"enable"` |
| **per_session_accounting**  string | Enable/disable per-session accounting.  Choices:   - `"disable"` - `"traffic-log-only"` - `"enable"` |
| **sleep_on_idle**  string | Enable/disable sleep-on-idle support for all FDH engines.  Choices:   - `"disable"` - `"enable"` |
| **status**  string | Enable/disable DPDK operation for the entire system.  Choices:   - `"disable"` - `"enable"` |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_dpdk_global_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_dpdk_global_module.md#id5)

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
  - name: Configure global DPDK options.
    fortios_dpdk_global:
      vdom:  "{{ vdom }}"
      dpdk_global:
        elasticbuffer: "disable"
        hugepage_percentage: "30"
        interface:
         -
            interface_name: "<your_own_value> (source system.interface.name)"
        ipsec_offload: "disable"
        mbufpool_percentage: "25"
        multiqueue: "disable"
        per_session_accounting: "disable"
        sleep_on_idle: "disable"
        status: "disable"
```

## [Return Values](fortios_dpdk_global_module.md#id6)

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
