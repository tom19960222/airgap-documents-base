---
collection: ansible
version: "6"
title: "azure.azcollection.azure_rm_loganalyticsworkspace_info module – Get facts of Azure Log Analytics workspaces"
source_url: https://docs.ansible.com/projects/ansible/6/collections/azure/azcollection/azure_rm_loganalyticsworkspace_info_module.html
fetched_at: 2026-07-27T16:46:32+00:00
---
# azure.azcollection.azure_rm_loganalyticsworkspace_info module – Get facts of Azure Log Analytics workspaces

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
> see [Requirements](azure_rm_loganalyticsworkspace_info_module.md#ansible-collections-azure-azcollection-azure-rm-loganalyticsworkspace-info-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_loganalyticsworkspace_info`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_loganalyticsworkspace_info_module.md#synopsis)
- [Requirements](azure_rm_loganalyticsworkspace_info_module.md#requirements)
- [Parameters](azure_rm_loganalyticsworkspace_info_module.md#parameters)
- [Notes](azure_rm_loganalyticsworkspace_info_module.md#notes)
- [See Also](azure_rm_loganalyticsworkspace_info_module.md#see-also)
- [Examples](azure_rm_loganalyticsworkspace_info_module.md#examples)
- [Return Values](azure_rm_loganalyticsworkspace_info_module.md#return-values)

## [Synopsis](azure_rm_loganalyticsworkspace_info_module.md#id1)

- Get, query Azure Log Analytics workspaces.

## [Requirements](azure_rm_loganalyticsworkspace_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_loganalyticsworkspace_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  added in azure.azcollection 0.0.1 | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  added in azure.azcollection 0.0.1 | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  Default: `"latest"` |
| **auth_source**  string  added in azure.azcollection 0.0.1 | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  Choices:   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  added in azure.azcollection 0.0.1 | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  Choices:   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  added in azure.azcollection 0.0.1 | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  Default: `"AzureCloud"` |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string | Name of the workspace. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **resource_group**  string / required | Name of resource group. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **show_intelligence_packs**  string | Show the intelligence packs for a workspace.  Note this will cost one more network overhead for each workspace, expected slow response. |
| **show_management_groups**  string | Show the management groups for a workspace.  Note this will cost one more network overhead for each workspace, expected slow response. |
| **show_shared_keys**  string | Show the shared keys for a workspace.  Note this will cost one more network overhead for each workspace, expected slow response. |
| **show_usages**  string | Show the list of usages for a workspace.  Note this will cost one more network overhead for each workspace, expected slow response. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  list / elements=string | Limit results by providing a list of tags. Format tags as ‘key’ or ‘key:value’. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_loganalyticsworkspace_info_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_loganalyticsworkspace_info_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_loganalyticsworkspace_info_module.md#id6)

```yaml+jinja
- name: Query a workspace
  azure_rm_loganalyticsworkspace_info:
      resource_group: myResourceGroup
      name: myLogAnalyticsWorkspace
      show_intelligence_packs: true
      show_management_groups: true
      show_shared_keys: true
      show_usages: true
```

## [Return Values](azure_rm_loganalyticsworkspace_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | Workspace resource path.  Returned: success  Sample: `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.OperationalInsights/workspaces/m yLogAnalyticsWorkspace"` |
| **intelligence_packs**  list / elements=string | Lists all the intelligence packs possible and whether they are enabled or disabled for a given workspace.  Returned: success  Sample: `[{"enabled": true, "name": "CapacityPerformance"}]` |
| **location**  string | Resource location.  Returned: success  Sample: `"eastus"` |
| **management_groups**  dictionary | Management groups connected to the workspace.  Returned: success  Sample: `{"value": []}` |
| **retention_in_days**  integer | The workspace data retention in days.  -1 means Unlimited retention for *sku=unlimited*.  730 days is the maximum allowed for all other SKUs.  Returned: success  Sample: `40` |
| **shared_keys**  dictionary | Shared keys for the workspace.  Returned: success  Sample: `{"primarySharedKey": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "secondarySharedKey": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}` |
| **sku**  string | The SKU of the workspace.  Returned: success  Sample: `"per_gb2018"` |
| **usages**  dictionary | Usage metrics for the workspace.  Returned: success  Sample: `{"value": [{"currentValue": 0, "limit": 524288000, "name": {"localizedValue": "Data Analyzed", "value": "DataAnalyzed"}, "nextResetTime": "2017-10-03T00:00:00Z", "quotaPeriod": "P1D", "unit": "Bytes"}]}` |

### Authors

- Yuwei Zhou (@yuwzho)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/azure/issues)
[Homepage](https://azure.microsoft.com)
[Repository (Sources)](https://github.com/ansible-collections/azure)
