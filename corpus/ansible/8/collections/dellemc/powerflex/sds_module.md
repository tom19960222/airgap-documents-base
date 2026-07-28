---
collection: ansible
version: "8"
title: "dellemc.powerflex.sds module – Manage SDS on Dell PowerFlex"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/powerflex/sds_module.html
fetched_at: 2026-07-28T02:05:14+00:00
---
# dellemc.powerflex.sds module – Manage SDS on Dell PowerFlex

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
> see [Requirements](sds_module.md#ansible-collections-dellemc-powerflex-sds-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.powerflex.sds`.

New in dellemc.powerflex 1.1.0

- [Synopsis](sds_module.md#synopsis)
- [Requirements](sds_module.md#requirements)
- [Parameters](sds_module.md#parameters)
- [Notes](sds_module.md#notes)
- [Examples](sds_module.md#examples)
- [Return Values](sds_module.md#return-values)

## [Synopsis](sds_module.md#id1)

- Managing SDS on PowerFlex storage system includes creating new SDS, getting details of SDS, adding/removing IP to/from SDS, modifying attributes of SDS, and deleting SDS.

Aliases: dellemc_powerflex_sds

## [Requirements](sds_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.5 or later.
- Ansible-core 2.13 or later.
- PyPowerFlex 1.8.0.
- Python 3.9, 3.10 or 3.11.

## [Parameters](sds_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostname**  aliases: gateway_host  string / required | IP or FQDN of the PowerFlex host. |
| **password**  string / required | The password of the PowerFlex host. |
| **performance_profile**  string | Performance profile to apply to the SDS.  The HighPerformance profile configures a predefined set of parameters for very high performance use cases.  Default value by API is `HighPerformance`.  **Choices:**   - `"Compact"` - `"HighPerformance"` |
| **port**  integer | Port number through which communication happens with PowerFlex host.  **Default:** `443` |
| **protection_domain_id**  string | The ID of the protection domain.  Mutually exclusive with *protection_domain_name*. |
| **protection_domain_name**  string | The name of the protection domain.  Mutually exclusive with *protection_domain_id*. |
| **rfcache_enabled**  boolean | Whether to enable the Read Flash cache.  **Choices:**   - `false` - `true` |
| **rmcache_enabled**  boolean | Whether to enable the Read RAM cache.  **Choices:**   - `false` - `true` |
| **rmcache_size**  integer | Read RAM cache size (in MB).  Minimum size is 128 MB.  Maximum size is 3911 MB. |
| **sds_id**  string | The ID of the SDS.  Except create operation, all other operations can be performed using *sds_id*.  Mutually exclusive with *sds_name*. |
| **sds_ip_list**  list / elements=dictionary | Dictionary of IPs and their roles for the SDS.  At least one IP-role is mandatory while creating a SDS.  IP-roles can be updated as well. |
| **ip**  string / required | IP address of the SDS. |
| **role**  string / required | Role assigned to the SDS IP address.  **Choices:**   - `"sdsOnly"` - `"sdcOnly"` - `"all"` |
| **sds_ip_state**  string | State of IP with respect to the SDS.  **Choices:**   - `"present-in-sds"` - `"absent-in-sds"` |
| **sds_name**  string | The name of the SDS.  Mandatory for create operation.  It is unique across the PowerFlex array.  Mutually exclusive with *sds_id*. |
| **sds_new_name**  string | SDS new name. |
| **state**  string / required | State of the SDS.  **Choices:**   - `"present"` - `"absent"` |
| **timeout**  integer | Time after which connection will get terminated.  It is to be mentioned in seconds.  **Default:** `120` |
| **username**  string / required | The username of the PowerFlex host. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](sds_module.md#id4)

> **Note:**
>
> - The maximum limit for the IPs that can be associated with an SDS is 8.
> - There needs to be at least 1 IP for SDS communication and 1 for SDC communication.
> - If only 1 IP exists, it must be with role ‘all’; else 1 IP can be with role ‘all’and other IPs with role ‘sdcOnly’; or 1 IP must be with role ‘sdsOnly’ and others with role ‘sdcOnly’.
> - There can be 1 or more IPs with role ‘sdcOnly’.
> - There must be only 1 IP with SDS role (either with role ‘all’ or ‘sdsOnly’).
> - SDS can be created with RF cache disabled, but, be aware that the RF cache is not always updated. In this case, the user should re-try the operation.
> - The *check_mode* is not supported.
> - The modules present in the collection named as ‘dellemc.powerflex’ are built to support the Dell PowerFlex storage platform.

## [Examples](sds_module.md#id5)

```yaml+jinja
- name: Create SDS
  dellemc.powerflex.sds:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    sds_name: "node0"
    protection_domain_name: "domain1"
    sds_ip_list:
      - ip: "198.10.xxx.xxx"
        role: "all"
    sds_ip_state: "present-in-sds"
    state: "present"

- name: Create SDS with all parameters
  dellemc.powerflex.sds:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    sds_name: "node1"
    protection_domain_name: "domain1"
    sds_ip_list:
      - ip: "198.10.xxx.xxx"
        role: "sdcOnly"
    sds_ip_state: "present-in-sds"
    rmcache_enabled: true
    rmcache_size: 128
    performance_profile: "HighPerformance"
    state: "present"

- name: Get SDS details using name
  dellemc.powerflex.sds:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    sds_name: "node0"
    state: "present"

- name: Get SDS details using ID
  dellemc.powerflex.sds:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    sds_id: "5718253c00000004"
    state: "present"

- name: Modify SDS attributes using name
  dellemc.powerflex.sds:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    sds_name: "node0"
    sds_new_name: "node0_new"
    rfcache_enabled: true
    rmcache_enabled: true
    rmcache_size: 256
    performance_profile: "HighPerformance"
    state: "present"

- name: Modify SDS attributes using ID
  dellemc.powerflex.sds:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    sds_id: "5718253c00000004"
    sds_new_name: "node0_new"
    rfcache_enabled: true
    rmcache_enabled: true
    rmcache_size: 256
    performance_profile: "HighPerformance"
    state: "present"

- name: Add IP and role to an SDS
  dellemc.powerflex.sds:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    sds_name: "node0"
    sds_ip_list:
      - ip: "198.10.xxx.xxx"
        role: "sdcOnly"
    sds_ip_state: "present-in-sds"
    state: "present"

- name: Remove IP and role from an SDS
  dellemc.powerflex.sds:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    sds_name: "node0"
    sds_ip_list:
      - ip: "198.10.xxx.xxx"
        role: "sdcOnly"
    sds_ip_state: "absent-in-sds"
    state: "present"

- name: Delete SDS using name
  dellemc.powerflex.sds:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    sds_name: "node0"
    state: "absent"

- name: Delete SDS using ID
  dellemc.powerflex.sds:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    sds_id: "5718253c00000004"
    state: "absent"
```

## [Return Values](sds_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `false` |
| **sds_details**  dictionary | Details of the SDS.  **Returned:** When SDS exists  **Sample:** `{"authenticationError": "None", "certificateInfo": null, "configuredDrlMode": "Volatile", "drlMode": "Volatile", "faultSetId": null, "fglMetadataCacheSize": 0, "fglMetadataCacheState": "Disabled", "fglNumConcurrentWrites": 1000, "id": "8f3bb0cc00000002", "ipList": [{"ip": "10.47.xxx.xxx", "role": "all"}], "lastUpgradeTime": 0, "links": [{"href": "/api/instances/Sds::8f3bb0cc00000002", "rel": "self"}, {"href": "/api/instances/Sds::8f3bb0cc00000002/relationships /Statistics", "rel": "/api/Sds/relationship/Statistics"}, {"href": "/api/instances/Sds::8f3bb0cc00000002/relationships /SpSds", "rel": "/api/Sds/relationship/SpSds"}, {"href": "/api/instances/Sds::8f3bb0cc00000002/relationships /Device", "rel": "/api/Sds/relationship/Device"}, {"href": "/api/instances/ProtectionDomain::9300c1f900000000", "rel": "/api/parent/relationship/protectionDomainId"}], "maintenanceState": "NoMaintenance", "maintenanceType": "NoMaintenance", "mdmConnectionState": "Connected", "membershipState": "Joined", "name": "node0", "numOfIoBuffers": null, "numRestarts": 2, "onVmWare": true, "perfProfile": "HighPerformance", "port": 7072, "protectionDomainId": "9300c1f900000000", "protectionDomainName": "domain1", "raidControllers": null, "rfcacheEnabled": true, "rfcacheErrorApiVersionMismatch": false, "rfcacheErrorDeviceDoesNotExist": false, "rfcacheErrorInconsistentCacheConfiguration": false, "rfcacheErrorInconsistentSourceConfiguration": false, "rfcacheErrorInvalidDriverPath": false, "rfcacheErrorLowResources": false, "rmcacheEnabled": true, "rmcacheFrozen": false, "rmcacheMemoryAllocationState": "AllocationPending", "rmcacheSizeInKb": 131072, "rmcacheSizeInMb": 128, "sdsConfigurationFailure": null, "sdsDecoupled": null, "sdsReceiveBufferAllocationFailures": null, "sdsState": "Normal", "softwareVersionInfo": "R3_6.0.0"}` |
| **authenticationError**  string | Indicates authentication error.  **Returned:** success |
| **certificateInfo**  string | Information about certificate.  **Returned:** success |
| **configuredDrlMode**  string | Configured DRL mode.  **Returned:** success |
| **drlMode**  string | DRL mode.  **Returned:** success |
| **faultSetId**  string | Fault set ID.  **Returned:** success |
| **fglMetadataCacheSize**  integer | FGL metadata cache size.  **Returned:** success |
| **fglMetadataCacheState**  string | FGL metadata cache state.  **Returned:** success |
| **fglNumConcurrentWrites**  integer | FGL concurrent writes.  **Returned:** success |
| **id**  string | SDS ID.  **Returned:** success |
| **ipList**  list / elements=string | SDS IP list.  **Returned:** success |
| **ip**  string | IP present in the SDS.  **Returned:** success |
| **role**  string | Role of the SDS IP.  **Returned:** success |
| **lastUpgradeTime**  string | Last time SDS was upgraded.  **Returned:** success |
| **links**  list / elements=string | SDS links.  **Returned:** success |
| **href**  string | SDS instance URL.  **Returned:** success |
| **rel**  string | SDS’s relationship with different entities.  **Returned:** success |
| **maintenanceState**  string | Maintenance state.  **Returned:** success |
| **maintenanceType**  string | Maintenance type.  **Returned:** success |
| **mdmConnectionState**  string | MDM connection state.  **Returned:** success |
| **membershipState**  string | Membership state.  **Returned:** success |
| **name**  string | Name of the SDS.  **Returned:** success |
| **numOfIoBuffers**  integer | Number of IO buffers.  **Returned:** success |
| **numRestarts**  integer | Number of restarts.  **Returned:** success |
| **onVmWare**  boolean | Presence on VMware.  **Returned:** success |
| **perfProfile**  string | Performance profile.  **Returned:** success |
| **port**  integer | SDS port.  **Returned:** success |
| **protectionDomainId**  string | Protection Domain ID.  **Returned:** success |
| **protectionDomainName**  string | Protection Domain Name.  **Returned:** success |
| **raidControllers**  integer | Number of RAID controllers.  **Returned:** success |
| **rfcacheEnabled**  boolean | Whether RF cache is enabled or not.  **Returned:** success |
| **rfcacheErrorApiVersionMismatch**  boolean | RF cache error for API version mismatch.  **Returned:** success |
| **rfcacheErrorDeviceDoesNotExist**  boolean | RF cache error for device does not exist.  **Returned:** success |
| **rfcacheErrorInconsistentCacheConfiguration**  boolean | RF cache error for inconsistent cache configuration.  **Returned:** success |
| **rfcacheErrorInconsistentSourceConfiguration**  boolean | RF cache error for inconsistent source configuration.  **Returned:** success |
| **rfcacheErrorInvalidDriverPath**  boolean | RF cache error for invalid driver path.  **Returned:** success |
| **rfcacheErrorLowResources**  boolean | RF cache error for low resources.  **Returned:** success |
| **rmcacheEnabled**  boolean | Whether Read RAM cache is enabled or not.  **Returned:** success |
| **rmcacheFrozen**  boolean | RM cache frozen.  **Returned:** success |
| **rmcacheMemoryAllocationState**  boolean | RM cache memory allocation state.  **Returned:** success |
| **rmcacheSizeInKb**  integer | RM cache size in KB.  **Returned:** success |
| **rmcacheSizeInMb**  integer | RM cache size in MB.  **Returned:** success |
| **sdsConfigurationFailure**  string | SDS configuration failure.  **Returned:** success |
| **sdsDecoupled**  string | SDS decoupled.  **Returned:** success |
| **sdsReceiveBufferAllocationFailures**  string | SDS receive buffer allocation failures.  **Returned:** success |
| **sdsState**  string | SDS state.  **Returned:** success |
| **softwareVersionInfo**  string | SDS software version information.  **Returned:** success |

### Authors

- Rajshree Khare (@khareRajshree)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-powerflex/tree/1.9.0)
