---
collection: ansible
version: "6"
title: "community.azure.azure_rm_virtualmachineextension module – Managed Azure Virtual Machine extension"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/azure/azure_rm_virtualmachineextension_module.html
fetched_at: 2026-07-27T17:05:59+00:00
---
# community.azure.azure_rm_virtualmachineextension module – Managed Azure Virtual Machine extension

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
> see [Requirements](azure_rm_virtualmachineextension_module.md#ansible-collections-community-azure-azure-rm-virtualmachineextension-module-requirements) for details.
>
> To use it in a playbook, specify: `community.azure.azure_rm_virtualmachineextension`.

- [DEPRECATED](azure_rm_virtualmachineextension_module.md#deprecated)
- [Synopsis](azure_rm_virtualmachineextension_module.md#synopsis)
- [Requirements](azure_rm_virtualmachineextension_module.md#requirements)
- [Parameters](azure_rm_virtualmachineextension_module.md#parameters)
- [Notes](azure_rm_virtualmachineextension_module.md#notes)
- [See Also](azure_rm_virtualmachineextension_module.md#see-also)
- [Examples](azure_rm_virtualmachineextension_module.md#examples)
- [Return Values](azure_rm_virtualmachineextension_module.md#return-values)
- [Status](azure_rm_virtualmachineextension_module.md#status)

## [DEPRECATED](azure_rm_virtualmachineextension_module.md#id1)

Removed in:
:   version 2.0.0

Why:
:   The Ansible collection community.azure is deprecated. Use azure.azcollection instead.

Alternative:
:   Use [azure.azcollection.azure_rm_virtualmachineextension](../../azure/azcollection/azure_rm_virtualmachineextension_module.md#ansible-collections-azure-azcollection-azure-rm-virtualmachineextension-module) instead.

## [Synopsis](azure_rm_virtualmachineextension_module.md#id2)

- Create, update and delete Azure Virtual Machine Extension.
- Note that this module was called [community.azure.azure_rm_virtualmachine_extension](azure_rm_virtualmachine_extension_module.md#ansible-collections-community-azure-azure-rm-virtualmachine-extension-module) before Ansible 2.8. The usage did not change.

## [Requirements](azure_rm_virtualmachineextension_module.md#id3)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_virtualmachineextension_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  added in azure.azcollection 0.0.1 | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  added in azure.azcollection 0.0.1 | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  Default: `"latest"` |
| **auth_source**  string  added in azure.azcollection 0.0.1 | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  Choices:   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **auto_upgrade_minor_version**  boolean | Whether the extension handler should be automatically upgraded across minor versions.  Choices:   - `false` - `true` |
| **cert_validation_mode**  string  added in azure.azcollection 0.0.1 | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  Choices:   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  added in azure.azcollection 0.0.1 | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  Default: `"AzureCloud"` |
| **location**  string | Valid Azure location. Defaults to location of the resource group. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string / required | Name of the vm extension. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **protected_settings**  string | Json formatted protected settings for the extension. |
| **publisher**  string | The name of the extension handler publisher. |
| **resource_group**  string / required | Name of a resource group where the vm extension exists or will be created. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **settings**  string | Json formatted public settings for the extension. |
| **state**  string | State of the vm extension. Use `present` to create or update a vm extension and `absent` to delete a vm extension.  Choices:   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **type_handler_version**  string | The type version of the extension handler. |
| **virtual_machine_extension_type**  string | The type of the extension handler. |
| **virtual_machine_name**  string | The name of the virtual machine where the extension should be create or updated. |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_virtualmachineextension_module.md#id5)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_virtualmachineextension_module.md#id6)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_virtualmachineextension_module.md#id7)

```yaml+jinja
- name: Create VM Extension
  community.azure.azure_rm_virtualmachineextension:
    name: myvmextension
    location: eastus
    resource_group: myResourceGroup
    virtual_machine_name: myvm
    publisher: Microsoft.Azure.Extensions
    virtual_machine_extension_type: CustomScript
    type_handler_version: 2.0
    settings: '{"commandToExecute": "hostname"}'
    auto_upgrade_minor_version: true

- name: Delete VM Extension
  community.azure.azure_rm_virtualmachineextension:
    name: myvmextension
    location: eastus
    resource_group: myResourceGroup
    virtual_machine_name: myvm
    state: absent
```

## [Return Values](azure_rm_virtualmachineextension_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  Returned: always  Sample: `true` |
| **state**  dictionary | Current state of the vm extension.  Returned: always  Sample: `{"state": "Deleted"}` |

## [Status](azure_rm_virtualmachineextension_module.md#id9)

- This module will be removed in version 2.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](azure_rm_virtualmachineextension_module.md#deprecated).

### Authors

- Sertac Ozercan (@sozercan)
- Julien Stroheker (@julienstroheker)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.azure/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.azure)
