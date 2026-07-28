---
collection: ansible
version: "6"
title: "azure.azcollection.azure_rm_expressroute module – Manage Express Route Circuits"
source_url: https://docs.ansible.com/projects/ansible/6/collections/azure/azcollection/azure_rm_expressroute_module.html
fetched_at: 2026-07-27T16:46:17+00:00
---
# azure.azcollection.azure_rm_expressroute module – Manage Express Route Circuits

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
> see [Requirements](azure_rm_expressroute_module.md#ansible-collections-azure-azcollection-azure-rm-expressroute-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_expressroute`.

New in azure.azcollection 1.7.0

- [Synopsis](azure_rm_expressroute_module.md#synopsis)
- [Requirements](azure_rm_expressroute_module.md#requirements)
- [Parameters](azure_rm_expressroute_module.md#parameters)
- [Notes](azure_rm_expressroute_module.md#notes)
- [See Also](azure_rm_expressroute_module.md#see-also)
- [Examples](azure_rm_expressroute_module.md#examples)
- [Return Values](azure_rm_expressroute_module.md#return-values)

## [Synopsis](azure_rm_expressroute_module.md#id3)

- Create, update and delete instance of Express Route.

## [Requirements](azure_rm_expressroute_module.md#id4)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_expressroute_module.md#id5)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  added in azure.azcollection 0.0.1 | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **allow_classic_operations**  boolean | Support for classic operations.  Choices:   - `false` - `true` |
| **api_profile**  string  added in azure.azcollection 0.0.1 | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  Default: `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  Choices:   - `false` - `true` ← (default) |
| **auth_source**  string  added in azure.azcollection 0.0.1 | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  Choices:   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **authorizations**  list / elements=dictionary | The list of authorizations. |
| **name**  string / required | Name of the authorization. |
| **cert_validation_mode**  string  added in azure.azcollection 0.0.1 | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  Choices:   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  added in azure.azcollection 0.0.1 | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  Default: `"AzureCloud"` |
| **global_reach_enabled**  boolean | Flag denoting global reach status.  Choices:   - `false` - `true` |
| **location**  string | Resource location. If not set, location from the resource group will be used as default. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string / required | Unique name of the app service plan to create or update. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **resource_group**  string / required | Name of the resource group to which the resource belongs. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **service_provider_properties**  dictionary | The service Provider properties |
| **bandwidth_in_mbps**  string | The bandwidth of the circuit when the circuit is provisioned on an ExpressRoutePort resource. |
| **peering_location**  string | The peering location |
| **service_provider_name**  string | Name of service provider |
| **sku**  dictionary | The name of the SKU.  Please see [`https://azure.microsoft.com/en-in/pricing/details/expressroute/ <>`__](azure_rm_expressroute_module.md#id1)  Required sku when *state=present*. |
| **family**  string / required | the family of the SKU  Choices:   - `"metereddata"` - `"unlimiteddata"` |
| **tier**  string / required | The tier of the SKU  Choices:   - `"standard"` - `"premium"` |
| **state**  string | Assert the state of the express route.  Use `present` to create or update an express route and `absent` to delete it.  Choices:   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_expressroute_module.md#id6)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_expressroute_module.md#id7)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_expressroute_module.md#id8)

```yaml+jinja
- name: "Create Express route"
  azure_rm_expressroute:
    resource_group: rg
    location: eastus
    name: exp
    allow_classic_operations: true
    global_reach_enabled: false
    tags:
       - a: b
    authorizations:
       - name: authorization_test
    service_provider_properties:
      service_provider_name: Aryaka Networks
      peering_location: Seattle
      bandwidth_in_mbps: '200'
    sku:
      tier: premium
      family: metereddata

- name: Delete Express route
  azure_rm_expressroute:
    resource_group: rg
    name: exp
    state: absent
```

## [Return Values](azure_rm_expressroute_module.md#id9)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **state**  dictionary | Current state of the express route.  Returned: always  Sample: `{"additional_properties": {}, "allow_classic_operations": true, "authorizations": [{"authorization_key": "d83e18b5-0200-4e0b-9cdb-6fdf95b00267", "authorization_use_status": "Available", "etag": "W/'09572845-c667-410c-b664-ed8e39242c13'", "id": "/subscriptions/subs_id/resourceGroups/rg/providers/Microsoft.Network/expressRouteCircuits/exp/authorizations/az", "name": "authorization_test", "provisioning_state": "Succeeded", "type": "Microsoft.Network/expressRouteCircuits/authorizations"}], "bandwidth_in_gbps": null, "circuit_provisioning_state": "Enabled", "express_route_port": null, "gateway_manager_etag": "", "global_reach_enabled": false, "id": "/subscriptions/subs_id/resourceGroups/rg/providers/Microsoft.Network/expressRouteCircuits/exp", "location": "eastus", "name": "exp", "peerings": [], "provisioning_state": "Succeeded", "service_key": "e1956383-63b6-4709-8baa-3615bbf5d22b", "service_provider_notes": null, "service_provider_provisioning_state": "NotProvisioned", "stag": 27, "status": "Deleted", "tags": {"a": "b"}, "type": "Microsoft.Network/expressRouteCircuits"}` |

### Authors

- Praveen Ghuge (@praveenghuge)
- Karl Dasan (@ikarldasan)
- Sakar Mehra (@sakar97)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/azure/issues)
[Homepage](https://azure.microsoft.com)
[Repository (Sources)](https://github.com/ansible-collections/azure)
