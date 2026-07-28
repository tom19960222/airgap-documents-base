---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_multiplemanageddisks module – Manage Multiple Azure Manage Disks"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_multiplemanageddisks_module.html
fetched_at: 2026-07-28T01:13:56+00:00
---
# azure.azcollection.azure_rm_multiplemanageddisks module – Manage Multiple Azure Manage Disks

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
> see [Requirements](azure_rm_multiplemanageddisks_module.md#ansible-collections-azure-azcollection-azure-rm-multiplemanageddisks-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_multiplemanageddisks`.

New in azure.azcollection 1.14.0

- [Synopsis](azure_rm_multiplemanageddisks_module.md#synopsis)
- [Requirements](azure_rm_multiplemanageddisks_module.md#requirements)
- [Parameters](azure_rm_multiplemanageddisks_module.md#parameters)
- [Notes](azure_rm_multiplemanageddisks_module.md#notes)
- [See Also](azure_rm_multiplemanageddisks_module.md#see-also)
- [Examples](azure_rm_multiplemanageddisks_module.md#examples)
- [Return Values](azure_rm_multiplemanageddisks_module.md#return-values)

## [Synopsis](azure_rm_multiplemanageddisks_module.md#id1)

- Create, update and delete one or more Azure Managed Disk.
- This module can be used also to attach/detach disks to/from one or more virtual machines.

## [Requirements](azure_rm_multiplemanageddisks_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_multiplemanageddisks_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  **Choices:**   - `false` - `true` ← (default) |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **managed_by_extended**  list / elements=dictionary | List of name and resource group of the VMs to managed disks.  When *state=present*, the disks will be attached to the list of VMs specified.  When *state=present*, use *[]* to detach disks from all the VMs.  When *state=absent* and this parameter is defined, the disks will be detached from the list of VMs.  When *state=absent* and this parameter is not defined, the disks will be deleted. |
| **name**  string | The name of the attache VM. |
| **resource_group**  string | The resource group of the attache VM. |
| **managed_disks**  list / elements=dictionary | List of managed disks to create, update, or delete. |
| **attach_caching**  string | Disk caching policy controlled by VM. Will be used when attached to the VM defined by `managed_by`.  If this option is different from the current caching policy, the managed disk will be deattached and attached with current caching option again.  **Choices:**   - `""` - `"read_only"` - `"read_write"` |
| **create_option**  string | `import` from a VHD file in *source_uri* and `copy` from previous managed disk *source_uri*.  **Choices:**   - `"empty"` - `"import"` - `"copy"` |
| **disk_size_gb**  integer | Size in GB of the managed disk to be created.  Required when *create_option=empty*.  If *create_option=copy* then the value must be greater than or equal to the source’s size. |
| **location**  string | Valid Azure location. Defaults to location of the resource group. |
| **lun**  integer | The logical unit number for data disk.  This value is used to identify data disks within the VM and therefore must be unique for each data disk attached to a VM. |
| **max_shares**  integer | The maximum number of VMs that can attach to the disk at the same time.  Value greater than one indicates a disk that can be mounted on multiple VMs at the same time. |
| **name**  string / required | Name of the managed disk. |
| **os_type**  string | Type of Operating System.  Used when *create_option=copy* or *create_option=import* and the source is an OS disk.  If omitted during creation, no value is set.  If omitted during an update, no change is made.  Once set, this value cannot be cleared.  **Choices:**   - `"linux"` - `"windows"` |
| **resource_group**  string / required | Name of a resource group where the managed disk exists or will be created. |
| **source_uri**  aliases: source_resource_uri  string | URI to a valid VHD file to be used or the resource ID of the managed disk to copy.  Required when *create_option=import* or *create_option=copy*. |
| **storage_account_id**  string | The full path to the storage account the image is to be imported from.  Required when *create_option=import*. |
| **storage_account_type**  string | Type of storage for the managed disk.  If not specified, the disk is created as `Standard_LRS`.  `Standard_LRS` is for Standard HDD.  `StandardSSD_LRS` (added in 2.8) is for Standard SSD.  `StandardSSD_ZRS` is for Standard SSD Zone-redundant.  `Premium_LRS` is for Premium SSD.  `Premium_ZRS` is for Premium SSD Zone-redundant.  `UltraSSD_LRS` (added in 2.8) is for Ultra SSD, which is only available on select instance types.  See <https://docs.microsoft.com/en-us/azure/virtual-machines/windows/disks-types> for more information about disk types.  **Choices:**   - `"Standard_LRS"` - `"StandardSSD_LRS"` - `"StandardSSD_ZRS"` - `"Premium_LRS"` - `"Premium_ZRS"` - `"UltraSSD_LRS"` |
| **zone**  string | The Azure managed disk’s zone.  Allowed values are `1`, `2`, `3` and `''`.  **Choices:**   - `"1"` - `"2"` - `"3"` - `""` |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **state**  string | Assert the state of the managed disks.  Use `present` to create or update managed disks and/or attach/detach managed disks to a list of VMs depending on the value specified in *managed_by_extended*.  Use `absent` to detach/delete managed disks depending on the value specified in *managed_by_extended*.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_multiplemanageddisks_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_multiplemanageddisks_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_multiplemanageddisks_module.md#id6)

```yaml+jinja
- name: Create managed operating system disks from page blob and attach them to a list of VMs
  azure_rm_multiplemanageddisks:
    managed_disks:
      - name: mymanageddisk1
        location: eastus2
        resource_group: myResourceGroup
        create_option: import
        source_uri: https://storageaccountname.blob.core.windows.net/containername/blob-name.vhd
        storage_account_id: /subscriptions/<uuid>/resourceGroups/myResourceGroup/providers/Microsoft.Storage/storageAccounts/storageaccountname
        os_type: windows
        storage_account_type: Premium_LRS
      - name: mymanageddisk2
        location: eastus2
        resource_group: myResourceGroup
        create_option: import
        source_uri: https://storageaccountname.blob.core.windows.net/containername/blob-name.vhd
        storage_account_id: /subscriptions/<uuid>/resourceGroups/myResourceGroup/providers/Microsoft.Storage/storageAccounts/storageaccountname
        os_type: windows
        storage_account_type: Premium_LRS
    managed_by_extended:
      - resource_group: myResourceGroupTest
        name: TestVM

- name: Detach disks from the VMs specified in the list
  azure_rm_multiplemanageddisks:
    state: absent
    managed_disks:
      - name: mymanageddisk1
        location: eastus2
        resource_group: myResourceGroup
        create_option: import
        source_uri: https://storageaccountname.blob.core.windows.net/containername/blob-name.vhd
        storage_account_id: /subscriptions/<uuid>/resourceGroups/myResourceGroup/providers/Microsoft.Storage/storageAccounts/storageaccountname
        os_type: windows
        storage_account_type: Premium_LRS
      - name: mymanageddisk2
        location: eastus2
        resource_group: myResourceGroup
        create_option: import
        source_uri: https://storageaccountname.blob.core.windows.net/containername/blob-name.vhd
        storage_account_id: /subscriptions/<uuid>/resourceGroups/myResourceGroup/providers/Microsoft.Storage/storageAccounts/storageaccountname
        os_type: windows
        storage_account_type: Premium_LRS
    managed_by_extended:
      - resource_group: myResourceGroupTest
        name: TestVM1
      - resource_group: myResourceGroupTest
        name: TestVM2

- name: Detach managed disks from all VMs without deletion
  azure_rm_multiplemanageddisks:
    state: present
    managed_disks:
      - name: mymanageddisk1
        location: eastus2
        resource_group: myResourceGroup
      - name: mymanageddisk2
        location: eastus2
        resource_group: myResourceGroup
    managed_by_extended: []

- name: Detach managed disks from all VMs and delete them
  azure_rm_multiplemanageddisks:
    state: absent
    managed_disks:
      - name: mymanageddisk1
        location: eastus2
        resource_group: myResourceGroup
      - name: mymanageddisk2
        location: eastus2
        resource_group: myResourceGroup
```

## [Return Values](azure_rm_multiplemanageddisks_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **state**  complex | Current state of the managed disks.  **Returned:** always |
| **create_option**  string | Create option of the disk.  **Returned:** success  **Sample:** `"copy"` |
| **disk_size_gb**  string | Size in GB of the managed disk to be created.  **Returned:** success |
| **id**  string | Resource id.  **Returned:** success |
| **location**  string | Valid Azure location.  **Returned:** success |
| **managed_by**  string | Name of an existing virtual machine with which the disk is or will be associated, this VM should be in the same resource group.  **Returned:** success |
| **managed_by_extended**  list / elements=string | List ID of an existing virtual machine with which the disk is or will be associated.  **Returned:** success  **Sample:** `["/subscriptions/xxx-xxx/resourceGroups/myRG/providers/Microsoft.Compute/virtualMachines/testVM"]` |
| **max_shares**  integer | The maximum number of VMs that can attach to the disk at the same time.  Value greater than one indicates a disk that can be mounted on multiple VMs at the same time.  **Returned:** success  **Sample:** `3` |
| **name**  string | Name of the managed disk.  **Returned:** success |
| **os_type**  string | Type of Operating System.  **Returned:** success  **Sample:** `"linux"` |
| **source_uri**  string | URI to a valid VHD file to be used or the resource ID of the managed disk to copy.  **Returned:** success |
| **storage_account_id**  string | The full path to the storage account the image is to be imported from  **Returned:** success  **Sample:** `"/subscriptions/<uuid>/resourceGroups/<resource group name>/providers/Microsoft.Storage/storageAccounts/<storage account name>"` |
| **storage_account_type**  string | Type of storage for the managed disk.  See <https://docs.microsoft.com/en-us/azure/virtual-machines/windows/disks-types> for more information about this type.  **Returned:** success  **Sample:** `"Standard_LRS"` |
| **tags**  dictionary | Tags to assign to the managed disk.  **Returned:** success  **Sample:** `{"tag": "value"}` |

### Authors

- Aubin Bikouo (@abikouo)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
