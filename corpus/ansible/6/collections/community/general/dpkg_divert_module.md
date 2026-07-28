---
collection: ansible
version: "6"
title: "community.general.dpkg_divert module – Override a debian package’s version of a file"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/dpkg_divert_module.html
fetched_at: 2026-07-27T17:08:49+00:00
---
# community.general.dpkg_divert module – Override a debian package’s version of a file

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
> see [Requirements](dpkg_divert_module.md#ansible-collections-community-general-dpkg-divert-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.dpkg_divert`.

New in community.general 0.2.0

- [Synopsis](dpkg_divert_module.md#synopsis)
- [Requirements](dpkg_divert_module.md#requirements)
- [Parameters](dpkg_divert_module.md#parameters)
- [Notes](dpkg_divert_module.md#notes)
- [Examples](dpkg_divert_module.md#examples)
- [Return Values](dpkg_divert_module.md#return-values)

## [Synopsis](dpkg_divert_module.md#id1)

- A diversion is for `dpkg` the knowledge that only a given package (or the local administrator) is allowed to install a file at a given location. Other packages shipping their own version of this file will be forced to *divert* it, i.e. to install it at another location. It allows one to keep changes in a file provided by a debian package by preventing its overwrite at package upgrade.
- This module manages diversions of debian packages files using the `dpkg-divert` commandline tool. It can either create or remove a diversion for a given file, but also update an existing diversion to modify its *holder* and/or its *divert* location.

## [Requirements](dpkg_divert_module.md#id2)

The below requirements are needed on the host that executes this module.

- dpkg-divert >= 1.15.0 (Debian family)

## [Parameters](dpkg_divert_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **divert**  path | The location where the versions of file will be diverted.  Default is to add suffix `.distrib` to the file path.  This parameter is ignored when *state=absent*. |
| **force**  boolean | When *rename=true* and *force=true*, renaming is performed even if the target of the renaming exists, i.e. the existing contents of the file at this location will be lost.  This parameter is ignored when *rename=false*.  Choices:   - `false` ← (default) - `true` |
| **holder**  string | The name of the package whose copy of file is not diverted, also known as the diversion holder or the package the diversion belongs to.  The actual package does not have to be installed or even to exist for its name to be valid. If not specified, the diversion is hold by ‘LOCAL’, that is reserved by/for dpkg for local diversions.  This parameter is ignored when *state=absent*. |
| **path**  path / required | The original and absolute path of the file to be diverted or undiverted. This path is unique, i.e. it is not possible to get two diversions for the same *path*. |
| **rename**  boolean | Actually move the file aside (when *state=present*) or back (when *state=absent*), but only when changing the state of the diversion. This parameter has no effect when attempting to add a diversion that already exists or when removing an unexisting one.  Unless *force=true*, renaming fails if the destination file already exists (this lock being a dpkg-divert feature, and bypassing it being a module feature).  Choices:   - `false` ← (default) - `true` |
| **state**  string | When *state=absent*, remove the diversion of the specified *path*; when *state=present*, create the diversion if it does not exist, or update its package *holder* or *divert* location, if it already exists.  Choices:   - `"absent"` - `"present"` ← (default) |

## [Notes](dpkg_divert_module.md#id4)

> **Note:**
>
> - This module supports *check_mode* and *diff*.

## [Examples](dpkg_divert_module.md#id5)

```yaml+jinja
- name: Divert /usr/bin/busybox to /usr/bin/busybox.distrib and keep file in place
  community.general.dpkg_divert:
    path: /usr/bin/busybox

- name: Divert /usr/bin/busybox by package 'branding'
  community.general.dpkg_divert:
    path: /usr/bin/busybox
    holder: branding

- name: Divert and rename busybox to busybox.dpkg-divert
  community.general.dpkg_divert:
    path: /usr/bin/busybox
    divert: /usr/bin/busybox.dpkg-divert
    rename: true

- name: Remove the busybox diversion and move the diverted file back
  community.general.dpkg_divert:
    path: /usr/bin/busybox
    state: absent
    rename: true
    force: true
```

## [Return Values](dpkg_divert_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The dpkg-divert commands ran internally by the module.  Returned: on_success  Sample: `["/usr/bin/dpkg-divert --no-rename --remove /etc/foobarrc"]` |
| **diversion**  dictionary | The status of the diversion after task execution.  Returned: always  Sample: `{"divert": "/etc/foobarrc.distrib", "holder": "LOCAL", "path": "/etc/foobarrc", "state": "present"}` |
| **divert**  string | The location of the diverted file.  Returned: success |
| **holder**  string | The package holding the diversion.  Returned: success |
| **path**  string | The path of the file to divert/undivert.  Returned: success |
| **state**  string | The state of the diversion.  Returned: success |
| **messages**  list / elements=string | The dpkg-divert relevant messages (stdout or stderr).  Returned: on_success  Sample: `["Removing 'local diversion of /etc/foobarrc to /etc/foobarrc.distrib'"]` |

### Authors

- quidame (@quidame)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
