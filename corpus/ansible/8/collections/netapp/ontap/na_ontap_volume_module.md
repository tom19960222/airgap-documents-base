---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_volume module – NetApp ONTAP manage volumes."
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_volume_module.html
fetched_at: 2026-07-28T02:43:33+00:00
---
# netapp.ontap.na_ontap_volume module – NetApp ONTAP manage volumes.

> **Note:**
>
> This module is part of the [netapp.ontap collection](https://galaxy.ansible.com/ui/repo/published/netapp/ontap/) (version 22.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.ontap`.
> You need further requirements to be able to use this module,
> see [Requirements](na_ontap_volume_module.md#ansible-collections-netapp-ontap-na-ontap-volume-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_volume`.

New in netapp.ontap 2.6.0

- [Synopsis](na_ontap_volume_module.md#synopsis)
- [Requirements](na_ontap_volume_module.md#requirements)
- [Parameters](na_ontap_volume_module.md#parameters)
- [Notes](na_ontap_volume_module.md#notes)
- [Examples](na_ontap_volume_module.md#examples)

## [Synopsis](na_ontap_volume_module.md#id1)

- Create or destroy or modify volumes on NetApp ONTAP.

## [Requirements](na_ontap_volume_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_volume_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aggr_list**  list / elements=string  *added in netapp.ontap 2.8.0* | an array of names of aggregates to be used for FlexGroup constituents. |
| **aggr_list_multiplier**  integer  *added in netapp.ontap 2.8.0* | The number of times to iterate over the aggregates listed with the aggr_list parameter when creating a FlexGroup. |
| **aggregate_name**  string | The name of the aggregate the flexvol should exist on.  Cannot be set when using the na_application_template option. |
| **analytics**  string  *added in netapp.ontap 22.0.0* | Set file system analytics state of the volume.  Only supported with REST and requires ONTAP 9.8 or later version.  Cannot enable analytics for volume that contains luns.  **Choices:**   - `"on"` - `"off"` |
| **atime_update**  boolean  *added in netapp.ontap 2.8.0* | This is an advanced option, the default is True.  If false, prevent the update of inode access times when a file is read.  This value is useful for volumes with extremely high read traffic, since it prevents writes to the inode file for the volume from contending with reads from other files.  This field should be used carefully.  That is, use this field when you know in advance that the correct access time for inodes will not be needed for files on that volume.  This option is supported in REST for ONTAP 9.8 or later with ONTAP collection version 22.8.0 or later.  **Choices:**   - `false` - `true` |
| **auto_provision_as**  string  *added in netapp.ontap 2.8.0* | Automatically provision a FlexGroup volume.  **Choices:**   - `"flexgroup"` |
| **auto_remap_luns**  boolean  *added in netapp.ontap 20.6.0* | Flag to control automatic map of LUNs.  **Choices:**   - `false` - `true` |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **check_interval**  integer  *added in netapp.ontap 20.6.0* | The amount of time in seconds to wait between checks of a volume to see if it has moved successfully.  **Default:** `30` |
| **comment**  string  *added in netapp.ontap 2.9.0* | Sets a comment associated with the volume. |
| **compression**  boolean  *added in netapp.ontap 20.12.0* | Whether to enable compression for the volume (HDD and Flash Pool aggregates).  If this option is not present, it is automatically set to true if inline_compression is true.  **Choices:**   - `false` - `true` |
| **cutover_action**  string  *added in netapp.ontap 20.5.0* | Specifies the action to be taken for cutover.  Possible values are ‘abort_on_failure’, ‘defer_on_failure’, ‘force’ and ‘wait’. Default is ‘defer_on_failure’.  **Choices:**   - `"abort_on_failure"` - `"defer_on_failure"` - `"force"` - `"wait"` |
| **efficiency_policy**  string  *added in netapp.ontap 2.7.0* | Allows a storage efficiency policy to be set on volume creation. |
| **encrypt**  boolean  *added in netapp.ontap 2.7.0* | Whether or not to enable Volume Encryption.  If not present, ONTAP defaults to false at volume creation.  Changing encrypt value after creation requires ONTAP 9.3 or later.  **Choices:**   - `false` - `true` |
| **export_policy**  aliases: policy  string | Name of the export policy.  Mutually exclusive with nfs_access suboption in nas_application_template. |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **force_restore**  boolean  *added in netapp.ontap 20.6.0* | If this field is set to “true”, the Snapshot copy is restored even if the volume has one or more newer Snapshot copies which are currently used as reference Snapshot copy by SnapMirror. If a restore is done in this situation, this will cause future SnapMirror transfers to fail.  Option should only be used along with snapshot_restore.  **Choices:**   - `false` - `true` |
| **force_unmap_luns**  boolean  *added in netapp.ontap 20.6.0* | Flag to control automatic unmap of LUNs.  **Choices:**   - `false` - `true` |
| **from_name**  string  *added in netapp.ontap 2.7.0* | Name of the existing volume to be renamed to name. |
| **from_vserver**  string  *added in netapp.ontap 20.6.0* | The source vserver of the volume is rehosted. |
| **group_id**  integer  *added in netapp.ontap 20.1.0* | The UNIX group ID for the volume. The default value is 0 (‘root’). |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **inline_compression**  boolean  *added in netapp.ontap 20.12.0* | Whether to enable inline compression for the volume (HDD and Flash Pool aggregates, AFF platforms).  **Choices:**   - `false` - `true` |
| **is_infinite**  boolean | Set True if the volume is an Infinite Volume.  Deleting an infinite volume is asynchronous.  **Choices:**   - `false` ← (default) - `true` |
| **is_online**  boolean | Whether the specified volume is online, or not.  **Choices:**   - `false` - `true` ← (default) |
| **junction_path**  string | Junction path of the volume.  To unmount, use junction path `''`. |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **language**  string  *added in netapp.ontap 2.8.0* | Language to use for Volume  Default uses SVM language  Possible values Language  c POSIX  ar Arabic  cs Czech  da Danish  de German  en English  en_us English (US)  es Spanish  fi Finnish  fr French  he Hebrew  hr Croatian  hu Hungarian  it Italian  ja Japanese euc-j  ja_v1 Japanese euc-j  ja_jp.pck Japanese PCK (sjis)  ja_jp.932 Japanese cp932  ja_jp.pck_v2 Japanese PCK (sjis)  ko Korean  no Norwegian  nl Dutch  pl Polish  pt Portuguese  ro Romanian  ru Russian  sk Slovak  sl Slovenian  sv Swedish  tr Turkish  zh Simplified Chinese  zh.gbk Simplified Chinese (GBK)  zh_tw Traditional Chinese euc-tw  zh_tw.big5 Traditional Chinese Big 5  To use UTF-8 as the NFS character set, append ‘.UTF-8’ to the language code |
| **logical_space_enforcement**  boolean  *added in netapp.ontap 20.16.0* | This optionally specifies whether to perform logical space accounting on the volume. When space is enforced logically, ONTAP enforces volume settings such that all the physical space saved by the storage efficiency features will be calculated as used.  This is only supported with REST.  **Choices:**   - `false` - `true` |
| **logical_space_reporting**  boolean  *added in netapp.ontap 20.16.0* | This optionally specifies whether to report space logically on the volume. When space is reported logically, ONTAP reports the volume space such that all the physical space saved by the storage efficiency features are also reported as used.  This is only supported with REST.  **Choices:**   - `false` - `true` |
| **max_files**  integer  *added in netapp.ontap 20.18.0* | The maximum number of files (inodes) for user-visible data allowed on the volume.  Note - ONTAP allocates a slightly different value, for instance 3990 when asking for 4000. Tp preserve idempotency, small variations in size are ignored. |
| **max_wait_time**  integer  *added in netapp.ontap 22.0.0* | Volume move and encryption operations might take longer time to complete.  With `wait_for_completion` set, module will wait for time set in this option for volume move and encryption to complete.  If time exipres, module exit and the operation may still be running.  Default is set to 10 minutes.  **Default:** `600` |
| **name**  string / required | The name of the volume to manage. |
| **nas_application_template**  dictionary  *added in netapp.ontap 20.12.0* | additional options when using the application/applications REST API to create a volume.  the module is using ZAPI by default, and switches to REST if any suboption is present.  create a FlexVol by default.  create a FlexGroup if `auto_provision_as` is set and `FlexCache` option is not present.  create a FlexCache if `flexcache` option is present. |
| **cifs_access**  list / elements=dictionary | The list of CIFS access controls. You must provide *user_or_group* or *access* to enable CIFS access. |
| **access**  string | The CIFS access granted to the user or group. Default is full_control.  **Choices:**   - `"change"` - `"full_control"` - `"no_access"` - `"read"` |
| **user_or_group**  string | The name of the CIFS user or group that will be granted access. Default is Everyone. |
| **exclude_aggregates**  list / elements=string  *added in netapp.ontap 21.7.0* | The list of aggregate names to exclude when creating a volume.  Requires ONTAP 9.9.1 GA or later. |
| **flexcache**  dictionary | whether to create a flexcache. If absent, a FlexVol or FlexGroup is created. |
| **dr_cache**  boolean  *added in netapp.ontap 21.3.0* | whether to use the same flexgroup msid as the origin.  requires ONTAP 9.9 and REST.  create only option, ignored if the flexcache already exists.  **Choices:**   - `false` - `true` |
| **origin_component_name**  string / required | the remote component for the flexcache. |
| **origin_svm_name**  string / required | the remote SVM for the flexcache. |
| **nfs_access**  list / elements=dictionary | The list of NFS access controls. You must provide *host* or *access* to enable NFS access.  Mutually exclusive with export_policy option. |
| **access**  string | The NFS access granted. Default is rw.  **Choices:**   - `"none"` - `"ro"` - `"rw"` |
| **host**  string | The name of the NFS entity granted access. Default is 0.0.0.0/0. |
| **storage_service**  string | The performance service level (PSL) for this volume  **Choices:**   - `"value"` - `"performance"` - `"extreme"` |
| **tiering**  dictionary | Cloud tiering policy (see `tiering_policy` for a more complete description). |
| **control**  string | Storage tiering placement rules for the container.  **Choices:**   - `"required"` - `"best_effort"` - `"disallowed"` |
| **object_stores**  list / elements=string | list of object store names for tiering. |
| **policy**  string | Cloud tiering policy (see `tiering_policy`).  Must match `tiering_policy` if both are present.  **Choices:**   - `"all"` - `"auto"` - `"none"` - `"snapshot-only"` |
| **use_nas_application**  boolean | Whether to use the application/applications REST/API to create a volume.  This will default to true if any other suboption is present.  **Choices:**   - `false` - `true` ← (default) |
| **nvfail_enabled**  boolean  *added in netapp.ontap 2.9.0* | If true, the controller performs additional work at boot and takeover times if it finds that there has been any potential data loss in the volume’s constituents due to an NVRAM failure.  The volume’s constituents would be put in a special state called ‘in-nvfailed-state’ such that protocol access is blocked.  This will cause the client applications to crash and thus prevent access to stale data.  To get out of this situation, the admin needs to manually clear the ‘in-nvfailed-state’ on the volume’s constituents.  **Choices:**   - `false` - `true` |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **percent_snapshot_space**  integer | Amount of space reserved for snapshot copies of the volume. |
| **preserve_lun_ids**  boolean  *added in netapp.ontap 20.6.0* | If this field is set to “true”, LUNs in the volume being restored will remain mapped and their identities preserved such that host connectivity will not be disrupted during the restore operation. I/O’s to the LUN will be fenced during the restore operation by placing the LUNs in an unavailable state. Once the restore operation has completed, hosts will be able to resume I/O access to the LUNs.  Option should only be used along with snapshot_restore.  **Choices:**   - `false` - `true` |
| **qos_adaptive_policy_group**  string  *added in netapp.ontap 2.9.0* | Specifies a QoS adaptive policy group to be set on volume. |
| **qos_policy_group**  string  *added in netapp.ontap 2.9.0* | Specifies a QoS policy group to be set on volume. |
| **size**  integer | The size of the volume in (size_unit). Required when `state=present`. |
| **size_change_threshold**  integer  *added in netapp.ontap 20.12.0* | Percentage in size change to trigger a resize.  When this parameter is greater than 0, a difference in size between what is expected and what is configured is ignored if it is below the threshold.  For instance, the nas application allocates a larger size than specified to account for overhead.  Set this to 0 for an exact match.  **Default:** `10` |
| **size_unit**  string | The unit used to interpret the size parameter.  **Choices:**   - `"bytes"` - `"b"` - `"kb"` - `"mb"` - `"gb"` ← (default) - `"tb"` - `"pb"` - `"eb"` - `"zb"` - `"yb"` |
| **sizing_method**  string  *added in netapp.ontap 20.12.0* | Represents the method to modify the size of a FlexGroup.  use_existing_resources - Increases or decreases the size of the FlexGroup by increasing or decreasing the size of the current FlexGroup resources.  add_new_resources - Increases the size of the FlexGroup by adding new resources. This is limited to two new resources per available aggregate.  This is only supported if REST is enabled (ONTAP 9.6 or later) and only for FlexGroups. ONTAP defaults to use_existing_resources.  **Choices:**   - `"add_new_resources"` - `"use_existing_resources"` |
| **snapdir_access**  boolean  *added in netapp.ontap 2.8.0* | This is an advanced option, the default is False.  Enable the visible ‘.snapshot’ directory that is normally present at system internal mount points.  This value also turns on access to all other ‘.snapshot’ directories in the volume.  This option is supported in REST for ONTAP 9.13.1 or later with ONTAP collection version 22.8.0 or later.  **Choices:**   - `false` - `true` |
| **snaplock**  dictionary  *added in netapp.ontap 21.18.0* | Starting with ONTAP 9.10.1, snaplock.type is set at the volume level.  The other suboptions can be set or modified when using REST on earlier versions of ONTAP.  This option and suboptions are only supported with REST. |
| **append_mode_enabled**  boolean | when enabled, all the files created with write permissions on the volume are, by default, WORM appendable files. The user can append the data to a WORM appendable file but cannot modify the existing contents of the file nor delete the file until it expires.  **Choices:**   - `false` - `true` |
| **autocommit_period**  string | autocommit period for SnapLock volume. All files which are not modified for a period greater than the autocommit period of the volume are committed to the WORM state.  duration is in the ISO-8601 duration format (eg PY, PM, PD, PTH, PTM).  examples P30M, P10Y, PT1H, “none”. A duration that combines different periods is not supported. |
| **privileged_delete**  string | privileged-delete attribute of a SnapLock volume.  On a SnapLock Enterprise (SLE) volume, a designated privileged user can selectively delete files irrespective of the retention time of the file.  On a SnapLock Compliance (SLC) volume, it is always permanently_disabled.  **Choices:**   - `"disabled"` - `"enabled"` - `"permanently_disabled"` |
| **retention**  dictionary | default, maximum, and minumum retention periods for files committed to the WORM state on the volume.  durations are in the ISO-8601 duration format, see autocommit_period. |
| **default**  string | default retention period that is applied to files while committing them to the WORM state without an associated retention period. |
| **maximum**  string | maximum allowed retention period for files committed to the WORM state on the volume. |
| **minimum**  string | minimum allowed retention period for files committed to the WORM state on the volume. |
| **type**  string | The SnapLock type of the volume.  compliance - A SnapLock Compliance (SLC) volume provides the highest level of WORM protection and an administrator cannot destroy a SLC volume if it contains unexpired WORM files.  enterprise - An administrator can delete a SnapLock Enterprise (SLE) volume.  non_snaplock - Indicates the volume is non-snaplock.  **Choices:**   - `"compliance"` - `"enterprise"` - `"non_snaplock"` |
| **snapshot_auto_delete**  dictionary  *added in netapp.ontap 20.4.0* | A dictionary for the auto delete options and values.  Supported options include ‘state’, ‘commitment’, ‘trigger’, ‘target_free_space’, ‘delete_order’, ‘defer_delete’, ‘prefix’, ‘destroy_list’.  All the above mentioned options except ‘destroy_list’ are supported in REST for ONTAP 9.13.1 or later with ONTAP collection version 22.8.0 or later.  Option ‘state’ determines if the snapshot autodelete is currently enabled for the volume. Possible values are ‘on’ and ‘off’.  Option ‘commitment’ determines the snapshots which snapshot autodelete is allowed to delete to get back space. Possible values are ‘try’, ‘disrupt’ and ‘destroy’.  Option ‘trigger’ determines the condition which starts the automatic deletion of snapshots. Possible values are ‘volume’, ‘snap_reserve’ and DEPRECATED ‘space_reserve’.  Option ‘target_free_space’ determines when snapshot autodelete should stop deleting snapshots. Depending on the trigger, snapshots are deleted till we reach the target free space percentage. Accepts int type.  Option ‘delete_order’ determines if the oldest or newest snapshot is deleted first. Possible values are ‘newest_first’ and ‘oldest_first’.  Option ‘defer_delete’ determines which kind of snapshots to delete in the end. Possible values are ‘scheduled’, ‘user_created’, ‘prefix’ and ‘none’.  Option ‘prefix’ can be set to provide the prefix string for the ‘prefix’ value of the ‘defer_delete’ option. The prefix string length can be 15 char long.  Option ‘destroy_list’ is a comma seperated list of services which can be destroyed if the snapshot backing that service is deleted. For 7-mode, the possible values for this option are a combination of ‘lun_clone’, ‘vol_clone’, ‘cifs_share’, ‘file_clone’ or ‘none’. For cluster-mode, the possible values for this option are a combination of ‘lun_clone,file_clone’ (for LUN clone and/or file clone), ‘lun_clone,sfsr’ (for LUN clone and/or sfsr), ‘vol_clone’, ‘cifs_share’, or ‘none’. |
| **snapshot_policy**  string  *added in netapp.ontap 2.8.0* | The name of the snapshot policy.  The default policy name is ‘default’.  If present, this will set the protection_type when using `nas_application_template`. |
| **snapshot_restore**  string  *added in netapp.ontap 20.6.0* | Name of snapshot to restore from.  Not supported on Infinite Volume. |
| **space_guarantee**  string | Space guarantee style for the volume.  The file setting is no longer supported.  **Choices:**   - `"none"` - `"file"` - `"volume"` |
| **space_slo**  string  *added in netapp.ontap 2.9.0* | Specifies the space SLO type for the volume. The space SLO type is the Service Level Objective for space management for the volume.  The space SLO value is used to enforce existing volume settings so that sufficient space is set aside on the aggregate to meet the space SLO.  This parameter is not supported on Infinite Volumes.  **Choices:**   - `"none"` - `"thick"` - `"semi-thick"` |
| **state**  string | Whether the specified volume should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string  *added in netapp.ontap 22.6.0* | Tags are an optional way to track the uses of a resource.  Tag values must be formatted as key:value strings, example [“team:csi”, “environment:test”] |
| **tiering_minimum_cooling_days**  integer  *added in netapp.ontap 20.16.0* | Determines how many days must pass before inactive data in a volume using the Auto or Snapshot-Only policy is considered cold and eligible for tiering.  This option is only supported in REST 9.8 or later. |
| **tiering_policy**  string  *added in netapp.ontap 2.9.0* | The tiering policy that is to be associated with the volume.  This policy decides whether the blocks of a volume will be tiered to the capacity tier.  snapshot-only policy allows tiering of only the volume snapshot copies not associated with the active file system.  auto policy allows tiering of both snapshot and active file system user data to the capacity tier.  backup policy on DP volumes allows all transferred user data blocks to start in the capacity tier.  all is the REST equivalent for backup.  When set to none, the Volume blocks will not be tiered to the capacity tier.  If no value specified, the volume is assigned snapshot only by default.  Requires ONTAP 9.4 or later.  **Choices:**   - `"snapshot-only"` - `"auto"` - `"backup"` - `"none"` - `"all"` |
| **time_out**  integer  *added in netapp.ontap 2.8.0* | With ZAPI - time to wait for Flexgroup creation, modification, or deletion in seconds.  With REST - time to wait for any volume creation, modification, or deletion in seconds.  Error out if task is not completed in defined time.  With ZAPI - if 0, the request is asynchronous.  Default is set to 3 minutes.  Use `max_wait_time` and `wait_for_completion` for volume move and encryption operations.  **Default:** `180` |
| **type**  string | The volume type, either read-write (RW) or data-protection (DP). |
| **unix_permissions**  string  *added in netapp.ontap 2.8.0* | Unix permission bits in octal or symbolic format.  For example, 0 is equivalent to ————, 777 is equivalent to —rwxrwxrwx,both formats are accepted.  The valid octal value ranges between 0 and 777 inclusive. |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **user_id**  integer  *added in netapp.ontap 20.1.0* | The UNIX user ID for the volume. The default value is 0 (‘root’). |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **vol_full_threshold_percent**  integer  *added in netapp.ontap 22.8.0* | Specifies the percentage at which the volume is considered full, and above which a critical EMS error will be generated.  The default value is 98%. The maximum value for this option is 100%.  Setting this threshold to 0 disables the volume full space alerts.  Supported only with in REST for ONTAP 9.9 or later. |
| **vol_nearly_full_threshold_percent**  integer  *added in netapp.ontap 22.8.0* | Specifies the percentage at which the volume is considered nearly full, and above which an EMS warning will be generated.  The default value is 95%. The maximum value for this option is 99%.  Setting this threshold to 0 disables the volume nearly full space alerts.  Supported only with in REST for ONTAP 9.9 or later. |
| **volume_security_style**  string | The security style associated with this volume.  **Choices:**   - `"mixed"` - `"ntfs"` - `"unified"` - `"unix"` |
| **vserver**  string / required | Name of the vserver to use. |
| **vserver_dr_protection**  string  *added in netapp.ontap 2.9.0* | Specifies the protection type for the volume in a Vserver DR setup.  **Choices:**   - `"protected"` - `"unprotected"` |
| **wait_for_completion**  boolean  *added in netapp.ontap 2.8.0* | Set this parameter to ‘true’ for synchronous execution during create (wait until volume status is online)  Set this parameter to ‘false’ for asynchronous execution  For asynchronous, execution exits as soon as the request is sent, without checking volume status  **Choices:**   - `false` ← (default) - `true` |

## [Notes](na_ontap_volume_module.md#id4)

> **Note:**
>
> - supports REST and ZAPI. REST requires ONTAP 9.6 or later. Efficiency with REST requires ONTAP 9.7 or later.
> - REST is enabled when `use_rest` is set to always.
> - The feature_flag `warn_or_fail_on_fabricpool_backend_change` controls whether an error is reported when tiering control would require or disallow FabricPool for an existing volume with a different backend. Allowed values are fail, warn, and ignore, and the default is set to fail.
> - snapshot_restore is not idempotent, it always restores.
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_volume_module.md#id5)

```yaml+jinja
- name: Create FlexVol
  netapp.ontap.na_ontap_volume:
    state: present
    name: ansibleVolume12
    is_infinite: False
    aggregate_name: ansible_aggr
    size: 100
    size_unit: mb
    user_id: 1001
    group_id: 2002
    space_guarantee: none
    tiering_policy: auto
    export_policy: default
    percent_snapshot_space: 60
    qos_policy_group: max_performance_gold
    vserver: ansibleVServer
    wait_for_completion: True
    space_slo: none
    nvfail_enabled: False
    comment: ansible created volume
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Volume Delete
  netapp.ontap.na_ontap_volume:
    state: absent
    name: ansibleVolume12
    aggregate_name: ansible_aggr
    vserver: ansibleVServer
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Make FlexVol offline
  netapp.ontap.na_ontap_volume:
    state: present
    name: ansibleVolume
    is_infinite: False
    is_online: False
    vserver: ansibleVServer
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Create Flexgroup volume manually
  netapp.ontap.na_ontap_volume:
    state: present
    name: ansibleVolume
    is_infinite: False
    aggr_list: "{{ aggr_list }}"
    aggr_list_multiplier: 2
    size: 200
    size_unit: mb
    space_guarantee: none
    export_policy: default
    vserver: "{{ vserver }}"
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    https: False
    unix_permissions: 777
    snapshot_policy: default
    time_out: 0

- name: Create Flexgroup volume auto provsion as flex group
  netapp.ontap.na_ontap_volume:
    state: present
    name: ansibleVolume
    is_infinite: False
    auto_provision_as: flexgroup
    size: 200
    size_unit: mb
    space_guarantee: none
    export_policy: default
    vserver: "{{ vserver }}"
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    https: False
    unix_permissions: 777
    snapshot_policy: default
    time_out: 0

- name: Create FlexVol with QoS adaptive
  netapp.ontap.na_ontap_volume:
    state: present
    name: ansibleVolume15
    is_infinite: False
    aggregate_name: ansible_aggr
    size: 100
    size_unit: gb
    space_guarantee: none
    export_policy: default
    percent_snapshot_space: 10
    qos_adaptive_policy_group: extreme
    vserver: ansibleVServer
    wait_for_completion: True
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Modify volume dr protection (vserver of the volume must be in a snapmirror relationship)
  netapp.ontap.na_ontap_volume:
    state: present
    name: ansibleVolume
    vserver_dr_protection: protected
    vserver: "{{ vserver }}"
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    https: False

- name: Modify volume with snapshot auto delete options
  netapp.ontap.na_ontap_volume:
    state: present
    name: vol_auto_delete
    snapshot_auto_delete:
      state: "on"
      commitment: try
      defer_delete: scheduled
      target_free_space: 30
      destroy_list: lun_clone,vol_clone
      delete_order: newest_first
    aggregate_name: "{{ aggr }}"
    vserver: "{{ vserver }}"
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    https: False

- name: Move volume with force cutover action
  netapp.ontap.na_ontap_volume:
    name: ansible_vol
    aggregate_name: aggr_ansible
    cutover_action: force
    vserver: "{{ vserver }}"
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    https: false

- name: Rehost volume to another vserver auto remap luns
  netapp.ontap.na_ontap_volume:
    name: ansible_vol
    from_vserver: ansible
    auto_remap_luns: true
    vserver: "{{ vserver }}"
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    https: false

- name: Rehost volume to another vserver force unmap luns
  netapp.ontap.na_ontap_volume:
    name: ansible_vol
    from_vserver: ansible
    force_unmap_luns: true
    vserver: "{{ vserver }}"
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    https: false

- name: Snapshot restore volume
  netapp.ontap.na_ontap_volume:
    name: ansible_vol
    vserver: ansible
    snapshot_restore: 2020-05-24-weekly
    force_restore: true
    preserve_lun_ids: true
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    https: true
    validate_certs: false

- name: Volume create using application/applications nas template
  netapp.ontap.na_ontap_volume:
    state: present
    name: ansibleVolume12
    vserver: ansibleSVM
    size: 100000000
    size_unit: b
    space_guarantee: none
    language: es
    percent_snapshot_space: 60
    unix_permissions: ---rwxrwxrwx
    snapshot_policy: default
    efficiency_policy: default
    comment: testing
    nas_application_template:
      nfs_access:   # the mere presence of a suboption is enough to enable this new feature
        - access: ro
        - access: rw
          host: 10.0.0.0/8
      exclude_aggregates: aggr0
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    https: true
    validate_certs: false

# requires Ontap collection version - 21.24.0 to use iso filter plugin.
- name: volume create with snaplock set.
  netapp.ontap.na_ontap_volume:
    state: present
    name: "{{ snaplock_volume }}"
    aggregate_name: "{{ aggregate }}"
    size: 20
    size_unit: mb
    space_guarantee: none
    policy: default
    type: rw
    snaplock:
      type: enterprise
      retention:
        default: "{{ 60 | netapp.ontap.iso8601_duration_from_seconds }}"

- name: Create volume with snapshot-auto-delete options - REST
  netapp.ontap.na_ontap_volume:
    state: present
    name: test_vol
    aggregate_name: "{{ aggr }}"
    size: 20
    size_unit: mb
    snapshot_auto_delete:
      state: 'on'
      trigger: volume
      delete_order: "oldest_first"
      defer_delete: "user_created"
      commitment: "try"
      target_free_space: 30
      prefix: "my_prefix"
    wait_for_completion: true

- name: Modify volume - REST
  netapp.ontap.na_ontap_volume:
    state: present
    name: test_vol
    aggregate_name: "{{ aggr }}"
    snapdir_access: false
    snapshot_auto_delete:
      state: 'on'
      target_free_space: 25
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
