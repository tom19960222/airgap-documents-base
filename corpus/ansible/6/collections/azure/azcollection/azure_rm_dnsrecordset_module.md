---
collection: ansible
version: "6"
title: "azure.azcollection.azure_rm_dnsrecordset module – Create, delete and update DNS record sets and records"
source_url: https://docs.ansible.com/projects/ansible/6/collections/azure/azcollection/azure_rm_dnsrecordset_module.html
fetched_at: 2026-07-27T16:46:15+00:00
---
# azure.azcollection.azure_rm_dnsrecordset module – Create, delete and update DNS record sets and records

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
> see [Requirements](azure_rm_dnsrecordset_module.md#ansible-collections-azure-azcollection-azure-rm-dnsrecordset-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_dnsrecordset`.

New in azure.azcollection 0.1.0

- [Synopsis](azure_rm_dnsrecordset_module.md#synopsis)
- [Requirements](azure_rm_dnsrecordset_module.md#requirements)
- [Parameters](azure_rm_dnsrecordset_module.md#parameters)
- [Notes](azure_rm_dnsrecordset_module.md#notes)
- [See Also](azure_rm_dnsrecordset_module.md#see-also)
- [Examples](azure_rm_dnsrecordset_module.md#examples)
- [Return Values](azure_rm_dnsrecordset_module.md#return-values)

## [Synopsis](azure_rm_dnsrecordset_module.md#id1)

- Creates, deletes, and updates DNS records sets and records within an existing Azure DNS Zone.

## [Requirements](azure_rm_dnsrecordset_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_dnsrecordset_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  added in azure.azcollection 0.0.1 | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  added in azure.azcollection 0.0.1 | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  Default: `"latest"` |
| **append_metadata**  boolean | Whether metadata should be appended or not  Choices:   - `false` - `true` ← (default) |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  Choices:   - `false` - `true` ← (default) |
| **auth_source**  string  added in azure.azcollection 0.0.1 | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  Choices:   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  added in azure.azcollection 0.0.1 | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  Choices:   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  added in azure.azcollection 0.0.1 | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  Default: `"AzureCloud"` |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **metadata**  dictionary | The metadata tags for the record sets. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **record_mode**  string | Whether existing record values not sent to the module should be purged.  Choices:   - `"append"` - `"purge"` ← (default) |
| **record_type**  string / required | The type of record set to create or delete.  Choices:   - `"A"` - `"AAAA"` - `"CNAME"` - `"MX"` - `"NS"` - `"SRV"` - `"TXT"` - `"PTR"` - `"CAA"` - `"SOA"` |
| **records**  list / elements=dictionary | List of records to be created depending on the type of record (set). |
| **entry**  string | Primary data value for all record types. |
| **port**  string | Used for creating an `SRV` record set/records. |
| **preference**  string | Used for creating an `MX` record set/records. |
| **priority**  string | Used for creating an `SRV` record set/records. |
| **weight**  string | Used for creating an `SRV` record set/records. |
| **relative_name**  string / required | Relative name of the record set. |
| **resource_group**  string / required | Name of resource group. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **state**  string | Assert the state of the record set. Use `present` to create or update and `absent` to delete.  Choices:   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **time_to_live**  integer | Time to live of the record set in seconds.  Default: `3600` |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |
| **zone_name**  string / required | Name of the existing DNS zone in which to manage the record set. |

## [Notes](azure_rm_dnsrecordset_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_dnsrecordset_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_dnsrecordset_module.md#id6)

```yaml+jinja
- name: ensure an "A" record set with multiple records
  azure_rm_dnsrecordset:
    resource_group: myResourceGroup
    relative_name: www
    zone_name: testing.com
    record_type: A
    records:
      - entry: 192.168.100.101
      - entry: 192.168.100.102
      - entry: 192.168.100.103

- name: delete a record set
  azure_rm_dnsrecordset:
    resource_group: myResourceGroup
    record_type: A
    relative_name: www
    zone_name: testing.com
    state: absent

- name: create A record set with metadata information
  azure_rm_dnsrecordset:
    resource_group: myResourceGroup
    relative_name: www
    zone_name: zone1.com
    record_type: A
    records:
      - entry: 192.168.100.104
    metadata:
      key1: "value1"

- name: create multiple "A" record sets with multiple records
  azure_rm_dnsrecordset:
    resource_group: myResourceGroup
    zone_name: testing.com
    relative_name: "{{ item.name }}"
    record_type: "{{ item.type }}"
    records: "{{ item.records }}"
  with_items:
    - { name: 'servera', type: 'A', records: [ { entry: '10.10.10.20' }, { entry: '10.10.10.21' }] }
    - { name: 'serverb', type: 'A', records: [ { entry: '10.10.10.30' }, { entry: '10.10.10.41' }] }
    - { name: 'serverc', type: 'A', records: [ { entry: '10.10.10.40' }, { entry: '10.10.10.41' }] }

- name: create SRV records in a new record set
  azure_rm_dnsrecordset:
    resource_group: myResourceGroup
    relative_name: _sip._tcp.testing.com
    zone_name: testing.com
    time_to_live: 7200
    record_type: SRV
    records:
    - entry: sip.testing.com
      preference: 10
      priority: 20
      weight: 10
      port: 5060

- name: create PTR record in a new record set
  azure_rm_dnsrecordset:
    resource_group: myResourceGroup
    relative_name: 192.168.100.101.in-addr.arpa
    zone_name: testing.com
    record_type: PTR
    records:
    - entry: servera.testing.com

- name: create TXT record in a new record set
  azure_rm_dnsrecordset:
    resource_group: myResourceGroup
    relative_name: mail.testing.com
    zone_name: testing.com
    record_type: TXT
    records:
    - entry: 'v=spf1 a -all'
```

## [Return Values](azure_rm_dnsrecordset_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **state**  complex | Current state of the DNS record set.  Returned: always |
| **arecords**  list / elements=string | A list of records in the record set.  Returned: always  Sample: `[{"ipv4_address": "192.0.2.2"}, {"ipv4_address": "192.0.2.4"}, {"ipv4_address": "192.0.2.8"}]` |
| **etag**  string | The etag of the record set.  Returned: always  Sample: `"692c3e92-a618-46fc-aecd-8f888807cd6c"` |
| **fqdn**  string | Fully qualified domain name of the record set.  Returned: always  Sample: `"www.b57dc95985712e4523282.com"` |
| **id**  string | The DNS record set ID.  Returned: always  Sample: `"/subscriptions/xxxx......xxx/resourceGroups/v-xisuRG/providers/Microsoft.Network/dnszones/b57dc95985712e4523282.com/A/www"` |
| **name**  string | Relate name of the record set.  Returned: always  Sample: `"www"` |
| **provisioning_state**  string | The DNS record set state.  Returned: always  Sample: `"Succeeded"` |
| **target_resource**  dictionary | The target resource of the record set.  Returned: always  Sample: `{}` |
| **ttl**  integer | The TTL(time-to-live) of the records in the records set.  Returned: always  Sample: `3600` |
| **type**  string | The type of DNS record in this record set.  Returned: always  Sample: `"A"` |

### Authors

- Obezimnaka Boms (@ozboms)
- Matt Davis (@nitzmahone)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/azure/issues)
[Homepage](https://azure.microsoft.com)
[Repository (Sources)](https://github.com/ansible-collections/azure)
