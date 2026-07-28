---
collection: ansible
version: "8"
title: "hpe.nimble.hpe_nimble_volume_collection module – Manage the HPE Nimble Storage volume collections"
source_url: https://docs.ansible.com/projects/ansible/8/collections/hpe/nimble/hpe_nimble_volume_collection_module.html
fetched_at: 2026-07-28T01:05:46+00:00
---
# hpe.nimble.hpe_nimble_volume_collection module – Manage the HPE Nimble Storage volume collections

> **Note:**
>
> This module is part of the [hpe.nimble collection](https://galaxy.ansible.com/ui/repo/published/hpe/nimble/) (version 1.1.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hpe.nimble`.
> You need further requirements to be able to use this module,
> see [Requirements](hpe_nimble_volume_collection_module.md#ansible-collections-hpe-nimble-hpe-nimble-volume-collection-module-requirements) for details.
>
> To use it in a playbook, specify: `hpe.nimble.hpe_nimble_volume_collection`.

New in hpe.nimble 1.0.0

- [Synopsis](hpe_nimble_volume_collection_module.md#synopsis)
- [Requirements](hpe_nimble_volume_collection_module.md#requirements)
- [Parameters](hpe_nimble_volume_collection_module.md#parameters)
- [Notes](hpe_nimble_volume_collection_module.md#notes)
- [Examples](hpe_nimble_volume_collection_module.md#examples)

## [Synopsis](hpe_nimble_volume_collection_module.md#id1)

- Manage the volume collections on an HPE Nimble Storage group.

## [Requirements](hpe_nimble_volume_collection_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later
- Python 3.6 or later
- HPE Nimble Storage SDK for Python
- HPE Nimble Storage arrays running NimbleOS 5.0 or later

## [Parameters](hpe_nimble_volume_collection_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **abort_handover**  boolean | Abort in-progress handover. If for some reason a previously invoked handover request is unable to complete, this action can be used to cancel it. This operation is not supported for synchronous replication volume collections.  **Choices:**   - `false` - `true` |
| **agent_hostname**  string | Generic backup agent hostname. |
| **agent_password**  string | Generic backup agent password. |
| **agent_username**  string | Generic backup agent username. |
| **app_cluster**  string | If the application is running within a Windows cluster environment, this is the cluster name. |
| **app_id**  string | Application ID running on the server.  **Choices:**   - `"inval"` - `"exchange"` - `"exchange_dag"` - `"hyperv"` - `"sql2005"` - `"sql2008"` - `"sql2012"` - `"sql2014"` - `"sql2016"` - `"sql2017"` |
| **app_server**  string | Application server hostname. |
| **app_service**  string | If the application is running within a windows cluster environment then this is the instance name of the service running within the cluster environment. |
| **app_sync**  string | Application synchronization.  **Choices:**   - `"none"` - `"vss"` - `"vmware"` - `"generic"` |
| **change_name**  string | Change name of the existing volume collection. |
| **demote**  boolean | Release ownership of the specified volume collection. The volumes associated with the volume collection will be set to offline and a snapshot will be created, then full control over the volume collection will be transferred to the new owner. This option can be used following a promote to revert the volume collection back to its prior configured state. This operation does not alter the configuration on the new owner itself, but does require the new owner to be running in order to obtain its identity information. This operation is not supported for synchronous replication volume collections.  **Choices:**   - `false` - `true` |
| **description**  string | Text description of volume collection. |
| **handover**  boolean | Gracefully transfer ownership of the specified volume collection. This action can be used to pass control of the volume collection to the downstream replication partner. Ownership and full control over the volume collection will be given to the downstream replication partner. The volumes associated with the volume collection will be set to offline prior to the final snapshot being taken and replicated, thus ensuring full data synchronization as part of the transfer. By default, the new owner will automatically begin replicating the volume collection back to this node when the handover completes.  **Choices:**   - `false` - `true` |
| **host**  string / required | HPE Nimble Storage IP address. |
| **invoke_on_upstream_partner**  boolean | Invoke handover request on upstream partner. This operation is not supported for synchronous replication volume collections.  **Choices:**   - `false` - `true` |
| **is_standalone_volcoll**  boolean | Indicates whether this is a standalone volume collection.  **Choices:**   - `false` - `true` |
| **metadata**  dictionary | User defined key-value pairs that augment a volume collection attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed. |
| **name**  string / required | Name of the volume collection. |
| **no_reverse**  boolean | Do not automatically reverse direction of replication. Using this argument will prevent the new owner from automatically replicating the volume collection to this node when the handover completes.  **Choices:**   - `false` - `true` |
| **override_upstream_down**  boolean | Allow the handover request to proceed even if upstream array is down. The default behavior is to return an error when upstream is down. This option is applicable for synchronous replication only.  **Choices:**   - `false` - `true` |
| **password**  string / required | HPE Nimble Storage password. |
| **promote**  boolean | Take ownership of the specified volume collection. The volumes associated with the volume collection will be set to online and be available for reading and writing. Replication will be disabled on the affected schedules and must be re-configured if desired. Snapshot retention for the affected schedules will be set to the greater of the current local or replica retention values. This operation is not supported for synchronous replication volume collections.  **Choices:**   - `false` - `true` |
| **prot_template**  string | Name of the protection template whose attributes will be used to create this volume collection. This attribute is only used for input when creating a volume collection and is not outputted. |
| **replication_partner**  string | Name of the new volume collection owner. |
| **replication_type**  string | Type of replication configured for the volume collection.  **Choices:**   - `"periodic_snapshot"` - `"synchronous"` |
| **state**  string / required | The volume collection operations.  **Choices:**   - `"present"` - `"absent"` - `"create"` |
| **username**  string / required | HPE Nimble Storage user name. |
| **validate**  boolean | Validate a volume collection with either Microsoft VSS or VMware application synchronization.  **Choices:**   - `false` - `true` |
| **vcenter_hostname**  string | VMware vCenter hostname. |
| **vcenter_password**  string | Application VMware vCenter password. A password with few constraints. |
| **vcenter_username**  string | Application VMware vCenter username. String of up to 80 alphanumeric characters, beginning with a letter. It can include ampersand (@), backslash (\), dash (-), period (.), and underscore (_). |

## [Notes](hpe_nimble_volume_collection_module.md#id4)

> **Note:**
>
> - This module does not support `check_mode`.

## [Examples](hpe_nimble_volume_collection_module.md#id5)

```yaml+jinja
# if state is create , then create a volcoll if not present. Fails if already present.
# if state is present, then create a volcoll if not present. Succeed if it already exists.
- name: Create volume collection if not present
  hpe.nimble.hpe_nimble_volume_collection:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    description: "{{ description | default(None)}}"
    state: "{{ state | default('present') }}"

- name: Delete volume collection
  hpe.nimble.hpe_nimble_volume_collection:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    state: absent

- name: Promote volume collection
  hpe.nimble.hpe_nimble_volume_collection:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    state: present
    promote: True

- name: Demote volume collection
  hpe.nimble.hpe_nimble_volume_collection:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    state: present
    demote: True

- name: Handover volume collection
  hpe.nimble.hpe_nimble_volume_collection:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    state: present
    handover: True

- name: Abort handover volume collection
  hpe.nimble.hpe_nimble_volume_collection:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    state: present
    abort_handover: True

- name: Validate volume collection
  hpe.nimble.hpe_nimble_volume_collection:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    state: present
    validate: True
```

### Authors

- HPE Nimble Storage Ansible Team (@ar-india)

### Collection links

- [Issue Tracker](https://github.com/hpe-storage/nimble-ansible-modules/issues)
- [Homepage](http://hpe.com/storage/nimble)
- [Repository (Sources)](https://github.com/hpe-storage/nimble-ansible-modules)
