---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_publicipaddress module – Manage Azure Public IP Addresses"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_publicipaddress_module.html
fetched_at: 2026-07-28T01:14:26+00:00
---
# azure.azcollection.azure_rm_publicipaddress module – Manage Azure Public IP Addresses

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
> see [Requirements](azure_rm_publicipaddress_module.md#ansible-collections-azure-azcollection-azure-rm-publicipaddress-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_publicipaddress`.

New in azure.azcollection 0.1.0

- [Synopsis](azure_rm_publicipaddress_module.md#synopsis)
- [Requirements](azure_rm_publicipaddress_module.md#requirements)
- [Parameters](azure_rm_publicipaddress_module.md#parameters)
- [Notes](azure_rm_publicipaddress_module.md#notes)
- [See Also](azure_rm_publicipaddress_module.md#see-also)
- [Examples](azure_rm_publicipaddress_module.md#examples)
- [Return Values](azure_rm_publicipaddress_module.md#return-values)

## [Synopsis](azure_rm_publicipaddress_module.md#id1)

- Create, update and delete a Public IP address.
- Allows setting and updating the address allocation method and domain name label.
- Use the [azure.azcollection.azure_rm_networkinterface](azure_rm_networkinterface_module.md#ansible-collections-azure-azcollection-azure-rm-networkinterface-module) module to associate a Public IP with a network interface.

## [Requirements](azure_rm_publicipaddress_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_publicipaddress_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **allocation_method**  string | Control whether the assigned Public IP remains permanently assigned to the object.  If not set to `Static`, the IP address may changed anytime an associated virtual machine is power cycled.  **Choices:**   - `"dynamic"` ← (default) - `"static"` - `"Static"` - `"Dynamic"` |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  **Choices:**   - `false` - `true` ← (default) |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **domain_name**  aliases: domain_name_label  string | The customizable portion of the FQDN assigned to public IP address. This is an explicit setting.  If no value is provided, any existing value will be removed on an existing public IP. |
| **idle_timeout**  integer | Idle timeout in minutes. |
| **ip_tags**  list / elements=dictionary | List of IpTag associated with the public IP address.  Each element should contain type:value pair. |
| **type**  string / required | Sets the ip_tags type. |
| **value**  string / required | Sets the ip_tags value. |
| **location**  string | Valid Azure location. Defaults to location of the resource group. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string / required | Name of the Public IP. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **resource_group**  string / required | Name of resource group with which the Public IP is associated. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **sku**  string | The public IP address SKU.  When *version=ipv6*, if *sku=standard* then set *allocation_method=static*.  When *version=ipv4*, if *sku=standard* then set *allocation_method=static*.  **Choices:**   - `"basic"` - `"standard"` - `"Basic"` - `"Standard"` |
| **state**  string | Assert the state of the Public IP. Use `present` to create or update a and `absent` to delete.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **version**  string | The public IP address version.  **Choices:**   - `"ipv4"` ← (default) - `"ipv6"` |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |
| **zones**  list / elements=string | A list of availability zones denoting the IP allocated for the resource needs to come from.  **Choices:**   - `"1"` - `"2"` - `"3"` |

## [Notes](azure_rm_publicipaddress_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_publicipaddress_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_publicipaddress_module.md#id6)

```yaml+jinja
- name: Create a public ip address
  azure_rm_publicipaddress:
    resource_group: myResourceGroup
    name: my_public_ip
    allocation_method: static
    domain_name: foobar

- name: Delete public ip
  azure_rm_publicipaddress:
    resource_group: myResourceGroup
    name: my_public_ip
    state: absent
```

## [Return Values](azure_rm_publicipaddress_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **state**  complex | Facts about the current state of the object.  **Returned:** always |
| **dns_settings**  dictionary | The FQDN of the DNS record associated with the public IP address.  **Returned:** always  **Sample:** `{"domain_name_label": "ansible-b57dc95985712e45eb8b9c2e", "fqdn": "ansible-b57dc95985712e45eb8b9c2e.eastus.cloudapp.azure.com", "reverse_fqdn": null}` |
| **etag**  string | A unique read-only string that changes whenever the resource is updated.  **Returned:** always  **Sample:** `"W/'1905ee13-7623-45b1-bc6b-4a12b2fb9d15'"` |
| **idle_timeout_in_minutes**  integer | The idle timeout of the public IP address.  **Returned:** always  **Sample:** `4` |
| **ip_address**  string | The Public IP Prefix this Public IP Address should be allocated from.  **Returned:** always  **Sample:** `"52.160.103.93"` |
| **location**  string | Resource location.  **Returned:** always  **Sample:** `"eastus"` |
| **name**  string | Name of the Public IP Address.  **Returned:** always  **Sample:** `"publicip002"` |
| **provisioning_state**  string | The provisioning state of the Public IP resource.  **Returned:** always  **Sample:** `"Succeeded"` |
| **public_ip_address_version**  string | The public IP address version.  **Returned:** always  **Sample:** `"ipv4"` |
| **public_ip_allocation_method**  string | The public IP allocation method.  **Returned:** always  **Sample:** `"static"` |
| **sku**  string | The public IP address SKU.  **Returned:** always  **Sample:** `"Basic"` |
| **tags**  dictionary | The resource tags.  **Returned:** always  **Sample:** `{"delete": "on-exit", "testing": "testing"}` |
| **type**  string | Type of the resource.  **Returned:** always  **Sample:** `"Microsoft.Network/publicIPAddresses"` |
| **zones**  list / elements=string | A list of availability zones denoting the IP allocated for the resource needs to come from.  **Returned:** always  **Sample:** `["1", "2"]` |

### Authors

- Chris Houseknecht (@chouseknecht)
- Matt Davis (@nitzmahone)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
