---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_snapmirror module – NetApp ONTAP or ElementSW Manage SnapMirror"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_snapmirror_module.html
fetched_at: 2026-07-28T02:43:18+00:00
---
# netapp.ontap.na_ontap_snapmirror module – NetApp ONTAP or ElementSW Manage SnapMirror

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
> see [Requirements](na_ontap_snapmirror_module.md#ansible-collections-netapp-ontap-na-ontap-snapmirror-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_snapmirror`.

New in netapp.ontap 2.7.0

- [Synopsis](na_ontap_snapmirror_module.md#synopsis)
- [Requirements](na_ontap_snapmirror_module.md#requirements)
- [Parameters](na_ontap_snapmirror_module.md#parameters)
- [Notes](na_ontap_snapmirror_module.md#notes)
- [Examples](na_ontap_snapmirror_module.md#examples)

## [Synopsis](na_ontap_snapmirror_module.md#id1)

- Create/Delete/Update/Initialize/Break/Resync/Resume SnapMirror volume/vserver relationships for ONTAP/ONTAP
- This includes SVM replication, aka vserver DR
- Create/Delete/Update/Initialize SnapMirror volume relationship between ElementSW and ONTAP
- Modify schedule for a SnapMirror relationship for ONTAP/ONTAP and ElementSW/ONTAP
- Pre-requisite for ElementSW to ONTAP relationship or vice-versa is an established SnapMirror endpoint for ONTAP cluster with ElementSW UI
- Pre-requisite for ElementSW to ONTAP relationship or vice-versa is to have SnapMirror enabled in the ElementSW volume
- For creating a SnapMirror ElementSW/ONTAP relationship, an existing ONTAP/ElementSW relationship should be present
- Performs resync if the `relationship_state=active` and the current mirror state of the snapmirror relationship is broken-off
- Performs resume if the `relationship_state=active`, the current snapmirror relationship status is quiesced and mirror state is snapmirrored
- Performs restore if the `relationship_type=restore` and all other operations will not be performed during this task

## [Requirements](na_ontap_snapmirror_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_snapmirror_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **clean_up_failure**  boolean  *added in netapp.ontap 21.20.0* | An optional parameter to recover from an aborted or failed restore operation.  Any temporary RST relationship is removed from the destination Vserver.  Only supported with ZAPI.  **Choices:**   - `false` ← (default) - `true` |
| **connection_type**  string  *added in netapp.ontap 2.9.0* | Type of SnapMirror relationship.  Pre-requisite for either elementsw_ontap or ontap_elementsw the ElementSW volume should have enableSnapmirror option set to true.  For using ontap_elementsw, elementsw_ontap snapmirror relationship should exist.  **Choices:**   - `"ontap_ontap"` ← (default) - `"elementsw_ontap"` - `"ontap_elementsw"` |
| **create_destination**  dictionary  *added in netapp.ontap 21.1.0* | Requires ONTAP 9.7 or later.  Creates the destination volume if enabled and destination_volume is present or destination_path includes a volume name.  Creates and peers the destination vserver for SVM DR. |
| **enabled**  boolean | Whether to create the destination volume or vserver.  This is automatically enabled if any other suboption is present.  **Choices:**   - `false` - `true` ← (default) |
| **storage_service**  dictionary | storage service associated with the destination endpoint. |
| **enabled**  boolean | whether to create the destination endpoint using storage service.  **Choices:**   - `false` - `true` |
| **enforce_performance**  boolean | whether to enforce storage service performance on the destination endpoint.  **Choices:**   - `false` - `true` |
| **name**  string | the performance service level (PSL) for this volume endpoint.  **Choices:**   - `"value"` - `"performance"` - `"extreme"` |
| **tiering**  dictionary | Cloud tiering policy. |
| **policy**  string | Cloud tiering policy.  **Choices:**   - `"all"` - `"auto"` - `"none"` - `"snapshot-only"` |
| **supported**  boolean | enable provisioning of the destination endpoint volumes on FabricPool aggregates.  only supported for FlexVol volume, FlexGroup volume, and Consistency Group endpoints.  **Choices:**   - `false` - `true` |
| **destination_cluster**  string  *added in netapp.ontap 21.1.0* | Requires ONTAP 9.7 or higher.  Required to create the destination vserver for SVM DR or the destination volume.  Deprecated as of 21.2.0, use destination_endpoint and cluster. |
| **destination_endpoint**  dictionary  *added in netapp.ontap 21.2.0* | destination endpoint of a SnapMirror relationship. |
| **cluster**  string | Requires ONTAP 9.7 or higher.  Required to create the destination vserver for SVM DR or the destination volume. |
| **consistency_group_volumes**  list / elements=string | Requires ONTAP 9.8 or higher.  Mandatory property for a Consistency Group endpoint. Specifies the list of FlexVol volumes for a Consistency Group. |
| **ipspace**  string | Requires ONTAP 9.8 or higher.  Optional property to specify the IPSpace of the SVM. |
| **path**  string / required | The destination endpoint for the relationship.  format is <vserver:volume>, <vserver:>, <vserver:/cg/cg_name> |
| **svm**  string | The name of the SVM. Not sure when this is needed. |
| **destination_path**  string | Specifies the destination endpoint of the SnapMirror relationship.  Deprecated as of 21.2.0, use destination_endpoint and path. |
| **destination_volume**  string | Specifies the name of the destination volume for the SnapMirror.  Deprecated as of 21.2.0, use source_endpoint and path. |
| **destination_vserver**  string | Name of the destination vserver for the SnapMirror.  Deprecated as of 21.2.0, use destination_endpoint and path, or svm. |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **identity_preservation**  string  *added in netapp.ontap 22.4.0* | Specifies which configuration of the source SVM is replicated to the destination SVM.  This property is applicable only for SVM data protection with “async” policy type.  Only supported with REST and requires ONTAP 9.11.1 or later.  **Choices:**   - `"full"` - `"exclude_network_config"` - `"exclude_network_and_protocol_config"` |
| **identity_preserve**  boolean  *added in netapp.ontap 2.9.0* | Specifies whether or not the identity of the source Vserver is replicated to the destination Vserver.  If this parameter is set to true, the source Vserver’s configuration will additionally be replicated to the destination.  If the parameter is set to false, then only the source Vserver’s volumes and RBAC configuration are replicated to the destination.  **Choices:**   - `false` - `true` |
| **initialize**  boolean  *added in netapp.ontap 19.11.0* | Specifies whether to initialize SnapMirror relation.  Default is True, it can be explicitly set to False to avoid initializing SnapMirror relation.  **Choices:**   - `false` - `true` ← (default) |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **max_transfer_rate**  integer  *added in netapp.ontap 2.9.0* | Specifies the upper bound, in kilobytes per second, at which data is transferred.  Default is unlimited, it can be explicitly set to 0 as unlimited. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **peer_options**  dictionary  *added in netapp.ontap 21.8.0* | IP address and connection options for the peer system.  If any if these options is not specified, the corresponding source option is used. |
| **cert_filepath**  string | path to SSL client cert file (.pem). |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  **Choices:**   - `false` - `true` |
| **key_filepath**  string | path to SSL client key file. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **use_rest**  string | REST API if supported by the target system for all the resources and attributes the module requires. Otherwise will revert to ZAPI.  always – will always use the REST API  never – will always use the ZAPI  auto – will try to use the REST Api |
| **username**  aliases: user  string | Username when using basic authentication. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` |
| **policy**  string  *added in netapp.ontap 2.8.0* | Specify the name of the SnapMirror policy that applies to this relationship. |
| **relationship_info_only**  boolean  *added in netapp.ontap 20.4.0* | If relationship-info-only is set to true then only relationship information is removed.  **Choices:**   - `false` ← (default) - `true` |
| **relationship_state**  string  *added in netapp.ontap 20.2.0* | Specifies whether to break SnapMirror relation or establish a SnapMirror relationship.  state must be present to use this option.  **Choices:**   - `"active"` ← (default) - `"broken"` |
| **relationship_type**  string | Specify the type of SnapMirror relationship.  for ‘restore’ unless ‘source_snapshot’ is specified the most recent Snapshot copy on the source volume is restored.  restore SnapMirror is not idempotent.  With REST, only ‘extended_data_protection’ and ‘restore’ are supported.  **Choices:**   - `"data_protection"` - `"load_sharing"` - `"vault"` - `"restore"` - `"transition_data_protection"` - `"extended_data_protection"` |
| **schedule**  aliases: transfer_schedule  string  *added in netapp.ontap 22.2.0* | Specify the name of the current schedule, which is used to update the SnapMirror relationship.  Optional for create, modifiable.  With REST, this option requires ONTAP 9.11.1 or later. |
| **source_cluster**  string  *added in netapp.ontap 21.1.0* | Requires ONTAP 9.7 or higher.  Required to create the peering relationship between source and destination SVMs.  Deprecated as of 21.2.0, use source_endpoint and cluster. |
| **source_endpoint**  dictionary  *added in netapp.ontap 21.2.0* | source endpoint of a SnapMirror relationship. |
| **cluster**  string | Requires ONTAP 9.7 or higher.  Required to create the peering relationship between source and destination SVMs. |
| **consistency_group_volumes**  list / elements=string | Requires ONTAP 9.8 or higher.  Mandatory property for a Consistency Group endpoint. Specifies the list of FlexVol volumes for a Consistency Group. |
| **ipspace**  string | Requires ONTAP 9.8 or higher.  Optional property to specify the IPSpace of the SVM. |
| **path**  string / required | The source endpoint for the relationship.  If the source is an ONTAP volume (FlexVol or FlexGroup), format should be <vserver:volume>  For SVM DR, format should be <vserver:>  For a consistency group, format should be <vserver:/cg/cg_name>  If the source is an ElementSW volume, format should be <Element_SVIP:/lun/Element_VOLUME_ID>  If the source is an ElementSW volume, the volume should have SnapMirror enabled. |
| **svm**  string | The name of the SVM. Not sure when this is needed. |
| **source_hostname**  string | DEPRECATED - please use `peer_options`.  Source hostname or management IP address for ONTAP or ElementSW cluster.  If present, when state is absent, the relationship is released at the source before being deleted at destination.  It is recommended to always release before deleting, so make sure this parameter is present if the source hostname is known. |
| **source_password**  string | DEPRECATED - please use `peer_options`.  Source password for ONTAP or ElementSW cluster.  Optional if this is same as destination password. |
| **source_path**  string | Specifies the source endpoint of the SnapMirror relationship.  If the source is an ONTAP volume, format should be <[vserver:][volume]> or <[[cluster:]//vserver/]volume>  If the source is an ElementSW volume, format should be <[Element_SVIP]:/lun/[Element_VOLUME_ID]>  If the source is an ElementSW volume, the volume should have SnapMirror enabled.  Deprecated as of 21.2.0, use source_endpoint and path. |
| **source_snapshot**  string  *added in netapp.ontap 20.6.0* | Specifies the Snapshot from the source to be restored. |
| **source_username**  string | DEPRECATED - please use `peer_options`.  Source username for ONTAP or ElementSW cluster.  Optional if this is same as destination username. |
| **source_volume**  string | Specifies the name of the source volume for the SnapMirror.  Deprecated as of 21.2.0, use source_endpoint and path. |
| **source_vserver**  string | Name of the source vserver for the SnapMirror.  Deprecated as of 21.2.0, use source_endpoint and path, or svm. |
| **state**  string | Whether the specified relationship should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **transferring_time_out**  integer  *added in netapp.ontap 21.20.0* | How long to wait when a transfer is in progress (after initializing for instance). Unit is seconds.  **Default:** `300` |
| **update**  boolean  *added in netapp.ontap 20.2.0* | Specifies whether to update the destination endpoint of the SnapMirror relationship only if the relationship is already present and active.  Default is True.  **Choices:**   - `false` - `true` ← (default) |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **validate_source_path**  boolean  *added in netapp.ontap 21.21.0* | The relationship is found based on the destination as it is unique.  By default, the source information is verified and an error is reported if there is a mismatch. This would mean the destination is already used by another relationship.  The check accounts for a local vserver name that may be different from the remote vserver name.  This may be disabled in case the check is too strict, to unconditionally delete a realtionship for instance.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](na_ontap_snapmirror_module.md#id4)

> **Note:**
>
> - supports REST and ZAPI.
> - supports check_mode.
> - restore is not idempotent.
> - snapmirror runs on the destination for most operations, peer_options identify the source cluster.
> - ONTAP supports either username/password or a SSL certificate for authentication.
> - ElementSW only supports username/password for authentication.
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_snapmirror_module.md#id5)

```yaml+jinja
# creates and initializes the snapmirror
- name: Create ONTAP/ONTAP SnapMirror
  netapp.ontap.na_ontap_snapmirror:
    state: present
    source_volume: test_src
    destination_volume: test_dest
    source_vserver: ansible_src
    destination_vserver: ansible_dest
    schedule: hourly
    policy: MirrorAllSnapshots
    max_transfer_rate: 1000
    initialize: False
    hostname: "{{ destination_cluster_hostname }}"
    username: "{{ destination_cluster_username }}"
    password: "{{ destination_cluster_password }}"

# creates and initializes the snapmirror between vservers
- name: Create ONTAP/ONTAP vserver SnapMirror
  netapp.ontap.na_ontap_snapmirror:
    state: present
    source_vserver: ansible_src
    destination_vserver: ansible_dest
    identity_preserve: true
    hostname: "{{ destination_cluster_hostname }}"
    username: "{{ destination_cluster_username }}"
    password: "{{ destination_cluster_password }}"

# existing snapmirror relation with status 'snapmirrored' will be initialized
- name: Inititalize ONTAP/ONTAP SnapMirror
  netapp.ontap.na_ontap_snapmirror:
    state: present
    source_path: 'ansible:test'
    destination_path: 'ansible:dest'
    relationship_state: active
    hostname: "{{ destination_cluster_hostname }}"
    username: "{{ destination_cluster_username }}"
    password: "{{ destination_cluster_password }}"

- name: Delete SnapMirror
  netapp.ontap.na_ontap_snapmirror:
    state: absent
    destination_path: <path>
    relationship_info_only: True
    source_hostname: "{{ source_hostname }}"
    hostname: "{{ destination_cluster_hostname }}"
    username: "{{ destination_cluster_username }}"
    password: "{{ destination_cluster_password }}"

- name: Break SnapMirror
  netapp.ontap.na_ontap_snapmirror:
    state: present
    relationship_state: broken
    destination_path: <path>
    source_hostname: "{{ source_hostname }}"
    hostname: "{{ destination_cluster_hostname }}"
    username: "{{ destination_cluster_username }}"
    password: "{{ destination_cluster_password }}"

- name: Restore SnapMirror volume using location (Idempotency)
  netapp.ontap.na_ontap_snapmirror:
    state: present
    source_path: <path>
    destination_path: <path>
    relationship_type: restore
    source_snapshot: "{{ snapshot }}"
    hostname: "{{ destination_cluster_hostname }}"
    username: "{{ destination_cluster_username }}"
    password: "{{ destination_cluster_password }}"

- name: Set schedule to NULL
  netapp.ontap.na_ontap_snapmirror:
    state: present
    destination_path: <path>
    schedule: ""
    hostname: "{{ destination_cluster_hostname }}"
    username: "{{ destination_cluster_username }}"
    password: "{{ destination_cluster_password }}"

- name: Create SnapMirror from ElementSW to ONTAP
  netapp.ontap.na_ontap_snapmirror:
    state: present
    connection_type: elementsw_ontap
    source_path: '10.10.10.10:/lun/300'
    destination_path: 'ansible_test:ansible_dest_vol'
    schedule: hourly
    policy: MirrorLatest
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    source_hostname: " {{ Element_cluster_mvip }}"
    source_username: "{{ Element_cluster_username }}"
    source_password: "{{ Element_cluster_password }}"

- name: Create SnapMirror from ONTAP to ElementSW
  netapp.ontap.na_ontap_snapmirror:
    state: present
    connection_type: ontap_elementsw
    destination_path: '10.10.10.10:/lun/300'
    source_path: 'ansible_test:ansible_dest_vol'
    policy: MirrorLatest
    hostname: "{{ Element_cluster_mvip }}"
    username: "{{ Element_cluster_username }}"
    password: "{{ Element_cluster_password }}"
    source_hostname: " {{ netapp_hostname }}"
    source_username: "{{ netapp_username }}"
    source_password: "{{ netapp_password }}"

- name: Create SnapMirror relationship (create destination volume)
  tags: create
  netapp.ontap.na_ontap_snapmirror:
    state: present
    source_endpoint:
      cluster: "{{ _source_cluster }}"
      path: "{{ source_vserver + ':' + source_volume }}"
    destination_endpoint:
      cluster: "{{ _destination_cluster }}"
      path: "{{ destination_vserver_VOLDP + ':' + destination_volume }}"
    create_destination:
      enabled: true
    hostname: "{{ destination_hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    https: true
    validate_certs: false

- name: Create SnapMirror relationship - SVM DR (creating and peering destination svm)
  tags: create_svmdr
  netapp.ontap.na_ontap_snapmirror:
    state: present
    source_endpoint:
      cluster: "{{ _source_cluster }}"
      path: "{{ source_vserver + ':' }}"
    destination_endpoint:
      cluster: "{{ _destination_cluster }}"
      path: "{{ destination_vserver_SVMDR + ':' }}"
    create_destination:
      enabled: true
    hostname: "{{ destination_hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    https: true
    validate_certs: false
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
