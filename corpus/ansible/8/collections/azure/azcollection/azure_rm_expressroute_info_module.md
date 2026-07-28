---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_expressroute_info module – Get Azure Express Route"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_expressroute_info_module.html
fetched_at: 2026-07-28T01:13:19+00:00
---
# azure.azcollection.azure_rm_expressroute_info module – Get Azure Express Route

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
> see [Requirements](azure_rm_expressroute_info_module.md#ansible-collections-azure-azcollection-azure-rm-expressroute-info-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_expressroute_info`.

New in azure.azcollection 1.7.0

- [Synopsis](azure_rm_expressroute_info_module.md#synopsis)
- [Requirements](azure_rm_expressroute_info_module.md#requirements)
- [Parameters](azure_rm_expressroute_info_module.md#parameters)
- [Notes](azure_rm_expressroute_info_module.md#notes)
- [See Also](azure_rm_expressroute_info_module.md#see-also)
- [Examples](azure_rm_expressroute_info_module.md#examples)
- [Return Values](azure_rm_expressroute_info_module.md#return-values)

## [Synopsis](azure_rm_expressroute_info_module.md#id1)

- Get facts of Azure Express Route.

## [Requirements](azure_rm_expressroute_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_expressroute_info_module.md#id3)

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
| **name**  string | The name of the express route. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **resource_group**  string / required | The name of the resource group. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  list / elements=string | Limit results by providing a list of tags. Format tags as ‘key’ or ‘key:value’. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_expressroute_info_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_expressroute_info_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_expressroute_info_module.md#id6)

```yaml+jinja
- name: Get facts of specific expressroute
  community.azure.azure_rm_expressroute_info:
    resource_group: myResourceGroup
    name: myExpressRoute
    tags:
      - key:value
```

## [Return Values](azure_rm_expressroute_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **state**  dictionary | Current state of the express route.  **Returned:** always  **Sample:** `{"additional_properties": {}, "allow_classic_operations": true, "authorizations": [{"authorization_key": "d83e18b5-0200-4e0b-9cdb-6fdf95b00267", "authorization_use_status": "Available", "etag": "W/'09572845-c667-410c-b664-ed8e39242c13'", "id": "/subscriptions/subs_id/resourceGroups/rg/providers/Microsoft.Network/expressRouteCircuits/exp/authorizations/az", "name": "authorization_test", "provisioning_state": "Succeeded", "type": "Microsoft.Network/expressRouteCircuits/authorizations"}], "bandwidth_in_gbps": null, "circuit_provisioning_state": "Enabled", "express_route_port": null, "gateway_manager_etag": "", "global_reach_enabled": false, "id": "/subscriptions/subs_id/resourceGroups/rg/providers/Microsoft.Network/expressRouteCircuits/exp", "location": "eastus", "name": "exp", "peerings": [], "provisioning_state": "Succeeded", "service_key": "e1956383-63b6-4709-8baa-3615bbf5d22b", "service_provider_notes": null, "service_provider_provisioning_state": "NotProvisioned", "stag": 27, "status": "Deleted", "tags": {"a": "b"}, "type": "Microsoft.Network/expressRouteCircuits"}` |

### Authors

- Praveen Ghuge (@praveenghuge)
- Karl Dasan (@ikarldasan)
- Sakar Mehra (@sakar97)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
