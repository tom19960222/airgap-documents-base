---
collection: ansible
version: "8"
title: "microsoft.ad.offline_join module – Get the Offline Domain Join BLOB"
source_url: https://docs.ansible.com/projects/ansible/8/collections/microsoft/ad/offline_join_module.html
fetched_at: 2026-07-28T02:40:53+00:00
---
# microsoft.ad.offline_join module – Get the Offline Domain Join BLOB

> **Note:**
>
> This module is part of the [microsoft.ad collection](https://galaxy.ansible.com/ui/repo/published/microsoft/ad/) (version 1.4.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install microsoft.ad`.
> You need further requirements to be able to use this module,
> see [Requirements](offline_join_module.md#ansible-collections-microsoft-ad-offline-join-module-requirements) for details.
>
> To use it in a playbook, specify: `microsoft.ad.offline_join`.

- [Synopsis](offline_join_module.md#synopsis)
- [Requirements](offline_join_module.md#requirements)
- [Parameters](offline_join_module.md#parameters)
- [Attributes](offline_join_module.md#attributes)
- [Notes](offline_join_module.md#notes)
- [See Also](offline_join_module.md#see-also)
- [Examples](offline_join_module.md#examples)
- [Return Values](offline_join_module.md#return-values)

## [Synopsis](offline_join_module.md#id1)

- Used to get the Offline Domain Join BLOB.
- This BLOB is used to join computers to a domain without any network access.

## [Requirements](offline_join_module.md#id2)

The below requirements are needed on the host that executes this module.

- `ActiveDirectory` PowerShell module

## [Parameters](offline_join_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **blob_path**  string | If set, will store the blob bytes into a file at this path.  This will not create the parent directory specified if it does not exist.  The existence of this file is also used as an idempotency check, if the file already exists the blob will not be regenerated.  If specified the module return value *blob* will be null. |
| **domain_server**  string | Specified the Active Directory Domain Services instance to connect to.  Can be in the form of an FQDN or NetBIOS name.  If not specified then the value is based on the default domain of the computer running PowerShell. |
| **identity**  string | The identity of the computer object used to generate the offline join blob for.  This is mutually exclusive with *name* and (path).  The identity can be in the form of a GUID representing the `objectGUID` value, `sAMAccountName`, `objectSid`, or `distinguishedName`.  This option or *name* must be specified. |
| **name**  string | The name of the computer object used to generate the offline join blob for.  This is mutually exclusive with *identity*.  The name is combined with *path* to find the AD computer object that matches the DistinguishedName `CN={{ name}},{{ path }}`.  This option or *identity* must be specified. |
| **path**  string | The path where the computer object specified by `name` is stored.  By default the default computer path defined in AD is used, for example `CN=Computers,DC=domain,DC=com`. |
| **provision_root_ca_certs**  boolean | Adds all the root Certificate Authority certificates on the local machine and adds them to the blob.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](offline_join_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **windows** | Target OS/families that can be operated against |

## [Notes](offline_join_module.md#id5)

> **Note:**
>
> - For more information on Offline Domain Join see [the step-by-step guide](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd392267%2528v=ws.10%2529).
> - There is no way to specify specific credentials to communicate with the domain controller when creating the blob. Use `become` with net credentials if the current user cannot authenticate itself and bypass the double hop problem.
> - The data returned by this module is very sensitive. If not using *blob_path* then `no_log=True` should be used on the task to avoid the data being leaked.
> - This module will always report a change unless *blob_path* is specified. If the path is specified then then the existence of that path will act as the idempotency check.
> - Generating a new blob will reset the password of the computer object, take care that this isn’t called under a computer account that has already been joined.

## [See Also](offline_join_module.md#id6)

> **See also:**
>
> [microsoft.ad.domain](domain_module.md#ansible-collections-microsoft-ad-domain-module)
> :   Ensures the existence of a Windows domain.
>
> [microsoft.ad.membership](membership_module.md#ansible-collections-microsoft-ad-membership-module)
> :   Manage domain/workgroup membership for a Windows host.
>
> [microsoft.ad.computer](computer_module.md#ansible-collections-microsoft-ad-computer-module)
> :   Manage Active Directory computer objects.

## [Examples](offline_join_module.md#id7)

```yaml+jinja
- name: create computer object
  microsoft.ad.computer:
    name: MyComputer
    state: present
  register: computer_obj

- name: create offline blob
  microsoft.ad.offline_join:
    identity: '{{ computer_obj.object_guid }}'
  when: computer_obj is changed
  register: offline_blob
  no_log: true

- name: join host by offline blob
  microsoft.ad.membership:
    offline_join_blob: '{{ offline_blob.blob }}'
    state: domain
    reboot: true
  delegate_to: member-host

- name: create blob and store it in a file on the target host
  microsoft.ad.offline_join:
    name: MyComputer
    path: OU=Production,DC=domain,DC=com
    blob_path: C:\Windows\TEMP\offline_blob
```

## [Return Values](offline_join_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **blob**  string | The blob as a base64 string.  This value is empty when running in check mode.  This value is null when *blob_path* is specified.  This value is highly sensitive as it contains the credentials and other authentication data needed for an offline join.  **Returned:** always  **Sample:** `"ARAIAMzMzMygCAAAAAAAAAAAAgABAAAA"` |

### Authors

- Jordan Borean (@jborean93)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/microsoft.ad/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/microsoft.ad)
- [Report an issue](https://github.com/ansible-collections/microsoft.ad/issues/new/choose)
- [Communication](index.md#communication-for-microsoft-ad)
