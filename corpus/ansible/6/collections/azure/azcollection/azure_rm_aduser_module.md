---
collection: ansible
version: "6"
title: "azure.azcollection.azure_rm_aduser module – Modify an Azure Active Directory user"
source_url: https://docs.ansible.com/projects/ansible/6/collections/azure/azcollection/azure_rm_aduser_module.html
fetched_at: 2026-07-27T16:45:42+00:00
---
# azure.azcollection.azure_rm_aduser module – Modify an Azure Active Directory user

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
> see [Requirements](azure_rm_aduser_module.md#ansible-collections-azure-azcollection-azure-rm-aduser-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_aduser`.

New in azure.azcollection 1.5.0

- [Synopsis](azure_rm_aduser_module.md#synopsis)
- [Requirements](azure_rm_aduser_module.md#requirements)
- [Parameters](azure_rm_aduser_module.md#parameters)
- [Notes](azure_rm_aduser_module.md#notes)
- [See Also](azure_rm_aduser_module.md#see-also)
- [Examples](azure_rm_aduser_module.md#examples)
- [Return Values](azure_rm_aduser_module.md#return-values)

## [Synopsis](azure_rm_aduser_module.md#id1)

- Create, delete, and update an Azure Active Directory user.

## [Requirements](azure_rm_aduser_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_aduser_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account_enabled**  boolean | A boolean determing whether or not the user account is enabled.  Used when either creating or updating a user account.  Choices:   - `false` - `true` |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  added in azure.azcollection 0.0.1 | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  added in azure.azcollection 0.0.1 | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  Default: `"latest"` |
| **attribute_name**  string | The name of an attribute that you want to match to attribute_value.  If attribute_name is not a collection type it will update or delete the user where attribute_name is equal to attribute_value.  If attribute_name is a collection type it will update or delete the user where attribute_value is in attribute_name.  Mutually exclusive with *object_id*, *user_principal_name*, and *odata_filter*.  Required together with *attribute_value*. |
| **attribute_value**  string | The value to match attribute_name to.  If attribute_name is not a collection type it will update or delete the user where attribute_name is equal to attribute_value.  If attribute_name is a collection type it will update or delete the user where attribute_value is in attribute_name.  Required together with *attribute_name*. |
| **auth_source**  string  added in azure.azcollection 0.0.1 | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  Choices:   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  added in azure.azcollection 0.0.1 | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  Choices:   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  added in azure.azcollection 0.0.1 | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  Default: `"AzureCloud"` |
| **display_name**  string | The display name of the user.  Used when either creating or updating a user account. |
| **given_name**  string | The given name for the user.  Used when either creating or updating a user account. |
| **immutable_id**  string | The immutable_id of the user.  Used when either creating or updating a user account. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **mail**  string | The primary email address of the user.  Used when either creating or updating a user account. |
| **mail_nickname**  string | The mail alias for the user.  Used when either creating or updating a user account. |
| **object_id**  string | The object id for the user.  Updates or deletes the user who has this object ID.  Mutually exclusive with *user_principal_name*, *attribute_name*, and *odata_filter*. |
| **odata_filter**  string | Filter that can be used to specify a user to update or delete.  Mutually exclusive with *object_id*, *attribute_name*, and *user_principal_name*. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **password_profile**  string | The password for the user.  Used when either creating or updating a user account. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **state**  string | State of the ad user. Use `present` to create or update an ad user and `absent` to delete an ad user.  Choices:   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **surname**  string | The surname for the user.  Used when either creating or updating a user account. |
| **tenant**  string / required | The tenant ID. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **usage_location**  string | A two letter country code, ISO standard 3166.  Required for a user that will be assigned licenses due to legal requirement to check for availability of services in countries.  Used when either creating or updating a user account. |
| **user_principal_name**  string | The principal name of the user.  Creates, updates, or deletes the user who has this principal name.  Mutually exclusive with *object_id*, *attribute_name*, and *odata_filter*. |
| **user_type**  string | A string value that can be used to classify user types in your directory, such as Member and Guest.  Used when either creating or updating a user account. |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_aduser_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_aduser_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_aduser_module.md#id6)

```yaml+jinja
- name: Create user
  azure_rm_aduser:
    user_principal_name: "{{ user_id }}"
    tenant: "{{ tenant_id }}"
    state: "present"
    account_enabled: "True"
    display_name: "Test_{{ user_principal_name }}_Display_Name"
    password_profile: "password"
    mail_nickname: "Test_{{ user_principal_name }}_mail_nickname"
    immutable_id: "{{ object_id }}"
    given_name: "First"
    surname: "Last"
    user_type: "Member"
    usage_location: "US"
    mail: "{{ user_principal_name }}@contoso.com"

- name: Update user with new value for account_enabled
  azure_rm_aduser:
    user_principal_name: "{{ user_id }}"
    tenant: "{{ tenant_id }}"
    state: "present"
    account_enabled: "False"

- name: Delete user
  azure_rm_aduser:
    user_principal_name: "{{ user_id }}"
    tenant: "{{ tenant_id }}"
    state: "absent"
```

## [Return Values](azure_rm_aduser_module.md#id7)

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
