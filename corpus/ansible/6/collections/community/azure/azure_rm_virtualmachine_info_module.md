---
collection: ansible
version: "6"
title: "community.azure.azure_rm_virtualmachine_info module – Get virtual machine facts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/azure/azure_rm_virtualmachine_info_module.html
fetched_at: 2026-07-27T17:05:58+00:00
---
# community.azure.azure_rm_virtualmachine_info module – Get virtual machine facts

> **Note:**
>
> This module is part of the [community.azure collection](https://galaxy.ansible.com/community/azure) (version 1.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.azure`.
> You need further requirements to be able to use this module,
> see [Requirements](azure_rm_virtualmachine_info_module.md#ansible-collections-community-azure-azure-rm-virtualmachine-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.azure.azure_rm_virtualmachine_info`.

- [DEPRECATED](azure_rm_virtualmachine_info_module.md#deprecated)
- [Synopsis](azure_rm_virtualmachine_info_module.md#synopsis)
- [Requirements](azure_rm_virtualmachine_info_module.md#requirements)
- [Parameters](azure_rm_virtualmachine_info_module.md#parameters)
- [Notes](azure_rm_virtualmachine_info_module.md#notes)
- [See Also](azure_rm_virtualmachine_info_module.md#see-also)
- [Examples](azure_rm_virtualmachine_info_module.md#examples)
- [Return Values](azure_rm_virtualmachine_info_module.md#return-values)
- [Status](azure_rm_virtualmachine_info_module.md#status)

## [DEPRECATED](azure_rm_virtualmachine_info_module.md#id1)

Removed in:
:   version 2.0.0

Why:
:   The Ansible collection community.azure is deprecated. Use azure.azcollection instead.

Alternative:
:   Use [azure.azcollection.azure_rm_virtualmachine_info](../../azure/azcollection/azure_rm_virtualmachine_info_module.md#ansible-collections-azure-azcollection-azure-rm-virtualmachine-info-module) instead.

## [Synopsis](azure_rm_virtualmachine_info_module.md#id2)

- Get facts for one or all virtual machines in a resource group.

## [Requirements](azure_rm_virtualmachine_info_module.md#id3)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_virtualmachine_info_module.md#id4)

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
| **name**  string | Name of the virtual machine. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **resource_group**  string | Name of the resource group containing the virtual machines (required when filtering by vm name). |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  string | Limit results by providing a list of tags. Format tags as ‘key’ or ‘key:value’. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_virtualmachine_info_module.md#id5)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_virtualmachine_info_module.md#id6)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_virtualmachine_info_module.md#id7)

```yaml+jinja
- name: Get facts for all virtual machines of a resource group
  community.azure.azure_rm_virtualmachine_info:
    resource_group: myResourceGroup

- name: Get facts by name
  community.azure.azure_rm_virtualmachine_info:
    resource_group: myResourceGroup
    name: myVm

- name: Get facts by tags
  community.azure.azure_rm_virtualmachine_info:
    resource_group: myResourceGroup
    tags:
      - testing
      - foo:bar
```

## [Return Values](azure_rm_virtualmachine_info_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vms**  complex | List of virtual machines.  Returned: always |
| **admin_username**  string | Administrator user name.  Returned: always  Sample: `"admin"` |
| **boot_diagnostics**  complex | Information about the boot diagnostics settings.  Returned: always |
| **console_screenshot_uri**  string | Contains a URI to grab a console screenshot.  Only present if enabled.  Returned: always  Sample: `"https://mystorageaccountname.blob.core.windows.net/bootdiagnostics-myvm01-a4db09a6-ab7f-4d80-9da8-fbceaef9288a/ myVm.a4db09a6-ab7f-4d80-9da8-fbceaef9288a.screenshot.bmp"` |
| **enabled**  boolean | Indicates if boot diagnostics are enabled.  Returned: always  Sample: `true` |
| **serial_console_log_uri**  string | Contains a URI to grab the serial console log.  Only present if enabled.  Returned: always  Sample: `"https://mystorageaccountname.blob.core.windows.net/bootdiagnostics-myvm01-a4db09a6-ab7f-4d80-9da8-fbceaef9288a/ myVm.a4db09a6-ab7f-4d80-9da8-fbceaef9288a.serialconsole.log"` |
| **storage_uri**  string | Indicates the storage account used by boot diagnostics.  Returned: always  Sample: `"https://mystorageaccountname.blob.core.windows.net/"` |
| **data_disks**  complex | List of attached data disks.  Returned: always |
| **caching**  string | Type of data disk caching.  Returned: always  Sample: `"ReadOnly"` |
| **disk_size_gb**  integer | The initial disk size in GB for blank data disks.  Returned: always  Sample: `64` |
| **lun**  integer | The logical unit number for data disk.  Returned: always  Sample: `0` |
| **managed_disk_type**  string | Managed data disk type.  Returned: always  Sample: `"Standard_LRS"` |
| **id**  string | Resource ID.  Returned: always  Sample: `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualMachines/myVm"` |
| **image**  complex | Image specification.  Returned: always |
| **id**  string | Custom image resource ID.  Returned: when created from custom image  Sample: `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Compute/images/myImage"` |
| **offer**  string | The offer of the platform image or marketplace image used to create the virtual machine.  Returned: when created from marketplace image  Sample: `"RHEL"` |
| **publisher**  string | Publisher name.  Returned: when created from marketplace image  Sample: `"RedHat"` |
| **sku**  string | SKU name.  Returned: when created from marketplace image  Sample: `"7-RAW"` |
| **version**  string | Image version.  Returned: when created from marketplace image  Sample: `"7.5.2018050901"` |
| **location**  string | Resource location.  Returned: always  Sample: `"japaneast"` |
| **name**  string | Resource name.  Returned: always  Sample: `"myVm"` |
| **network_interface_names**  list / elements=string | List of attached network interfaces.  Returned: always  Sample: `["myNetworkInterface"]` |
| **os_disk_caching**  string | Type of OS disk caching.  Returned: always  Sample: `"ReadOnly"` |
| **os_type**  string | Base type of operating system.  Returned: always  Sample: `"Linux"` |
| **power_state**  string | Power state of the virtual machine.  Returned: always  Sample: `"running"` |
| **resource_group**  string | Resource group.  Returned: always  Sample: `"myResourceGroup"` |
| **state**  string | State of the resource.  Returned: always  Sample: `"present"` |
| **tags**  dictionary | Resource tags.  Returned: always  Sample: `{"key1": "value1"}` |
| **vm_size**  string | Virtual machine size.  Returned: always  Sample: `"Standard_D4"` |

## [Status](azure_rm_virtualmachine_info_module.md#id9)

- This module will be removed in version 2.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](azure_rm_virtualmachine_info_module.md#deprecated).

### Authors

- Gustavo Muniz do Carmo (@gustavomcarmo)
- Zim Kalinowski (@zikalino)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.azure/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.azure)
