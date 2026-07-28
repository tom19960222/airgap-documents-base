---
collection: ansible
version: "6"
title: "azure.azcollection.azure_rm_virtualmachinescaleset_info module – Get Virtual Machine Scale Set facts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/azure/azcollection/azure_rm_virtualmachinescaleset_info_module.html
fetched_at: 2026-07-27T16:47:19+00:00
---
# azure.azcollection.azure_rm_virtualmachinescaleset_info module – Get Virtual Machine Scale Set facts

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
> see [Requirements](azure_rm_virtualmachinescaleset_info_module.md#ansible-collections-azure-azcollection-azure-rm-virtualmachinescaleset-info-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_virtualmachinescaleset_info`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_virtualmachinescaleset_info_module.md#synopsis)
- [Requirements](azure_rm_virtualmachinescaleset_info_module.md#requirements)
- [Parameters](azure_rm_virtualmachinescaleset_info_module.md#parameters)
- [Notes](azure_rm_virtualmachinescaleset_info_module.md#notes)
- [See Also](azure_rm_virtualmachinescaleset_info_module.md#see-also)
- [Examples](azure_rm_virtualmachinescaleset_info_module.md#examples)
- [Return Values](azure_rm_virtualmachinescaleset_info_module.md#return-values)

## [Synopsis](azure_rm_virtualmachinescaleset_info_module.md#id1)

- Get facts for a virtual machine scale set.
- Note that this module was called azure.azcollection.azure_rm_virtualmachine_scaleset_facts before Ansible 2.8. The usage did not change.

## [Requirements](azure_rm_virtualmachinescaleset_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_virtualmachinescaleset_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  added in azure.azcollection 0.0.1 | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  added in azure.azcollection 0.0.1 | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  Default: `"latest"` |
| **auth_source**  string  added in azure.azcollection 0.0.1 | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  Choices:   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  added in azure.azcollection 0.0.1 | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  Choices:   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  added in azure.azcollection 0.0.1 | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  Default: `"AzureCloud"` |
| **format**  string | Format of the data returned.  If `raw` is selected information will be returned in raw format from Azure Python SDK.  If `curated` is selected the structure will be identical to input parameters of [azure.azcollection.azure_rm_virtualmachinescaleset](azure_rm_virtualmachinescaleset_module.md#ansible-collections-azure-azcollection-azure-rm-virtualmachinescaleset-module) module.  In Ansible 2.5 and lower facts are always returned in raw format.  Please note that this option will be deprecated in 2.10 when curated format will become the only supported format.  Choices:   - `"curated"` - `"raw"` ← (default) |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string | Limit results to a specific virtual machine scale set. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **resource_group**  string | The resource group to search for the desired virtual machine scale set. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  list / elements=string | Limit results by providing a list of tags. Format tags as ‘key’ or ‘key:value’. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_virtualmachinescaleset_info_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_virtualmachinescaleset_info_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_virtualmachinescaleset_info_module.md#id6)

```yaml+jinja
- name: Get facts for a virtual machine scale set
  azure_rm_virtualmachinescaleset_info:
    resource_group: myResourceGroup
    name: testvmss001
    format: curated

- name: Get facts for all virtual networks
  azure_rm_virtualmachinescaleset_info:
    resource_group: myResourceGroup

- name: Get facts by tags
  azure_rm_virtualmachinescaleset_info:
    resource_group: myResourceGroup
    tags:
      - testing
```

## [Return Values](azure_rm_virtualmachinescaleset_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vmss**  complex | List of virtual machine scale sets.  Returned: always |
| **admin_username**  string | Admin username used to access the host after it is created.  Returned: always  Sample: `"adminuser"` |
| **capacity**  integer | Capacity of VMSS.  Returned: always  Sample: `2` |
| **data_disks**  complex | List of attached data disks.  Returned: always |
| **caching**  string | Type of data disk caching.  Returned: always  Sample: `"ReadOnly"` |
| **disk_size_gb**  integer | The initial disk size in GB for blank data disks.  Returned: always  Sample: `64` |
| **lun**  integer | The logical unit number for data disk.  Returned: always  Sample: `0` |
| **managed_disk_type**  string | Managed data disk type.  Returned: always  Sample: `"Standard_LRS"` |
| **id**  string | Resource ID.  Returned: always  Sample: `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Compute/scalesets/myscaleset"` |
| **image**  complex | Image specification.  Returned: always |
| **offer**  string | The offer of the platform image or marketplace image used to create the virtual machine.  Returned: always  Sample: `"RHEL"` |
| **publisher**  string | Publisher name.  Returned: always  Sample: `"RedHat"` |
| **sku**  string | SKU name.  Returned: always  Sample: `"7-RAW"` |
| **version**  string | Image version.  Returned: always  Sample: `"7.5.2018050901"` |
| **load_balancer**  string | Load balancer name.  Returned: always  Sample: `"testlb"` |
| **location**  string | Resource location.  Returned: always  Sample: `"japaneast"` |
| **managed_disk_type**  string | Managed data disk type.  Returned: always  Sample: `"Standard_LRS"` |
| **name**  string | Resource name.  Returned: always  Sample: `"myvmss"` |
| **orchestrationMode**  string | The orchestration mode for the virtual machine scale set.  Returned: always  Sample: `"Flexible"` |
| **os_disk_caching**  string | Type of OS disk caching.  Returned: always  Sample: `"ReadOnly"` |
| **os_type**  string | Base type of operating system.  Returned: always  Sample: `"Linux"` |
| **overprovision**  boolean | Specifies whether the Virtual Machine Scale Set should be overprovisioned.  Returned: success  Sample: `true` |
| **platformFaultDomainCount**  integer | Fault Domain count for each placement group.  Returned: always  Sample: `1` |
| **resource_group**  string | Resource group.  Returned: always  Sample: `"myResourceGroup"` |
| **ssh_password_enabled**  boolean | Is SSH password authentication enabled. Valid only for Linux.  Returned: always  Sample: `true` |
| **subnet_name**  string | Subnet name.  Returned: always  Sample: `"testsubnet"` |
| **tags**  dictionary | Tags assigned to the resource. Dictionary of string:string pairs.  Returned: always  Sample: `{"tag1": "abc"}` |
| **tier**  string | SKU Tier.  Returned: always  Sample: `"Basic"` |
| **upgrade_policy**  string | Upgrade policy.  Returned: always  Sample: `"Manual"` |
| **virtual_network_name**  string | Associated virtual network name.  Returned: always  Sample: `"testvn"` |
| **vm_size**  string | Virtual machine size.  Returned: always  Sample: `"Standard_D4"` |

### Authors

- Sertac Ozercan (@sozercan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/azure/issues)
[Homepage](https://azure.microsoft.com)
[Repository (Sources)](https://github.com/ansible-collections/azure)
