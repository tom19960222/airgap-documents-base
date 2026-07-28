---
collection: ansible
version: "6"
title: "netapp.storagegrid.na_sg_org_info module – NetApp StorageGRID Org information gatherer."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/storagegrid/na_sg_org_info_module.html
fetched_at: 2026-07-28T00:13:46+00:00
---
# netapp.storagegrid.na_sg_org_info module – NetApp StorageGRID Org information gatherer.

> **Note:**
>
> This module is part of the [netapp.storagegrid collection](https://galaxy.ansible.com/netapp/storagegrid) (version 21.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.storagegrid`.
>
> To use it in a playbook, specify: `netapp.storagegrid.na_sg_org_info`.

New in netapp.storagegrid 20.11.0

- [Synopsis](na_sg_org_info_module.md#synopsis)
- [Parameters](na_sg_org_info_module.md#parameters)
- [Notes](na_sg_org_info_module.md#notes)
- [Examples](na_sg_org_info_module.md#examples)
- [Return Values](na_sg_org_info_module.md#return-values)

## [Synopsis](na_sg_org_info_module.md#id1)

- This module allows you to gather various information about StorageGRID Org configuration.

## [Parameters](na_sg_org_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_url**  string / required | The url to the StorageGRID Admin Node REST API. |
| **auth_token**  string / required | The authorization token for the API request |
| **gather_subset**  list / elements=string | When supplied, this argument will restrict the information collected to a given subset.  Either the info name or the Rest API can be given.  Possible values for this argument include  `org_compliance_global_info` or `org/compliance-global`  `org_config_info` or `org/config`  `org_config_product_version_info` or `org/config/product-version`  `org_containers_info` or `org/containers`  `org_deactivated_features_info` or `org/deactivated-features`  `org_endpoints_info` or `org/endpoints`  `org_groups_info` or `org/groups`  `org_identity_source_info` or `org/identity-source`  `org_regions_info` or `org/regions`  `org_users_current_user_s3_access_keys_info` or `org/users/current-user/s3-access-keys`  `org_usage_info` or `org/usage`  `org_users_info` or `org/users`  `org_users_root_info` or `org/users/root`  `versions_info` or `versions`  Can specify a list of values to include a larger subset.  Default: `["all"]` |
| **parameters**  dictionary | Allows for any rest option to be passed in. |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Notes](na_sg_org_info_module.md#id3)

> **Note:**
>
> - The modules prefixed with `na_sg` are built to manage NetApp StorageGRID.

## [Examples](na_sg_org_info_module.md#id4)

```yaml+jinja
- name: Gather StorageGRID Org info
  netapp.storagegrid.na_sg_org_info:
    api_url: "https://1.2.3.4/"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
  register: sg_org_info

- name: Gather StorageGRID Org info for org/containers and org/config subsets
  netapp.storagegrid.na_sg_org_info:
    api_url: "https://1.2.3.4/"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    gather_subset:
      - org_containers_info
      - org/config
  register: sg_org_info

- name: Gather StorageGRID Org info for all subsets
  netapp.storagegrid.na_sg_org_info:
    api_url: "https://1.2.3.4/"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    gather_subset:
      - all
  register: sg_org_info

- name: Gather StorageGRID Org info for org/containers and org/users subsets, limit to 5 results for each subset
  netapp.storagegrid.na_sg_org_info:
    api_url: "https://1.2.3.4/"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    gather_subset:
      - org/containers
      - org/users
    parameters:
      limit: 5
  register: sg_org_info
```

## [Return Values](na_sg_org_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **sg_info**  dictionary | Returns various information about the StorageGRID Grid configuration.  Returned: always  Sample: `{"org/compliance-global": {"...": null}, "org/config": {"...": null}, "org/config/product-version": {"...": null}, "org/containers": {"...": null}, "org/deactivated-features": {"...": null}, "org/endpoints": {"...": null}, "org/groups": {"...": null}, "org/identity-source": {"...": null}, "org/regions": {"...": null}, "org/usage": {"...": null}, "org/users": {"...": null}, "org/users/current-user/s3-access-keys": {"...": null}, "org/users/root": {"...": null}, "org/versions": {"...": null}}` |

### Authors

- NetApp Ansible Team (@jasonl4)

### Collection links

[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.storagegrid)
