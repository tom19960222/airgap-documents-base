---
collection: ansible
version: "6"
title: "cisco.ucs.ucs_vnic_template module – Configures vNIC templates on Cisco UCS Manager"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ucs/ucs_vnic_template_module.html
fetched_at: 2026-07-27T17:03:01+00:00
---
# cisco.ucs.ucs_vnic_template module – Configures vNIC templates on Cisco UCS Manager

> **Note:**
>
> This module is part of the [cisco.ucs collection](https://galaxy.ansible.com/cisco/ucs) (version 1.8.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ucs`.
> You need further requirements to be able to use this module,
> see [Requirements](ucs_vnic_template_module.md#ansible-collections-cisco-ucs-ucs-vnic-template-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_vnic_template`.

New in cisco.ucs 2.5

- [Synopsis](ucs_vnic_template_module.md#synopsis)
- [Requirements](ucs_vnic_template_module.md#requirements)
- [Parameters](ucs_vnic_template_module.md#parameters)
- [Examples](ucs_vnic_template_module.md#examples)

## [Synopsis](ucs_vnic_template_module.md#id1)

- Configures vNIC templates on Cisco UCS Manager.

## [Requirements](ucs_vnic_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_vnic_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cdn_name**  string | CDN Name used when cdn_source is set to user-defined. |
| **cdn_source**  string | CDN Source field.  This can be one of the following options:  vnic-name - Uses the vNIC template name of the vNIC instance as the CDN name. This is the default option.  user-defined - Uses a user-defined CDN name for the vNIC template. If this option is chosen, cdn_name must also be provided.  Choices:   - `"vnic-name"` ← (default) - `"user-defined"` |
| **description**  aliases: descr  string | A user-defined description of the vNIC template.  Enter up to 256 characters.  You can use any characters or spaces except the following:  ` (accent mark), (backslash), ^ (carat), ” (double quote), = (equal sign), > (greater than), < (less than), or ‘ (single quote). |
| **fabric**  string | The Fabric ID field specifying the fabric interconnect associated with vNICs created from this template.  If you want fabric failover enabled on vNICs created from this template, use of of the following:”  A-B to use Fabric A by default with failover enabled.  B-A to use Fabric B by default with failover enabled.  Do not enable vNIC fabric failover under the following circumstances:   - If the Cisco UCS domain is running in Ethernet switch mode. vNIC fabric failover is not supported in that mode. - If you plan to associate one or more vNICs created from this template to a server with an adapter that does not support fabric failover.   Choices:   - `"A"` ← (default) - `"B"` - `"A-B"` - `"B-A"` |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **mac_pool**  string | The MAC address pool that vNICs created from this vNIC template should use. |
| **mtu**  string | The MTU field.  The maximum transmission unit, or packet size, that vNICs created from this vNIC template should use.  Enter a string between ‘1500’ and ‘9000’.  If the vNIC template has an associated QoS policy, the MTU specified here must be equal to or less than the MTU specified in the QoS system class.  Default: `"1500"` |
| **name**  string / required | The name of the vNIC template.  This name can be between 1 and 16 alphanumeric characters.  You cannot use spaces or any special characters other than - (hyphen), “_” (underscore), : (colon), and . (period).  You cannot change this name after the template is created. |
| **network_control_policy**  string | The network control policy that vNICs created from this vNIC template should use. |
| **org_dn**  string | Org dn (distinguished name)  Default: `"org-root"` |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **peer_redundancy_template**  aliases: peer_redundancy_templ  string | The Peer Redundancy Template.  The name of the vNIC template sharing a configuration with this template.  If the redundancy_type is primary, the name of the secondary template should be provided.  If the redundancy_type is secondary, the name of the primary template should be provided.  Secondary templates can only configure non-shared properties (name, description, and mac_pool). |
| **pin_group**  string | The LAN pin group that vNICs created from this vNIC template should use. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **qos_policy**  string | The quality of service (QoS) policy that vNICs created from this vNIC template should use. |
| **redundancy_type**  string | The Redundancy Type used for vNIC redundancy pairs during fabric failover.  This can be one of the following:  primary — Creates configurations that can be shared with the Secondary template.  secondary — All shared configurations are inherited from the Primary template.  none - Legacy vNIC template behavior. Select this option if you do not want to use redundancy.  Choices:   - `"none"` ← (default) - `"primary"` - `"secondary"` |
| **state**  string | If `present`, will verify vNIC templates are present and will create if needed.  If `absent`, will verify vNIC templates are absent and will delete if needed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **stats_policy**  string | The statistics collection policy that vNICs created from this vNIC template should use.  Default: `"default"` |
| **target**  string | The possible target for vNICs created from this template.  The target determines whether or not Cisco UCS Manager automatically creates a VM-FEX port profile with the appropriate settings for the vNIC template.  This can be one of the following:  adapter — The vNICs apply to all adapters. No VM-FEX port profile is created if you choose this option.  vm - The vNICs apply to all virtual machines. A VM-FEX port profile is created if you choose this option.  Default: `"adapter"` |
| **template_type**  string | The Template Type field.  This can be one of the following:  initial-template — vNICs created from this template are not updated if the template changes.  updating-template - vNICs created from this template are updated if the template changes.  Choices:   - `"initial-template"` ← (default) - `"updating-template"` |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  Choices:   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  Choices:   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  Default: `"admin"` |
| **vlans_list**  string | List of VLANs used by the vNIC template.  Each list element has the following suboptions:  = name  The name of the VLAN (required).   - native  Designates the VLAN as a native VLAN. Only one VLAN in the list can be a native VLAN.  [choices: ‘no’, ‘yes’]  [Default: ‘no’] - state  If present, will verify VLAN is present on template.  If absent, will verify VLAN is absent on template.  choices: [present, absent]  default: present |

## [Examples](ucs_vnic_template_module.md#id4)

```yaml+jinja
- name: Configure vNIC template
  cisco.ucs.ucs_vnic_template:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: vNIC-A
    fabric: A
    vlans_list:
    - name: default
      native: 'yes'

- name: Configure vNIC template with failover
  cisco.ucs.ucs_vnic_template:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: vNIC-A-B
    fabric: A-B
    vlans_list:
    - name: default
      native: 'yes'
      state: present

- name: Remove vNIC template
  cisco.ucs.ucs_vnic_template:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: vNIC-A
    state: absent

- name: Remove another vNIC template
  cisco.ucs.ucs_vnic_template:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: vNIC-A-B
    state: absent

- name: Remove VLAN from template
  cisco.ucs.ucs_vnic_template:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: vNIC-A-B
    fabric: A-B
    vlans_list:
    - name: default
      native: 'yes'
      state: absent
```

### Authors

- David Soper (@dsoper2)
- John McDonough (@movinalot)
- CiscoUcs (@CiscoUcs)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
