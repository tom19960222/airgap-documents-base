---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_vpn_ipsec_concentrator module – Concentrator configuration in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_vpn_ipsec_concentrator_module.html
fetched_at: 2026-07-28T02:30:16+00:00
---
# fortinet.fortios.fortios_vpn_ipsec_concentrator module – Concentrator configuration in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_vpn_ipsec_concentrator_module.md#ansible-collections-fortinet-fortios-fortios-vpn-ipsec-concentrator-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_vpn_ipsec_concentrator`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_vpn_ipsec_concentrator_module.md#synopsis)
- [Requirements](fortios_vpn_ipsec_concentrator_module.md#requirements)
- [Parameters](fortios_vpn_ipsec_concentrator_module.md#parameters)
- [Notes](fortios_vpn_ipsec_concentrator_module.md#notes)
- [Examples](fortios_vpn_ipsec_concentrator_module.md#examples)
- [Return Values](fortios_vpn_ipsec_concentrator_module.md#return-values)

## [Synopsis](fortios_vpn_ipsec_concentrator_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify vpn_ipsec feature and concentrator category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_vpn_ipsec_concentrator_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_vpn_ipsec_concentrator_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |
| **vpn_ipsec_concentrator**  dictionary | Concentrator configuration. |
| **id**  integer / required | Concentrator ID (1 - 65535). see <a href=’#notes’>Notes</a>. |
| **member**  list / elements=dictionary | Names of up to 3 VPN tunnels to add to the concentrator. |
| **name**  string / required | Member name. Source vpn.ipsec.manualkey.name vpn.ipsec.phase1.name. |
| **name**  string | Concentrator name. |
| **src_check**  string | Enable to check source address of phase 2 selector. Disable to check only the destination selector.  **Choices:**   - `"disable"` - `"enable"` |

## [Notes](fortios_vpn_ipsec_concentrator_module.md#id4)

> **Note:**
>
> - We highly recommend using your own value as the id instead of 0, while ‘0’ is a special placeholder that allows the backend to assign the latest available number for the object, it does have limitations. Please find more details in Q&A.
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_vpn_ipsec_concentrator_module.md#id5)

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
  - name: Concentrator configuration.
    fortios_vpn_ipsec_concentrator:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      vpn_ipsec_concentrator:
        id:  "3"
        member:
         -
            name: "default_name_5 (source vpn.ipsec.manualkey.name vpn.ipsec.phase1.name)"
        name: "default_name_6"
        src_check: "disable"
```

## [Return Values](fortios_vpn_ipsec_concentrator_module.md#id6)

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
