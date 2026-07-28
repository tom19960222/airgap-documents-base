---
collection: ansible
version: "6"
title: "azure.azcollection.azure_keyvault_secret lookup – Read secret from Azure Key Vault."
source_url: https://docs.ansible.com/projects/ansible/6/collections/azure/azcollection/azure_keyvault_secret_lookup.html
fetched_at: 2026-07-27T16:43:22+00:00
---
# azure.azcollection.azure_keyvault_secret lookup – Read secret from Azure Key Vault.

> **Note:**
>
> This lookup plugin is part of the [azure.azcollection collection](https://galaxy.ansible.com/azure/azcollection) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install azure.azcollection`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](azure_keyvault_secret_lookup.md#ansible-collections-azure-azcollection-azure-keyvault-secret-lookup-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_keyvault_secret`.

New in azure.azcollection 1.12.0

- [Synopsis](azure_keyvault_secret_lookup.md#synopsis)
- [Requirements](azure_keyvault_secret_lookup.md#requirements)
- [Terms](azure_keyvault_secret_lookup.md#terms)
- [Keyword parameters](azure_keyvault_secret_lookup.md#keyword-parameters)
- [Notes](azure_keyvault_secret_lookup.md#notes)
- [Return Value](azure_keyvault_secret_lookup.md#return-value)

## [Synopsis](azure_keyvault_secret_lookup.md#id1)

- This lookup returns the content of secret saved in Azure Key Vault.
- When ansible host is MSI enabled Azure VM, user don’t need provide any credential to access to Azure Key Vault.

## [Requirements](azure_keyvault_secret_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- requests
- azure
- msrest

## [Terms](azure_keyvault_secret_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | Secret name, version can be included like secret_name/secret_version. |

## [Keyword parameters](azure_keyvault_secret_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('azure.azcollection.azure_keyvault_secret', key1=value1, key2=value2, ...)` and `query('azure.azcollection.azure_keyvault_secret', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **client_id**  string | Client id of service principal that has access to the Azure Key Vault |
| **secret**  string | Secret of the service principal. |
| **tenant_id**  string | Tenant id of service principal. |
| **vault_url**  string / required | Url of Azure Key Vault. |

## [Notes](azure_keyvault_secret_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('azure.azcollection.azure_keyvault_secret', term1, term2, key1=value1, key2=value2)` and `query('azure.azcollection.azure_keyvault_secret', term1, term2, key1=value1, key2=value2)`
> - If version is not provided, this plugin will return the latest version of the secret.
> - If ansible is running on Azure Virtual Machine with MSI enabled, client_id, secret and tenant isn’t required.
> - For enabling MSI on Azure VM, please refer to this doc <https://docs.microsoft.com/en-us/azure/active-directory/managed-service-identity/>
> - After enabling MSI on Azure VM, remember to grant access of the Key Vault to the VM by adding a new Acess Policy in Azure Portal.
> - If MSI is not enabled on ansible host, it’s required to provide a valid service principal which has access to the key vault.
> - To use a plugin from a collection, please reference the full namespace, collection name, and lookup plugin name that you want to use.

## [Return Value](azure_keyvault_secret_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  string | secret content string  Returned: success |

### Authors

- Hai Cao

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/azure/issues)
[Homepage](https://azure.microsoft.com)
[Repository (Sources)](https://github.com/ansible-collections/azure)
