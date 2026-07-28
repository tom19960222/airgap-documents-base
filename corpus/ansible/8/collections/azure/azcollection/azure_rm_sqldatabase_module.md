---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_sqldatabase module – Manage SQL Database instance"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_sqldatabase_module.html
fetched_at: 2026-07-28T01:14:48+00:00
---
# azure.azcollection.azure_rm_sqldatabase module – Manage SQL Database instance

> **Note:**
>
> This module is part of the [azure.azcollection collection](https://galaxy.ansible.com/ui/repo/published/azure/azcollection/) (version 1.19.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install azure.azcollection`.
> You need further requirements to be able to use this module,
> see [Requirements](azure_rm_sqldatabase_module.md#ansible-collections-azure-azcollection-azure-rm-sqldatabase-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_sqldatabase`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_sqldatabase_module.md#synopsis)
- [Requirements](azure_rm_sqldatabase_module.md#requirements)
- [Parameters](azure_rm_sqldatabase_module.md#parameters)
- [Notes](azure_rm_sqldatabase_module.md#notes)
- [See Also](azure_rm_sqldatabase_module.md#see-also)
- [Examples](azure_rm_sqldatabase_module.md#examples)
- [Return Values](azure_rm_sqldatabase_module.md#return-values)

## [Synopsis](azure_rm_sqldatabase_module.md#id1)

- Create, update and delete instance of SQL Database.

## [Requirements](azure_rm_sqldatabase_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_sqldatabase_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  **Choices:**   - `false` - `true` ← (default) |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **collation**  string | The collation of the database. If not *create_mode=default*, this value is ignored. |
| **create_mode**  string | Specifies the mode of database creation.  `default`, regular database creation.  `copy`, creates a database as a copy of an existing database.  `online_secondary`/`non_readable_secondary`, creates a database as a (readable or nonreadable) secondary replica of an existing database.  `point_in_time_restore`, Creates a database by restoring a point in time backup of an existing database.  `recovery`, Creates a database by restoring a geo-replicated backup.  `restore`, Creates a database by restoring a backup of a deleted database.  `restore_long_term_retention_backup`, Creates a database by restoring from a long term retention vault.  `copy`, `non_readable_secondary`, `online_secondary` and `restore_long_term_retention_backup` are not supported for `data_warehouse` edition.  **Choices:**   - `"copy"` - `"default"` - `"non_readable_secondary"` - `"online_secondary"` - `"point_in_time_restore"` - `"recovery"` - `"restore"` - `"restore_long_term_retention_backup"` |
| **edition**  string | (Deprecate)The edition of the database. The DatabaseEditions enumeration contains all the valid editions.  This option will be deprecated in 2.11, use *sku* instead.  Cannot set `sku` when this field set.  **Choices:**   - `"web"` - `"business"` - `"basic"` - `"standard"` - `"premium"` - `"free"` - `"stretch"` - `"data_warehouse"` - `"system"` - `"system2"` |
| **elastic_pool_name**  string | The name of the elastic pool the database is in. Not supported for *edition=data_warehouse*. |
| **force_update**  boolean | SQL Database will be updated if given parameters differ from existing resource state.  To force SQL Database update in any circumstances set this parameter to True.  **Choices:**   - `false` - `true` |
| **location**  string | Resource location. If not set, location from the resource group will be used as default. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **max_size_bytes**  string | The max size of the database expressed in bytes.  If not *create_mode=default*, this value is ignored.  To see possible values, query the capabilities API (/subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationID}/capabilities). referred to by operationId:’Capabilities_ListByLocation’. |
| **name**  string / required | The name of the database to be operated on (updated or created). |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **read_scale**  boolean | If the database is a geo-secondary, indicates whether read-only connections are allowed to this database or not.  Not supported for *edition=data_warehouse*.  **Choices:**   - `false` ← (default) - `true` |
| **recovery_services_recovery_point_resource_id**  string | Required if *create_mode=restore_long_term_retention_backup*, then this value is required.  Specifies the resource ID of the recovery point to restore from. |
| **resource_group**  string / required | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. |
| **restore_point_in_time**  string | Required if *create_mode=point_in_time_restore*, this value is required. If *create_mode=restore*, this value is optional.  Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database.  Must be greater than or equal to the source database’s earliestRestoreDate value. |
| **sample_name**  string | Indicates the name of the sample schema to apply when creating this database.  If not *create_mode=default*, this value is ignored.  Not supported for *edition=data_warehouse*.  **Choices:**   - `"adventure_works_lt"` |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **server_name**  string / required | The name of the server. |
| **sku**  dictionary | The sku of the database. The DatabaseEditions enumeration contains all the valid sku.  If *create_mode=non_readable_secondary* or *create_mode=online_secondary*, this value is ignored.  To see possible values, query the capabilities API (/subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationID}/capabilities) referred to by operationId:’Capabilities_ListByLocation’.  Cannot set `edition` when this field set. |
| **capacity**  integer | Capacity of the particular SKU. |
| **family**  string | If the service has different generations of hardware, for the same SKU, then that can be used here |
| **name**  string / required | Name of the database SKU, typically, a letter + Number code, e.g. P3 |
| **size**  string | Size of the particular SKU |
| **tier**  string | The tier or edition of the particular SKU, e.g. Basic, Premium |
| **source_database_deletion_date**  string | Required if *create_mode=restore* and *source_database_id* is the deleted database’s original resource id when it existed (as opposed to its current restorable dropped database ID), then this value is required. Specifies the time that the database was deleted. |
| **source_database_id**  string | Required unless *create_mode=default* or *create_mode=restore_long_term_retention_backup*.  Specifies the resource ID of the source database. |
| **state**  string | Assert the state of the SQL Database. Use `present` to create or update an SQL Database and `absent` to delete it.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |
| **zone_redundant**  boolean | Is this database is zone redundant? It means the replicas of this database will be spread across multiple availability zones.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](azure_rm_sqldatabase_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_sqldatabase_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_sqldatabase_module.md#id6)

```yaml+jinja
- name: Create (or update) SQL Database
  azure_rm_sqldatabase:
    resource_group: myResourceGroup
    server_name: sqlcrudtest-5961
    name: testdb
    location: eastus

- name: Restore SQL Database
  azure_rm_sqldatabase:
    resource_group: myResourceGroup
    server_name: sqlcrudtest-5961
    name: restoreddb
    location: eastus
    create_mode: restore
    restorable_dropped_database_id: "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Sql/s
                                     ervers/testsvr/restorableDroppedDatabases/testdb2,131444841315030000"

- name: Create SQL Database in Copy Mode
  azure_rm_sqldatabase:
    resource_group: myResourceGroup
    server_name: sqlcrudtest-5961
    name: copydb
    location: eastus
    create_mode: copy
    source_database_id: "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Sql/servers/tests
                         vr/databases/testdb"

- name: Create (or update) SQL Database with SKU
  azure_rm_sqldatabase:
    resource_group: myResourceGroup
    server_name: sqlcrudtest-5961
    name: testdb
    location: eastus
    sku:
      name: S0
```

## [Return Values](azure_rm_sqldatabase_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **database_id**  string | The ID of the database.  **Returned:** always  **Sample:** `"database_id"` |
| **id**  string | Resource ID.  **Returned:** always  **Sample:** `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Sql/servers/sqlcrudtest-5961/databases/t estdb"` |
| **status**  string | The status of the database.  **Returned:** always  **Sample:** `"Online"` |

### Authors

- Zim Kalinowski (@zikalino)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
