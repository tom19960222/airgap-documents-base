---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_subnet_info module – Get Azure Subnet facts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_subnet_info_module.html
fetched_at: 2026-07-28T01:15:00+00:00
---
# azure.azcollection.azure_rm_subnet_info module – Get Azure Subnet facts

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
> see [Requirements](azure_rm_subnet_info_module.md#ansible-collections-azure-azcollection-azure-rm-subnet-info-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_subnet_info`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_subnet_info_module.md#synopsis)
- [Requirements](azure_rm_subnet_info_module.md#requirements)
- [Parameters](azure_rm_subnet_info_module.md#parameters)
- [Notes](azure_rm_subnet_info_module.md#notes)
- [See Also](azure_rm_subnet_info_module.md#see-also)
- [Examples](azure_rm_subnet_info_module.md#examples)
- [Return Values](azure_rm_subnet_info_module.md#return-values)

## [Synopsis](azure_rm_subnet_info_module.md#id1)

- Get facts of Azure Subnet.

## [Requirements](azure_rm_subnet_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_subnet_info_module.md#id3)

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
| **name**  string | The name of the subnet. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **resource_group**  string / required | The name of the resource group. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **virtual_network_name**  string / required | The name of the virtual network. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_subnet_info_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_subnet_info_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_subnet_info_module.md#id6)

```yaml+jinja
- name: Get facts of specific subnet
  azure_rm_subnet_info:
    resource_group: myResourceGroup
    virtual_network_name: myVirtualNetwork
    name: mySubnet

- name: List facts for all subnets in virtual network
  azure_rm_subnet_info:
    resource_group: myResourceGroup
    virtual_network_name: myVirtualNetwork
    name: mySubnet
```

## [Return Values](azure_rm_subnet_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **subnets**  complex | A list of dictionaries containing facts for subnet.  **Returned:** always |
| **address_prefix_cidr**  string | CIDR defining the IPv4 address space of the subnet.  **Returned:** always  **Sample:** `"10.1.0.0/16"` |
| **address_prefixes_cidr**  list / elements=string | CIDR defining the IPv4 and IPv6 address space of the subnet.  **Returned:** always  **Sample:** `["10.2.0.0/24", "fdda:e69b:1587:495e::/64"]` |
| **delegations**  list / elements=string | Associated delegation of subnets  **Returned:** always |
| **actions**  list / elements=string | list of actions associated with service of delegation  **Returned:** when delegation is present  **Sample:** `["Microsoft.Network/virtualNetworks/subnets/action"]` |
| **name**  string | name of delegation  **Returned:** when delegation is present  **Sample:** `"delegationname"` |
| **provisioning_state**  string | Provisioning state of delegation.  **Returned:** when delegation is present  **Sample:** `"Succeeded"` |
| **serviceName**  string | service associated to delegation  **Returned:** when delegation is present  **Sample:** `"Microsoft.ContainerInstance/containerGroups"` |
| **id**  string | Subnet resource ID.  **Returned:** always  **Sample:** `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/my VirtualNetwork/subnets/mySubnet"` |
| **name**  string | Name of the subnet.  **Returned:** always  **Sample:** `"mySubnet"` |
| **nat_gateway**  string | ID of the associated NAT Gateway.  **Returned:** when available  **Sample:** `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Network/natGateways/myGw"` |
| **private_endpoint_network_policies**  string | `Enabled` or `Disabled` apply network policies on private endpoints in the subnet.  **Returned:** always  **Sample:** `"Enabled"` |
| **private_link_service_network_policies**  string | `Enabled` or `Disabled` apply network policies on private link service in the subnet.  **Returned:** always  **Sample:** `"Disabled"` |
| **provisioning_state**  string | Provisioning state.  **Returned:** always  **Sample:** `"Succeeded"` |
| **resource_group**  string | Name of resource group.  **Returned:** always  **Sample:** `"myResourceGroup"` |
| **route_table**  string | Associated route table ID.  **Returned:** always  **Sample:** `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Network/routeTables/myRouteTable"` |
| **security_group**  string | Associated security group ID.  **Returned:** always  **Sample:** `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkSecurityGr oups/myNsg"` |
| **service_endpoints**  list / elements=string | List of service endpoints.  **Returned:** when available |
| **locations**  list / elements=string | A list of location names.  **Returned:** always  **Sample:** `["eastus", "westus"]` |
| **provisioning_state**  string | Provisioning state.  **Returned:** always  **Sample:** `"Succeeded"` |
| **service**  string | The type of the endpoint service.  **Returned:** always  **Sample:** `"Microsoft.Sql"` |
| **virtual_network_name**  string | Name of the containing virtual network.  **Returned:** always  **Sample:** `"myVirtualNetwork"` |

### Authors

- Zim Kalinowski (@zikalino)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
