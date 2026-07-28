---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_resource module – Create any Azure resource"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_resource_module.html
fetched_at: 2026-07-28T01:14:34+00:00
---
# azure.azcollection.azure_rm_resource module – Create any Azure resource

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
> see [Requirements](azure_rm_resource_module.md#ansible-collections-azure-azcollection-azure-rm-resource-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_resource`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_resource_module.md#synopsis)
- [Requirements](azure_rm_resource_module.md#requirements)
- [Parameters](azure_rm_resource_module.md#parameters)
- [Notes](azure_rm_resource_module.md#notes)
- [See Also](azure_rm_resource_module.md#see-also)
- [Examples](azure_rm_resource_module.md#examples)
- [Return Values](azure_rm_resource_module.md#return-values)

## [Synopsis](azure_rm_resource_module.md#id1)

- Create, update or delete any Azure resource using Azure REST API.
- This module gives access to resources that are not supported via Ansible modules.
- Refer to <https://docs.microsoft.com/en-us/rest/api/> regarding details related to specific resource REST API.

## [Requirements](azure_rm_resource_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_resource_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **api_version**  string | Specific API version to be used. |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **body**  any | The body of the HTTP request/response to the web service. |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **idempotency**  boolean | If enabled, idempotency check will be done by using *method=GET* first and then comparing with *body*.  **Choices:**   - `false` ← (default) - `true` |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **method**  string | The HTTP method of the request or response. It must be uppercase.  **Choices:**   - `"GET"` - `"PUT"` ← (default) - `"POST"` - `"HEAD"` - `"PATCH"` - `"DELETE"` - `"MERGE"` |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **polling_interval**  integer | If enabled, idempotency check will be done by using *method=GET* first and then comparing with *body*.  **Default:** `60` |
| **polling_timeout**  integer | If enabled, idempotency check will be done by using *method=GET* first and then comparing with *body*.  **Default:** `0` |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **provider**  string | Provider type.  Required if URL is not specified. |
| **resource_group**  string | Resource group to be used.  Required if URL is not specified. |
| **resource_name**  string | Resource name.  Required if URL Is not specified. |
| **resource_type**  string | Resource type.  Required if URL is not specified. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **state**  string | Assert the state of the resource. Use `present` to create or update resource or `absent` to delete resource.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **status_code**  list / elements=integer | A valid, numeric, HTTP status code that signifies success of the request. Can also be comma separated list of status codes.  **Default:** `[200, 201, 202]` |
| **subresource**  list / elements=dictionary | List of subresources.  **Default:** `[]` |
| **name**  string | Subresource name. |
| **namespace**  string | Subresource namespace. |
| **type**  string | Subresource type. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **url**  string | Azure RM Resource URL. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_resource_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_resource_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_resource_module.md#id6)

```yaml+jinja
- name: Update scaleset info using azure_rm_resource
  azure_rm_resource:
    resource_group: myResourceGroup
    provider: compute
    resource_type: virtualmachinescalesets
    resource_name: myVmss
    api_version: "2017-12-01"
    body: { body }
```

## [Return Values](azure_rm_resource_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **response**  complex | Response specific to resource type.  **Returned:** always |
| **id**  string | Resource ID.  **Returned:** always  **Sample:** `"/subscriptions/xxxx...xxxx/resourceGroups/v-xisuRG/providers/Microsoft.Storage/storageAccounts/staccb57dc95183"` |
| **kind**  string | The kind of storage.  **Returned:** always  **Sample:** `"Storage"` |
| **location**  string | The resource location, defaults to location of the resource group.  **Returned:** always  **Sample:** `"eastus"` |
| **name**  string | The storage account name.  **Returned:** always  **Sample:** `"staccb57dc95183"` |
| **properties**  dictionary | The storage account’s related properties.  **Returned:** always  **Sample:** `{"creationTime": "2019-06-13T06:34:33.0996676Z", "encryption": {"keySource": "Microsoft.Storage", "services": {"blob": {"enabled": true, "lastEnabledTime": "2019-06-13T06:34:33.1934074Z"}, "file": {"enabled": true, "lastEnabledTime": "2019-06-13T06:34:33.1934074Z"}}}, "networkAcls": {"bypass": "AzureServices", "defaultAction": "Allow", "ipRules": [], "virtualNetworkRules": []}, "primaryEndpoints": {"blob": "https://staccb57dc95183.blob.core.windows.net/", "file": "https://staccb57dc95183.file.core.windows.net/", "queue": "https://staccb57dc95183.queue.core.windows.net/", "table": "https://staccb57dc95183.table.core.windows.net/"}, "primaryLocation": "eastus", "provisioningState": "Succeeded", "secondaryLocation": "westus", "statusOfPrimary": "available", "statusOfSecondary": "available", "supportsHttpsTrafficOnly": false}` |
| **sku**  dictionary | The storage account SKU.  **Returned:** always  **Sample:** `{"name": "Standard_GRS", "tier": "Standard"}` |
| **tags**  dictionary | Resource tags.  **Returned:** always  **Sample:** `{"key1": "value1"}` |
| **type**  string | The resource type.  **Returned:** always  **Sample:** `"Microsoft.Storage/storageAccounts"` |

### Authors

- Zim Kalinowski (@zikalino)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
