---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_publicipaddress_info module – Get public IP facts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_publicipaddress_info_module.html
fetched_at: 2026-07-28T01:14:27+00:00
---
# azure.azcollection.azure_rm_publicipaddress_info module – Get public IP facts

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
> see [Requirements](azure_rm_publicipaddress_info_module.md#ansible-collections-azure-azcollection-azure-rm-publicipaddress-info-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_publicipaddress_info`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_publicipaddress_info_module.md#synopsis)
- [Requirements](azure_rm_publicipaddress_info_module.md#requirements)
- [Parameters](azure_rm_publicipaddress_info_module.md#parameters)
- [Notes](azure_rm_publicipaddress_info_module.md#notes)
- [See Also](azure_rm_publicipaddress_info_module.md#see-also)
- [Examples](azure_rm_publicipaddress_info_module.md#examples)
- [Return Values](azure_rm_publicipaddress_info_module.md#return-values)

## [Synopsis](azure_rm_publicipaddress_info_module.md#id1)

- Get facts for a specific public IP or all public IPs within a resource group.

## [Requirements](azure_rm_publicipaddress_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_publicipaddress_info_module.md#id3)

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
| **name**  string | Only show results for a specific Public IP. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **resource_group**  string | Limit results by resource group. Required when using name parameter. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  list / elements=string | Limit results by providing a list of tags. Format tags as ‘key’ or ‘key:value’. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_publicipaddress_info_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_publicipaddress_info_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_publicipaddress_info_module.md#id6)

```yaml+jinja
- name: Get facts for one Public IP
  azure_rm_publicipaddress_info:
    resource_group: myResourceGroup
    name: publicip001

- name: Get facts for all Public IPs within a resource groups
  azure_rm_publicipaddress_info:
    resource_group: myResourceGroup
    tags:
      - key:value
```

## [Return Values](azure_rm_publicipaddress_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **azure_publicipaddresses**  list / elements=string | List of public IP address dicts.  Please note that this option will be deprecated in 2.10 when curated format will become the only supported format.  **Returned:** always  **Sample:** `[{"etag": "W/\"a31a6d7d-cb18-40a5-b16d-9f4a36c1b18a\"", "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup/providers/Microsoft.Network/publicIPAddresses/pip2001", "location": "eastus2", "name": "pip2001", "properties": {"idleTimeoutInMinutes": 4, "provisioningState": "Succeeded", "publicIPAllocationMethod": "Dynamic", "resourceGuid": "29de82f4-a7da-440e-bd3d-9cabb79af95a"}, "type": "Microsoft.Network/publicIPAddresses"}]` |
| **publicipaddresses**  complex | List of publicipaddress.  Contains the detail which matches azure_rm_publicipaddress parameters.  Returned when the format parameter set to curated.  **Returned:** always |
| **allocation_method**  string | The public IP allocation method.  Possible values are `static` and `dynamic`.  **Returned:** always  **Sample:** `"static"` |
| **dns_settings**  dictionary | The FQDN of the DNS record associated with the public IP address.  **Returned:** always  **Sample:** `{"domain_name_label": "ansible-b57dc95985712e45eb8b9c2e", "fqdn": "ansible-b57dc95985712e45eb8b9c2e.eastus.cloudapp.azure.com", "reverse_fqdn": null}` |
| **etag**  string | A unique read-only string that changes whenever the resource is updated.  **Returned:** always  **Sample:** `"W/'1905ee13-7623-45b1-bc6b-4a12b2fb9d15'"` |
| **id**  string | Resource ID.  **Returned:** always  **Sample:** `"/subscriptions/xxx---xxxxx/resourceGroups/v-xisuRG/providers/Microsoft.Network/publicIPAddresses/pipb57dc95224"` |
| **idle_timeout**  integer | The idle timeout of the public IP address.  **Returned:** always  **Sample:** `4` |
| **ip_address**  string | The Public IP Prefix this Public IP Address should be allocated from.  **Returned:** always  **Sample:** `"40.121.144.14"` |
| **ip_tags**  list / elements=string | The list of tags associated with the public IP address.  **Returned:** always  **Sample:** `[{"type": "FirstPartyUsage", "value": "Storage"}]` |
| **location**  string | Resource location.  **Returned:** always  **Sample:** `"eastus"` |
| **name**  string | Name of the public IP address.  **Returned:** always  **Sample:** `"pipb57dc95224"` |
| **provisioning_state**  string | The provisioning state of the PublicIP resource.  Possible values is `Succeeded`.  **Returned:** always  **Sample:** `"Succeeded"` |
| **sku**  string | The public IP address SKU.  **Returned:** always  **Sample:** `"Basic"` |
| **tags**  dictionary | Resource tags.  **Returned:** always  **Sample:** `{"delete": "on-exit", "testing": "testing"}` |
| **type**  string | Resource type.  **Returned:** always  **Sample:** `"Microsoft.Network/publicIPAddresses"` |
| **version**  string | The public IP address version.  Possible values are `ipv4` and `ipv6`.  **Returned:** always  **Sample:** `"ipv4"` |
| **zones**  list / elements=string | A list of availability zones denoting the IP allocated for the resource needs to come from.  **Returned:** always  **Sample:** `["1", "2"]` |

### Authors

- Chris Houseknecht (@chouseknecht)
- Matt Davis (@nitzmahone)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
