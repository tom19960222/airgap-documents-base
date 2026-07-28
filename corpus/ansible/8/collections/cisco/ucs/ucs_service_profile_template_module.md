---
collection: ansible
version: "8"
title: "cisco.ucs.ucs_service_profile_template module – Configures Service Profile Templates on Cisco UCS Manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ucs/ucs_service_profile_template_module.html
fetched_at: 2026-07-28T01:39:42+00:00
---
# cisco.ucs.ucs_service_profile_template module – Configures Service Profile Templates on Cisco UCS Manager

> **Note:**
>
> This module is part of the [cisco.ucs collection](https://galaxy.ansible.com/ui/repo/published/cisco/ucs/) (version 1.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ucs`.
> You need further requirements to be able to use this module,
> see [Requirements](ucs_service_profile_template_module.md#ansible-collections-cisco-ucs-ucs-service-profile-template-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_service_profile_template`.

New in cisco.ucs 2.8

- [Synopsis](ucs_service_profile_template_module.md#synopsis)
- [Requirements](ucs_service_profile_template_module.md#requirements)
- [Parameters](ucs_service_profile_template_module.md#parameters)
- [Examples](ucs_service_profile_template_module.md#examples)

## [Synopsis](ucs_service_profile_template_module.md#id1)

- Configures Service Profile Templates on Cisco UCS Manager.

## [Requirements](ucs_service_profile_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_service_profile_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **bios_policy**  string | The name of the BIOS policy you want to associate with service profiles created from this template. |
| **boot_policy**  string | The name of the boot order policy you want to associate with service profiles created from this template.  **Default:** `"default"` |
| **description**  aliases: descr  string | A user-defined description of the service profile template.  Enter up to 256 characters.  You can use any characters or spaces except the following:  ` (accent mark), (backslash), ^ (carat), ” (double quote), = (equal sign), > (greater than), < (less than), or ‘ (single quote). |
| **graphics_card_policy**  string | The name of the graphics card policy you want to associate with service profiles created from this template. |
| **host_firmware_package**  string | The name of the host firmware package you want to associate with service profiles created from this template. |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **ipmi_access_profile**  string | The name of the IPMI access profile you want to associate with service profiles created from this template. |
| **iqn_pool**  string | The name of the IQN pool (initiator) you want to apply to all iSCSI vNICs for service profiles created from this template. |
| **kvm_mgmt_policy**  string | The name of the KVM management policy you want to associate with service profiles created from this template. |
| **lan_connectivity_policy**  string | The name of the LAN connectivity policy you want to associate with service profiles created from this template. |
| **local_disk_policy**  string | The name of the local disk policy you want to associate with service profiles created from this template. |
| **maintenance_policy**  string | The name of the maintenance policy you want to associate with service profiles created from this template. |
| **mgmt_inband_pool_name**  string | How the inband management IPv4 address is derived for the server associated with this service profile. |
| **mgmt_interface_mode**  string | The Management Interface you want to assign to service profiles created from this template.  **Choices:**   - `""` - `"in-band"` |
| **mgmt_ip_pool**  string | The name of the Outband Management IP pool you want to use with service profiles created from this template.  **Default:** `"ext-mgmt"` |
| **mgmt_ip_state**  string | The state for the Outband Management IP pool you want to use with service profiles created from this template.  **Choices:**   - `"none"` - `"pooled"` ← (default) |
| **mgmt_vnet_name**  string | A VLAN selected from the associated VLAN group. |
| **name**  string / required | The name of the service profile template.  This name can be between 2 and 32 alphanumeric characters.  You cannot use spaces or any special characters other than - (hyphen), “_” (underscore), : (colon), and . (period).  This name must be unique across all service profiles and service profile templates within the same organization. |
| **org_dn**  string | Org dn (distinguished name)  **Default:** `"org-root"` |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **power_control_policy**  string | The name of the power control policy you want to associate with service profiles created from this template.  **Default:** `"default"` |
| **power_state**  string | The power state to be applied when a service profile created from this template is associated with a server.  **Choices:**   - `"up"` ← (default) - `"down"` |
| **power_sync_policy**  string | The name of the power sync policy you want to associate with service profiles created from this template. |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **san_connectivity_policy**  string | The name of the SAN connectivity policy you want to associate with service profiles created from this template. |
| **scrub_policy**  string | The name of the scrub policy you want to associate with service profiles created from this template. |
| **server_pool**  string | The name of the server pool you want to associate with this service profile template. |
| **server_pool_qualification**  string | The name of the server pool policy qualificaiton you want to use for this service profile template. |
| **sol_policy**  string | The name of the Serial over LAN (SoL) policy you want to associate with service profiles created from this template. |
| **state**  string | If `present`, will verify Service Profile Templates are present and will create if needed.  If `absent`, will verify Service Profile Templates are absent and will delete if needed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **storage_profile**  string | The name of the storage profile you want to associate with service profiles created from this template |
| **template_type**  string | The template type field which can be one of the following:  initial-template — Any service profiles created from this template are not updated if the template changes.  updating-template — Any service profiles created from this template are updated if the template changes.  **Choices:**   - `"initial-template"` ← (default) - `"updating-template"` |
| **threshold_policy**  string | The name of the threshold policy you want to associate with service profiles created from this template.  **Default:** `"default"` |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  **Choices:**   - `false` - `true` ← (default) |
| **user_label**  string | The User Label you want to assign to service profiles created from this template. |
| **username**  string | Username for Cisco UCS Manager authentication.  **Default:** `"admin"` |
| **uuid_pool**  string | Specifies how the UUID will be set on a server associated with a service profile created from this template.  The uuid_pool option can be the name of the UUID pool to use or ‘’ (the empty string).  An empty string will use the UUID assigned to the server by the manufacturer, and the  UUID remains unassigned until a service profile created from this template is associated with a server. At that point,  the UUID is set to the UUID value assigned to the server by the manufacturer. If the service profile is later moved to  a different server, the UUID is changed to match the new server.”  **Default:** `"default"` |
| **vmedia_policy**  string | The name of the vMedia policy you want to associate with service profiles created from this template. |

## [Examples](ucs_service_profile_template_module.md#id4)

```yaml+jinja
- name: Configure Service Profile Template with LAN/SAN Connectivity and all other options defaulted
  cisco.ucs.ucs_service_profile_template:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: DEE-Ctrl
    template_type: updating-template
    uuid_pool: UUID-Pool
    storage_profile: DEE-StgProf
    lan_connectivity_policy: Cntr-FC-Boot
    iqn_pool: iSCSI-Boot-A
    san_connectivity_policy: Cntr-FC-Boot
    boot_policy: DEE-vMedia
    maintenance_policy: default
    server_pool: Container-Pool
    host_firmware_package: 3.1.2b
    bios_policy: Docker

- name: Remove Service Profile Template
  cisco.ucs.ucs_service_profile_template:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: DEE-Ctrl
    state: absent
```

### Authors

- David Soper (@dsoper2)
- CiscoUcs (@CiscoUcs)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
