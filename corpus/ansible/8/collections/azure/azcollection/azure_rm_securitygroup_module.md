---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_securitygroup module – Manage Azure network security groups"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_securitygroup_module.html
fetched_at: 2026-07-28T01:04:21+00:00
---
# azure.azcollection.azure_rm_securitygroup module – Manage Azure network security groups

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
> see [Requirements](azure_rm_securitygroup_module.md#ansible-collections-azure-azcollection-azure-rm-securitygroup-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_securitygroup`.

New in azure.azcollection 0.1.0

- [Synopsis](azure_rm_securitygroup_module.md#synopsis)
- [Requirements](azure_rm_securitygroup_module.md#requirements)
- [Parameters](azure_rm_securitygroup_module.md#parameters)
- [Notes](azure_rm_securitygroup_module.md#notes)
- [See Also](azure_rm_securitygroup_module.md#see-also)
- [Examples](azure_rm_securitygroup_module.md#examples)
- [Return Values](azure_rm_securitygroup_module.md#return-values)

## [Synopsis](azure_rm_securitygroup_module.md#id1)

- Create, update or delete a network security group.
- A security group contains Access Control List (ACL) rules that allow or deny network traffic to subnets or individual network interfaces.
- A security group is created with a set of default security rules and an empty set of security rules.
- Shape traffic flow by adding rules to the empty set of security rules.

## [Requirements](azure_rm_securitygroup_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_securitygroup_module.md#id3)

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
| **default_rules**  list / elements=dictionary | The set of default rules automatically added to a security group at creation.  In general default rules will not be modified. Modify rules to shape the flow of traffic to or from a subnet or NIC.  See rules below for the makeup of a rule dict. |
| **access**  string | Whether or not to allow the traffic flow.  **Choices:**   - `"Allow"` ← (default) - `"Deny"` |
| **description**  string | Short description of the rule’s purpose. |
| **destination_address_prefix**  any | The destination address prefix.  CIDR or destination IP range.  Asterisk `*` can also be used to match all source IPs.  Default tags such as `VirtualNetwork`, `AzureLoadBalancer` and `Internet` can also be used.  It can accept string type or a list of string type.  Asterisk `*` and default tags can only be specified as single string type, not as a list of string.  **Default:** `"*"` |
| **destination_application_security_groups**  list / elements=any | List of the destination application security groups.  It could be list of resource id.  It could be list of names in same resource group.  It could be list of dict containing *resource_group* and *name*.  It is mutually exclusive with `destination_address_prefix` and `destination_address_prefixes`. |
| **destination_port_range**  any | Port or range of ports to which traffic is headed.  It can accept string type or a list of string type.  **Default:** `"*"` |
| **direction**  string | Indicates the direction of the traffic flow.  **Choices:**   - `"Inbound"` ← (default) - `"Outbound"` |
| **name**  string / required | Unique name for the rule. |
| **priority**  integer / required | Order in which to apply the rule. Must a unique integer between 100 and 4096 inclusive. |
| **protocol**  string | Accepted traffic protocol.  **Choices:**   - `"Udp"` - `"Tcp"` - `"Icmp"` - `"*"` ← (default) |
| **source_address_prefix**  any | The CIDR or source IP range.  Asterisk `*` can also be used to match all source IPs.  Default tags such as `VirtualNetwork`, `AzureLoadBalancer` and `Internet` can also be used.  If this is an ingress rule, specifies where network traffic originates from.  It can accept string type or a list of string type.  Asterisk `*` and default tags can only be specified as single string type, not as a list of string.  **Default:** `"*"` |
| **source_application_security_groups**  list / elements=any | List of the source application security groups.  It could be list of resource id.  It could be list of names in same resource group.  It could be list of dict containing resource_group and name.  It is mutually exclusive with `source_address_prefix` and `source_address_prefixes`. |
| **source_port_range**  any | Port or range of ports from which traffic originates.  It can accept string type or a list of string type.  **Default:** `"*"` |
| **location**  string | Valid azure location. Defaults to location of the resource group. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string / required | Name of the security group to operate on. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **purge_default_rules**  boolean | Remove any existing rules not matching those defined in the default_rules parameter.  **Choices:**   - `false` ← (default) - `true` |
| **purge_rules**  boolean | Remove any existing rules not matching those defined in the rules parameters.  **Choices:**   - `false` ← (default) - `true` |
| **resource_group**  string / required | Name of the resource group the security group belongs to. |
| **rules**  list / elements=dictionary | Set of rules shaping traffic flow to or from a subnet or NIC. Each rule is a dictionary. |
| **access**  string | Whether or not to allow the traffic flow.  **Choices:**   - `"Allow"` ← (default) - `"Deny"` |
| **description**  string | Short description of the rule’s purpose. |
| **destination_address_prefix**  any | The destination address prefix.  CIDR or destination IP range.  Asterisk `*` can also be used to match all source IPs.  Default tags such as `VirtualNetwork`, `AzureLoadBalancer` and `Internet` can also be used.  It can accept string type or a list of string type.  Asterisk `*` and default tags can only be specified as single string type, not as a list of string.  **Default:** `"*"` |
| **destination_application_security_groups**  list / elements=any | List of the destination application security groups.  It could be list of resource id.  It could be list of names in same resource group.  It could be list of dict containing *resource_group* and *name*.  It is mutually exclusive with `destination_address_prefix` and `destination_address_prefixes`. |
| **destination_port_range**  any | Port or range of ports to which traffic is headed.  It can accept string type or a list of string type.  **Default:** `"*"` |
| **direction**  string | Indicates the direction of the traffic flow.  **Choices:**   - `"Inbound"` ← (default) - `"Outbound"` |
| **name**  string / required | Unique name for the rule. |
| **priority**  integer / required | Order in which to apply the rule. Must a unique integer between 100 and 4096 inclusive. |
| **protocol**  string | Accepted traffic protocol.  **Choices:**   - `"Udp"` - `"Tcp"` - `"Icmp"` - `"*"` ← (default) |
| **source_address_prefix**  any | The CIDR or source IP range.  Asterisk `*` can also be used to match all source IPs.  Default tags such as `VirtualNetwork`, `AzureLoadBalancer` and `Internet` can also be used.  If this is an ingress rule, specifies where network traffic originates from.  It can accept string type or a list of string type.  Asterisk `*` and default tags can only be specified as single string type, not as a list of string.  **Default:** `"*"` |
| **source_application_security_groups**  list / elements=any | List of the source application security groups.  It could be list of resource id.  It could be list of names in same resource group.  It could be list of dict containing resource_group and name.  It is mutually exclusive with `source_address_prefix` and `source_address_prefixes`. |
| **source_port_range**  any | Port or range of ports from which traffic originates.  It can accept string type or a list of string type.  **Default:** `"*"` |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **state**  string | Assert the state of the security group. Set to `present` to create or update a security group. Set to `absent` to remove a security group.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_securitygroup_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_securitygroup_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_securitygroup_module.md#id6)

```yaml+jinja
- name: Create a security group
  azure_rm_securitygroup:
    resource_group: myResourceGroup
    name: mysecgroup
    purge_rules: true
    rules:
      - name: DenySSH
        protocol: Tcp
        destination_port_range: 22
        access: Deny
        priority: 100
        direction: Inbound
      - name: 'AllowSSH'
        protocol: Tcp
        source_address_prefix:
          - '174.109.158.0/24'
          - '174.109.159.0/24'
        destination_port_range: 22
        access: Allow
        priority: 101
        direction: Inbound
      - name: 'AllowMultiplePorts'
        protocol: Tcp
        source_address_prefix:
          - '174.109.158.0/24'
          - '174.109.159.0/24'
        destination_port_range:
          - 80
          - 443
        access: Allow
        priority: 102

- name: Update rules on existing security group
  azure_rm_securitygroup:
    resource_group: myResourceGroup
    name: mysecgroup
    rules:
      - name: DenySSH
        protocol: Tcp
        destination_port_range: 22-23
        access: Deny
        priority: 100
        direction: Inbound
      - name: AllowSSHFromHome
        protocol: Tcp
        source_address_prefix: '174.109.158.0/24'
        destination_port_range: 22-23
        access: Allow
        priority: 102
        direction: Inbound
    tags:
      testing: testing
      delete: on-exit

- name: Create a securiy group with I(protocol=Icmp)
  azure_rm_securitygroup:
    name: mysecgroup
    resource_group: myResourceGroup
    rules:
      - name: SSH
        protocol: Tcp
        destination_port_range: 22
        access: Allow
        priority: 105
        direction: Inbound
      - name: ICMP
        protocol: Icmp
        priority: 106

- name: Delete security group
  azure_rm_securitygroup:
    resource_group: myResourceGroup
    name: mysecgroup
    state: absent
```

## [Return Values](azure_rm_securitygroup_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **state**  complex | Current state of the security group.  **Returned:** always |
| **default_rules**  list / elements=string | The default security rules of network security group.  **Returned:** always  **Sample:** `[{"access": "Allow", "description": "Allow inbound traffic from all VMs in VNET", "destination_address_prefix": "VirtualNetwork", "destination_port_range": "*", "direction": "Inbound", "etag": "W/\"edf48d56-b315-40ca-a85d-dbcb47f2da7d\"", "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup/providers/Microsoft.Network/networkSecurityGroups/mysecgroup/defaultSecurityRules/AllowVnetInBound", "name": "AllowVnetInBound", "priority": 65000, "protocol": "*", "provisioning_state": "Succeeded", "source_address_prefix": "VirtualNetwork", "source_port_range": "*"}, {"access": "Allow", "description": "Allow inbound traffic from azure load balancer", "destination_address_prefix": "*", "destination_port_range": "*", "direction": "Inbound", "etag": "W/\"edf48d56-b315-40ca-a85d-dbcb47f2da7d\"", "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup/providers/Microsoft.Network/networkSecurityGroups/mysecgroup/defaultSecurityRules/AllowAzureLoadBalancerInBound", "name": "AllowAzureLoadBalancerInBound", "priority": 65001, "protocol": "*", "provisioning_state": "Succeeded", "source_address_prefix": "AzureLoadBalancer", "source_port_range": "*"}, {"access": "Deny", "description": "Deny all inbound traffic", "destination_address_prefix": "*", "destination_port_range": "*", "direction": "Inbound", "etag": "W/\"edf48d56-b315-40ca-a85d-dbcb47f2da7d\"", "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup/providers/Microsoft.Network/networkSecurityGroups/mysecgroup/defaultSecurityRules/DenyAllInBound", "name": "DenyAllInBound", "priority": 65500, "protocol": "*", "provisioning_state": "Succeeded", "source_address_prefix": "*", "source_port_range": "*"}, {"access": "Allow", "description": "Allow outbound traffic from all VMs to all VMs in VNET", "destination_address_prefix": "VirtualNetwork", "destination_port_range": "*", "direction": "Outbound", "etag": "W/\"edf48d56-b315-40ca-a85d-dbcb47f2da7d\"", "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup/providers/Microsoft.Network/networkSecurityGroups/mysecgroup/defaultSecurityRules/AllowVnetOutBound", "name": "AllowVnetOutBound", "priority": 65000, "protocol": "*", "provisioning_state": "Succeeded", "source_address_prefix": "VirtualNetwork", "source_port_range": "*"}, {"access": "Allow", "description": "Allow outbound traffic from all VMs to Internet", "destination_address_prefix": "Internet", "destination_port_range": "*", "direction": "Outbound", "etag": "W/\"edf48d56-b315-40ca-a85d-dbcb47f2da7d\"", "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup/providers/Microsoft.Network/networkSecurityGroups/mysecgroup/defaultSecurityRules/AllowInternetOutBound", "name": "AllowInternetOutBound", "priority": 65001, "protocol": "*", "provisioning_state": "Succeeded", "source_address_prefix": "*", "source_port_range": "*"}, {"access": "Deny", "description": "Deny all outbound traffic", "destination_address_prefix": "*", "destination_port_range": "*", "direction": "Outbound", "etag": "W/\"edf48d56-b315-40ca-a85d-dbcb47f2da7d\"", "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup/providers/Microsoft.Network/networkSecurityGroups/mysecgroup/defaultSecurityRules/DenyAllOutBound", "name": "DenyAllOutBound", "priority": 65500, "protocol": "*", "provisioning_state": "Succeeded", "source_address_prefix": "*", "source_port_range": "*"}]` |
| **id**  string | The resource ID.  **Returned:** always  **Sample:** `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup/providers/Microsoft.Network/networkSecurityGroups/mysecgroup"` |
| **location**  string | The resource location.  **Returned:** always  **Sample:** `"westus"` |
| **name**  string | Name of the secrurity group.  **Returned:** always  **Sample:** `"mysecgroup"` |
| **network_interfaces**  list / elements=string | A collection of references to network interfaces.  **Returned:** always  **Sample:** `[]` |
| **rules**  list / elements=string | A collection of security rules of the network security group.  **Returned:** always  **Sample:** `[{"access": "Deny", "description": null, "destination_address_prefix": "*", "destination_port_range": "22", "direction": "Inbound", "etag": "W/\"edf48d56-b315-40ca-a85d-dbcb47f2da7d\"", "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup/providers/Microsoft.Network/networkSecurityGroups/mysecgroup/securityRules/DenySSH", "name": "DenySSH", "priority": 100, "protocol": "Tcp", "provisioning_state": "Succeeded", "source_address_prefix": "*", "source_port_range": "*"}, {"access": "Allow", "description": null, "destination_address_prefix": "*", "destination_port_range": "22", "direction": "Inbound", "etag": "W/\"edf48d56-b315-40ca-a85d-dbcb47f2da7d\"", "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroup/myResourceGroup/providers/Microsoft.Network/networkSecurityGroups/mysecgroup/securityRules/AllowSSH", "name": "AllowSSH", "priority": 101, "protocol": "Tcp", "provisioning_state": "Succeeded", "source_address_prefix": "174.109.158.0/24", "source_port_range": "*"}]` |
| **subnets**  list / elements=string | A collection of references to subnets.  **Returned:** always  **Sample:** `[]` |
| **tags**  dictionary | Tags to assign to the security group.  **Returned:** always  **Sample:** `{"delete": "on-exit", "foo": "bar", "testing": "testing"}` |
| **type**  string | The resource type.  **Returned:** always  **Sample:** `"Microsoft.Network/networkSecurityGroups"` |

### Authors

- Chris Houseknecht (@chouseknecht)
- Matt Davis (@nitzmahone)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
