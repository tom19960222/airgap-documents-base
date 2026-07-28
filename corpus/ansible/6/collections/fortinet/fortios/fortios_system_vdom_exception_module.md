---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_system_vdom_exception module – Global configuration objects that can be configured independently across different ha peers for all VDOMs or for the defined VDOM scope in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_system_vdom_exception_module.html
fetched_at: 2026-07-27T17:45:42+00:00
---
# fortinet.fortios.fortios_system_vdom_exception module – Global configuration objects that can be configured independently across different ha peers for all VDOMs or for the defined VDOM scope in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_vdom_exception_module.md#ansible-collections-fortinet-fortios-fortios-system-vdom-exception-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_vdom_exception`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_vdom_exception_module.md#synopsis)
- [Requirements](fortios_system_vdom_exception_module.md#requirements)
- [Parameters](fortios_system_vdom_exception_module.md#parameters)
- [Notes](fortios_system_vdom_exception_module.md#notes)
- [Examples](fortios_system_vdom_exception_module.md#examples)
- [Return Values](fortios_system_vdom_exception_module.md#return-values)

## [Synopsis](fortios_system_vdom_exception_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and vdom_exception category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_vdom_exception_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_system_vdom_exception_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **system_vdom_exception**  dictionary | Global configuration objects that can be configured independently across different ha peers for all VDOMs or for the defined VDOM scope. |
| **id**  integer / required | Index (1 - 4096). |
| **object**  string | Name of the configuration object that can be configured independently for all VDOMs.  Choices:   - `"log.fortianalyzer.setting"` - `"log.fortianalyzer.override-setting"` - `"log.fortianalyzer2.setting"` - `"log.fortianalyzer2.override-setting"` - `"log.fortianalyzer3.setting"` - `"log.fortianalyzer3.override-setting"` - `"log.fortianalyzer-cloud.setting"` - `"log.fortianalyzer-cloud.override-setting"` - `"log.syslogd.setting"` - `"log.syslogd.override-setting"` - `"log.syslogd2.setting"` - `"log.syslogd2.override-setting"` - `"log.syslogd3.setting"` - `"log.syslogd3.override-setting"` - `"log.syslogd4.setting"` - `"log.syslogd4.override-setting"` - `"system.gre-tunnel"` - `"system.central-management"` - `"system.csf"` - `"user.radius"` - `"system.interface"` - `"vpn.ipsec.phase1-interface"` - `"vpn.ipsec.phase2-interface"` - `"router.bgp"` - `"router.route-map"` - `"router.prefix-list"` - `"firewall.ippool"` - `"firewall.ippool6"` - `"router.static"` - `"router.static6"` - `"firewall.vip"` - `"firewall.vip6"` - `"system.sdwan"` - `"system.saml"` - `"router.policy"` - `"router.policy6"` - `"firewall.vip46"` - `"firewall.vip64"` |
| **oid**  integer | Object ID. |
| **scope**  string | Determine whether the configuration object can be configured separately for all VDOMs or if some VDOMs share the same configuration.  Choices:   - `"all"` - `"inclusive"` - `"exclusive"` |
| **vdom**  list / elements=dictionary | Names of the VDOMs. |
| **name**  string | VDOM name. Source system.vdom.name. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_system_vdom_exception_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_vdom_exception_module.md#id5)

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
  - name: Global configuration objects that can be configured independently across different ha peers for all VDOMs or for the defined VDOM scope.
    fortios_system_vdom_exception:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_vdom_exception:
        id:  "3"
        object: "log.fortianalyzer.setting"
        oid: "32767"
        scope: "all"
        vdom:
         -
            name: "default_name_8 (source system.vdom.name)"
```

## [Return Values](fortios_system_vdom_exception_module.md#id6)

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
