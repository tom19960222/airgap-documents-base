---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_datalakestore_info module – Get Azure Data Lake Store info"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_datalakestore_info_module.html
fetched_at: 2026-07-28T01:12:56+00:00
---
# azure.azcollection.azure_rm_datalakestore_info module – Get Azure Data Lake Store info

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
> see [Requirements](azure_rm_datalakestore_info_module.md#ansible-collections-azure-azcollection-azure-rm-datalakestore-info-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_datalakestore_info`.

New in azure.azcollection 1.4.0

- [Synopsis](azure_rm_datalakestore_info_module.md#synopsis)
- [Requirements](azure_rm_datalakestore_info_module.md#requirements)
- [Parameters](azure_rm_datalakestore_info_module.md#parameters)
- [Notes](azure_rm_datalakestore_info_module.md#notes)
- [See Also](azure_rm_datalakestore_info_module.md#see-also)
- [Examples](azure_rm_datalakestore_info_module.md#examples)
- [Return Values](azure_rm_datalakestore_info_module.md#return-values)

## [Synopsis](azure_rm_datalakestore_info_module.md#id1)

- Get Azure Data Lake Store info.

## [Requirements](azure_rm_datalakestore_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_datalakestore_info_module.md#id3)

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
| **name**  string | The name of the Data Lake Store account. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **resource_group**  aliases: resource_group_name  string | The name of the Azure resource group. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_datalakestore_info_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_datalakestore_info_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_datalakestore_info_module.md#id6)

```yaml+jinja
- name: Get Azure Data Lake Store info from resource group 'myResourceGroup' and name 'myDataLakeStore'
  azure_rm_datalakestore_info:
    resource_group: myResourceGroup
    name: myDataLakeStore

- name: Get Azure Data Lake Store info from resource group 'myResourceGroup'
  azure_rm_datalakestore_info:
    resource_group: myResourceGroup

- name: Get Azure Data Lake Store info
  azure_rm_datalakestore_info:
```

## [Return Values](azure_rm_datalakestore_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **datalake**  complex | A list of dictionaries containing facts for Azure Data Lake Store.  **Returned:** always |
| **account_id**  string | The unique identifier associated with this Data Lake Store account.  **Returned:** always  **Sample:** `"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"` |
| **creation_time**  string | The account creation time.  **Returned:** always  **Sample:** `"2020-01-01T00:00:00.000000+00:00"` |
| **current_tier**  string | The commitment tier in use for the current month.  **Returned:** success  **Sample:** `"Consumption"` |
| **default_group**  string | The default owner group for all new folders and files created in the Data Lake Store account.  **Returned:** success |
| **encryption_config**  complex | The Key Vault encryption configuration.  **Returned:** success |
| **key_vault_meta_info**  complex | The Key Vault information for connecting to user managed encryption keys.  **Returned:** success |
| **encryption_key_name**  string | The name of the user managed encryption key.  **Returned:** always  **Sample:** `"KeyName"` |
| **encryption_key_version**  string | The version of the user managed encryption key.  **Returned:** always  **Sample:** `"86a1e3b7406f45afa0d54e21eff47e39"` |
| **key_vault_resource_id**  string | The resource identifier for the user managed Key Vault being used to encrypt.  **Returned:** always  **Sample:** `"/subscriptions/{subscriptionId}/resourceGroups/myRG/providers/Microsoft.KeyVault/vaults/testkv"` |
| **type**  string | The type of encryption configuration being used.  **Returned:** always  **Sample:** `"ServiceManaged"` |
| **encryption_provisioning_state**  string | The current state of encryption provisioning for this Data Lake Store account.  **Returned:** success  **Sample:** `"Succeeded"` |
| **encryption_state**  string | The current state of encryption for this Data Lake Store account.  **Returned:** success  **Sample:** `"Enabled"` |
| **endpoint**  string | The full CName endpoint for this account.  **Returned:** always  **Sample:** `"testaccount.azuredatalakestore.net"` |
| **firewall_allow_azure_ips**  string | The current state of allowing or disallowing IPs originating within Azure through the firewall.  **Returned:** success  **Sample:** `"Disabled"` |
| **firewall_rules**  list / elements=string | The list of firewall rules associated with this Data Lake Store account.  **Returned:** success |
| **end_ip_address**  string | The end IP address for the firewall rule.  This can be either ipv4 or ipv6.  Start and End should be in the same protocol.  **Returned:** always  **Sample:** `"192.168.1.254"` |
| **name**  string | The resource name.  **Returned:** always  **Sample:** `"Example Name"` |
| **start_ip_address**  string | The start IP address for the firewall rule.  This can be either ipv4 or ipv6.  Start and End should be in the same protocol.  **Returned:** always  **Sample:** `"192.168.1.1"` |
| **firewall_state**  string | The current state of the IP address firewall for this Data Lake Store account.  **Returned:** success  **Sample:** `"Enabled"` |
| **id**  string | The resource identifier.  **Returned:** always  **Sample:** `"/subscriptions/{subscriptionId}/resourceGroups/myResourceGroup/providers/Microsoft.DataLakeStore/accounts/testaccount"` |
| **identity**  complex | The Key Vault encryption identity, if any.  **Returned:** success |
| **principal_id**  string | The principal identifier associated with the encryption.  **Returned:** success  **Sample:** `"00000000-0000-0000-0000-000000000000"` |
| **tenant_id**  string | The tenant identifier associated with the encryption.  **Returned:** success  **Sample:** `"00000000-0000-0000-0000-000000000000"` |
| **type**  string | The type of encryption being used.  **Returned:** success  **Sample:** `"SystemAssigned"` |
| **last_modified_time**  string | The account last modified time.  **Returned:** always  **Sample:** `"2020-01-01T00:00:00.000000+00:00"` |
| **location**  string | The resource location.  **Returned:** always  **Sample:** `"westeurope"` |
| **name**  string | The resource name.  **Returned:** always  **Sample:** `"testaccount"` |
| **new_tier**  string | The commitment tier to use for next month.  **Returned:** success  **Sample:** `"Consumption"` |
| **provisioning_state**  string | The provisioning status of the Data Lake Store account.  **Returned:** always  **Sample:** `"Succeeded"` |
| **state**  string | The state of the Data Lake Store account.  **Returned:** always  **Sample:** `"Active"` |
| **tags**  dictionary | The resource tags.  **Returned:** always  **Sample:** `{"tag1": "abc"}` |
| **trusted_id_provider_state**  string | The list of trusted identity providers associated with this Data Lake Store account.  **Returned:** success  **Sample:** `"Enabled"` |
| **trusted_id_providers**  list / elements=string | The current state of the trusted identity provider feature for this Data Lake Store account.  **Returned:** success |
| **id**  string | The resource identifier.  **Returned:** success |
| **id_provider**  string | The URL of this trusted identity provider.  **Returned:** success |
| **name**  string | The resource name.  **Returned:** success |
| **type**  string | The resource type.  **Returned:** success |
| **type**  string | The resource type.  **Returned:** always  **Sample:** `"Microsoft.DataLakeStore/accounts"` |
| **virtual_network_rules**  list / elements=string | The list of virtual network rules associated with this Data Lake Store account.  **Returned:** success |
| **name**  string | The resource name.  **Returned:** success  **Sample:** `"Rule Name"` |
| **subnet_id**  string | The resource identifier for the subnet.  **Returned:** success  **Sample:** `"/subscriptions/{subscriptionId}/resourceGroups/myRG/providers/Microsoft.Network/virtualNetworks/vnet/subnets/default"` |

### Authors

- David Duque Hernández (@next-davidduquehernandez)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
