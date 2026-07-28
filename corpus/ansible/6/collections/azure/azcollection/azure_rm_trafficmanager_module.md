---
collection: ansible
version: "6"
title: "azure.azcollection.azure_rm_trafficmanager module – Manage a Traffic Manager profile."
source_url: https://docs.ansible.com/projects/ansible/6/collections/azure/azcollection/azure_rm_trafficmanager_module.html
fetched_at: 2026-07-27T16:47:13+00:00
---
# azure.azcollection.azure_rm_trafficmanager module – Manage a Traffic Manager profile.

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
> see [Requirements](azure_rm_trafficmanager_module.md#ansible-collections-azure-azcollection-azure-rm-trafficmanager-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_trafficmanager`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_trafficmanager_module.md#synopsis)
- [Requirements](azure_rm_trafficmanager_module.md#requirements)
- [Parameters](azure_rm_trafficmanager_module.md#parameters)
- [Notes](azure_rm_trafficmanager_module.md#notes)
- [See Also](azure_rm_trafficmanager_module.md#see-also)
- [Examples](azure_rm_trafficmanager_module.md#examples)
- [Return Values](azure_rm_trafficmanager_module.md#return-values)

## [Synopsis](azure_rm_trafficmanager_module.md#id1)

- Create, update and delete a Traffic Manager profile.

## [Requirements](azure_rm_trafficmanager_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_trafficmanager_module.md#id3)

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
| **dns_config**  string | The DNS settings of the Traffic Manager profile. |
| **relative_name**  string | The relative DNS name provided by this Traffic Manager profile.  If no provided, name of the Traffic Manager will be used |
| **ttl**  string | The DNS Time-To-Live (TTL), in seconds.  Default: `60` |
| **endpoints**  string | The list of endpoints in the Traffic Manager profile. |
| **endpoint_location**  string | Specifies the location of the external or nested endpoints when using the ‘Performance’ traffic routing method. |
| **endpoint_status**  string | The status of the endpoint.  Choices:   - `"Enabled"` - `"Disabled"` |
| **geo_mapping**  string | The list of countries/regions mapped to this endpoint when using the ‘Geographic’ traffic routing method. |
| **id**  string | Fully qualified resource Id for the resource. |
| **min_child_endpoints**  string | The minimum number of endpoints that must be available in the child profile in order for the parent profile to be considered available.  Only applicable to endpoint of type ‘NestedEndpoints’. |
| **name**  string / required | The name of the endpoint. |
| **priority**  string | The priority of this endpoint when using the ‘Priority’ traffic routing method.  Possible values are from 1 to 1000, lower values represent higher priority.  This is an optional parameter. If specified, it must be specified on all endpoints.  No two endpoints can share the same priority value. |
| **target**  string | The fully-qualified DNS name of the endpoint. |
| **target_resource_id**  string | The Azure Resource URI of the of the endpoint.  Not applicable to endpoints of type ‘ExternalEndpoints’. |
| **type**  string / required | The type of the endpoint. Ex- Microsoft.network/TrafficManagerProfiles/ExternalEndpoints. |
| **weight**  string | The weight of this endpoint when using the ‘Weighted’ traffic routing method.  Possible values are from 1 to 1000. |
| **location**  string | Valid azure location. Defaults to ‘global’. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **monitor_config**  string | The endpoint monitoring settings of the Traffic Manager profile.  Default: `{"path": "/", "port": 80, "protocol": "HTTP"}` |
| **interval_in_seconds**  string | The monitor interval for endpoints in this profile. |
| **path**  string | The path relative to the endpoint domain name used to probe for endpoint health. |
| **port**  string | The TCP port used to probe for endpoint health. |
| **protocol**  string | The protocol (HTTP, HTTPS or TCP) used to probe for endpoint health.  Choices:   - `"HTTP"` - `"HTTPS"` - `"TCP"` |
| **timeout_in_seconds**  string | The monitor timeout for endpoints in this profile. |
| **tolerated_number_of_failures**  string | The number of consecutive failed health check before declaring an endpoint in this profile Degraded after the next failed health check. |
| **name**  string / required | Name of the Traffic Manager profile. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **profile_status**  string | The status of the Traffic Manager profile.  Choices:   - `"Enabled"` ← (default) - `"Disabled"` |
| **resource_group**  string / required | Name of a resource group where the Traffic Manager profile exists or will be created. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **state**  string | Assert the state of the Traffic Manager profile. Use `present` to create or update a Traffic Manager profile and `absent` to delete it.  Choices:   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **traffic_routing_method**  string | The traffic routing method of the Traffic Manager profile.  Choices:   - `"Performance"` ← (default) - `"Priority"` - `"Weighted"` - `"Geographic"` |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_trafficmanager_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_trafficmanager_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_trafficmanager_module.md#id6)

```yaml+jinja
- name: Create a Traffic Manager Profile
  azure_rm_trafficmanager:
    name: tmtest
    resource_group: tmt
    location: global
    profile_status: Enabled
    traffic_routing_method: Priority
    dns_config:
      relative_name: tmtest
      ttl: 60
    monitor_config:
      protocol: HTTPS
      port: 80
      path: '/'
    endpoints:
      - name: e1
        type: Microsoft.network/TrafficManagerProfiles/ExternalEndpoints
        endpoint_location: West US 2
        endpoint_status: Enabled
        priority: 2
        target: 1.2.3.4
        weight: 1
    tags:
      Environment: Test

- name: Delete a Traffic Manager Profile
  azure_rm_trafficmanager:
    state: absent
    name: tmtest
    resource_group: tmt
```

## [Return Values](azure_rm_trafficmanager_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **state**  dictionary | Current state of the Traffic Manager Profile  Returned: always  Sample: `{"dns_config": {"fqdn": "tmtest.trafficmanager.net", "relative_name": "tmtest", "ttl": 60}, "endpoints": [{"endpoint_location": "West US 2", "endpoint_monitor_status": "Degraded", "endpoint_status": "Enabled", "geo_mapping": null, "id": "/subscriptions/XXXXXX...XXXXXXXXX/resourceGroups/tmt/providers/Microsoft.Network/trafficManagerProfiles/tmtest/externalEndpoints/e1", "min_child_endpoints": null, "name": "e1", "priority": 2, "target": "1.2.3.4", "target_resource_id": null, "type": "Microsoft.Network/trafficManagerProfiles/externalEndpoints", "weight": 1}], "id": "/subscriptions/XXXXXX...XXXXXXXXX/resourceGroups/tmt/providers/Microsoft.Network/trafficManagerProfiles/tmtest", "location": "global", "monitor_config": {"interval_in_seconds": 30, "path": "/", "port": 80, "profile_monitor_status": "Degraded", "protocol": "HTTPS", "timeout_in_seconds": 10, "tolerated_number_of_failures": 3}, "name": "tmtest", "profile_status": "Enabled", "tags": {"Environment": "Test"}, "traffic_routing_method": "Priority", "type": "Microsoft.Network/trafficManagerProfiles"}` |

### Authors

- Hai Cao

### Collection links

[Issue Tracker](https://github.com/ansible-collections/azure/issues)
[Homepage](https://azure.microsoft.com)
[Repository (Sources)](https://github.com/ansible-collections/azure)
