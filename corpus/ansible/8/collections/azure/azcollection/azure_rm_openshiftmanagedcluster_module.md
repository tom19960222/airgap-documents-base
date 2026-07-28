---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_openshiftmanagedcluster module – Manage Azure Red Hat OpenShift Managed Cluster instance"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_openshiftmanagedcluster_module.html
fetched_at: 2026-07-28T01:14:07+00:00
---
# azure.azcollection.azure_rm_openshiftmanagedcluster module – Manage Azure Red Hat OpenShift Managed Cluster instance

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
> see [Requirements](azure_rm_openshiftmanagedcluster_module.md#ansible-collections-azure-azcollection-azure-rm-openshiftmanagedcluster-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_openshiftmanagedcluster`.

New in azure.azcollection 1.2.0

- [Synopsis](azure_rm_openshiftmanagedcluster_module.md#synopsis)
- [Requirements](azure_rm_openshiftmanagedcluster_module.md#requirements)
- [Parameters](azure_rm_openshiftmanagedcluster_module.md#parameters)
- [Notes](azure_rm_openshiftmanagedcluster_module.md#notes)
- [See Also](azure_rm_openshiftmanagedcluster_module.md#see-also)
- [Examples](azure_rm_openshiftmanagedcluster_module.md#examples)
- [Return Values](azure_rm_openshiftmanagedcluster_module.md#return-values)

## [Synopsis](azure_rm_openshiftmanagedcluster_module.md#id1)

- Create, update and delete instance of Azure Red Hat OpenShift Managed Cluster instance.

## [Requirements](azure_rm_openshiftmanagedcluster_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_openshiftmanagedcluster_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **api_server_profile**  dictionary | API server configuration. |
| **ip**  string | IP address of api server (immutable), only appears in response. |
| **url**  string | Url of api server (immutable), only appears in response. |
| **visibility**  string | API server visibility.  **Choices:**   - `"Public"` ← (default) - `"Private"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  **Choices:**   - `false` - `true` ← (default) |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **cluster_profile**  dictionary | Configuration for OpenShift cluster.  **Default:** `{}` |
| **cluster_resource_group_id**  string | The ID of the cluster resource group (immutable). |
| **domain**  string | The domain for the cluster (immutable). |
| **pull_secret**  string | Pull secret for the cluster (immutable). |
| **version**  string | The Openshift version (immutable). |
| **ingress_profiles**  list / elements=dictionary | Ingress profiles configuration. only one profile is supported at the current API version. |
| **ip**  string | IP of the ingress (immutable), only appears in response. |
| **name**  string | Name of the ingress (immutable).  **Choices:**   - `"default"` ← (default) |
| **visibility**  string | Ingress visibility.  **Choices:**   - `"Public"` ← (default) - `"Private"` |
| **location**  string / required | Resource location. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **master_profile**  dictionary | Configuration for OpenShift master VMs. |
| **subnet_id**  string / required | The Azure resource ID of the master subnet (immutable). |
| **vm_size**  string | Size of agent VMs (immutable).  **Choices:**   - `"Standard_D8s_v3"` - `"Standard_D16s_v3"` - `"Standard_D32s_v3"` |
| **name**  string / required | Resource name. |
| **network_profile**  dictionary | Configuration for OpenShift networking (immutable).  **Default:** `{"pod_cidr": "10.128.0.0/14", "service_cidr": "172.30.0.0/16"}` |
| **pod_cidr**  string | CIDR for the OpenShift Pods (immutable). |
| **service_cidr**  string | CIDR for OpenShift Services (immutable). |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **provisioning_state**  string | The current deployment or provisioning state, which only appears in the response. |
| **resource_group**  string / required | The name of the resource group. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **service_principal_profile**  dictionary | service principal. |
| **client_id**  string / required | Client ID of the service principal (immutable). |
| **client_secret**  string / required | Client secret of the service principal (immutable). |
| **state**  string | Assert the state of the OpenShiftManagedCluster.  Use `present` to create or update an OpenShiftManagedCluster and `absent` to delete it.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **worker_profiles**  list / elements=dictionary | Configuration for OpenShift worker Vms. |
| **count**  integer | The number of worker VMs. Must be between 3 and 20 (immutable). |
| **disk_size**  integer | The disk size of the worker VMs in GB. Must be 128 or greater (immutable). |
| **name**  string / required | name of the worker profile (immutable).  **Choices:**   - `"worker"` |
| **subnet_id**  string / required | The Azure resource ID of the worker subnet (immutable). |
| **vm_size**  string | The size of the worker Vms (immutable).  **Choices:**   - `"Standard_D4s_v3"` - `"Standard_D8s_v3"` |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_openshiftmanagedcluster_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_openshiftmanagedcluster_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_openshiftmanagedcluster_module.md#id6)

```yaml+jinja
- name: Create openshift cluster
  azure_rm_openshiftmanagedcluster:
    resource_group: "myResourceGroup"
    name: "myCluster"
    location: "eastus"
    cluster_profile:
      cluster_resource_group_id: "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/clusterResourceGroup"
      domain: "mydomain"
    service_principal_profile:
      client_id: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
      client_secret: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    network_profile:
      pod_cidr: "10.128.0.0/14"
      service_cidr: "172.30.0.0/16"
    worker_profiles:
      - vm_size: "Standard_D4s_v3"
        subnet_id: "/subscriptions/xx-xx-xx-xx-xx/resourceGroups/myResourceGroup/Microsoft.Network/virtualNetworks/myVnet/subnets/worker"
        disk_size: 128
        count: 3
    master_profile:
      vm_size: "Standard_D8s_v3"
      subnet_id: "/subscriptions/xx-xx-xx-xx-xx/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/myVnet/subnets/master"
- name: Delete OpenShift Managed Cluster
  azure_rm_openshiftmanagedcluster:
    resource_group: myResourceGroup
    name: myCluster
    location: eastus
    state: absent
```

## [Return Values](azure_rm_openshiftmanagedcluster_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | Resource ID.  **Returned:** always  **Sample:** `"/subscriptions/xx-xx-xx-xx/resourceGroups/mycluster-eastus/providers/Microsoft.RedHatOpenShift/openShiftClusters/mycluster"` |
| **location**  string | Resource location.  **Returned:** always  **Sample:** `"eatus"` |
| **name**  string | Resource name.  **Returned:** always  **Sample:** `"mycluster"` |
| **properties**  complex | Properties of a OpenShift managed cluster.  **Returned:** always |
| **apiserverProfile**  complex | API server configuration.  **Returned:** always |
| **visibility**  string | api server visibility.  **Returned:** always  **Sample:** `"Public"` |
| **clusterProfile**  complex | Configuration for Openshift cluster.  **Returned:** always |
| **domain**  string | Domain for the cluster.  **Returned:** always  **Sample:** `"mycluster"` |
| **resourceGroupId**  string | The ID of the cluster resource group.  **Returned:** always  **Sample:** `"/subscriptions/xx-xx-xx-xx/resourceGroups/mycluster-eastus-cluster"` |
| **version**  string | Openshift version.  **Returned:** always  **Sample:** `"4.4.17"` |
| **ingressProfiles**  list / elements=string | Ingress configruation.  **Returned:** always  **Sample:** `[{"name": "default", "visibility": "Public"}]` |
| **masterProfile**  complex | Configuration for OpenShift master VMs.  **Returned:** always |
| **subnetId**  string | The Azure resource ID of the master subnet (immutable).  **Returned:** always  **Sample:** `"/subscriptions/xx-xx-xx-xx/resourceGroups/mycluster-eastus/providers/Microsoft.Network/ virtualNetworks/mycluster-vnet/subnets/mycluster-worker"` |
| **vmSize**  string | Size of agent VMs (immutable).  **Returned:** always  **Sample:** `"Standard_D8s_v3"` |
| **networkProfile**  complex | Configuration for OpenShift networking.  **Returned:** always |
| **podCidr**  string | CIDR for the OpenShift Pods.  **Returned:** always  **Sample:** `"10.128.0.0/14"` |
| **serviceCidr**  string | CIDR for OpenShift Services.  **Returned:** always  **Sample:** `"172.30.0.0/16"` |
| **provisioningState**  string | The current deployment or provisioning state, which only appears in the response.  **Returned:** always  **Sample:** `"Creating"` |
| **servicePrincipalProfile**  complex | Service principal.  **Returned:** always |
| **clientId**  string | Client ID of the service principal.  **Returned:** always  **Sample:** `"xxxxxxxx-xxxx-xxxx-xxxxxxxxxxxx"` |
| **workerProfiles**  complex | Configuration of OpenShift cluster VMs.  **Returned:** always |
| **count**  integer | Number of agents (VMs) to host docker containers.  **Returned:** always  **Sample:** `3` |
| **diskSizeGB**  integer | disk size in GB.  **Returned:** always  **Sample:** `128` |
| **name**  string | Unique name of the pool profile in the context of the subscription and resource group.  **Returned:** always  **Sample:** `"worker"` |
| **subnetId**  string | Subnet ID for worker pool.  **Returned:** always  **Sample:** `"/subscriptions/xx-xx-xx-xx/resourceGroups/mycluster-eastus/providers/Microsoft.Network/ virtualNetworks/mycluster-vnet/subnets/mycluster-worker"` |
| **vmSize**  string | Size of agent VMs.  **Returned:** always  **Sample:** `"Standard_D4s_v3"` |
| **type**  string | Resource type.  **Returned:** always  **Sample:** `"Microsoft.RedHatOpenShift/openShiftClusters"` |

### Authors

- Haiyuan Zhang (@haiyuazhang)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
