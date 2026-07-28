---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_keyvaultkey module – Use Azure KeyVault keys"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_keyvaultkey_module.html
fetched_at: 2026-07-28T01:13:38+00:00
---
# azure.azcollection.azure_rm_keyvaultkey module – Use Azure KeyVault keys

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
> see [Requirements](azure_rm_keyvaultkey_module.md#ansible-collections-azure-azcollection-azure-rm-keyvaultkey-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_keyvaultkey`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_keyvaultkey_module.md#synopsis)
- [Requirements](azure_rm_keyvaultkey_module.md#requirements)
- [Parameters](azure_rm_keyvaultkey_module.md#parameters)
- [Notes](azure_rm_keyvaultkey_module.md#notes)
- [See Also](azure_rm_keyvaultkey_module.md#see-also)
- [Examples](azure_rm_keyvaultkey_module.md#examples)
- [Return Values](azure_rm_keyvaultkey_module.md#return-values)

## [Synopsis](azure_rm_keyvaultkey_module.md#id1)

- Create or delete a key within a given keyvault.
- By using Key Vault, you can encrypt keys and secrets.
- Such as authentication keys, storage account keys, data encryption keys, .PFX files, and passwords.

## [Requirements](azure_rm_keyvaultkey_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_keyvaultkey_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  **Choices:**   - `false` - `true` ← (default) |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **byok_file**  string | BYOK file. |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **curve**  string | Elliptic curve name. For valid values, see JsonWebKeyCurveName. Possible values include P-256, P-384, P-521, P-256K. |
| **key_attributes**  dictionary | The attributes of a key managed by the key vault service. |
| **enabled**  boolean | Whether the key is enabled.  **Choices:**   - `false` - `true` |
| **expires**  string | not valid after date in UTC ISO format without the Z at the end |
| **not_before**  string | not valid before date in UTC ISO format without the Z at the end |
| **key_name**  string / required | Name of the keyvault key. |
| **key_size**  integer | The key size in bits. For example 2048, 3072, or 4096 for RSA. |
| **key_type**  string | The type of key to create. For valid values, see JsonWebKeyType. Possible values include EC, EC-HSM, RSA, RSA-HSM, oct  **Default:** `"RSA"` |
| **keyvault_uri**  string / required | URI of the keyvault endpoint. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **pem_file**  string | PEM file. |
| **pem_password**  string | PEM password. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **state**  string | Assert the state of the key. Use `present` to create a key and `absent` to delete a key.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_keyvaultkey_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_keyvaultkey_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_keyvaultkey_module.md#id6)

```yaml+jinja
- name: Create a key
  azure_rm_keyvaultkey:
    key_name: MyKey
    keyvault_uri: https://contoso.vault.azure.net/

- name: Delete a key
  azure_rm_keyvaultkey:
    key_name: MyKey
    keyvault_uri: https://contoso.vault.azure.net/
    state: absent
```

## [Return Values](azure_rm_keyvaultkey_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **state**  complex | Current state of the key.  **Returned:** success |
| **key_id**  string | key resource path.  **Returned:** success  **Sample:** `"https://contoso.vault.azure.net/keys/hello/e924f053839f4431b35bc54393f98423"` |

### Authors

- Ian Philpot (@iphilpot)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
