---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_virtualhub module – Manage Azure VirtualHub instance"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_virtualhub_module.html
fetched_at: 2026-07-28T01:15:05+00:00
---
# azure.azcollection.azure_rm_virtualhub module – Manage Azure VirtualHub instance

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
> see [Requirements](azure_rm_virtualhub_module.md#ansible-collections-azure-azcollection-azure-rm-virtualhub-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_virtualhub`.

New in azure.azcollection 1.10.0

- [Synopsis](azure_rm_virtualhub_module.md#synopsis)
- [Requirements](azure_rm_virtualhub_module.md#requirements)
- [Parameters](azure_rm_virtualhub_module.md#parameters)
- [Notes](azure_rm_virtualhub_module.md#notes)
- [See Also](azure_rm_virtualhub_module.md#see-also)
- [Examples](azure_rm_virtualhub_module.md#examples)
- [Return Values](azure_rm_virtualhub_module.md#return-values)

## [Synopsis](azure_rm_virtualhub_module.md#id1)

- Create, update and delete instance of Azure VirtualHub.

## [Requirements](azure_rm_virtualhub_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_virtualhub_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **address_prefix**  string | Address-prefix for this VirtualHub. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  **Choices:**   - `false` - `true` ← (default) |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **azure_firewall**  dictionary | The azureFirewall associated with this VirtualHub. |
| **id**  string | Resource ID. |
| **bgp_connections**  list / elements=dictionary | List of references to Bgp Connections. |
| **id**  string | Resource ID. |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **enable_virtual_router_route_propogation**  boolean | Flag to control route propogation for VirtualRouter hub.  **Choices:**   - `false` - `true` |
| **express_route_gateway**  dictionary | The expressRouteGateway associated with this VirtualHub. |
| **id**  string | Resource ID. |
| **ip_configurations**  list / elements=dictionary | List of references to IpConfigurations. |
| **id**  string | Resource ID. |
| **location**  string | The location of the VirtualHub. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string / required | The name of the VirtualHub. |
| **p2_s_vpn_gateway**  dictionary | The P2SVpnGateway associated with this VirtualHub. |
| **id**  string | Resource ID. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **resource_group**  string / required | The resource group name of the VirtualHub. |
| **route_table**  dictionary | The routeTable associated with this virtual hub. |
| **routes**  list / elements=dictionary | List of all routes. |
| **address_prefixes**  list / elements=string | List of all addressPrefixes. |
| **next_hop_ip_address**  string | NextHop ip address. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **security_partner_provider**  dictionary | The securityPartnerProvider associated with this VirtualHub. |
| **id**  string | Resource ID. |
| **security_provider_name**  string | The Security Provider name. |
| **sku**  string | The sku of this VirtualHub. |
| **state**  string | Assert the state of the VirtualHub.  Use `present` to create or update an VirtualHub and `absent` to delete it.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **virtual_hub_route_table_v2_s**  list / elements=dictionary | List of all virtual hub route table v2s associated with this VirtualHub. |
| **attached_connections**  list / elements=string | List of all connections attached to this route table v2. |
| **name**  string | The name of the resource that is unique within a resource group.  This name can be used to access the resource. |
| **routes**  list / elements=dictionary | List of all routes. |
| **destination_type**  string | The type of destinations. |
| **destinations**  list / elements=string | List of all destinations. |
| **next_hop_type**  string | The type of next hops. |
| **next_hops**  list / elements=string | NextHops ip address. |
| **virtual_router_asn**  integer | VirtualRouter ASN. |
| **virtual_router_ips**  list / elements=string | VirtualRouter IPs. |
| **virtual_wan**  dictionary | The VirtualWAN to which the VirtualHub belongs. |
| **id**  string | Resource ID. |
| **vpn_gateway**  dictionary | The VpnGateway associated with this VirtualHub. |
| **id**  string | Resource ID. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_virtualhub_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_virtualhub_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_virtualhub_module.md#id6)

```yaml+jinja
- name: Create a VirtualHub
  azure_rm_virtualhub:
    resource_group: myResourceGroup
    name: my_virtual_hub_name
    address_prefix: 10.2.0.0/24
    sku: Standard
    location: eastus
    enable_virtual_router_route_propogation: false
    virtual_wan:
      id: /subscriptions/xxx-xxx/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualWans/fredwan

- name: Delete VirtualHub
  azure_rm_virtualhub:
    resource_group: myResourceGroup
    name: my_virtual_hub_name
    location: eastus
    state: absent
```

## [Return Values](azure_rm_virtualhub_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **state**  complex | Current state of the virtual hub.  **Returned:** always |
| **address_prefix**  string | Address-prefix for this VirtualHub.  **Returned:** always  **Sample:** `"10.2.0.0/24"` |
| **azure_firewall**  complex | The azureFirewall associated with this VirtualHub.  **Returned:** always |
| **id**  string | Resource ID.  **Returned:** always |
| **bgp_connections**  list / elements=string | List of references to Bgp Connections.  **Returned:** always |
| **id**  string | Resource ID.  **Returned:** always |
| **enable_virtual_router_route_propogation**  boolean | Flag to control route propogation for VirtualRouter hub.  **Returned:** always |
| **etag**  string | A unique read-only string that changes whenever the resource is updated.  **Returned:** always  **Sample:** `"cf8c0b06-d339-4155-95fd-2a363945cce4"` |
| **express_route_gateway**  dictionary | The expressRouteGateway associated with this VirtualHub.  **Returned:** always |
| **id**  string | Resource ID.  **Returned:** always |
| **id**  string | Resource ID.  **Returned:** always  **Sample:** `"/subscriptions/xxx-xxx/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualHubs/my_virtual_hub_name"` |
| **ip_configurations**  list / elements=string | List of references to IpConfigurations.  **Returned:** always |
| **id**  string | Resource ID.  **Returned:** always |
| **location**  string | Resource location.  **Returned:** always  **Sample:** `"eastus"` |
| **name**  string | Resource name.  **Returned:** always  **Sample:** `"my_virtual_hub_name"` |
| **p2_s_vpn_gateway**  complex | The P2SVpnGateway associated with this VirtualHub.  **Returned:** always |
| **id**  string | Resource ID.  **Returned:** always |
| **provisioning_state**  string | The provisioning state of the virtual hub resource.  **Returned:** always  **Sample:** `"Succeeded"` |
| **route_table**  complex | The routeTable associated with this virtual hub.  **Returned:** always |
| **routes**  list / elements=string | List of all routes.  **Returned:** always |
| **address_prefixes**  list / elements=string | List of all addressPrefixes.  **Returned:** always |
| **next_hop_ip_address**  string | NextHop ip address.  **Returned:** always |
| **routing_state**  string | The routing state.  **Returned:** always  **Sample:** `"Standard"` |
| **security_partner_provider**  complex | The securityPartnerProvider associated with this VirtualHub.  **Returned:** always |
| **id**  string | Resource ID.  **Returned:** always |
| **security_provider_name**  string | The Security Provider name.  **Returned:** always |
| **sku**  string | The sku of this VirtualHub.  **Returned:** always |
| **tags**  dictionary | Resource tags.  **Returned:** always  **Sample:** `{"key1": "value1"}` |
| **type**  string | Resource type.  **Returned:** always  **Sample:** `"Microsoft.Network/virtualHubs"` |
| **virtual_hub_route_table_v2_s**  complex | List of all virtual hub route table v2s associated with this VirtualHub.  **Returned:** always |
| **attached_connections**  list / elements=string | List of all connections attached to this route table v2.  **Returned:** always |
| **name**  string | The name of the resource that is unique within a resource group.  This name can be used to access the resource.  **Returned:** always |
| **routes**  list / elements=string | List of all routes.  **Returned:** always |
| **destination_type**  string | The type of destinations.  **Returned:** always |
| **destinations**  list / elements=string | List of all destinations.  **Returned:** always |
| **next_hop_type**  string | The type of next hops.  **Returned:** always |
| **next_hops**  list / elements=string | NextHops ip address.  **Returned:** always |
| **virtual_router_asn**  integer | VirtualRouter ASN.  **Returned:** always |
| **virtual_router_ips**  list / elements=string | VirtualRouter IPs.  **Returned:** always |
| **virtual_wan**  complex | The VirtualWAN to which the VirtualHub belongs.  **Returned:** always |
| **id**  string | Resource ID.  **Returned:** always  **Sample:** `"/subscriptions/xxx-xxx/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualWans/fredwan"` |
| **vpn_gateway**  complex | The VpnGateway associated with this VirtualHub.  **Returned:** always |
| **id**  string | Resource ID.  **Returned:** always |

### Authors

- Fred-Sun (@Fred-Sun)
- Haiyuan Zhang (@haiyuazhang)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
