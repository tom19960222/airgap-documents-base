---
collection: ansible
version: "6"
title: "azure.azcollection.azure_rm_cosmosdbaccount module – Manage Azure Database Account instance"
source_url: https://docs.ansible.com/projects/ansible/6/collections/azure/azcollection/azure_rm_cosmosdbaccount_module.html
fetched_at: 2026-07-27T16:46:03+00:00
---
# azure.azcollection.azure_rm_cosmosdbaccount module – Manage Azure Database Account instance

> **Note:**
>
> This module is part of the [azure.azcollection collection](https://galaxy.ansible.com/azure/azcollection) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install azure.azcollection`.
> You need further requirements to be able to use this module,
> see [Requirements](azure_rm_cosmosdbaccount_module.md#ansible-collections-azure-azcollection-azure-rm-cosmosdbaccount-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_cosmosdbaccount`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_cosmosdbaccount_module.md#synopsis)
- [Requirements](azure_rm_cosmosdbaccount_module.md#requirements)
- [Parameters](azure_rm_cosmosdbaccount_module.md#parameters)
- [Notes](azure_rm_cosmosdbaccount_module.md#notes)
- [See Also](azure_rm_cosmosdbaccount_module.md#see-also)
- [Examples](azure_rm_cosmosdbaccount_module.md#examples)
- [Return Values](azure_rm_cosmosdbaccount_module.md#return-values)

## [Synopsis](azure_rm_cosmosdbaccount_module.md#id1)

- Create, update and delete instance of Azure Database Account.

## [Requirements](azure_rm_cosmosdbaccount_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_cosmosdbaccount_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  added in azure.azcollection 0.0.1 | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  added in azure.azcollection 0.0.1 | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  Default: `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  Choices:   - `false` - `true` ← (default) |
| **auth_source**  string  added in azure.azcollection 0.0.1 | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  Choices:   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  added in azure.azcollection 0.0.1 | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  Choices:   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  added in azure.azcollection 0.0.1 | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  Default: `"AzureCloud"` |
| **consistency_policy**  string | The consistency policy for the Cosmos DB account. |
| **default_consistency_level**  string | The default consistency level and configuration settings of the Cosmos DB account.  Required when *state=present*.  Choices:   - `"eventual"` - `"session"` - `"bounded_staleness"` - `"strong"` - `"consistent_prefix"` |
| **max_interval_in_seconds**  integer | When used with the Bounded Staleness consistency level, this value represents the time amount of staleness (in seconds) tolerated.  Accepted range for this value is 5 - 86400. Required when *default_consistency_policy=bounded_staleness*. |
| **max_staleness_prefix**  integer | When used with the Bounded Staleness consistency level, this value represents the number of stale requests tolerated.  Accepted range for this value is 1 - 2,147,483,647. Required when *default_consistency_policy=bounded_staleness*. |
| **database_account_offer_type**  string | Database account offer type, for example *Standard*  Required when *state=present*. |
| **enable_automatic_failover**  boolean | Enables automatic failover of the write region in the rare event that the region is unavailable due to an outage.  Automatic failover will result in a new write region for the account and is chosen based on the failover priorities configured for the account.  Choices:   - `false` - `true` |
| **enable_cassandra**  boolean | Enable Cassandra.  Choices:   - `false` - `true` |
| **enable_free_tier**  boolean  added in azure.azcollection 1.10.0 | If enabled the account is free-tier.  Choices:   - `false` ← (default) - `true` |
| **enable_gremlin**  boolean | Enable Gremlin.  Choices:   - `false` - `true` |
| **enable_multiple_write_locations**  boolean | Enables the account to write in multiple locations  Choices:   - `false` - `true` |
| **enable_table**  boolean | Enable Table.  Choices:   - `false` - `true` |
| **geo_rep_locations**  list / elements=string | An array that contains the georeplication locations enabled for the Cosmos DB account.  Required when *state=present*. |
| **failover_priority**  integer | The failover priority of the region. A failover priority of 0 indicates a write region.  The maximum value for a failover priority = (total number of regions - 1).  Failover priority values must be unique for each of the regions in which the database account exists. |
| **name**  string | The name of the region. |
| **ip_range_filter**  string | (deprecated) Cosmos DB Firewall support. This value specifies the set of IP addresses or IP address ranges.  In CIDR form to be included as the allowed list of client IPs for a given database account.  IP addresses/ranges must be comma separated and must not contain any spaces.  This value has been deprecated, and will be removed in a later version. Use *ip_rules* instead. |
| **ip_rules**  list / elements=string  added in azure.azcollection 1.10.0 | The IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IPs. |
| **is_virtual_network_filter_enabled**  boolean | Flag to indicate whether to enable/disable Virtual Network ACL rules.  Choices:   - `false` - `true` |
| **kind**  string | Indicates the type of database account. This can only be set at database account creation.  Choices:   - `"global_document_db"` - `"mongo_db"` - `"parse"` |
| **location**  string | The location of the resource group to which the resource belongs.  Required when *state=present*. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **mongo_version**  string  added in azure.azcollection 1.10.0 | Server version for the MongoDB account, such as c(3.2) or c(4.0).  Only used when c(kind) = i(mongo_db). |
| **name**  string / required | Cosmos DB database account name. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **public_network_access**  string  added in azure.azcollection 1.10.0 | Enables or disables public network access to server.  Choices:   - `"Enabled"` ← (default) - `"Disabled"` |
| **resource_group**  string / required | Name of an Azure resource group. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **state**  string | Assert the state of the Database Account.  Use `present` to create or update an Database Account and `absent` to delete it.  Choices:   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **virtual_network_rules**  list / elements=string | List of Virtual Network ACL rules configured for the Cosmos DB account. |
| **ignore_missing_v_net_service_endpoint**  boolean | Create Cosmos DB account without existing virtual network service endpoint.  Choices:   - `false` - `true` |
| **subnet**  string | It can be a string containing resource id of a subnet.  It can be a dictionary containing ‘resource_group’, ‘virtual_network_name’ and ‘subnet_name’ |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_cosmosdbaccount_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_cosmosdbaccount_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_cosmosdbaccount_module.md#id6)

```yaml+jinja
- name: Create Cosmos DB Account - min
  azure_rm_cosmosdbaccount:
    resource_group: myResourceGroup
    name: myDatabaseAccount
    location: westus
    geo_rep_locations:
      - name: southcentralus
        failover_priority: 0
    database_account_offer_type: Standard

- name: Create Cosmos DB Account - max
  azure_rm_cosmosdbaccount:
    resource_group: myResourceGroup
    name: myDatabaseAccount
    location: westus
    kind: mongo_db
    geo_rep_locations:
      - name: southcentralus
        failover_priority: 0
    database_account_offer_type: Standard
    ip_rules:
      - 10.10.10.10
    enable_multiple_write_locations: yes
    virtual_network_rules:
      - subnet: "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/myVi
                 rtualNetwork/subnets/mySubnet"
    consistency_policy:
      default_consistency_level: bounded_staleness
      max_staleness_prefix: 10
      max_interval_in_seconds: 1000
```

## [Return Values](azure_rm_cosmosdbaccount_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | The unique resource identifier of the database account.  Returned: always  Sample: `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.DocumentDB/databaseAccounts/myData baseAccount"` |

### Authors

- Zim Kalinowski (@zikalino)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/azure/issues)
[Homepage](https://azure.microsoft.com)
[Repository (Sources)](https://github.com/ansible-collections/azure)
