---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_storageblob module – Manage blob containers and blob objects"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_storageblob_module.html
fetched_at: 2026-07-28T01:14:57+00:00
---
# azure.azcollection.azure_rm_storageblob module – Manage blob containers and blob objects

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
> see [Requirements](azure_rm_storageblob_module.md#ansible-collections-azure-azcollection-azure-rm-storageblob-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_storageblob`.

New in azure.azcollection 0.0.1

- [Synopsis](azure_rm_storageblob_module.md#synopsis)
- [Requirements](azure_rm_storageblob_module.md#requirements)
- [Parameters](azure_rm_storageblob_module.md#parameters)
- [Notes](azure_rm_storageblob_module.md#notes)
- [See Also](azure_rm_storageblob_module.md#see-also)
- [Examples](azure_rm_storageblob_module.md#examples)
- [Return Values](azure_rm_storageblob_module.md#return-values)

## [Synopsis](azure_rm_storageblob_module.md#id1)

- Create, update and delete blob containers and blob objects.
- Use to upload a file and store it as a blob object, or download a blob object to a file(upload and download mode)
- Use to upload a batch of files under a given directory(batch upload mode)
- In the batch upload mode, the existing blob object will be overwritten if a blob object with the same name is to be created.
- the module can work exclusively in three modes, when `batch_upload_src` is set, it is working in batch upload mode; when `src` is set, it is working in upload mode and when `dst` is set, it is working in dowload mode.

## [Requirements](azure_rm_storageblob_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_storageblob_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **append_tags**  boolean | Use to control if tags field is canonical or just appends to existing tags.  When canonical, any tags not found in the tags parameter will be removed from the object’s metadata.  **Choices:**   - `false` - `true` ← (default) |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **batch_upload_dst**  path | Base directory in container when upload batch of files. |
| **batch_upload_src**  path | Batch upload source directory. Use with state `present` to upload batch of files under the directory. |
| **blob**  aliases: blob_name  string | Name of a blob object within the container. |
| **blob_type**  string  *added in azure.azcollection 0.0.1* | Type of blob object.  **Choices:**   - `"block"` ← (default) - `"page"` |
| **cache_control**  string | Set the blob cache-control header. |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **container**  aliases: container_name  string / required | Name of a blob container within the storage account. |
| **content_disposition**  string | Set the blob content-disposition header. |
| **content_encoding**  string | Set the blob encoding header. |
| **content_language**  string | Set the blob content-language header. |
| **content_md5**  string | Set the blob md5 hash value. |
| **content_type**  string | Set the blob content-type header. For example `image/png`. |
| **dest**  aliases: destination  path | Destination file path. Use with state `present` to download a blob. |
| **force**  boolean | Overwrite existing blob or file when uploading or downloading. Force deletion of a container that contains blobs.  **Choices:**   - `false` ← (default) - `true` |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **public_access**  string | A container’s level of public access. By default containers are private.  Can only be set at time of container creation.  **Choices:**   - `"container"` - `"blob"` |
| **resource_group**  aliases: resource_group_name  string / required | Name of the resource group to use. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **src**  aliases: source  string | Source file path. Use with state `present` to upload a blob. |
| **state**  string | State of a container or blob.  Use state `absent` with a container value only to delete a container. Include a blob value to remove a specific blob. A container will not be deleted, if it contains blobs. Use the *force* option to override, deleting the container and all associated blobs.  Use state `present` to create or update a container and upload or download a blob. If the container does not exist, it will be created. If it exists, it will be updated with configuration options. Provide a blob name and either src or dest to upload or download. Provide a src path to upload and a dest path to download. If a blob (uploading) or a file (downloading) already exists, it will not be overwritten unless *force=true*.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **storage_account_name**  aliases: account_name, storage_account  string / required | Name of the storage account to use. |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  dictionary | Dictionary of string:string pairs to assign as metadata to the object.  Metadata tags on the object will be updated with any provided values.  To remove tags set append_tags option to false.  Currently, Azure DNS zones and Traffic Manager services also don’t allow the use of spaces in the tag.  Azure Front Door doesn’t support the use of  Azure Automation and Azure CDN only support 15 tags on resources. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_storageblob_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_storageblob_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_storageblob_module.md#id6)

```yaml+jinja
- name: Remove container foo
  azure_rm_storageblob:
    resource_group: myResourceGroup
    storage_account_name: clh0002
    container: foo
    state: absent

- name: Create container foo and upload a file
  azure_rm_storageblob:
    resource_group: myResourceGroup
    storage_account_name: clh0002
    container: foo
    blob: graylog.png
    src: ./files/graylog.png
    public_access: container
    content_type: 'application/image'

- name: Download the file
  azure_rm_storageblob:
    resource_group: myResourceGroup
    storage_account_name: clh0002
    container: foo
    blob: graylog.png
    dest: ~/tmp/images/graylog.png
```

## [Return Values](azure_rm_storageblob_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **blob**  dictionary | Facts about the current state of the blob.  **Returned:** when a blob is operated on  **Sample:** `{"content_length": 136532, "content_settings": {"cache_control": null, "content_disposition": null, "content_encoding": null, "content_language": null, "content_md5": null, "content_type": "application/image"}, "last_modified": "09-Mar-2016 22:08:25 +0000", "name": "graylog.png", "tags": {}, "type": "BlockBlob"}` |
| **container**  dictionary | Facts about the current state of the selected container.  **Returned:** always  **Sample:** `{"last_modified": "09-Mar-2016 19:28:26 +0000", "name": "foo", "tags": {}}` |

### Authors

- Chris Houseknecht (@chouseknecht)
- Matt Davis (@nitzmahone)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
