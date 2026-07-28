---
collection: ansible
version: "6"
title: "theforeman.foreman.content_upload module – Upload content to a repository"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/content_upload_module.html
fetched_at: 2026-07-28T00:20:36+00:00
---
# theforeman.foreman.content_upload module – Upload content to a repository

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/theforeman/foreman) (version 3.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](content_upload_module.md#ansible-collections-theforeman-foreman-content-upload-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.content_upload`.

New in theforeman.foreman 1.0.0

- [Synopsis](content_upload_module.md#synopsis)
- [Requirements](content_upload_module.md#requirements)
- [Parameters](content_upload_module.md#parameters)
- [Notes](content_upload_module.md#notes)
- [Examples](content_upload_module.md#examples)

## [Synopsis](content_upload_module.md#id1)

- Allows the upload of content to a repository

## [Requirements](content_upload_module.md#id2)

The below requirements are needed on the host that executes this module.

- python-debian (For deb Package upload)
- requests
- rpm (For rpm upload)

## [Parameters](content_upload_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **organization**  string / required | Organization that the entity is in |
| **ostree_repository_name**  string | Name of repository within the OSTree archive.  Required for OSTree uploads. |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **product**  string / required | Product to which the repository lives in |
| **repository**  string / required | Repository to upload file in to |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **src**  aliases: file  path / required | File (on the remote/target machine) to upload |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Notes](content_upload_module.md#id4)

> **Note:**
>
> - Currently only uploading to deb, RPM, OSTree & file repositories is supported
> - For anything but file repositories, a supporting library must be installed. See Requirements.
> - OSTree content upload is not idempotent - running mutliple times will attempt to upload the content unit.

## [Examples](content_upload_module.md#id5)

```yaml+jinja
- name: "Upload my.rpm"
  theforeman.foreman.content_upload:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    src: "my.rpm"
    repository: "Build RPMs"
    product: "My Product"
    organization: "Default Organization"

- name: "Upload ostree-archive.tar"
  theforeman.foreman.content_upload:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    src: "ostree_archive.tar"
    repository: "My OStree Repository"
    product: "My Product"
    organization: "Default Organization"
    ostree_repository_name: "small"
```

### Authors

- Eric D Helms (@ehelms)

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
