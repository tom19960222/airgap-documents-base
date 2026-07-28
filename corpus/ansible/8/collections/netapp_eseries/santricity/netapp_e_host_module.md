---
collection: ansible
version: "8"
title: "netapp_eseries.santricity.netapp_e_host module – NetApp E-Series manage eseries hosts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp_eseries/santricity/netapp_e_host_module.html
fetched_at: 2026-07-28T02:44:31+00:00
---
# netapp_eseries.santricity.netapp_e_host module – NetApp E-Series manage eseries hosts

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
> To use it in a playbook, specify: `netapp_eseries.santricity.netapp_e_host`.

New in netapp_eseries.santricity 2.2

- [Synopsis](netapp_e_host_module.md#synopsis)
- [Parameters](netapp_e_host_module.md#parameters)
- [Notes](netapp_e_host_module.md#notes)
- [Examples](netapp_e_host_module.md#examples)
- [Return Values](netapp_e_host_module.md#return-values)

## [Synopsis](netapp_e_host_module.md#id1)

- Create, update, remove hosts on NetApp E-series storage arrays

## [Parameters](netapp_e_host_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API. Example <https://prod-1.wahoo.acme.com/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **force_port**  boolean  *added in netapp_eseries.santricity 2.7* | Allow ports that are already assigned to be re-assigned to your current host  **Choices:**   - `false` - `true` |
| **group**  aliases: cluster  string | The unique identifier of the host-group you want the host to be a member of; this is used for clustering. |
| **host_type**  aliases: host_type_index  string | This is the type of host to be mapped  Required when `state=present`  Either one of the following names can be specified, Linux DM-MP, VMWare, Windows, Windows Clustered, or a host type index which can be found in **ERROR while parsing**: While parsing “M(netapp_e_facts)” at index 145: Module name “netapp_e_facts” is not a FQCN |
| **log_path**  string  *added in netapp_eseries.santricity 2.7* | A local path to a file to be used for debug logging |
| **name**  aliases: label  string / required | If the host doesn’t yet exist, the label/name to assign at creation time.  If the hosts already exists, this will be used to uniquely identify the host to make any required changes |
| **ports**  list / elements=string | A list of host ports you wish to associate with the host.  Host ports are uniquely identified by their WWN or IQN. Their assignments to a particular host are uniquely identified by a label and these must be unique. |
| **label**  string / required | A unique label to assign to this port assignment. |
| **port**  string / required | The WWN or IQN of the hostPort to assign to this port definition. |
| **type**  string / required | The interface type of the port to define.  Acceptable choices depend on the capabilities of the target hardware/software platform.  **Choices:**   - `"iscsi"` - `"sas"` - `"fc"` - `"ib"` - `"nvmeof"` - `"ethernet"` |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  **Default:** `"1"` |
| **state**  string  *added in netapp_eseries.santricity 2.7* | Set to absent to remove an existing host  Set to present to modify or create a new host definition  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **validate_certs**  boolean | Should https certificates be validated?  **Choices:**   - `false` - `true` ← (default) |

## [Notes](netapp_e_host_module.md#id3)

> **Note:**
>
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing “M(netapp_e_storage_system)” at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](netapp_e_host_module.md#id4)

```yaml+jinja
- name: Define or update an existing host named 'Host1'
  netapp_e_host:
    ssid: "1"
    api_url: "10.113.1.101:8443"
    api_username: admin
    api_password: myPassword
    name: "Host1"
    state: present
    host_type_index: Linux DM-MP
    ports:
      - type: 'iscsi'
        label: 'PORT_1'
        port: 'iqn.1996-04.de.suse:01:56f86f9bd1fe'
      - type: 'fc'
        label: 'FC_1'
        port: '10:00:FF:7C:FF:FF:FF:01'
      - type: 'fc'
        label: 'FC_2'
        port: '10:00:FF:7C:FF:FF:FF:00'

- name: Ensure a host named 'Host2' doesn't exist
  netapp_e_host:
    ssid: "1"
    api_url: "10.113.1.101:8443"
    api_username: admin
    api_password: myPassword
    name: "Host2"
    state: absent
```

## [Return Values](netapp_e_host_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_url**  string  *added in netapp_eseries.santricity 2.6* | the url of the API that this request was processed by  **Returned:** on success  **Sample:** `"https://webservices.example.com:8443"` |
| **id**  string  *added in netapp_eseries.santricity 2.6* | the unique identifier of the host on the E-Series storage-system  **Returned:** on success when state=present  **Sample:** `"00000000600A098000AAC0C3003004700AD86A52"` |
| **msg**  string | A user-readable description of the actions performed.  **Returned:** on success  **Sample:** `"The host has been created."` |
| **ssid**  string  *added in netapp_eseries.santricity 2.6* | the unique identifier of the E-Series storage-system with the current api  **Returned:** on success  **Sample:** `"1"` |

### Authors

- Kevin Hulquest (@hulquest)
- Nathan Swartz (@ndswartz)

### Collection links

- [Issue Tracker](https://github.com/netappeseries/santricity/issues)
- [Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
