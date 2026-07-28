---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_aksagentpool module – Manage node pools in Kubernetes kubernetes cluster"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_aksagentpool_module.html
fetched_at: 2026-07-28T01:12:04+00:00
---
# azure.azcollection.azure_rm_aksagentpool module – Manage node pools in Kubernetes kubernetes cluster

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
> see [Requirements](azure_rm_aksagentpool_module.md#ansible-collections-azure-azcollection-azure-rm-aksagentpool-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_aksagentpool`.

New in azure.azcollection 1.14.0

- [Synopsis](azure_rm_aksagentpool_module.md#synopsis)
- [Requirements](azure_rm_aksagentpool_module.md#requirements)
- [Parameters](azure_rm_aksagentpool_module.md#parameters)
- [Notes](azure_rm_aksagentpool_module.md#notes)
- [See Also](azure_rm_aksagentpool_module.md#see-also)
- [Examples](azure_rm_aksagentpool_module.md#examples)
- [Return Values](azure_rm_aksagentpool_module.md#return-values)

## [Synopsis](azure_rm_aksagentpool_module.md#id1)

- Create, update or delete node pools in kubernetes cluster.

## [Requirements](azure_rm_aksagentpool_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_aksagentpool_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  **Choices:**   - `false` - `true` ← (default) |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **availability_zones**  list / elements=integer | Availability zones for nodes. Must use VirtualMachineScaleSets AgentPoolType.  **Choices:**   - `1` - `2` - `3` |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **cluster_name**  string / required | The name of the kubernetes cluster. |
| **count**  integer | Number of agents (VMs) to host docker containers. |
| **enable_auto_scaling**  boolean | Whether to enable auto-scaler.  **Choices:**   - `false` - `true` |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **max_count**  integer | Maximum number of nodes for auto-scaling. |
| **max_pods**  integer | Maximum number of pods that can run on a node. |
| **min_count**  integer | Minimum number of nodes for auto-scaling. |
| **mode**  string | AgentPoolMode represents mode of an agent pool.  **Choices:**   - `"System"` - `"User"` |
| **name**  string / required | The name of the node agent pool. |
| **node_labels**  dictionary | Agent pool node labels to be persisted across all nodes in agent pool. |
| **orchestrator_version**  string | Version of orchestrator specified when creating the managed cluster. |
| **os_disk_size_gb**  integer | OS Disk Size in GB to be used to specify the disk size for every machine in this master/agent pool. |
| **os_type**  string | OsType to be used to specify os type.  **Choices:**   - `"Linux"` - `"Windows"` |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **resource_group**  string / required | The name of the resource group. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **state**  string | State of the automation runbook. Use `present` to create or update a automation runbook and use `absent` to delete.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **type_properties_type**  string | AgentPoolType represents types of an agent pool.  **Choices:**   - `"VirtualMachineScaleSets"` - `"AvailabilitySet"` |
| **vm_size**  string | Size of agent VMs |
| **vnet_subnet_id**  string | VNet SubnetID specifies the VNet’s subnet identifier. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_aksagentpool_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_aksagentpool_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_aksagentpool_module.md#id6)

```yaml+jinja
- name: Add new node agent pool
  azure_rm_aksagentpool:
    resource_group: "{{ resource_group }}"
    cluster_name: aksfred01
    name: default-new
    count: 2
    vm_size: Standard_B2s
    type_properties_type: VirtualMachineScaleSets
    mode: System
    node_labels: {"release":"stable"}
    max_pods: 42
    orchestrator_version: 1.23.5
    availability_zones:
      - 1
      - 2
- name: Delete node agent pool
  azure_rm_aksagentpool:
    resource_group: "{{ resource_group }}"
    cluster_name: aksfred01
    name: default-new
```

## [Return Values](azure_rm_aksagentpool_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **aks_agent_pools**  complex | Details for a node pool in the managed Kubernetes cluster.  **Returned:** always |
| **availability_zones**  list / elements=string | Availability zones for nodes. Must use VirtualMachineScaleSets AgentPoolType.  **Returned:** always  **Sample:** `[1, 2]` |
| **cluster_name**  string | The cluster name.  **Returned:** always  **Sample:** `"testcluster"` |
| **count**  integer | Number of agents (VMs) to host docker containers.  **Returned:** always  **Sample:** `2` |
| **enable_auto_scaling**  string | Whether to enable auto-scaler.  **Returned:** always |
| **enable_node_public_ip**  string | Enable public IP for nodes.  **Returned:** always  **Sample:** `"bool"` |
| **id**  string | Resource ID.  **Returned:** always  **Sample:** `"/subscriptions/xxx-xxxf/resourcegroups/myRG/providers/Microsoft.ContainerService/managedClusters/cluster/agentPools/default"` |
| **max_count**  integer | Maximum number of nodes for auto-scaling.  **Returned:** always  **Sample:** `10` |
| **max_pods**  integer | Maximum number of pods that can run on a node.  **Returned:** always  **Sample:** `42` |
| **min_count**  integer | Minimum number of nodes for auto-scaling.  **Returned:** always  **Sample:** `1` |
| **mode**  string | AgentPoolMode represents mode of an agent pool.  **Returned:** always  **Sample:** `"System"` |
| **name**  string | Resource name.  **Returned:** always  **Sample:** `"default"` |
| **node_image_version**  string | Version of node image.  **Returned:** always  **Sample:** `"AKSUbuntu-1804gen2containerd-2022.08.23"` |
| **node_labels**  list / elements=string | Agent pool node labels to be persisted across all nodes in agent pool.  **Returned:** always  **Sample:** `[{"release": "stable"}]` |
| **node_taints**  string | Taints added to new nodes during node pool create and scale.  **Returned:** always |
| **orchestrator_version**  string | Version of orchestrator specified when creating the managed cluster.  **Returned:** always  **Sample:** `"1.22.11"` |
| **os_disk_size_gb**  integer | OS Disk Size in GB to be used to specify the disk size for every machine in this master/agent pool.  **Returned:** always  **Sample:** `128` |
| **os_type**  string | OsType to be used to specify os type.  **Returned:** always  **Sample:** `"Linux"` |
| **provisioning_state**  string | The current deployment or provisioning state, which only appears in the response.  **Returned:** always  **Sample:** `"Succeeded"` |
| **resource_group**  string | Resource group name.  **Returned:** always  **Sample:** `"myRG"` |
| **scale_set_eviction_policy**  string | ScaleSetEvictionPolicy to be used to specify eviction policy for Spot virtual machine scale set.  **Returned:** always |
| **scale_set_priority**  string | caleSetPriority to be used to specify virtual machine scale set priority.  **Returned:** always |
| **spot_max_price**  float | SpotMaxPrice to be used to specify the maximum price you are willing to pay in US Dollars.  **Returned:** always |
| **type**  string | Resource Type.  **Returned:** always  **Sample:** `"Microsoft.ContainerService/managedClusters/agentPools"` |
| **type_properties_type**  string | AgentPoolType represents types of an agent pool.  **Returned:** always  **Sample:** `"VirtualMachineScaleSets"` |
| **upgrade_settings**  string | Settings for upgrading the agentpool.  **Returned:** always |
| **vm_size**  string | Size of agent VMs.  **Returned:** always  **Sample:** `"Standard_B2s"` |
| **vnet_subnet_id**  string | VNet SubnetID specifies the VNet’s subnet identifier.  **Returned:** always |

### Authors

- xuzhang3 (@xuzhang3)
- Fred Sun (@Fred-sun)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
