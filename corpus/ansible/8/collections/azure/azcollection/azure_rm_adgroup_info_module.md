---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_adgroup_info module – Get Azure Active Directory group info"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_adgroup_info_module.html
fetched_at: 2026-07-28T01:11:56+00:00
---
# azure.azcollection.azure_rm_adgroup_info module – Get Azure Active Directory group info

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
> see [Requirements](azure_rm_adgroup_info_module.md#ansible-collections-azure-azcollection-azure-rm-adgroup-info-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_adgroup_info`.

New in azure.azcollection 1.6.0

- [Synopsis](azure_rm_adgroup_info_module.md#synopsis)
- [Requirements](azure_rm_adgroup_info_module.md#requirements)
- [Parameters](azure_rm_adgroup_info_module.md#parameters)
- [Notes](azure_rm_adgroup_info_module.md#notes)
- [See Also](azure_rm_adgroup_info_module.md#see-also)
- [Examples](azure_rm_adgroup_info_module.md#examples)
- [Return Values](azure_rm_adgroup_info_module.md#return-values)

## [Synopsis](azure_rm_adgroup_info_module.md#id1)

- Get Azure Active Directory group info.

## [Requirements](azure_rm_adgroup_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_adgroup_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **all**  boolean | If True, will return all groups in tenant.  If False will return no users.  It is recommended that you instead identify a subset of groups and use filter.  **Choices:**   - `false` ← (default) - `true` |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **attribute_name**  string | The name of an attribute that you want to match to *attribute_value*.  If *attribute_name* is not a collection type it will return groups where *attribute_name* is equal to *attribute_value*.  If *attribute_name* is a collection type it will return groups where *attribute_value* is in *attribute_name*. |
| **attribute_value**  string | The value to match attribute_name to.  If *attribute_name* is not a collection type it will return groups where *attribute_name* is equal to *attribute_value*.  If *attribute_name* is a collection type it will groups users where *attribute_value* is in *attribute_name*. |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **check_membership**  string | The object ID of the contact, group, user, or service principal to check for membership against returned groups. |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **object_id**  string | The object id for the ad group.  returns the group which has this object ID. |
| **odata_filter**  string | returns groups based on the the OData filter passed into this parameter. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **return_group_members**  boolean | Indicate whether the members of a group should be returned with the returned groups.  **Choices:**   - `false` ← (default) - `true` |
| **return_member_groups**  boolean | Indicate whether the groups in which a groups is a member should be returned with the returned groups.  **Choices:**   - `false` ← (default) - `true` |
| **return_owners**  boolean | Indicate whether the owners of a group should be returned with the returned groups.  **Choices:**   - `false` ← (default) - `true` |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tenant**  string / required | The tenant ID. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_adgroup_info_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_adgroup_info_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_adgroup_info_module.md#id6)

```yaml+jinja
- name: Return a specific group using object_id
  azure_rm_adgroup_info:
    object_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    tenant: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

- name: Return a specific group using object_id and  return the owners of the group
  azure_rm_adgroup_info:
    object_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    return_owners: true
    tenant: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

- name: Return a specific group using object_id and return the owners and members of the group
  azure_rm_adgroup_info:
    object_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    return_owners: true
    return_group_members: true
    tenant: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

- name: Return a specific group using object_id and return the groups the group is a member of
  azure_rm_adgroup_info:
    object_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    return_member_groups: true
    tenant: "{{ tenant_id }}"

- name: Return a specific group using object_id and check an ID for membership
  azure_rm_adgroup_info:
    object_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    check_membership: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    tenant: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

- name: Return a specific group using displayName for attribute_name
  azure_rm_adgroup_info:
    attribute_name: "displayName"
    attribute_value: "Display-Name-Of-AD-Group"
    tenant: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

- name: Return groups matching odata_filter
  azure_rm_adgroup_info:
    odata_filter: "mailNickname eq 'Mail-Nickname-Of-AD-Group'"
    tenant: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

- name: Return all groups
  azure_rm_adgroup_info:
    tenant: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    all: true
```

## [Return Values](azure_rm_adgroup_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **display_name**  string | The display name of the group.  **Returned:** always  **Sample:** `"GroupName"` |
| **group_members**  list / elements=string | The members of the group.  **Returned:** always |
| **group_owners**  list / elements=string | The owners of the group.  **Returned:** always |
| **mail**  string | The primary email address of the group.  **Returned:** always  **Sample:** `"group@contoso.com"` |
| **mail_enabled**  boolean | Whether the group is mail-enabled. Must be false. This is because only pure security groups can be created using the Graph API.  **Returned:** always  **Sample:** `false` |
| **mail_nickname**  string | The mail alias for the group.  **Returned:** always  **Sample:** `"groupname"` |
| **object_id**  string | The object_id for the group.  **Returned:** always  **Sample:** `"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"` |
| **security_enabled**  boolean | Whether the group is security-enable.  **Returned:** always  **Sample:** `false` |

### Authors

- Cole Neubauer(@coleneubauer)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
