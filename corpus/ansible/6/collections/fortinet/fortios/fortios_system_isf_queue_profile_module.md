---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_system_isf_queue_profile module – Create a queue profile of switch in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_system_isf_queue_profile_module.html
fetched_at: 2026-07-27T17:44:47+00:00
---
# fortinet.fortios.fortios_system_isf_queue_profile module – Create a queue profile of switch in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_isf_queue_profile_module.md#ansible-collections-fortinet-fortios-fortios-system-isf-queue-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_isf_queue_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_isf_queue_profile_module.md#synopsis)
- [Requirements](fortios_system_isf_queue_profile_module.md#requirements)
- [Parameters](fortios_system_isf_queue_profile_module.md#parameters)
- [Notes](fortios_system_isf_queue_profile_module.md#notes)
- [Examples](fortios_system_isf_queue_profile_module.md#examples)
- [Return Values](fortios_system_isf_queue_profile_module.md#return-values)

## [Synopsis](fortios_system_isf_queue_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and isf_queue_profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_isf_queue_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_system_isf_queue_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **system_isf_queue_profile**  dictionary | Create a queue profile of switch. |
| **bandwidth_unit**  string | Unit of measurement for guaranteed and maximum bandwidth.  Choices:   - `"kbps"` - `"pps"` |
| **burst_bps_granularity**  string | Burst granularity based on bytes per second.  Choices:   - `"disable"` - `"512-bytes"` - `"1k-bytes"` - `"2k-bytes"` - `"4k-bytes"` - `"8k-bytes"` - `"16k-bytes"` - `"32k-bytes"` |
| **burst_control**  string | Burst control.  Choices:   - `"disable"` - `"enable"` |
| **burst_pps_granularity**  string | Burst granularity based on packets per second.  Choices:   - `"disable"` - `"half-packet"` - `"1-packet"` - `"2-packets"` - `"4-packets"` - `"16-packets"` - `"65-packets"` - `"262-packets"` |
| **guaranteed_bandwidth**  integer | Guaranteed bandwidth. |
| **maximum_bandwidth**  integer | Upper bandwidth limit enforced. |
| **name**  string / required | Profile name. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_system_isf_queue_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_isf_queue_profile_module.md#id5)

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
  - name: Create a queue profile of switch.
    fortios_system_isf_queue_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_isf_queue_profile:
        bandwidth_unit: "kbps"
        burst_bps_granularity: "disable"
        burst_control: "disable"
        burst_pps_granularity: "disable"
        guaranteed_bandwidth: "0"
        maximum_bandwidth: "0"
        name: "default_name_9"
```

## [Return Values](fortios_system_isf_queue_profile_module.md#id6)

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
