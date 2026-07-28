---
collection: ansible
version: "6"
title: "netapp.ontap.na_ontap_aggregate module – NetApp ONTAP manage aggregates."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/ontap/na_ontap_aggregate_module.html
fetched_at: 2026-07-28T00:11:59+00:00
---
# netapp.ontap.na_ontap_aggregate module – NetApp ONTAP manage aggregates.

> **Note:**
>
> This module is part of the [netapp.ontap collection](https://galaxy.ansible.com/netapp/ontap) (version 21.24.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.ontap`.
> You need further requirements to be able to use this module,
> see [Requirements](na_ontap_aggregate_module.md#ansible-collections-netapp-ontap-na-ontap-aggregate-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_aggregate`.

New in netapp.ontap 2.6.0

- [Synopsis](na_ontap_aggregate_module.md#synopsis)
- [Requirements](na_ontap_aggregate_module.md#requirements)
- [Parameters](na_ontap_aggregate_module.md#parameters)
- [Notes](na_ontap_aggregate_module.md#notes)
- [Examples](na_ontap_aggregate_module.md#examples)

## [Synopsis](na_ontap_aggregate_module.md#id1)

- Create, delete, or manage aggregates on ONTAP.

## [Requirements](na_ontap_aggregate_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_aggregate_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **disk_class**  string  added in netapp.ontap 21.16.0 | Class of disk to use to build aggregate.  `capacity_flash` is listed in swagger, but rejected as invalid by ONTAP.  Choices:   - `"capacity"` - `"performance"` - `"archive"` - `"solid_state"` - `"array"` - `"virtual"` - `"data_center"` - `"capacity_flash"` |
| **disk_count**  integer | Number of disks to place into the aggregate, including parity disks.  The disks in this newly-created aggregate come from the spare disk pool.  The smallest disks in this pool join the aggregate first, unless the `disk-size` argument is provided.  Either `disk-count` or `disks` must be supplied. Range [0..2^31-1].  Required when `state=present`.  Modifiable only if specified disk_count is larger than current disk_count.  Cannot create raidgroup with 1 disk when using raid type raid4.  If the disk_count % raid_size == 1, only disk_count/raid_size \* raid_size will be added.  If disk_count is 6, raid_type is raid4, raid_size 4, all 6 disks will be added.  If disk_count is 5, raid_type is raid4, raid_size 4, 5/4 \* 4 = 4 will be added. 1 will not be added.  With REST, `nodes` is required if `disk_count` is present. |
| **disk_size**  integer  added in netapp.ontap 2.7.0 | Disk size to use in 4K block size. Disks within 10% of specified size will be used.  With REST, this is converted to bytes using 4096. Use `disk_size_with_unit` to skip the conversion. |
| **disk_size_with_unit**  string | Disk size to use in the specified unit.  It is a positive integer number followed by unit of T/G/M/K. For example, 72G, 1T and 32M.  Or the unit can be omitted for bytes (REST also accepts B).  This option is ignored if a specific list of disks is specified through the “disks” parameter.  You must only use one of either “disk-size” or “disk-size-with-unit” parameters.  With REST, this is converted to bytes, assuming K=1024. |
| **disk_type**  string  added in netapp.ontap 2.7.0 | Type of disk to use to build aggregate.  Not supported with REST - see `disk_class`.  SSD-NVM, SSD-CAP were added with ONTAP 9.6.  VMLUN was added with ONTAP 9.9.  Choices:   - `"ATA"` - `"BSAS"` - `"FCAL"` - `"FSAS"` - `"LUN"` - `"MSATA"` - `"SAS"` - `"SSD"` - `"SSD-CAP"` - `"SSD-NVM"` - `"VMDISK"` - `"VMLUN"` - `"VMLUN-SSD"` |
| **disks**  list / elements=string  added in netapp.ontap 2.8.0 | Specific list of disks to use for the new aggregate.  To create a “mirrored” aggregate with a specific list of disks, both ‘disks’ and ‘mirror_disks’ options must be supplied. Additionally, the same number of disks must be supplied in both lists.  Not supported with REST. |
| **encryption**  boolean  added in netapp.ontap 21.14.0 | whether to enable software encryption.  this is equivalent to -encrypt-with-aggr-key when using the CLI.  requires a VE license.  Choices:   - `false` - `true` |
| **feature_flags**  dictionary  added in netapp.ontap 20.5.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  added in netapp.ontap 21.23.0 | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **from_name**  string  added in netapp.ontap 2.7.0 | Name of the aggregate to be renamed. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  Choices:   - `false` ← (default) - `true` |
| **ignore_pool_checks**  boolean  added in netapp.ontap 20.8.0 | only valid when *disks* option is used.  disks in a plex should belong to the same spare pool, and mirror disks to another spare pool.  when set to true, these checks are ignored.  Ignored with REST as *disks* is not supported.  Choices:   - `false` - `true` |
| **is_mirrored**  boolean  added in netapp.ontap 2.8.0 | Specifies that the new aggregate be mirrored (have two plexes).  If set to true, then the indicated disks will be split across the two plexes. By default, the new aggregate will not be mirrored.  This option cannot be used when a specific list of disks is supplied with either the ‘disks’ or ‘mirror_disks’ options.  Choices:   - `false` - `true` |
| **key_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client key file. |
| **mirror_disks**  list / elements=string  added in netapp.ontap 2.8.0 | List of mirror disks to use. It must contain the same number of disks specified in ‘disks’.  Not supported with REST. |
| **name**  string / required | The name of the aggregate to manage. |
| **nodes**  list / elements=string | Node(s) for the aggregate to be created on. If no node specified, mgmt lif home will be used.  ZAPI only - if multiple nodes specified an aggr stripe will be made.  With REST, only one node can be specified. If disk_count is present, node name is required. |
| **object_store_name**  string  added in netapp.ontap 2.9.0 | Name of the object store configuration attached to the aggregate. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **raid_size**  integer  added in netapp.ontap 2.7.0 | Sets the maximum number of drives per raid group. |
| **raid_type**  string  added in netapp.ontap 2.7.0 | Specifies the type of RAID groups to use in the new aggregate.  raid_0 is only available on ONTAP Select.  Choices:   - `"raid4"` - `"raid_dp"` - `"raid_tec"` - `"raid_0"` |
| **service_state**  string | Whether the specified aggregate should be enabled or disabled. Creates aggregate if doesnt exist.  Not supported with REST when set to offline.  REST does not support changing the state from offline to online, and reciprocally.  Choices:   - `"online"` - `"offline"` |
| **snaplock_type**  string  added in netapp.ontap 20.1.0 | Type of snaplock for the aggregate being created.  Choices:   - `"compliance"` - `"enterprise"` - `"non_snaplock"` |
| **spare_pool**  string  added in netapp.ontap 2.8.0 | Specifies the spare pool from which to select spare disks to use in creation of a new aggregate.  Not supported with REST.  Choices:   - `"Pool0"` - `"Pool1"` |
| **state**  string | Whether the specified aggregate should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **time_out**  integer  added in netapp.ontap 2.8.0 | time to wait for aggregate creation in seconds.  default is set to 100 seconds.  Default: `100` |
| **unmount_volumes**  boolean | If set to “TRUE”, this option specifies that all of the volumes hosted by the given aggregate are to be unmounted before the offline operation is executed.  By default, the system will reject any attempt to offline an aggregate that hosts one or more online volumes.  Ignored with REST as offlining an aggregate is not supported.  Choices:   - `false` - `true` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  Default: `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **wait_for_online**  boolean  added in netapp.ontap 2.8.0 | Set this parameter to ‘true’ for synchronous execution during create (wait until aggregate status is online).  Set this parameter to ‘false’ for asynchronous execution.  For asynchronous, execution exits as soon as the request is sent, without checking aggregate status.  Ignored with REST (always wait).  Choices:   - `false` ← (default) - `true` |

## [Notes](na_ontap_aggregate_module.md#id4)

> **Note:**
>
> - supports check_mode.
> - support ZAPI and REST.
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_aggregate_module.md#id5)

```yaml+jinja
- name: Create Aggregates and wait 5 minutes until aggregate is online
  netapp.ontap.na_ontap_aggregate:
    state: present
    service_state: online
    name: ansibleAggr
    disk_count: 1
    wait_for_online: True
    time_out: 300
    snaplock_type: non_snaplock
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Manage Aggregates
  netapp.ontap.na_ontap_aggregate:
    state: present
    service_state: offline
    unmount_volumes: true
    name: ansibleAggr
    disk_count: 1
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Attach object store
  netapp.ontap.na_ontap_aggregate:
    state: present
    name: aggr4
    object_store_name: sgws_305
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Rename Aggregates
  netapp.ontap.na_ontap_aggregate:
    state: present
    service_state: online
    from_name: ansibleAggr
    name: ansibleAggr2
    disk_count: 1
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Delete Aggregates
  netapp.ontap.na_ontap_aggregate:
    state: absent
    service_state: offline
    unmount_volumes: true
    name: ansibleAggr
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
