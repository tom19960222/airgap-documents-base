---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_monitordiagnosticsetting module – Create, update, or manage Azure Monitor diagnostic settings."
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_monitordiagnosticsetting_module.html
fetched_at: 2026-07-28T01:13:54+00:00
---
# azure.azcollection.azure_rm_monitordiagnosticsetting module – Create, update, or manage Azure Monitor diagnostic settings.

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
> see [Requirements](azure_rm_monitordiagnosticsetting_module.md#ansible-collections-azure-azcollection-azure-rm-monitordiagnosticsetting-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_monitordiagnosticsetting`.

New in azure.azcollection 1.10.0

- [Synopsis](azure_rm_monitordiagnosticsetting_module.md#synopsis)
- [Requirements](azure_rm_monitordiagnosticsetting_module.md#requirements)
- [Parameters](azure_rm_monitordiagnosticsetting_module.md#parameters)
- [Notes](azure_rm_monitordiagnosticsetting_module.md#notes)
- [See Also](azure_rm_monitordiagnosticsetting_module.md#see-also)
- [Examples](azure_rm_monitordiagnosticsetting_module.md#examples)
- [Return Values](azure_rm_monitordiagnosticsetting_module.md#return-values)

## [Synopsis](azure_rm_monitordiagnosticsetting_module.md#id1)

- Create, update, or manage Azure Monitor diagnostic settings for any type of resource.

## [Requirements](azure_rm_monitordiagnosticsetting_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_monitordiagnosticsetting_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **event_hub**  dictionary | An event hub which will receive the diagnostic logs.  At least one of *storage_account*, *log_analytics*, or *event_hub* must be specified for the diagnostic setting. |
| **hub**  string | An event hub name to receive logs. If none is specified, the default event hub will be selected. |
| **namespace**  string / required | The event hub namespace. |
| **policy**  string / required | The shared access policy. |
| **resource_group**  string | The resource group containing the event hub. If none is specified, the resource group of the *resource* parameter will be used. |
| **subscription_id**  string | The subscription ID containing the event hub. If none is specified, the subscription ID of the *resource* parameter will be used. |
| **log_analytics**  any | A log analytics workspace which will receive the diagnostic logs.  It can be a string containing the log analytics workspace resource ID.  It can be a dictionary containing *name* and optionally *subscription_id* and *resource_group*.  At least one of *storage_account*, *log_analytics*, or *event_hub* must be specified for the diagnostic setting. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **logs**  list / elements=dictionary | The list of log setttings.  At least one of *metrics* or *logs* must be specified for the diagnostic setting. |
| **category**  string | Name of a Management Group Diagnostic Log category for a resource type this setting is applied to. |
| **category_group**  string | Name of a Management Group Diagnostic Log category group for a resource type this setting is applied to. |
| **enabled**  boolean | Whether the log is enabled.  **Choices:**   - `false` - `true` ← (default) |
| **retention_policy**  dictionary | The retention policy for this log. |
| **days**  integer | The number of days for the retention policy.  **Default:** `0` |
| **enabled**  boolean | Whether the retention policy is enabled.  **Choices:**   - `false` - `true` ← (default) |
| **metrics**  list / elements=dictionary | The list of metric setttings.  At least one of *metrics* or *logs* must be specified for the diagnostic setting. |
| **category**  string | Name of a Diagnostic Metric category for a resource type this setting is applied to. |
| **enabled**  boolean | Whether the metric category is enabled.  **Choices:**   - `false` - `true` ← (default) |
| **retention_policy**  dictionary | The retention policy for this metric. |
| **days**  integer | The number of days for the retention policy.  **Default:** `0` |
| **enabled**  boolean | Whether the retention policy is enabled.  **Choices:**   - `false` - `true` ← (default) |
| **name**  string / required | The name of the diagnostic settings. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **resource**  any / required | The resource which will be monitored with the diagnostic setting.  It can be a string containing the resource ID.  It can be a dictionary containing *name*, *type*, *resource_group*, and optionally *subscription_id*.  *name*. The resource name.  *type*. The resource type including namespace, such as ‘Microsoft.Network/virtualNetworks’.  *resource_group*. The resource group containing the resource.  *subscription_id*. The subscription ID containing the resource. If none is specified, the credential’s subscription ID will be used. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **state**  string | State of the private endpoint DNS zone group. Use `present` to create or update and `absent` to delete.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **storage_account**  any | A storage account which will receive the diagnostic logs.  It can be a string containing the storage account resource ID.  It can be a dictionary containing *name* and optionally *subscription_id* and *resource_group*.  At least one of *storage_account*, *log_analytics*, or *event_hub* must be specified for the diagnostic setting. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_monitordiagnosticsetting_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_monitordiagnosticsetting_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_monitordiagnosticsetting_module.md#id6)

```yaml+jinja
- name: Create storage-based diagnostic setting for a virtual network
  azure_rm_monitordiagnosticsetting:
    name: "logs-storage"
    resource: "{{ vnet_output.state.id }}"
    storage_account: "{{ storage_output.state.id }}"
    logs:
      - category_group: "allLogs"
    metrics:
      - category: "AllMetrics"

- name: Create diagnostic setting for webapp with log analytics, event hub, and storage
  azure_rm_monitordiagnosticsetting:
    name: "webapp-logs"
    resource:
      name: "my-webapp"
      type: "Microsoft.Web/sites"
      resource_group: "my-webapp-resource-group"
    event_hub:
      namespace: "my-event-hub"
      policy: "RootManageSharedAccessKey"
    log_analytics:
      name: "my-log-analytics-workspace"
      resource_group: "my-log-analytics-workspace-resource-group"
    storage_account:
      name: "mystorageaccount"
    logs:
      - category: "AppServiceHTTPLogs"
      - category: "AppServiceConsoleLogs"
      - category: "AppServiceAppLogs"
      - category: "AppServiceAuditLogs"
      - category: "AppServiceIPSecAuditLogs"
      - category: "AppServicePlatformLogs"

- name: Delete diagnostic setting
  azure_rm_monitordiagnosticsetting:
    name: "webapp-logs"
    resource:
      name: "my-webapp"
      type: "Microsoft.Web/sites"
      resource_group: "my-webapp-resource-group"
    state: "absent"
```

## [Return Values](azure_rm_monitordiagnosticsetting_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **state**  dictionary | The state of the diagnostic setting.  **Returned:** always |
| **event_hub**  dictionary | The event hub for the diagnostic setting, if configured.  **Returned:** always |
| **hub**  string | Name of the hub within the namespace.  **Returned:** always  **Sample:** `"my-event-hub"` |
| **id**  string | ID of the event hub namespace.  **Returned:** always  **Sample:** `"/subscriptions/xxx/resourceGroups/my-resource-group/providers/Microsoft.EventHub/namespaces/my-event-hub-namespace"` |
| **namespace**  string | Name of the event hub namespace.  **Returned:** always  **Sample:** `"my-event-hub-namespace"` |
| **policy**  string | Name of the event hub shared access policy.  **Returned:** always  **Sample:** `"RootManageSharedAccessKey"` |
| **id**  string | ID of the diagnostic setting.  **Returned:** always  **Sample:** `"/subscriptions/xxx/resourcegroups/my-resource-group/providers/microsoft.network/applicationgateways/my-appgw/ providers/microsoft.insights/diagnosticSettings/my-diagnostic-setting"` |
| **log_analytics**  dictionary | The log analytics workspace for the diagnostic setting, if configured.  **Returned:** always |
| **id**  string | ID of the log analytics workspace.  **Returned:** always  **Sample:** `"/subscriptions/xxx/resourcegroups/my-resource-group/providers/microsoft.operationalinsights/workspaces/my-log-analytics-workspace"` |
| **logs**  list / elements=dictionary | Enabled log configurations for the diagnostic setting.  **Returned:** always |
| **category**  string | Name of a Management Group Diagnostic Log category for a resource type this setting is applied to.  **Returned:** always |
| **category_group**  string | Name of a Management Group Diagnostic Log category group for a resource type this setting is applied to.  **Returned:** always |
| **enabled**  boolean | Whether this log is enabled.  **Returned:** always |
| **retention_policy**  dictionary | The retention policy for this log.  **Returned:** always |
| **days**  integer | The number of days for the retention policy.  **Returned:** always |
| **enabled**  boolean | Whether the retention policy is enabled.  **Returned:** always |
| **metrics**  list / elements=dictionary | Enabled metric configurations for the diagnostic setting.  **Returned:** always |
| **category**  string | Name of a Diagnostic Metric category for a resource type this setting is applied to.  **Returned:** always |
| **enabled**  boolean | Whether the metric category is enabled.  **Returned:** always |
| **retention_policy**  dictionary | The retention policy for the metric category.  **Returned:** always |
| **days**  integer | The number of days for the retention policy.  **Returned:** always |
| **enabled**  boolean | Whether the retention policy is enabled.  **Returned:** always |
| **name**  string | Name of the diagnostic setting.  **Returned:** always  **Sample:** `"my-diagnostic-setting"` |
| **storage_account**  dictionary | The storage account for the diagnostic setting, if configured.  **Returned:** always |
| **id**  string | ID of the storage account.  **Returned:** always  **Sample:** `"/subscriptions/xxx/resourceGroups/my-resource-group/providers/Microsoft.Storage/storageAccounts/my-storage-account"` |

### Authors

- Ross Bender (@l3ender)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
