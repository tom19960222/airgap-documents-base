---
collection: ansible
version: "8"
title: "ibm.spectrum_virtualize.ibm_svc_info module – This module gathers various information from the IBM Spectrum Virtualize family storage systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/spectrum_virtualize/ibm_svc_info_module.html
fetched_at: 2026-07-28T02:34:50+00:00
---
# ibm.spectrum_virtualize.ibm_svc_info module – This module gathers various information from the IBM Spectrum Virtualize family storage systems

> **Note:**
>
> This module is part of the [ibm.spectrum_virtualize collection](https://galaxy.ansible.com/ui/repo/published/ibm/spectrum_virtualize/) (version 1.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ibm.spectrum_virtualize`.
>
> To use it in a playbook, specify: `ibm.spectrum_virtualize.ibm_svc_info`.

New in ibm.spectrum_virtualize 1.0.0

- [Synopsis](ibm_svc_info_module.md#synopsis)
- [Parameters](ibm_svc_info_module.md#parameters)
- [Notes](ibm_svc_info_module.md#notes)
- [Examples](ibm_svc_info_module.md#examples)
- [Return Values](ibm_svc_info_module.md#return-values)

## [Synopsis](ibm_svc_info_module.md#id1)

- Gathers the list of specified IBM Spectrum Virtualize family storage system entities. These include the list of nodes, pools, volumes, hosts, host clusters, FC ports, iSCSI ports, target port FC, FC consistgrp, vdiskcopy, I/O groups, FC map, FC connectivity, NVMe fabric, array, and system.

## [Parameters](ibm_svc_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Spectrum Virtualize storage system. |
| **domain**  string | Domain for the Spectrum Virtualize storage system.  Valid when hostname is used for the parameter *clustername*. |
| **gather_subset**  list / elements=string | List of string variables to specify the Spectrum Virtualize entities for which information is required.  all - list of all Spectrum Virtualize entities supported by the module.  vol - lists information for VDisks.  pool - lists information for mdiskgrps.  node - lists information for nodes.  iog - lists information for I/O groups.  host - lists information for hosts.  hostvdiskmap - lists all VDisks mapped to host ‘objectname’  vdiskhostmap - lists all hosts VDisk ‘objectname’ is mapped to  hc - lists information for host clusters.  fc - lists information for FC connectivity.  fcport - lists information for FC ports.  targetportfc - lists information for WWPN which is required to set up FC zoning and to display the current failover status of host I/O ports.  fcmap - lists information for FC maps.  rcrelationship - lists information for remote copy relationships.  fcconsistgrp - displays a concise list or a detailed view of flash copy consistency groups.  rcconsistgrp - displays a concise list or a detailed view of remote copy consistency groups.  iscsiport - lists information for iSCSI ports.  vdiskcopy - lists information for volume copy.  array - lists information for array MDisks.  system - displays the storage system information.  cloudaccount - lists all the configured cloud accounts.  cloudaccountusage - lists the usage information about the configured cloud storage accounts.  cloudimportcandidate - lists information about systems that have data that is stored in the cloud accounts.  ldapserver - lists the most recent details for all configured Lightweight Directory Access Protocol (LDAP) servers.  drive - lists the configuration information and drive vital product data (VPD).  user - lists all the users that are created on the system.  usergroup - lists the user groups that is created on the system.  ownershipgroup - displays the ownership groups that are available in the system.  partnership - lists all the clustered systems (systems) that are associated with the local system.  replicationpolicy - lists all the replication policies on the system.  cloudbackup - lists the volumes that have cloud snapshot enabled and volumes that have cloud snapshots in the cloud account.  cloudbackupgeneration - lists any volume snapshots available on the specified volume. *objectname* is a mandatory parameter.  snapshotpolicy - lists all the snapshot policies on the system.  snapshotpolicyschedule - lists all snapshot schedules on the system.  volumegroup - lists all volume groups on the system.  volumegroupsnapshotpolicy - lists the snapshot policy attributes associated with a volume group on the system.  volumesnapshot - lists all volume snapshots.  dnsserver - lists the information for any Domain Name System (DNS) servers in the system.  systemcertificate - lists the information about the current system Secure Sockets Layer (SSL) certificate.  truststore - lists the current certificate stores.  sra - command to check both secure remote assistance status and the time of the last login.  syslogserver - lists the syslog servers that are configured on the clustered system.  emailserver - lists the email servers that are configured on the system.  emailuser - lists the Email event notification settings for all Email recipients, an individual Email recipient, or a specified type (local or support) of an Email recipient.  provisioningpolicy - lists the provisioning policies available on the system.  volumegroupsnapshot - lists the snapshot objects available on the system.  callhome - displays the status of the Call Home information that is sent to a server in the Cloud.  ip - lists the currently configured IP addresses.  portset - lists the currently configured portset on the system.  safeguardedpolicy - lists the Safeguarded policies available on the system.  mdisk - displays a concise list or a detailed view of managed disks (MDisks) visible to the system.  safeguardedpolicyschedule - displays the Safeguarded backup schedule that is associated with Safeguarded policies.  eventlog - displays the concise view of system event log  enclosurestats - lists the most recent values (averaged) of all enclosure statistics.  enclosurestatshistory - lists the history values of all enclosure statistics including power consumed, temperature in fahrenheit and temperature in celsius.  **Choices:**   - `"vol"` - `"pool"` - `"node"` - `"iog"` - `"host"` - `"hostvdiskmap"` - `"vdiskhostmap"` - `"hc"` - `"fcport"` - `"iscsiport"` - `"fc"` - `"fcmap"` - `"fcconsistgrp"` - `"rcrelationship"` - `"rcconsistgrp"` - `"vdiskcopy"` - `"targetportfc"` - `"array"` - `"system"` - `"cloudaccount"` - `"cloudaccountusage"` - `"ldapserver"` - `"drive"` - `"user"` - `"usergroup"` - `"ownershipgroup"` - `"partnership"` - `"replicationpolicy"` - `"cloudbackup"` - `"enclosurestats"` - `"cloudbackupgeneration"` - `"snapshotpolicy"` - `"snapshotpolicyschedule"` - `"volumegroup"` - `"volumegroupsnapshotpolicy"` - `"volumesnapshot"` - `"dnsserver"` - `"systemcertificate"` - `"sra"` - `"syslogserver"` - `"enclosurestatshistory"` - `"emailserver"` - `"emailuser"` - `"provisioningpolicy"` - `"volumegroupsnapshot"` - `"truststore"` - `"callhome"` - `"ip"` - `"portset"` - `"safeguardedpolicy"` - `"mdisk"` - `"safeguardedpolicyschedule"` - `"cloudimportcandidate"` - `"eventlog"` - `"all"` ← (default)   **Default:** `["all"]` |
| **log_path**  string | Path of debug log file. |
| **objectname**  string | If specified, only the instance with the *objectname* is returned. If not specified, all the instances are returned. |
| **password**  string | REST API password for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **token**  string  *added in ibm.spectrum_virtualize 1.5.0* | The authentication token to verify a user on the Spectrum Virtualize storage system.  To generate a token, use the ibm_svc_auth module. |
| **username**  string | REST API username for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_svc_info_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_info_module.md#id4)

```yaml+jinja
- name: Get volume info
  ibm.spectrum_virtualize.ibm_svc_info:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/ansible.log
    gather_subset: vol
- name: Get volume info
  ibm.spectrum_virtualize.ibm_svc_info:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/ansible.log
    objectname: volumename
    gather_subset: vol
- name: Get pool info
  ibm.spectrum_virtualize.ibm_svc_info:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/ansible.log
    gather_subset: pool
```

## [Return Values](ibm_svc_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **Array**  list / elements=dictionary | Data will be populated when *gather_subset=array* or *gather_subset=all*  Lists information for array MDisks  **Returned:** success  **Sample:** `[{"...": null}]` |
| **CallHome**  list / elements=dictionary | Data will be populated when *gather_subset=callhome* or *gather_subset=all*  Displays the status of the Call Home information that is sent to a server in the Cloud  **Returned:** success  **Sample:** `[{"...": null}]` |
| **CloudAccount**  list / elements=dictionary | Data will be populated when *gather_subset=cloudaccount* or *gather_subset=all*  Lists all the configured cloud accounts  **Returned:** success  **Sample:** `[{"...": null}]` |
| **CloudAccountUsage**  list / elements=dictionary | Data will be populated when *gather_subset=cloudaccountusage* or *gather_subset=all*  Lists the usage information about the configured cloud storage accounts  **Returned:** success  **Sample:** `[{"...": null}]` |
| **CloudBackup**  list / elements=dictionary | Data will be populated when *gather_subset=cloudbackup* or *gather_subset=all*  Lists the volumes that have cloud snapshot that enabled and volumes that have cloud snapshots in the cloud account  **Returned:** success  **Sample:** `[{"...": null}]` |
| **CloudBackupGeneration**  list / elements=dictionary | Data will be populated when *gather_subset=cloudbackupgeneration*  List any volume snapshots available on the specified volume  **Returned:** success  **Sample:** `[{"...": null}]` |
| **CloudImportCandidate**  list / elements=dictionary | Data will be populated when *gather_subset=cloudimportcandidate* or *gather_subset=all*  Lists information about systems that have data that is stored in the cloud accounts  **Returned:** success  **Sample:** `[{"...": null}]` |
| **DnsServer**  list / elements=dictionary | Data will be populated when *gather_subset=dnsserver* or *gather_subset=all*  Lists the information for any Domain Name System (DNS) servers in the system  **Returned:** success  **Sample:** `[{"...": null}]` |
| **Drive**  list / elements=dictionary | Data will be populated when *gather_subset=drive* or *gather_subset=all*  Lists the configuration information and drive vital product data (VPD)  **Returned:** success  **Sample:** `[{"...": null}]` |
| **EmailServer**  list / elements=dictionary | Data will be populated when *gather_subset=emailserver* or *gather_subset=all*  Lists the Email servers that are configured on the system  **Returned:** success  **Sample:** `[{"...": null}]` |
| **EmailUser**  list / elements=dictionary | Data will be populated when *gather_subset=emailuser* or *gather_subset=all*  Lists the Email event notification settings for all Email recipients, an individual Email recipient, or a specified type (local or support) of Email recipient  **Returned:** success  **Sample:** `[{"...": null}]` |
| **EnclosureStats**  list / elements=dictionary | Data will be populated when *gather_subset=enclosurestats* or *gather_subset=all*  Lists the most recent values (averaged) of all enclosure statistics.  **Returned:** success  **Sample:** `[{"...": null}]` |
| **EnclosureStatsHistory**  list / elements=dictionary | Data will be populated when *gather_subset=enclosurestatshistory* or *gather_subset=all*  Lists the history values of all enclosure statistics including power consumed, temperature in fahrenheit and temperature in celsius.  **Returned:** success  **Sample:** `[{"...": null}]` |
| **EventLog**  list / elements=dictionary | Data will be populated when *gather_subset=eventlog* or *gather_subset=all*  Lists information about the system event log  **Returned:** success  **Sample:** `[{"...": null}]` |
| **FCConnectivitie**  list / elements=dictionary | Data will be populated when *gather_subset=fc* or *gather_subset=all*  Lists information for FC connectivity  **Returned:** success  **Sample:** `[{"...": null}]` |
| **FCConsistgrp**  list / elements=dictionary | Data will be populated when *gather_subset=fcconsistgrp* or *gather_subset=all*  Displays a concise list or a detailed view of flash copy consistency groups  **Returned:** success  **Sample:** `[{"...": null}]` |
| **FCMap**  list / elements=dictionary | Data will be populated when *gather_subset=fcmap* or *gather_subset=all*  Lists information for FC maps  **Returned:** success  **Sample:** `[{"...": null}]` |
| **FCPort**  list / elements=dictionary | Data will be populated when *gather_subset=fcport* or *gather_subset=all*  Lists information for FC ports  **Returned:** success  **Sample:** `[{"...": null}]` |
| **Host**  list / elements=dictionary | Data will be populated when *gather_subset=host* or *gather_subset=all*  Lists information for hosts  **Returned:** success  **Sample:** `[{"...": null}]` |
| **HostCluster**  list / elements=dictionary | Data will be populated when *gather_subset=hc* or *gather_subset=all*  Lists information for host clusters  **Returned:** success  **Sample:** `[{"...": null}]` |
| **HostVdiskMap**  list / elements=dictionary | Data will be populated when *gather_subset=hostvdiskmap* or *gather_subset=all*  Lists all VDisks mapped to host ‘objectname’  **Returned:** success  **Sample:** `[{"...": null}]` |
| **IOGroup**  list / elements=dictionary | Data will be populated when *gather_subset=iog* or *gather_subset=all*  Lists information for I/O groups  **Returned:** success  **Sample:** `[{"...": null}]` |
| **IP**  list / elements=dictionary | Data will be populated when *gather_subset=ip* or *gather_subset=all*  Lists the currently configured IP addresses  **Returned:** success  **Sample:** `[{"...": null}]` |
| **iSCSIPort**  list / elements=dictionary | Data will be populated when *gather_subset=iscsiport* or *gather_subset=all*  Lists information for iSCSI ports  **Returned:** success  **Sample:** `[{"...": null}]` |
| **LdapServer**  list / elements=dictionary | Data will be populated when *gather_subset=ldapserver* or *gather_subset=all*  Lists the most recent details for all configured Lightweight Directory Access Protocol (LDAP) servers  **Returned:** success  **Sample:** `[{"...": null}]` |
| **Mdisk**  list / elements=dictionary | Data will be populated when *gather_subset=mdisk* or *gather_subset=all*  Displays a concise list or a detailed view of managed disks (MDisks) visible to the system  **Returned:** success  **Sample:** `[{"...": null}]` |
| **Node**  list / elements=dictionary | Data will be populated when *gather_subset=node* or *gather_subset=all*  Lists information for nodes  **Returned:** success  **Sample:** `[{"...": null}]` |
| **Ownershipgroup**  list / elements=dictionary | Data will be populated when *gather_subset=ownershipgroup* or *gather_subset=all*  Displays the ownership groups that are available in the system  **Returned:** success  **Sample:** `[{"...": null}]` |
| **Partnership**  list / elements=dictionary | Data will be populated when *gather_subset=partnership* or *gather_subset=all*  Lists all the clustered systems (systems) that are associated with the local system  **Returned:** success  **Sample:** `[{"...": null}]` |
| **Pool**  list / elements=dictionary | Data will be populated when *gather_subset=pool* or *gather_subset=all*  Lists information for mdiskgrps  **Returned:** success  **Sample:** `[{"...": null}]` |
| **Portset**  list / elements=dictionary | Data will be populated when *gather_subset=portset* or *gather_subset=all*  Lists the currently configured portset on the system  **Returned:** success  **Sample:** `[{"...": null}]` |
| **ProvisioningPolicy**  list / elements=dictionary | Data will be populated when *gather_subset=provisioningpolicy* or *gather_subset=all*  Lists the provisioning policies available on the system  **Returned:** success  **Sample:** `[{"...": null}]` |
| **RCConsistgrp**  list / elements=dictionary | Data will be populated when *gather_subset=rcconsistgrp* or *gather_subset=all*  Displays a concise list or a detailed view of remote copy consistency groups  **Returned:** success  **Sample:** `[{"...": null}]` |
| **RemoteCopy**  list / elements=dictionary | Data will be populated when *gather_subset=rcrelationship* or *gather_subset=all*  Lists information for remote copy relationships  **Returned:** success  **Sample:** `[{"...": null}]` |
| **ReplicationPolicy**  list / elements=dictionary | Data will be populated when *gather_subset=replicationpolicy* or *gather_subset=all*  Lists all the replication policies on the system  **Returned:** success  **Sample:** `[{"...": null}]` |
| **SafeguardedPolicy**  list / elements=dictionary | Data will be populated when *gather_subset=safeguardedpolicy* or *gather_subset=all*  Lists the Safeguarded policies available on the system  **Returned:** success  **Sample:** `[{"...": null}]` |
| **SafeguardedSchedule**  list / elements=dictionary | Data will be populated when *gather_subset=safeguardedpolicyschedule* or *gather_subset=all*  Displays the Safeguarded backup schedule that is associated with Safeguarded policies  **Returned:** success  **Sample:** `[{"...": null}]` |
| **SnapshotPolicy**  list / elements=dictionary | Data will be populated when *gather_subset=snapshotpolicy* or *gather_subset=all*  Lists all the snapshot policies on the system  **Returned:** success  **Sample:** `[{"...": null}]` |
| **SnapshotSchedule**  list / elements=dictionary | Data will be populated when *gather_subset=snapshotpolicyschedule* or *gather_subset=all*  Lists all snapshot schedules on the system  **Returned:** success  **Sample:** `[{"...": null}]` |
| **Sra**  list / elements=dictionary | Data will be populated when *gather_subset=sra* or *gather_subset=all*  Command to check both secure remote assistance status and the time of the last login  **Returned:** success  **Sample:** `[{"...": null}]` |
| **SysLogServer**  list / elements=dictionary | Data will be populated when *gather_subset=syslogserver* or *gather_subset=all*  Lists the syslog servers that are configured on the clustered system  **Returned:** success  **Sample:** `[{"...": null}]` |
| **System**  list / elements=dictionary | Data will be populated when *gather_subset=system* or *gather_subset=all*  Displays the storage system information  **Returned:** success  **Sample:** `[{"...": null}]` |
| **SystemCert**  list / elements=dictionary | Data will be populated when *gather_subset=systemcertificate* or *gather_subset=all*  Lists the information about the current system Secure Sockets Layer (SSL) certificate  **Returned:** success  **Sample:** `[{"...": null}]` |
| **TargetPortFC**  list / elements=dictionary | Data will be populated when *gather_subset=targetportfc* or *gather_subset=all*  Lists information for WWPN which is required to set up FC zoning and to display the current failover status of host I/O ports  **Returned:** success  **Sample:** `[{"...": null}]` |
| **TrustStore**  list / elements=dictionary | Data will be populated when *gather_subset=truststore* or *gather_subset=all*  Lists the current certificate stores  **Returned:** success  **Sample:** `[{"...": null}]` |
| **User**  list / elements=dictionary | Data will be populated when *gather_subset=user* or *gather_subset=all*  Lists all the users that are created on the system  **Returned:** success  **Sample:** `[{"...": null}]` |
| **UserGrp**  list / elements=dictionary | Data will be populated when *gather_subset=usergroup* or *gather_subset=all*  Lists the user groups that is created on the system  **Returned:** success  **Sample:** `[{"...": null}]` |
| **VdiskCopy**  list / elements=dictionary | Data will be populated when *gather_subset=vdiskcopy* or *gather_subset=all*  Lists information for volume copy  **Returned:** success  **Sample:** `[{"...": null}]` |
| **VdiskHostMap**  list / elements=dictionary | Data will be populated when *gather_subset=vdiskhostmap* or *gather_subset=all*  Lists all hosts the VDisk ‘objectname’ is mapped to  **Returned:** success  **Sample:** `[{"...": null}]` |
| **Volume**  list / elements=dictionary | Data will be populated when *gather_subset=vol* or *gather_subset=all*  Lists information for VDisks  **Returned:** success  **Sample:** `[{"...": null}]` |
| **VolumeGroup**  list / elements=dictionary | Data will be populated when *gather_subset=volumegroup* or *gather_subset=all*  Lists all volume groups on the system  **Returned:** success  **Sample:** `[{"...": null}]` |
| **VolumeGroupSnapshot**  list / elements=dictionary | Data will be populated when *gather_subset=volumegroupsnapshot* or *gather_subset=all*  Lists the snapshot objects available on the system based on volume group  **Returned:** success  **Sample:** `[{"...": null}]` |
| **VolumeGroupSnapshotPolicy**  list / elements=dictionary | Data will be populated when *gather_subset=volumegroupsnapshotpolicy* or *gather_subset=all*  Lists view snapshot objects on the system  **Returned:** success  **Sample:** `[{"...": null}]` |
| **VolumeSnapshot**  list / elements=dictionary | Data will be populated when *gather_subset=volumesnapshot* or *gather_subset=all*  Lists all volume snapshots  **Returned:** success  **Sample:** `[{"...": null}]` |

### Authors

- Peng Wang (@wangpww)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.spectrum_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.spectrum_virtualize)
