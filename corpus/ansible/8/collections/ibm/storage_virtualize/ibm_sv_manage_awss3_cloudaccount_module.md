---
collection: ansible
version: "8"
title: "ibm.storage_virtualize.ibm_sv_manage_awss3_cloudaccount module – This module configures and manages Amazon Simple Storage Service (Amazon S3) cloud account on IBM Storage Virtualize family systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/storage_virtualize/ibm_sv_manage_awss3_cloudaccount_module.html
fetched_at: 2026-07-28T02:35:12+00:00
---
# ibm.storage_virtualize.ibm_sv_manage_awss3_cloudaccount module – This module configures and manages Amazon Simple Storage Service (Amazon S3) cloud account on IBM Storage Virtualize family systems

> **Note:**
>
> This module is part of the [ibm.storage_virtualize collection](https://galaxy.ansible.com/ui/repo/published/ibm/storage_virtualize/) (version 2.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ibm.storage_virtualize`.
>
> To use it in a playbook, specify: `ibm.storage_virtualize.ibm_sv_manage_awss3_cloudaccount`.

New in ibm.storage_virtualize 1.11.0

- [Synopsis](ibm_sv_manage_awss3_cloudaccount_module.md#synopsis)
- [Parameters](ibm_sv_manage_awss3_cloudaccount_module.md#parameters)
- [Notes](ibm_sv_manage_awss3_cloudaccount_module.md#notes)
- [Examples](ibm_sv_manage_awss3_cloudaccount_module.md#examples)

## [Synopsis](ibm_sv_manage_awss3_cloudaccount_module.md#id1)

- Ansible interface to manage mkcloudaccountawss3, chcloudaccountawss3, and rmcloudaccount commands.

## [Parameters](ibm_sv_manage_awss3_cloudaccount_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **accesskeyid**  string | Specifies the public part of the Amazon S3 access key credential of the AWS user that the system use to access the cloud storage. |
| **bucketprefix**  string | Specifies the prefix for the bucket object.  Applies, when *state=present*, to create an Amazon S3 account. |
| **clustername**  string / required | The hostname or management IP of the Storage Virtualize system. |
| **domain**  string | Domain for the Storage Virtualize system.  Valid when hostname is used for the parameter *clustername*. |
| **downbandwidthmbits**  string | Specifies the download bandwidth limit in megabits per second (Mbps).  The value must be a number 1-10240. |
| **encrypt**  string | Specifies whether to encrypt the data in the cloud account.  By default, encryption is enabled if encryption is enabled on the cluster unless *encrypt=no* is specified.  Valid when *state=present* to create an Amazon S3 account.  **Choices:**   - `"yes"` - `"no"` |
| **ignorefailures**  boolean | Specify to change the access key whether the new access key works or not.  Valid when *state=present* to update an existing Amazon S3 account.  Parameter is allowed only when *accesskeyid* and *secretaccesskey* are entered.  **Choices:**   - `false` - `true` |
| **importsystem**  string | Specifies that the system’s data be imported.  Valid when *state=present* to update an existing Amazon S3 account. |
| **log_path**  string | Path of debug log file. |
| **mode**  string | Specifies the new or modified cloud account mode.  Valid when *state=present* to update an existing Amazon S3 account.  **Choices:**   - `"import"` - `"normal"` |
| **name**  string / required | Specifies the name of an Amazon S3 account. |
| **old_name**  string | Specifies the old name of an Amazon S3 account.  Valid when *state=present*, to rename the existing Amazon S3 account. |
| **password**  string | REST API password for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **refresh**  boolean | Specifies a refresh of the system import candidates.  If the account is in import mode, this parameter specifies a refresh of the data available for import.  **Choices:**   - `false` - `true` |
| **region**  string | Specifies the AWS region to use to access the cloud account and store data. |
| **resetusagehistory**  boolean | Resets the usage history (to 0).  Storage consumption that reflects the space that is consumed on the cloud account is cumulative, which means that it remains in the current day row (the 0th row).  Valid when *state=present* to update an existing Amazon S3 account.  **Choices:**   - `false` - `true` |
| **secretaccesskey**  string | Specifies the secret access key of an Amazon S3 cloud account. |
| **state**  string / required | Creates, updates (`present`), or deletes (`absent`) an Amazon S3 account.  **Choices:**   - `"present"` - `"absent"` |
| **token**  string | The authentication token to verify a user on the Storage Virtualize system.  To generate a token, use the [ibm.storage_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-auth-module) module. |
| **upbandwidthmbits**  string | Specifies the upload bandwidth limit in megabits per second (Mbps).  The value must be a number 1-10240. |
| **username**  string | REST API username for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_sv_manage_awss3_cloudaccount_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_sv_manage_awss3_cloudaccount_module.md#id4)

```yaml+jinja
- name: Configure Amazon S3 account
  ibm.storage_virtualize.ibm_sv_manage_awss3_cloudaccount:
    clustername: "{{cluster}}"
    username: "{{username}}"
    password: "{{password}}"
    name: awss3
    bucketprefix: "{{bucketprefix}}"
    accesskeyid: "{{accesskeyid}}"
    secretaccesskey: "{{secretaccesskey}}"
    state: present
- name: Update Amazon S3 account configuration
  ibm.storage_virtualize.ibm_sv_manage_awss3_cloudaccount:
    clustername: "{{cluster}}"
    username: "{{username}}"
    password: "{{password}}"
    name: awss3
    upbandwidthmbits: "{{upbandwidthmbits}}"
    downbandwidthmbits: "{{downbandwidthmbits}}"
    state: present
- name: Update Amazon S3 account mode to import
  ibm.storage_virtualize.ibm_sv_manage_awss3_cloudaccount:
    clustername: "{{cluster}}"
    username: "{{username}}"
    password: "{{password}}"
    name: awss3
    mode: import
    importsystem: 123456789
    state: present
- name: Delete Amazon S3 account configuration
  ibm.storage_virtualize.ibm_sv_manage_awss3_cloudaccount:
    clustername: "{{cluster}}"
    username: "{{username}}"
    password: "{{password}}"
    name: awss3
    state: absent
```

### Authors

- Sanjaikumaar M (@sanjaikumaar)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.storage_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.storage_virtualize)
- [Report an issue](https://github.com/ansible-collections/community.REPO_NAME/issues/new/choose)
- [Communication](index.md#communication-for-ibm-storage-virtualize)
