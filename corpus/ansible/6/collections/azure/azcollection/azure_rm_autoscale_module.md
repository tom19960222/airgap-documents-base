---
collection: ansible
version: "6"
title: "azure.azcollection.azure_rm_autoscale module – Manage Azure autoscale setting"
source_url: https://docs.ansible.com/projects/ansible/6/collections/azure/azcollection/azure_rm_autoscale_module.html
fetched_at: 2026-07-27T16:45:51+00:00
---
# azure.azcollection.azure_rm_autoscale module – Manage Azure autoscale setting

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
> see [Requirements](azure_rm_autoscale_module.md#ansible-collections-azure-azcollection-azure-rm-autoscale-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_autoscale`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_autoscale_module.md#synopsis)
- [Requirements](azure_rm_autoscale_module.md#requirements)
- [Parameters](azure_rm_autoscale_module.md#parameters)
- [Notes](azure_rm_autoscale_module.md#notes)
- [See Also](azure_rm_autoscale_module.md#see-also)
- [Examples](azure_rm_autoscale_module.md#examples)
- [Return Values](azure_rm_autoscale_module.md#return-values)

## [Synopsis](azure_rm_autoscale_module.md#id1)

- Create, delete an autoscale setting.

## [Requirements](azure_rm_autoscale_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_autoscale_module.md#id3)

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
| **enabled**  boolean | Specifies whether automatic scaling is enabled for the resource.  Choices:   - `false` - `true` ← (default) |
| **location**  string | location of the resource. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string / required | name of the resource. |
| **notifications**  string | The collection of notifications. |
| **custom_emails**  string | The custom e-mails list. This value can be null or empty, in which case this attribute will be ignored. |
| **send_to_subscription_administrator**  boolean | A value indicating whether to send email to subscription administrator.  Choices:   - `false` ← (default) - `true` |
| **send_to_subscription_co_administrators**  boolean | A value indicating whether to send email to subscription co-administrators.  Choices:   - `false` ← (default) - `true` |
| **webhooks**  string | The list of webhook notifications service uri. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **profiles**  string | The collection of automatic scaling profiles that specify different scaling parameters for different time periods.  A maximum of 20 profiles can be specified. |
| **count**  string / required | The number of instances that will be set if metrics are not available for evaluation.  The default is only used if the current instance count is lower than the default. |
| **fixed_date_end**  string | The specific date-time end for the profile.  This element is not used if the Recurrence element is used. |
| **fixed_date_start**  string | The specific date-time start for the profile.  This element is not used if the Recurrence element is used. |
| **fixed_date_timezone**  string | The specific date-time timezone for the profile.  This element is not used if the Recurrence element is used. |
| **max_count**  string | The maximum number of instances for the resource.  The actual maximum number of instances is limited by the cores that are available in the subscription. |
| **min_count**  string | The minimum number of instances for the resource. |
| **name**  string / required | The name of the profile. |
| **recurrence_days**  string | The days of repeating times at which this profile begins.  This element is not used if the FixedDate element is used. |
| **recurrence_frequency**  string | How often the schedule profile should take effect.  If this value is `Week`, meaning each week will have the same set of profiles.  This element is not used if the FixedDate element is used.  Choices:   - `"None"` ← (default) - `"Second"` - `"Minute"` - `"Hour"` - `"Day"` - `"Week"` - `"Month"` - `"Year"` |
| **recurrence_hours**  string | The hours of repeating times at which this profile begins.  This element is not used if the FixedDate element is used. |
| **recurrence_mins**  string | The mins of repeating times at which this profile begins.  This element is not used if the FixedDate element is used. |
| **recurrence_timezone**  string | The timezone of repeating times at which this profile begins.  This element is not used if the FixedDate element is used. |
| **rules**  string | The collection of rules that provide the triggers and parameters for the scaling action.  A maximum of 10 rules can be specified. |
| **cooldown**  string | The amount of time (minutes) to wait since the last scaling action before this action occurs.  It must be between 1 ~ 10080. |
| **direction**  string | Whether the scaling action increases or decreases the number of instances.  Choices:   - `"Increase"` - `"Decrease"` |
| **metric_name**  string / required | The name of the metric that defines what the rule monitors. |
| **metric_resource_uri**  string | The resource identifier of the resource the rule monitors. |
| **operator**  string | The operator that is used to compare the metric data and the threshold.  Choices:   - `"Equals"` - `"NotEquals"` - `"GreaterThan"` ← (default) - `"GreaterThanOrEqual"` - `"LessThan"` - `"LessThanOrEqual"` |
| **statistic**  string | How the metrics from multiple instances are combined.  Choices:   - `"Average"` ← (default) - `"Min"` - `"Max"` - `"Sum"` |
| **threshold**  string | The threshold of the metric that triggers the scale action.  Default: `70` |
| **time_aggregation**  string | How the data that is collected should be combined over time.  Choices:   - `"Average"` ← (default) - `"Minimum"` - `"Maximum"` - `"Total"` - `"Count"` |
| **time_grain**  string / required | The granularity(minutes) of metrics the rule monitors.  Must be one of the predefined values returned from metric definitions for the metric.  Must be between 1 ~ 720. |
| **time_window**  string / required | The range of time(minutes) in which instance data is collected.  This value must be greater than the delay in metric collection, which can vary from resource-to-resource.  Must be between 5 ~ 720. |
| **type**  string | The type of action that should occur when the scale rule fires.  Choices:   - `"PercentChangeCount"` - `"ExactCount"` - `"ChangeCount"` |
| **value**  string | The number of instances that are involved in the scaling action.  This value must be 1 or greater. |
| **resource_group**  string / required | Resource group of the resource. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **state**  string | Assert the state of the virtual network. Use `present` to create or update and `absent` to delete.  Choices:   - `"present"` ← (default) - `"absent"` |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **target**  string | The identifier of the resource to apply autoscale setting.  It could be the resource id string.  It also could be a dict contains the `name`, `subscription_id`, `namespace`, `types`, `resource_group` of the resource. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_autoscale_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_autoscale_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_autoscale_module.md#id6)

```yaml+jinja
- name: Create an auto scale
  azure_rm_autoscale:
      target: "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualMachineScaleSets/myVmss"
      enabled: true
      profiles:
      - count: '1'
        recurrence_days:
        - Monday
        name: Auto created scale condition
        recurrence_timezone: China Standard Time
        recurrence_mins:
        - '0'
        min_count: '1'
        max_count: '1'
        recurrence_frequency: Week
        recurrence_hours:
        - '18'
      name: scale
      resource_group: myResourceGroup

- name: Create an auto scale with complicated profile
  azure_rm_autoscale:
      target: "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualMachineScaleSets
               /myVmss"
      enabled: true
      profiles:
      - count: '1'
        recurrence_days:
        - Monday
        name: Auto created scale condition 0
        rules:
        - time_aggregation: Average
          time_window: 10
          direction: Increase
          metric_name: Percentage CPU
          metric_resource_uri: "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtua
                                lMachineScaleSets/vmss"
          value: '1'
          threshold: 70
          cooldown: 5
          time_grain: 1
          statistic: Average
          operator: GreaterThan
          type: ChangeCount
        max_count: '1'
        recurrence_mins:
        - '0'
        min_count: '1'
        recurrence_timezone: China Standard Time
        recurrence_frequency: Week
        recurrence_hours:
        - '6'
      notifications:
      - email_admin: True
        email_co_admin: False
        custom_emails:
        - yuwzho@microsoft.com
      name: scale
      resource_group: myResourceGroup

- name: Delete an Azure Auto Scale Setting
  azure_rm_autoscale:
    state: absent
    resource_group: myResourceGroup
    name: scale
```

## [Return Values](azure_rm_autoscale_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **state**  dictionary | Current state of the resource.  Returned: always  Sample: `{"changed": false, "enabled": true, "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/microsoft.insights/autoscalesettings/scale", "location": "eastus", "name": "scale", "notifications": [{"custom_emails": ["yuwzho@microsoft.com"], "send_to_subscription_administrator": true, "send_to_subscription_co_administrators": false, "webhooks": []}], "profiles": [{"count": "1", "max_count": "1", "min_count": "1", "name": "Auto created scale condition 0", "recurrence_days": ["Monday"], "recurrence_frequency": "Week", "recurrence_hours": ["6"], "recurrence_mins": ["0"], "recurrence_timezone": "China Standard Time", "rules": [{"cooldown": 5.0, "direction": "Increase", "metric_name": "Percentage CPU", "metric_resource_uri": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsof t.Compute/virtualMachineScaleSets/MyVmss", "operator": "GreaterThan", "statistic": "Average", "threshold": 70.0, "time_aggregation": "Average", "time_grain": 1.0, "time_window": 10.0, "type": "ChangeCount", "value": "1"}]}], "target": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualMachineScale Sets/myVmss"}` |

### Authors

- Yuwei Zhou (@yuwzho)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/azure/issues)
[Homepage](https://azure.microsoft.com)
[Repository (Sources)](https://github.com/ansible-collections/azure)
