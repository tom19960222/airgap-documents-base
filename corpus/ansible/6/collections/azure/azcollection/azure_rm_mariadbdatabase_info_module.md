---
collection: ansible
version: "6"
title: "azure.azcollection.azure_rm_mariadbdatabase_info module – Get Azure MariaDB Database facts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/azure/azcollection/azure_rm_mariadbdatabase_info_module.html
fetched_at: 2026-07-27T16:46:35+00:00
---
# azure.azcollection.azure_rm_mariadbdatabase_info module – Get Azure MariaDB Database facts

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
> see [Requirements](azure_rm_mariadbdatabase_info_module.md#ansible-collections-azure-azcollection-azure-rm-mariadbdatabase-info-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_mariadbdatabase_info`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_mariadbdatabase_info_module.md#synopsis)
- [Requirements](azure_rm_mariadbdatabase_info_module.md#requirements)
- [Parameters](azure_rm_mariadbdatabase_info_module.md#parameters)
- [Notes](azure_rm_mariadbdatabase_info_module.md#notes)
- [See Also](azure_rm_mariadbdatabase_info_module.md#see-also)
- [Examples](azure_rm_mariadbdatabase_info_module.md#examples)
- [Return Values](azure_rm_mariadbdatabase_info_module.md#return-values)

## [Synopsis](azure_rm_mariadbdatabase_info_module.md#id1)

- Get facts of MariaDB Database.

## [Requirements](azure_rm_mariadbdatabase_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_mariadbdatabase_info_module.md#id3)

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
| **name**  string | The name of the database. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **resource_group**  string / required | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **server_name**  string / required | The name of the server. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_mariadbdatabase_info_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_mariadbdatabase_info_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_mariadbdatabase_info_module.md#id6)

```yaml+jinja
- name: Get instance of MariaDB Database
  azure_rm_mariadbdatabase_info:
    resource_group: myResourceGroup
    server_name: server_name
    name: database_name

- name: List instances of MariaDB Database
  azure_rm_mariadbdatabase_info:
    resource_group: myResourceGroup
    server_name: server_name
```

## [Return Values](azure_rm_mariadbdatabase_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **databases**  complex | A list of dictionaries containing facts for MariaDB Databases.  Returned: always |
| **charset**  string | The charset of the database.  Returned: always  Sample: `"UTF8"` |
| **collation**  string | The collation of the database.  Returned: always  Sample: `"English_United States.1252"` |
| **id**  string | Resource ID.  Returned: always  Sample: `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.DBforMariaDB/servers/testser ver/databases/db1"` |
| **name**  string | Resource name.  Returned: always  Sample: `"db1"` |
| **resource_group**  string | Resource group name.  Returned: always  Sample: `"testrg"` |
| **server_name**  string | Server name.  Returned: always  Sample: `"testserver"` |

### Authors

- Zim Kalinowski (@zikalino)
- Matti Ranta (@techknowlogick)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/azure/issues)
[Homepage](https://azure.microsoft.com)
[Repository (Sources)](https://github.com/ansible-collections/azure)
