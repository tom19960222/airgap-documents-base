---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_appgateway module – Manage Application Gateway instance"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_appgateway_module.html
fetched_at: 2026-07-28T01:12:13+00:00
---
# azure.azcollection.azure_rm_appgateway module – Manage Application Gateway instance

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
> see [Requirements](azure_rm_appgateway_module.md#ansible-collections-azure-azcollection-azure-rm-appgateway-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_appgateway`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_appgateway_module.md#synopsis)
- [Requirements](azure_rm_appgateway_module.md#requirements)
- [Parameters](azure_rm_appgateway_module.md#parameters)
- [Notes](azure_rm_appgateway_module.md#notes)
- [See Also](azure_rm_appgateway_module.md#see-also)
- [Examples](azure_rm_appgateway_module.md#examples)
- [Return Values](azure_rm_appgateway_module.md#return-values)

## [Synopsis](azure_rm_appgateway_module.md#id1)

- Create, update and delete instance of Application Gateway.

## [Requirements](azure_rm_appgateway_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_appgateway_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  **Choices:**   - `false` - `true` ← (default) |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **authentication_certificates**  list / elements=dictionary | Authentication certificates of the application gateway resource. |
| **data**  string | Certificate public data - base64 encoded pfx. |
| **name**  string | Name of the resource that is unique within a resource group. This name can be used to access the resource. |
| **autoscale_configuration**  dictionary  *added in azure.azcollection 1.15.0* | Autoscale configuration of the application gateway resource. |
| **max_capacity**  integer | Upper bound on number of Application Gateway capacity. |
| **min_capacity**  integer | Lower bound on number of Application Gateway capacity. |
| **backend_address_pools**  list / elements=dictionary | List of backend address pool of the application gateway resource. |
| **backend_addresses**  list / elements=dictionary | List of backend addresses. |
| **fqdn**  string | Fully qualified domain name (FQDN). |
| **ip_address**  string | IP address. |
| **name**  string | Resource that is unique within a resource group. This name can be used to access the resource. |
| **backend_http_settings_collection**  list / elements=dictionary | Backend http settings of the application gateway resource. |
| **affinity_cookie_name**  string | Cookie name to use for the affinity cookie. |
| **authentication_certificates**  list / elements=dictionary | List of references to application gateway authentication certificates.  Applicable only when `cookie_based_affinity` is enabled, otherwise quietly ignored. |
| **id**  string | Resource ID. |
| **connection_draining**  dictionary  *added in azure.azcollection 1.15.0* | Connection draining of the backend http settings resource. |
| **drain_timeout_in_sec**  integer | The number of seconds connection draining is active. Acceptable values are from 1 second to 3600 seconds. |
| **enabled**  boolean | Whether connection draining is enabled or not.  **Choices:**   - `false` - `true` |
| **cookie_based_affinity**  string | Cookie based affinity.  **Choices:**   - `"enabled"` - `"disabled"` |
| **host_name**  string | Host header to be sent to the backend servers. |
| **name**  string | Name of the resource that is unique within a resource group. This name can be used to access the resource. |
| **path**  string | Path which should be used as a prefix for all `http` requests.  Null means no path will be prefixed. Default value is null. |
| **pick_host_name_from_backend_address**  boolean | Whether host header should be picked from the host name of the backend server. Default value is false.  **Choices:**   - `false` - `true` |
| **port**  integer | The destination port on the backend. |
| **probe**  any | Probe resource of an application gateway. |
| **protocol**  string | The protocol used to communicate with the backend.  **Choices:**   - `"http"` - `"https"` |
| **request_timeout**  integer | Request timeout in seconds.  Application Gateway will fail the request if response is not received within RequestTimeout.  Acceptable values are from 1 second to 86400 seconds. |
| **trusted_root_certificates**  list / elements=any  *added in azure.azcollection 1.15.0* | Array of references to application gateway trusted root certificates.  Can be the name of the trusted root certificate or full resource ID. |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **enable_http2**  boolean  *added in azure.azcollection 1.15.0* | Whether HTTP2 is enabled on the application gateway resource.  **Choices:**   - `false` ← (default) - `true` |
| **frontend_ip_configurations**  list / elements=dictionary | Frontend IP addresses of the application gateway resource. |
| **name**  string | Name of the resource that is unique within a resource group. This name can be used to access the resource. |
| **private_ip_address**  string | PrivateIPAddress of the network interface IP Configuration. |
| **private_ip_allocation_method**  string | PrivateIP allocation method.  **Choices:**   - `"static"` - `"dynamic"` |
| **public_ip_address**  any | Reference of the PublicIP resource. |
| **subnet**  dictionary | Reference of the subnet resource. |
| **id**  string | Full ID of the subnet resource. Required if *name* and *virtual_network_name* are not provided. |
| **name**  string | Name of the subnet. Only used if *virtual_network_name* is also provided. |
| **virtual_network_name**  string | Name of the virtual network. Only used if *name* is also provided. |
| **frontend_ports**  list / elements=dictionary | List of frontend ports of the application gateway resource. |
| **name**  string | Name of the resource that is unique within a resource group. This name can be used to access the resource. |
| **port**  string | Frontend port. |
| **gateway_ip_configurations**  list / elements=dictionary | List of subnets used by the application gateway. |
| **name**  string | Name of the resource that is unique within a resource group. This name can be used to access the resource. |
| **subnet**  dictionary | Reference of the subnet resource. A subnet from where application gateway gets its private address. |
| **id**  string | Full ID of the subnet resource. Required if *name* and *virtual_network_name* are not provided. |
| **name**  string | Name of the subnet. Only used if *virtual_network_name* is also provided. |
| **virtual_network_name**  string | Name of the virtual network. Only used if *name* is also provided. |
| **gateway_state**  string | Start or Stop the application gateway. When specified, no updates will occur to the gateway.  **Choices:**   - `"started"` - `"stopped"` |
| **http_listeners**  list / elements=dictionary | List of HTTP listeners of the application gateway resource. |
| **frontend_ip_configuration**  any | Frontend IP configuration resource of an application gateway. |
| **frontend_port**  any | Frontend port resource of an application gateway. |
| **host_name**  string | Host name of `http` listener. |
| **name**  string | Name of the resource that is unique within a resource group. This name can be used to access the resource. |
| **protocol**  string | Protocol of the `http` listener.  **Choices:**   - `"http"` - `"https"` |
| **require_server_name_indication**  boolean | Applicable only if *protocol* is `https`. Enables SNI for multi-hosting.  **Choices:**   - `false` - `true` |
| **ssl_certificate**  any | SSL certificate resource of an application gateway. |
| **location**  string | Resource location. If not set, location from the resource group will be used as default. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string / required | The name of the application gateway. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **probes**  list / elements=dictionary | Probes available to the application gateway resource. |
| **host**  string | Host name to send the *probe* to. |
| **interval**  integer | The probing interval in seconds.  This is the time interval between two consecutive probes.  Acceptable values are from 1 second to 86400 seconds. |
| **name**  string | Name of the *probe* that is unique within an Application Gateway. |
| **path**  string | Relative path of *probe*.  Valid path starts from ‘/’.  Probe is sent to <Protocol>://<host>:<port><path>. |
| **pick_host_name_from_backend_http_settings**  boolean | Whether host header should be picked from the host name of the backend HTTP settings. Default value is false.  **Choices:**   - `false` ← (default) - `true` |
| **protocol**  string | The protocol used for the *probe*.  **Choices:**   - `"http"` - `"https"` |
| **timeout**  integer | The probe timeout in seconds.  Probe marked as failed if valid response is not received with this timeout period.  Acceptable values are from 1 second to 86400 seconds. |
| **unhealthy_threshold**  integer | The *probe* retry count.  Backend server is marked down after consecutive probe failure count reaches UnhealthyThreshold.  Acceptable values are from 1 second to 20. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **redirect_configurations**  list / elements=dictionary | Redirect configurations of the application gateway resource. |
| **include_path**  boolean | Include path in the redirected url.  **Choices:**   - `false` - `true` |
| **include_query_string**  boolean | Include query string in the redirected url.  **Choices:**   - `false` - `true` |
| **name**  string | Name of the resource that is unique within a resource group. |
| **path_rules**  list / elements=dictionary  *added in azure.azcollection 1.10.0* | List of URL path rules within a c(path_based_routing) rule to which the redirect is bound. |
| **name**  string | Name of the URL rule. |
| **path_map_name**  string | Name of URL path map. |
| **redirect_type**  string | Redirection type.  **Choices:**   - `"permanent"` - `"found"` - `"see_other"` - `"temporary"` |
| **request_routing_rules**  list / elements=string  *added in azure.azcollection 1.10.0* | List of c(basic) request routing rule names within the application gateway to which the redirect is bound. |
| **target_listener**  string | Reference to a listener to redirect the request to. |
| **url_path_maps**  list / elements=string  *added in azure.azcollection 1.10.0* | List of URL path map names (c(path_based_routing) rules) within the application gateway to which the redirect is bound. |
| **request_routing_rules**  list / elements=dictionary | List of request routing rules of the application gateway resource. |
| **backend_address_pool**  any | Backend address pool resource of the application gateway. Not used if *rule_type* is `path_based_routing`. |
| **backend_http_settings**  any | Backend `http` settings resource of the application gateway. |
| **http_listener**  any | Http listener resource of the application gateway. |
| **name**  string | Name of the resource that is unique within a resource group. This name can be used to access the resource. |
| **redirect_configuration**  any | Redirect configuration resource of the application gateway. |
| **rewrite_rule_set**  any  *added in azure.azcollection 1.11.0* | Rewrite rule set for the path map.  Can be the name of the rewrite rule set or full resource ID. |
| **rule_type**  string | Rule type.  **Choices:**   - `"basic"` - `"path_based_routing"` |
| **url_path_map**  any | URL path map resource of the application gateway. Required if *rule_type* is `path_based_routing`. |
| **resource_group**  string / required | The name of the resource group. |
| **rewrite_rule_sets**  list / elements=dictionary  *added in azure.azcollection 1.11.0* | List of rewrite configurations for the application gateway resource. |
| **name**  string / required | Name of the rewrite rule set. |
| **rewrite_rules**  list / elements=dictionary / required | List of rewrite rules. |
| **action_set**  dictionary / required | Set of actions to be done as part of the rewrite rule. |
| **request_header_configurations**  list / elements=dictionary | List of actions to be taken on request headers.  **Default:** `[]` |
| **header_name**  string / required | Name of the header. |
| **header_value**  string | Value of the header.  Leave the parameter unset to remove the header.  **Default:** `""` |
| **response_header_configurations**  list / elements=dictionary | List of actions to be taken on response headers.  **Default:** `[]` |
| **header_name**  string / required | Name of the header. |
| **header_value**  string | Value of the header.  Leave the parameter unset to remove the header.  **Default:** `""` |
| **url_configuration**  dictionary | Action to be taken on the URL. |
| **modified_path**  string | Value to which the URL path will be rewriten.  Leave parameter unset to keep the original URL path. |
| **modified_query_string**  string | Value to which the URL query string will be rewriten.  Leave parameter unset to keep the original URL query string. |
| **reroute**  boolean | If set to true, will re-evaluate the path map provided in path-based request routing rules using modified path.  **Choices:**   - `false` ← (default) - `true` |
| **conditions**  list / elements=dictionary | Conditions based on which the action set execution will be evaluated.  **Default:** `[]` |
| **ignore_case**  boolean | Setting this value to true will force the pattern to do a case in-sensitive comparison.  **Choices:**   - `false` - `true` ← (default) |
| **negate**  boolean | Setting this value to true will force to check the negation of the condition given by the user.  **Choices:**   - `false` ← (default) - `true` |
| **pattern**  string / required | The pattern, either fixed string or regular expression, that evaluates the truthfulness of the condition. |
| **variable**  string / required | The parameter for the condition. |
| **name**  string / required | Name of the rewrite rule. |
| **rule_sequence**  integer / required | Sequence of the rule that determines the order of execution within the set. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **sku**  dictionary | SKU of the application gateway resource. |
| **capacity**  integer | Capacity (instance count) of an application gateway. |
| **name**  string | Name of an application gateway SKU.  **Choices:**   - `"standard_small"` - `"standard_medium"` - `"standard_large"` - `"standard_v2"` - `"waf_medium"` - `"waf_large"` - `"waf_v2"` |
| **tier**  string | Tier of an application gateway.  **Choices:**   - `"standard"` - `"standard_v2"` - `"waf"` - `"waf_v2"` |
| **ssl_certificates**  list / elements=dictionary | SSL certificates of the application gateway resource. |
| **data**  string | Base-64 encoded pfx certificate.  Only applicable in PUT Request. |
| **name**  string | Name of the resource that is unique within a resource group. This name can be used to access the resource. |
| **password**  string | Password for the pfx file specified in *data*.  Only applicable in PUT request. |
| **ssl_policy**  dictionary | SSL policy of the application gateway resource. |
| **cipher_suites**  list / elements=string | List of SSL cipher suites to be enabled in the specified order to application gateway.  **Choices:**   - `"tls_ecdhe_rsa_with_aes_256_gcm_sha384"` - `"tls_ecdhe_rsa_with_aes_128_gcm_sha256"` - `"tls_ecdhe_rsa_with_aes_256_cbc_sha384"` - `"tls_ecdhe_rsa_with_aes_128_cbc_sha256"` - `"tls_ecdhe_rsa_with_aes_256_cbc_sha"` - `"tls_ecdhe_rsa_with_aes_128_cbc_sha"` - `"tls_dhe_rsa_with_aes_256_gcm_sha384"` - `"tls_dhe_rsa_with_aes_128_gcm_sha256"` - `"tls_dhe_rsa_with_aes_256_cbc_sha"` - `"tls_dhe_rsa_with_aes_128_cbc_sha"` - `"tls_rsa_with_aes_256_gcm_sha384"` - `"tls_rsa_with_aes_128_gcm_sha256"` - `"tls_rsa_with_aes_256_cbc_sha256"` - `"tls_rsa_with_aes_128_cbc_sha256"` - `"tls_rsa_with_aes_256_cbc_sha"` - `"tls_rsa_with_aes_128_cbc_sha"` - `"tls_ecdhe_ecdsa_with_aes_256_gcm_sha384"` - `"tls_ecdhe_ecdsa_with_aes_128_gcm_sha256"` - `"tls_ecdhe_ecdsa_with_aes_256_cbc_sha384"` - `"tls_ecdhe_ecdsa_with_aes_128_cbc_sha256"` - `"tls_ecdhe_ecdsa_with_aes_256_cbc_sha"` - `"tls_ecdhe_ecdsa_with_aes_128_cbc_sha"` - `"tls_dhe_dss_with_aes_256_cbc_sha256"` - `"tls_dhe_dss_with_aes_128_cbc_sha256"` - `"tls_dhe_dss_with_aes_256_cbc_sha"` - `"tls_dhe_dss_with_aes_128_cbc_sha"` - `"tls_rsa_with_3des_ede_cbc_sha"` - `"tls_dhe_dss_with_3des_ede_cbc_sha"` |
| **disabled_ssl_protocols**  list / elements=string | List of SSL protocols to be disabled on application gateway.  **Choices:**   - `"tls_v1_0"` - `"tls_v1_1"` - `"tls_v1_2"` |
| **min_protocol_version**  string | Minimum version of SSL protocol to be supported on application gateway.  **Choices:**   - `"tls_v1_0"` - `"tls_v1_1"` - `"tls_v1_2"` |
| **policy_name**  string | Name of Ssl `predefined` policy.  **Choices:**   - `"ssl_policy20150501"` - `"ssl_policy20170401"` - `"ssl_policy20170401_s"` |
| **policy_type**  string | Type of SSL Policy.  **Choices:**   - `"predefined"` - `"custom"` |
| **state**  string | Assert the state of the application gateway. Use `present` to create or update and `absent` to delete.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **trusted_root_certificates**  list / elements=dictionary  *added in azure.azcollection 1.15.0* | Trusted Root certificates of the application gateway resource. |
| **data**  string | Certificate public data. |
| **key_vault_secret_id**  string | Secret Id of (base-64 encoded unencrypted pfx) ‘Secret’ or ‘Certificate’ object stored in KeyVault.  **Default:** `""` |
| **name**  string | Name of the trusted root certificate that is unique within an Application Gateway. |
| **url_path_maps**  list / elements=dictionary | List of URL path maps of the application gateway resource. |
| **default_backend_address_pool**  string | Backend address pool resource of the application gateway which will be used if no path matches occur.  Mutually exclusive with *default_redirect_configuration*. |
| **default_backend_http_settings**  string | Backend http settings resource of the application gateway; used with *default_backend_address_pool*. |
| **default_redirect_configuration**  string  *added in azure.azcollection 1.10.0* | Name of redirect configuration resource of the application gateway which will be used if no path matches occur.  Mutually exclusive with *default_backend_address_pool*. |
| **default_rewrite_rule_set**  string  *added in azure.azcollection 1.11.0* | Default rewrite rule set for the path map.  Can be the name of the rewrite rule set or full resource ID. |
| **name**  string | Name of the resource that is unique within the application gateway. This name can be used to access the resource. |
| **path_rules**  list / elements=dictionary | List of URL path rules. |
| **backend_address_pool**  string | Backend address pool resource of the application gateway which will be used if the path is matched.  Mutually exclusive with *redirect_configuration*. |
| **backend_http_settings**  string | Backend http settings resource of the application gateway; used for the path’s *backend_address_pool*. |
| **name**  string | Name of the resource that is unique within the path map. |
| **paths**  list / elements=string | List of paths. |
| **redirect_configuration**  string  *added in azure.azcollection 1.10.0* | Name of redirect configuration resource of the application gateway which will be used if the path is matched.  Mutually exclusive with *backend_address_pool*. |
| **rewrite_rule_set**  string  *added in azure.azcollection 1.11.0* | Rewrite rule set for the path map.  Can be the name of the rewrite rule set or full resource ID. |
| **web_application_firewall_configuration**  dictionary  *added in azure.azcollection 1.15.0* | Web application firewall configuration of the application gateway reosurce. |
| **disabled_rule_groups**  list / elements=dictionary | The disabled rule groups.  **Default:** `[]` |
| **rule_group_name**  string | The name of the rule group that will be disabled. |
| **rules**  list / elements=integer | The list of rules that will be disabled. If null, all rules of the rule group will be disabled.  **Default:** `[]` |
| **enabled**  boolean | Whether the web application firewall is enabled or not.  **Choices:**   - `false` - `true` |
| **exclusions**  list / elements=dictionary | The exclusion list.  **Default:** `[]` |
| **match_variable**  string | The variable to be excluded. |
| **selector**  string | When match_variable is a collection, operator used to specify which elements in the collection this exclusion applies to. |
| **selector_match_operator**  string | When match_variable is a collection, operate on the selector to specify which elements in the collection this exclusion applies to. |
| **file_upload_limit_in_mb**  integer | Maximum file upload size in Mb for WAF. |
| **firewall_mode**  string | Web application firewall mode.  **Choices:**   - `"Detection"` - `"Prevention"` |
| **max_request_body_size**  integer | Maximum request body size for WAF. |
| **max_request_body_size_in_kb**  integer | Maximum request body size in Kb for WAF. |
| **request_body_check**  boolean | Whether allow WAF to check request Body.  **Choices:**   - `false` - `true` |
| **rule_set_type**  string | The type of the web application firewall rule set.  Possible values are ‘OWASP’.  **Choices:**   - `"OWASP"` |
| **rule_set_version**  string | The version of the rule set type. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_appgateway_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_appgateway_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_appgateway_module.md#id6)

```yaml+jinja
- name: Create instance of Application Gateway
  azure_rm_appgateway:
    resource_group: myResourceGroup
    name: myAppGateway
    sku:
      name: standard_small
      tier: standard
      capacity: 2
    gateway_ip_configurations:
      - subnet:
          id: "{{ subnet_id }}"
        name: app_gateway_ip_config
    frontend_ip_configurations:
      - subnet:
          id: "{{ subnet_id }}"
        name: sample_gateway_frontend_ip_config
    frontend_ports:
      - port: 90
        name: ag_frontend_port
    backend_address_pools:
      - backend_addresses:
          - ip_address: 10.0.0.4
        name: test_backend_address_pool
    backend_http_settings_collection:
      - port: 80
        protocol: http
        cookie_based_affinity: enabled
        connection_draining:
          drain_timeout_in_sec: 60
          enabled: true
        name: sample_appgateway_http_settings
    http_listeners:
      - frontend_ip_configuration: sample_gateway_frontend_ip_config
        frontend_port: ag_frontend_port
        name: sample_http_listener
    request_routing_rules:
      - rule_type: basic
        backend_address_pool: test_backend_address_pool
        backend_http_settings: sample_appgateway_http_settings
        http_listener: sample_http_listener
        name: rule1

- name: Create instance of Application Gateway with custom trusted root certificate
  azure_rm_appgateway:
    resource_group: myResourceGroup
    name: myAppGateway
    sku:
      name: standard_small
      tier: standard
      capacity: 2
    gateway_ip_configurations:
      - subnet:
          id: "{{ subnet_id }}"
        name: app_gateway_ip_config
    frontend_ip_configurations:
      - subnet:
          id: "{{ subnet_id }}"
        name: sample_gateway_frontend_ip_config
    frontend_ports:
      - port: 90
        name: ag_frontend_port
    trusted_root_certificates:
      - name: "root_cert"
        key_vault_secret_id: "https://kv/secret"
    backend_address_pools:
      - backend_addresses:
          - ip_address: 10.0.0.4
        name: test_backend_address_pool
    backend_http_settings_collection:
      - port: 80
        protocol: http
        cookie_based_affinity: enabled
        connection_draining:
          drain_timeout_in_sec: 60
          enabled: true
        name: sample_appgateway_http_settings
        trusted_root_certificates:
          - "root_cert"
    http_listeners:
      - frontend_ip_configuration: sample_gateway_frontend_ip_config
        frontend_port: ag_frontend_port
        name: sample_http_listener
    request_routing_rules:
      - rule_type: basic
        backend_address_pool: test_backend_address_pool
        backend_http_settings: sample_appgateway_http_settings
        http_listener: sample_http_listener
        name: rule1

- name: Create instance of Application Gateway by looking up virtual network and subnet
  azure_rm_appgateway:
    resource_group: myResourceGroup
    name: myAppGateway
    sku:
      name: standard_small
      tier: standard
      capacity: 2
    gateway_ip_configurations:
      - subnet:
          name: default
          virtual_network_name: my-vnet
        name: app_gateway_ip_config
    frontend_ip_configurations:
      - subnet:
          name: default
          virtual_network_name: my-vnet
        name: sample_gateway_frontend_ip_config
    frontend_ports:
      - port: 90
        name: ag_frontend_port
    backend_address_pools:
      - backend_addresses:
          - ip_address: 10.0.0.4
        name: test_backend_address_pool
    backend_http_settings_collection:
      - port: 80
        protocol: http
        cookie_based_affinity: enabled
        name: sample_appgateway_http_settings
    http_listeners:
      - frontend_ip_configuration: sample_gateway_frontend_ip_config
        frontend_port: ag_frontend_port
        name: sample_http_listener
    request_routing_rules:
      - rule_type: basic
        backend_address_pool: test_backend_address_pool
        backend_http_settings: sample_appgateway_http_settings
        http_listener: sample_http_listener
        name: rule1

- name: Create instance of Application Gateway with path based rules
  azure_rm_appgateway:
    resource_group: myResourceGroup
    name: myAppGateway
    sku:
      name: standard_small
      tier: standard
      capacity: 2
    gateway_ip_configurations:
      - subnet:
          id: "{{ subnet_id }}"
        name: app_gateway_ip_config
    frontend_ip_configurations:
      - subnet:
          id: "{{ subnet_id }}"
        name: sample_gateway_frontend_ip_config
    frontend_ports:
      - port: 90
        name: ag_frontend_port
    backend_address_pools:
      - backend_addresses:
          - ip_address: 10.0.0.4
        name: test_backend_address_pool
    backend_http_settings_collection:
      - port: 80
        protocol: http
        cookie_based_affinity: enabled
        name: sample_appgateway_http_settings
    http_listeners:
      - frontend_ip_configuration: sample_gateway_frontend_ip_config
        frontend_port: ag_frontend_port
        name: sample_http_listener
    request_routing_rules:
      - rule_type: path_based_routing
        http_listener: sample_http_listener
        name: rule1
        url_path_map: path_mappings
    url_path_maps:
      - name: path_mappings
        default_backend_address_pool: test_backend_address_pool
        default_backend_http_settings: sample_appgateway_http_settings
        path_rules:
          - name: path_rules
            backend_address_pool: test_backend_address_pool
            backend_http_settings: sample_appgateway_http_settings
            paths:
              - "/abc"
              - "/123/*"

- name: Create instance of Application Gateway with complex routing and redirect rules
  azure_rm_appgateway:
    resource_group: myResourceGroup
    name: myComplexAppGateway
    sku:
      name: standard_small
      tier: standard
      capacity: 2
    ssl_policy:
      policy_type: "predefined"
      policy_name: "ssl_policy20170401_s"
    ssl_certificates:
      - name: ssl_cert
        password: your-password
        data: "{{ lookup('file', 'certfile') }}"
    gateway_ip_configurations:
      - subnet:
          id: "{{ subnet_output.state.id }}"
          name: app_gateway_ip_config
    frontend_ip_configurations:
      - subnet:
          id: "{{ subnet_output.state.id }}"
          name: sample_gateway_frontend_ip_config
    frontend_ports:
      - name: "inbound-http"
        port: 80
      - name: "inbound-https"
        port: 443
    backend_address_pools:
      - name: test_backend_address_pool1
        backend_addresses:
          - ip_address: 10.0.0.1
      - name: test_backend_address_pool2
        backend_addresses:
          - ip_address: 10.0.0.2
    backend_http_settings_collection:
      - name: "http-profile1"
        port: 443
        protocol: https
        pick_host_name_from_backend_address: true
        probe: "http-probe1"
        cookie_based_affinity: "Disabled"
      - name: "http-profile2"
        port: 8080
        protocol: http
        pick_host_name_from_backend_address: true
        probe: "http-probe2"
        cookie_based_affinity: "Disabled"
    http_listeners:
      - name: "inbound-http"
        protocol: "http"
        frontend_ip_configuration: "sample_gateway_frontend_ip_config"
        frontend_port: "inbound-http"
      - name: "inbound-traffic1"
        protocol: "https"
        frontend_ip_configuration: "sample_gateway_frontend_ip_config"
        frontend_port: "inbound-https"
        host_name: "traffic1.example.com"
        require_server_name_indication: true
        ssl_certificate: "ssl_cert"
      - name: "inbound-traffic2"
        protocol: "https"
        frontend_ip_configuration: "sample_gateway_frontend_ip_config"
        frontend_port: "inbound-https"
        host_name: "traffic2.example.com"
        require_server_name_indication: true
        ssl_certificate: "ssl_cert"
    url_path_maps:
      - name: "path_mappings"
        default_redirect_configuration: "redirect-traffic1"
        path_rules:
          - name: "path_rules"
            backend_address_pool: "test_backend_address_pool1"
            backend_http_settings: "http-profile1"
            paths:
              - "/abc"
              - "/123/*"
    request_routing_rules:
      - name: "app-routing1"
        rule_type: "basic"
        http_listener: "inbound-traffic1"
        backend_address_pool: "test_backend_address_pool2"
        backend_http_settings: "http-profile1"
      - name: "app-routing2"
        rule_type: "path_based_routing"
        http_listener: "inbound-traffic2"
        url_path_map: "path_mappings"
      - name: "redirect-routing"
        rule_type: "basic"
        http_listener: "inbound-http"
        redirect_configuration: "redirect-http"
    probes:
      - name: "http-probe1"
        interval: 30
        path: "/abc"
        protocol: "https"
        pick_host_name_from_backend_http_settings: true
        timeout: 30
        unhealthy_threshold: 2
      - name: "http-probe2"
        interval: 30
        path: "/xyz"
        protocol: "http"
        pick_host_name_from_backend_http_settings: true
        timeout: 30
        unhealthy_threshold: 2
    redirect_configurations:
      - name: "redirect-http"
        redirect_type: "permanent"
        target_listener: "inbound-traffic1"
        include_path: true
        include_query_string: true
        request_routing_rules:
          - "redirect-routing"
      - name: "redirect-traffic1"
        redirect_type: "found"
        target_listener: "inbound-traffic1"
        include_path: true
        include_query_string: true
        url_path_maps:
          - "path_mappings"

- name: Create v2 instance of Application Gateway with rewrite rules
  azure_rm_appgateway:
    resource_group: myResourceGroup
    name: myV2AppGateway
    sku:
      name: standard_v2
      tier: standard_v2
      capacity: 2
    ssl_policy:
      policy_type: predefined
      policy_name: ssl_policy20170401_s
    ssl_certificates:
      - name: ssl_cert
        password: your-password
        data: "{{ lookup('file', ssl_cert) }}"
    gateway_ip_configurations:
      - subnet:
          id: "{{ subnet_output.state.id }}"
        name: app_gateway_ip_config
    frontend_ip_configurations:
      - name: "public-inbound-ip"
        public_ip_address: my-appgw-pip
    frontend_ports:
      - name: "inbound-http"
        port: 80
      - name: "inbound-https"
        port: 443
    backend_address_pools:
      - name: test_backend_address_pool1
        backend_addresses:
          - ip_address: 10.0.0.1
      - name: test_backend_address_pool2
        backend_addresses:
          - ip_address: 10.0.0.2
    backend_http_settings_collection:
      - name: "http-profile1"
        port: 443
        protocol: https
        pick_host_name_from_backend_address: true
        probe: "http-probe1"
        cookie_based_affinity: "Disabled"
      - name: "http-profile2"
        port: 8080
        protocol: http
        pick_host_name_from_backend_address: true
        probe: "http-probe2"
        cookie_based_affinity: "Disabled"
    http_listeners:
      - name: "inbound-http"
        protocol: "http"
        frontend_ip_configuration: "public-inbound-ip"
        frontend_port: "inbound-http"
      - name: "inbound-traffic1"
        protocol: "https"
        frontend_ip_configuration: "public-inbound-ip"
        frontend_port: "inbound-https"
        host_name: "traffic1.example.com"
        require_server_name_indication: true
        ssl_certificate: "ssl_cert"
      - name: "inbound-traffic2"
        protocol: "https"
        frontend_ip_configuration: "public-inbound-ip"
        frontend_port: "inbound-https"
        host_name: "traffic2.example.com"
        require_server_name_indication: true
        ssl_certificate: "ssl_cert"
    url_path_maps:
      - name: "path_mappings"
        default_redirect_configuration: "redirect-traffic1"
        default_rewrite_rule_set: "configure-headers"
        path_rules:
          - name: "path_rules"
            backend_address_pool: "test_backend_address_pool1"
            backend_http_settings: "http-profile1"
            paths:
              - "/abc"
              - "/123/*"
    request_routing_rules:
      - name: "app-routing1"
        rule_type: "basic"
        http_listener: "inbound-traffic1"
        backend_address_pool: "test_backend_address_pool2"
        backend_http_settings: "http-profile1"
        rewrite_rule_set: "configure-headers"
      - name: "app-routing2"
        rule_type: "path_based_routing"
        http_listener: "inbound-traffic2"
        url_path_map: "path_mappings"
      - name: "redirect-routing"
        rule_type: "basic"
        http_listener: "inbound-http"
        redirect_configuration: "redirect-http"
    rewrite_rule_sets:
      - name: "configure-headers"
        rewrite_rules:
          - name: "add-security-response-header"
            rule_sequence: 1
            action_set:
              response_header_configurations:
                - header_name: "Strict-Transport-Security"
                  header_value: "max-age=31536000"
          - name: "remove-backend-response-headers"
            rule_sequence: 2
            action_set:
              response_header_configurations:
                - header_name: "Server"
                - header_name: "X-Powered-By"
          - name: "set-custom-header-condition"
            rule_sequence: 3
            conditions:
              - variable: "var_client_ip"
                pattern: "1.1.1.1"
              - variable: "http_req_Authorization"
                pattern: "12345"
                ignore_case: false
            action_set:
              request_header_configurations:
                - header_name: "Foo"
                  header_value: "Bar"
    probes:
      - name: "http-probe1"
        interval: 30
        path: "/abc"
        protocol: "https"
        pick_host_name_from_backend_http_settings: true
        timeout: 30
        unhealthy_threshold: 2
      - name: "http-probe2"
        interval: 30
        path: "/xyz"
        protocol: "http"
        pick_host_name_from_backend_http_settings: true
        timeout: 30
        unhealthy_threshold: 2
    redirect_configurations:
      - name: "redirect-http"
        redirect_type: "permanent"
        target_listener: "inbound-traffic1"
        include_path: true
        include_query_string: true
        request_routing_rules:
          - "redirect-routing"
      - name: "redirect-traffic1"
        redirect_type: "found"
        target_listener: "inbound-traffic1"
        include_path: true
        include_query_string: true
        url_path_maps:
          - "path_mappings"

- name: Create instance of Application Gateway with autoscale configuration
  azure_rm_appgateway:
    resource_group: myResourceGroup
    name: myAppGateway
    sku:
      name: standard_small
      tier: standard
    autoscale_configuration:
      max_capacity: 2
      min_capacity: 1
    gateway_ip_configurations:
      - subnet:
          id: "{{ subnet_id }}"
        name: app_gateway_ip_config
    frontend_ip_configurations:
      - subnet:
          id: "{{ subnet_id }}"
        name: sample_gateway_frontend_ip_config
    frontend_ports:
      - port: 90
        name: ag_frontend_port
    backend_address_pools:
      - backend_addresses:
          - ip_address: 10.0.0.4
        name: test_backend_address_pool
    backend_http_settings_collection:
      - port: 80
        protocol: http
        cookie_based_affinity: enabled
        name: sample_appgateway_http_settings
    http_listeners:
      - frontend_ip_configuration: sample_gateway_frontend_ip_config
        frontend_port: ag_frontend_port
        name: sample_http_listener
    request_routing_rules:
      - rule_type: basic
        backend_address_pool: test_backend_address_pool
        backend_http_settings: sample_appgateway_http_settings
        http_listener: sample_http_listener
        name: rule1

- name: Create instance of Application Gateway waf_v2 with waf configuration
  azure_rm_appgateway:
    resource_group: myResourceGroup
    name: myAppGateway
    sku:
      name: waf_v2
      tier: waf_v2
      capacity: 2
    gateway_ip_configurations:
      - subnet:
          id: "{{ subnet_id }}"
        name: app_gateway_ip_config
    frontend_ip_configurations:
      - subnet:
          id: "{{ subnet_id }}"
        name: sample_gateway_frontend_ip_config
    frontend_ports:
      - port: 90
        name: ag_frontend_port
    backend_address_pools:
      - backend_addresses:
          - ip_address: 10.0.0.4
        name: test_backend_address_pool
    backend_http_settings_collection:
      - port: 80
        protocol: http
        cookie_based_affinity: enabled
        name: sample_appgateway_http_settings
    http_listeners:
      - frontend_ip_configuration: sample_gateway_frontend_ip_config
        frontend_port: ag_frontend_port
        name: sample_http_listener
    request_routing_rules:
      - rule_type: basic
        backend_address_pool: test_backend_address_pool
        backend_http_settings: sample_appgateway_http_settings
        http_listener: sample_http_listener
        name: rule1
    web_application_firewall_configuration:
      - enabled: true
        firewall_mode: Detection
        rule_set_type: OWASP
        rule_set_version: 3.0
        request_body_check: true
        max_request_body_size_in_kb: 128
        file_upload_limit_in_mb: 100

- name: Stop an Application Gateway instance
  azure_rm_appgateway:
    resource_group: myResourceGroup
    name: myAppGateway
    gateway_state: stopped

- name: Start an Application Gateway instance
  azure_rm_appgateway:
    resource_group: myResourceGroup
    name: myAppGateway
    gateway_state: started
```

## [Return Values](azure_rm_appgateway_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | Application gateway resource ID.  **Returned:** always  **Sample:** `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Network/applicationGateways/myAppGw"` |
| **location**  string | Location of application gateway.  **Returned:** always  **Sample:** `"centralus"` |
| **name**  string | Name of application gateway.  **Returned:** always  **Sample:** `"myAppGw"` |
| **operational_state**  string | Operating state of application gateway.  **Returned:** always  **Sample:** `"Running"` |
| **provisioning_state**  string | Provisioning state of application gateway.  **Returned:** always  **Sample:** `"Succeeded"` |
| **resource_group**  string | Name of resource group.  **Returned:** always  **Sample:** `"myResourceGroup"` |

### Authors

- Zim Kalinowski (@zikalino)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
