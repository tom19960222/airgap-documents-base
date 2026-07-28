---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_rediscache module – Manage Azure Cache for Redis instance"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_rediscache_module.html
fetched_at: 2026-07-28T01:14:29+00:00
---
# azure.azcollection.azure_rm_rediscache module – Manage Azure Cache for Redis instance

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
> see [Requirements](azure_rm_rediscache_module.md#ansible-collections-azure-azcollection-azure-rm-rediscache-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_rediscache`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_rediscache_module.md#synopsis)
- [Requirements](azure_rm_rediscache_module.md#requirements)
- [Parameters](azure_rm_rediscache_module.md#parameters)
- [Notes](azure_rm_rediscache_module.md#notes)
- [See Also](azure_rm_rediscache_module.md#see-also)
- [Examples](azure_rm_rediscache_module.md#examples)
- [Return Values](azure_rm_rediscache_module.md#return-values)

## [Synopsis](azure_rm_rediscache_module.md#id1)

- Create, update and delete instance of Azure Cache for Redis.

## [Requirements](azure_rm_rediscache_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_rediscache_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  **Choices:**   - `false` - `true` ← (default) |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **enable_non_ssl_port**  boolean | When set *enable_non_ssl_port=true*, the non-ssl Redis server port 6379 will be enabled.  **Choices:**   - `false` ← (default) - `true` |
| **location**  string | Resource location. If not set, location from the resource group will be used as default. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **maxfragmentationmemory_reserved**  integer | Configures the amount of memory in MB that is reserved to accommodate for memory fragmentation.  Please see <https://docs.microsoft.com/en-us/azure/redis-cache/cache-configure#advanced-settings> for more detail. |
| **maxmemory_policy**  string | Configures the eviction policy of the cache.  Please see <https://docs.microsoft.com/en-us/azure/redis-cache/cache-configure#advanced-settings> for more detail.  **Choices:**   - `"volatile_lru"` - `"allkeys_lru"` - `"volatile_random"` - `"allkeys_random"` - `"volatile_ttl"` - `"noeviction"` |
| **maxmemory_reserved**  integer | Configures the amount of memory in MB that is reserved for non-cache operations.  Please see <https://docs.microsoft.com/en-us/azure/redis-cache/cache-configure#advanced-settings> for more detail. |
| **minimum_tls_version**  string  *added in azure.azcollection 1.10.0* | Require clients to use a specified TLS version.  **Choices:**   - `"1.0"` - `"1.1"` - `"1.2"` |
| **name**  string / required | Unique name of the Azure Cache for Redis to create or update. |
| **notify_keyspace_events**  string | Allows clients to receive notifications when certain events occur.  Please see <https://docs.microsoft.com/en-us/azure/redis-cache/cache-configure#advanced-settings> for more detail. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **public_network_access**  string  *added in azure.azcollection 1.10.0* | Whether or not public endpoint access is allowed for this cache.  **Choices:**   - `"Enabled"` ← (default) - `"Disabled"` |
| **reboot**  dictionary | Reboot specified Redis node(s). There can be potential data loss. |
| **reboot_type**  string | Which Redis node(s) to reboot.  **Choices:**   - `"primary"` - `"secondary"` - `"all"` |
| **shard_id**  string | If clustering is enabled, the id of the shard to be rebooted. |
| **redis_version**  string  *added in azure.azcollection 1.10.0* | The major version of Redis.  **Choices:**   - `"4"` - `"6"` ← (default) |
| **regenerate_key**  dictionary | Regenerate Redis cache’s access keys. |
| **key_type**  string | The Redis key to regenerate.  **Choices:**   - `"primary"` - `"secondary"` |
| **resource_group**  string / required | Name of the resource group to which the resource belongs. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **shard_count**  integer | The number of shards to be created when *sku=premium*. |
| **sku**  dictionary / required | SKU info of Azure Cache for Redis. |
| **name**  string / required | Type of Azure Cache for Redis to deploy.  **Choices:**   - `"basic"` - `"standard"` - `"premium"` |
| **size**  string / required | Size of Azure Cache for Redis to deploy.  When *sku=basic* or *sku=standard*, allowed values are `C0`, `C1`, `C2`, `C3`, `C4`, `C5`, `C6`.  When *sku=premium*, allowed values are `P1`, `P2`, `P3`, `P4`.  Please see <https://docs.microsoft.com/en-us/rest/api/redis/redis/create#sku> for allowed values.  **Choices:**   - `"C0"` - `"C1"` - `"C2"` - `"C3"` - `"C4"` - `"C5"` - `"C6"` - `"P1"` - `"P2"` - `"P3"` - `"P4"` |
| **state**  string | Assert the state of the Azure Cache for Redis.  Use `present` to create or update an Azure Cache for Redis and `absent` to delete it.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **static_ip**  string | Static IP address. Required when deploying an Azure Cache for Redis inside an existing Azure virtual network. |
| **subnet**  any | Subnet in a virtual network to deploy the Azure Cache for Redis in.  It can be resource id of subnet, for example /subscriptions/{subid}/resourceGroups/{resourceGroupName}/Microsoft.{Network|ClassicNetwork}/VirtualNetworks/vnet1/subnets/subnet1.  It can be a dictionary where contains *name*, *virtual_network_name* and *resource_group*.  *name*. Name of the subnet.  *resource_group*. Resource group name of the subnet.  *virtual_network_name*. Name of virtual network to which this subnet belongs. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **tenant_settings**  dictionary | Dict of tenant settings. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **wait_for_provisioning**  boolean | Wait till the Azure Cache for Redis instance provisioning_state is Succeeded.  It takes several minutes for Azure Cache for Redis to be provisioned ready for use after creating/updating/rebooting.  Set this option to `true` to wait for provisioning_state. Set to `false` if you don’t care about provisioning_state.  Poll wait timeout is 60 minutes.  **Choices:**   - `false` - `true` ← (default) |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_rediscache_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_rediscache_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_rediscache_module.md#id6)

```yaml+jinja
- name: Create an Azure Cache for Redis
  azure_rm_rediscache:
    resource_group: myResourceGroup
    name: myRedis
    sku:
      name: basic
      size: C1

- name: Scale up the Azure Cache for Redis
  azure_rm_rediscache:
    resource_group: myResourceGroup
    name: myRedis
    sku:
      name: standard
      size: C1
    tags:
      testing: foo

- name: Force reboot the redis cache
  azure_rm_rediscache:
    resource_group: myResourceGroup
    name: myRedisCache
    reboot:
      reboot_type: all

- name: Create Azure Cache for Redis with subnet
  azure_rm_rediscache:
    resource_group: myResourceGroup
    name: myRedis
    sku:
      name: premium
      size: P1
    subnet: "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/myVirt
                ualNetwork/subnets/mySubnet"

- name: Regenerate primary Redis key
  azure_rm_rediscache:
    resource_group: myResourceGroup
    name: myRedis
    regenerate_key:
      key_type: primary
```

## [Return Values](azure_rm_rediscache_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **host_name**  string | Host name of the Azure Cache for Redis.  **Returned:** when *state=present*  **Sample:** `"myredis.redis.cache.windows.net"` |
| **id**  string | Id of the Azure Cache for Redis.  **Returned:** always  **Sample:** `"/subscriptions/xxxxxxxx-xxxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Cache/Redis/myRedis"` |

### Authors

- Yunge Zhu(@yungezz)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
