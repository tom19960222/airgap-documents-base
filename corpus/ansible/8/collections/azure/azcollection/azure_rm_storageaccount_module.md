---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_storageaccount module – Manage Azure storage accounts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_storageaccount_module.html
fetched_at: 2026-07-28T01:14:55+00:00
---
# azure.azcollection.azure_rm_storageaccount module – Manage Azure storage accounts

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
> see [Requirements](azure_rm_storageaccount_module.md#ansible-collections-azure-azcollection-azure-rm-storageaccount-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_storageaccount`.

New in azure.azcollection 0.1.0

- [Synopsis](azure_rm_storageaccount_module.md#synopsis)
- [Requirements](azure_rm_storageaccount_module.md#requirements)
- [Parameters](azure_rm_storageaccount_module.md#parameters)
- [Notes](azure_rm_storageaccount_module.md#notes)
- [See Also](azure_rm_storageaccount_module.md#see-also)
- [Examples](azure_rm_storageaccount_module.md#examples)
- [Return Values](azure_rm_storageaccount_module.md#return-values)

## [Synopsis](azure_rm_storageaccount_module.md#id1)

- Create, update or delete a storage account.

## [Requirements](azure_rm_storageaccount_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_storageaccount_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_tier**  string | The access tier for this storage account. Required when *kind=BlobStorage*.  **Choices:**   - `"Hot"` - `"Cool"` |
| **account_type**  aliases: type  string | Type of storage account. Required when creating a storage account.  `Standard_ZRS` and `Premium_LRS` accounts cannot be changed to other account types.  Other account types cannot be changed to `Standard_ZRS` or `Premium_LRS`.  **Choices:**   - `"Premium_LRS"` - `"Standard_GRS"` - `"Standard_LRS"` - `"Standard_RAGRS"` - `"Standard_ZRS"` - `"Premium_ZRS"` - `"Standard_RAGZRS"` - `"Standard_GZRS"` |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **allow_blob_public_access**  boolean  *added in azure.azcollection 1.1.0* | Allows blob containers in account to be set for anonymous public access.  If set to false, no containers in this account will be able to allow anonymous public access.  If omitted, new account creation will default to null which is currently interpreted to True. Existing accounts will not be modified.  **Choices:**   - `false` - `true` |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  **Choices:**   - `false` - `true` ← (default) |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **blob_cors**  list / elements=dictionary | Specifies CORS rules for the Blob service.  You can include up to five CorsRule elements in the request.  If no blob_cors elements are included in the argument list, nothing about CORS will be changed.  If you want to delete all CORS rules and disable CORS for the Blob service, explicitly set *blob_cors=[]*. |
| **allowed_headers**  list / elements=string / required | A list of headers allowed to be part of the cross-origin request. |
| **allowed_methods**  list / elements=string / required | A list of HTTP methods that are allowed to be executed by the origin. |
| **allowed_origins**  list / elements=string / required | A list of origin domains that will be allowed via CORS, or “\*” to allow all domains. |
| **exposed_headers**  list / elements=string / required | A list of response headers to expose to CORS clients. |
| **max_age_in_seconds**  integer / required | The number of seconds that the client/browser should cache a preflight response. |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **custom_domain**  aliases: custom_dns_domain_suffix  dictionary | User domain assigned to the storage account.  Must be a dictionary with *name* and *use_sub_domain* keys where *name* is the CNAME source.  Only one custom domain is supported per storage account at this time.  To clear the existing custom domain, use an empty string for the custom domain name property.  Can be added to an existing storage account. Will be ignored during storage account creation. |
| **encryption**  dictionary | The encryption settings on the storage account. |
| **key_source**  string | The encryption keySource (provider).  **Choices:**   - `"Microsoft.Storage"` ← (default) - `"Microsoft.Keyvault"` |
| **require_infrastructure_encryption**  boolean | A boolean indicating whether or not the service applies a secondary layer of encryption with platform managed keys for data at rest.  **Choices:**   - `false` - `true` |
| **services**  dictionary | List of services which support encryption. |
| **blob**  dictionary | The encryption function of the blob storage service. |
| **enabled**  boolean | Whether to encrypt the blob type.  **Choices:**   - `false` - `true` |
| **file**  dictionary | The encryption function of the file storage service. |
| **enabled**  boolean | Whether to encrypt the file type.  **Choices:**   - `false` - `true` |
| **queue**  dictionary | The encryption function of the queue storage service. |
| **enabled**  boolean | Whether to encrypt the queue type.  **Choices:**   - `false` - `true` |
| **table**  dictionary | The encryption function of the table storage service. |
| **enabled**  boolean | Whether to encrypt the table type.  **Choices:**   - `false` - `true` |
| **force_delete_nonempty**  aliases: force  boolean | Attempt deletion if resource already exists and cannot be updated.  **Choices:**   - `false` ← (default) - `true` |
| **https_only**  boolean | Allows https traffic only to storage service when set to `True`.  If omitted, new account creation will default to True, while existing accounts will not be change.  **Choices:**   - `false` - `true` |
| **is_hns_enabled**  boolean | Account HierarchicalNamespace enabled if sets to true.  When *is_hns_enabled=True*, *kind* cannot be `Storage`.  **Choices:**   - `false` - `true` |
| **kind**  string | The kind of storage.  The `FileStorage` and (BlockBlobStorage) only used when *account_type=Premium_LRS* or *account_type=Premium_ZRS*.  **Choices:**   - `"Storage"` ← (default) - `"StorageV2"` - `"BlobStorage"` - `"BlockBlobStorage"` - `"FileStorage"` |
| **location**  string | Valid Azure location. Defaults to location of the resource group. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **minimum_tls_version**  string  *added in azure.azcollection 1.0.0* | The minimum required version of Transport Layer Security (TLS) for requests to a storage account.  If omitted, new account creation will default to null which is currently interpreted to TLS1_0. Existing accounts will not be modified.  **Choices:**   - `"TLS1_0"` - `"TLS1_1"` - `"TLS1_2"` |
| **name**  string / required | Name of the storage account to update or create. |
| **network_acls**  dictionary | Manages the Firewall and virtual networks settings of the storage account. |
| **bypass**  string | When *default_action=Deny* this controls which Azure components can still reach the Storage Account.  The list is comma separated.  It can be any combination of the example `AzureServices`, `Logging`, `Metrics`.  If no Azure components are allowed, explicitly set *bypass=””*.  **Default:** `"AzureServices"` |
| **default_action**  string | Default firewall traffic rule.  If *default_action=Allow* no other settings have effect.  **Choices:**   - `"Allow"` ← (default) - `"Deny"` |
| **ip_rules**  list / elements=dictionary | A list of IP addresses or ranges in CIDR format. |
| **action**  string | The only logical *action=Allow* because this setting is only accessible when *default_action=Deny*.  **Default:** `"Allow"` |
| **value**  string | The IP address or range. |
| **virtual_network_rules**  list / elements=dictionary | A list of subnets and their actions. |
| **action**  string | The only logical *action=Allow* because this setting is only accessible when *default_action=Deny*.  **Default:** `"Allow"` |
| **id**  string | The complete path to the subnet. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **public_network_access**  string  *added in azure.azcollection 1.12.0* | Allow or disallow public network access to Storage Account.  **Choices:**   - `"Enabled"` - `"Disabled"` |
| **resource_group**  aliases: resource_group_name  string / required | Name of the resource group to use. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **state**  string | State of the storage account. Use `present` to create or update a storage account and use `absent` to delete an account.  `failover` is used to failover the storage account to its secondary. This process can take up to a hour.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"failover"` |
| **static_website**  dictionary  *added in azure.azcollection 1.13.0* | Manage static website configuration for the storage account. |
| **enabled**  boolean | Indicates whether this account is hosting a static website.  **Choices:**   - `false` ← (default) - `true` |
| **error_document404_path**  string | The absolute path of the custom 404 page. |
| **index_document**  string | The default name of the index page under each directory. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_storageaccount_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_storageaccount_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_storageaccount_module.md#id6)

```yaml+jinja
- name: remove account, if it exists
  azure_rm_storageaccount:
    resource_group: myResourceGroup
    name: clh0002
    state: absent

- name: create an account
  azure_rm_storageaccount:
    resource_group: myResourceGroup
    name: clh0002
    type: Standard_RAGRS
    tags:
      testing: testing
      delete: on-exit

- name: Create an account with kind of FileStorage
  azure_rm_storageaccount:
    resource_group: myResourceGroup
    name: c1h0002
    type: Premium_LRS
    kind: FileStorage
    tags:
      testing: testing

- name: configure firewall and virtual networks
  azure_rm_storageaccount:
    resource_group: myResourceGroup
    name: clh0002
    type: Standard_RAGRS
    network_acls:
      bypass: AzureServices,Metrics
      default_action: Deny
      virtual_network_rules:
        - id: /subscriptions/mySubscriptionId/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/myVnet/subnets/mySubnet
          action: Allow
      ip_rules:
        - value: 1.2.3.4
          action: Allow
        - value: 123.234.123.0/24
          action: Allow

- name: create an account with blob CORS
  azure_rm_storageaccount:
    resource_group: myResourceGroup
    name: clh002
    type: Standard_RAGRS
    blob_cors:
      - allowed_origins:
          - http://www.example.com/
        allowed_methods:
          - GET
          - POST
        allowed_headers:
          - x-ms-meta-data*
          - x-ms-meta-target*
          - x-ms-meta-abc
        exposed_headers:
          - x-ms-meta-*
        max_age_in_seconds: 200
```

## [Return Values](azure_rm_storageaccount_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **state**  complex | Current state of the storage account.  **Returned:** always |
| **account_type**  string | Type of storage account.  **Returned:** always  **Sample:** `"Standard_RAGRS"` |
| **allow_blob_public_access**  boolean | Public access to all blobs or containers in the storage account allowed or disallowed.  **Returned:** always  **Sample:** `true` |
| **custom_domain**  complex | User domain assigned to the storage account.  **Returned:** always |
| **name**  string | CNAME source.  **Returned:** always  **Sample:** `"testaccount"` |
| **use_sub_domain**  boolean | Whether to use sub domain.  **Returned:** always  **Sample:** `true` |
| **encryption**  complex | The encryption settings on the storage account.  **Returned:** always |
| **key_source**  string | The encryption keySource (provider).  **Returned:** always  **Sample:** `"Microsoft.Storage"` |
| **require_infrastructure_encryption**  boolean | A boolean indicating whether or not the service applies a secondary layer of encryption with platform managed keys for data at rest.  **Returned:** always  **Sample:** `false` |
| **services**  dictionary | List of services which support encryption.  **Returned:** always |
| **blob**  dictionary | The encryption function of the blob storage service.  **Returned:** always  **Sample:** `{"enabled": true}` |
| **file**  dictionary | The encryption function of the file storage service.  **Returned:** always  **Sample:** `{"enabled": true}` |
| **queue**  dictionary | The encryption function of the queue storage service.  **Returned:** always  **Sample:** `{"enabled": true}` |
| **table**  dictionary | The encryption function of the table storage service.  **Returned:** always  **Sample:** `{"enabled": true}` |
| **failover_in_progress**  boolean | Status indicating the storage account is currently failing over to its secondary location.  **Returned:** always  **Sample:** `false` |
| **https_only**  boolean | Allows https traffic only to storage service when set to `true`.  **Returned:** always  **Sample:** `false` |
| **id**  string | Resource ID.  **Returned:** always  **Sample:** `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Storage/storageAccounts/clh0003"` |
| **is_hns_enabled**  boolean | Account HierarchicalNamespace enabled if sets to true.  **Returned:** always  **Sample:** `true` |
| **location**  string | Valid Azure location. Defaults to location of the resource group.  **Returned:** always  **Sample:** `"eastus2"` |
| **minimum_tls_version**  string | The minimum TLS version permitted on requests to storage.  **Returned:** always  **Sample:** `"TLS1_2"` |
| **name**  string | Name of the storage account to update or create.  **Returned:** always  **Sample:** `"clh0003"` |
| **network_acls**  dictionary | A set of firewall and virtual network rules  **Returned:** always  **Sample:** `{"bypass": "AzureServices", "default_action": "Deny", "ip_rules": [{"action": "Allow", "value": "1.2.3.4"}, {"action": "Allow", "value": "123.234.123.0/24"}], "virtual_network_rules": [{"action": "Allow", "id": "/subscriptions/mySubscriptionId/resourceGroups/myResourceGroup/                                    providers/Microsoft.Network/virtualNetworks/myVnet/subnets/mySubnet"}]}` |
| **primary_endpoints**  dictionary | The URLs to retrieve the public *blob*, *queue*, or *table* object from the primary location.  **Returned:** always  **Sample:** `{"blob": "https://clh0003.blob.core.windows.net/", "queue": "https://clh0003.queue.core.windows.net/", "table": "https://clh0003.table.core.windows.net/"}` |
| **primary_location**  string | The location of the primary data center for the storage account.  **Returned:** always  **Sample:** `"eastus2"` |
| **provisioning_state**  string | The status of the storage account.  Possible values include `Creating`, `ResolvingDNS`, `Succeeded`.  **Returned:** always  **Sample:** `"Succeeded"` |
| **public_network_access**  string | Public network access to Storage Account allowed or disallowed.  **Returned:** always  **Sample:** `"Enabled"` |
| **resource_group**  string | The resource group’s name.  **Returned:** always  **Sample:** `"Testing"` |
| **secondary_endpoints**  dictionary | The URLs to retrieve the public *blob*, *queue*, or *table* object from the secondary location.  **Returned:** always  **Sample:** `{"blob": "https://clh0003-secondary.blob.core.windows.net/", "queue": "https://clh0003-secondary.queue.core.windows.net/", "table": "https://clh0003-secondary.table.core.windows.net/"}` |
| **secondary_location**  string | The location of the geo-replicated secondary for the storage account.  **Returned:** always  **Sample:** `"centralus"` |
| **static_website**  complex  *added in azure.azcollection 1.13.0* | Static website configuration for the storage account.  **Returned:** always |
| **enabled**  boolean | Whether this account is hosting a static website.  **Returned:** always  **Sample:** `true` |
| **error_document404_path**  string | The absolute path of the custom 404 page.  **Returned:** always  **Sample:** `"error.html"` |
| **index_document**  string | The default name of the index page under each directory.  **Returned:** always  **Sample:** `"index.html"` |
| **status_of_primary**  string | The status of the primary location of the storage account; either `available` or `unavailable`.  **Returned:** always  **Sample:** `"available"` |
| **status_of_secondary**  string | The status of the secondary location of the storage account; either `available` or `unavailable`.  **Returned:** always  **Sample:** `"available"` |
| **tags**  dictionary | Resource tags.  **Returned:** always  **Sample:** `{"tags1": "value1"}` |
| **type**  string | The storage account type.  **Returned:** always  **Sample:** `"Microsoft.Storage/storageAccounts"` |

### Authors

- Chris Houseknecht (@chouseknecht)
- Matt Davis (@nitzmahone)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
