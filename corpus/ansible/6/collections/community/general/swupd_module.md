---
collection: ansible
version: "6"
title: "community.general.swupd module – Manages updates and bundles in ClearLinux systems"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/swupd_module.html
fetched_at: 2026-07-27T17:13:30+00:00
---
# community.general.swupd module – Manages updates and bundles in ClearLinux systems

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.swupd`.

- [Synopsis](swupd_module.md#synopsis)
- [Parameters](swupd_module.md#parameters)
- [Examples](swupd_module.md#examples)
- [Return Values](swupd_module.md#return-values)

## [Synopsis](swupd_module.md#id1)

- Manages updates and bundles with the swupd bundle manager, which is used by the Clear Linux Project for Intel Architecture.

## [Parameters](swupd_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **contenturl**  string | URL pointing to the contents of available bundles. If not specified, the contents are retrieved from clearlinux.org. |
| **format**  string | The format suffix for version file downloads. For example [1,2,3,staging,etc]. If not specified, the default format is used. |
| **manifest**  aliases: release, version  integer | The manifest contains information about the bundles at certain version of the OS. Specify a Manifest version to verify against that version or leave unspecified to verify against the current version. |
| **name**  aliases: bundle  string | Name of the (I)bundle to install or remove. |
| **state**  string | Indicates the desired (I)bundle state. `present` ensures the bundle is installed while `absent` ensures the (I)bundle is not installed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **update**  boolean | Updates the OS to the latest version.  Choices:   - `false` ← (default) - `true` |
| **url**  string | Overrides both *contenturl* and *versionurl*. |
| **verify**  boolean | Verify content for OS version.  Choices:   - `false` ← (default) - `true` |
| **versionurl**  string | URL for version string download. |

## [Examples](swupd_module.md#id3)

```yaml+jinja
- name: Update the OS to the latest version
  community.general.swupd:
    update: true

- name: Installs the "foo" bundle
  community.general.swupd:
    name: foo
    state: present

- name: Removes the "foo" bundle
  community.general.swupd:
    name: foo
    state: absent

- name: Check integrity of filesystem
  community.general.swupd:
    verify: true

- name: Downgrade OS to release 12920
  community.general.swupd:
    verify: true
    manifest: 12920
```

## [Return Values](swupd_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **stderr**  string | stderr of swupd  Returned: always |
| **stdout**  string | stdout of swupd  Returned: always |

### Authors

- Alberto Murillo (@albertomurillo)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
