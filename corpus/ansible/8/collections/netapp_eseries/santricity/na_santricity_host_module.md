---
collection: ansible
version: "8"
title: "netapp_eseries.santricity.na_santricity_host module – NetApp E-Series manage eseries hosts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp_eseries/santricity/na_santricity_host_module.html
fetched_at: 2026-07-28T02:44:10+00:00
---
# netapp_eseries.santricity.na_santricity_host module – NetApp E-Series manage eseries hosts

> **Note:**
>
> This module is part of the [netapp_eseries.santricity collection](https://galaxy.ansible.com/ui/repo/published/netapp_eseries/santricity/) (version 1.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp_eseries.santricity`.
>
> To use it in a playbook, specify: `netapp_eseries.santricity.na_santricity_host`.

- [Synopsis](na_santricity_host_module.md#synopsis)
- [Parameters](na_santricity_host_module.md#parameters)
- [Notes](na_santricity_host_module.md#notes)
- [Examples](na_santricity_host_module.md#examples)
- [Return Values](na_santricity_host_module.md#return-values)

## [Synopsis](na_santricity_host_module.md#id1)

- Create, update, remove hosts on NetApp E-series storage arrays

## [Parameters](na_santricity_host_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API.  Example <https://prod-1.wahoo.acme.com:8443/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **force_port**  boolean | Allow ports that are already assigned to be re-assigned to your current host  **Choices:**   - `false` - `true` |
| **host_type**  aliases: host_type_index  string | Host type includes operating system and multipath considerations.  If not specified, the default host type will be utilized. Default host type can be set using [netapp_eseries.santricity.na_santricity_global](na_santricity_global_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-global-module).  For storage array specific options see [netapp_eseries.santricity.na_santricity_facts](na_santricity_facts_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-facts-module).  All values are case-insensitive.  AIX MPIO - The Advanced Interactive Executive (AIX) OS and the native MPIO driver  AVT 4M - Silicon Graphics, Inc. (SGI) proprietary multipath driver  HP-UX - The HP-UX OS with native multipath driver  Linux ATTO - The Linux OS and the ATTO Technology, Inc. driver (must use ATTO FC HBAs)  Linux DM-MP - The Linux OS and the native DM-MP driver  Linux Pathmanager - The Linux OS and the SGI proprietary multipath driver  Mac - The Mac OS and the ATTO Technology, Inc. driver  ONTAP - FlexArray  Solaris 11 or later - The Solaris 11 or later OS and the native MPxIO driver  Solaris 10 or earlier - The Solaris 10 or earlier OS and the native MPxIO driver  SVC - IBM SAN Volume Controller  VMware - ESXi OS  Windows - Windows Server OS and Windows MPIO with a DSM driver  Windows Clustered - Clustered Windows Server OS and Windows MPIO with a DSM driver  Windows ATTO - Windows OS and the ATTO Technology, Inc. driver |
| **name**  aliases: label  string / required | If the host doesn’t yet exist, the label/name to assign at creation time.  If the hosts already exists, this will be used to uniquely identify the host to make any required changes |
| **ports**  list / elements=string | A list of host ports you wish to associate with the host.  Host ports are uniquely identified by their WWN or IQN. Their assignments to a particular host are uniquely identified by a label and these must be unique. |
| **label**  string / required | A unique label to assign to this port assignment. |
| **port**  string / required | The WWN or IQN of the hostPort to assign to this port definition. |
| **type**  string / required | The interface type of the port to define.  Acceptable choices depend on the capabilities of the target hardware/software platform.  **Choices:**   - `"iscsi"` - `"sas"` - `"fc"` - `"ib"` - `"nvmeof"` |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  **Default:** `"1"` |
| **state**  string | Set to absent to remove an existing host  Set to present to modify or create a new host definition  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **validate_certs**  boolean | Should https certificates be validated?  **Choices:**   - `false` - `true` ← (default) |

## [Notes](na_santricity_host_module.md#id3)

> **Note:**
>
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing “M(netapp_e_storage_system)” at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](na_santricity_host_module.md#id4)

```yaml+jinja
- name: Define or update an existing host named "Host1"
  na_santricity_host:
    ssid: "1"
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    validate_certs: true
    name: "Host1"
    state: present
    host_type_index: Linux DM-MP
    ports:
      - type: "iscsi"
        label: "PORT_1"
        port: "iqn.1996-04.de.suse:01:56f86f9bd1fe"
      - type: "fc"
        label: "FC_1"
        port: "10:00:FF:7C:FF:FF:FF:01"
      - type: "fc"
        label: "FC_2"
        port: "10:00:FF:7C:FF:FF:FF:00"

- name: Ensure a host named "Host2" doesn"t exist
  na_santricity_host:
    ssid: "1"
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    validate_certs: true
    name: "Host2"
    state: absent
```

## [Return Values](na_santricity_host_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_url**  string | the url of the API that this request was proccessed by  **Returned:** on success  **Sample:** `"https://webservices.example.com:8443"` |
| **id**  string | the unique identifier of the host on the E-Series storage-system  **Returned:** on success when state=present  **Sample:** `"00000000600A098000AAC0C3003004700AD86A52"` |
| **msg**  string | A user-readable description of the actions performed.  **Returned:** on success  **Sample:** `"The host has been created."` |
| **ssid**  string | the unique identifer of the E-Series storage-system with the current api  **Returned:** on success  **Sample:** `"1"` |

### Authors

- Kevin Hulquest (@hulquest)
- Nathan Swartz (@ndswartz)

### Collection links

- [Issue Tracker](https://github.com/netappeseries/santricity/issues)
- [Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
