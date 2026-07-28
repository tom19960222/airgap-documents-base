---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.netapp_e_facts module – NetApp E-Series retrieve facts about NetApp E-Series storage arrays"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/netapp_e_facts_module.html
fetched_at: 2026-07-28T00:14:15+00:00
---
# netapp_eseries.santricity.netapp_e_facts module – NetApp E-Series retrieve facts about NetApp E-Series storage arrays

> **Note:**
>
> This module is part of the [netapp_eseries.santricity collection](https://galaxy.ansible.com/netapp_eseries/santricity) (version 1.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp_eseries.santricity`.
>
> To use it in a playbook, specify: `netapp_eseries.santricity.netapp_e_facts`.

New in netapp_eseries.santricity 2.2

- [Synopsis](netapp_e_facts_module.md#synopsis)
- [Parameters](netapp_e_facts_module.md#parameters)
- [Notes](netapp_e_facts_module.md#notes)
- [Examples](netapp_e_facts_module.md#examples)
- [Return Values](netapp_e_facts_module.md#return-values)

## [Synopsis](netapp_e_facts_module.md#id1)

- The netapp_e_facts module returns a collection of facts regarding NetApp E-Series storage arrays.

## [Parameters](netapp_e_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API. Example <https://prod-1.wahoo.acme.com/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  Default: `"1"` |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Notes](netapp_e_facts_module.md#id3)

> **Note:**
>
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing M() at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](netapp_e_facts_module.md#id4)

```yaml+jinja
---
- name: Get array facts
  netapp_e_facts:
    ssid: "1"
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    validate_certs: true
```

## [Return Values](netapp_e_facts_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success message  Returned: on success  Sample: `"['Gathered facts for storage array. Array ID [1].', 'Gathered facts for web services proxy.']"` |
| **storage_array_facts**  complex | provides details about the array, controllers, management interfaces, hostside interfaces, driveside interfaces, disks, storage pools, volumes, snapshots, and features.  Returned: on successful inquiry from from embedded web services rest api |
| **netapp_controllers**  complex | storage array controller list that contains basic controller identification and status  Returned: success  Sample: `[[{"name": "A", "serial": "021632007299", "status": "optimal"}, {"name": "B", "serial": "021632007300", "status": "failed"}]]` |
| **netapp_disks**  complex | drive list that contains identification, type, and status information for each drive  Returned: success  Sample: `[[{"available": false, "firmware_version": "MS02", "id": "01000000500003960C8B67880000000000000000", "media_type": "ssd", "product_id": "PX02SMU080      ", "serial_number": "15R0A08LT2BA", "status": "optimal", "tray_ref": "0E00000000000000000000000000000000000000", "usable_bytes": "799629205504"}]]` |
| **netapp_driveside_interfaces**  complex | drive side interface list that contains identification, type, and speed for each interface  Returned: success  Sample: `[[{"controller": "A", "interface_speed": "12g", "interface_type": "sas"}], [{"controller": "B", "interface_speed": "10g", "interface_type": "iscsi"}]]` |
| **netapp_enabled_features**  complex | specifies the enabled features on the storage array.  Returned: on success  Sample: `[["flashReadCache", "performanceTier", "protectionInformation", "secureVolume"]]` |
| **netapp_host_groups**  complex | specifies the host groups on the storage arrays.  Returned: on success  Sample: `[[{"id": "85000000600A098000A4B28D003610705C40B964", "name": "group1"}]]` |
| **netapp_host_types**  complex | lists the available host types on the storage array.  Returned: on success  Sample: `[[{"index": 0, "type": "FactoryDefault"}, {"index": 1, "type": "W2KNETNCL"}, {"index": 2, "type": "SOL"}, {"index": 5, "type": "AVT_4M"}, {"index": 6, "type": "LNX"}, {"index": 7, "type": "LnxALUA"}, {"index": 8, "type": "W2KNETCL"}, {"index": 9, "type": "AIX MPIO"}, {"index": 10, "type": "VmwTPGSALUA"}, {"index": 15, "type": "HPXTPGS"}, {"index": 17, "type": "SolTPGSALUA"}, {"index": 18, "type": "SVC"}, {"index": 22, "type": "MacTPGSALUA"}, {"index": 23, "type": "WinTPGSALUA"}, {"index": 24, "type": "LnxTPGSALUA"}, {"index": 25, "type": "LnxTPGSALUA_PM"}, {"index": 26, "type": "ONTAP_ALUA"}, {"index": 27, "type": "LnxTPGSALUA_SF"}, {"index": 28, "type": "LnxDHALUA"}, {"index": 29, "type": "ATTOClusterAllOS"}]]` |
| **netapp_hosts**  complex | specifies the hosts on the storage arrays.  Returned: on success  Sample: `[[{"group_id": "85000000600A098000A4B28D003610705C40B964", "host_type_index": 28, "id": "8203800000000000000000000000000000000000", "name": "host1", "ports": [{"address": "1000FF7CFFFFFF01", "label": "FC_1", "type": "fc"}, {"address": "1000FF7CFFFFFF00", "label": "FC_2", "type": "fc"}]}]]` |
| **netapp_hostside_interfaces**  complex | host side interface list that contains identification, configuration, type, speed, and status information for each interface  Returned: success  Sample: `[[{"iscsi": [{"controller": "A", "current_interface_speed": "10g", "ipv4_address": "10.10.10.1", "ipv4_enabled": true, "ipv4_gateway": "10.10.10.1", "ipv4_subnet_mask": "255.255.255.0", "ipv6_enabled": false, "iqn": "iqn.1996-03.com.netapp:2806.600a098000a81b6d0000000059d60c76", "link_status": "up", "mtu": 9000, "supported_interface_speeds": ["10g"]}]}]]` |
| **netapp_management_interfaces**  complex | management interface list that contains identification, configuration, and status for each interface  Returned: success  Sample: `[[{"alias": "ict-2800-A", "channel": 1, "controller": "A", "dns_config_method": "dhcp", "dns_servers": [], "ipv4_address": "10.1.1.1", "ipv4_address_config_method": "static", "ipv4_enabled": true, "ipv4_gateway": "10.113.1.1", "ipv4_subnet_mask": "255.255.255.0", "ipv6_enabled": false, "link_status": "up", "mac_address": "00A098A81B5D", "name": "wan0", "ntp_config_method": "disabled", "ntp_servers": [], "remote_ssh_access": false}]]` |
| **netapp_storage_array**  dictionary | provides storage array identification, firmware version, and available capabilities  Returned: success  Sample: `[{"cacheBlockSizes": [4096, 8192, 16384, 32768], "chassis_serial": "021540006043", "firmware": "08.40.00.01", "name": "ict-2800-11_40", "supportedSegSizes": [8192, 16384, 32768, 65536, 131072, 262144, 524288], "wwn": "600A098000A81B5D0000000059D60C76"}]` |
| **netapp_storage_pools**  complex | storage pool list that contains identification and capacity information for each pool  Returned: success  Sample: `[[{"available_capacity": "3490353782784", "id": "04000000600A098000A81B5D000002B45A953A61", "name": "Raid6", "total_capacity": "5399466745856", "used_capacity": "1909112963072"}]]` |
| **netapp_volumes**  complex | storage volume list that contains identification and capacity information for each volume  Returned: success  Sample: `[[{"capacity": "5368709120", "id": "02000000600A098000AAC0C3000002C45A952BAA", "is_thin_provisioned": false, "name": "5G", "parent_storage_pool_id": "04000000600A098000A81B5D000002B45A953A61"}]]` |
| **netapp_volumes_by_initiators**  complex | list of available volumes keyed by the mapped initiators.  Returned: success  Sample: `[{"192_168_1_1": [{"id": "02000000600A098000A4B9D1000015FD5C8F7F9E", "meta_data": {"filetype": "xfs", "public": true}, "name": "some_volume", "workload_name": "test2_volumes", "wwn": "600A098000A4B9D1000015FD5C8F7F9E"}]}]` |
| **netapp_workload_tags**  complex | workload tag list  Returned: success  Sample: `[[{"id": "87e19568-43fb-4d8d-99ea-2811daaa2b38", "name": "ftp_server", "workloadAttributes": [{"key": "use", "value": "general"}]}]]` |
| **snapshot_images**  complex | snapshot image list that contains identification, capacity, and status information for each snapshot image  Returned: success  Sample: `[[{"active_cow": true, "creation_method": "user", "id": "34000000600A098000A81B5D00630A965B0535AC", "pit_capacity": "5368709120", "reposity_cap_utilization": "0", "rollback_source": false, "status": "optimal"}]]` |

### Authors

- Kevin Hulquest (@hulquest)
- Nathan Swartz (@ndswartz)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
