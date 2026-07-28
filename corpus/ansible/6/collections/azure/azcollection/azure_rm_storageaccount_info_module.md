---
collection: ansible
version: "6"
title: "azure.azcollection.azure_rm_storageaccount_info module – Get storage account facts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/azure/azcollection/azure_rm_storageaccount_info_module.html
fetched_at: 2026-07-27T16:47:09+00:00
---
# azure.azcollection.azure_rm_storageaccount_info module – Get storage account facts

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
> see [Requirements](azure_rm_storageaccount_info_module.md#ansible-collections-azure-azcollection-azure-rm-storageaccount-info-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_storageaccount_info`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_storageaccount_info_module.md#synopsis)
- [Requirements](azure_rm_storageaccount_info_module.md#requirements)
- [Parameters](azure_rm_storageaccount_info_module.md#parameters)
- [Notes](azure_rm_storageaccount_info_module.md#notes)
- [See Also](azure_rm_storageaccount_info_module.md#see-also)
- [Examples](azure_rm_storageaccount_info_module.md#examples)
- [Return Values](azure_rm_storageaccount_info_module.md#return-values)

## [Synopsis](azure_rm_storageaccount_info_module.md#id1)

- Get facts for one storage account or all storage accounts within a resource group.

## [Requirements](azure_rm_storageaccount_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_storageaccount_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  added in azure.azcollection 0.0.1 | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  added in azure.azcollection 0.0.1 | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  Default: `"latest"` |
| **auth_source**  string  added in azure.azcollection 0.0.1 | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  Choices:   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  added in azure.azcollection 0.0.1 | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  Choices:   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  added in azure.azcollection 0.0.1 | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  Default: `"AzureCloud"` |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string | Only show results for a specific account. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **resource_group**  aliases: resource_group_name  string | Limit results to a resource group. Required when filtering by name. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **show_blob_cors**  boolean | Show the blob CORS settings for each blob related to the storage account.  Querying all storage accounts will take a long time.  Choices:   - `false` - `true` |
| **show_connection_string**  boolean | Show the connection string for each of the storageaccount’s endpoints.  For convenient usage, `show_connection_string` will also show the access keys for each of the storageaccount’s endpoints.  Note that it will cost a lot of time when list all storageaccount rather than query a single one.  Choices:   - `false` - `true` |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  list / elements=string | Limit results by providing a list of tags. Format tags as ‘key’ or ‘key:value’. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_storageaccount_info_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_storageaccount_info_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_storageaccount_info_module.md#id6)

```yaml+jinja
- name: Get facts for one account
  azure_rm_storageaccount_info:
    resource_group: myResourceGroup
    name: clh0002

- name: Get facts for all accounts in a resource group
  azure_rm_storageaccount_info:
    resource_group: myResourceGroup

- name: Get facts for all accounts by tags
  azure_rm_storageaccount_info:
    tags:
      - testing
      - foo:bar
```

## [Return Values](azure_rm_storageaccount_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **azure_storageaccounts**  list / elements=string | List of storage account dicts.  Returned: always  Sample: `[{"id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/myResourceGroups/testing/providers/Microsoft.Storage/storageAccounts/testaccount001", "location": "eastus2", "name": "testaccount001", "properties": {"accountType": "Standard_LRS", "creationTime": "2016-03-28T02:46:58.290113Z", "primaryEndpoints": {"blob": "https://testaccount001.blob.core.windows.net/", "file": "https://testaccount001.file.core.windows.net/", "queue": "https://testaccount001.queue.core.windows.net/", "table": "https://testaccount001.table.core.windows.net/"}, "primaryLocation": "eastus2", "provisioningState": "Succeeded", "statusOfPrimary": "Available"}, "tags": {}, "type": "Microsoft.Storage/storageAccounts"}]` |
| **storageaccounts**  complex | List of storage account dicts in resource module’s parameter format.  Returned: always |
| **access_tier**  string | The access tier for this storage account.  Returned: always  Sample: `"Hot"` |
| **account_type**  string | Type of storage account.  `Standard_ZRS` and `Premium_LRS` accounts cannot be changed to other account types.  Other account types cannot be changed to `Standard_ZRS` or `Premium_LRS`.  Returned: always  Sample: `"Standard_ZRS"` |
| **allow_blob_public_access**  boolean | Public access to all blobs or containers in the storage account allowed or disallowed.  Returned: always  Sample: `true` |
| **custom_domain**  complex | User domain assigned to the storage account.  Must be a dictionary with *name* and *use_sub_domain* keys where *name* is the CNAME source.  Returned: always |
| **name**  string | CNAME source.  Returned: always  Sample: `"testaccount"` |
| **use_sub_domain**  boolean | Whether to use sub domain.  Returned: always  Sample: `true` |
| **encryption**  complex | The encryption settings on the storage account.  Returned: always |
| **key_source**  string | The encryption keySource (provider).  Returned: always  Sample: `"Microsoft.Storage"` |
| **require_infrastructure_encryption**  boolean | A boolean indicating whether or not the service applies a secondary layer of encryption with platform managed keys for data at rest.  Returned: always  Sample: `false` |
| **services**  dictionary | List of services which support encryption.  Returned: always |
| **blob**  dictionary | The encryption function of the blob storage service.  Returned: always  Sample: `{"enabled": true}` |
| **file**  dictionary | The encryption function of the file storage service.  Returned: always  Sample: `{"enabled": true}` |
| **queue**  dictionary | The encryption function of the queue storage service.  Returned: always  Sample: `{"enabled": true}` |
| **table**  dictionary | The encryption function of the table storage service.  Returned: always  Sample: `{"enabled": true}` |
| **https_only**  boolean | Allows https traffic only to storage service when set to `true`.  Returned: always  Sample: `false` |
| **id**  string | Resource ID.  Returned: always  Sample: `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Storage/storageAccounts/t estaccount001"` |
| **is_hns_enabled**  boolean | Account HierarchicalNamespace enabled if sets to true.  Returned: always  Sample: `true` |
| **kind**  string | The kind of storage.  Returned: always  Sample: `"Storage"` |
| **location**  string | Valid Azure location. Defaults to location of the resource group.  Returned: always  Sample: `"eastus"` |
| **minimum_tls_version**  string | The minimum TLS version permitted on requests to storage.  Returned: always  Sample: `"TLS1_2"` |
| **name**  string | Name of the storage account to update or create.  Returned: always  Sample: `"testaccount001"` |
| **network_acls**  dictionary | A set of firewall and virtual network rules  Returned: always  Sample: `{"bypass": "AzureServices", "default_action": "Deny", "ip_rules": [{"action": "Allow", "value": "1.2.3.4"}, {"action": "Allow", "value": "123.234.123.0/24"}], "virtual_network_rules": [{"action": "Allow", "id": "/subscriptions/mySubscriptionId/resourceGroups/myResourceGroup/                                     providers/Microsoft.Network/virtualNetworks/myVnet/subnets/mySubnet"}]}` |
| **primary_endpoints**  complex | URLs to retrieve a public *blob*, *file*, *queue*, or *table* object.  Note that `Standard_ZRS` and `Premium_LRS` accounts only return the blob endpoint.  Returned: always |
| **blob**  complex | The primary blob endpoint and connection string.  Returned: always |
| **connectionstring**  string | Connectionstring of the blob endpoint.  Returned: always  Sample: `"DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=X;AccountKey=X;BlobEndpoint=X"` |
| **endpoint**  string | The primary blob endpoint.  Returned: always  Sample: `"https://testaccount001.blob.core.windows.net/"` |
| **file**  complex | The primary file endpoint and connection string.  Returned: always |
| **connectionstring**  string | Connectionstring of the file endpoint.  Returned: always  Sample: `"DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=X;AccountKey=X;FileEndpoint=X"` |
| **endpoint**  string | The primary file endpoint.  Returned: always  Sample: `"https://testaccount001.file.core.windows.net/"` |
| **key**  string | The account key for the primary_endpoints  Returned: always  Sample: `"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"` |
| **queue**  complex | The primary queue endpoint and connection string.  Returned: always |
| **connectionstring**  string | Connectionstring of the queue endpoint.  Returned: always  Sample: `"DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=X;AccountKey=X;QueueEndpoint=X"` |
| **endpoint**  string | The primary queue endpoint.  Returned: always  Sample: `"https://testaccount001.queue.core.windows.net/"` |
| **table**  complex | The primary table endpoint and connection string.  Returned: always |
| **connectionstring**  string | Connectionstring of the table endpoint.  Returned: always  Sample: `"DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=X;AccountKey=X;TableEndpoint=X"` |
| **endpoint**  string | The primary table endpoint.  Returned: always  Sample: `"https://testaccount001.table.core.windows.net/"` |
| **primary_location**  string | The location of the primary data center for the storage account.  Returned: always  Sample: `"eastus"` |
| **provisioning_state**  string | The status of the storage account at the time the operation was called.  Possible values include `Creating`, `ResolvingDNS`, `Succeeded`.  Returned: always  Sample: `"Succeeded"` |
| **public_network_access**  string | Public network access to Storage Account allowed or disallowed.  Returned: always  Sample: `"Enabled"` |
| **secondary_endpoints**  complex | The URLs to retrieve a public *blob*, *file*, *queue*, or *table* object from the secondary location.  Only available if the SKU *name=Standard_RAGRS*.  Returned: always |
| **blob**  complex | The secondary blob endpoint and connection string.  Returned: always |
| **connectionstring**  string | Connectionstring of the blob endpoint.  Returned: always  Sample: `"DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=X;AccountKey=X;BlobEndpoint=X"` |
| **endpoint**  string | The secondary blob endpoint.  Returned: always  Sample: `"https://testaccount001.blob.core.windows.net/"` |
| **file**  complex | The secondary file endpoint and connection string.  Returned: always |
| **connectionstring**  string | Connectionstring of the file endpoint.  Returned: always  Sample: `"DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=X;AccountKey=X;FileEndpoint=X"` |
| **endpoint**  string | The secondary file endpoint.  Returned: always  Sample: `"https://testaccount001.file.core.windows.net/"` |
| **key**  string | The account key for the secondary_endpoints  Returned: success  Sample: `"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"` |
| **queue**  complex | The secondary queue endpoint and connection string.  Returned: always |
| **connectionstring**  string | Connectionstring of the queue endpoint.  Returned: always  Sample: `"DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=X;AccountKey=X;QueueEndpoint=X"` |
| **endpoint**  string | The secondary queue endpoint.  Returned: always  Sample: `"https://testaccount001.queue.core.windows.net/"` |
| **table**  complex | The secondary table endpoint and connection string.  Returned: always |
| **connectionstring**  string | Connectionstring of the table endpoint.  Returned: always  Sample: `"DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=X;AccountKey=X;TableEndpoint=X"` |
| **endpoint**  string | The secondary table endpoint.  Returned: always  Sample: `"https://testaccount001.table.core.windows.net/"` |
| **secondary_location**  string | The location of the geo-replicated secondary for the storage account.  Only available if the *account_type=Standard_GRS* or *account_type=Standard_RAGRS*.  Returned: always  Sample: `"westus"` |
| **static_website**  complex  added in azure.azcollection 1.13.0 | Static website configuration for the storage account.  Returned: always |
| **enabled**  boolean | Whether this account is hosting a static website.  Returned: always  Sample: `true` |
| **error_document404_path**  string | The absolute path of the custom 404 page.  Returned: always  Sample: `"error.html"` |
| **index_document**  string | The default name of the index page under each directory.  Returned: always  Sample: `"index.html"` |
| **status_of_primary**  string | Status of the primary location of the storage account; either `available` or `unavailable`.  Returned: always  Sample: `"available"` |
| **status_of_secondary**  string | Status of the secondary location of the storage account; either `available` or `unavailable`.  Returned: always  Sample: `"available"` |
| **tags**  dictionary | Resource tags.  Returned: always  Sample: `{"tag1": "abc"}` |

### Authors

- Chris Houseknecht (@chouseknecht)
- Matt Davis (@nitzmahone)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/azure/issues)
[Homepage](https://azure.microsoft.com)
[Repository (Sources)](https://github.com/ansible-collections/azure)
