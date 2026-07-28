---
collection: ansible
version: "8"
title: "netapp.azure.azure_rm_netapp_volume module – Manage NetApp Azure Files Volume"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/azure/azure_rm_netapp_volume_module.html
fetched_at: 2026-07-28T02:41:03+00:00
---
# netapp.azure.azure_rm_netapp_volume module – Manage NetApp Azure Files Volume

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
> see [Requirements](azure_rm_netapp_volume_module.md#ansible-collections-netapp-azure-azure-rm-netapp-volume-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.azure.azure_rm_netapp_volume`.

New in netapp.azure 19.10.0

- [Synopsis](azure_rm_netapp_volume_module.md#synopsis)
- [Requirements](azure_rm_netapp_volume_module.md#requirements)
- [Parameters](azure_rm_netapp_volume_module.md#parameters)
- [Notes](azure_rm_netapp_volume_module.md#notes)
- [See Also](azure_rm_netapp_volume_module.md#see-also)
- [Examples](azure_rm_netapp_volume_module.md#examples)
- [Return Values](azure_rm_netapp_volume_module.md#return-values)

## [Synopsis](azure_rm_netapp_volume_module.md#id2)

- Create and delete NetApp Azure volume.

## [Requirements](azure_rm_netapp_volume_module.md#id3)

The below requirements are needed on the host that executes this module.

- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- For authentication with Azure NetApp log in before you run your tasks or playbook with `az login`.
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>
- Python azure-mgmt-netapp. Install using ‘pip install azure-mgmt-netapp’
- Python azure-mgmt. Install using ‘pip install azure-mgmt’
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- azure >= 2.0.0
- python >= 2.7

## [Parameters](azure_rm_netapp_volume_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **account_name**  string / required | The name of the NetApp account. |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in netapp.azure 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  *added in netapp.azure 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  **Choices:**   - `false` - `true` ← (default) |
| **auth_source**  string  *added in netapp.azure 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  *added in netapp.azure 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in netapp.azure 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **feature_flags**  dictionary  *added in netapp.azure 21.9.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **file_path**  string | A unique file path for the volume. Used when creating mount targets. |
| **location**  string | Resource location.  Required for create. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string / required | The name of the volume. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **pool_name**  string / required | The name of the capacity pool. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **protocol_types**  list / elements=string  *added in netapp.azure 21.2.0* | Protocol types - NFSv3, NFSv4.1, CIFS (for SMB). |
| **resource_group**  string / required | Name of the resource group. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **service_level**  string | The service level of the file system.  default is Premium.  **Choices:**   - `"Premium"` - `"Standard"` - `"Ultra"` |
| **size**  integer  *added in netapp.azure 20.5.0* | Provisioned size of the volume (in GiB).  Minimum size is 100 GiB. Upper limit is 100TiB  default is 100GiB. |
| **state**  string | State `present` will check that the volume exists with the requested configuration.  State `absent` will delete the volume.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subnet_name**  aliases: subnet_id  string  *added in netapp.azure 21.1.0* | Azure resource name for a delegated subnet. Must have the delegation Microsoft.NetApp/volumes.  Provide name of the subnet ID.  Required for create. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **virtual_network**  string | The name of the virtual network required for the subnet to create a volume.  Required for create. |
| **vnet_resource_group_for_subnet**  string  *added in netapp.azure 20.5.0* | Only required if virtual_network to be used is of different resource_group.  Name of the resource group for virtual_network and subnet_name to be used. |

## [Notes](azure_rm_netapp_volume_module.md#id5)

> **Note:**
>
> - feature_flags is setting ignore_change_ownership_mode to true by default to bypass a ‘change ownership mode’ issue with azure-mgmt-netapp 4.0.0.
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.
> - The modules prefixed with azure_rm_netapp are built to support the Cloud Volume Services for Azure NetApp Files.

## [See Also](azure_rm_netapp_volume_module.md#id6)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_netapp_volume_module.md#id7)

```yaml+jinja
- name: Create Azure NetApp volume
  netapp.azure.azure_rm_netapp_volume:
    resource_group: myResourceGroup
    account_name: tests-netapp
    pool_name: tests-pool
    name: tests-volume2
    location: eastus
    file_path: tests-volume2
    virtual_network: myVirtualNetwork
    vnet_resource_group_for_subnet: myVirtualNetworkResourceGroup
    subnet_name: test
    service_level: Ultra
    size: 100

- name: Delete Azure NetApp volume
  netapp.azure.azure_rm_netapp_volume:
    state: absent
    resource_group: myResourceGroup
    account_name: tests-netapp
    pool_name: tests-pool
    name: tests-volume2
```

## [Return Values](azure_rm_netapp_volume_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **mount_path**  string | Returns mount_path of the Volume  **Returned:** always |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.azure/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.azure)
