---
collection: ansible
version: "6"
title: "azure.azcollection.azure_rm_aduser_info module – Get Azure Active Directory user info"
source_url: https://docs.ansible.com/projects/ansible/6/collections/azure/azcollection/azure_rm_aduser_info_module.html
fetched_at: 2026-07-27T16:45:43+00:00
---
# azure.azcollection.azure_rm_aduser_info module – Get Azure Active Directory user info

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
> see [Requirements](azure_rm_aduser_info_module.md#ansible-collections-azure-azcollection-azure-rm-aduser-info-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_aduser_info`.

New in azure.azcollection 1.4.0

- [Synopsis](azure_rm_aduser_info_module.md#synopsis)
- [Requirements](azure_rm_aduser_info_module.md#requirements)
- [Parameters](azure_rm_aduser_info_module.md#parameters)
- [Notes](azure_rm_aduser_info_module.md#notes)
- [See Also](azure_rm_aduser_info_module.md#see-also)
- [Examples](azure_rm_aduser_info_module.md#examples)
- [Return Values](azure_rm_aduser_info_module.md#return-values)

## [Synopsis](azure_rm_aduser_info_module.md#id1)

- Get Azure Active Directory user info.

## [Requirements](azure_rm_aduser_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_aduser_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  added in azure.azcollection 0.0.1 | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **all**  boolean | If True, will return all users in tenant.  If False will return no users.  It is recommended that you instead identify a subset of users and use filter.  Mutually exclusive with *object_id*, *attribute_name*, *odata_filter* and *user_principal_name*.  Choices:   - `false` - `true` |
| **api_profile**  string  added in azure.azcollection 0.0.1 | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  Default: `"latest"` |
| **attribute_name**  string | The name of an attribute that you want to match to attribute_value.  If attribute_name is not a collection type it will return users where attribute_name is equal to attribute_value.  If attribute_name is a collection type it will return users where attribute_value is in attribute_name.  Mutually exclusive with *object_id*, *user_principal_name*, *odata_filter* and *all*.  Required together with *attribute_value*. |
| **attribute_value**  string | The value to match attribute_name to.  If attribute_name is not a collection type it will return users where attribute_name is equal to attribute_value.  If attribute_name is a collection type it will return users where attribute_value is in attribute_name.  Required together with *attribute_name*. |
| **auth_source**  string  added in azure.azcollection 0.0.1 | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  Choices:   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  added in azure.azcollection 0.0.1 | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  Choices:   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  added in azure.azcollection 0.0.1 | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  Default: `"AzureCloud"` |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **object_id**  string | The object id for the user.  returns the user who has this object ID.  Mutually exclusive with *user_principal_name*, *attribute_name*, *odata_filter* and *all*. |
| **odata_filter**  string | returns users based on the the OData filter passed into this parameter.  Mutually exclusive with *object_id*, *attribute_name*, *user_principal_name* and *all*. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tenant**  string / required | The tenant ID. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **user_principal_name**  string | The principal name of the user.  returns the user who has this principal name.  Mutually exclusive with *object_id*, *attribute_name*, *odata_filter* and *all*. |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_aduser_info_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_aduser_info_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_aduser_info_module.md#id6)

```yaml+jinja
- name: Using user_principal_name
  azure.azcollection.azure_rm_aduser_info:
    user_principal_name: user@contoso.com
    tenant: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

- name: Using object_id
  azure.azcollection.azure_rm_aduser_info:
    object_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    tenant: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

- name: Using attribute mailNickname - not a collection
  azure.azcollection.azure_rm_aduser_info:
    attribute_name: mailNickname
    attribute_value: users_mailNickname
    tenant: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

- name: Using attribute proxyAddresses - a collection
  azure.azcollection.azure_rm_aduser_info:
    attribute_name: proxyAddresses
    attribute_value: SMTP:user@contoso.com
    tenant: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

- name: Using Filter mailNickname
  azure.azcollection.azure_rm_aduser_info:
    odata_filter: mailNickname eq 'user@contoso.com'
    tenant: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

- name: Using Filter proxyAddresses
  azure.azcollection.azure_rm_aduser_info:
    odata_filter: proxyAddresses/any(c:c eq 'SMTP:user@contoso.com')
    tenant: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

## [Return Values](azure_rm_aduser_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account_enabled**  boolean | Whether the account is enabled.  Returned: always  Sample: `false` |
| **display_name**  string | The display name of the user.  Returned: always  Sample: `"John Smith"` |
| **mail**  string | The primary email address of the user.  Returned: always  Sample: `"John.Smith@contoso.com"` |
| **mail_nickname**  string | The mail alias for the user.  Returned: always  Sample: `"jsmith"` |
| **object_id**  string | The object_id for the user.  Returned: always  Sample: `"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"` |
| **user_principal_name**  string | The principal name of the user.  Returned: always  Sample: `"jsmith@contoso.com"` |
| **user_type**  string | A string value that can be used to classify user types in your directory.  Returned: always  Sample: `"Member"` |

### Authors

- Cole Neubauer(@coleneubauer)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/azure/issues)
[Homepage](https://azure.microsoft.com)
[Repository (Sources)](https://github.com/ansible-collections/azure)
