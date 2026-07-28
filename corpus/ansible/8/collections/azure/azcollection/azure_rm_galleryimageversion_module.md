---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_galleryimageversion module – Manage Azure SIG Image Version instance"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_galleryimageversion_module.html
fetched_at: 2026-07-28T01:13:25+00:00
---
# azure.azcollection.azure_rm_galleryimageversion module – Manage Azure SIG Image Version instance

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
> see [Requirements](azure_rm_galleryimageversion_module.md#ansible-collections-azure-azcollection-azure-rm-galleryimageversion-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_galleryimageversion`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_galleryimageversion_module.md#synopsis)
- [Requirements](azure_rm_galleryimageversion_module.md#requirements)
- [Parameters](azure_rm_galleryimageversion_module.md#parameters)
- [Notes](azure_rm_galleryimageversion_module.md#notes)
- [See Also](azure_rm_galleryimageversion_module.md#see-also)
- [Examples](azure_rm_galleryimageversion_module.md#examples)
- [Return Values](azure_rm_galleryimageversion_module.md#return-values)

## [Synopsis](azure_rm_galleryimageversion_module.md#id1)

- Create, update and delete instance of Azure SIG Image Version.

## [Requirements](azure_rm_galleryimageversion_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_galleryimageversion_module.md#id3)

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
| **gallery_image_name**  string / required | The name of the gallery Image Definition in which the Image Version is to be created. |
| **gallery_name**  string / required | The name of the Shared Image Gallery in which the Image Definition resides. |
| **location**  string | Resource location. |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string / required | The name of the gallery Image Version to be created.  Needs to follow semantic version name pattern, The allowed characters are digit and period.  Digits must be within the range of a 32-bit integer. For example <MajorVersion>.<MinorVersion>.<Patch>. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **publishing_profile**  dictionary | Publishing profile. |
| **end_of_life_date**  string | The end of life date of the gallery Image Version.  This property can be used for decommissioning purposes.  This property is updatable. Format should be according to ISO-8601, for instance “2019-06-26”. |
| **exclude_from_latest**  boolean | If *exclude_from_latest=true*, Virtual Machines deployed from the latest version of the Image Definition won’t use this Image Version.  **Choices:**   - `false` - `true` |
| **managed_image**  any | Managed image reference, could be resource ID, or dictionary containing *resource_group* and *name*  Obsolete since 2.10, use storage_profile instead |
| **replica_count**  integer | The number of replicas of the Image Version to be created per region.  This property would take effect for a region when regionalReplicaCount is not specified.  This property is updatable. |
| **snapshot**  any | Source snapshot to be used.  Obsolete since 2.10, use storage_profile instead |
| **storage_account_type**  string | Specifies the storage account type to be used to store the image.  This property is not updatable.  **Choices:**   - `"Standard_LRS"` - `"Standard_ZRS"` |
| **target_regions**  list / elements=any | The target regions where the Image Version is going to be replicated to.  This property is updatable. |
| **name**  string / required | Region name. |
| **regional_replica_count**  integer | The number of replicas of the Image Version to be created per region.  This property would take effect for a region when regionalReplicaCount is not specified.  This property is updatable. |
| **storage_account_type**  string | Storage account type. |
| **resource_group**  string / required | The name of the resource group. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **state**  string | Assert the state of the GalleryImageVersion.  Use `present` to create or update an GalleryImageVersion and `absent` to delete it.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **storage_profile**  dictionary | Storage profile  Required when creating. |
| **data_disks**  list / elements=any | list of data disk snapshot  Mutual exclusive with source_image |
| **host_caching**  string | host disk caching  **Choices:**   - `"None"` ← (default) - `"ReadOnly"` - `"ReadWrite"` |
| **lun**  integer | lun of the data disk |
| **source**  any | Reference to data disk snapshot. Could be resource ID or dictionary containing *resource_group* and *name* |
| **os_disk**  dictionary | os disk snapshot  Mutual exclusive with source_image |
| **host_caching**  string | host disk caching  **Choices:**   - `"None"` ← (default) - `"ReadOnly"` - `"ReadWrite"` |
| **source**  any | Reference to os disk snapshot. Could be resource ID or dictionary containing *resource_group* and *name* |
| **source_image**  any | Reference to managed image or gallery image version  Could be resource ID to managed image, or dictionary containing *resource_group* and *name*  Could be resource ID to image version, or dictionary containing *resource_group*,*gallery_name*, *gallery_image_name* and *version*  Mutual exclusive with os_disk and data_disks |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_galleryimageversion_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_galleryimageversion_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_galleryimageversion_module.md#id6)

```yaml+jinja
- name: Create a gallery image version form a managed image
  azure_rm_galleryimageversion:
    resource_group: myResourceGroup
    gallery_name: myGallery
    gallery_image_name: myGalleryImage
    name: 1.1.0
    location: East US
    publishing_profile:
      end_of_life_date: "2020-10-01t00:00:00+00:00"
      exclude_from_latest: true
      replica_count: 4
      storage_account_type: Standard_LRS
      target_regions:
        - name: West US
          regional_replica_count: 1
        - name: East US
          regional_replica_count: 3
          storage_account_type: Standard_LRS
    storage_profile:
      source_image: /subscriptions/sub123/resourceGroups/group123/providers/Microsoft.Compute/images/myOsImage

- name: Create a gallery image version from another gallery image version
  azure_rm_galleryimageversion:
    resource_group: myResourceGroup
    gallery_name: myGallery
    gallery_image_name: myGalleryImage
    name: 1.2.0
    location: East US
    publishing_profile:
      end_of_life_date: "2020-10-01t00:00:00+00:00"
      exclude_from_latest: true
      replica_count: 4
      storage_account_type: Standard_LRS
      target_regions:
        - name: West US
          regional_replica_count: 1
        - name: East US
          regional_replica_count: 3
          storage_account_type: Standard_LRS
    storage_profile:
      source_image:
        version: 1.1.0
        gallery_name: myGallery2
        gallery_image_name: myGalleryImage2

- name: Create gallery image by using one os dist snapshot and zero or many data disk snapshots
  azure_rm_galleryimageversion:
    resource_group: myRsourceGroup
    gallery_name: myGallery
    gallery_image_name: myGalleryImage
    name: 3.4.0
    location: East  US
    publishing_profile:
      end_of_life_date: "2020-10-01t00:00:00+00:00"
      exclude_from_latest: true
      replica_count: 1
      storage_account_type: Standard_LRS
      target_regions:
        - name: East US
          regional_replica_count: 1
          storage_account_type: Standard_LRS
    storage_profile:
      os_disk:
        source: "/subscriptions/mySub/resourceGroups/myGroup/providers/Microsoft.Compute/snapshots/os_snapshot_vma"
      data_disks:
        - lun: 0
          source:
            name: data_snapshot_vma
        - lun: 1
          source: "/subscriptions/mySub/resourceGroups/myGroup/providers/Microsoft.Compute/snapshots/data_snapshot_vmb"
```

## [Return Values](azure_rm_galleryimageversion_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | Resource ID.  **Returned:** always  **Sample:** `"/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.Compute/galleries/myGalle ry1283/images/myImage/versions/10.1.3"` |

### Authors

- Zim Kalinowski (@zikalino)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
