---
collection: ansible
version: "8"
title: "netapp.azure.azure_rm_netapp_account module – Manage NetApp Azure Files Account"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/azure/azure_rm_netapp_account_module.html
fetched_at: 2026-07-28T02:41:01+00:00
---
# netapp.azure.azure_rm_netapp_account module – Manage NetApp Azure Files Account

> **Note:**
>
> This module is part of the [netapp.azure collection](https://galaxy.ansible.com/ui/repo/published/netapp/azure/) (version 21.10.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.azure`.
> You need further requirements to be able to use this module,
> see [Requirements](azure_rm_netapp_account_module.md#ansible-collections-netapp-azure-azure-rm-netapp-account-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.azure.azure_rm_netapp_account`.

New in netapp.azure 19.10.0

- [Synopsis](azure_rm_netapp_account_module.md#synopsis)
- [Requirements](azure_rm_netapp_account_module.md#requirements)
- [Parameters](azure_rm_netapp_account_module.md#parameters)
- [Notes](azure_rm_netapp_account_module.md#notes)
- [See Also](azure_rm_netapp_account_module.md#see-also)
- [Examples](azure_rm_netapp_account_module.md#examples)

## [Synopsis](azure_rm_netapp_account_module.md#id2)

- Create and delete NetApp Azure account. Provide the Resource group name for the NetApp account to be created.

## [Requirements](azure_rm_netapp_account_module.md#id3)

The below requirements are needed on the host that executes this module.

- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- For authentication with Azure NetApp log in before you run your tasks or playbook with `az login`.
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>
- Python azure-mgmt-netapp. Install using ‘pip install azure-mgmt-netapp’
- Python azure-mgmt. Install using ‘pip install azure-mgmt’
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- azure >= 2.0.0
- python >= 2.7

## [Parameters](azure_rm_netapp_account_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **active_directories**  list / elements=dictionary  *added in netapp.azure 21.2.0* | list of active directory dictionaries.  The list is currently limited to a single active directory (ANF or Azure limit of one AD per subscription). |
| **active_directory_id**  string | not used for create. Not needed for join. |
| **ad_name**  string  *added in netapp.azure 21.3.0* | Name of the active directory machine. Used only while creating kerberos volume. |
| **aes_encryption**  boolean | If enabled, AES encryption will be enabled for SMB communication.  **Choices:**   - `false` - `true` |
| **dns**  list / elements=string | list of DNS addresses. Required for create or join. |
| **domain**  string | Fully Qualified Active Directory DNS Domain Name. Required for create or join. |
| **kdc_ip**  string  *added in netapp.azure 21.3.0* | kdc server IP addresses for the active directory machine. Used only while creating kerberos volume. |
| **ldap_signing**  boolean | Specifies whether or not the LDAP traffic needs to be signed.  **Choices:**   - `false` - `true` |
| **organizational_unit**  string | LDAP Path for the Organization Unit where SMB Server machine accounts will be created (i.e. OU=SecondLevel,OU=FirstLevel). |
| **password**  string | see username. If password is present, the module is not idempotent, as we cannot check the current value. Required for create or join. |
| **server_root_ca_certificate**  string  *added in netapp.azure 21.3.0* | When LDAP over SSL/TLS is enabled, the LDAP client is required to have base64 encoded Active Directory Certificate Service’s self-signed root CA certificate, this optional parameter is used only for dual protocol with LDAP user-mapping volumes. |
| **site**  string | The Active Directory site the service will limit Domain Controller discovery to. |
| **smb_server_name**  string | Prefix for creating the SMB server’s computer account name in the Active Directory domain. Required for create or join. |
| **username**  string | Credentials that have permissions to create SMB server machine account in the AD domain. Required for create or join. |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in netapp.azure 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  *added in netapp.azure 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  **Choices:**   - `false` - `true` ← (default) |
| **auth_source**  string  *added in netapp.azure 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  *added in netapp.azure 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in netapp.azure 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **debug**  boolean | output details about current account if it exists.  **Choices:**   - `false` ← (default) - `true` |
| **location**  string | Resource location.  Required for create. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string / required | The name of the NetApp account. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **resource_group**  string / required | Name of the resource group. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **state**  string | State `present` will check that the NetApp account exists with the requested configuration.  State `absent` will delete the NetApp account.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |

## [Notes](azure_rm_netapp_account_module.md#id5)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.
> - The modules prefixed with azure_rm_netapp are built to support the Cloud Volume Services for Azure NetApp Files.

## [See Also](azure_rm_netapp_account_module.md#id6)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_netapp_account_module.md#id7)

```yaml+jinja
- name: Create NetApp Azure Account
  netapp.azure.azure_rm_netapp_account:
    resource_group: myResourceGroup
    name: testaccount
    location: eastus
    tags: {'abc': 'xyz', 'cba': 'zyx'}

- name: Modify Azure NetApp account (Join AD)
  netapp.azure.azure_rm_netapp_account:
    resource_group: myResourceGroup
    name: testaccount
    location: eastus
    active_directories:
      - site: ln
        dns: 10.10.10.10
        domain: domain.com
        smb_server_name: dummy
        password: xxxxxx
        username: laurentn

- name: Delete NetApp Azure Account
  netapp.azure.azure_rm_netapp_account:
    state: absent
    resource_group: myResourceGroup
    name: testaccount
    location: eastus

- name: Create Azure NetApp account (with AD)
  netapp.azure.azure_rm_netapp_account:
    resource_group: laurentngroupnodash
    name: tests-netapp11
    location: eastus
    tags:
      creator: laurentn
      use: Ansible
    active_directories:
      - site: ln
        dns: 10.10.10.10
        domain: domain.com
        smb_server_name: dummy
        password: xxxxxx
        username: laurentn
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.azure/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.azure)
