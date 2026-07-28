---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_resource_info module – Generic facts of Azure resources"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_resource_info_module.html
fetched_at: 2026-07-28T01:14:35+00:00
---
# azure.azcollection.azure_rm_resource_info module – Generic facts of Azure resources

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
> see [Requirements](azure_rm_resource_info_module.md#ansible-collections-azure-azcollection-azure-rm-resource-info-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_resource_info`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_resource_info_module.md#synopsis)
- [Requirements](azure_rm_resource_info_module.md#requirements)
- [Parameters](azure_rm_resource_info_module.md#parameters)
- [Notes](azure_rm_resource_info_module.md#notes)
- [See Also](azure_rm_resource_info_module.md#see-also)
- [Examples](azure_rm_resource_info_module.md#examples)
- [Return Values](azure_rm_resource_info_module.md#return-values)

## [Synopsis](azure_rm_resource_info_module.md#id1)

- Obtain facts of any resource using Azure REST API.
- This module gives access to resources that are not supported via Ansible modules.
- Refer to <https://docs.microsoft.com/en-us/rest/api/> regarding details related to specific resource REST API.

## [Requirements](azure_rm_resource_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_resource_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **api_version**  string | Specific API version to be used. |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **method**  string | The HTTP method of the request or response. It must be uppercase.  **Choices:**   - `"GET"` ← (default) - `"PUT"` - `"POST"` - `"HEAD"` - `"PATCH"` - `"DELETE"` - `"MERGE"` |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **provider**  string | Provider type, should be specified in no URL is given. |
| **resource_group**  string | Resource group to be used.  Required if URL is not specified. |
| **resource_name**  string | Resource name. |
| **resource_type**  string | Resource type. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **subresource**  list / elements=dictionary | List of subresources.  **Default:** `[]` |
| **name**  string | Subresource name. |
| **namespace**  string | Subresource namespace. |
| **type**  string | Subresource type. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **url**  string | Azure RM Resource URL. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_resource_info_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_resource_info_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_resource_info_module.md#id6)

```yaml+jinja
- name: Get scaleset info
  azure_rm_resource_info:
    resource_group: myResourceGroup
    provider: compute
    resource_type: virtualmachinescalesets
    resource_name: myVmss
    api_version: "2017-12-01"

- name: Query all the resources in the resource group
  azure_rm_resource_info:
    resource_group: "{{ resource_group }}"
    resource_type: resources
```

## [Return Values](azure_rm_resource_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **response**  complex | Response specific to resource type.  **Returned:** always |
| **id**  string | Id of the Azure resource.  **Returned:** always  **Sample:** `"/subscriptions/xxxx...xxxx/resourceGroups/v-xisuRG/providers/Microsoft.Compute/virtualMachines/myVM"` |
| **location**  string | Resource location.  **Returned:** always  **Sample:** `"eastus"` |
| **name**  string | Resource name.  **Returned:** always  **Sample:** `"myVM"` |
| **properties**  complex | Specifies the virtual machine’s property.  **Returned:** always |
| **diagnosticsProfile**  complex | Specifies the boot diagnostic settings state.  **Returned:** always |
| **bootDiagnostics**  dictionary | A debugging feature, which to view Console Output and Screenshot to diagnose VM status.  **Returned:** always  **Sample:** `{"enabled": true, "storageUri": "https://vxisurgdiag.blob.core.windows.net/"}` |
| **hardwareProfile**  dictionary | Specifies the hardware settings for the virtual machine.  **Returned:** always  **Sample:** `{"vmSize": "Standard_D2s_v3"}` |
| **networkProfile**  complex | Specifies the network interfaces of the virtual machine.  **Returned:** always |
| **networkInterfaces**  list / elements=string | Describes a network interface reference.  **Returned:** always  **Sample:** `[{"id": "/subscriptions/xxxx...xxxx/resourceGroups/v-xisuRG/providers/Microsoft.Network/networkInterfaces/myvm441"}]` |
| **osProfile**  complex | Specifies the operating system settings for the virtual machine.  **Returned:** always |
| **adminUsername**  string | Specifies the name of the administrator account.  **Returned:** always  **Sample:** `"azureuser"` |
| **allowExtensionOperations**  boolean | Specifies whether extension operations should be allowed on the virtual machine.  This may only be set to False when no extensions are present on the virtual machine.  **Returned:** always  **Sample:** `true` |
| **computerName**  string | Specifies the host OS name of the virtual machine.  **Returned:** always  **Sample:** `"myVM"` |
| **linuxConfiguration**  dictionary | Specifies the Linux operating system settings on the virtual machine.  **Returned:** when OS type is Linux  **Sample:** `{"disablePasswordAuthentication": false, "provisionVMAgent": true}` |
| **requireGuestProvisionSignale**  boolean | Specifies the host require guest provision signal or not.  **Returned:** always  **Sample:** `true` |
| **secrets**  list / elements=string | Specifies set of certificates that should be installed onto the virtual machine.  **Returned:** always  **Sample:** `[]` |
| **provisioningState**  string | The provisioning state.  **Returned:** always  **Sample:** `"Succeeded"` |
| **storageProfile**  complex | Specifies the storage account type for the managed disk.  **Returned:** always |
| **dataDisks**  list / elements=string | Specifies the parameters that are used to add a data disk to virtual machine.  **Returned:** always  **Sample:** `[{"caching": "None", "createOption": "Attach", "diskSizeGB": 1023, "lun": 2, "managedDisk": {"id": "/subscriptions/xxxx....xxxx/resourceGroups/V-XISURG/providers/Microsoft.Compute/disks/testdisk2", "storageAccountType": "StandardSSD_LRS"}, "name": "testdisk2"}, {"caching": "None", "createOption": "Attach", "diskSizeGB": 1023, "lun": 1, "managedDisk": {"id": "/subscriptions/xxxx...xxxx/resourceGroups/V-XISURG/providers/Microsoft.Compute/disks/testdisk3", "storageAccountType": "StandardSSD_LRS"}, "name": "testdisk3"}]` |
| **imageReference**  dictionary | Specifies information about the image to use.  **Returned:** always  **Sample:** `{"offer": "UbuntuServer", "publisher": "Canonical", "sku": "20_04-lts", "version": "latest"}` |
| **osDisk**  dictionary | Specifies information about the operating system disk used by the virtual machine.  **Returned:** always  **Sample:** `{"caching": "ReadWrite", "createOption": "FromImage", "diskSizeGB": 30, "managedDisk": {"id": "/subscriptions/xxx...xxxx/resourceGroups/v-xisuRG/providers/Microsoft.Compute/disks/myVM_disk1_xxx", "storageAccountType": "Premium_LRS"}, "name": "myVM_disk1_xxx", "osType": "Linux"}` |
| **vmID**  string | Specifies the VM unique ID which is a 128-bits identifier that is encoded and stored in all Azure laaS VMs SMBIOS.  It can be read using platform BIOS commands.  **Returned:** always  **Sample:** `"eb86d9bb-6725-4787-a487-2e497d5b340c"` |
| **type**  string | The type of identity used for the virtual machine.  **Returned:** always  **Sample:** `"Microsoft.Compute/virtualMachines"` |

### Authors

- Zim Kalinowski (@zikalino)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
