---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_privatelinkservice module – Managed private link service resource"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_privatelinkservice_module.html
fetched_at: 2026-07-28T01:14:23+00:00
---
# azure.azcollection.azure_rm_privatelinkservice module – Managed private link service resource

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
> see [Requirements](azure_rm_privatelinkservice_module.md#ansible-collections-azure-azcollection-azure-rm-privatelinkservice-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_privatelinkservice`.

New in azure.azcollection 1.12.0

- [Synopsis](azure_rm_privatelinkservice_module.md#synopsis)
- [Requirements](azure_rm_privatelinkservice_module.md#requirements)
- [Parameters](azure_rm_privatelinkservice_module.md#parameters)
- [Notes](azure_rm_privatelinkservice_module.md#notes)
- [See Also](azure_rm_privatelinkservice_module.md#see-also)
- [Examples](azure_rm_privatelinkservice_module.md#examples)
- [Return Values](azure_rm_privatelinkservice_module.md#return-values)

## [Synopsis](azure_rm_privatelinkservice_module.md#id1)

- Create, Update or Delete private link service resource.

## [Requirements](azure_rm_privatelinkservice_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_privatelinkservice_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  **Choices:**   - `false` - `true` ← (default) |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **auto_approval**  dictionary | The auto-approval list of the private link service. |
| **subscriptions**  list / elements=string | The list of subscriptions. |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **enable_proxy_protocol**  boolean | Whether the private link service is enabled for proxy protocol or not.  **Choices:**   - `false` - `true` |
| **fqdns**  list / elements=string | The list of Fqdn. |
| **ip_configurations**  list / elements=dictionary | An array of private link service IP configurations. |
| **name**  string | The name of private link service ip configuration. |
| **properties**  dictionary | The property of the private link service IP configurations. |
| **primary**  boolean | Whether the ip configuration is primary or not.  **Choices:**   - `false` - `true` |
| **private_ip_address_version**  string | Whether the specific IP configuration is IPv4 or IPv6.  **Choices:**   - `"IPv4"` - `"IPv6"` |
| **private_ip_allocation_method**  string | The private IP address allocation method.  **Choices:**   - `"Static"` - `"Dynamic"` |
| **subnet**  dictionary | The reference to the subnet resource. |
| **id**  string | The ID of the subnet. |
| **load_balancer_frontend_ip_configurations**  list / elements=dictionary | An array of references to the load balancer IP configurations  Cannot have more than one load balancer frontend IP configuration on the private link service. |
| **id**  string | The load balancer frontend IP’s ID. |
| **location**  string | The resource location. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string / required | The name of the private link service. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **resource_group**  string / required | The name of the resource group. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **state**  string | Assert the state of the pirvate link service.  Use *state=present* to create or update the link service and *state=absent* to delete it.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **visibility**  dictionary | The visibility list of the private link service. |
| **subscriptions**  list / elements=string | The list of subscriptions. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_privatelinkservice_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_privatelinkservice_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_privatelinkservice_module.md#id6)

```yaml+jinja
- name: Create the private link service
  azure_rm_privatelinkservice:
    name: linkservice-name
    resource_group: myResourceGroup
    enable_proxy_protocol: true
    fqdns:
      - 'dns01.com'
      - 'dns02.com'
    visibility:
      subscriptions:
        - xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
        - yyyyyy-yyyyy-yyyy-yyyy-yyyyyyyyyyy
    auto_approval:
      subscriptions:
        - xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
        - yyyyyy-yyyyy-yyyy-yyyy-yyyyyyyyyyy
    load_balancer_frontend_ip_configurations:
      - id: load_balancer_frontend_ip_configurations_id
    ip_configurations:
      - name: testSubnet
        properties:
          primary: false
          private_ip_allocation_method: 'Dynamic'
          private_ip_address_version: 'IPv4'
          subnet:
            id: subnet_id
      - name: subnetfredprivate-1
        properties:
          primary: true
          private_ip_allocation_method: 'Static'
          private_ip_address_version: 'IPv4'
          subnet:
            id: subnet_id
    tags:
      key1: value1
      key2: value2

- name: delete the private link service
  azure_rm_privatelinkservice:
    name: linkservice-name
    resource_group: myResourceGroup
    state: absent
```

## [Return Values](azure_rm_privatelinkservice_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **link_service**  complex | List of private link service info.  **Returned:** always |
| **alias**  string | The alias of the private link service.  **Returned:** always  **Sample:** `"linkservice.6a244dd8-8416-40cf-8c04-52b353bdd507.eastus.azure.privatelinkservice"` |
| **auto_approval**  dictionary | The auto-approval list of the private link service.  **Returned:** always  **Sample:** `{"subscriptions": ["xxxx-xxxx", "yyyy-yyyyy"]}` |
| **enable_proxy_protocol**  boolean | Whether the private link service is enabled for proxy protocol or not.  **Returned:** always  **Sample:** `false` |
| **etag**  string | A unique read-only string that changes whenever the resource is updated.  **Returned:** always  **Sample:** `"f7d60f37-ea2b-4091-8546-1327f35468c4"` |
| **fqdns**  list / elements=string | The list of Fqdn.  **Returned:** always  **Sample:** `["fqdns1.com", "fqdns2.com"]` |
| **id**  string | Resource ID of the private link service.  **Returned:** always  **Sample:** `"/subscriptions/xxx-xxx/resourceGroups/myResourceGroup/providers/Microsoft.Network/privateLinkServices/linkservice"` |
| **ip_configurations**  complex | An array of private link service IP configurations.  **Returned:** always |
| **name**  string | The name of the IP configurations  **Returned:** always  **Sample:** `"subnetfredprivate-1"` |
| **properties**  complex | The IP configuration properties.  **Returned:** always |
| **primary**  boolean | Whether the ip configuration is primary or not.  **Returned:** always  **Sample:** `true` |
| **private_ip_address_version**  string | Whether the specific IP configuration is IPv4 or IPv6.  **Returned:** always  **Sample:** `"IPv4"` |
| **private_ip_allocation_method**  string | The private IP address allocation method.  **Returned:** always  **Sample:** `"Dynamic"` |
| **subnet**  dictionary | The reference to the subnet resource.  **Returned:** always  **Sample:** `{"id": "/subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Network/virtualNetworks/vnet/subnets/subnamee"}` |
| **load_balancer_frontend_ip_configurations**  list / elements=string | An array of references to the load balancer IP configurations.  **Returned:** awalys  **Sample:** `[{"id": "/subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Network/loadBalancers/testlb/frontendIPConfigurations/front01"}]` |
| **location**  string | Resource location.  **Returned:** always  **Sample:** `"eastus"` |
| **name**  string | Name of the private link service.  **Returned:** always  **Sample:** `"linkservice"` |
| **network_interfaces**  list / elements=string | An array of references to the network interfaces created for this private link service.  **Returned:** always  **Sample:** `[{"id": "/subscriptions/xxx-xxx/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/testlinkservice.nic.f5"}]` |
| **private_endpoint_connections**  complex | An array of list about connections to the private endpoint.  **Returned:** always |
| **id**  string | The ID of the private endpoint connection.  **Returned:** always  **Sample:** `"/subscriptions/xxx/resourceGroups/myRG/providers/Microsoft.Network/privateLinkServices/linkservice/privateEndpointConnections/tes"` |
| **private_endpoint**  string | The ID of the private endpoint.  **Returned:** always  **Sample:** `"/subscriptions/xxx-xxx/resourceGroups/myResourceGroup/providers/Microsoft.Network/privateEndpoints/test002"` |
| **provisioning_state**  string | The provisioning state of the private link service resource.  **Returned:** always  **Sample:** `"Succeeded"` |
| **tags**  dictionary | The resource tags.  **Returned:** always  **Sample:** `{"key1": "value1"}` |
| **type**  string | The resource type.  **Returned:** always  **Sample:** `"Microsoft.Network/privateLinkServices"` |
| **visibility**  dictionary | The visibility list of the private link service.  **Returned:** always  **Sample:** `{"subscriptions": ["xxxx-xxxx", "yyyy-yyyyy"]}` |

### Authors

- xuzhang3 (@xuzhang3)
- Fred-sun (@Fred-sun)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
