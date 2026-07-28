---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_system_gre_tunnel module – Configure GRE tunnel in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_system_gre_tunnel_module.html
fetched_at: 2026-07-27T17:44:37+00:00
---
# fortinet.fortios.fortios_system_gre_tunnel module – Configure GRE tunnel in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_gre_tunnel_module.md#ansible-collections-fortinet-fortios-fortios-system-gre-tunnel-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_gre_tunnel`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_gre_tunnel_module.md#synopsis)
- [Requirements](fortios_system_gre_tunnel_module.md#requirements)
- [Parameters](fortios_system_gre_tunnel_module.md#parameters)
- [Notes](fortios_system_gre_tunnel_module.md#notes)
- [Examples](fortios_system_gre_tunnel_module.md#examples)
- [Return Values](fortios_system_gre_tunnel_module.md#return-values)

## [Synopsis](fortios_system_gre_tunnel_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and gre_tunnel category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_gre_tunnel_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_system_gre_tunnel_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **system_gre_tunnel**  dictionary | Configure GRE tunnel. |
| **checksum_reception**  string | Enable/disable validating checksums in received GRE packets.  Choices:   - `"disable"` - `"enable"` |
| **checksum_transmission**  string | Enable/disable including checksums in transmitted GRE packets.  Choices:   - `"disable"` - `"enable"` |
| **diffservcode**  string | DiffServ setting to be applied to GRE tunnel outer IP header. |
| **dscp_copying**  string | Enable/disable DSCP copying.  Choices:   - `"disable"` - `"enable"` |
| **interface**  string | Interface name. Source system.interface.name. |
| **ip_version**  string | IP version to use for VPN interface.  Choices:   - `"4"` - `"6"` |
| **keepalive_failtimes**  integer | Number of consecutive unreturned keepalive messages before a GRE connection is considered down (1 - 255). |
| **keepalive_interval**  integer | Keepalive message interval (0 - 32767, 0 = disabled). |
| **key_inbound**  integer | Require received GRE packets contain this key (0 - 4294967295). |
| **key_outbound**  integer | Include this key in transmitted GRE packets (0 - 4294967295). |
| **local_gw**  string | IP address of the local gateway. |
| **local_gw6**  string | IPv6 address of the local gateway. |
| **name**  string / required | Tunnel name. |
| **remote_gw**  string | IP address of the remote gateway. |
| **remote_gw6**  string | IPv6 address of the remote gateway. |
| **sequence_number_reception**  string | Enable/disable validating sequence numbers in received GRE packets.  Choices:   - `"disable"` - `"enable"` |
| **sequence_number_transmission**  string | Enable/disable including of sequence numbers in transmitted GRE packets.  Choices:   - `"disable"` - `"enable"` |
| **use_sdwan**  string | Enable/disable use of SD-WAN to reach remote gateway.  Choices:   - `"disable"` - `"enable"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_system_gre_tunnel_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_gre_tunnel_module.md#id5)

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
  - name: Configure GRE tunnel.
    fortios_system_gre_tunnel:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_gre_tunnel:
        checksum_reception: "disable"
        checksum_transmission: "disable"
        diffservcode: "<your_own_value>"
        dscp_copying: "disable"
        interface: "<your_own_value> (source system.interface.name)"
        ip_version: "4"
        keepalive_failtimes: "10"
        keepalive_interval: "0"
        key_inbound: "0"
        key_outbound: "0"
        local_gw: "<your_own_value>"
        local_gw6: "<your_own_value>"
        name: "default_name_15"
        remote_gw: "<your_own_value>"
        remote_gw6: "<your_own_value>"
        sequence_number_reception: "disable"
        sequence_number_transmission: "disable"
        use_sdwan: "disable"
```

## [Return Values](fortios_system_gre_tunnel_module.md#id6)

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
