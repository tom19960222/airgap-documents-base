---
collection: ansible
version: "6"
title: "community.general.svr4pkg module – Manage Solaris SVR4 packages"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/svr4pkg_module.html
fetched_at: 2026-07-27T17:13:28+00:00
---
# community.general.svr4pkg module – Manage Solaris SVR4 packages

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
> To use it in a playbook, specify: `community.general.svr4pkg`.

- [Synopsis](svr4pkg_module.md#synopsis)
- [Parameters](svr4pkg_module.md#parameters)
- [Examples](svr4pkg_module.md#examples)

## [Synopsis](svr4pkg_module.md#id1)

- Manages SVR4 packages on Solaris 10 and 11.
- These were the native packages on Solaris <= 10 and are available as a legacy feature in Solaris 11.
- Note that this is a very basic packaging system. It will not enforce dependencies on install or remove.

## [Parameters](svr4pkg_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **category**  boolean | Install/Remove category instead of a single package.  Choices:   - `false` ← (default) - `true` |
| **name**  string / required | Package name, e.g. `SUNWcsr` |
| **proxy**  string | HTTP[s] proxy to be used if *src* is a URL. |
| **response_file**  string | Specifies the location of a response file to be used if package expects input on install. (added in Ansible 1.4) |
| **src**  string | Specifies the location to install the package from. Required when *state=present*.  Can be any path acceptable to the `pkgadd` command’s `-d` option. e.g.: `somefile.pkg`, `/dir/with/pkgs`, `http:/server/mypkgs.pkg`.  If using a file or directory, they must already be accessible by the host. See the [ansible.builtin.copy](../../ansible/builtin/copy_module.md#ansible-collections-ansible-builtin-copy-module) module for a way to get them there. |
| **state**  string / required | Whether to install (`present`), or remove (`absent`) a package.  If the package is to be installed, then *src* is required.  The SVR4 package system doesn’t provide an upgrade operation. You need to uninstall the old, then install the new package.  Choices:   - `"present"` - `"absent"` |
| **zone**  string | Whether to install the package only in the current zone, or install it into all zones.  The installation into all zones works only if you are working with the global zone.  Choices:   - `"current"` - `"all"` ← (default) |

## [Examples](svr4pkg_module.md#id3)

```yaml+jinja
- name: Install a package from an already copied file
  community.general.svr4pkg:
    name: CSWcommon
    src: /tmp/cswpkgs.pkg
    state: present

- name: Install a package directly from an http site
  community.general.svr4pkg:
    name: CSWpkgutil
    src: 'http://get.opencsw.org/now'
    state: present
    zone: current

- name: Install a package with a response file
  community.general.svr4pkg:
    name: CSWggrep
    src: /tmp/third-party.pkg
    response_file: /tmp/ggrep.response
    state: present

- name: Ensure that a package is not installed
  community.general.svr4pkg:
    name: SUNWgnome-sound-recorder
    state: absent

- name: Ensure that a category is not installed
  community.general.svr4pkg:
    name: FIREFOX
    state: absent
    category: true
```

### Authors

- Boyd Adamson (@brontitall)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
