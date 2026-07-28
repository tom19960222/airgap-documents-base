---
collection: ansible
version: "6"
title: "azure.azcollection.azure_rm_adgroup module – Manage Azure Active Directory group"
source_url: https://docs.ansible.com/projects/ansible/6/collections/azure/azcollection/azure_rm_adgroup_module.html
fetched_at: 2026-07-27T16:45:40+00:00
---
# azure.azcollection.azure_rm_adgroup module – Manage Azure Active Directory group

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
> see [Requirements](azure_rm_adgroup_module.md#ansible-collections-azure-azcollection-azure-rm-adgroup-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_adgroup`.

New in azure.azcollection 1.6.0

- [Synopsis](azure_rm_adgroup_module.md#synopsis)
- [Requirements](azure_rm_adgroup_module.md#requirements)
- [Parameters](azure_rm_adgroup_module.md#parameters)
- [Notes](azure_rm_adgroup_module.md#notes)
- [See Also](azure_rm_adgroup_module.md#see-also)
- [Examples](azure_rm_adgroup_module.md#examples)
- [Return Values](azure_rm_adgroup_module.md#return-values)

## [Synopsis](azure_rm_adgroup_module.md#id1)

- Create, update or delete Azure Active Directory group.

## [Requirements](azure_rm_adgroup_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_adgroup_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **absent_members**  list / elements=string | The azure ad objects asserted to not be members of the group. |
| **absent_owners**  list / elements=string | The azure ad objects asserted to not be owners of the group. |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  added in azure.azcollection 0.0.1 | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  added in azure.azcollection 0.0.1 | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  Default: `"latest"` |
| **auth_source**  string  added in azure.azcollection 0.0.1 | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  Choices:   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  added in azure.azcollection 0.0.1 | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  Choices:   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  added in azure.azcollection 0.0.1 | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  Default: `"AzureCloud"` |
| **display_name**  string | The display name of the ad group.  Can be used with *mail_nickname* instead of *object_id* to reference existing group.  Required when creating a new ad group. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **mail_nickname**  string | The mail nickname of the ad group.  Can be used with *display_name* instead of *object_id* to reference existing group.  Required when creating a new ad group. |
| **object_id**  string | The object id for the ad group.  Can be used to reference when updating an existing group.  Ignored when attempting to create a group. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **present_members**  list / elements=string | The azure ad objects asserted to be members of the group.  This list does not need to be all inclusive. Objects that are members and not on this list remain members. |
| **present_owners**  list / elements=string | The azure ad objects asserted to be owners of the group.  This list does not need to be all inclusive. Objects that are owners and not on this list remain members. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **state**  string | Assert the state of the resource group. Use `present` to create or update and `absent` to delete.  Choices:   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **tenant**  string / required | The tenant ID. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_adgroup_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_adgroup_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_adgroup_module.md#id6)

```yaml+jinja
- name: Create Group
  azure_rm_adgroup:
    tenant: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    display_name: "Group-Name"
    mail_nickname: "Group-Mail-Nickname"
    state: 'present'

- name: Delete Group using display_name and mail_nickname
  azure_rm_adgroup:
    tenant: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    display_name: "Group-Name"
    mail_nickname: "Group-Mail-Nickname"
    state: 'absent'

- name: Delete Group using object_id
  azure_rm_adgroup:
    tenant: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    object_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    state: 'absent'

- name: Ensure Users are Members of a Group using display_name and mail_nickname
  azure_rm_adgroup:
    tenant: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    display_name: "Group-Name"
    mail_nickname: "Group-Mail-Nickname"
    state: 'present'
    present_members:
      - "https://graph.windows.net/{{ tenant_id }}/directoryObjects/{{ ad_object_1_object_id }}"
      - "https://graph.windows.net/{{ tenant_id }}/directoryObjects/{{ ad_object_2_object_id }}"

- name: Ensure Users are Members of a Group using object_id
  azure_rm_adgroup:
    tenant: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    object_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    state: 'present'
    present_members:
      - "https://graph.windows.net/{{ ad_object_1_tenant_id }}/directoryObjects/{{ ad_object_1_object_id }}"
      - "https://graph.windows.net/{{ ad_object_2_tenant_id }}/directoryObjects/{{ ad_object_2_object_id }}"

- name: Ensure Users are not Members of a Group using display_name and mail_nickname
  azure_rm_adgroup:
    tenant: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    display_name: "Group-Name"
    mail_nickname: "Group-Mail-Nickname"
    state: 'present'
    absent_members:
      - "{{ ad_object_1_object_id }}"

- name: Ensure Users are Members of a Group using object_id
  azure_rm_adgroup:
    tenant: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    object_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    state: 'present'
    absent_members:
      - "{{ ad_object_1_object_id }}"

- name: Ensure Users are Owners of a Group using display_name and mail_nickname
  azure_rm_adgroup:
    tenant: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    display_name: "Group-Name"
    mail_nickname: "Group-Mail-Nickname"
    state: 'present'
    present_owners:
      - "https://graph.windows.net/{{ tenant_id }}/directoryObjects/{{ ad_object_1_object_id }}"
      - "https://graph.windows.net/{{ tenant_id }}/directoryObjects/{{ ad_object_2_object_id }}"

- name: Ensure Users are Owners of a Group using object_id
  azure_rm_adgroup:
    tenant: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    object_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    state: 'present'
    present_owners:
      - "https://graph.windows.net/{{ ad_object_1_tenant_id }}/directoryObjects/{{ ad_object_1_object_id }}"
      - "https://graph.windows.net/{{ ad_object_2_tenant_id }}/directoryObjects/{{ ad_object_2_object_id }}"

- name: Ensure Users are not Owners of a Group using display_name and mail_nickname
  azure_rm_adgroup:
    tenant: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    display_name: "Group-Name"
    mail_nickname: "Group-Mail-Nickname"
    state: 'present'
    absent_owners:
      - "{{ ad_object_1_object_id }}"
      - "{{ ad_object_2_object_id }}"

- name: Ensure Users are Owners of a Group using object_id
  azure_rm_adgroup:
    tenant: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    object_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    state: 'present'
    absent_owners:
      - "{{ ad_object_1_object_id }}"
      - "{{ ad_object_2_object_id }}"
```

## [Return Values](azure_rm_adgroup_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **display_name**  string | The display name of the group.  Returned: always  Sample: `"GroupName"` |
| **group_members**  list / elements=string | The members of the group.  Returned: always |
| **group_owners**  list / elements=string | The owners of the group.  Returned: always |
| **mail**  string | The primary email address of the group.  Returned: always  Sample: `"group@contoso.com"` |
| **mail_enabled**  boolean | Whether the group is mail-enabled. Must be false. This is because only pure security groups can be created using the Graph API.  Returned: always  Sample: `false` |
| **mail_nickname**  string | The mail alias for the group.  Returned: always  Sample: `"groupname"` |
| **object_id**  string | The object_id for the group.  Returned: always  Sample: `"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"` |
| **security_enabled**  boolean | Whether the group is security-enable.  Returned: always  Sample: `false` |

### Authors

- Cole Neubauer(@coleneubauer)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/azure/issues)
[Homepage](https://azure.microsoft.com)
[Repository (Sources)](https://github.com/ansible-collections/azure)
