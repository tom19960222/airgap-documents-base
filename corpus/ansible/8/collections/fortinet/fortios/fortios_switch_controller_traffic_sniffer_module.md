---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_switch_controller_traffic_sniffer module – Configure FortiSwitch RSPAN/ERSPAN traffic sniffing parameters in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_switch_controller_traffic_sniffer_module.html
fetched_at: 2026-07-28T02:27:46+00:00
---
# fortinet.fortios.fortios_switch_controller_traffic_sniffer module – Configure FortiSwitch RSPAN/ERSPAN traffic sniffing parameters in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_switch_controller_traffic_sniffer_module.md#ansible-collections-fortinet-fortios-fortios-switch-controller-traffic-sniffer-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_switch_controller_traffic_sniffer`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_switch_controller_traffic_sniffer_module.md#synopsis)
- [Requirements](fortios_switch_controller_traffic_sniffer_module.md#requirements)
- [Parameters](fortios_switch_controller_traffic_sniffer_module.md#parameters)
- [Notes](fortios_switch_controller_traffic_sniffer_module.md#notes)
- [Examples](fortios_switch_controller_traffic_sniffer_module.md#examples)
- [Return Values](fortios_switch_controller_traffic_sniffer_module.md#return-values)

## [Synopsis](fortios_switch_controller_traffic_sniffer_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify switch_controller feature and traffic_sniffer category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_switch_controller_traffic_sniffer_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_switch_controller_traffic_sniffer_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **switch_controller_traffic_sniffer**  dictionary | Configure FortiSwitch RSPAN/ERSPAN traffic sniffing parameters. |
| **erspan_ip**  string | Configure ERSPAN collector IP address. |
| **mode**  string | Configure traffic sniffer mode.  **Choices:**   - `"erspan-auto"` - `"rspan"` - `"none"` |
| **target_ip**  list / elements=dictionary | Sniffer IPs to filter. |
| **description**  string | Description for the sniffer IP. |
| **dst_entry_id**  integer | FortiSwitch dest entry ID for the sniffer IP. |
| **ip**  string / required | Sniffer IP. |
| **src_entry_id**  integer | FortiSwitch source entry ID for the sniffer IP. |
| **target_mac**  list / elements=dictionary | Sniffer MACs to filter. |
| **description**  string | Description for the sniffer MAC. |
| **dst_entry_id**  integer | FortiSwitch dest entry ID for the sniffer MAC. |
| **mac**  string / required | Sniffer MAC. |
| **src_entry_id**  integer | FortiSwitch source entry ID for the sniffer MAC. |
| **target_port**  list / elements=dictionary | Sniffer ports to filter. |
| **description**  string | Description for the sniffer port entry. |
| **in_ports**  list / elements=dictionary | Configure source ingress port interfaces. |
| **name**  string / required | Interface name. |
| **out_ports**  list / elements=dictionary | Configure source egress port interfaces. |
| **name**  string / required | Interface name. |
| **switch_id**  string / required | Managed-switch ID. Source switch-controller.managed-switch.switch-id. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_switch_controller_traffic_sniffer_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_switch_controller_traffic_sniffer_module.md#id5)

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
  - name: Configure FortiSwitch RSPAN/ERSPAN traffic sniffing parameters.
    fortios_switch_controller_traffic_sniffer:
      vdom:  "{{ vdom }}"
      switch_controller_traffic_sniffer:
        erspan_ip: "<your_own_value>"
        mode: "erspan-auto"
        target_ip:
         -
            description: "<your_own_value>"
            dst_entry_id: "2147483647"
            ip: "<your_own_value>"
            src_entry_id: "2147483647"
        target_mac:
         -
            description: "<your_own_value>"
            dst_entry_id: "2147483647"
            mac: "<your_own_value>"
            src_entry_id: "2147483647"
        target_port:
         -
            description: "<your_own_value>"
            in_ports:
             -
                name: "default_name_18"
            out_ports:
             -
                name: "default_name_20"
            switch_id: "<your_own_value> (source switch-controller.managed-switch.switch-id)"
```

## [Return Values](fortios_switch_controller_traffic_sniffer_module.md#id6)

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
