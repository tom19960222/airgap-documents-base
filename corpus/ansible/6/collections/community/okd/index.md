---
collection: ansible
version: "6"
title: "Community.Okd"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/okd/index.html
fetched_at: 2026-07-27T16:41:48+00:00
---
# Community.Okd

Collection version 2.2.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

OKD Collection for Ansible.

**Authors:**

- geerlingguy (<https://www.jeffgeerling.com/>)
- fabianvf (<https://github.com/fabianvf>)
- willthames (<https://github.com/willthames>)
- Akasurde (<https://github.com/akasurde>)

**Supported ansible-core versions:**

- 2.9.17 or newer

[Issue Tracker](https://github.com/openshift/community.okd/issues)
[Repository (Sources)](https://github.com/openshift/community.okd)

## [Plugin Index](index.md#id2)

These are the plugins in the community.okd collection:

### Modules

- [k8s module](k8s_module.md#ansible-collections-community-okd-k8s-module) – Manage OpenShift objects
- [openshift_adm_groups_sync module](openshift_adm_groups_sync_module.md#ansible-collections-community-okd-openshift-adm-groups-sync-module) – Sync OpenShift Groups with records from an external provider.
- [openshift_adm_migrate_template_instances module](openshift_adm_migrate_template_instances_module.md#ansible-collections-community-okd-openshift-adm-migrate-template-instances-module) – Update TemplateInstances to point to the latest group-version-kinds
- [openshift_adm_prune_auth module](openshift_adm_prune_auth_module.md#ansible-collections-community-okd-openshift-adm-prune-auth-module) – Removes references to the specified roles, clusterroles, users, and groups
- [openshift_adm_prune_deployments module](openshift_adm_prune_deployments_module.md#ansible-collections-community-okd-openshift-adm-prune-deployments-module) – Remove old completed and failed deployment configs
- [openshift_adm_prune_images module](openshift_adm_prune_images_module.md#ansible-collections-community-okd-openshift-adm-prune-images-module) – Remove unreferenced images
- [openshift_auth module](openshift_auth_module.md#ansible-collections-community-okd-openshift-auth-module) – Authenticate to OpenShift clusters which require an explicit login step
- [openshift_import_image module](openshift_import_image_module.md#ansible-collections-community-okd-openshift-import-image-module) – Import the latest image information from a tag in a container image registry.
- [openshift_process module](openshift_process_module.md#ansible-collections-community-okd-openshift-process-module) – Process an OpenShift template.openshift.io/v1 Template
- [openshift_registry_info module](openshift_registry_info_module.md#ansible-collections-community-okd-openshift-registry-info-module) – Display information about the integrated registry.
- [openshift_route module](openshift_route_module.md#ansible-collections-community-okd-openshift-route-module) – Expose a Service as an OpenShift Route.

### Connection Plugins

- [oc connection](oc_connection.md#ansible-collections-community-okd-oc-connection) – Execute tasks in pods running on OpenShift.

### Inventory Plugins

- [openshift inventory](openshift_inventory.md#ansible-collections-community-okd-openshift-inventory) – OpenShift inventory source

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
