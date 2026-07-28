---
collection: ansible
version: "6"
title: "azure.azcollection.azure_rm_virtualhubconnection module – Manage Azure VirtualHub instance"
source_url: https://docs.ansible.com/projects/ansible/6/collections/azure/azcollection/azure_rm_virtualhubconnection_module.html
fetched_at: 2026-07-27T16:47:15+00:00
---
# azure.azcollection.azure_rm_virtualhubconnection module – Manage Azure VirtualHub instance

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
> see [Requirements](azure_rm_virtualhubconnection_module.md#ansible-collections-azure-azcollection-azure-rm-virtualhubconnection-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_virtualhubconnection`.

New in azure.azcollection 1.14.0

- [Synopsis](azure_rm_virtualhubconnection_module.md#synopsis)
- [Requirements](azure_rm_virtualhubconnection_module.md#requirements)
- [Parameters](azure_rm_virtualhubconnection_module.md#parameters)
- [Notes](azure_rm_virtualhubconnection_module.md#notes)
- [See Also](azure_rm_virtualhubconnection_module.md#see-also)
- [Examples](azure_rm_virtualhubconnection_module.md#examples)
- [Return Values](azure_rm_virtualhubconnection_module.md#return-values)

## [Synopsis](azure_rm_virtualhubconnection_module.md#id1)

- Create, update and delete instance of Azure VirtualHub.

## [Requirements](azure_rm_virtualhubconnection_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_virtualhubconnection_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  added in azure.azcollection 0.0.1 | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **allow_hub_to_remote_vnet_transit**  boolean | VirtualHub to RemoteVnet transit to enabled or not.  Choices:   - `false` - `true` |
| **allow_remote_vnet_to_use_hub_vnet_gateways**  boolean | Allow RemoteVnet to use Virtual Hub’s gateways.  Choices:   - `false` - `true` |
| **api_profile**  string  added in azure.azcollection 0.0.1 | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  Default: `"latest"` |
| **auth_source**  string  added in azure.azcollection 0.0.1 | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  Choices:   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  added in azure.azcollection 0.0.1 | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  Choices:   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  added in azure.azcollection 0.0.1 | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  Default: `"AzureCloud"` |
| **enable_internet_security**  boolean | Enable internet security.  Choices:   - `false` - `true` |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string / required | The name of the VirtualHub connection. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **remote_virtual_network**  dictionary | ID of the remote VNet to connect to. |
| **id**  string | The remote virtual network ID. |
| **resource_group**  string / required | The resource group name of the VirtualHub. |
| **routing_configuration**  dictionary | The Routing Configuration indicating the associated and propagated route tables on this connection. |
| **propagated_route_tables**  dictionary | The list of RouteTables to advertise the routes to. |
| **ids**  list / elements=dictionary | -The list of resource ids of all the virtual hub RouteTables. |
| **id**  string | The ID of the RouteTables. |
| **labels**  list / elements=string | The list of labels. |
| **vnet_routes**  dictionary | List of routes that control routing from VirtualHub into a virtual network connection. |
| **static_routes**  list / elements=dictionary | List of all Static Routes. |
| **address_prefixes**  list / elements=string | List of all address prefixes. |
| **name**  string | The name of the StaticRoute that is unique within a VnetRoute. |
| **next_hop_ip_address**  string | The ip address of the next hop. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **state**  string | Assert the state of the VirtualHub connection.  Use `present` to create or update an VirtualHub connection and `absent` to delete it.  Choices:   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **vhub_name**  string / required | The VirtualHub name. |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_virtualhubconnection_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_virtualhubconnection_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_virtualhubconnection_module.md#id6)

```yaml+jinja
- name: Create virtual hub connection
  azure_rm_virtualhubconnection:
    resource_group: myRG
    vhub_name: testhub
    name: Myconnection
    enable_internet_security: false
    allow_remote_vnet_to_use_hub_vnet_gateways: true
    allow_hub_to_remote_vnet_transit: true
    remote_virtual_network:
      id: /subscriptions/xxx-xxx/resourceGroups/myRG/providers/Microsoft.Network/virtualNetworks/testvnet
    routing_configuration:
      propagated_route_tables:
        labels:
          - labels1
          - labels3
        ids:
          - id: /subscriptions/xxx-xxx/resourceGroups/myRG/providers/Microsoft.Network/virtualHubs/testhub01/hubRouteTables/testtable
      vnet_routes:
        static_routes:
          - name: route1
            address_prefixes:
              - 10.1.0.0/16
              - 10.2.0.0/16
            next_hop_ip_address: 10.0.0.68
          - name: route2
            address_prefixes:
              - 10.4.0.0/16
            next_hop_ip_address: 10.0.0.65

- name: Delete virtual hub connection
  azure_rm_virtualhubconnection:
    resource_group: myRG
    vhub_name: testhub
    name: Myconnection
    state: absent
```

## [Return Values](azure_rm_virtualhubconnection_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **state**  complex | A list of dict results for the virtual hub connection info.  Returned: always |
| **allow_hub_to_remote_vnet_transit**  boolean | Enable hub to remote VNet transit.  Returned: always  Sample: `true` |
| **allow_remote_vnet_to_use_hub_vnet_gateways**  boolean | Allow remote VNet to use hub’s VNet gateways.  Returned: always  Sample: `true` |
| **enable_internet_security**  boolean | Enable internet security and default is enabled.  Returned: always  Sample: `true` |
| **etag**  string | A unique read-only string that changes whenever the resource is updated.  Returned: always  Sample: `"31102041-49e7-4cac-8573-aac1e1a16793"` |
| **id**  string | Resource ID.  Returned: always  Sample: `"/subscriptions/xxx-xxx/resourceGroups/myRG/providers/Microsoft.Network/virtualHubs/vhub/hubVirtualNetworkConnections/MyConnection"` |
| **name**  string | Resource name.  Returned: always  Sample: `"MyConnection"` |
| **provisioning_state**  string | The provisioning state of the virtual hub connection resource.  Returned: always  Sample: `"Succeeded"` |
| **remote_virtual_network**  complex | Name of ID of the remote VNet to connect to.  Returned: always |
| **id**  string | The ID of the remote VNet to connect to.  Returned: always  Sample: `"/subscriptions/xxx-xxx/resourceGroups/myRG/providers/Microsoft.Network/virtualNetworks/testvnet"` |
| **routing_configuration**  complex | The routing configuration information  Returned: always |
| **associated_route_table**  complex | The resource ID of route table associated with this routing configuration.  Returned: always |
| **id**  string | The ID of the routetable.  Returned: always  Sample: `"/subscriptions/xxx-xxx/resourceGroups/myRG/providers/Microsoft.Network/virtualHubs/testhub/hubRouteTables/rt_name"` |
| **propagated_route_tables**  complex | Space-separated list of resource id of propagated route tables.  Returned: always |
| **ids**  list / elements=string | The list resource ID of propagated route tables.  Returned: always  Sample: `[{"id": "/subscriptions/xxx-xxx/resourceGroups/myRG/providers/Microsoft.Network/virtualHubs/testhub/hubRouteTables/rt_name"}]` |
| **labels**  list / elements=string | Space-separated list of labels for propagated route tables.  Returned: always  Sample: `["labels1", "labels2"]` |
| **vnet_routes**  complex | The name of the Static Route that is unique within a Vnet Route.  Returned: always |
| **static_routes**  list / elements=string | The name of the Static Route.  Returned: always |
| **address_prefixes**  list / elements=string | Space-separated list of all address prefixes.  Returned: always  Sample: `["10.1.0.0/16", "10.2.0.0/16"]` |
| **name**  string | The name of static router.  Returned: always  Sample: `"route1"` |
| **next_hop_ip_address**  string | The next hop ip address.  Returned: always  Sample: `"10.0.0.65"` |

### Authors

- Fred-Sun (@Fred-Sun)
- Xu Zhang (@xuzhang3)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/azure/issues)
[Homepage](https://azure.microsoft.com)
[Repository (Sources)](https://github.com/ansible-collections/azure)
