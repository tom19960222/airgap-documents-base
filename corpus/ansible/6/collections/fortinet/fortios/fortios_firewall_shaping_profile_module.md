---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_firewall_shaping_profile module – Configure shaping profiles in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_firewall_shaping_profile_module.html
fetched_at: 2026-07-27T17:41:33+00:00
---
# fortinet.fortios.fortios_firewall_shaping_profile module – Configure shaping profiles in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_shaping_profile_module.md#ansible-collections-fortinet-fortios-fortios-firewall-shaping-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_shaping_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_shaping_profile_module.md#synopsis)
- [Requirements](fortios_firewall_shaping_profile_module.md#requirements)
- [Parameters](fortios_firewall_shaping_profile_module.md#parameters)
- [Notes](fortios_firewall_shaping_profile_module.md#notes)
- [Examples](fortios_firewall_shaping_profile_module.md#examples)
- [Return Values](fortios_firewall_shaping_profile_module.md#return-values)

## [Synopsis](fortios_firewall_shaping_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and shaping_profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_shaping_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_firewall_shaping_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **firewall_shaping_profile**  dictionary | Configure shaping profiles. |
| **comment**  string | Comment. |
| **default_class_id**  integer | Default class ID to handle unclassified packets (including all local traffic). Source firewall.traffic-class.class-id. |
| **profile_name**  string | Shaping profile name. |
| **shaping_entries**  list / elements=dictionary | Define shaping entries of this shaping profile. |
| **burst_in_msec**  integer | Number of bytes that can be burst at maximum-bandwidth speed. Formula: burst = maximum-bandwidth\*burst-in-msec. |
| **cburst_in_msec**  integer | Number of bytes that can be burst as fast as the interface can transmit. Formula: cburst = maximum-bandwidth\*cburst-in-msec. |
| **class_id**  integer | Class ID. Source firewall.traffic-class.class-id. |
| **guaranteed_bandwidth_percentage**  integer | Guaranteed bandwidth in percentage. |
| **id**  integer | ID number. |
| **limit**  integer | Hard limit on the real queue size in packets. |
| **max**  integer | Average queue size in packets at which RED drop probability is maximal. |
| **maximum_bandwidth_percentage**  integer | Maximum bandwidth in percentage. |
| **min**  integer | Average queue size in packets at which RED drop becomes a possibility. |
| **priority**  string | Priority.  Choices:   - `"top"` - `"critical"` - `"high"` - `"medium"` - `"low"` |
| **red_probability**  integer | Maximum probability (in percentage) for RED marking. |
| **type**  string | Select shaping profile type: policing / queuing.  Choices:   - `"policing"` - `"queuing"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_firewall_shaping_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_shaping_profile_module.md#id5)

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
  - name: Configure shaping profiles.
    fortios_firewall_shaping_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_shaping_profile:
        comment: "Comment."
        default_class_id: "0"
        profile_name: "<your_own_value>"
        shaping_entries:
         -
            burst_in_msec: "0"
            cburst_in_msec: "0"
            class_id: "0"
            guaranteed_bandwidth_percentage: "0"
            id:  "11"
            limit: "1000"
            max: "250"
            maximum_bandwidth_percentage: "1"
            min: "83"
            priority: "top"
            red_probability: "0"
        type: "policing"
```

## [Return Values](fortios_firewall_shaping_profile_module.md#id6)

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
