---
collection: ansible
version: "6"
title: "azure.azcollection.azure_rm_cognitivesearch module – Manage Azure Cognitive Search service"
source_url: https://docs.ansible.com/projects/ansible/6/collections/azure/azcollection/azure_rm_cognitivesearch_module.html
fetched_at: 2026-07-27T16:45:58+00:00
---
# azure.azcollection.azure_rm_cognitivesearch module – Manage Azure Cognitive Search service

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
> see [Requirements](azure_rm_cognitivesearch_module.md#ansible-collections-azure-azcollection-azure-rm-cognitivesearch-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_cognitivesearch`.

New in azure.azcollection 1.4.0

- [Synopsis](azure_rm_cognitivesearch_module.md#synopsis)
- [Requirements](azure_rm_cognitivesearch_module.md#requirements)
- [Parameters](azure_rm_cognitivesearch_module.md#parameters)
- [Notes](azure_rm_cognitivesearch_module.md#notes)
- [See Also](azure_rm_cognitivesearch_module.md#see-also)
- [Examples](azure_rm_cognitivesearch_module.md#examples)
- [Return Values](azure_rm_cognitivesearch_module.md#return-values)

## [Synopsis](azure_rm_cognitivesearch_module.md#id1)

- Create, update or delete Azure Cognitive Search service.

## [Requirements](azure_rm_cognitivesearch_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_cognitivesearch_module.md#id3)

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
| **hosting_mode**  string | Applicable only for the standard3 SKU.  You can set this property to enable up to 3 high density partitions that allow up to 1000 indexes.  For the standard3 SKU, the value is either ‘default’ or ‘highDensity’.  For all other SKUs, this value must be ‘default’.  Choices:   - `"default"` ← (default) - `"highDensity"` |
| **identity**  string | The identity for the resource.  Choices:   - `"None"` ← (default) - `"SystemAssigned"` |
| **location**  string | Valid azure location. Defaults to location of the resource group. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string / required | The name of the Azure Cognitive Search service.  Search service names must only contain lowercase letters, digits or dashes.  Cannot use dash as the first two or last one characters.  Cannot contain consecutive dashes.  Must be between 2 and 60 characters in length.  Search service names must be globally unique.  You cannot change the service name after the service is created. |
| **network_rule_set**  list / elements=string | Network specific rules that determine how the Azure Cognitive Search service may be reached. |
| **partition_count**  integer | The number of partitions in the search service.  It can be `1`, `2`, `3`, `4`, `6`, or `12`.  Values greater than 1 are only valid for standard SKUs.  For ‘standard3’ services with hostingMode set to ‘highDensity’, the allowed values are between 1 and 3.  Default: `1` |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **public_network_access**  string | This value can be set to `enabled` to avoid breaking changes on existing customer resources and templates.  If set to `enabled`, traffic over public interface is not allowed, and private endpoint connections would be the exclusive access method.  Choices:   - `"enabled"` ← (default) - `"disabled"` |
| **replica_count**  integer | The number of replicas in the search service.  It must be a value between 1 and 12 inclusive for *sku=standard*.  It must be a value between 1 and 3 inclusive for *sku=basic*.  Default: `1` |
| **resource_group**  string / required | The name of the resource group within the current subscription. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **sku**  string | The SKU of the Search Service, which determines price tier and capacity limits.  This property is required when creating a new Search Service.  Choices:   - `"free"` - `"basic"` ← (default) - `"standard"` - `"standard2"` - `"standard3"` - `"storage_optimized_l1"` - `"storage_optimized_l2"` |
| **state**  string | Assert the state of the search instance. Set to `present` to create or update a search instance. Set to `absent` to remove a search instance.  Choices:   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_cognitivesearch_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_cognitivesearch_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_cognitivesearch_module.md#id6)

```yaml+jinja
- name: Create Azure Cognitive Search
  azure_rm_cognitivesearch:
    resource_group: myResourceGroup
    name: myAzureSearch
```

## [Return Values](azure_rm_cognitivesearch_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **state**  dictionary | Info for Azure Cognitive Search.  Returned: always |
| **hosting_mode**  string | Type of hosting mode selected.  Returned: always  Sample: `"default"` |
| **id**  string | The unique identifier associated with this Azure Cognitive Search.  Returned: always  Sample: `"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"` |
| **identity**  dictionary | The identity of the Azure Cognitive Search Service.  Returned: always  Sample: `{"principal_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", "type": "SystemAssigned"}` |
| **principal_id**  string | Identifier assigned.  Returned: success  Sample: `"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"` |
| **type**  string | Identity type.  Returned: always  Sample: `"SystemAssigned"` |
| **location**  string | The geo-location where the Azure Cognitive Search Service lives.  Returned: always  Sample: `"West Europe"` |
| **name**  string | The name of the Azure Cognitive Search Service.  Returned: always  Sample: `"myazuresearch"` |
| **network_rule_set**  list / elements=string | Network specific rules that determine how the Azure Cognitive Search service may be reached.  Returned: always  Sample: `["1.1.1.1", "8.8.8.8/31"]` |
| **partition_count**  integer | The number of partitions in the Azure Cognitive Search Service.  Returned: always  Sample: `3` |
| **provisioning_state**  string | The state of the provisioning state of Azure Cognitive Search Service.  Returned: always  Sample: `"succeeded"` |
| **public_network_access**  string | If it’s allowed traffic over public interface.  Returned: always  Sample: `"enabled"` |
| **replica_count**  integer | The number of replicas in the Azure Cognitive Search Service.  Returned: always  Sample: `3` |
| **sku**  string | The SKU of the Azure Cognitive Search Service.  Returned: always  Sample: `"standard"` |
| **status**  string | The state of the Azure Cognitive Search.  Returned: always  Sample: `"Active running"` |
| **tags**  dictionary | The resource tags.  Returned: always  Sample: `{"tag1": "abc"}` |

### Authors

- David Duque Hernández (@next-davidduquehernandez)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/azure/issues)
[Homepage](https://azure.microsoft.com)
[Repository (Sources)](https://github.com/ansible-collections/azure)
