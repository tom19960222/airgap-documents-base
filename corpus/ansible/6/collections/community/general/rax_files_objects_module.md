---
collection: ansible
version: "6"
title: "community.general.rax_files_objects module – Upload, download, and delete objects in Rackspace Cloud Files"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/rax_files_objects_module.html
fetched_at: 2026-07-27T17:12:26+00:00
---
# community.general.rax_files_objects module – Upload, download, and delete objects in Rackspace Cloud Files

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](rax_files_objects_module.md#ansible-collections-community-general-rax-files-objects-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.rax_files_objects`.

- [Synopsis](rax_files_objects_module.md#synopsis)
- [Requirements](rax_files_objects_module.md#requirements)
- [Parameters](rax_files_objects_module.md#parameters)
- [Notes](rax_files_objects_module.md#notes)
- [Examples](rax_files_objects_module.md#examples)

## [Synopsis](rax_files_objects_module.md#id1)

- Upload, download, and delete objects in Rackspace Cloud Files.

## [Requirements](rax_files_objects_module.md#id2)

The below requirements are needed on the host that executes this module.

- pyrax
- python >= 2.6

## [Parameters](rax_files_objects_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  aliases: password  string | Rackspace API key, overrides *credentials*. |
| **auth_endpoint**  string | The URI of the authentication service.  If not specified will be set to <https://identity.api.rackspacecloud.com/v2.0/> |
| **clear_meta**  boolean | Optionally clear existing metadata when applying metadata to existing objects. Selecting this option is only appropriate when setting *type=meta*.  Choices:   - `false` ← (default) - `true` |
| **container**  string / required | The container to use for file object operations. |
| **credentials**  aliases: creds_file  path | File to find the Rackspace credentials in. Ignored if *api_key* and *username* are provided. |
| **dest**  string | The destination of a `get` operation; i.e. a local directory, `/home/user/myfolder`. Used to specify the destination of an operation on a remote object; i.e. a file name, `file1`, or a comma-separated list of remote objects, `file1,file2,file17`. |
| **env**  string | Environment as configured in *~/.pyrax.cfg*, see <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration>. |
| **expires**  integer | Used to set an expiration in seconds on an uploaded file or folder. |
| **identity_type**  string | Authentication mechanism to use, such as rackspace or keystone.  Default: `"rackspace"` |
| **meta**  dictionary | Items to set as metadata values on an uploaded file or folder.  Default: `{}` |
| **method**  string | The method of operation to be performed: `put` to upload files, `get` to download files or `delete` to remove remote objects in Cloud Files.  Choices:   - `"get"` ← (default) - `"put"` - `"delete"` |
| **region**  string | Region to create an instance in. |
| **src**  string | Source from which to upload files. Used to specify a remote object as a source for an operation, i.e. a file name, `file1`, or a comma-separated list of remote objects, `file1,file2,file17`. Parameters *src* and *dest* are mutually exclusive on remote-only object operations |
| **structure**  boolean | Used to specify whether to maintain nested directory structure when downloading objects from Cloud Files. Setting to false downloads the contents of a container to a single, flat directory  Choices:   - `false` - `true` ← (default) |
| **tenant_id**  string | The tenant ID used for authentication. |
| **tenant_name**  string | The tenant name used for authentication. |
| **type**  string | Type of object to do work on  Metadata object or a file object  Choices:   - `"file"` ← (default) - `"meta"` |
| **username**  string | Rackspace username, overrides *credentials*. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to require SSL validation of API endpoints.  Choices:   - `false` - `true` |

## [Notes](rax_files_objects_module.md#id4)

> **Note:**
>
> - The following environment variables can be used, `RAX_USERNAME`, `RAX_API_KEY`, `RAX_CREDS_FILE`, `RAX_CREDENTIALS`, `RAX_REGION`.
> - `RAX_CREDENTIALS` and `RAX_CREDS_FILE` points to a credentials file appropriate for pyrax. See <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#authenticating>
> - `RAX_USERNAME` and `RAX_API_KEY` obviate the use of a credentials file
> - `RAX_REGION` defines a Rackspace Public Cloud region (DFW, ORD, LON, …)
> - The following environment variables can be used, `RAX_USERNAME`, `RAX_API_KEY`, `RAX_CREDS_FILE`, `RAX_CREDENTIALS`, `RAX_REGION`.
> - `RAX_CREDENTIALS` and `RAX_CREDS_FILE` points to a credentials file appropriate for pyrax. See <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#authenticating>
> - `RAX_USERNAME` and `RAX_API_KEY` obviate the use of a credentials file
> - `RAX_REGION` defines a Rackspace Public Cloud region (DFW, ORD, LON, …)

## [Examples](rax_files_objects_module.md#id5)

```yaml+jinja
- name: "Test Cloud Files Objects"
  hosts: local
  gather_facts: false
  tasks:
    - name: "Get objects from test container"
      community.general.rax_files_objects:
        container: testcont
        dest: ~/Downloads/testcont

    - name: "Get single object from test container"
      community.general.rax_files_objects:
        container: testcont
        src: file1
        dest: ~/Downloads/testcont

    - name: "Get several objects from test container"
      community.general.rax_files_objects:
        container: testcont
        src: file1,file2,file3
        dest: ~/Downloads/testcont

    - name: "Delete one object in test container"
      community.general.rax_files_objects:
        container: testcont
        method: delete
        dest: file1

    - name: "Delete several objects in test container"
      community.general.rax_files_objects:
        container: testcont
        method: delete
        dest: file2,file3,file4

    - name: "Delete all objects in test container"
      community.general.rax_files_objects:
        container: testcont
        method: delete

    - name: "Upload all files to test container"
      community.general.rax_files_objects:
        container: testcont
        method: put
        src: ~/Downloads/onehundred

    - name: "Upload one file to test container"
      community.general.rax_files_objects:
        container: testcont
        method: put
        src: ~/Downloads/testcont/file1

    - name: "Upload one file to test container with metadata"
      community.general.rax_files_objects:
        container: testcont
        src: ~/Downloads/testcont/file2
        method: put
        meta:
          testkey: testdata
          who_uploaded_this: someuser@example.com

    - name: "Upload one file to test container with TTL of 60 seconds"
      community.general.rax_files_objects:
        container: testcont
        method: put
        src: ~/Downloads/testcont/file3
        expires: 60

    - name: "Attempt to get remote object that does not exist"
      community.general.rax_files_objects:
        container: testcont
        method: get
        src: FileThatDoesNotExist.jpg
        dest: ~/Downloads/testcont
      ignore_errors: true

    - name: "Attempt to delete remote object that does not exist"
      community.general.rax_files_objects:
        container: testcont
        method: delete
        dest: FileThatDoesNotExist.jpg
      ignore_errors: true

- name: "Test Cloud Files Objects Metadata"
  hosts: local
  gather_facts: false
  tasks:
    - name: "Get metadata on one object"
      community.general.rax_files_objects:
        container: testcont
        type: meta
        dest: file2

    - name: "Get metadata on several objects"
      community.general.rax_files_objects:
        container: testcont
        type: meta
        src: file2,file1

    - name: "Set metadata on an object"
      community.general.rax_files_objects:
        container: testcont
        type: meta
        dest: file17
        method: put
        meta:
          key1: value1
          key2: value2
        clear_meta: true

    - name: "Verify metadata is set"
      community.general.rax_files_objects:
        container: testcont
        type: meta
        src: file17

    - name: "Delete metadata"
      community.general.rax_files_objects:
        container: testcont
        type: meta
        dest: file17
        method: delete
        meta:
          key1: ''
          key2: ''

    - name: "Get metadata on all objects"
      community.general.rax_files_objects:
        container: testcont
        type: meta
```

### Authors

- Paul Durivage (@angstwad)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
