---
collection: ansible
version: "6"
title: "dellemc.openmanage.ome_firmware_catalog module – Create, modify, or delete a firmware catalog on OpenManage Enterprise or OpenManage Enterprise Modular"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/ome_firmware_catalog_module.html
fetched_at: 2026-07-27T17:25:42+00:00
---
# dellemc.openmanage.ome_firmware_catalog module – Create, modify, or delete a firmware catalog on OpenManage Enterprise or OpenManage Enterprise Modular

> **Note:**
>
> This module is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/dellemc/openmanage) (version 5.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.openmanage`.
> You need further requirements to be able to use this module,
> see [Requirements](ome_firmware_catalog_module.md#ansible-collections-dellemc-openmanage-ome-firmware-catalog-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_firmware_catalog`.

New in dellemc.openmanage 2.0.0

- [Synopsis](ome_firmware_catalog_module.md#synopsis)
- [Requirements](ome_firmware_catalog_module.md#requirements)
- [Parameters](ome_firmware_catalog_module.md#parameters)
- [Notes](ome_firmware_catalog_module.md#notes)
- [Examples](ome_firmware_catalog_module.md#examples)
- [Return Values](ome_firmware_catalog_module.md#return-values)

## [Synopsis](ome_firmware_catalog_module.md#id1)

- This module allows to create, modify, or delete a firmware catalog on OpenManage Enterprise or OpenManage Enterprise Modular.

## [Requirements](ome_firmware_catalog_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_firmware_catalog_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **catalog_description**  string | Description for the catalog. |
| **catalog_id**  list / elements=integer  added in dellemc.openmanage 3.4.0 | ID of the catalog.  This option is mutually exclusive with *catalog_name*.  Provide the list of firmware catalog IDs that are supported when *state* is `absent`. |
| **catalog_name**  list / elements=string | Name of the firmware catalog to be created.  This option is mutually exclusive with *catalog_id*.  Provide the list of firmware catalog names that are supported when *state* is `absent`. |
| **check_certificate**  boolean | The certificate warnings are ignored when *repository_type* is HTTPS. If `True`. If not, certificate warnings are not ignored.  Choices:   - `false` ← (default) - `true` |
| **file_name**  string | Catalog file name associated with the *source_path*.  This option is ignored when *repository_type* is `DELL_ONLINE`. |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **job_wait**  boolean  added in dellemc.openmanage 3.4.0 | Provides the option to wait for job completion.  This option is applicable when *state* is `present`.  Choices:   - `false` - `true` ← (default) |
| **job_wait_timeout**  integer  added in dellemc.openmanage 3.4.0 | The maximum wait time of *job_wait* in seconds. The job is tracked only for this duration.  This option is applicable when *job_wait* is `True`.  Default: `600` |
| **new_catalog_name**  string  added in dellemc.openmanage 3.4.0 | New name of the firmware catalog. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  Default: `443` |
| **repository_domain**  string | Domain name of the repository.  This option is ignored when *repository_type* is `DELL_ONLINE`. |
| **repository_password**  string | Password to access the repository.  This option is mandatory when *repository_type* is CIFS.  This option is ignored when *repository_type* is `DELL_ONLINE`.  `NOTE` The module always reports the changed status, when this is provided. |
| **repository_type**  string | Type of repository. The supported types are NFS, CIFS, HTTP, HTTPS,and DELL_ONLINE.  Choices:   - `"NFS"` - `"CIFS"` - `"HTTP"` - `"HTTPS"` - `"DELL_ONLINE"` |
| **repository_username**  string | User name of the repository where the catalog is stored.  This option is mandatory when *repository_type* is CIFS.  This option is ignored when *repository_type* is `DELL_ONLINE`. |
| **source**  string | The IP address of the system where the firmware catalog is stored on the local network.  By default, this option is set to downloads.dell.com when *repository_type* is `DELL_ONLINE`. |
| **source_path**  string | Specify the complete path of the catalog file location without the file name.  This is option ignored when *repository_type* is `DELL_ONLINE`. |
| **state**  string  added in dellemc.openmanage 3.4.0 | `present` creates or modifies a catalog.  `absent` deletes an existing catalog.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](ome_firmware_catalog_module.md#id4)

> **Note:**
>
> - If *repository_password* is provided, then the module always reports the changed status.
> - Run this module from a system that has direct access to DellEMC OpenManage Enterprise or OpenManage Enterprise Modular.
> - This module supports `check_mode`.

## [Examples](ome_firmware_catalog_module.md#id5)

```yaml+jinja
---
- name: Create a catalog from HTTPS repository
  dellemc.openmanage.ome_firmware_catalog:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    catalog_name: "catalog_name"
    catalog_description: "catalog_description"
    repository_type: "HTTPS"
    source: "downloads.dell.com"
    source_path: "catalog"
    file_name: "catalog.gz"
    check_certificate: True

- name: Create a catalog from HTTP repository
  dellemc.openmanage.ome_firmware_catalog:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    catalog_name: "catalog_name"
    catalog_description: "catalog_description"
    repository_type: "HTTP"
    source: "downloads.dell.com"
    source_path: "catalog"
    file_name: "catalog.gz"

- name: Create a catalog using CIFS share
  dellemc.openmanage.ome_firmware_catalog:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    catalog_name: "catalog_name"
    catalog_description: "catalog_description"
    repository_type: "CIFS"
    source: "192.167.0.1"
    source_path: "cifs/R940"
    file_name: "catalog.gz"
    repository_username: "repository_username"
    repository_password: "repository_password"
    repository_domain: "repository_domain"

- name: Create a catalog using NFS share
  dellemc.openmanage.ome_firmware_catalog:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    catalog_name: "catalog_name"
    catalog_description: "catalog_description"
    repository_type: "NFS"
    source: "192.166.0.2"
    source_path: "/nfs/R940"
    file_name: "catalog.xml"

- name: Create a catalog using repository from Dell.com
  dellemc.openmanage.ome_firmware_catalog:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    catalog_name: "catalog_name"
    catalog_description: "catalog_description"
    repository_type: "DELL_ONLINE"
    check_certificate: True

- name: Modify a catalog using a repository from CIFS share
  dellemc.openmanage.ome_firmware_catalog:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    catalog_name: "catalog_name"
    catalog_description: "new catalog_description"
    repository_type: "CIFS"
    source: "192.167.0.2"
    source_path: "cifs/R941"
    file_name: "catalog1.gz"
    repository_username: "repository_username"
    repository_password: "repository_password"
    repository_domain: "repository_domain"

- name: Modify a catalog using a repository from Dell.com
  dellemc.openmanage.ome_firmware_catalog:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    catalog_id: 10
    new_catalog_name: "new_catalog_name"
    repository_type: "DELL_ONLINE"
    catalog_description: "catalog_description"

- name: Delete catalog using catalog name
  dellemc.openmanage.ome_firmware_catalog:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: absent
    catalog_name: ["catalog_name1", "catalog_name2"]

- name: Delete catalog using catalog id
  dellemc.openmanage.ome_firmware_catalog:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: absent
    catalog_id: [11, 34]
```

## [Return Values](ome_firmware_catalog_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **associated_baselines**  list / elements=dictionary | IDs of the baselines associated with catalog.  Returned: When *state* is `absent`  Sample: `[{"BaselineId": 24, "BaselineName": "new"}, {"BaselineId": 25, "BaselineName": "c7"}, {"BaselineId": 27, "BaselineName": "c4"}]` |
| **catalog_id**  integer | IDs of the deleted catalog.  Returned: When *state* is `absent`  Sample: `10123` |
| **catalog_status**  dictionary | Details of the catalog operation.  Returned: When *state* is `present`  Sample: `{"AssociatedBaselines": [], "BaseLocation": null, "BundlesCount": 0, "Filename": "catalog.gz", "Id": 0, "LastUpdated": null, "ManifestIdentifier": null, "ManifestVersion": null, "NextUpdate": null, "PredecessorIdentifier": null, "ReleaseDate": null, "ReleaseIdentifier": null, "Repository": {"CheckCertificate": true, "Description": "HTTPS Desc", "DomainName": null, "Id": null, "Name": "catalog4", "Password": null, "RepositoryType": "HTTPS", "Source": "company.com", "Username": null}, "Schedule": null, "SourcePath": "catalog", "Status": null, "TaskId": 10094}` |
| **error_info**  dictionary | Details of the http error.  Returned: on http error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to create or update the catalog because a repository with the same name already exists.", "Resolution": "Enter a different name and retry the operation.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **job_id**  integer | Job ID of the catalog task.  Returned: When catalog job is in a running state  Sample: `10123` |
| **msg**  string | Overall status of the firmware catalog operation.  Returned: always  Sample: `"Successfully triggered the job to create a catalog with Task ID : 10094"` |

### Authors

- Sajna Shetty(@Sajna-Shetty)
- Jagadeesh N V(@jagadeeshnv)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
