---
collection: ansible
version: "6"
title: "azure.azcollection.azure_rm_sqlserver module – Manage SQL Server instance"
source_url: https://docs.ansible.com/projects/ansible/6/collections/azure/azcollection/azure_rm_sqlserver_module.html
fetched_at: 2026-07-27T16:47:08+00:00
---
# azure.azcollection.azure_rm_sqlserver module – Manage SQL Server instance

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
> see [Requirements](azure_rm_sqlserver_module.md#ansible-collections-azure-azcollection-azure-rm-sqlserver-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_sqlserver`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_sqlserver_module.md#synopsis)
- [Requirements](azure_rm_sqlserver_module.md#requirements)
- [Parameters](azure_rm_sqlserver_module.md#parameters)
- [Notes](azure_rm_sqlserver_module.md#notes)
- [See Also](azure_rm_sqlserver_module.md#see-also)
- [Examples](azure_rm_sqlserver_module.md#examples)
- [Return Values](azure_rm_sqlserver_module.md#return-values)

## [Synopsis](azure_rm_sqlserver_module.md#id1)

- Create, update and delete instance of SQL Server.

## [Requirements](azure_rm_sqlserver_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_sqlserver_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  added in azure.azcollection 0.0.1 | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **admin_password**  string | Password of the SQL administrator account for server (required for server creation). |
| **admin_username**  string | Username of the SQL administrator account for server. Once created it cannot be changed. |
| **administrators**  dictionary  added in azure.azcollection 1.11.0 | The Azure Active Directory identity of the server. |
| **administrator_type**  string | Type of the Azure AD administrator.  Default: `"ActiveDirectory"` |
| **azure_ad_only_authentication**  boolean | Azure AD only authentication enabled.  Choices:   - `false` - `true` |
| **login**  string | Login name of the Azure AD administrator. |
| **principal_type**  string | Principal Type of the Azure AD administrator.  Choices:   - `"User"` - `"Group"` - `"Application"` |
| **sid**  string | SID (object ID) of the Azure AD administrator. |
| **tenant_id**  string | Tenant ID of the Azure AD administrator. |
| **api_profile**  string  added in azure.azcollection 0.0.1 | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  Default: `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  Choices:   - `false` - `true` ← (default) |
| **auth_source**  string  added in azure.azcollection 0.0.1 | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  Choices:   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  added in azure.azcollection 0.0.1 | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  Choices:   - `"ignore"` - `"validate"` |
| **change_admin_password**  boolean  added in azure.azcollection 1.11.0 | Whether or not the c(admin_password) should be updated for an existing server. If true, the password is the only value which will be updated.  Choices:   - `false` ← (default) - `true` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  added in azure.azcollection 0.0.1 | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  Default: `"AzureCloud"` |
| **identity**  string | The identity type. Set this to `SystemAssigned` in order to automatically create and assign an Azure Active Directory principal for the resource.  Possible values include `SystemAssigned`. |
| **location**  string | Resource location. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **minimal_tls_version**  string  added in azure.azcollection 1.11.0 | Require clients to use a specified TLS version.  Choices:   - `"1.0"` - `"1.1"` - `"1.2"` |
| **name**  string / required | The name of the server. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **public_network_access**  string  added in azure.azcollection 1.11.0 | Whether or not public endpoint access is allowed for the server.  Choices:   - `"Enabled"` - `"Disabled"` |
| **resource_group**  string / required | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. |
| **restrict_outbound_network_access**  string  added in azure.azcollection 1.11.0 | Whether or not to restrict outbound network access for this server.  Choices:   - `"Enabled"` - `"Disabled"` |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **state**  string | State of the SQL server. Use `present` to create or update a server and use `absent` to delete a server.  Choices:   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **version**  string | The version of the server. For example `12.0`. |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_sqlserver_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_sqlserver_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_sqlserver_module.md#id6)

```yaml+jinja
- name: Create (or update) SQL Server
  azure_rm_sqlserver:
    resource_group: myResourceGroup
    name: server_name
    location: westus
    admin_username: mylogin
    admin_password: Testpasswordxyz12!

- name: Change SQL Server admin password
  azure_rm_sqlserver:
    resource_group: myResourceGroup
    name: server_name
    location: westus
    admin_password: NewPasswordx123!
    change_admin_password: true

- name: Create SQL Server with Azure Active Directory admin
  azure_rm_sqlserver:
    resource_group: myResourceGroup
    name: server_name
    location: westus
    admin_username: mylogin
    admin_password: Testpasswordxyz12!
    administrators:
      principal_type: Group
      login: MySqlAdminGroup
      sid: "{{ MySqlAdminGroup.object_id }}"
      tenant_id: "{{ my_tenant_id }}"
      azure_ad_only_authentication: false
```

## [Return Values](azure_rm_sqlserver_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **fully_qualified_domain_name**  string | The fully qualified domain name of the server.  Returned: always  Sample: `"sqlcrudtest-4645.database.windows.net"` |
| **id**  string | Resource ID.  Returned: always  Sample: `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Sql/servers/sqlcrudtest-4645"` |
| **state**  string | The state of the server.  Returned: always  Sample: `"state"` |
| **version**  string | The version of the server.  Returned: always  Sample: `"12.0"` |

### Authors

- Zim Kalinowski (@zikalino)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/azure/issues)
[Homepage](https://azure.microsoft.com)
[Repository (Sources)](https://github.com/ansible-collections/azure)
