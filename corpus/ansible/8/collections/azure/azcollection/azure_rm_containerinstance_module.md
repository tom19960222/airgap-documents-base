---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_containerinstance module – Manage an Azure Container Instance"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_containerinstance_module.html
fetched_at: 2026-07-28T01:12:44+00:00
---
# azure.azcollection.azure_rm_containerinstance module – Manage an Azure Container Instance

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
> see [Requirements](azure_rm_containerinstance_module.md#ansible-collections-azure-azcollection-azure-rm-containerinstance-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_containerinstance`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_containerinstance_module.md#synopsis)
- [Requirements](azure_rm_containerinstance_module.md#requirements)
- [Parameters](azure_rm_containerinstance_module.md#parameters)
- [Notes](azure_rm_containerinstance_module.md#notes)
- [See Also](azure_rm_containerinstance_module.md#see-also)
- [Examples](azure_rm_containerinstance_module.md#examples)
- [Return Values](azure_rm_containerinstance_module.md#return-values)

## [Synopsis](azure_rm_containerinstance_module.md#id1)

- Create, update and delete an Azure Container Instance.

## [Requirements](azure_rm_containerinstance_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_containerinstance_module.md#id3)

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
| **containers**  list / elements=dictionary | List of containers.  Required when creation. |
| **commands**  list / elements=string | List of commands to execute within the container instance in exec form.  When updating existing container all existing commands will be replaced by new ones. |
| **cpu**  float | The required number of CPU cores of the containers.  **Default:** `1.0` |
| **environment_variables**  list / elements=dictionary | List of container environment variables.  When updating existing container all existing variables will be replaced by new ones. |
| **is_secure**  boolean | Is variable secure.  **Choices:**   - `false` - `true` |
| **name**  string / required | Environment variable name. |
| **value**  string / required | Environment variable value. |
| **image**  string / required | The container image name. |
| **memory**  float | The required memory of the containers in GB.  **Default:** `1.5` |
| **name**  string / required | The name of the container instance. |
| **ports**  list / elements=integer | List of ports exposed within the container group. |
| **volume_mounts**  list / elements=dictionary | The volume mounts for the container instance |
| **mount_path**  string / required | The path within the container where the volume should be mounted |
| **name**  string / required | The name of the volume mount |
| **read_only**  boolean | The flag indicating whether the volume mount is read-only  **Choices:**   - `false` - `true` |
| **dns_name_label**  string | The Dns name label for the IP. |
| **force_update**  boolean | Force update of existing container instance. Any update will result in deletion and recreation of existing containers.  **Choices:**   - `false` ← (default) - `true` |
| **ip_address**  string | The IP address type of the container group.  Default is `none` and creating an instance without public IP.  **Choices:**   - `"public"` - `"none"` ← (default) - `"private"` |
| **location**  string | Valid azure location. Defaults to location of the resource group. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string / required | The name of the container group. |
| **os_type**  string | The OS type of containers.  **Choices:**   - `"linux"` ← (default) - `"windows"` |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **ports**  list / elements=integer | List of ports exposed within the container group.  This option is deprecated, using *ports* under *containers*“.  **Default:** `[]` |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **registry_login_server**  string | The container image registry login server. |
| **registry_password**  string | The password to log in container image registry server. |
| **registry_username**  string | The username to log in container image registry server. |
| **resource_group**  string / required | Name of resource group. |
| **restart_policy**  string | Restart policy for all containers within the container group.  **Choices:**   - `"always"` - `"on_failure"` - `"never"` |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **state**  string | Assert the state of the container instance. Use `present` to create or update an container instance and `absent` to delete it.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **subnet_ids**  list / elements=string | The subnet resource IDs for a container group.  Multiple subnets are not yet supported. Only 1 subnet can be used. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **volumes**  list / elements=dictionary | List of Volumes that can be mounted by containers in this container group. |
| **azure_file**  dictionary | The Azure File volume |
| **read_only**  boolean | The flag indicating whether the Azure File shared mounted as a volume is read-only  **Choices:**   - `false` - `true` |
| **share_name**  string / required | The name of the Azure File share to be mounted as a volume |
| **storage_account_key**  string / required | The storage account access key used to access the Azure File share |
| **storage_account_name**  string / required | The name of the storage account that contains the Azure File share |
| **empty_dir**  dictionary | The empty directory volume |
| **git_repo**  dictionary | The git repo volume |
| **directory**  string | Target directory name |
| **repository**  string / required | Repository URL |
| **revision**  string | Commit hash for the specified revision |
| **name**  string / required | The name of the Volume |
| **secret**  dictionary | The secret volume |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_containerinstance_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_containerinstance_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_containerinstance_module.md#id6)

```yaml+jinja
- name: Create sample container group
  azure_rm_containerinstance:
    resource_group: myResourceGroup
    name: myContainerInstanceGroup
    os_type: linux
    ip_address: public
    containers:
      - name: myContainer1
        image: httpd
        memory: 1.5
        ports:
          - 80
          - 81

- name: Create sample container group with azure file share volume
  azure_rm_containerinstance:
    resource_group: myResourceGroup
    name: myContainerInstanceGroupz
    os_type: linux
    ip_address: public
    containers:
      - name: mycontainer1
        image: httpd
        memory: 1
        volume_mounts:
          - name: filesharevolume
            mount_path: "/data/files"
        ports:
          - 80
          - 81
    volumes:
      - name: filesharevolume
        azure_file:
          storage_account_name: mystorageaccount
          share_name: acishare
          storage_account_key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

- name: Create sample container group with git repo volume
  azure_rm_containerinstance:
    resource_group: myResourceGroup
    name: myContainerInstanceGroup
    os_type: linux
    ip_address: public
    containers:
      - name: mycontainer1
        image: httpd
        memory: 1
        volume_mounts:
          - name: myvolume1
            mount_path: "/mnt/test"
        ports:
          - 80
          - 81
    volumes:
      - name: myvolume1
        git_repo:
          repository: "https://github.com/Azure-Samples/aci-helloworld.git"

- name: Create sample container instance with subnet
  azure_rm_containerinstance:
    resource_group: myResourceGroup
    name: myContainerInstanceGroup
    os_type: linux
    ip_address: private
    location: eastus
    subnet_ids:
      - "{{ subnet_id }}"
    ports:
      - 80
    containers:
      - name: mycontainer1
        image: httpd
        memory: 1.5
        ports:
          - 80
          - 81
```

## [Return Values](azure_rm_containerinstance_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **containers**  list / elements=dictionary | The containers within the container group.  **Returned:** always  **Sample:** `[{"commands": null, "cpu": 1.0, "environment_variables": null, "image": "httpd", "memory": 1.0, "name": "mycontainer1", "ports": [80, 81], "volume_mounts": [{"mount_path": "/data/files", "name": "filesharevolume", "read_only": false}]}]` |
| **id**  string | Resource ID.  **Returned:** always  **Sample:** `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.ContainerInstance/containerGroups/aci1b6dd89"` |
| **ip_address**  string | Public IP Address of created container group.  **Returned:** if address is public  **Sample:** `"175.12.233.11"` |
| **provisioning_state**  string | Provisioning state of the container.  **Returned:** always  **Sample:** `"Creating"` |
| **volumes**  list / elements=dictionary | The list of volumes that mounted by containers in container group  **Returned:** if volumes specified |
| **azure_file**  dictionary | Azure file share volume details  **Returned:** If Azure file share type of volume requested  **Sample:** `{"read_only": null, "share_name": "acishare", "storage_account_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "storage_account_name": "mystorageaccount"}` |
| **empty_dir**  dictionary | Empty directory volume details  **Returned:** If Empty directory type of volume requested  **Sample:** `{}` |
| **git_repo**  dictionary | Git Repo volume details  **Returned:** If Git repo type of volume requested  **Sample:** `{"directory": null, "repository": "https://github.com/Azure-Samples/aci-helloworld.git", "revision": null}` |
| **name**  string | The name of the Volume  **Returned:** always  **Sample:** `"filesharevolume"` |
| **secret**  dictionary | Secret volume details  **Returned:** If Secret type of volume requested  **Sample:** `{}` |

### Authors

- Zim Kalinowski (@zikalino)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
