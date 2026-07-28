---
collection: ansible
version: "8"
title: "netapp.storagegrid.na_sg_grid_info module – NetApp StorageGRID Grid information gatherer."
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/storagegrid/na_sg_grid_info_module.html
fetched_at: 2026-07-28T02:43:52+00:00
---
# netapp.storagegrid.na_sg_grid_info module – NetApp StorageGRID Grid information gatherer.

> **Note:**
>
> This module is part of the [netapp.storagegrid collection](https://galaxy.ansible.com/ui/repo/published/netapp/storagegrid/) (version 21.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.storagegrid`.
>
> To use it in a playbook, specify: `netapp.storagegrid.na_sg_grid_info`.

New in netapp.storagegrid 20.11.0

- [Synopsis](na_sg_grid_info_module.md#synopsis)
- [Parameters](na_sg_grid_info_module.md#parameters)
- [Notes](na_sg_grid_info_module.md#notes)
- [Examples](na_sg_grid_info_module.md#examples)
- [Return Values](na_sg_grid_info_module.md#return-values)

## [Synopsis](na_sg_grid_info_module.md#id1)

- This module allows you to gather various information about StorageGRID Grid configuration.

## [Parameters](na_sg_grid_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_url**  string / required | The url to the StorageGRID Admin Node REST API. |
| **auth_token**  string / required | The authorization token for the API request |
| **gather_subset**  list / elements=string | When supplied, this argument will restrict the information collected to a given subset.  Either the info name or the REST API can be given.  Possible values for this argument include  `grid_accounts_info` or `grid/accounts`  `grid_alarms_info` or `grid/alarms`  `grid_audit_info` or `grid/audit`  `grid_compliance_global_info` or `grid/compliance-global`  `grid_config_info` or `grid/config`  `grid_config_management_info` or `grid/config/management`  `grid_config_product_version_info` or `grid/config/product-version`  `grid_deactivated_features_info` or `grid/deactivated-features`  `grid_dns_servers_info` or `grid/dns-servers`  `grid_domain_names_info` or `grid/domain-names`  `grid_ec_profiles_info` or `grid/ec-profiles`  `grid_expansion_info` or `grid/expansion`  `grid_expansion_nodes_info` or `grid/expansion/nodes`  `grid_expansion_sites_info` or `grid/expansion/sites`  `grid_grid_networks_info` or `grid/grid-networks`  `grid_groups_info` or `grid/groups`  `grid_health_info` or `grid/health`  `grid_health_topology_info` or `grid/health/topology`  `grid_identity_source_info` or `grid/identity-source`  `grid_ilm_criteria_info` or `grid/ilm-criteria`  `grid_ilm_policies_info` or `grid/ilm-policies`  `grid_ilm_rules_info` or `grid/ilm-rules`  `grid_license_info` or `grid/license`  `grid_management_certificate_info` or `grid/management-certificate`  `grid_ntp_servers_info` or `grid/ntp-servers`  `grid_recovery_available_nodes_info` or `grid/recovery/available-nodes`  `grid_recovery_info` or `grid/recovery`  `grid_regions_info` or `grid/regions`  `grid_schemes_info` or `grid/schemes`  `grid_snmp_info` or `grid/snmp`  `grid_storage_api_certificate_info` or `grid/storage-api-certificate`  `grid_untrusted_client_network_info` or `grid/untrusted-client-network`  `grid_users_info` or `grid/users`  `grid_users_root_info` or `grid/users/root`  `versions_info` or `versions`  Can specify a list of values to include a larger subset.  **Default:** `["all"]` |
| **parameters**  dictionary | Allows for any rest option to be passed in. |
| **validate_certs**  boolean | Should https certificates be validated?  **Choices:**   - `false` - `true` ← (default) |

## [Notes](na_sg_grid_info_module.md#id3)

> **Note:**
>
> - The modules prefixed with `na_sg` are built to manage NetApp StorageGRID.

## [Examples](na_sg_grid_info_module.md#id4)

```yaml+jinja
- name: Gather StorageGRID Grid info
  netapp.storagegrid.na_sg_grid_info:
    api_url: "https://1.2.3.4/"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
  register: sg_grid_info

- name: Gather StorageGRID Grid info for grid/accounts and grid/config subsets
  netapp.storagegrid.na_sg_grid_info:
    api_url: "https://1.2.3.4/"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    gather_subset:
      - grid_accounts_info
      - grid/config
  register: sg_grid_info

- name: Gather StorageGRID Grid info for all subsets
  netapp.storagegrid.na_sg_grid_info:
    api_url: "https://1.2.3.4/"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    gather_subset:
      - all
  register: sg_grid_info

- name: Gather StorageGRID Grid info for grid/accounts and grid/users subsets, limit to 5 results for each subset
  netapp.storagegrid.na_sg_grid_info:
    api_url: "https://1.2.3.4/"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    gather_subset:
      - grid/accounts
      - grid/users
    parameters:
      limit: 5
  register: sg_grid_info
```

## [Return Values](na_sg_grid_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **sg_info**  dictionary | Returns various information about the StorageGRID Grid configuration.  **Returned:** always  **Sample:** `{"grid/accounts": {"...": null}, "grid/alarms": {"...": null}, "grid/audit": {"...": null}, "grid/compliance-global": {"...": null}, "grid/config": {"...": null}, "grid/config/management": {"...": null}, "grid/config/product-version": {"...": null}, "grid/deactivated-features": {"...": null}, "grid/dns-servers": {"...": null}, "grid/domain-names": {"...": null}, "grid/ec-profiles": {"...": null}, "grid/expansion": {"...": null}, "grid/expansion/nodes": {"...": null}, "grid/expansion/sites": {"...": null}, "grid/groups": {"...": null}, "grid/health": {"...": null}, "grid/health/topology": {"...": null}, "grid/identity-source": {"...": null}, "grid/ilm-criteria": {"...": null}, "grid/ilm-policies": {"...": null}, "grid/ilm-rules": {"...": null}, "grid/license": {"...": null}, "grid/management-certificate": {"...": null}, "grid/networks": {"...": null}, "grid/ntp-servers": {"...": null}, "grid/recovery": {"...": null}, "grid/recovery/available-nodes": {"...": null}, "grid/regions": {"...": null}, "grid/schemes": {"...": null}, "grid/snmp": {"...": null}, "grid/storage-api-certificate": {"...": null}, "grid/untrusted-client-network": {"...": null}, "grid/users": {"...": null}, "grid/users/root": {"...": null}, "grid/versions": {"...": null}}` |

### Authors

- NetApp Ansible Team (@jasonl4)

### Collection links

- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.storagegrid)
