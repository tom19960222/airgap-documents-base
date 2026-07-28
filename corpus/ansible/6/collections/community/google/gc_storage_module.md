---
collection: ansible
version: "6"
title: "community.google.gc_storage module – This module manages objects/buckets in Google Cloud Storage."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/google/gc_storage_module.html
fetched_at: 2026-07-27T17:15:15+00:00
---
# community.google.gc_storage module – This module manages objects/buckets in Google Cloud Storage.

> **Note:**
>
> This module is part of the [community.google collection](https://galaxy.ansible.com/community/google) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.google`.
> You need further requirements to be able to use this module,
> see [Requirements](gc_storage_module.md#ansible-collections-community-google-gc-storage-module-requirements) for details.
>
> To use it in a playbook, specify: `community.google.gc_storage`.

- [Synopsis](gc_storage_module.md#synopsis)
- [Requirements](gc_storage_module.md#requirements)
- [Parameters](gc_storage_module.md#parameters)
- [Examples](gc_storage_module.md#examples)

## [Synopsis](gc_storage_module.md#id1)

- This module allows users to manage their objects/buckets in Google Cloud Storage. It allows upload and download operations and can set some canned permissions. It also allows retrieval of URLs for objects for use in playbooks, and retrieval of string contents of objects. This module requires setting the default project in GCS prior to playbook usage. See <https://developers.google.com/storage/docs/reference/v1/apiversion1> for information about setting the default project.

## [Requirements](gc_storage_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- boto >= 2.9

## [Parameters](gc_storage_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **bucket**  string / required | Bucket name. |
| **dest**  path | The destination file path when downloading an object/key with a GET operation. |
| **expiration**  aliases: expiry  integer | Time limit (in seconds) for the URL generated and returned by GCA when performing a mode=put or mode=get_url operation. This url is only available when public-read is the acl for the object.  Default: `600` |
| **gs_access_key**  string / required | GS access key. If not set then the value of the GS_ACCESS_KEY_ID environment variable is used. |
| **gs_secret_key**  string / required | GS secret key. If not set then the value of the GS_SECRET_ACCESS_KEY environment variable is used. |
| **headers**  dictionary | Headers to attach to object.  Default: `{}` |
| **mode**  string / required | Switches the module behaviour between upload, download, get_url (return download url) , get_str (download object as string), create (bucket) and delete (bucket).  Choices:   - `"get"` - `"put"` - `"get_url"` - `"get_str"` - `"delete"` - `"create"` |
| **object**  path | Keyname of the object inside the bucket. Can be also be used to create “virtual directories” (see examples). |
| **overwrite**  aliases: force  boolean | Forces an overwrite either locally on the filesystem or remotely with the object/key. Used with PUT and GET operations.  Choices:   - `false` - `true` ← (default) |
| **permission**  string | This option let’s the user set the canned permissions on the object/bucket that are created. The permissions that can be set are ‘private’, ‘public-read’, ‘authenticated-read’.  Choices:   - `"private"` ← (default) - `"public-read"` - `"authenticated-read"` |
| **region**  string | The gs region to use. If not defined then the value ‘US’ will be used. See <https://cloud.google.com/storage/docs/bucket-locations>  Default: `"US"` |
| **src**  string | The source file path when performing a PUT operation. |
| **versioning**  boolean | Whether versioning is enabled or disabled (note that once versioning is enabled, it can only be suspended)  Choices:   - `false` ← (default) - `true` |

## [Examples](gc_storage_module.md#id4)

```yaml+jinja
- name: Upload some content
  community.google.gc_storage:
    bucket: mybucket
    object: key.txt
    src: /usr/local/myfile.txt
    mode: put
    permission: public-read

- name: Upload some headers
  community.google.gc_storage:
    bucket: mybucket
    object: key.txt
    src: /usr/local/myfile.txt
    headers: '{"Content-Encoding": "gzip"}'

- name: Download some content
  community.google.gc_storage:
    bucket: mybucket
    object: key.txt
    dest: /usr/local/myfile.txt
    mode: get

- name: Download an object as a string to use else where in your playbook
  community.google.gc_storage:
    bucket: mybucket
    object: key.txt
    mode: get_str

- name: Create an empty bucket
  community.google.gc_storage:
    bucket: mybucket
    mode: create

- name: Create a bucket with key as directory
  community.google.gc_storage:
    bucket: mybucket
    object: /my/directory/path
    mode: create

- name: Delete a bucket and all contents
  community.google.gc_storage:
    bucket: mybucket
    mode: delete

- name: Create a bucket with versioning enabled
  community.google.gc_storage:
    bucket: "mybucket"
    versioning: yes
    mode: create

- name: Create a bucket located in the eu
  community.google.gc_storage:
    bucket: "mybucket"
    region: "europe-west3"
    mode: create
```

### Authors

- Benno Joy (@bennojoy)
- Lukas Beumer (@Nitaco)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.google/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.google)
