---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_offload module – Create, modify and delete NFS, S3 or Azure offload targets"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_offload_module.html
fetched_at: 2026-07-28T02:51:10+00:00
---
# purestorage.flasharray.purefa_offload module – Create, modify and delete NFS, S3 or Azure offload targets

> **Note:**
>
> This module is part of the [purestorage.flasharray collection](https://galaxy.ansible.com/ui/repo/published/purestorage/flasharray/) (version 1.24.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flasharray`.
> You need further requirements to be able to use this module,
> see [Requirements](purefa_offload_module.md#ansible-collections-purestorage-flasharray-purefa-offload-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_offload`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_offload_module.md#synopsis)
- [Requirements](purefa_offload_module.md#requirements)
- [Parameters](purefa_offload_module.md#parameters)
- [Notes](purefa_offload_module.md#notes)
- [Examples](purefa_offload_module.md#examples)

## [Synopsis](purefa_offload_module.md#id1)

- Create, modify and delete NFS, S3 or Azure offload targets.
- Only supported on Purity v5.2.0 or higher.
- You must have a correctly configured offload network for offload to work.

## [Requirements](purefa_offload_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_offload_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  string | Access Key ID of the offload target |
| **account**  string | Name of the Azure blob storage account |
| **address**  string | The IP or FQDN address of the NFS server |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **bucket**  string | Name of the bucket for the S3 or GCP target |
| **container**  string | Name of the blob container of the Azure target  **Default:** `"offload"` |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **initialize**  boolean | Define whether to initialize the offload bucket  **Choices:**   - `false` - `true` ← (default) |
| **name**  string / required | The name of the offload target |
| **options**  string | Additonal mount options for the NFS share  Supported mount options include *port*, *rsize*, *wsize*, *nfsvers*, and *tcp* or *udp*  **Default:** `""` |
| **placement**  string | AWS S3 placement strategy  **Choices:**   - `"retention-based"` ← (default) - `"aws-standard-class"` |
| **profile**  string  *added in purestorage.flasharray 1.21.0* | The Offload target profile that will be selected for this target.  This option allows more granular configuration for the target on top of the protocol parameter  **Choices:**   - `"azure"` - `"gcp"` - `"nfs"` - `"nfs-flashblade"` - `"s3-aws"` - `"s3-flashblade"` - `"s3-scality-ring"` - `"s3-wasabi-pay-as-you-go"` - `"s3-wasabi-rcs"` - `"s3-other"` |
| **protocol**  string | Define which protocol the offload engine uses  NFS is not a supported protocl from Purity//FA 6.6.0 and higher  **Choices:**   - `"nfs"` ← (default) - `"s3"` - `"azure"` - `"gcp"` |
| **secret**  string | Secret Access Key for the offload target |
| **share**  string | NFS export on the NFS server |
| **state**  string | Define state of offload  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](purefa_offload_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_offload_module.md#id5)

```yaml+jinja
- name: Create NFS offload target
  purestorage.flasharray.purefa_offload:
    name: nfs-offload
    protocol: nfs
    address: 10.21.200.4
    share: "/offload_target"
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create S3 offload target
  purestorage.flasharray.purefa_offload:
    name: s3-offload
    protocol: s3
    access_key: "3794fb12c6204e19195f"
    bucket: offload-bucket
    secret: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    placement: aws-standard-class
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create Azure offload target
  purestorage.flasharray.purefa_offload:
    name: azure-offload
    protocol: azure
    secret: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    container: offload-container
    account: user1
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete offload target
  purestorage.flasharray.purefa_offload:
    name: nfs-offload
    protocol: nfs
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
- [Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
- [Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
- [Communication](index.md#communication-for-purestorage-flasharray)
