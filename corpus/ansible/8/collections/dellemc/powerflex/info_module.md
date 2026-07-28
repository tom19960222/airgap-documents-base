---
collection: ansible
version: "8"
title: "dellemc.powerflex.info module – Gathering information about Dell PowerFlex"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/powerflex/info_module.html
fetched_at: 2026-07-28T02:05:09+00:00
---
# dellemc.powerflex.info module – Gathering information about Dell PowerFlex

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
> see [Requirements](info_module.md#ansible-collections-dellemc-powerflex-info-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.powerflex.info`.

New in dellemc.powerflex 1.0.0

- [Synopsis](info_module.md#synopsis)
- [Requirements](info_module.md#requirements)
- [Parameters](info_module.md#parameters)
- [Notes](info_module.md#notes)
- [Examples](info_module.md#examples)
- [Return Values](info_module.md#return-values)

## [Synopsis](info_module.md#id1)

- Gathering information about Dell PowerFlex storage system includes getting the api details, list of volumes, SDSs, SDCs, storage pools, protection domains, snapshot policies, and devices.

Aliases: dellemc_powerflex_gatherfacts

## [Requirements](info_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.5 or later.
- Ansible-core 2.13 or later.
- PyPowerFlex 1.8.0.
- Python 3.9, 3.10 or 3.11.

## [Parameters](info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **filters**  list / elements=dictionary | List of filters to support filtered output for storage entities.  Each filter is a list of *filter_key*, *filter_operator*, *filter_value*.  Supports passing of multiple filters. |
| **filter_key**  string / required | Name identifier of the filter. |
| **filter_operator**  string / required | Operation to be performed on filter key.  **Choices:**   - `"equal"` |
| **filter_value**  string / required | Value of the filter key. |
| **gather_subset**  list / elements=string | List of string variables to specify the Powerflex storage system entities for which information is required.  Volumes - `vol`.  Storage pools - `storage_pool`.  Protection domains - `protection_domain`.  SDCs - `sdc`.  SDSs - `sds`.  Snapshot policies - `snapshot_policy`.  Devices - `device`.  Replication consistency groups - `rcg`.  Replication pairs - `replication_pair`.  **Choices:**   - `"vol"` - `"storage_pool"` - `"protection_domain"` - `"sdc"` - `"sds"` - `"snapshot_policy"` - `"device"` - `"rcg"` - `"replication_pair"` |
| **hostname**  aliases: gateway_host  string / required | IP or FQDN of the PowerFlex host. |
| **password**  string / required | The password of the PowerFlex host. |
| **port**  integer | Port number through which communication happens with PowerFlex host.  **Default:** `443` |
| **timeout**  integer | Time after which connection will get terminated.  It is to be mentioned in seconds.  **Default:** `120` |
| **username**  string / required | The username of the PowerFlex host. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](info_module.md#id4)

> **Note:**
>
> - The *check_mode* is supported.
> - The modules present in the collection named as ‘dellemc.powerflex’ are built to support the Dell PowerFlex storage platform.

## [Examples](info_module.md#id5)

```yaml+jinja
- name: Get detailed list of PowerFlex entities
  dellemc.powerflex.info:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    gather_subset:
      - vol
      - storage_pool
      - protection_domain
      - sdc
      - sds
      - snapshot_policy
      - device
      - rcg
      - replication_pair

- name: Get a subset list of PowerFlex volumes
  dellemc.powerflex.info:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    gather_subset:
      - vol
    filters:
      - filter_key: "name"
        filter_operator: "equal"
        filter_value: "ansible_test"
```

## [Return Values](info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **API_Version**  string | API version of PowerFlex API Gateway.  **Returned:** always  **Sample:** `"3.5"` |
| **Array_Details**  dictionary | System entities of PowerFlex storage array.  **Returned:** always  **Sample:** `{"addressSpaceUsage": "Normal", "authenticationMethod": "Native", "capacityAlertCriticalThresholdPercent": 90, "capacityAlertHighThresholdPercent": 80, "capacityTimeLeftInDays": "24", "cliPasswordAllowed": true, "daysInstalled": 66, "defragmentationEnabled": true, "enterpriseFeaturesEnabled": true, "id": "4a54a8ba6df0690f", "installId": "38622771228e56db", "isInitialLicense": true, "lastUpgradeTime": 0, "managementClientSecureCommunicationEnabled": true, "maxCapacityInGb": "Unlimited", "mdmCluster": {"clusterMode": "ThreeNodes", "clusterState": "ClusteredNormal", "goodNodesNum": 3, "goodReplicasNum": 2, "id": "5356091375512217871", "master": {"id": "6101582c2ca8db00", "ips": ["10.47.xxx.xxx"], "managementIPs": ["10.47.xxx.xxx"], "name": "node0", "opensslVersion": "OpenSSL 1.0.2k-fips  26 Jan 2017", "port": 9011, "role": "Manager", "status": "Normal", "versionInfo": "R3_6.0.0", "virtualInterfaces": ["ens160"]}, "slaves": [{"id": "23fb724015661901", "ips": ["10.47.xxx.xxx"], "managementIPs": ["10.47.xxx.xxx"], "opensslVersion": "OpenSSL 1.0.2k-fips  26 Jan 2017", "port": 9011, "role": "Manager", "status": "Normal", "versionInfo": "R3_6.0.0", "virtualInterfaces": ["ens160"]}], "tieBreakers": [{"id": "6ef27eb20d0c1202", "ips": ["10.47.xxx.xxx"], "managementIPs": ["10.47.xxx.xxx"], "opensslVersion": "N/A", "port": 9011, "role": "TieBreaker", "status": "Normal", "versionInfo": "R3_6.0.0"}]}, "mdmExternalPort": 7611, "mdmManagementPort": 6611, "mdmSecurityPolicy": "None", "showGuid": true, "swid": "", "systemVersionName": "DellEMC PowerFlex Version: R3_6.0.354", "tlsVersion": "TLSv1.2", "upgradeState": "NoUpgrade"}` |
| **addressSpaceUsage**  string | Address space usage.  **Returned:** success |
| **authenticationMethod**  string | Authentication method.  **Returned:** success |
| **capacityAlertCriticalThresholdPercent**  integer | Capacity alert critical threshold percentage.  **Returned:** success |
| **capacityAlertHighThresholdPercent**  integer | Capacity alert high threshold percentage.  **Returned:** success |
| **capacityTimeLeftInDays**  string | Capacity time left in days.  **Returned:** success |
| **cliPasswordAllowed**  boolean | CLI password allowed.  **Returned:** success |
| **daysInstalled**  integer | Days installed.  **Returned:** success |
| **defragmentationEnabled**  boolean | Defragmentation enabled.  **Returned:** success |
| **enterpriseFeaturesEnabled**  boolean | Enterprise features enabled.  **Returned:** success |
| **id**  string | The ID of the system.  **Returned:** success |
| **installId**  string | installation Id.  **Returned:** success |
| **isInitialLicense**  boolean | Initial license.  **Returned:** success |
| **lastUpgradeTime**  integer | Last upgrade time.  **Returned:** success |
| **managementClientSecureCommunicationEnabled**  boolean | Management client secure communication enabled.  **Returned:** success |
| **maxCapacityInGb**  dictionary | Maximum capacity in GB.  **Returned:** success |
| **mdmCluster**  dictionary | MDM cluster details.  **Returned:** success |
| **mdmExternalPort**  integer | MDM external port.  **Returned:** success |
| **mdmManagementPort**  integer | MDM management port.  **Returned:** success |
| **mdmSecurityPolicy**  string | MDM security policy.  **Returned:** success |
| **showGuid**  boolean | Show guid.  **Returned:** success |
| **swid**  string | SWID.  **Returned:** success |
| **systemVersionName**  string | System version and name.  **Returned:** success |
| **tlsVersion**  string | TLS version.  **Returned:** success |
| **upgradeState**  string | Upgrade state.  **Returned:** success |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `false` |
| **Devices**  list / elements=string | Details of devices.  **Returned:** always  **Sample:** `[{"id": "b6efa59900000000", "name": "device230"}, {"id": "b6efa5fa00020000", "name": "device_node0"}, {"id": "b7f3a60900010000", "name": "device22"}]` |
| **id**  string | device id.  **Returned:** success |
| **name**  string | device name.  **Returned:** success |
| **Protection_Domains**  list / elements=string | Details of all protection domains.  **Returned:** always  **Sample:** `[{"id": "9300e90900000001", "name": "domain2"}, {"id": "9300c1f900000000", "name": "domain1"}]` |
| **id**  string | protection domain id.  **Returned:** success |
| **name**  string | protection domain name.  **Returned:** success |
| **Replication_Consistency_Groups**  list / elements=string | Details of rcgs.  **Returned:** always  **Sample:** `{"abstractState": "Ok", "activeLocal": true, "activeRemote": true, "currConsistMode": "Consistent", "disasterRecoveryState": "None", "error": 65, "failoverState": "None", "failoverType": "None", "freezeState": "Unfrozen", "id": "aadc17d500000000", "inactiveReason": 11, "lastSnapCreationRc": "SUCCESS", "lastSnapGroupId": "e58280b300000001", "lifetimeState": "Normal", "localActivityState": "Active", "name": "test_rcg", "pauseMode": "None", "peerMdmId": "6c3d94f600000000", "protectionDomainId": "b969400500000000", "remoteActivityState": "Active", "remoteDisasterRecoveryState": "None", "remoteId": "2130961a00000000", "remoteMdmId": "0e7a082862fedf0f", "remoteProtectionDomainId": "4eeb304600000000", "remoteProtectionDomainName": "domain1", "replicationDirection": "LocalToRemote", "rpoInSeconds": 30, "snapCreationInProgress": false, "targetVolumeAccessMode": "NoAccess", "type": "User"}` |
| **abstractState**  string | The abstract state of the replication consistency group.  **Returned:** success |
| **activeLocal**  boolean | Whether the local replication consistency group is active.  **Returned:** success |
| **activeRemote**  boolean | Whether the remote replication consistency group is active  **Returned:** success |
| **currConsistMode**  string | The current consistency mode of the replication consistency group.  **Returned:** success |
| **disasterRecoveryState**  string | The state of disaster recovery of the local replication consistency group.  **Returned:** success |
| **error**  integer | The error code of the replication consistency group.  **Returned:** success |
| **failoverState**  string | The state of failover of the replication consistency group.  **Returned:** success |
| **failoverType**  string | The type of failover of the replication consistency group.  **Returned:** success |
| **freezeState**  string | The freeze state of the replication consistency group.  **Returned:** success |
| **id**  string | The ID of the replication consistency group.  **Returned:** success |
| **inactiveReason**  integer | The reason for the inactivity of the replication consistency group.  **Returned:** success |
| **lastSnapCreationRc**  integer | The return code of the last snapshot of the replication consistency group.  **Returned:** success |
| **lastSnapGroupId**  string | ID of the last snapshot of the replication consistency group.  **Returned:** success |
| **lifetimeState**  string | The Lifetime state of the replication consistency group.  **Returned:** success |
| **localActivityState**  string | The state of activity of the local replication consistency group.  **Returned:** success |
| **name**  string | The name of the replication consistency group.  **Returned:** success |
| **pauseMode**  string | The Lifetime state of the replication consistency group.  **Returned:** success |
| **peerMdmId**  string | The ID of the peer MDM of the replication consistency group.  **Returned:** success |
| **protectionDomainId**  string | The Protection Domain ID of the replication consistency group.  **Returned:** success |
| **remoteActivityState**  string | The state of activity of the remote replication consistency group..  **Returned:** success |
| **remoteDisasterRecoveryState**  string | The state of disaster recovery of the remote replication consistency group.  **Returned:** success |
| **remoteId**  string | The ID of the remote replication consistency group.  **Returned:** success |
| **remoteMdmId**  string | The ID of the remote MDM of the replication consistency group.  **Returned:** success |
| **remoteProtectionDomainId**  string | The ID of the remote Protection Domain.  **Returned:** success |
| **remoteProtectionDomainName**  string | The Name of the remote Protection Domain.  **Returned:** success |
| **replicationDirection**  string | The direction of the replication of the replication consistency group.  **Returned:** success |
| **rpoInSeconds**  integer | The RPO value of the replication consistency group in seconds.  **Returned:** success |
| **snapCreationInProgress**  boolean | Whether the process of snapshot creation of the replication consistency group is in progress or not.  **Returned:** success |
| **targetVolumeAccessMode**  string | The access mode of the target volume of the replication consistency group.  **Returned:** success |
| **type**  string | The type of the replication consistency group.  **Returned:** success |
| **Replication_pairs**  list / elements=string | Details of the replication pairs.  **Returned:** Always  **Sample:** `{"copyType": "OnlineCopy", "id": "23aa0bc900000001", "initialCopyPriority": -1, "initialCopyState": "Done", "lifetimeState": "Normal", "localActivityState": "RplEnabled", "localVolumeId": "e2bc1fab00000008", "name": null, "peerSystemName": null, "remoteActivityState": "RplEnabled", "remoteCapacityInMB": 8192, "remoteId": "a058446700000001", "remoteVolumeId": "1cda7af20000000d", "remoteVolumeName": "vol", "replicationConsistencyGroupId": "e2ce036b00000002", "userRequestedPauseTransmitInitCopy": false}` |
| **copyType**  string | The copy type of the replication pair.  **Returned:** success |
| **id**  string | The ID of the replication pair.  **Returned:** success |
| **initialCopyState**  string | The inital copy state of the replication pair.  **Returned:** success |
| **localActivityState**  string | The state of activity of the local replication pair.  **Returned:** success |
| **localVolumeId**  string | The ID of the local volume.  **Returned:** success |
| **name**  string | The name of the replication pair.  **Returned:** success |
| **remoteActivityState**  string | The state of activity of the remote replication pair.  **Returned:** success |
| **remoteId**  string | The ID of the remote replication pair.  **Returned:** success |
| **replicationConsistencyGroupId**  string | The ID of the replication consistency group.  **Returned:** success |
| **SDCs**  list / elements=string | Details of storage data clients.  **Returned:** always  **Sample:** `[{"id": "07335d3d00000006", "name": "LGLAP203"}, {"id": "07335d3c00000005", "name": "LGLAP178"}, {"id": "0733844a00000003"}]` |
| **id**  string | storage data client id.  **Returned:** success |
| **name**  string | storage data client name.  **Returned:** success |
| **SDSs**  list / elements=string | Details of storage data servers.  **Returned:** always  **Sample:** `[{"id": "8f3bb0cc00000002", "name": "node0"}, {"id": "8f3bb0ce00000000", "name": "node1"}, {"id": "8f3bb15300000001", "name": "node22"}]` |
| **id**  string | storage data server id.  **Returned:** success |
| **name**  string | storage data server name.  **Returned:** success |
| **Snapshot_Policies**  list / elements=string | Details of snapshot policies.  **Returned:** always  **Sample:** `[{"id": "2b380c5c00000000", "name": "sample_snap_policy"}, {"id": "2b380c5d00000001", "name": "sample_snap_policy_1"}]` |
| **id**  string | snapshot policy id.  **Returned:** success |
| **name**  string | snapshot policy name.  **Returned:** success |
| **Storage_Pools**  list / elements=string | Details of storage pools.  **Returned:** always  **Sample:** `[{"addressSpaceUsage": "Normal", "addressSpaceUsageType": "DeviceCapacityLimit", "backgroundScannerBWLimitKBps": 3072, "backgroundScannerMode": "DataComparison", "bgScannerCompareErrorAction": "ReportAndFix", "bgScannerReadErrorAction": "ReportAndFix", "capacityAlertCriticalThreshold": 90, "capacityAlertHighThreshold": 80, "capacityUsageState": "Normal", "capacityUsageType": "NetCapacity", "checksumEnabled": false, "compressionMethod": "Invalid", "dataLayout": "MediumGranularity", "externalAccelerationType": "None", "fglAccpId": null, "fglExtraCapacity": null, "fglMaxCompressionRatio": null, "fglMetadataSizeXx100": null, "fglNvdimmMetadataAmortizationX100": null, "fglNvdimmWriteCacheSizeInMb": null, "fglOverProvisioningFactor": null, "fglPerfProfile": null, "fglWriteAtomicitySize": null, "fragmentationEnabled": true, "id": "e0d8f6c900000000", "links": [{"href": "/api/instances/StoragePool::e0d8f6c900000000", "rel": "self"}, {"href": "/api/instances/StoragePool::e0d8f6c900000000 /relationships/Statistics", "rel": "/api/StoragePool/relationship/Statistics"}, {"href": "/api/instances/StoragePool::e0d8f6c900000000 /relationships/SpSds", "rel": "/api/StoragePool/relationship/SpSds"}, {"href": "/api/instances/StoragePool::e0d8f6c900000000 /relationships/Volume", "rel": "/api/StoragePool/relationship/Volume"}, {"href": "/api/instances/StoragePool::e0d8f6c900000000 /relationships/Device", "rel": "/api/StoragePool/relationship/Device"}, {"href": "/api/instances/StoragePool::e0d8f6c900000000 /relationships/VTree", "rel": "/api/StoragePool/relationship/VTree"}, {"href": "/api/instances/ProtectionDomain::9300c1f900000000", "rel": "/api/parent/relationship/protectionDomainId"}], "mediaType": "HDD", "name": "pool1", "numOfParallelRebuildRebalanceJobsPerDevice": 2, "persistentChecksumBuilderLimitKb": 3072, "persistentChecksumEnabled": true, "persistentChecksumState": "Protected", "persistentChecksumValidateOnRead": false, "protectedMaintenanceModeIoPriorityAppBwPerDeviceThresholdInKbps": null, "protectedMaintenanceModeIoPriorityAppIopsPerDeviceThreshold": null, "protectedMaintenanceModeIoPriorityBwLimitPerDeviceInKbps": 10240, "protectedMaintenanceModeIoPriorityNumOfConcurrentIosPerDevice": 1, "protectedMaintenanceModeIoPriorityPolicy": "limitNumOfConcurrentIos", "protectedMaintenanceModeIoPriorityQuietPeriodInMsec": null, "protectionDomainId": "9300c1f900000000", "protectionDomainName": "domain1", "rebalanceEnabled": true, "rebalanceIoPriorityAppBwPerDeviceThresholdInKbps": null, "rebalanceIoPriorityAppIopsPerDeviceThreshold": null, "rebalanceIoPriorityBwLimitPerDeviceInKbps": 10240, "rebalanceIoPriorityNumOfConcurrentIosPerDevice": 1, "rebalanceIoPriorityPolicy": "favorAppIos", "rebalanceIoPriorityQuietPeriodInMsec": null, "rebuildEnabled": true, "rebuildIoPriorityAppBwPerDeviceThresholdInKbps": null, "rebuildIoPriorityAppIopsPerDeviceThreshold": null, "rebuildIoPriorityBwLimitPerDeviceInKbps": 10240, "rebuildIoPriorityNumOfConcurrentIosPerDevice": 1, "rebuildIoPriorityPolicy": "limitNumOfConcurrentIos", "rebuildIoPriorityQuietPeriodInMsec": null, "replicationCapacityMaxRatio": 32, "rmcacheWriteHandlingMode": "Cached", "sparePercentage": 10, "statistics": {"BackgroundScannedInMB": 3466920, "activeBckRebuildCapacityInKb": 0, "activeEnterProtectedMaintenanceModeCapacityInKb": 0, "aggregateCompressionLevel": "Uncompressed", "atRestCapacityInKb": 1248256, "backgroundScanCompareErrorCount": 0, "backgroundScanFixedCompareErrorCount": 0, "bckRebuildReadBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "bckRebuildWriteBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "capacityAvailableForVolumeAllocationInKb": 369098752, "capacityInUseInKb": 2496512, "capacityInUseNoOverheadInKb": 2496512, "capacityLimitInKb": 845783040, "compressedDataCompressionRatio": 0.0, "compressionRatio": 1.0, "currentFglMigrationSizeInKb": 0, "deviceIds": [], "enterProtectedMaintenanceModeCapacityInKb": 0, "enterProtectedMaintenanceModeReadBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "enterProtectedMaintenanceModeWriteBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "exitProtectedMaintenanceModeReadBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "exitProtectedMaintenanceModeWriteBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "exposedCapacityInKb": 0, "failedCapacityInKb": 0, "fwdRebuildReadBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "fwdRebuildWriteBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "inMaintenanceCapacityInKb": 0, "inMaintenanceVacInKb": 0, "inUseVacInKb": 184549376, "inaccessibleCapacityInKb": 0, "logWrittenBlocksInKb": 0, "maxCapacityInKb": 845783040, "migratingVolumeIds": [], "migratingVtreeIds": [], "movingCapacityInKb": 0, "netCapacityInUseInKb": 1248256, "normRebuildCapacityInKb": 0, "normRebuildReadBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "normRebuildWriteBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "numOfDeviceAtFaultRebuilds": 0, "numOfDevices": 3, "numOfIncomingVtreeMigrations": 0, "numOfVolumes": 8, "numOfVolumesInDeletion": 0, "numOfVtrees": 8, "overallUsageRatio": 73.92289, "pendingBckRebuildCapacityInKb": 0, "pendingEnterProtectedMaintenanceModeCapacityInKb": 0, "pendingExitProtectedMaintenanceModeCapacityInKb": 0, "pendingFwdRebuildCapacityInKb": 0, "pendingMovingCapacityInKb": 0, "pendingMovingInBckRebuildJobs": 0, "persistentChecksumBuilderProgress": 100.0, "persistentChecksumCapacityInKb": 414720, "primaryReadBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "primaryReadFromDevBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "primaryReadFromRmcacheBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "primaryVacInKb": 92274688, "primaryWriteBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "protectedCapacityInKb": 2496512, "protectedVacInKb": 184549376, "provisionedAddressesInKb": 2496512, "rebalanceCapacityInKb": 0, "rebalanceReadBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "rebalanceWriteBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "rfacheReadHit": 0, "rfacheWriteHit": 0, "rfcacheAvgReadTime": 0, "rfcacheAvgWriteTime": 0, "rfcacheIoErrors": 0, "rfcacheIosOutstanding": 0, "rfcacheIosSkipped": 0, "rfcacheReadMiss": 0, "rmPendingAllocatedInKb": 0, "rmPendingThickInKb": 0, "rplJournalCapAllowed": 0, "rplTotalJournalCap": 0, "rplUsedJournalCap": 0, "secondaryReadBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "secondaryReadFromDevBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "secondaryReadFromRmcacheBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "secondaryVacInKb": 92274688, "secondaryWriteBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "semiProtectedCapacityInKb": 0, "semiProtectedVacInKb": 0, "snapCapacityInUseInKb": 0, "snapCapacityInUseOccupiedInKb": 0, "snapshotCapacityInKb": 0, "spSdsIds": ["abdfe71b00030001", "abdce71d00040001", "abdde71e00050001"], "spareCapacityInKb": 84578304, "targetOtherLatency": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "targetReadLatency": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "targetWriteLatency": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "tempCapacityInKb": 0, "tempCapacityVacInKb": 0, "thickCapacityInUseInKb": 0, "thinAndSnapshotRatio": 73.92289, "thinCapacityAllocatedInKm": 184549376, "thinCapacityInUseInKb": 0, "thinUserDataCapacityInKb": 2496512, "totalFglMigrationSizeInKb": 0, "totalReadBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "totalWriteBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "trimmedUserDataCapacityInKb": 0, "unreachableUnusedCapacityInKb": 0, "unusedCapacityInKb": 758708224, "userDataCapacityInKb": 2496512, "userDataCapacityNoTrimInKb": 2496512, "userDataReadBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "userDataSdcReadLatency": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "userDataSdcTrimLatency": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "userDataSdcWriteLatency": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "userDataTrimBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "userDataWriteBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "volMigrationReadBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "volMigrationWriteBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "volumeAddressSpaceInKb": "922XXXXX", "volumeAllocationLimitInKb": "3707XXXXX", "volumeIds": ["456afc7900XXXXXXXX"], "vtreeAddresSpaceInKb": 92274688, "vtreeIds": ["32b1681bXXXXXXXX"]}, "useRfcache": false, "useRmcache": false, "vtreeMigrationIoPriorityAppBwPerDeviceThresholdInKbps": null, "vtreeMigrationIoPriorityAppIopsPerDeviceThreshold": null, "vtreeMigrationIoPriorityBwLimitPerDeviceInKbps": 10240, "vtreeMigrationIoPriorityNumOfConcurrentIosPerDevice": 1, "vtreeMigrationIoPriorityPolicy": "favorAppIos", "vtreeMigrationIoPriorityQuietPeriodInMsec": null, "zeroPaddingEnabled": true}]` |
| **id**  string | ID of the storage pool under protection domain.  **Returned:** success |
| **mediaType**  string | Type of devices in the storage pool.  **Returned:** success |
| **name**  string | Name of the storage pool under protection domain.  **Returned:** success |
| **protectionDomainId**  string | ID of the protection domain in which pool resides.  **Returned:** success |
| **protectionDomainName**  string | Name of the protection domain in which pool resides.  **Returned:** success |
| **statistics**  dictionary | Statistics details of the storage pool.  **Returned:** success |
| **capacityInUseInKb**  string | Total capacity of the storage pool.  **Returned:** success |
| **deviceIds**  list / elements=string | Device Ids of the storage pool.  **Returned:** success |
| **unusedCapacityInKb**  string | Unused capacity of the storage pool.  **Returned:** success |
| **useRfcache**  boolean | Enable/Disable RFcache on a specific storage pool.  **Returned:** success |
| **useRmcache**  boolean | Enable/Disable RMcache on a specific storage pool.  **Returned:** success |
| **Volumes**  list / elements=string | Details of volumes.  **Returned:** always  **Sample:** `[{"accessModeLimit": "ReadWrite", "ancestorVolumeId": null, "autoSnapshotGroupId": null, "compressionMethod": "Invalid", "consistencyGroupId": null, "creationTime": 1661234220, "dataLayout": "MediumGranularity", "id": "456afd7XXXXXXX", "lockedAutoSnapshot": false, "lockedAutoSnapshotMarkedForRemoval": false, "managedBy": "ScaleIO", "mappedSdcInfo": [{"accessMode": "ReadWrite", "isDirectBufferMapping": false, "limitBwInMbps": 0, "limitIops": 0, "sdcId": "c42425cbXXXXX", "sdcIp": "10.XXX.XX.XX", "sdcName": null}], "name": "vol-1", "notGenuineSnapshot": false, "originalExpiryTime": 0, "pairIds": null, "replicationJournalVolume": false, "replicationTimeStamp": 0, "retentionLevels": [], "secureSnapshotExpTime": 0, "sizeInKb": 8388608, "snplIdOfAutoSnapshot": null, "snplIdOfSourceVolume": null, "statistics": {"childVolumeIds": [], "descendantVolumeIds": [], "initiatorSdcId": null, "mappedSdcIds": ["c42425XXXXXX"], "numOfChildVolumes": 0, "numOfDescendantVolumes": 0, "numOfMappedSdcs": 1, "registrationKey": null, "registrationKeys": [], "replicationJournalVolume": false, "replicationState": "UnmarkedForReplication", "reservationType": "NotReserved", "rplTotalJournalCap": 0, "rplUsedJournalCap": 0, "userDataReadBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "userDataSdcReadLatency": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "userDataSdcTrimLatency": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "userDataSdcWriteLatency": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "userDataTrimBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "userDataWriteBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}}, "storagePoolId": "7630a248XXXXXXX", "timeStampIsAccurate": false, "useRmcache": false, "volumeReplicationState": "UnmarkedForReplication", "volumeType": "ThinProvisioned", "vtreeId": "32b168bXXXXXX"}]` |
| **id**  string | The ID of the volume.  **Returned:** success |
| **mappedSdcInfo**  dictionary | The details of the mapped SDC.  **Returned:** success |
| **accessMode**  string | mapping access mode for the specified volume.  **Returned:** success |
| **limitBwInMbps**  integer | Bandwidth limit for the SDC.  **Returned:** success |
| **limitIops**  integer | IOPS limit for the SDC.  **Returned:** success |
| **sdcId**  string | ID of the SDC.  **Returned:** success |
| **sdcIp**  string | IP of the SDC.  **Returned:** success |
| **sdcName**  string | Name of the SDC.  **Returned:** success |
| **name**  string | Name of the volume.  **Returned:** success |
| **protectionDomainId**  string | ID of the protection domain in which volume resides.  **Returned:** success |
| **protectionDomainName**  string | Name of the protection domain in which volume resides.  **Returned:** success |
| **sizeInGb**  integer | Size of the volume in Gb.  **Returned:** success |
| **sizeInKb**  integer | Size of the volume in Kb.  **Returned:** success |
| **snapshotPolicyId**  string | ID of the snapshot policy associated with volume.  **Returned:** success |
| **snapshotPolicyName**  string | Name of the snapshot policy associated with volume.  **Returned:** success |
| **snapshotsList**  string | List of snapshots associated with the volume.  **Returned:** success |
| **statistics**  dictionary | Statistics details of the storage pool.  **Returned:** success |
| **numOfChildVolumes**  integer | Number of child volumes.  **Returned:** success |
| **numOfMappedSdcs**  integer | Number of mapped Sdcs of the volume.  **Returned:** success |
| **storagePoolId**  string | ID of the storage pool in which volume resides.  **Returned:** success |
| **storagePoolName**  string | Name of the storage pool in which volume resides.  **Returned:** success |

### Authors

- Arindam Datta (@dattaarindam)
- Trisha Datta (@trisha-dell)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-powerflex/tree/1.9.0)
