---
collection: ansible
version: "6"
title: "azure.azcollection.azure_rm_loadbalancer module – Manage Azure load balancers"
source_url: https://docs.ansible.com/projects/ansible/6/collections/azure/azcollection/azure_rm_loadbalancer_module.html
fetched_at: 2026-07-27T16:46:30+00:00
---
# azure.azcollection.azure_rm_loadbalancer module – Manage Azure load balancers

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
> see [Requirements](azure_rm_loadbalancer_module.md#ansible-collections-azure-azcollection-azure-rm-loadbalancer-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_loadbalancer`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_loadbalancer_module.md#synopsis)
- [Requirements](azure_rm_loadbalancer_module.md#requirements)
- [Parameters](azure_rm_loadbalancer_module.md#parameters)
- [Notes](azure_rm_loadbalancer_module.md#notes)
- [See Also](azure_rm_loadbalancer_module.md#see-also)
- [Examples](azure_rm_loadbalancer_module.md#examples)
- [Return Values](azure_rm_loadbalancer_module.md#return-values)

## [Synopsis](azure_rm_loadbalancer_module.md#id1)

- Create, update and delete Azure load balancers.

## [Requirements](azure_rm_loadbalancer_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_loadbalancer_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  added in azure.azcollection 0.0.1 | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  added in azure.azcollection 0.0.1 | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  Default: `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  Choices:   - `false` - `true` ← (default) |
| **auth_source**  string  added in azure.azcollection 0.0.1 | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  Choices:   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **backend_address_pools**  string | List of backend address pools. |
| **name**  string / required | Name of the backend address pool. |
| **backend_port**  string | (deprecated) Backend port that will be exposed for the load balancer.  This option has been deprecated, and will be removed in 2.9. Use *load_balancing_rules* instead. |
| **cert_validation_mode**  string  added in azure.azcollection 0.0.1 | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  Choices:   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  added in azure.azcollection 0.0.1 | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  Default: `"AzureCloud"` |
| **frontend_ip_configurations**  string | List of frontend IPs to be used. |
| **name**  string / required | Name of the frontend ip configuration. |
| **private_ip_address**  string | The reference of the Public IP resource. |
| **private_ip_allocation_method**  string | The Private IP allocation method.  Choices:   - `"Static"` - `"Dynamic"` |
| **public_ip_address**  string | Name of an existing public IP address object in the current resource group to associate with the security group. |
| **subnet**  string | The reference of the subnet resource.  Should be an existing subnet’s resource id. |
| **zones**  list / elements=string | list of availability zones denoting the IP allocated for the resource needs to come from.  This must be specified *sku=Standard* and *subnet* when setting zones. |
| **frontend_port**  string | (deprecated) Frontend port that will be exposed for the load balancer.  This option has been deprecated, and will be removed in 2.9. Use *load_balancing_rules* instead. |
| **idle_timeout**  string | (deprecated) Timeout for TCP idle connection in minutes.  This option has been deprecated, and will be removed in 2.9. Use *load_balancing_rules* instead.  Default: `4` |
| **inbound_nat_pools**  string | Defines an external port range for inbound NAT to a single backend port on NICs associated with a load balancer.  Inbound NAT rules are created automatically for each NIC associated with the Load Balancer using an external port from this range.  Defining an Inbound NAT pool on your Load Balancer is mutually exclusive with defining inbound Nat rules.  Inbound NAT pools are referenced from virtual machine scale sets.  NICs that are associated with individual virtual machines cannot reference an inbound NAT pool.  They have to reference individual inbound NAT rules. |
| **backend_port**  string | The port used for internal connections on the endpoint.  Acceptable values are between 1 and 65535. |
| **frontend_ip_configuration_name**  string / required | A reference to frontend IP addresses. |
| **frontend_port_range_end**  string / required | The last port in the range of external ports that will be used to provide inbound NAT to NICs associated with the load balancer.  Acceptable values range between 1 and 65535. |
| **frontend_port_range_start**  string / required | The first port in the range of external ports that will be used to provide inbound NAT to NICs associated with the load balancer.  Acceptable values range between 1 and 65534. |
| **name**  string / required | Name of the inbound NAT pool. |
| **protocol**  string | IP protocol for the NAT pool.  Choices:   - `"Tcp"` - `"Udp"` - `"All"` |
| **inbound_nat_rules**  string | Collection of inbound NAT Rules used by a load balancer.  Defining inbound NAT rules on your load balancer is mutually exclusive with defining an inbound NAT pool.  Inbound NAT pools are referenced from virtual machine scale sets.  NICs that are associated with individual virtual machines cannot reference an Inbound NAT pool.  They have to reference individual inbound NAT rules. |
| **backend_port**  string | The port used for internal connections on the endpoint.  Acceptable values are between 0 and 65535.  Note that value 0 enables “Any Port”. |
| **enable_floating_ip**  string | Configures a virtual machine’s endpoint for the floating IP capability required to configure a SQL AlwaysOn Availability Group.  This setting is required when using the SQL AlwaysOn Availability Groups in SQL server.  This setting can’t be changed after you create the endpoint. |
| **enable_tcp_reset**  string | Receive bidirectional TCP Reset on TCP flow idle timeout or unexpected connection termination.  This element is only used when *protocol=Tcp*. |
| **frontend_ip_configuration**  string / required | A reference to frontend IP addresses. |
| **frontend_port**  string | The port for the external endpoint.  Frontend port numbers must be unique across all rules within the load balancer.  Acceptable values are between 0 and 65534.  Note that value 0 enables “Any Port”. |
| **idle_timeout**  string | The timeout for the TCP idle connection.  The value can be set between 4 and 30 minutes.  The default value is `4` minutes.  This element is only used when *protocol=Tcp*. |
| **name**  string / required | name of the inbound nat rule. |
| **protocol**  string | IP protocol for the inbound nat rule.  Choices:   - `"Tcp"` - `"Udp"` - `"All"` |
| **load_balancing_rules**  string | Object collection representing the load balancing rules Gets the provisioning. |
| **backend_address_pool**  string / required | A reference to a pool of DIPs. Inbound traffic is randomly load balanced across IPs in the backend IPs. |
| **backend_port**  string | The port used for internal connections on the endpoint.  Acceptable values are between 0 and 65535.  Note that value 0 enables “Any Port”. |
| **disable_outbound_snat**  string | Configure outbound source network address translation (SNAT).  The default behavior when omitted is equivalent to *disable_outbound_snat=True*.  True is equivalent to “(Recommended) Use outbound rules to provide backend pool members access to the internet” in portal.  False is equivalent to “Use default outbound access” in portal. |
| **enable_floating_ip**  string | Configures a virtual machine’s endpoint for the floating IP capability required to configure a SQL AlwaysOn Availability Group. |
| **frontend_ip_configuration**  string / required | A reference to frontend IP addresses. |
| **frontend_port**  string | The port for the external endpoint.  Frontend port numbers must be unique across all rules within the load balancer.  Acceptable values are between 0 and 65534.  Note that value 0 enables “Any Port”. |
| **idle_timeout**  string | The timeout for the TCP idle connection.  The value can be set between 4 and 30 minutes.  The default value is `4` minutes.  This element is only used when the protocol is set to TCP. |
| **load_distribution**  string | The session persistence policy for this rule; `Default` is no persistence.  Choices:   - `"Default"` ← (default) - `"SourceIP"` - `"SourceIPProtocol"` |
| **name**  string / required | Name of the load balancing rule. |
| **probe**  string / required | The name of the load balancer probe this rule should use for health checks. |
| **protocol**  string | IP protocol for the load balancing rule.  Choices:   - `"Tcp"` - `"Udp"` - `"All"` |
| **load_distribution**  string | (deprecated) The type of load distribution that the load balancer will employ.  This option has been deprecated, and will be removed in 2.9. Use *load_balancing_rules* instead.  Choices:   - `"Default"` - `"SourceIP"` - `"SourceIPProtocol"` |
| **location**  string | Valid Azure location. Defaults to location of the resource group. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string / required | Name of the load balancer. |
| **natpool_backend_port**  string | (deprecated) Backend port used by the NAT pool.  This option has been deprecated, and will be removed in 2.9. Use *inbound_nat_pools* instead. |
| **natpool_frontend_port_end**  string | (deprecated) End of the port range for a NAT pool.  This option has been deprecated, and will be removed in 2.9. Use *inbound_nat_pools* instead. |
| **natpool_frontend_port_start**  string | (deprecated) Start of the port range for a NAT pool.  This option has been deprecated, and will be removed in 2.9. Use *inbound_nat_pools* instead. |
| **natpool_protocol**  string | (deprecated) The protocol for the NAT pool.  This option has been deprecated, and will be removed in 2.9. Use *inbound_nat_pools* instead. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **probe_fail_count**  string | (deprecated) The amount of probe failures for the load balancer to make a health determination.  This option has been deprecated, and will be removed in 2.9. Use *probes* instead.  Default: `3` |
| **probe_interval**  string | (deprecated) Time (in seconds) between endpoint health probes.  This option has been deprecated, and will be removed in 2.9. Use *probes* instead.  Default: `15` |
| **probe_port**  string | (deprecated) The port that the health probe will use.  This option has been deprecated, and will be removed in 2.9. Use *probes* instead. |
| **probe_protocol**  string | (deprecated) The protocol to use for the health probe.  This option has been deprecated, and will be removed in 2.9. Use *probes* instead.  Choices:   - `"Tcp"` - `"Http"` - `"Https"` |
| **probe_request_path**  string | (deprecated) The URL that an HTTP probe or HTTPS probe will use (only relevant if *probe_protocol=Http* or *probe_protocol=Https*).  This option has been deprecated, and will be removed in 2.9. Use *probes* instead. |
| **probes**  string | List of probe definitions used to check endpoint health. |
| **fail_count**  aliases: number_of_probes  string | The number of probes where if no response, will result in stopping further traffic from being delivered to the endpoint.  This values allows endpoints to be taken out of rotation faster or slower than the typical times used in Azure.  Default: `3` |
| **interval**  string | The interval, in seconds, for how frequently to probe the endpoint for health status.  Slightly less than half the allocated timeout period, which allows two full probes before taking the instance out of rotation.  The default value is `15`, the minimum value is `5`.  Default: `15` |
| **name**  string / required | Name of the probe. |
| **port**  string / required | Probe port for communicating the probe. Possible values range from 1 to 65535, inclusive. |
| **protocol**  string | The protocol of the end point to be probed.  If `Tcp` is specified, a received ACK is required for the probe to be successful.  If `Http` or `Https` is specified, a 200 OK response from the specified URL is required for the probe to be successful.  Choices:   - `"Tcp"` - `"Http"` - `"Https"` |
| **request_path**  string | The URI used for requesting health status from the VM.  Path is required if *protocol=Http* or *protocol=Https*. Otherwise, it is not allowed. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **protocol**  string | (deprecated) The protocol (TCP or UDP) that the load balancer will use.  This option has been deprecated, and will be removed in 2.9. Use *load_balancing_rules* instead.  Choices:   - `"Tcp"` - `"Udp"` |
| **public_ip_address_name**  aliases: public_ip_address, public_ip_name, public_ip  string | (deprecated) Name of an existing public IP address object to associate with the security group.  This option has been deprecated, and will be removed in 2.9. Use *frontend_ip_configurations* instead. |
| **resource_group**  string / required | Name of a resource group where the load balancer exists or will be created. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **sku**  string | The load balancer SKU.  Choices:   - `"Basic"` - `"Standard"` |
| **state**  string | Assert the state of the load balancer. Use `present` to create/update a load balancer, or `absent` to delete one.  Choices:   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_loadbalancer_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_loadbalancer_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_loadbalancer_module.md#id6)

```yaml+jinja
- name: create load balancer
  azure_rm_loadbalancer:
    resource_group: myResourceGroup
    name: testloadbalancer1
    frontend_ip_configurations:
      - name: frontendipconf0
        public_ip_address: testpip
    backend_address_pools:
      - name: backendaddrpool0
    probes:
      - name: prob0
        port: 80
    inbound_nat_pools:
      - name: inboundnatpool0
        frontend_ip_configuration_name: frontendipconf0
        protocol: Tcp
        frontend_port_range_start: 80
        frontend_port_range_end: 81
        backend_port: 8080
    load_balancing_rules:
      - name: lbrbalancingrule0
        frontend_ip_configuration: frontendipconf0
        backend_address_pool: backendaddrpool0
        frontend_port: 80
        backend_port: 80
        probe: prob0
    inbound_nat_rules:
      - name: inboundnatrule0
        backend_port: 8080
        protocol: Tcp
        frontend_port: 8080
        frontend_ip_configuration: frontendipconf0
```

## [Return Values](azure_rm_loadbalancer_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  Returned: always |
| **state**  dictionary | Current state of the load balancer.  Returned: always |

### Authors

- Thomas Stringer (@trstringer)
- Yuwei Zhou (@yuwzho)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/azure/issues)
[Homepage](https://azure.microsoft.com)
[Repository (Sources)](https://github.com/ansible-collections/azure)
