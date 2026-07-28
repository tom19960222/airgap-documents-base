---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_aks module – Manage a managed Azure Container Service (AKS) instance"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_aks_module.html
fetched_at: 2026-07-28T01:12:02+00:00
---
# azure.azcollection.azure_rm_aks module – Manage a managed Azure Container Service (AKS) instance

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
> see [Requirements](azure_rm_aks_module.md#ansible-collections-azure-azcollection-azure-rm-aks-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_aks`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_aks_module.md#synopsis)
- [Requirements](azure_rm_aks_module.md#requirements)
- [Parameters](azure_rm_aks_module.md#parameters)
- [Notes](azure_rm_aks_module.md#notes)
- [See Also](azure_rm_aks_module.md#see-also)
- [Examples](azure_rm_aks_module.md#examples)
- [Return Values](azure_rm_aks_module.md#return-values)

## [Synopsis](azure_rm_aks_module.md#id1)

- Create, update and delete a managed Azure Container Service (AKS) instance.

## [Requirements](azure_rm_aks_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_aks_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aad_profile**  dictionary | Profile of Azure Active Directory configuration. |
| **admin_group_object_ids**  list / elements=string | AAD group object IDs that will have admin role of the cluster. |
| **client_app_id**  string | The client AAD application ID. |
| **managed**  boolean | Whether to enable manged AAD.  **Choices:**   - `false` ← (default) - `true` |
| **server_app_id**  string | The server AAD application ID. |
| **server_app_secret**  string | The server AAD application secret. |
| **tenant_id**  string | The AAD tenant ID to use for authentication.  If not specified, will use the tenant of the deployment subscription. |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **addon**  dictionary | Profile of managed cluster add-on.  Key can be `http_application_routing`, `monitoring`, `virtual_node`.  Value must be a dict contains a bool variable `enabled`. |
| **http_application_routing**  aliases: httpApplicationRouting  dictionary | The HTTP application routing solution makes it easy to access applications that are deployed to your cluster. |
| **enabled**  boolean | Whether the solution enabled.  **Choices:**   - `false` - `true` ← (default) |
| **monitoring**  aliases: omsagent  dictionary | It gives you performance visibility by collecting memory and processor metrics from controllers, nodes, and containers that are available in Kubernetes through the Metrics API. |
| **enabled**  boolean | Whether the solution enabled.  **Choices:**   - `false` - `true` ← (default) |
| **log_analytics_workspace_resource_id**  aliases: logAnalyticsWorkspaceResourceID  string / required | Where to store the container metrics. |
| **virtual_node**  aliases: aciConnector  dictionary | With virtual nodes, you have quick provisioning of pods, and only pay per second for their execution time.  You don’t need to wait for Kubernetes cluster autoscaler to deploy VM compute nodes to run the additional pods. |
| **enabled**  boolean | Whether the solution enabled.  **Choices:**   - `false` - `true` ← (default) |
| **subnet_resource_id**  aliases: SubnetName  string / required | Subnet associated to the cluster. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **agent_pool_profiles**  list / elements=dictionary | The agent pool profile suboptions. |
| **availability_zones**  list / elements=integer | Availability zones for nodes. Must use VirtualMachineScaleSets AgentPoolType.  **Choices:**   - `1` - `2` - `3` |
| **count**  integer / required | Number of agents (VMs) to host docker containers.  Allowed values must be in the range of `1` to `100` (inclusive). |
| **dns_prefix**  string | DNS prefix specified when creating the managed cluster. |
| **enable_auto_scaling**  boolean | To enable auto-scaling.  **Choices:**   - `false` - `true` |
| **max_count**  integer | Maximum number of nodes for auto-scaling.  Required if *enable_auto_scaling=True*. |
| **max_pods**  integer | Maximum number of pods schedulable on nodes. |
| **min_count**  integer | Minmum number of nodes for auto-scaling.  Required if *enable_auto_scaling=True*. |
| **mode**  string | AgentPoolMode represents mode of an agent pool.  Possible values include `System` and `User`.  System AgentPoolMode requires a minimum VM SKU of at least 2 vCPUs and 4GB memory.  **Choices:**   - `"System"` - `"User"` |
| **name**  string / required | Unique name of the agent pool profile in the context of the subscription and resource group. |
| **node_labels**  dictionary | Agent pool node labels to be persisted across all nodes in agent pool. |
| **orchestrator_version**  string | Version of kubernetes running on the node pool. |
| **os_disk_size_gb**  integer | Size of the OS disk. |
| **os_type**  string | The operating system type.  **Choices:**   - `"Linux"` - `"Windows"` |
| **ports**  list / elements=integer | List of the agent pool’s port. |
| **storage_profiles**  string | Storage profile specifies what kind of storage used.  **Choices:**   - `"StorageAccount"` - `"ManagedDisks"` |
| **type**  string | AgentPoolType represents types of an agent pool.  Possible values include `VirtualMachineScaleSets` and `AvailabilitySet`.  **Choices:**   - `"VirtualMachineScaleSets"` - `"AvailabilitySet"` |
| **vm_size**  string / required | The VM Size of each of the Agent Pool VM’s (e.g. `Standard_F1` / `Standard_D2v2`). |
| **vnet_subnet_id**  string | Specifies the VNet’s subnet identifier. |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **api_server_access_profile**  dictionary | Profile of API Access configuration. |
| **authorized_ip_ranges**  list / elements=string | Authorized IP Ranges to kubernetes API server.  Cannot be enabled when using private cluster |
| **enable_private_cluster**  boolean | Whether to create the cluster as a private cluster or not.  Cannot be changed for an existing cluster.  **Choices:**   - `false` - `true` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  **Choices:**   - `false` - `true` ← (default) |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **dns_prefix**  string | DNS prefix specified when creating the managed cluster. |
| **enable_rbac**  boolean | Enable RBAC.  Existing non-RBAC enabled AKS clusters cannot currently be updated for RBAC use.  **Choices:**   - `false` ← (default) - `true` |
| **kubernetes_version**  string | Version of Kubernetes specified when creating the managed cluster. |
| **linux_profile**  dictionary | The Linux profile suboptions.  Optional, provide if you need an ssh access to the cluster nodes. |
| **admin_username**  string / required | The Admin Username for the cluster. |
| **ssh_key**  string / required | The Public SSH Key used to access the cluster. |
| **location**  string | Valid azure location. Defaults to location of the resource group. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string / required | Name of the managed Azure Container Services (AKS) instance. |
| **network_profile**  dictionary | Profile of network configuration. |
| **dns_service_ip**  string | An IP address assigned to the Kubernetes DNS service.  It must be within the Kubernetes service address range specified in serviceCidr. |
| **docker_bridge_cidr**  string | A CIDR notation IP range assigned to the Docker bridge network.  It must not overlap with any Subnet IP ranges or the Kubernetes service address range. |
| **load_balancer_sku**  string | The load balancer sku for the managed cluster.  **Choices:**   - `"standard"` - `"basic"` |
| **network_plugin**  string | Network plugin used for building Kubernetes network.  This property cannot been changed.  With `kubenet`, nodes get an IP address from the Azure virtual network subnet.  AKS features such as Virtual Nodes or network policies aren’t supported with `kubenet`.  `azure` enables Azure Container Networking Interface(CNI), every pod gets an IP address from the subnet and can be accessed directly.  **Choices:**   - `"azure"` - `"kubenet"` |
| **network_policy**  string | Network policy used for building Kubernetes network.  **Choices:**   - `"azure"` - `"calico"` |
| **outbound_type**  string | How outbound traffic will be configured for a cluster.  **Choices:**   - `"loadBalancer"` ← (default) - `"userDefinedRouting"` |
| **pod_cidr**  string | A CIDR notation IP range from which to assign pod IPs when *network_plugin=kubenet* is used.  It should be a large address space that isn’t in use elsewhere in your network environment.  This address range must be large enough to accommodate the number of nodes that you expect to scale up to. |
| **service_cidr**  string | A CIDR notation IP range from which to assign service cluster IPs.  It must not overlap with any Subnet IP ranges.  It should be the \*.10 address of your service IP address range. |
| **node_resource_group**  string | Name of the resource group containing agent pool nodes.  Unable to update. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **resource_group**  string / required | Name of a resource group where the managed Azure Container Services (AKS) exists or will be created. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **service_principal**  dictionary | The service principal suboptions. If not provided - use system-assigned managed identity. |
| **client_id**  string / required | The ID for the Service Principal. |
| **client_secret**  string | The secret password associated with the service principal. |
| **state**  string | Assert the state of the AKS. Use `present` to create or update an AKS and `absent` to delete it.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_aks_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_aks_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_aks_module.md#id6)

```yaml+jinja
- name: Create an AKS instance With A System Node Pool & A User Node Pool
  azure_rm_aks:
    name: myAKS
    resource_group: myResourceGroup
    location: eastus
    dns_prefix: akstest
    kubernetes_version: 1.14.6
    linux_profile:
      admin_username: azureuser
      ssh_key: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAA...
    service_principal:
      client_id: "cf72ca99-f6b9-4004-b0e0-bee10c521948"
      client_secret: "Password1234!"
    agent_pool_profiles:
      - name: default
        count: 1
        vm_size: Standard_B2s
        enable_auto_scaling: true
        type: VirtualMachineScaleSets
        mode: System
        max_count: 3
        min_count: 1
        enable_rbac: true
      - name: user
        count: 1
        vm_size: Standard_D2_v2
        enable_auto_scaling: true
        type: VirtualMachineScaleSets
        mode: User
        max_count: 3
        min_count: 1
        enable_rbac: true

- name: Create a managed Azure Container Services (AKS) instance
  azure_rm_aks:
    name: myAKS
    location: eastus
    resource_group: myResourceGroup
    dns_prefix: akstest
    kubernetes_version: 1.14.6
    linux_profile:
      admin_username: azureuser
      ssh_key: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAA...
    service_principal:
      client_id: "cf72ca99-f6b9-4004-b0e0-bee10c521948"
      client_secret: "Password123!"
    agent_pool_profiles:
      - name: default
        count: 5
        mode: System
        vm_size: Standard_B2s
    tags:
      Environment: Production

- name: Use minimal parameters and system-assigned identity
  azure_rm_aks:
    name: myMinimalCluster
    location: eastus
    resource_group: myExistingResourceGroup
    dns_prefix: akstest
    agent_pool_profiles:
      - name: default
        count: 1
        vm_size: Standard_D2_v2

- name: Create AKS with userDefinedRouting "Link:https://docs.microsoft.com/en-us/azure/aks/limit-egress-traffic#add-a-dnat-rule-to-azure-firewall"
  azure_rm_aks:
    name: "minimal{{ rpfx }}"
    location: eastus
    resource_group: "{{ resource_group }}"
    kubernetes_version: "{{ versions.azure_aks_versions[0] }}"
    dns_prefix: "aks{{ rpfx }}"
    service_principal:
      client_id: "{{ client_id }}"
      client_secret: "{{ client_secret }}"
    network_profile:
      network_plugin: azure
      load_balancer_sku: standard
      outbound_type: userDefinedRouting
      service_cidr: "10.41.0.0/16"
      dns_service_ip: "10.41.0.10"
      docker_bridge_cidr: "172.17.0.1/16"
    api_server_access_profile:
      authorized_ip_ranges:
        - "20.106.246.252/32"
      enable_private_cluster: false
    agent_pool_profiles:
      - name: default
        count: 1
        vm_size: Standard_B2s
        mode: System
        vnet_subnet_id: "{{ output.subnets[0].id }}"
        type: VirtualMachineScaleSets
        enable_auto_scaling: false

- name: Remove a managed Azure Container Services (AKS) instance
  azure_rm_aks:
    name: myAKS
    resource_group: myResourceGroup
    state: absent
```

## [Return Values](azure_rm_aks_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **state**  dictionary | Current state of the Azure Container Service (AKS).  **Returned:** always  **Sample:** `{"agent_pool_profiles": [{"count": 1, "dns_prefix": null, "moode": "System", "name": "default", "node_labels": {"environment": "dev", "release": "stable"}, "os_disk_size_gb": null, "os_type": "Linux", "ports": null, "storage_profile": "ManagedDisks", "vm_size": "Standard_B2s", "vnet_subnet_id": null}], "changed": false, "dns_prefix": "aks9860bdcd89", "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourcegroups/myResourceGroup/providers/Microsoft.ContainerService/managedClusters/aks9860bdc", "kube_config": "......", "kubernetes_version": "1.14.6", "linux_profile": {"admin_username": "azureuser", "ssh_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADA....."}, "location": "eastus", "name": "aks9860bdc", "provisioning_state": "Succeeded", "service_principal_profile": {"client_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"}, "tags": {}, "type": "Microsoft.ContainerService/ManagedClusters"}` |

### Authors

- Sertac Ozercan (@sozercan)
- Yuwei Zhou (@yuwzho)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
