---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_apimanagement module – Manage Azure api instances"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_apimanagement_module.html
fetched_at: 2026-07-28T01:12:09+00:00
---
# azure.azcollection.azure_rm_apimanagement module – Manage Azure api instances

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
> see [Requirements](azure_rm_apimanagement_module.md#ansible-collections-azure-azcollection-azure-rm-apimanagement-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_apimanagement`.

New in azure.azcollection 1.6.0

- [Synopsis](azure_rm_apimanagement_module.md#synopsis)
- [Requirements](azure_rm_apimanagement_module.md#requirements)
- [Parameters](azure_rm_apimanagement_module.md#parameters)
- [Notes](azure_rm_apimanagement_module.md#notes)
- [See Also](azure_rm_apimanagement_module.md#see-also)
- [Examples](azure_rm_apimanagement_module.md#examples)
- [Return Values](azure_rm_apimanagement_module.md#return-values)

## [Synopsis](azure_rm_apimanagement_module.md#id2)

- Create azure api instance.
- Update the existing azure api instance.
- Delete azure api instance.

## [Requirements](azure_rm_apimanagement_module.md#id3)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_apimanagement_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_id**  string / required | API revision identifier. It must be unique in the current API Management service instance. |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **api_revision**  string | Describes the Revision of the Api.  If no value is provided, default revision 1 is created |
| **api_revision_description**  string | Description of the Api Revision. |
| **api_type**  string | Type of Api to create.  `http` creates a SOAP to REST API.  `soap` creates a SOAP pass-through API.  **Choices:**   - `"soap"` - `"http"` |
| **api_version**  string | Indicates the Version identifier of the API if the API is versioned |
| **api_version_description**  string | Description of the Api Version. |
| **api_version_set**  dictionary | Version set details |
| **description**  string | Description of API Version Set. |
| **id**  string | Identifier for existing API Version Set  Omit this value to create a new Version Set. |
| **name**  string | The display Name of the API Version Set. |
| **version_header_name**  string | Name of HTTP header parameter that indicates the API Version if versioningScheme is set to `header`. |
| **version_query_name**  string | Name of query parameter that indicates the API Version if versioningScheme is set to `query`. |
| **versioning_scheme**  string | An value that determines where the API Version identifer will be located in a HTTP request.  **Choices:**   - `"Segment"` - `"Query"` - `"Header"` |
| **api_version_set_id**  string | A resource identifier for the related ApiVersionSet. |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  **Choices:**   - `false` - `true` ← (default) |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **authentication_settings**  dictionary | Collection of authentication settings included into this API. |
| **o_auth2**  dictionary | OAuth2 Authentication settings |
| **authorization_server_id**  string | OAuth authorization server identifier. |
| **scope**  string | operations scope. |
| **openid**  dictionary | OpenID Connect Authentication Settings |
| **bearer_token_sending_methods**  list / elements=string | How to send token to the server.  **Choices:**   - `"authorizationHeader"` - `"query"` |
| **openid_provider_id**  string | OAuth authorization server identifier. |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **description**  string | Description of the API. |
| **display_name**  string | API Name to be displayed. It must be 1 to 300 characters long. |
| **format**  string | Format of the Content in which the API is getting imported.  **Choices:**   - `"wadl-xml"` - `"wadl-link-json"` - `"swagger-json"` - `"swagger-link-json"` - `"wsdl"` - `"wsdl-link"` - `"openapi"` - `"openapi+json"` - `"openapi-link"` |
| **is_current**  boolean | Indicates if API revision is current api revision.  **Choices:**   - `false` - `true` |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **path**  string | Relative URL uniquely identifying this API. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **protocols**  list / elements=string | Describes on which protocols the operations in this API can be invoked.  **Choices:**   - `"http"` - `"https"` |
| **resource_group**  string / required | The name of the resource group. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **service_name**  string / required | The name of the API Management service. |
| **service_url**  string | Absolute URL of the backend service implementing this API  Cannot be more than 2000 characters long. |
| **source_api_id**  string | API identifier of the source API. |
| **state**  string | State of the Api.  Use `present` to create or update an Api and `absent` to delete it.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **subscription_key_parameter_names**  dictionary | Protocols over which API is made available. |
| **header**  string | Subscription key header name. |
| **query**  string | Subscription key query string parameter name. |
| **subscription_required**  boolean | Specifies whether an API or Product subscription is required for accessing the API.  **Choices:**   - `false` - `true` |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **type**  string | Type of API  **Choices:**   - `"http"` - `"soap"` |
| **value**  string | Content value when Importing an API. |
| **wsdl_selector**  dictionary | Criteria to limit import of WSDL to a subset of the document. |
| **wsdl_endpoint_name**  string | Name of endpoint(port) to import from WSDL. |
| **wsdl_service_name**  string | Name of service to import from WSDL. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_apimanagement_module.md#id5)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_apimanagement_module.md#id6)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_apimanagement_module.md#id7)

```yaml+jinja
- name: Create a new API instance
  azure_rm_apimanagement:
    resource_group: 'myResourceGroup'
    service_name: myService
    api_id: testApi
    description: testDescription
    display_name: TestAPI
    service_url: 'http://testapi.example.net/api'
    path: myapiPath
    protocols:
      - https
- name: Update an existing API instance.
  azure_rm_apimanagement:
    resource_group: myResourceGroup
    service_name: myService
    api_id: testApi
    display_name: newTestAPI
    service_url: 'http://testapi.example.net/api'
    path: myapiPath
    protocols:
      - https
- name: ApiManagementDeleteApi
  azure_rm_apimanagement:
    resource_group: myResourceGroup
    service_name: myService
    api_id: testApi
    state: absent
```

## [Return Values](azure_rm_apimanagement_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | Resource ID.  **Returned:** always |

### Authors

- Sakar Mehra (@sakar97)
- Nikhil Patne (@nikhilpatne)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
