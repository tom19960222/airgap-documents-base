---
collection: ansible
version: "6"
title: "netapp.cloudmanager.na_cloudmanager_connector_azure module – NetApp Cloud Manager connector for Azure."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/cloudmanager/na_cloudmanager_connector_azure_module.html
fetched_at: 2026-07-27T17:55:55+00:00
---
# netapp.cloudmanager.na_cloudmanager_connector_azure module – NetApp Cloud Manager connector for Azure.

> **Note:**
>
> This module is part of the [netapp.cloudmanager collection](https://galaxy.ansible.com/netapp/cloudmanager) (version 21.21.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.cloudmanager`.
>
> To use it in a playbook, specify: `netapp.cloudmanager.na_cloudmanager_connector_azure`.

New in netapp.cloudmanager 21.4.0

- [Synopsis](na_cloudmanager_connector_azure_module.md#synopsis)
- [Parameters](na_cloudmanager_connector_azure_module.md#parameters)
- [Notes](na_cloudmanager_connector_azure_module.md#notes)
- [Examples](na_cloudmanager_connector_azure_module.md#examples)
- [Return Values](na_cloudmanager_connector_azure_module.md#return-values)

## [Synopsis](na_cloudmanager_connector_azure_module.md#id1)

- Create or delete Cloud Manager connector for Azure.

## [Parameters](na_cloudmanager_connector_azure_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **account_id**  string / required | The NetApp tenancy account ID. |
| **admin_password**  string / required | The password for the Connector. |
| **admin_username**  string / required | The user name for the Connector. |
| **associate_public_ip_address**  boolean | Indicates whether to associate the public IP address to the virtual machine.  Choices:   - `false` - `true` ← (default) |
| **client_id**  string | The unique client ID of the Connector.  The connector ID. |
| **company**  string / required | The name of the company of the user. |
| **environment**  string  added in netapp.cloudmanager 21.8.0 | The environment for NetApp Cloud Manager API operations.  Choices:   - `"prod"` ← (default) - `"stage"` |
| **feature_flags**  dictionary  added in netapp.cloudmanager 21.11.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **location**  string / required | The location where the Cloud Manager Connector will be created. |
| **name**  string / required | The name of the Cloud Manager connector for Azure to manage. |
| **network_security_group_name**  string / required | The name of the security group for the deployment. |
| **network_security_resource_group**  string | The resource group in Azure associated with the security group.  If not provided, its assumed that the security group is within the previously specified resource group. |
| **proxy_certificates**  list / elements=string | The proxy certificates, a list of certificate file names. |
| **proxy_password**  string | The proxy password, if using a proxy to connect to the internet. |
| **proxy_url**  string | The proxy URL, if using a proxy to connect to the internet. |
| **proxy_user_name**  string | The proxy user name, if using a proxy to connect to the internet. |
| **refresh_token**  string | The refresh token for NetApp Cloud Manager API operations. |
| **resource_group**  string / required | The resource group in Azure where the resources will be created. |
| **sa_client_id**  string | The service account secret client ID for NetApp Cloud Manager API operations. |
| **sa_secret_key**  string | The service account secret key for NetApp Cloud Manager API operations. |
| **state**  string | Whether the specified Cloud Manager connector for Azure should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **storage_account**  string  added in netapp.cloudmanager 21.17.0 | The storage account can be created automatically.  When `storage_account` is not set, the name is constructed by appending ‘sa’ to the connector `name`.  Storage account name must be between 3 and 24 characters in length and use numbers and lower-case letters only. |
| **subnet_name**  aliases: subnet_id  string / required  added in netapp.cloudmanager 21.7.0 | The name of the subnet for the virtual machine.  For example, in /subscriptions/xxx/resourceGroups/xxx/providers/Microsoft.Network/virtualNetworks/xxx/subnets/default, only default is needed. |
| **subscription_id**  string / required | The ID of the Azure subscription. |
| **virtual_machine_size**  string | The virtual machine type. (for example, Standard_DS3_v2).  At least 4 CPU and 16 GB of memory are required.  Default: `"Standard_DS3_v2"` |
| **vnet_name**  aliases: vnet_id  string / required  added in netapp.cloudmanager 21.7.0 | The name of the virtual network.  for example, in /subscriptions/xxx/resourceGroups/xxx/providers/Microsoft.Network/virtualNetworks/default, only default is needed. |
| **vnet_resource_group**  string | The resource group in Azure associated with the virtual network.  If not provided, its assumed that the VNet is within the previously specified resource group. |

## [Notes](na_cloudmanager_connector_azure_module.md#id3)

> **Note:**
>
> - The modules prefixed with na_cloudmanager are built to manage CloudManager and CVO deployments in AWS/GCP/Azure clouds.
> - If sa_client_id and sa_secret_key are provided, service account will be used in operations. refresh_token will be ignored.

## [Examples](na_cloudmanager_connector_azure_module.md#id4)

```yaml+jinja
- name: Create NetApp Cloud Manager connector for Azure.
  netapp.cloudmanager.na_cloudmanager_connector_azure:
    state: present
    refresh_token: "{{ xxxxxxxxxxxxxxx }}"
    name: bsuhas_ansible_occm
    location: westus
    resource_group: occm_group_westus
    subnet_name: subnetxxxxx
    vnet_name: Vnetxxxxx
    subscription_id: "{{ xxxxxxxxxxxxxxxxx }}"
    account_id: "{{ account-xxxxxxx }}"
    company: NetApp
    admin_password: Netapp123456
    admin_username: bsuhas
    network_security_group_name: OCCM_SG
    proxy_url: abc.com
    proxy_user_name: xyz
    proxy_password: abcxyz
    proxy_certificates: [abc.crt.txt, xyz.crt.txt]

- name: Delete NetApp Cloud Manager connector for Azure.
  netapp.cloudmanager.na_cloudmanager_connector_azure:
    state: absent
    name: ansible
    location: westus
    resource_group: occm_group_westus
    network_security_group_name: OCCM_SG
    subnet_name: subnetxxxxx
    company: NetApp
    admin_password: Netapp123456
    admin_username: bsuhas
    vnet_name: Vnetxxxxx
    subscription_id: "{{ xxxxxxxxxxxxxxxxx }}"
    account_id: "{{ account-xxxxxxx }}"
    refresh_token: "{{ xxxxxxxxxxxxxxx }}"
    client_id: xxxxxxxxxxxxxxxxxxx
```

## [Return Values](na_cloudmanager_connector_azure_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Newly created Azure connector id in cloud manager.  Returned: success  Sample: `"xxxxxxxxxxxxxxxx"` |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.cloudmanager)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.cloudmanager)
