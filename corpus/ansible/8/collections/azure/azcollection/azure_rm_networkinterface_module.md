---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_networkinterface module – Manage Azure network interfaces"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_networkinterface_module.html
fetched_at: 2026-07-28T01:14:04+00:00
---
# azure.azcollection.azure_rm_networkinterface module – Manage Azure network interfaces

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
> see [Requirements](azure_rm_networkinterface_module.md#ansible-collections-azure-azcollection-azure-rm-networkinterface-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_networkinterface`.

New in azure.azcollection 0.1.0

- [Synopsis](azure_rm_networkinterface_module.md#synopsis)
- [Requirements](azure_rm_networkinterface_module.md#requirements)
- [Parameters](azure_rm_networkinterface_module.md#parameters)
- [Notes](azure_rm_networkinterface_module.md#notes)
- [See Also](azure_rm_networkinterface_module.md#see-also)
- [Examples](azure_rm_networkinterface_module.md#examples)
- [Return Values](azure_rm_networkinterface_module.md#return-values)

## [Synopsis](azure_rm_networkinterface_module.md#id1)

- Create, update or delete a network interface.
- When creating a network interface you must provide the name of an existing virtual network, the name of an existing subnet within the virtual network.
- A default security group and public IP address will be created automatically.
- Or you can provide the name of an existing security group and public IP address.
- See the examples below for more details.

## [Requirements](azure_rm_networkinterface_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_networkinterface_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  **Choices:**   - `false` - `true` ← (default) |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **create_with_security_group**  boolean | Whether a security group should be be created with the NIC.  If this flag set to `True` and no *security_group* set, a default security group will be created.  **Choices:**   - `false` - `true` ← (default) |
| **dns_servers**  list / elements=string | Which DNS servers should the NIC lookup.  List of IP addresses. |
| **enable_accelerated_networking**  boolean | Whether the network interface should be created with the accelerated networking feature or not.  **Choices:**   - `false` ← (default) - `true` |
| **enable_ip_forwarding**  aliases: ip_forwarding  boolean | Whether to enable IP forwarding.  **Choices:**   - `false` ← (default) - `true` |
| **ip_configurations**  list / elements=dictionary | List of IP configurations. Each configuration object should include field *private_ip_address*, *private_ip_allocation_method*, *public_ip_address_name*, *public_ip*, *public_ip_allocation_method*, *name*.  **Default:** `[]` |
| **application_gateway_backend_address_pools**  list / elements=any  *added in azure.azcollection 1.10.0* | List of existing application gateway backend address pools to associate with the network interface.  Can be written as a resource ID.  Also can be a dict of *name* and *application_gateway*. |
| **application_security_groups**  list / elements=any | List of application security groups in which the IP configuration is included.  Element of the list could be a resource id of application security group, or dict of *resource_group* and *name*. |
| **load_balancer_backend_address_pools**  list / elements=any | List of existing load-balancer backend address pools to associate with the network interface.  Can be written as a resource ID.  Also can be a dict of *name* and *load_balancer*. |
| **name**  string / required | Name of the IP configuration. |
| **primary**  boolean | Whether the IP configuration is the primary one in the list.  The first IP configuration default set to *primary=True*.  **Choices:**   - `false` ← (default) - `true` |
| **private_ip_address**  string | Private IP address for the IP configuration. |
| **private_ip_address_version**  string | The version of the IP configuration.  **Choices:**   - `"IPv4"` ← (default) - `"IPv6"` |
| **private_ip_allocation_method**  string | Private IP allocation method.  **Choices:**   - `"Dynamic"` ← (default) - `"Static"` |
| **public_ip_address_name**  aliases: public_ip_address, public_ip_name  string | Name of the public IP address. None for disable IP address. |
| **public_ip_allocation_method**  string | Public IP allocation method.  **Choices:**   - `"Dynamic"` ← (default) - `"Static"` |
| **location**  string | Valid Azure location. Defaults to location of the resource group. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string / required | Name of the network interface. |
| **open_ports**  list / elements=string | When a default security group is created for a Linux host a rule will be added allowing inbound TCP connections to the default SSH port `22`, and for a Windows host rules will be added allowing inbound access to RDP ports `3389` and `5986`. Override the default ports by providing a list of open ports. |
| **os_type**  string | Determines any rules to be added to a default security group.  When creating a network interface, if no security group name is provided, a default security group will be created.  If the *os_type=Windows*, a rule allowing RDP access will be added.  If the *os_type=Linux*, a rule allowing SSH access will be added.  **Choices:**   - `"Windows"` - `"Linux"` ← (default) |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **private_ip_address**  string | (Deprecate) Valid IPv4 address that falls within the specified subnet.  This option will be deprecated in 2.9, use *ip_configurations* instead. |
| **private_ip_allocation_method**  string | (Deprecate) Whether or not the assigned IP address is permanent.  When creating a network interface, if you specify *private_ip_address=Static*, you must provide a value for *private_ip_address*.  You can update the allocation method to `Static` after a dynamic private IP address has been assigned.  This option will be deprecated in 2.9, use *ip_configurations* instead.  **Choices:**   - `"Dynamic"` ← (default) - `"Static"` |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **public_ip**  boolean | (Deprecate) When creating a network interface, if no public IP address name is provided a default public IP address will be created.  Set to `false` if you do not want a public IP address automatically created.  This option will be deprecated in 2.9, use *ip_configurations* instead.  **Choices:**   - `false` - `true` ← (default) |
| **public_ip_address_name**  aliases: public_ip_address, public_ip_name  string | (Deprecate) Name of an existing public IP address object to associate with the security group.  This option will be deprecated in 2.9, use *ip_configurations* instead. |
| **public_ip_allocation_method**  string | (Deprecate) If a *public_ip_address_name* is not provided, a default public IP address will be created.  The allocation method determines whether or not the public IP address assigned to the network interface is permanent.  This option will be deprecated in 2.9, use *ip_configurations* instead.  **Choices:**   - `"Dynamic"` ← (default) - `"Static"` |
| **resource_group**  string / required | Name of a resource group where the network interface exists or will be created. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **security_group**  aliases: security_group_name  any | An existing security group with which to associate the network interface.  If not provided, a default security group will be created when *create_with_security_group=true*.  It can be the name of security group.  Make sure the security group is in the same resource group when you only give its name.  It can be the resource id.  It can be a dict contains security_group’s *name* and *resource_group*. |
| **state**  string | Assert the state of the network interface. Use `present` to create or update an interface and `absent` to delete an interface.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **subnet_name**  aliases: subnet  string | Name of an existing subnet within the specified virtual network. Required when creating a network interface.  Use the `virtual_network`‘s resource group.  Required when creating. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **virtual_network**  aliases: virtual_network_name  any | An existing virtual network with which the network interface will be associated. Required when creating a network interface.  It can be the virtual network’s name.  Make sure your virtual network is in the same resource group as NIC when you give only the name.  It can be the virtual network’s resource id.  It can be a dict which contains *name* and *resource_group* of the virtual network.  Required when creating. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_networkinterface_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_networkinterface_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_networkinterface_module.md#id6)

```yaml+jinja
- name: Create a network interface with minimal parameters
  azure_rm_networkinterface:
    name: nic001
    resource_group: myResourceGroup
    virtual_network: vnet001
    subnet_name: subnet001
    ip_configurations:
      - name: ipconfig1
        public_ip_address_name: publicip001
        primary: true

- name: Create a network interface with private IP address only (no Public IP)
  azure_rm_networkinterface:
    name: nic001
    resource_group: myResourceGroup
    virtual_network: vnet001
    subnet_name: subnet001
    create_with_security_group: false
    ip_configurations:
      - name: ipconfig1
        primary: true

- name: Create a network interface for use in a Windows host (opens RDP port) with custom RDP port
  azure_rm_networkinterface:
    name: nic002
    resource_group: myResourceGroup
    virtual_network: vnet001
    subnet_name: subnet001
    os_type: Windows
    rdp_port: 3399
    security_group: "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup/providers/Microsoft.Network/networkSecurit
                     yGroups/nsg001"
    ip_configurations:
      - name: ipconfig1
        public_ip_address_name: publicip001
        primary: true

- name: Create a network interface using existing security group and public IP
  azure_rm_networkinterface:
    name: nic003
    resource_group: myResourceGroup
    virtual_network: vnet001
    subnet_name: subnet001
    security_group: secgroup001
    ip_configurations:
      - name: ipconfig1
        public_ip_address_name: publicip001
        primary: true

- name: Create a network with multiple ip configurations
  azure_rm_networkinterface:
    name: nic004
    resource_group: myResourceGroup
    subnet_name: subnet001
    virtual_network: vnet001
    security_group:
      name: testnic002
      resource_group: Testing1
    ip_configurations:
      - name: ipconfig1
        public_ip_address_name: publicip001
        primary: true
      - name: ipconfig2
        load_balancer_backend_address_pools:
          - "{{ loadbalancer001.state.backend_address_pools[0].id }}"
          - name: backendaddrpool1
            load_balancer: loadbalancer001

- name: Create network interface attached to application gateway backend address pool
  azure_rm_networkinterface:
    name: nic-appgw
    resource_group: myResourceGroup
    virtual_network: vnet001
    subnet_name: subnet001
    create_with_security_group: false
    public_ip: false
    ip_configurations:
      - name: default
        primary: true
        application_gateway_backend_address_pools:
          - name: myApplicationGatewayBackendAddressPool
            application_gateway: myApplicationGateway

- name: Create a network interface in accelerated networking mode
  azure_rm_networkinterface:
    name: nic005
    resource_group: myResourceGroup
    virtual_network_name: vnet001
    subnet_name: subnet001
    enable_accelerated_networking: true

- name: Create a network interface with IP forwarding
  azure_rm_networkinterface:
    name: nic001
    resource_group: myResourceGroup
    virtual_network: vnet001
    subnet_name: subnet001
    ip_forwarding: true
    ip_configurations:
      - name: ipconfig1
        public_ip_address_name: publicip001
        primary: true

- name: Create a network interface with dns servers
  azure_rm_networkinterface:
    name: nic009
    resource_group: myResourceGroup
    virtual_network: vnet001
    subnet_name: subnet001
    dns_servers:
      - 8.8.8.8

- name: Delete network interface
  azure_rm_networkinterface:
    resource_group: myResourceGroup
    name: nic003
    state: absent
```

## [Return Values](azure_rm_networkinterface_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **state**  complex | The current state of the network interface.  **Returned:** always |
| **dns_server**  list / elements=string | Which DNS servers should the NIC lookup.  List of IP addresses.  **Returned:** success  **Sample:** `["8.9.10.11", "7.8.9.10"]` |
| **dns_setting**  dictionary | The DNS settings in network interface.  **Returned:** success  **Sample:** `{"applied_dns_servers": [], "dns_servers": ["8.9.10.11", "7.8.9.10"], "internal_dns_name_label": null, "internal_fqdn": null}` |
| **enable_accelerated_networking**  boolean | Whether the network interface should be created with the accelerated networking feature or not.  **Returned:** success  **Sample:** `true` |
| **enable_ip_forwarding**  boolean | Whether to enable IP forwarding.  **Returned:** success  **Sample:** `true` |
| **etag**  string | A unique read-only string that changes whenever the resource is updated.  **Returned:** success  **Sample:** `"W/\"be115a43-2148-4545-a324-f33ad444c926\""` |
| **id**  string | Id of the network interface.  **Returned:** success  **Sample:** `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup/providers/Microsoft.Network/networkInterfaces/nic003"` |
| **ip_configurations**  complex | List of IP configurations.  **Returned:** success |
| **application_gateway_backend_address_pools**  list / elements=string  *added in azure.azcollection 1.10.0* | List of existing application gateway backend address pool resource IDs associated with the network interface.  **Returned:** success  **Sample:** `["/subscriptions/xxx/resourceGroups/myResourceGroup/providers/Microsoft.Network/applicationGateways/myGateway/ backendAddressPools/myBackendAddressPool"]` |
| **load_balancer_backend_address_pools**  list / elements=string | List of existing load-balancer backend address pools associated with the network interface.  **Returned:** success |
| **name**  string | Name of the IP configuration.  **Returned:** success  **Sample:** `"default"` |
| **private_ip_address**  string | Private IP address for the IP configuration.  **Returned:** success  **Sample:** `"10.1.0.10"` |
| **private_ip_address_version**  string | The version of the IP configuration.  **Returned:** success  **Sample:** `"IPv4"` |
| **private_ip_allocation_method**  string | Private IP allocation method.  **Returned:** success  **Sample:** `"Static"` |
| **public_ip_address**  dictionary | Name of the public IP address. None for disable IP address.  **Returned:** success  **Sample:** `{"id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup/providers/Microsoft.Network/publicIPAddresse s/publicip001", "name": "publicip001"}` |
| **subnet**  dictionary | The reference of the subnet resource.  **Returned:** success  **Sample:** `{"id": "/subscriptions/xxxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/ myresourcegroup/providers/Microsoft.Network/virtualNetworks/tnb57dc95318/subnets/tnb57dc95318", "name": "tnb57dc95318", "resource_group": "myresourcegroup", "virtual_network_name": "tnb57dc95318"}` |
| **location**  string | The network interface resource location.  **Returned:** success  **Sample:** `"eastus"` |
| **mac_address**  string | The MAC address of the network interface.  **Returned:** success |
| **name**  string | Name of the network interface.  **Returned:** success  **Sample:** `"nic003"` |
| **network_security_group**  dictionary | The reference of the network security group resource.  **Returned:** success  **Sample:** `{"id": "/subscriptions//xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/ myResourceGroup/providers/Microsoft.Network/networkSecurityGroups/nsg001", "name": "nsg001"}` |
| **primary**  boolean | Get whether this is a primary network interface on virtual machine.  **Returned:** success  **Sample:** `true` |
| **provisioning_state**  string | The provisioning state of the public IP resource.  **Returned:** success  **Sample:** `"Succeeded"` |
| **tags**  dictionary | -Tags of the network interface.  **Returned:** success  **Sample:** `{"key": "value"}` |
| **type**  string | Type of the resource.  **Returned:** success  **Sample:** `"Microsoft.Network/networkInterfaces"` |

### Authors

- Chris Houseknecht (@chouseknecht)
- Matt Davis (@nitzmahone)
- Yuwei Zhou (@yuwzho)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
