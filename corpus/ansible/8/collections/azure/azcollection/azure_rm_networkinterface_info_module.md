---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_networkinterface_info module – Get network interface facts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_networkinterface_info_module.html
fetched_at: 2026-07-28T01:14:05+00:00
---
# azure.azcollection.azure_rm_networkinterface_info module – Get network interface facts

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
> see [Requirements](azure_rm_networkinterface_info_module.md#ansible-collections-azure-azcollection-azure-rm-networkinterface-info-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_networkinterface_info`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_networkinterface_info_module.md#synopsis)
- [Requirements](azure_rm_networkinterface_info_module.md#requirements)
- [Parameters](azure_rm_networkinterface_info_module.md#parameters)
- [Notes](azure_rm_networkinterface_info_module.md#notes)
- [See Also](azure_rm_networkinterface_info_module.md#see-also)
- [Examples](azure_rm_networkinterface_info_module.md#examples)
- [Return Values](azure_rm_networkinterface_info_module.md#return-values)

## [Synopsis](azure_rm_networkinterface_info_module.md#id1)

- Get facts for a specific network interface or all network interfaces within a resource group.

## [Requirements](azure_rm_networkinterface_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_networkinterface_info_module.md#id3)

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
| **name**  string | Only show results for a specific network interface. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **resource_group**  string | Name of the resource group containing the network interface(s). Required when searching by name. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  list / elements=string | Limit results by providing a list of tags. Format tags as ‘key’ or ‘key:value’. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_networkinterface_info_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_networkinterface_info_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_networkinterface_info_module.md#id6)

```yaml+jinja
- name: Get facts for one network interface
  azure_rm_networkinterface_info:
    resource_group: myResourceGroup
    name: nic001

- name: Get network interfaces within a resource group
  azure_rm_networkinterface_info:
    resource_group: myResourceGroup

- name: Get network interfaces by tag
  azure_rm_networkinterface_info:
    resource_group: myResourceGroup
    tags:
      - testing
      - foo:bar
```

## [Return Values](azure_rm_networkinterface_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **azure_networkinterfaces**  list / elements=string | List of network interface dicts.  **Returned:** always  **Sample:** `[{"dns_settings": {"applied_dns_servers": [], "dns_servers": [], "internal_dns_name_label": null, "internal_fqdn": null}, "enable_ip_forwarding": false, "etag": "W/\"59726bfc-08c4-44ed-b900-f6a559876a9d\"", "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup/providers/Microsoft.Network/networkInterfaces/nic003", "ip_configuration": {"name": "default", "private_ip_address": "10.10.0.4", "private_ip_allocation_method": "Dynamic", "public_ip_address": {"id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup/providers/Microsoft.Network/publicIPAddresses/publicip001", "name": "publicip001"}, "subnet": {"id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup/providers/Microsoft.Network/virtualNetworks/vnet001/subnets/subnet001", "name": "subnet001", "virtual_network_name": "vnet001"}}, "location": "westus", "mac_address": null, "name": "nic003", "network_security_group": {"id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup/providers/Microsoft.Network/networkSecurityGroups/secgroup001", "name": "secgroup001"}, "primary": null, "provisioning_state": "Succeeded", "tags": {}, "type": "Microsoft.Network/networkInterfaces"}]` |
| **networkinterfaces**  list / elements=string | List of network interface dicts. Each dict contains parameters can be passed to [azure.azcollection.azure_rm_networkinterface](azure_rm_networkinterface_module.md#ansible-collections-azure-azcollection-azure-rm-networkinterface-module) module.  **Returned:** always |
| **create_with_security_group**  boolean | Specifies whether a default security group should be be created with the NIC. Only applies when creating a new NIC.  **Returned:** success |
| **dns_servers**  list / elements=string | Which DNS servers should the NIC lookup.  List of IP addresses.  **Returned:** success |
| **dns_settings**  complex | The DNS settings in network interface.  **Returned:** success |
| **applied_dns_servers**  list / elements=string | If the VM that uses this NIC is part of an Availability Set, then this list will have the union of all DNS servers from all NICs that are part of the Availability Set. This property is what is configured on each of those VMs.  **Returned:** success |
| **dns_servers**  list / elements=string | List of DNS servers IP addresses.  **Returned:** success |
| **internal_dns_name_label**  string | Relative DNS name for this NIC used for internal communications between VMs in the same virtual network.  **Returned:** success |
| **internal_fqdn**  string | Fully qualified DNS name supporting internal communications between VMs in the same virtual network.  **Returned:** success |
| **enable_accelerated_networking**  boolean | Specifies whether the network interface should be created with the accelerated networking feature or not.  **Returned:** success |
| **enable_ip_forwarding**  boolean | Whether to enable IP forwarding  **Returned:** success |
| **id**  string | Id of the network interface.  **Returned:** success |
| **ip_configurations**  complex | List of IP configurations, if contains multiple configurations.  **Returned:** success |
| **application_gateway_backend_address_pools**  list / elements=string  *added in azure.azcollection 1.10.0* | List of existing application gateway backend address pools associated with the network interface.  **Returned:** success |
| **application_security_groups**  list / elements=string | List of Application security groups.  **Returned:** success  **Sample:** `["/subscriptions/<subsid>/resourceGroups/<rg>/providers/Microsoft.Network/applicationSecurityGroups/myASG"]` |
| **load_balancer_backend_address_pools**  list / elements=string | List of existing load-balancer backend address pools associated with the network interface.  **Returned:** success |
| **name**  string | Name of the IP configuration.  **Returned:** success |
| **primary**  boolean | Whether the IP configuration is the primary one in the list.  **Returned:** success |
| **private_ip_address**  list / elements=string | Private IP address for the IP configuration.  **Returned:** success |
| **private_ip_allocation_method**  string | Private IP allocation method.  **Returned:** success |
| **public_ip_address**  string | Name of the public IP address. None for disable IP address.  **Returned:** success |
| **public_ip_allocation_method**  string | Public IP allocation method.  **Returned:** success |
| **location**  string | Azure location.  **Returned:** success |
| **mac_address**  string | The MAC address of the network interface.  **Returned:** success |
| **name**  string | Name of the network interface.  **Returned:** success |
| **provisioning_state**  string | The provisioning state of the network interface.  **Returned:** success |
| **resource_group**  string | Name of a resource group where the network interface exists.  **Returned:** success |
| **security_group**  string | A security group resource ID with which to associate the network interface.  **Returned:** success |
| **subnet**  string | Name of an existing subnet within the specified virtual network.  **Returned:** success |
| **tags**  dictionary | Tags of the network interface.  **Returned:** success |
| **virtual_network**  any | An existing virtual network with which the network interface will be associated.  It is a dict which contains *name* and *resource_group* of the virtual network.  **Returned:** success |

### Authors

- Chris Houseknecht (@chouseknecht)
- Matt Davis (@nitzmahone)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
