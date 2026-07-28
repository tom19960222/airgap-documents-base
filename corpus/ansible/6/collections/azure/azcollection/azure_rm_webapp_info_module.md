---
collection: ansible
version: "6"
title: "azure.azcollection.azure_rm_webapp_info module – Get Azure web app facts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/azure/azcollection/azure_rm_webapp_info_module.html
fetched_at: 2026-07-27T16:47:26+00:00
---
# azure.azcollection.azure_rm_webapp_info module – Get Azure web app facts

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
> see [Requirements](azure_rm_webapp_info_module.md#ansible-collections-azure-azcollection-azure-rm-webapp-info-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_webapp_info`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_webapp_info_module.md#synopsis)
- [Requirements](azure_rm_webapp_info_module.md#requirements)
- [Parameters](azure_rm_webapp_info_module.md#parameters)
- [Notes](azure_rm_webapp_info_module.md#notes)
- [See Also](azure_rm_webapp_info_module.md#see-also)
- [Examples](azure_rm_webapp_info_module.md#examples)
- [Return Values](azure_rm_webapp_info_module.md#return-values)

## [Synopsis](azure_rm_webapp_info_module.md#id1)

- Get facts for a specific web app or all web app in a resource group, or all web app in current subscription.

## [Requirements](azure_rm_webapp_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_webapp_info_module.md#id3)

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
| **name**  string | Only show results for a specific web app. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **resource_group**  string | Limit results by resource group. |
| **return_publish_profile**  boolean | Indicate whether to return publishing profile of the web app.  Choices:   - `false` ← (default) - `true` |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  list / elements=string | Limit results by providing a list of tags. Format tags as ‘key’ or ‘key:value’. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_webapp_info_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_webapp_info_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_webapp_info_module.md#id6)

```yaml+jinja
- name: Get facts for web app by name
  azure_rm_webapp_info:
    resource_group: myResourceGroup
    name: winwebapp1

- name: Get facts for web apps in resource group
  azure_rm_webapp_info:
    resource_group: myResourceGroup

- name: Get facts for web apps with tags
  azure_rm_webapp_info:
    tags:
      - testtag
      - foo:bar
```

## [Return Values](azure_rm_webapp_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **webapps**  complex | List of web apps.  Returned: always |
| **always_on**  boolean | If the app is kept loaded even when there’s no traffic.  Returned: always  Sample: `true` |
| **app_settings**  dictionary | App settings of the application. Only returned when web app has app settings.  Returned: always  Sample: `{"testkey": "testvalue", "testkey2": "testvalue2"}` |
| **availability_state**  string | Availability of this web app.  Returned: always  Sample: `"Normal"` |
| **default_host_name**  string | Host name of the web app.  Returned: always  Sample: `"vxxisurg397winapp4.azurewebsites.net"` |
| **enabled**  boolean | Indicates the web app enabled or not.  Returned: always  Sample: `true` |
| **enabled_host_names**  list / elements=string | Enabled host names of the web app.  Returned: always  Sample: `["vxxisurg397winapp4.azurewebsites.net", "vxxisurg397winapp4.scm.azurewebsites.net"]` |
| **frameworks**  list / elements=string | Frameworks of the application. Only returned when web app has frameworks.  Returned: always  Sample: `[{"name": "net_framework", "version": "v4.0"}, {"name": "java", "settings": {"java_container": "tomcat", "java_container_version": "8.5"}, "version": "1.7"}, {"name": "php", "version": "5.6"}]` |
| **ftp_publish_url**  string | Publishing URL of the web app when deployment type is FTP.  Returned: always  Sample: `"ftp://xxxx.ftp.azurewebsites.windows.net"` |
| **ftps_state**  string | The state of the FTP/FTPS service.  Returned: always  Sample: `"FtpsOnly"` |
| **host_name_ssl_states**  list / elements=string | SSL state per host names of the web app.  Returned: always  Sample: `[{"hostType": "Standard", "name": "vxxisurg397winapp4.azurewebsites.net", "sslState": "Disabled"}, {"hostType": "Repository", "name": "vxxisurg397winapp4.scm.azurewebsites.net", "sslState": "Disabled"}]` |
| **host_names**  list / elements=string | Host names of the web app.  Returned: always  Sample: `["vxxisurg397winapp4.azurewebsites.net"]` |
| **id**  string | ID of the web app.  Returned: always  Sample: `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Web/sites/myWebApp"` |
| **location**  string | Location of the web app.  Returned: always  Sample: `"eastus"` |
| **min_tls_version**  string | The minimum TLS encryption version required for the app.  Returned: always  Sample: `"1.2"` |
| **name**  string | Name of the web app.  Returned: always  Sample: `"winwebapp1"` |
| **outbound_ip_addresses**  string | Outbound IP address of the web app.  Returned: always  Sample: `"40.71.11.131,40.85.166.200,168.62.166.67,137.135.126.248,137.135.121.45"` |
| **plan**  string | ID of app service plan used by the web app.  Returned: always  Sample: `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Web/serverfarms/myAppServicePlan"` |
| **publishing_password**  string | Publishing profile password.  Returned: only when *return_publish_profile=True*.  Sample: `"uvANsPQpGjWJmrFfm4Ssd5rpBSqGhjMk11pMSgW2vCsQtNx9tcgZ0xN26s9A"` |
| **publishing_username**  string | Publishing profile user name.  Returned: only when *return_publish_profile=True*.  Sample: `"$vxxisuRG397winapp4"` |
| **resource_group**  string | Resource group of the web app.  Returned: always  Sample: `"myResourceGroup"` |
| **state**  string | State of the web app.  Returned: always  Sample: `"running"` |
| **tags**  dictionary | Tags assigned to the resource. Dictionary of string:string pairs.  Returned: always  Sample: `{"tag1": "abc"}` |

### Authors

- Yunge Zhu (@yungezz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/azure/issues)
[Homepage](https://azure.microsoft.com)
[Repository (Sources)](https://github.com/ansible-collections/azure)
