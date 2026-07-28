---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_sqlmanagedinstance module – Manage SQL managed instances"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_sqlmanagedinstance_module.html
fetched_at: 2026-07-28T01:14:53+00:00
---
# azure.azcollection.azure_rm_sqlmanagedinstance module – Manage SQL managed instances

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
> see [Requirements](azure_rm_sqlmanagedinstance_module.md#ansible-collections-azure-azcollection-azure-rm-sqlmanagedinstance-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_sqlmanagedinstance`.

New in azure.azcollection 1.14.0

- [Synopsis](azure_rm_sqlmanagedinstance_module.md#synopsis)
- [Requirements](azure_rm_sqlmanagedinstance_module.md#requirements)
- [Parameters](azure_rm_sqlmanagedinstance_module.md#parameters)
- [Notes](azure_rm_sqlmanagedinstance_module.md#notes)
- [See Also](azure_rm_sqlmanagedinstance_module.md#see-also)
- [Examples](azure_rm_sqlmanagedinstance_module.md#examples)
- [Return Values](azure_rm_sqlmanagedinstance_module.md#return-values)

## [Synopsis](azure_rm_sqlmanagedinstance_module.md#id1)

- Create, update, or delete SQL managed instances.

## [Requirements](azure_rm_sqlmanagedinstance_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_sqlmanagedinstance_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **administrator_login**  string | Administrator username for the managed instance.  Can only be specified when the managed instance is being created (and is required for creation). |
| **administrator_login_password**  string | The administrator login password (required for managed instance creation). |
| **administrators**  string | The Azure Active Directory administrator of the server. |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  **Choices:**   - `false` - `true` ← (default) |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **collation**  string | Collation of the managed instance. |
| **dns_zone**  string | The Dns Zone that the managed instance is in. |
| **dns_zone_partner**  string | The resource ID of another managed instance whose DNS zone this managed instance will share after creation. |
| **identity**  dictionary | Azure Active Directory identity configuration for a resource. |
| **principal_id**  string | The Azure Active Directory principal ID. |
| **tenant_id**  string | The Azure Active Directory tenant id. |
| **type**  string | The identity type.  Set this to `SystemAssigned` in order to automatically create and assign an Azure Active Directory principal for the resource. |
| **user_assigned_identities**  string | The resource ids of the user assigned identities to use. |
| **instance_pool_id**  string | The ID of the instance pool this managed server belongs to. |
| **key_id**  string | A CMK URI of the key to use for encryption. |
| **license_type**  string | The license type.  Possible values are `LicenseIncluded` and `BasePrice`.  Discounted AHB price for bringing your own SQL licenses.  Regular price inclusive of a new SQL license.  **Choices:**   - `"LicenseIncluded"` - `"BasePrice"` |
| **location**  string | The location of the sql managed instance. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **maintenance_configuration_id**  string | Specifies maintenance configuration ID to apply to this managed instance. |
| **managed_instance_create_mode**  string | Specifies the mode of database creation. |
| **minimal_tls_version**  string | Minimal TLS version. Allowed values `None`, `1.0`, `1.1`, `1.2`.  **Choices:**   - `"None"` - `"1.0"` - `"1.1"` - `"1.2"` |
| **name**  string / required | The name of the sql managed instance. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **primary_user_assigned_identity_id**  string | The resource id of a user assigned identity to be used by default. |
| **private_endpoint_connections**  list / elements=string | List of private endpoint connections on a managed instance. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **proxy_override**  string | Connection type used for connecting to the instance.  **Choices:**   - `"Proxy"` - `"Redirect"` - `"Default"` |
| **public_data_endpoint_enabled**  boolean | Whether or not the public data endpoint is enabled.  **Choices:**   - `false` - `true` |
| **resource_group**  string / required | The name of the resource group. |
| **restore_point_in_time**  string | Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **sku**  dictionary | An ARM Resource SKU. |
| **capacity**  string | The capacity of the managed instance in integer number of vcores. |
| **family**  string | If the service has different generations of hardware, for the same SKU, then that can be captured here. |
| **name**  string | The name of the SKU, typically, a letter add Number code. |
| **size**  string | Size of the particular SKU. |
| **tier**  string | The tier or edition of the particular SKU. |
| **source_managed_instance_id**  string | The resource identifier of the source managed instance associated with create operation of this instance. |
| **state**  string | State of the sql managed instance.  Use `present` to create or update a automation runbook and use `absent` to delete.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **storage_account_type**  string | The storage account type used to store backups for this instance. |
| **storage_size_in_gb**  integer | Storage size in GB.  Minimum value is `32`. Maximum value is `8192`.  Increments of 32 GB allowed only. |
| **subnet_id**  string | Subnet resource ID for the managed instance. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **timezone_id**  string | ID of the timezone.  Allowed values are timezones supported by Windows.  Windows keeps details on supported timezones. |
| **v_cores**  integer | The number of vCores.  **Choices:**   - `8` - `16` - `24` - `32` - `40` - `64` - `80` |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |
| **zone_redundant**  boolean | Whether or not the multi-az is enabled.  **Choices:**   - `false` - `true` |

## [Notes](azure_rm_sqlmanagedinstance_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_sqlmanagedinstance_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_sqlmanagedinstance_module.md#id6)

```yaml+jinja
- name: Create sql managed instance
  azure_rm_sqlmanagedinstance:
    resource_group: "{{ resource_group }}"
    name: testmanagedinstance
    subnet_id: subnet_id
    sku:
      name: GP_Gen5
      tier: GeneralPurpose
      family: Gen5
      capacity: 5
    identity:
      type: SystemAssigned
    administrator_login: azureuser
    administrator_login_password: Ft@password0329test
    storage_size_in_gb: 256
    v_cores: 8

- name: Delete sql managed instance
  azure_rm_sqlmanagedinstance:
    resource_group: "{{ resource_group }}"
    name: testmanagedinstance
    state: absent
```

## [Return Values](azure_rm_sqlmanagedinstance_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **sql_managed_instance**  complex | A list of dictionaries containing facts for SQL Managed Instance.  **Returned:** always |
| **administrator_login**  string | Administrator username for the managed instance.  **Returned:** always  **Sample:** `"azureuser"` |
| **administrators**  string | The Azure Active Directory administrator of the server.  **Returned:** always |
| **collation**  string | The collation of the SQL managed instance.  **Returned:** always  **Sample:** `"SQL_Latin1_General_CP1_CI_AS"` |
| **dns_zone**  string | -The Dns Zone that the managed instance is in.  **Returned:** always  **Sample:** `"8a23abba54cd"` |
| **dns_zone_partner**  string | The resource ID of another managed instance whose DNS zone this managed instance will share after creation.  **Returned:** always |
| **fully_qualified_domain_name**  string | The fully qualified domain name of the managed instance.  **Returned:** always  **Sample:** `"fredsqlinstance.8a23abba54cd.database.windows.net"` |
| **id**  string | Resource ID.  **Returned:** always  **Sample:** `"/subscription/xxx-xxx/resourceGroups/testRG/providers/Microsoft.Sql/managedInstances/fredsqlinstance"` |
| **identity**  complex | Azure Active Directory identity configuration for a resource.  **Returned:** always |
| **principal_id**  string | The Azure Active Directory principal ID.  **Returned:** always  **Sample:** `"895c-xxx-xxxbe"` |
| **tenant_id**  string | The Azure Active Directory tenant ID.  **Returned:** always  **Sample:** `"72fxxxxx-xxxx-xxxx-xxxx-xxxxxx11db47"` |
| **type**  string | The identity type.  **Returned:** always  **Sample:** `"SystemAssigned"` |
| **user_assigned_identities**  string | The resource ids of the user assigned identities to use.  **Returned:** always |
| **instance_pool_id**  string | The ID of the instance pool this managed server belongs to.  **Returned:** always |
| **key_id**  string | A CMK URI of the key to use for encryption.  **Returned:** always |
| **license_type**  string | The license type.  **Returned:** always  **Sample:** `"LicenseIncluded"` |
| **location**  string | Resource location.  **Returned:** always  **Sample:** `"eastus"` |
| **maintenance_configuration_id**  string | Specifies maintenance configuration ID to apply to this managed instance.  **Returned:** always  **Sample:** `"/subscriptions/xxx-xxxx/providers/Microsoft.Maintenance/publicMaintenanceConfigurations/SQL_Default"` |
| **managed_instance_create_mode**  string | Specifies the mode of database creation.  **Returned:** always |
| **minimal_tls_version**  string | Minimal TLS version. Allowed values ‘None’, ‘1.0’, ‘1.1’, ‘1.2’.  **Returned:** always  **Sample:** `"1.2"` |
| **name**  string | SQL manged instance name.  **Returned:** always  **Sample:** `"testmanagedinstance"` |
| **primary_user_assigned_identity_id**  string | The resource id of a user assigned identity to be used by default.  **Returned:** always |
| **private_endpoint_connections**  list / elements=string | List of private endpoint connections on a managed instance.  **Returned:** always  **Sample:** `[]` |
| **provisioning_state**  string | The Status of the SQL managed instance.  **Returned:** always  **Sample:** `"Successed"` |
| **proxy_override**  string | Connection type used for connecting to the instance.  **Returned:** always  **Sample:** `"Proxy"` |
| **public_data_endpoint_enabled**  boolean | Whether or not the public data endpoint is enabled.  **Returned:** always  **Sample:** `false` |
| **restore_point_in_time**  string | Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database.  **Returned:** always |
| **sku**  complex | An ARM Resource SKU.  **Returned:** always |
| **capacity**  integer | The SKU capacity.  **Returned:** always  **Sample:** `2` |
| **family**  string | If the service has different generations of hardware, for the same SKU, then that can be captured here.  **Returned:** always  **Sample:** `"Gen5"` |
| **name**  string | The name of the SKU.  **Returned:** always  **Sample:** `"BC_Gen4_2"` |
| **size**  string | Size of the particular SKU.  **Returned:** always |
| **tier**  string | The SKU tier.  **Returned:** always  **Sample:** `"BusinessCritical"` |
| **source_managed_instance_id**  string | The resource identifier of the source managed instance associated with create operation of this instance.  **Returned:** always |
| **state**  string | The state of the managed instance.  **Returned:** always  **Sample:** `"Ready"` |
| **storage_account_type**  string | The storage account type used to store backups for this instance.  **Returned:** always  **Sample:** `"GRS"` |
| **storage_size_in_gb**  integer | Storage size in GB. Minimum value 32. Maximum value 8192.  **Returned:** always  **Sample:** `256` |
| **subnet_id**  string | Subnet resource ID for the managed instance.  **Returned:** always  **Sample:** `"/subscriptions/xxx-xxxx/resourceGroups/testRG/providers/Microsoft.Network/virtualNetworks/vnet-smi/subnets/sqi_sub"` |
| **tags**  dictionary | Resource tags.  **Returned:** always  **Sample:** `{"taga": "aaa", "tagb": "bbb"}` |
| **timezone_id**  string | Id of the timezone. Allowed values are timezones supported by Windows.  **Returned:** always  **Sample:** `"UTC"` |
| **type**  string | The SQL managed instance type.  **Returned:** always  **Sample:** `"Microsoft.Sql/managedInstances"` |
| **v_cores**  integer | The number of vCores. Allowed values 8, 16, 24, 32, 40, 64, 80.  **Returned:** always  **Sample:** `8` |
| **zone_redundant**  boolean | Whether or not the multi-az is enabled.  **Returned:** always  **Sample:** `false` |

### Authors

- xuzhang3 (@xuzhang3)
- Fred Sun (@Fred-sun)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
