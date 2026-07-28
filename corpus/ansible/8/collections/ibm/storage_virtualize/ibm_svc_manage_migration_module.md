---
collection: ansible
version: "8"
title: "ibm.storage_virtualize.ibm_svc_manage_migration module – This module manages volume migration between clusters on IBM Storage Virtualize family systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/storage_virtualize/ibm_svc_manage_migration_module.html
fetched_at: 2026-07-28T02:35:32+00:00
---
# ibm.storage_virtualize.ibm_svc_manage_migration module – This module manages volume migration between clusters on IBM Storage Virtualize family systems

> **Note:**
>
> This module is part of the [ibm.storage_virtualize collection](https://galaxy.ansible.com/ui/repo/published/ibm/storage_virtualize/) (version 2.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ibm.storage_virtualize`.
>
> To use it in a playbook, specify: `ibm.storage_virtualize.ibm_svc_manage_migration`.

New in ibm.storage_virtualize 1.6.0

- [Synopsis](ibm_svc_manage_migration_module.md#synopsis)
- [Parameters](ibm_svc_manage_migration_module.md#parameters)
- [Notes](ibm_svc_manage_migration_module.md#notes)
- [Examples](ibm_svc_manage_migration_module.md#examples)

## [Synopsis](ibm_svc_manage_migration_module.md#id1)

- Ansible interface to manage the migration commands.

## [Parameters](ibm_svc_manage_migration_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Storage Virtualize system. |
| **domain**  string | Domain for the Storage Virtualize system.  Valid when hostname is used for the parameter *clustername*. |
| **log_path**  string | Path of debug log file. |
| **new_pool**  string  *added in ibm.storage_virtualize 1.11.0* | Specifies the pool on which the volume has to be migrated.  Valid only when *type_of_migration=across_pools*. |
| **password**  string | REST API password for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user on the local system. |
| **relationship_name**  string | Name of the migration relationship. Required when *state=initiate* or *state=switch*. |
| **remote_cluster**  string | Specifies the name of the remote cluster.  Required when *state=initiate*. |
| **remote_password**  string | REST API password for the partner Storage Virtualize system.  The parameters *remote_username* and *remote_password* are required if not using *remote_token* to authenticate a user on the partner system.  Valid when *state=initiate*. |
| **remote_pool**  string | Specifies the pool on which the volume on Partner Storage Virtualize system should get created.  Required when *state=initiate*. |
| **remote_token**  string | The authentication token to verify a user on the partner Storage Virtualize system.  To generate a token, use the ibm_svc_auth module. Valid when *state=initiate*. |
| **remote_username**  string | REST API username for the partner Storage Virtualize system.  The parameters *remote_username* and *remote_password* are required if not using *remote_token* to authenticate a user on the partner system.  Valid when `state=initiate`. |
| **remote_validate_certs**  boolean | Validates certification for partner Storage Virtualize system.  Valid when *state=initiate*.  **Choices:**   - `false` ← (default) - `true` |
| **replicate_hosts**  boolean | Replicates the hosts mapped to a source volume on the source system, to the target system, and maps the hosts to the target volume. The user can use ibm_svc_host and ibm_svc_vol_map modules to create and map hosts to the target volume for an existing migration relationship.  Valid when *state=initiate*.  **Choices:**   - `false` ← (default) - `true` |
| **source_volume**  string | Specifies the name of the existing source volume to be used in migration.  Required when *state=initiate* or *state=cleanup* or *type_of_migration=across_pools*. |
| **state**  string | Specifies the different states of the migration process when *type_of_migration=across_clusters*.  `initiate`, creates a volume on remote cluster; optionally used to replicate hosts, and to create and start a migration relationship.  `switch`, switches the migration relationship direction allowing write access on the target volume.  `cleanup`, deletes the source volume and migration relationship after a ‘switch’.  **Choices:**   - `"initiate"` - `"switch"` - `"cleanup"` |
| **target_volume**  string | Specifies the name of the volume to be created on the target system.  Required when *state=initiate*. |
| **token**  string | The authentication token to verify a user on the Storage Virtualize system.  To generate a token, use the ibm_svc_auth module. |
| **type_of_migration**  string  *added in ibm.storage_virtualize 1.11.0* | Specifies the type of migration whether it is migration across pools or migration across clusters  **Choices:**   - `"across_pools"` - `"across_clusters"` ← (default) |
| **username**  string | REST API username for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user on the local system. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_svc_manage_migration_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.
> - This module supports both volume migration across pools and volume migration across clusters.
> - In case, user does not specify type_of_migration, the module shall proceed with migration across clusters by default.
> - In case of *type_of_migration=across_pools*, the only parameters allowed are *new_pool* and *source_volume* along with cluster credentials.

## [Examples](ibm_svc_manage_migration_module.md#id4)

```yaml+jinja
- name: Create a target volume
        Create a relationship
        Replicate hosts from source volume to target volume
        Start a relationship
  ibm.storage_virtualize.ibm_svc_manage_migration:
    source_volume: "src_vol"
    target_volume: "target_vol"
    clustername: "{{ source_cluster }}"
    remote_cluster: "{{ remote_cluster }}"
    token: "{{ source_cluster_token }}"
    state: initiate
    replicate_hosts: true
    remote_token: "{{ partner_cluster_token }}"
    relationship_name: "migrate_vol"
    log_path: /tmp/ansible.log
    remote_pool: "{{ remote_pool }}"
- name: Switch replication direction
  ibm.storage_virtualize.ibm_svc_manage_migration:
    relationship_name: "migrate_vol"
    clustername: "{{ source_cluster }}"
    token: "{{ source_cluster_token }}"
    state: switch
    log_path: /tmp/ansible.log
- name: Delete source volume and migration relationship
  ibm.storage_virtualize.ibm_svc_manage_migration:
    clustername: "{{ source_cluster }}"
    state: cleanup
    source_volume: "src_vol"
    token: "{{ source_cluster_token }}"
    log_path : /tmp/ansible.log
- name: Migration an existing vol from pool0 to pool1
  ibm.storage_virtualize.ibm_svc_manage_migration:
    clustername: "{{ source_cluster }}"
    token: "{{ source_cluster_token }}"
    log_path : /tmp/ansible.log
    type_of_migration : across_pools
    source_volume : vol1
    new_pool : pool1
```

### Authors

- Rohit Kumar(@rohitk-github)
- Shilpi Jain(@Shilpi-J)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.storage_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.storage_virtualize)
- [Report an issue](https://github.com/ansible-collections/community.REPO_NAME/issues/new/choose)
- [Communication](index.md#communication-for-ibm-storage-virtualize)
