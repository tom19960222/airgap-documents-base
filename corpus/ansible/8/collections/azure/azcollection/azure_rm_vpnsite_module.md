---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_vpnsite module – Manage Azure VpnSite instance"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_vpnsite_module.html
fetched_at: 2026-07-28T01:15:25+00:00
---
# azure.azcollection.azure_rm_vpnsite module – Manage Azure VpnSite instance

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
> see [Requirements](azure_rm_vpnsite_module.md#ansible-collections-azure-azcollection-azure-rm-vpnsite-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_vpnsite`.

New in azure.azcollection 1.5.0

- [Synopsis](azure_rm_vpnsite_module.md#synopsis)
- [Requirements](azure_rm_vpnsite_module.md#requirements)
- [Parameters](azure_rm_vpnsite_module.md#parameters)
- [Notes](azure_rm_vpnsite_module.md#notes)
- [See Also](azure_rm_vpnsite_module.md#see-also)
- [Examples](azure_rm_vpnsite_module.md#examples)
- [Return Values](azure_rm_vpnsite_module.md#return-values)

## [Synopsis](azure_rm_vpnsite_module.md#id1)

- Create, update and delete instance of Azure VpnSite.

## [Requirements](azure_rm_vpnsite_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_vpnsite_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **address_space**  dictionary | The AddressSpace that contains an array of IP address ranges. |
| **address_prefixes**  list / elements=string | A list of address blocks reserved for this virtual network in CIDR notation. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  **Choices:**   - `false` - `true` ← (default) |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **bgp_properties**  dictionary | The set of bgp properties. |
| **asn**  integer | The BGP speaker’s ASN. |
| **bgp_peering_address**  string | The BGP peering address and BGP identifier of this BGP speaker. |
| **bgp_peering_addresses**  list / elements=dictionary | BGP peering address with IP configuration ID for virtual network gateway. |
| **custom_bgp_ip_addresses**  list / elements=string | The list of custom BGP peering addresses which belong to IP configuration. |
| **default_bgp_ip_addresses**  list / elements=string | The list of default BGP peering addresses which belong to IP configuration. |
| **ipconfiguration_id**  string | The ID of IP configuration which belongs to gateway. |
| **tunnel_ip_addresses**  list / elements=string | The list of tunnel public IP addresses which belong to IP configuration. |
| **peer_weight**  integer | The weight added to routes learned from this BGP speaker. |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **device_properties**  dictionary | The device properties. |
| **device_model**  string | Model of the device. |
| **device_vendor**  string | Name of the device Vendor. |
| **link_speed_in_mbps**  integer | Link speed. |
| **ip_address**  string | The ip-address for the vpn-site. |
| **is_security_site**  boolean | IsSecuritySite flag.  **Choices:**   - `false` - `true` |
| **location**  string | The location of the VpnSite |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string / required | The name of the VpnSite. |
| **o365_policy**  dictionary | Office365 Policy. |
| **break_out_categories**  dictionary | Office365 breakout categories. |
| **allow**  boolean | Flag to control allow category.  **Choices:**   - `false` - `true` |
| **default**  boolean | Flag to control default category.  **Choices:**   - `false` - `true` |
| **optimize**  boolean | Flag to control optimize category.  **Choices:**   - `false` - `true` |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **resource_group**  string / required | The resource group name of the VpnSite. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **site_key**  string | The key for vpn-site that can be used for connections. |
| **state**  string | Assert the state of the VpnSite.  Use `present` to create or update an VpnSite and `absent` to delete it.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **virtual_wan**  dictionary | The VirtualWAN to which the vpnSite belongs. |
| **id**  string | The resource ID of the related virtual wan. |
| **vpn_site_links**  list / elements=dictionary | List of all vpn site links. |
| **bgp_properties**  dictionary | The set of bgp properties. |
| **asn**  integer | The BGP speaker’s ASN. |
| **bgp_peering_address**  string | The BGP peering address and BGP identifier of this BGP speaker. |
| **fqdn**  string | FQDN of vpn-site-link. |
| **ip_address**  string | The IP address for the vpn site link. |
| **link_properties**  dictionary | The link provider properties. |
| **link_provider_name**  string | Name of the link provider. |
| **link_speed_in_mbps**  integer | Link speed. |
| **name**  string | The name of the resource that is unique within a resource group.  This name can be used to access the resource. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_vpnsite_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_vpnsite_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_vpnsite_module.md#id6)

```yaml+jinja
- name: Create VpnSite
  azure_rm_vpnsite:
    resource_group: myResourceGroup
    name: vpnSite_name

- name: Delete Vpn Site
  azure_rm_vpnsite:
    resource_group: myResourceGroup
    name: vpnSite_name
```

## [Return Values](azure_rm_vpnsite_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **state**  complex | Current state of the vpn site.  **Returned:** success |
| **device_properties**  complex | The device properties.  **Returned:** always |
| **device_vendor**  string | Name of the device Vendor.  **Returned:** always  **Sample:** `"{'link_speed_in_mbps': 0}"` |
| **etag**  string | A unique read-only string that changes whenever the resource is updated.  **Returned:** always  **Sample:** `"8d7415fe-d92c-4331-92ea-460aadfb9648"` |
| **id**  string | Resource ID.  **Returned:** always  **Sample:** `"/subscriptions/xxx-xxx/resourceGroups/v-xisuRG/providers/Microsoft.Network/vpnSites/vpn_site_name"` |
| **is_security_site**  boolean | IsSecuritySite flag.  **Returned:** always  **Sample:** `false` |
| **location**  string | Resource location.  **Returned:** always  **Sample:** `"eastus"` |
| **name**  string | Resource name.  **Returned:** always  **Sample:** `"vpn_site_name"` |
| **provisioning_state**  string | The provisioning state of the VPN site resource.  **Returned:** always  **Sample:** `"Succeeded"` |
| **tags**  dictionary | Resource tags.  **Returned:** always  **Sample:** `{"key1": "value1"}` |
| **type**  string | Resource type.  **Returned:** always  **Sample:** `"Microsoft.Network/vpnSites"` |
| **virtual_wan**  complex | The VirtualWAN to which the vpnSite belongs.  **Returned:** always |
| **id**  string | Resource ID.  **Returned:** always  **Sample:** `"/subscriptions/xxx-xxx/resourceGroups/v-xisuRG/providers/Microsoft.Network/virtualWans/virtualwan_name"` |

### Authors

- Fred-Sun (@Fred-Sun)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
