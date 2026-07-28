---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_vmssnetworkinterface_info module – Get information about network interface in virtul machine scale"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_vmssnetworkinterface_info_module.html
fetched_at: 2026-07-28T01:15:24+00:00
---
# azure.azcollection.azure_rm_vmssnetworkinterface_info module – Get information about network interface in virtul machine scale

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
> see [Requirements](azure_rm_vmssnetworkinterface_info_module.md#ansible-collections-azure-azcollection-azure-rm-vmssnetworkinterface-info-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_vmssnetworkinterface_info`.

New in azure.azcollection 1.15.0

- [Synopsis](azure_rm_vmssnetworkinterface_info_module.md#synopsis)
- [Requirements](azure_rm_vmssnetworkinterface_info_module.md#requirements)
- [Parameters](azure_rm_vmssnetworkinterface_info_module.md#parameters)
- [Notes](azure_rm_vmssnetworkinterface_info_module.md#notes)
- [See Also](azure_rm_vmssnetworkinterface_info_module.md#see-also)
- [Examples](azure_rm_vmssnetworkinterface_info_module.md#examples)
- [Return Values](azure_rm_vmssnetworkinterface_info_module.md#return-values)

## [Synopsis](azure_rm_vmssnetworkinterface_info_module.md#id1)

- Get information about network interface in virtual machine scale set.

## [Requirements](azure_rm_vmssnetworkinterface_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_vmssnetworkinterface_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string | The name of the network interface.  If configure *name*, you must set the parameters *vm_index*. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **resource_group**  string / required | Name of the resource group. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **vm_index**  string | The virtual machine index, such as *vm_index=0*. |
| **vmss_name**  string / required | The name of the virtual machine scale set. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_vmssnetworkinterface_info_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_vmssnetworkinterface_info_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_vmssnetworkinterface_info_module.md#id6)

```yaml+jinja
- name: Get information by the network name
  azure_rm_vmssnetworkinterface_info:
    resource_group: myResourceGroup
    name: nic001
    vmss_name: testVMSS
    vm_index: 0

- name: Get all network interface information in virtual machine scale set
  azure_rm_vmssnetworkinterface_info:
    resource_group: myResourceGroup
    vmss_name: testVMSS

- name: Get all network interface information in the same virtual machine index.
  azure_rm_vmssnetworkinterface_info:
    resource_group: myResourceGroup
    vmss_name: testVMSS
    vm_index: 1
```

## [Return Values](azure_rm_vmssnetworkinterface_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vmss_networkinterfaces**  complex | List of network interface dicts. Each dict contains parameters can be passed to azure.azcollection.azure_rm_vmssnetworkinterface module.  **Returned:** always |
| **create_with_security_group**  boolean | Specifies whether a default security group should be be created with the NIC. Only applies when creating a new NIC.  **Returned:** always  **Sample:** `true` |
| **dns_servers**  list / elements=string | Which DNS servers should the NIC lookup.  List of IP addresses.  **Returned:** always  **Sample:** `[]` |
| **dns_settings**  complex | The DNS settings in network interface.  **Returned:** always |
| **applied_dns_servers**  list / elements=string | If the VM that uses this NIC is part of an Availability Set, then this list will have the union of all DNS servers from all NICs that are part of the Availability Set. This property is what is configured on each of those VMs.  **Returned:** always  **Sample:** `[]` |
| **dns_servers**  list / elements=string | List of DNS servers IP addresses.  **Returned:** always  **Sample:** `[]` |
| **internal_dns_name_label**  string | Relative DNS name for this NIC used for internal communications between VMs in the same virtual network.  **Returned:** always |
| **internal_fqdn**  string | Fully qualified DNS name supporting internal communications between VMs in the same virtual network.  **Returned:** always |
| **enable_accelerated_networking**  boolean | Specifies whether the network interface should be created with the accelerated networking feature or not.  **Returned:** always  **Sample:** `true` |
| **enable_ip_forwarding**  boolean | Whether to enable IP forwarding  **Returned:** always  **Sample:** `true` |
| **id**  string | Id of the network interface.  **Returned:** always  **Sample:** `"/subscriptions/xxx-xxx/resourceGroups/RG/providers/Microsoft.Compute/virtualMachineScaleSets/fredvmss/virtualMachines/1/networkInterfaces/nic01"` |
| **ip_configurations**  complex | List of IP configurations, if contains multiple configurations.  **Returned:** always |
| **application_gateway_backend_address_pools**  string | List of existing application gateway backend address pools associated with the network interface.  **Returned:** always |
| **application_security_groups**  string | List of Application security groups.  **Returned:** always  **Sample:** `"/subscriptions/<subsid>/resourceGroups/<rg>/providers/Microsoft.Network/applicationSecurityGroups/myASG"` |
| **load_balancer_backend_address_pools**  string | List of existing load-balancer backend address pools associated with the network interface.  **Returned:** always |
| **name**  string | Name of the IP configuration.  **Returned:** always  **Sample:** `"defaultIpConfiguration"` |
| **primary**  boolean | Whether the IP configuration is the primary one in the list.  **Returned:** always  **Sample:** `true` |
| **private_ip_address**  string | Private IP address for the IP configuration.  **Returned:** always  **Sample:** `"10.3.0.5"` |
| **private_ip_allocation_method**  string | Private IP allocation method.  **Returned:** always  **Sample:** `"Dynamic"` |
| **public_ip_address**  string | Name of the public IP address. None for disable IP address.  **Returned:** always |
| **public_ip_allocation_method**  string | Public IP allocation method.  **Returned:** always |
| **location**  string | Azure location.  **Returned:** always  **Sample:** `"eastus"` |
| **mac_address**  string | The MAC address of the network interface.  **Returned:** always  **Sample:** `"00-0D-3A-17-EC-36"` |
| **name**  string | Name of the network interface.  **Returned:** always  **Sample:** `"nic01"` |
| **provisioning_state**  string | The provisioning state of the network interface.  **Returned:** always  **Sample:** `"Succeeded"` |
| **resource_group**  string | Name of a resource group where the network interface exists.  **Returned:** always  **Sample:** `"RG"` |
| **security_group**  string | A security group resource ID with which to associate the network interface.  **Returned:** always  **Sample:** `"/subscriptions/xxx-xxx/resourceGroups/RG/providers/Microsoft.Network/networkSecurityGroups/nic01"` |
| **subnet**  string | Name of an existing subnet within the specified virtual network.  **Returned:** always  **Sample:** `"default"` |
| **tags**  dictionary | Tags of the network interface.  **Returned:** always  **Sample:** `{"key1": "value1"}` |
| **virtual_network**  dictionary | An existing virtual network with which the network interface will be associated.  It is a dict which contains *name* and *resource_group* of the virtual network.  **Returned:** always  **Sample:** `{"name": "vnet01", "resource_group": "RG"}` |

### Authors

- xuzhang3 (@xuzhang3)
- Fred-sun (@Fred-sun)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
