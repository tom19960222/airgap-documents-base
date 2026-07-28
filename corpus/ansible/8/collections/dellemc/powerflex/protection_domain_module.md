---
collection: ansible
version: "8"
title: "dellemc.powerflex.protection_domain module – Manage Protection Domain on Dell PowerFlex"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/powerflex/protection_domain_module.html
fetched_at: 2026-07-28T02:05:11+00:00
---
# dellemc.powerflex.protection_domain module – Manage Protection Domain on Dell PowerFlex

> **Note:**
>
> This module is part of the [dellemc.powerflex collection](https://galaxy.ansible.com/ui/repo/published/dellemc/powerflex/) (version 1.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.powerflex`.
> You need further requirements to be able to use this module,
> see [Requirements](protection_domain_module.md#ansible-collections-dellemc-powerflex-protection-domain-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.powerflex.protection_domain`.

New in dellemc.powerflex 1.2.0

- [Synopsis](protection_domain_module.md#synopsis)
- [Requirements](protection_domain_module.md#requirements)
- [Parameters](protection_domain_module.md#parameters)
- [Notes](protection_domain_module.md#notes)
- [Examples](protection_domain_module.md#examples)
- [Return Values](protection_domain_module.md#return-values)

## [Synopsis](protection_domain_module.md#id1)

- Managing Protection Domain on PowerFlex storage system includes creating, modifying attributes, deleting and getting details of Protection Domain.

## [Requirements](protection_domain_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.5 or later.
- Ansible-core 2.13 or later.
- PyPowerFlex 1.8.0.
- Python 3.9, 3.10 or 3.11.

## [Parameters](protection_domain_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostname**  aliases: gateway_host  string / required | IP or FQDN of the PowerFlex host. |
| **is_active**  boolean | Used to activate or deactivate the protection domain.  **Choices:**   - `false` - `true` |
| **network_limits**  dictionary | Network bandwidth limit used by all SDS in protection domain. |
| **bandwidth_unit**  string | Unit for network bandwidth limits.  **Choices:**   - `"KBps"` ← (default) - `"MBps"` - `"GBps"` |
| **overall_limit**  integer | Limit the overall network bandwidth. |
| **rebalance_limit**  integer | Limit the network bandwidth for rebalance. |
| **rebuild_limit**  integer | Limit the network bandwidth for rebuild. |
| **vtree_migration_limit**  integer | Limit the network bandwidth for vtree migration. |
| **password**  string / required | The password of the PowerFlex host. |
| **port**  integer | Port number through which communication happens with PowerFlex host.  **Default:** `443` |
| **protection_domain_id**  string | The ID of the protection domain.  Except for create operation, all other operations can be performed using protection_domain_id.  Mutually exclusive with *protection_domain_name*. |
| **protection_domain_name**  string | The name of the protection domain.  Mandatory for create operation.  It is unique across the PowerFlex array.  Mutually exclusive with *protection_domain_id*. |
| **protection_domain_new_name**  string | Used to rename the protection domain. |
| **rf_cache_limits**  dictionary | Used to set the RFcache parameters of the protection domain. |
| **is_enabled**  boolean | Used to enable or disable RFcache in the protection domain.  **Choices:**   - `false` - `true` |
| **max_io_limit**  integer | Used to set cache maximum I/O limit in KB. |
| **page_size**  integer | Used to set the cache page size in KB. |
| **pass_through_mode**  string | Used to set the cache mode.  **Choices:**   - `"None"` - `"Read"` - `"Write"` - `"ReadAndWrite"` - `"WriteMiss"` |
| **state**  string / required | State of the protection domain.  **Choices:**   - `"present"` - `"absent"` |
| **timeout**  integer | Time after which connection will get terminated.  It is to be mentioned in seconds.  **Default:** `120` |
| **username**  string / required | The username of the PowerFlex host. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](protection_domain_module.md#id4)

> **Note:**
>
> - The protection domain can only be deleted if all its related objects have been dissociated from the protection domain.
> - If the protection domain set to inactive, then no operation can be performed on protection domain.
> - The *check_mode* is not supported.
> - The modules present in the collection named as ‘dellemc.powerflex’ are built to support the Dell PowerFlex storage platform.

## [Examples](protection_domain_module.md#id5)

```yaml+jinja
- name: Create protection domain
  dellemc.powerflex.protection_domain:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    protection_domain_name: "domain1"
    state: "present"

- name: Create protection domain with all parameters
  dellemc.powerflex.protection_domain:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    protection_domain_name: "domain1"
    is_active: true
    network_limits:
      rebuild_limit: 10
      rebalance_limit: 17
      vtree_migration_limit: 14
      overall_limit: 20
      bandwidth_unit: "MBps"
    rf_cache_limits:
      is_enabled: true
      page_size: 16
      max_io_limit: 128
      pass_through_mode: "Read"
    state: "present"

- name: Get protection domain details using name
  dellemc.powerflex.protection_domain:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    protection_domain_name: "domain1"
    state: "present"

- name: Get protection domain details using ID
  dellemc.powerflex.protection_domain:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    protection_domain_id: "5718253c00000004"
    state: "present"

- name: Modify protection domain attributes
  dellemc.powerflex.protection_domain:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    protection_domain_name: "domain1"
    protection_domain_new_name: "domain1_new"
    network_limits:
      rebuild_limit: 14
      rebalance_limit: 20
      overall_limit: 25
      bandwidth_unit: "MBps"
    rf_cache_limits:
      page_size: 64
      pass_through_mode: "WriteMiss"
    state: "present"

- name: Delete protection domain using name
  dellemc.powerflex.protection_domain:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    protection_domain_name: "domain1_new"
    state: "absent"
```

## [Return Values](protection_domain_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `false` |
| **protection_domain_details**  dictionary | Details of the protection domain.  **Returned:** When protection domain exists  **Sample:** `{"fglDefaultMetadataCacheSize": 0, "fglDefaultNumConcurrentWrites": 1000, "fglMetadataCacheEnabled": false, "id": "7bd6457000000000", "links": [{"href": "/api/instances/ProtectionDomain::7bd6457000000000", "rel": "self"}, {"href": "/api/instances/ProtectionDomain::7bd6457000000000/ relationships/Statistics", "rel": "/api/ProtectionDomain/relationship/Statistics"}, {"href": "/api/instances/ProtectionDomain::7bd6457000000000/ relationships/Sdr", "rel": "/api/ProtectionDomain/relationship/Sdr"}, {"href": "/api/instances/ProtectionDomain::7bd6457000000000/ relationships/AccelerationPool", "rel": "/api/ProtectionDomain/relationship/AccelerationPool"}, {"href": "/api/instances/ProtectionDomain::7bd6457000000000/ relationships/StoragePool", "rel": "/api/ProtectionDomain/relationship/StoragePool"}, {"href": "/api/instances/ProtectionDomain::7bd6457000000000/ relationships/Sds", "rel": "/api/ProtectionDomain/relationship/Sds"}, {"href": "/api/instances/ProtectionDomain::7bd6457000000000/ relationships/ReplicationConsistencyGroup", "rel": "/api/ProtectionDomain/relationship/ ReplicationConsistencyGroup"}, {"href": "/api/instances/ProtectionDomain::7bd6457000000000/ relationships/FaultSet", "rel": "/api/ProtectionDomain/relationship/FaultSet"}, {"href": "/api/instances/System::0989ce79058f150f", "rel": "/api/parent/relationship/systemId"}], "mdmSdsNetworkDisconnectionsCounterParameters": {"longWindow": {"threshold": 700, "windowSizeInSec": 86400}, "mediumWindow": {"threshold": 500, "windowSizeInSec": 3600}, "shortWindow": {"threshold": 300, "windowSizeInSec": 60}}, "name": "domain1", "overallIoNetworkThrottlingEnabled": false, "overallIoNetworkThrottlingInKbps": null, "protectedMaintenanceModeNetworkThrottlingEnabled": false, "protectedMaintenanceModeNetworkThrottlingInKbps": null, "protectionDomainState": "Active", "rebalanceNetworkThrottlingEnabled": false, "rebalanceNetworkThrottlingInKbps": null, "rebuildNetworkThrottlingEnabled": false, "rebuildNetworkThrottlingInKbps": null, "rfcacheAccpId": null, "rfcacheEnabled": true, "rfcacheMaxIoSizeKb": 128, "rfcacheOpertionalMode": "WriteMiss", "rfcachePageSizeKb": 64, "sdrSdsConnectivityInfo": {"clientServerConnStatus": "CLIENT_SERVER_CONN_STATUS_ALL _CONNECTED", "disconnectedClientId": null, "disconnectedClientName": null, "disconnectedServerId": null, "disconnectedServerIp": null, "disconnectedServerName": null}, "sdsConfigurationFailureCounterParameters": {"longWindow": {"threshold": 700, "windowSizeInSec": 86400}, "mediumWindow": {"threshold": 500, "windowSizeInSec": 3600}, "shortWindow": {"threshold": 300, "windowSizeInSec": 60}}, "sdsDecoupledCounterParameters": {"longWindow": {"threshold": 700, "windowSizeInSec": 86400}, "mediumWindow": {"threshold": 500, "windowSizeInSec": 3600}, "shortWindow": {"threshold": 300, "windowSizeInSec": 60}}, "sdsReceiveBufferAllocationFailuresCounterParameters": {"longWindow": {"threshold": 2000000, "windowSizeInSec": 86400}, "mediumWindow": {"threshold": 200000, "windowSizeInSec": 3600}, "shortWindow": {"threshold": 20000, "windowSizeInSec": 60}}, "sdsSdsNetworkDisconnectionsCounterParameters": {"longWindow": {"threshold": 700, "windowSizeInSec": 86400}, "mediumWindow": {"threshold": 500, "windowSizeInSec": 3600}, "shortWindow": {"threshold": 300, "windowSizeInSec": 60}}, "storagePool": [{"id": "8d1cba1700000000", "name": "pool1"}], "systemId": "0989ce79058f150f", "vtreeMigrationNetworkThrottlingEnabled": false, "vtreeMigrationNetworkThrottlingInKbps": null}` |
| **fglDefaultMetadataCacheSize**  integer | FGL metadata cache size.  **Returned:** success |
| **fglDefaultNumConcurrentWrites**  string | FGL concurrent writes.  **Returned:** success |
| **fglMetadataCacheEnabled**  boolean | Whether FGL cache enabled.  **Returned:** success |
| **id**  string | Protection domain ID.  **Returned:** success |
| **links**  list / elements=string | Protection domain links.  **Returned:** success |
| **href**  string | Protection domain instance URL.  **Returned:** success |
| **rel**  string | Protection domain’s relationship with different entities.  **Returned:** success |
| **mdmSdsNetworkDisconnectionsCounterParameters**  dictionary | MDM’s SDS counter parameter.  **Returned:** success |
| **longWindow**  integer | Long window for Counter Parameters.  **Returned:** success |
| **mediumWindow**  integer | Medium window for Counter Parameters.  **Returned:** success |
| **shortWindow**  integer | Short window for Counter Parameters.  **Returned:** success |
| **name**  string | Name of the protection domain.  **Returned:** success |
| **overallIoNetworkThrottlingEnabled**  boolean | Whether overall network throttling enabled.  **Returned:** success |
| **overallIoNetworkThrottlingInKbps**  integer | Overall network throttling in KBps.  **Returned:** success |
| **protectedMaintenanceModeNetworkThrottlingEnabled**  boolean | Whether protected maintenance mode network throttling enabled.  **Returned:** success |
| **protectedMaintenanceModeNetworkThrottlingInKbps**  integer | Protected maintenance mode network throttling in KBps.  **Returned:** success |
| **protectionDomainState**  integer | State of protection domain.  **Returned:** success |
| **rebalanceNetworkThrottlingEnabled**  integer | Whether rebalance network throttling enabled.  **Returned:** success |
| **rebalanceNetworkThrottlingInKbps**  integer | Rebalance network throttling in KBps.  **Returned:** success |
| **rebuildNetworkThrottlingEnabled**  integer | Whether rebuild network throttling enabled.  **Returned:** success |
| **rebuildNetworkThrottlingInKbps**  integer | Rebuild network throttling in KBps.  **Returned:** success |
| **rfcacheAccpId**  string | Id of RF cache acceleration pool.  **Returned:** success |
| **rfcacheEnabled**  boolean | Whether RF cache is enabled or not.  **Returned:** success |
| **rfcacheMaxIoSizeKb**  integer | RF cache maximum I/O size in KB.  **Returned:** success |
| **rfcacheOpertionalMode**  string | RF cache operational mode.  **Returned:** success |
| **rfcachePageSizeKb**  boolean | RF cache page size in KB.  **Returned:** success |
| **sdrSdsConnectivityInfo**  dictionary | Connectivity info of SDR and SDS.  **Returned:** success |
| **clientServerConnStatus**  string | Connectivity status of client and server.  **Returned:** success |
| **disconnectedClientId**  string | Disconnected client ID.  **Returned:** success |
| **disconnectedClientName**  string | Disconnected client name.  **Returned:** success |
| **disconnectedServerId**  string | Disconnected server ID.  **Returned:** success |
| **disconnectedServerIp**  string | Disconnected server IP.  **Returned:** success |
| **disconnectedServerName**  string | Disconnected server name.  **Returned:** success |
| **sdsSdsNetworkDisconnectionsCounterParameters**  dictionary | Counter parameter for SDS-SDS network.  **Returned:** success |
| **longWindow**  integer | Long window for Counter Parameters.  **Returned:** success |
| **mediumWindow**  integer | Medium window for Counter Parameters.  **Returned:** success |
| **shortWindow**  integer | Short window for Counter Parameters.  **Returned:** success |
| **storagePool**  list / elements=string | List of storage pools.  **Returned:** success |
| **systemId**  string | ID of system.  **Returned:** success |
| **vtreeMigrationNetworkThrottlingEnabled**  boolean | Whether V-Tree migration network throttling enabled.  **Returned:** success |
| **vtreeMigrationNetworkThrottlingInKbps**  integer | V-Tree migration network throttling in KBps.  **Returned:** success |

### Authors

- Bhavneet Sharma (@sharmb5)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-powerflex/tree/1.9.0)
