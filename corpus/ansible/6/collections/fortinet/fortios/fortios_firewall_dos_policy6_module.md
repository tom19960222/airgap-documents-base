---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_firewall_dos_policy6 module – Configure IPv6 DoS policies in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_firewall_dos_policy6_module.html
fetched_at: 2026-07-27T17:40:50+00:00
---
# fortinet.fortios.fortios_firewall_dos_policy6 module – Configure IPv6 DoS policies in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_dos_policy6_module.md#ansible-collections-fortinet-fortios-fortios-firewall-dos-policy6-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_dos_policy6`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_dos_policy6_module.md#synopsis)
- [Requirements](fortios_firewall_dos_policy6_module.md#requirements)
- [Parameters](fortios_firewall_dos_policy6_module.md#parameters)
- [Notes](fortios_firewall_dos_policy6_module.md#notes)
- [Examples](fortios_firewall_dos_policy6_module.md#examples)
- [Return Values](fortios_firewall_dos_policy6_module.md#return-values)

## [Synopsis](fortios_firewall_dos_policy6_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and dos_policy6 category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_dos_policy6_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_firewall_dos_policy6_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **firewall_dos_policy6**  dictionary | Configure IPv6 DoS policies. |
| **anomaly**  list / elements=dictionary | Anomaly name. |
| **action**  string | Action taken when the threshold is reached.  Choices:   - `"pass"` - `"block"` - `"proxy"` |
| **log**  string | Enable/disable anomaly logging.  Choices:   - `"enable"` - `"disable"` |
| **name**  string | Anomaly name. |
| **quarantine**  string | Quarantine method.  Choices:   - `"none"` - `"attacker"` |
| **quarantine_expiry**  string | Duration of quarantine. (Format |
| **quarantine_log**  string | Enable/disable quarantine logging.  Choices:   - `"disable"` - `"enable"` |
| **status**  string | Enable/disable this anomaly.  Choices:   - `"disable"` - `"enable"` |
| **threshold**  integer | Anomaly threshold. Number of detected instances (packets per second or concurrent session number) that triggers the anomaly action. |
| **threshold_default**  integer | Number of detected instances per minute which triggers action (1 - 2147483647). Note that each anomaly has a different threshold value assigned to it. |
| **comments**  string | Comment. |
| **dstaddr**  list / elements=dictionary | Destination address name from available addresses. |
| **name**  string | Address name. Source firewall.address6.name firewall.addrgrp6.name. |
| **interface**  string | Incoming interface name from available interfaces. Source system.zone.name system.interface.name. |
| **name**  string | Policy name. |
| **policyid**  integer / required | Policy ID. |
| **service**  list / elements=dictionary | Service object from available options. |
| **name**  string | Service name. Source firewall.service.custom.name firewall.service.group.name. |
| **srcaddr**  list / elements=dictionary | Source address name from available addresses. |
| **name**  string | Address name. Source firewall.address6.name firewall.addrgrp6.name. |
| **status**  string | Enable/disable this policy.  Choices:   - `"enable"` - `"disable"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_firewall_dos_policy6_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_dos_policy6_module.md#id5)

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
  - name: Configure IPv6 DoS policies.
    fortios_firewall_dos_policy6:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_dos_policy6:
        anomaly:
         -
            action: "pass"
            log: "enable"
            name: "default_name_6"
            quarantine: "none"
            quarantine_expiry: "<your_own_value>"
            quarantine_log: "disable"
            status: "disable"
            threshold: "0"
            threshold_default: "0"
        comments: "<your_own_value>"
        dstaddr:
         -
            name: "default_name_15 (source firewall.address6.name firewall.addrgrp6.name)"
        interface: "<your_own_value> (source system.zone.name system.interface.name)"
        name: "default_name_17"
        policyid: "0"
        service:
         -
            name: "default_name_20 (source firewall.service.custom.name firewall.service.group.name)"
        srcaddr:
         -
            name: "default_name_22 (source firewall.address6.name firewall.addrgrp6.name)"
        status: "enable"
```

## [Return Values](fortios_firewall_dos_policy6_module.md#id6)

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
