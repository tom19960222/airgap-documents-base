---
collection: ansible
version: "6"
title: "community.azure.azure_rm_dnsrecordset_info module – Get DNS Record Set facts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/azure/azure_rm_dnsrecordset_info_module.html
fetched_at: 2026-07-27T17:05:32+00:00
---
# community.azure.azure_rm_dnsrecordset_info module – Get DNS Record Set facts

> **Note:**
>
> This module is part of the [community.azure collection](https://galaxy.ansible.com/community/azure) (version 1.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.azure`.
> You need further requirements to be able to use this module,
> see [Requirements](azure_rm_dnsrecordset_info_module.md#ansible-collections-community-azure-azure-rm-dnsrecordset-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.azure.azure_rm_dnsrecordset_info`.

- [DEPRECATED](azure_rm_dnsrecordset_info_module.md#deprecated)
- [Synopsis](azure_rm_dnsrecordset_info_module.md#synopsis)
- [Requirements](azure_rm_dnsrecordset_info_module.md#requirements)
- [Parameters](azure_rm_dnsrecordset_info_module.md#parameters)
- [Notes](azure_rm_dnsrecordset_info_module.md#notes)
- [See Also](azure_rm_dnsrecordset_info_module.md#see-also)
- [Examples](azure_rm_dnsrecordset_info_module.md#examples)
- [Return Values](azure_rm_dnsrecordset_info_module.md#return-values)
- [Status](azure_rm_dnsrecordset_info_module.md#status)

## [DEPRECATED](azure_rm_dnsrecordset_info_module.md#id1)

Removed in:
:   version 2.0.0

Why:
:   The Ansible collection community.azure is deprecated. Use azure.azcollection instead.

Alternative:
:   Use [azure.azcollection.azure_rm_dnsrecordset_info](../../azure/azcollection/azure_rm_dnsrecordset_info_module.md#ansible-collections-azure-azcollection-azure-rm-dnsrecordset-info-module) instead.

## [Synopsis](azure_rm_dnsrecordset_info_module.md#id2)

- Get facts for a specific DNS Record Set in a Zone, or a specific type in all Zones or in one Zone etc.

## [Requirements](azure_rm_dnsrecordset_info_module.md#id3)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_dnsrecordset_info_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  added in azure.azcollection 0.0.1 | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  added in azure.azcollection 0.0.1 | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  Default: `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  Choices:   - `false` - `true` ← (default) |
| **auth_source**  string  added in azure.azcollection 0.0.1 | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  Choices:   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  added in azure.azcollection 0.0.1 | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  Choices:   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  added in azure.azcollection 0.0.1 | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  Default: `"AzureCloud"` |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **record_type**  string | Limit record sets by record type. |
| **relative_name**  string | Only show results for a Record Set. |
| **resource_group**  string | Limit results by resource group. Required when filtering by name or type. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **top**  integer | Limit the maximum number of record sets to return. |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |
| **zone_name**  string | Limit results by zones. Required when filtering by name or type. |

## [Notes](azure_rm_dnsrecordset_info_module.md#id5)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_dnsrecordset_info_module.md#id6)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_dnsrecordset_info_module.md#id7)

```yaml+jinja
- name: Get facts for one Record Set
  community.azure.azure_rm_dnsrecordset_info:
    resource_group: myResourceGroup
    zone_name: example.com
    relative_name: server10
    record_type: A
- name: Get facts for all Type A Record Sets in a Zone
  community.azure.azure_rm_dnsrecordset_info:
    resource_group: myResourceGroup
    zone_name: example.com
    record_type: A
- name: Get all record sets in one zone
  community.azure.azure_rm_dnsrecordset_info:
    resource_group: myResourceGroup
    zone_name: example.com
```

## [Return Values](azure_rm_dnsrecordset_info_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **azure_dnsrecordset**  list / elements=string | List of record set dicts.  Returned: always  Sample: `[{"etag": "60ac0480-44dd-4881-a2ed-680d20b3978e", "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Network/dnszones/newzone.com/A/servera", "name": "servera", "properties": {"ARecords": [{"ipv4Address": "10.4.5.7"}, {"ipv4Address": "2.4.5.8"}], "TTL": 12900}, "type": "Microsoft.Network/dnszones/A"}]` |
| **dnsrecordsets**  list / elements=string | List of record set dicts, which shares the same hierarchy as community.azure.azure_rm_dnsrecordset module’s parameter.  Returned: always |
| **fqdn**  string | Fully qualified domain name of the record set.  Returned: success  Sample: `"www.newzone.com"` |
| **id**  string | ID of the dns recordset.  Returned: success  Sample: `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Network/dnszones/newzone. com/A/servera"` |
| **provisioning_state**  string | Provision state of the resource.  Returned: success  Sample: `"Successed"` |
| **record_type**  string | The type of the record set.  Can be `A`, `AAAA`, `CNAME`, `MX`, `NS`, `SRV`, `TXT`, `PTR`.  Returned: success  Sample: `"A"` |
| **records**  string | List of records depending on the type of recordset.  Returned: success  Sample: `[{"ipv4Address": "10.4.5.7"}, {"ipv4Address": "2.4.5.8"}]` |
| **relative_name**  string | Name of the dns recordset.  Returned: success  Sample: `"servera"` |
| **time_to_live**  string | Time to live of the record set in seconds.  Returned: success  Sample: `12900` |

## [Status](azure_rm_dnsrecordset_info_module.md#id9)

- This module will be removed in version 2.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](azure_rm_dnsrecordset_info_module.md#deprecated).

### Authors

- Ozi Boms (@ozboms)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.azure/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.azure)
