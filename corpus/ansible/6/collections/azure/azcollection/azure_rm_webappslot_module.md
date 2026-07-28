---
collection: ansible
version: "6"
title: "azure.azcollection.azure_rm_webappslot module – Manage Azure Web App slot"
source_url: https://docs.ansible.com/projects/ansible/6/collections/azure/azcollection/azure_rm_webappslot_module.html
fetched_at: 2026-07-27T16:47:27+00:00
---
# azure.azcollection.azure_rm_webappslot module – Manage Azure Web App slot

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
> see [Requirements](azure_rm_webappslot_module.md#ansible-collections-azure-azcollection-azure-rm-webappslot-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_webappslot`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_webappslot_module.md#synopsis)
- [Requirements](azure_rm_webappslot_module.md#requirements)
- [Parameters](azure_rm_webappslot_module.md#parameters)
- [Notes](azure_rm_webappslot_module.md#notes)
- [See Also](azure_rm_webappslot_module.md#see-also)
- [Examples](azure_rm_webappslot_module.md#examples)
- [Return Values](azure_rm_webappslot_module.md#return-values)

## [Synopsis](azure_rm_webappslot_module.md#id1)

- Create, update and delete Azure Web App slot.

## [Requirements](azure_rm_webappslot_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_webappslot_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  added in azure.azcollection 0.0.1 | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  added in azure.azcollection 0.0.1 | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  Default: `"latest"` |
| **app_settings**  string | Configure web app slot application settings. Suboptions are in key value pair format. |
| **app_state**  string | Start/Stop/Restart the slot.  Choices:   - `"started"` ← (default) - `"stopped"` - `"restarted"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  Choices:   - `false` - `true` ← (default) |
| **auth_source**  string  added in azure.azcollection 0.0.1 | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  Choices:   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **auto_swap_slot_name**  string | Used to configure target slot name to auto swap, or disable auto swap.  Set it target slot name to auto swap.  Set it to False to disable auto slot swap. |
| **cert_validation_mode**  string  added in azure.azcollection 0.0.1 | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  Choices:   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  added in azure.azcollection 0.0.1 | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  Default: `"AzureCloud"` |
| **configuration_source**  string | Source slot to clone configurations from when creating slot. Use webapp’s name to refer to the production slot. |
| **container_settings**  string | Web app slot container settings. |
| **name**  string | Name of container, for example `imagename:tag`. |
| **registry_server_password**  string | The container registry server password. |
| **registry_server_url**  string | Container registry server URL, for example `mydockerregistry.io`. |
| **registry_server_user**  string | The container registry server user name. |
| **deployment_source**  string | Deployment source for git. |
| **branch**  string | The branch name of the repository. |
| **url**  string | Repository URL of deployment source. |
| **frameworks**  string | Set of run time framework settings. Each setting is a dictionary.  See <https://docs.microsoft.com/en-us/azure/app-service/app-service-web-overview> for more info. |
| **name**  string | Name of the framework.  Supported framework list for Windows web app and Linux web app is different.  Windows web apps support `java`, `net_framework`, `php`, `python`, and `node` from June 2018.  Windows web apps support multiple framework at same time.  Linux web apps support `java`, `ruby`, `php`, `dotnetcore`, and `node` from June 2018.  Linux web apps support only one framework.  Java framework is mutually exclusive with others.  Choices:   - `"java"` - `"net_framework"` - `"php"` - `"python"` - `"ruby"` - `"dotnetcore"` - `"node"` |
| **settings**  string | List of settings of the framework. |
| **java_container**  string | Name of Java container. This is supported by specific framework `java` onlys, for example `Tomcat`, `Jetty`. |
| **java_container_version**  string | Version of Java container. This is supported by specific framework `java` only.  For `Tomcat`, for example `8.0`, `8.5`, `9.0`. For `Jetty`, for example `9.1`, `9.3`. |
| **version**  string | Version of the framework. For Linux web app supported value, see <https://aka.ms/linux-stacks> for more info.  `net_framework` supported value sample, `v4.0` for .NET 4.6 and `v3.0` for .NET 3.5.  `php` supported value sample, `5.5`, `5.6`, `7.0`.  `python` supported value sample, `5.5`, `5.6`, `7.0`.  `node` supported value sample, `6.6`, `6.9`.  `dotnetcore` supported value sample, `1.0`, `1.1`, `1.2`.  `ruby` supported value sample, 2.3.  `java` supported value sample, `1.9` for Windows web app. `1.8` for Linux web app. |
| **location**  string | Resource location. If not set, location from the resource group will be used as default. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string / required | Unique name of the deployment slot to create or update. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **purge_app_settings**  boolean | Purge any existing application settings. Replace slot application settings with app_settings.  Choices:   - `false` ← (default) - `true` |
| **resource_group**  string / required | Name of the resource group to which the resource belongs. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **startup_file**  string | The slot startup file.  This only applies for Linux web app slot. |
| **state**  string | State of the Web App deployment slot.  Use `present` to create or update a slot and `absent` to delete it.  Choices:   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **swap**  string | Swap deployment slots of a web app. |
| **action**  string | Swap types.  `preview` is to apply target slot settings on source slot first.  `swap` is to complete swapping.  `reset` is to reset the swap.  Choices:   - `"preview"` ← (default) - `"swap"` - `"reset"` |
| **preserve_vnet**  boolean | `True` to preserve virtual network to the slot during swap. Otherwise `False`.  Choices:   - `false` - `true` ← (default) |
| **target_slot**  string | Name of target slot to swap. If set to None, then swap with production slot. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **webapp_name**  string / required | Web app name which this deployment slot belongs to. |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_webappslot_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_webappslot_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_webappslot_module.md#id6)

```yaml+jinja
- name: Create a webapp slot
  azure_rm_webappslot:
    resource_group: myResourceGroup
    webapp_name: myJavaWebApp
    name: stage
    configuration_source: myJavaWebApp
    app_settings:
      testkey: testvalue

- name: swap the slot with production slot
  azure_rm_webappslot:
    resource_group: myResourceGroup
    webapp_name: myJavaWebApp
    name: stage
    swap:
      action: swap

- name: stop the slot
  azure_rm_webappslot:
    resource_group: myResourceGroup
    webapp_name: myJavaWebApp
    name: stage
    app_state: stopped

- name: udpate a webapp slot app settings
  azure_rm_webappslot:
    resource_group: myResourceGroup
    webapp_name: myJavaWebApp
    name: stage
    app_settings:
      testkey: testvalue2

- name: udpate a webapp slot frameworks
  azure_rm_webappslot:
    resource_group: myResourceGroup
    webapp_name: myJavaWebApp
    name: stage
    frameworks:
      - name: "node"
        version: "10.1"
```

## [Return Values](azure_rm_webappslot_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | ID of current slot.  Returned: always  Sample: `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Web/sites/testapp/slots/stage1"` |

### Authors

- Yunge Zhu(@yungezz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/azure/issues)
[Homepage](https://azure.microsoft.com)
[Repository (Sources)](https://github.com/ansible-collections/azure)
