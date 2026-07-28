---
collection: ansible
version: "6"
title: "azure.azcollection.azure_rm_keyvault module – Manage Key Vault instance"
source_url: https://docs.ansible.com/projects/ansible/6/collections/azure/azcollection/azure_rm_keyvault_module.html
fetched_at: 2026-07-27T16:46:28+00:00
---
# azure.azcollection.azure_rm_keyvault module – Manage Key Vault instance

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
> see [Requirements](azure_rm_keyvault_module.md#ansible-collections-azure-azcollection-azure-rm-keyvault-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_keyvault`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_keyvault_module.md#synopsis)
- [Requirements](azure_rm_keyvault_module.md#requirements)
- [Parameters](azure_rm_keyvault_module.md#parameters)
- [Notes](azure_rm_keyvault_module.md#notes)
- [See Also](azure_rm_keyvault_module.md#see-also)
- [Examples](azure_rm_keyvault_module.md#examples)
- [Return Values](azure_rm_keyvault_module.md#return-values)

## [Synopsis](azure_rm_keyvault_module.md#id1)

- Create, update and delete instance of Key Vault.

## [Requirements](azure_rm_keyvault_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_keyvault_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_policies**  string | An array of 0 to 16 identities that have access to the key vault.  All identities in the array must use the same tenant ID as the key vault’s tenant ID. |
| **application_id**  string | Application ID of the client making request on behalf of a principal. |
| **certificates**  string | List of permissions to certificates.  Choices:   - `"get"` - `"list"` - `"delete"` - `"create"` - `"import"` - `"update"` - `"managecontacts"` - `"getissuers"` - `"listissuers"` - `"setissuers"` - `"deleteissuers"` - `"manageissuers"` - `"recover"` - `"purge"` |
| **keys**  string | List of permissions to keys.  Choices:   - `"encrypt"` - `"decrypt"` - `"wrapkey"` - `"unwrapkey"` - `"sign"` - `"verify"` - `"get"` - `"list"` - `"create"` - `"update"` - `"import"` - `"delete"` - `"backup"` - `"restore"` - `"recover"` - `"purge"` |
| **object_id**  string / required | The object ID of a user, service principal or security group in the Azure Active Directory tenant for the vault.  The object ID must be unique for the list of access policies.  Please note this is not application id. Object id can be obtained by running “az ad sp show –id <application id>”. |
| **secrets**  string | List of permissions to secrets.  Choices:   - `"get"` - `"list"` - `"set"` - `"delete"` - `"backup"` - `"restore"` - `"recover"` - `"purge"` |
| **storage**  string | List of permissions to storage accounts. |
| **tenant_id**  string | The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault.  Current keyvault `tenant_id` value will be used if not specified. |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  added in azure.azcollection 0.0.1 | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  added in azure.azcollection 0.0.1 | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  Default: `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  Choices:   - `false` - `true` ← (default) |
| **auth_source**  string  added in azure.azcollection 0.0.1 | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  Choices:   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  added in azure.azcollection 0.0.1 | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  Choices:   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  added in azure.azcollection 0.0.1 | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  Default: `"AzureCloud"` |
| **enable_purge_protection**  boolean | Property specifying whether protection against purge is enabled for this vault.  Choices:   - `false` ← (default) - `true` |
| **enable_soft_delete**  boolean | Property to specify whether the soft delete functionality is enabled for this key vault.  Choices:   - `false` - `true` ← (default) |
| **enabled_for_deployment**  boolean | Property to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault.  Choices:   - `false` - `true` |
| **enabled_for_disk_encryption**  boolean | Property to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys.  Choices:   - `false` - `true` |
| **enabled_for_template_deployment**  boolean | Property to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault.  Choices:   - `false` - `true` |
| **location**  string | Resource location. If not set, location from the resource group will be used as default. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **recover_mode**  boolean | Create vault in recovery mode.  Choices:   - `false` - `true` |
| **resource_group**  string / required | The name of the Resource Group to which the server belongs. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **sku**  string | SKU details. |
| **family**  string | SKU family name. |
| **name**  string / required | SKU name to specify whether the key vault is a standard vault or a premium vault.  Choices:   - `"standard"` - `"premium"` |
| **soft_delete_retention_in_days**  integer | Property specifying the number of days to retain deleted vaults. |
| **state**  string | Assert the state of the KeyVault. Use `present` to create or update an KeyVault and `absent` to delete it.  Choices:   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **vault_name**  string / required | Name of the vault. |
| **vault_tenant**  string | The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault. |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_keyvault_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_keyvault_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_keyvault_module.md#id6)

```yaml+jinja
- name: Create instance of Key Vault
  azure_rm_keyvault:
    resource_group: myResourceGroup
    vault_name: samplekeyvault
    enabled_for_deployment: yes
    vault_tenant: 72f98888-8666-4144-9199-2d7cd0111111
    sku:
      name: standard
    access_policies:
      - tenant_id: 72f98888-8666-4144-9199-2d7cd0111111
        object_id: 99998888-8666-4144-9199-2d7cd0111111
        keys:
          - get
          - list
```

## [Return Values](azure_rm_keyvault_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | The Azure Resource Manager resource ID for the key vault.  Returned: always  Sample: `"id"` |

### Authors

- Zim Kalinowski (@zikalino)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/azure/issues)
[Homepage](https://azure.microsoft.com)
[Repository (Sources)](https://github.com/ansible-collections/azure)
