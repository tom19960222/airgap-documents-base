---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_adapplication module – Manage Azure Active Directory application"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_adapplication_module.html
fetched_at: 2026-07-28T01:11:53+00:00
---
# azure.azcollection.azure_rm_adapplication module – Manage Azure Active Directory application

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
> see [Requirements](azure_rm_adapplication_module.md#ansible-collections-azure-azcollection-azure-rm-adapplication-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_adapplication`.

New in azure.azcollection 1.6.0

- [Synopsis](azure_rm_adapplication_module.md#synopsis)
- [Requirements](azure_rm_adapplication_module.md#requirements)
- [Parameters](azure_rm_adapplication_module.md#parameters)
- [Notes](azure_rm_adapplication_module.md#notes)
- [See Also](azure_rm_adapplication_module.md#see-also)
- [Examples](azure_rm_adapplication_module.md#examples)
- [Return Values](azure_rm_adapplication_module.md#return-values)

## [Synopsis](azure_rm_adapplication_module.md#id1)

- Manage Azure Active Directory application.

## [Requirements](azure_rm_adapplication_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_adapplication_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **allow_guests_sign_in**  boolean | A property on the application to indicate if the application accepts other IDPs or not or partially accepts.  **Choices:**   - `false` - `true` |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **app_id**  string | Application ID. |
| **app_roles**  list / elements=dictionary | Declare the roles you want to associate with your application. |
| **allowed_member_types**  list / elements=string / required | Specifies whether this app role can be assigned to users and groups *allowed_member_types=User*.  To other application’s *allowed_member_types=Application*.  Or both `User` and `Appplication`. |
| **description**  string | The description for the app role.  This is displayed when the app role is being assigned.  if the app role functions as an application permission, during consent experiences. |
| **display_name**  string | Display name for the permission that appears in the app role assignment and consent experiences. |
| **is_enabled**  boolean | When creating or updating an app role, this must be set to true (which is the default).  To delete a role, this must first be set to false.  At that point, in a subsequent call, this role may be removed.  **Choices:**   - `false` - `true` |
| **value**  string | Specifies the value to include in the roles claim in ID tokens and access tokens authenticating an assigned user or service principal.  Must not exceed 120 characters in length.  Allowed characters include !  Any other character, including the space character, are not allowed. |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **available_to_other_tenants**  boolean | The application can be used from any Azure AD tenants.  **Choices:**   - `false` - `true` |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **credential_description**  string | The description of the password. |
| **display_name**  string | The display name of the application. |
| **end_date**  string | Date or datetime after which credentials expire(e.g. ‘2017-12-31’).  Default value is one year after current time. |
| **homepage**  string | The url where users can sign in and use your app. |
| **identifier_uris**  list / elements=string | Space-separated unique URIs that Azure AD can use for this app. |
| **key_type**  string | The type of the key credentials associated with the application.  **Choices:**   - `"AsymmetricX509Cert"` ← (default) - `"Password"` - `"Symmetric"` |
| **key_usage**  string | The usage of the key credentials associated with the application.  **Choices:**   - `"Sign"` - `"Verify"` ← (default) |
| **key_value**  string | The value for the key credentials associated with the application. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **native_app**  boolean | An application which can be installed on a user’s device or computer.  **Choices:**   - `false` - `true` |
| **oauth2_allow_implicit_flow**  boolean | Whether to allow implicit grant flow for OAuth2.  **Choices:**   - `false` - `true` |
| **optional_claims**  list / elements=dictionary | Declare the optional claims for the application. |
| **additional_properties**  string | Additional properties of the claim.  If a property exists in this collection, it modifies the behavior of the optional claim specified in the name property. |
| **essential**  boolean | If the value is true, the claim specified by the client is necessary to ensure a smooth authorization experience for the specific task requested by the end user.  The default value is false.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | The name of the optional claim. |
| **source**  string | The source (directory object) of the claim.  There are predefined claims and user-defined claims from extension properties.  If the source value is null, the claim is a predefined optional claim.  If the source value is user, the value in the name property is the extension property from the user object. |
| **password**  string | App password, aka ‘client secret’. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **reply_urls**  list / elements=string | Space-separated URIs to which Azure AD will redirect in response to an OAuth 2.0 request.  The value does not need to be a physical endpoint, but must be a valid URI. |
| **required_resource_accesses**  list / elements=dictionary | Resource scopes and roles the application requires access to.  Should be in manifest json format. |
| **resource_access**  list / elements=dictionary | The description of the app role. |
| **id**  string | The unique identifier for one of the oauth2PermissionScopes or appRole instances that the resource application exposes. |
| **type**  string | Specifies whether the id property references an oauth2PermissionScopes or an appRole.  Possible values are Scope or Role. |
| **resource_app_id**  string | The unique identifier for the resource that the application requires access to.  This should be equal to the appId declared on the target resource application. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **start_date**  string | Date or datetime at which credentials become valid, such as ‘2017-01-01’.  Default value is current time. |
| **state**  string | Assert the state of Active Dirctory service principal.  Use `present` to create or update a Password and use `absent` to delete.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **tenant**  string / required | The tenant ID. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_adapplication_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_adapplication_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_adapplication_module.md#id6)

```yaml+jinja
- name: Create ad application
  azure_rm_adapplication:
    tenant: "{{ tenant_id }}"
    display_name: "{{ display_name }}"

- name: Create application with more parameter
  azure_rm_adapplication:
    tenant: "{{ tenant_id }}"
    display_name: "{{ display_name }}"
    available_to_other_tenants: false
    credential_description: "for test"
    end_date: 2021-10-01
    start_date: 2021-05-18
    identifier_uris: fredtest02.com

- name: delete ad application
  azure_rm_adapplication:
    tenant: "{{ tenant_id }}"
    app_id: "{{ app_id }}"
    state: absent
```

## [Return Values](azure_rm_adapplication_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **output**  complex | Current state of the adapplication.  **Returned:** awalys |
| **app_id**  string | The application ID.  **Returned:** always  **Sample:** `"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"` |
| **available_to_other_tenants**  boolean | The application can be used from any Azure AD tenants.  **Returned:** always  **Sample:** `false` |
| **display_name**  string | Object’s display name or its prefix.  **Returned:** always  **Sample:** `"fredAKSCluster"` |
| **homepage**  string | The url where users can sign in and use your app.  **Returned:** always |
| **identifier_uris**  list / elements=string | Space-separated unique URIs that Azure AD can use for this app.  **Returned:** always  **Sample:** `[]` |
| **oauth2_allow_implicit_flow**  boolean | Whether to allow implicit grant flow for OAuth2.  **Returned:** always  **Sample:** `false` |
| **object_id**  string | Object ID of the application  **Returned:** always  **Sample:** `"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"` |
| **optional_claims**  list / elements=string | The optional claims for the application.  **Returned:** always  **Sample:** `[]` |
| **reply_urls**  list / elements=string | Space-separated URIs to which Azure AD will redirect in response to an OAuth 2.0 request.  **Returned:** always  **Sample:** `[]` |

### Authors

- guopeng_lin (@guopenglin) haiyuan_zhang (@haiyuazhang) Fred-sun (@Fred-sun)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
