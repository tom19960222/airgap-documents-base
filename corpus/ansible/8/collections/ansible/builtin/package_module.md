---
collection: ansible
version: "8"
title: "ansible.builtin.package module – Generic OS package manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/package_module.html
fetched_at: 2026-07-28T01:07:36+00:00
---
# ansible.builtin.package module – Generic OS package manager

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `package` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.package` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](package_module.md#synopsis)
- [Requirements](package_module.md#requirements)
- [Parameters](package_module.md#parameters)
- [Attributes](package_module.md#attributes)
- [Notes](package_module.md#notes)
- [Examples](package_module.md#examples)

## [Synopsis](package_module.md#id1)

- This modules manages packages on a target without specifying a package manager module (like [ansible.builtin.yum](yum_module.md#ansible-collections-ansible-builtin-yum-module), [ansible.builtin.apt](apt_module.md#ansible-collections-ansible-builtin-apt-module), …). It is convenient to use in an heterogeneous environment of machines without having to create a specific task for each package manager. `package` calls behind the module for the package manager used by the operating system discovered by the module [ansible.builtin.setup](setup_module.md#ansible-collections-ansible-builtin-setup-module). If `setup` was not yet run, `package` will run it.
- This module acts as a proxy to the underlying package manager module. While all arguments will be passed to the underlying module, not all modules support the same arguments. This documentation only covers the minimum intersection of module arguments that all packaging modules support.
- For Windows targets, use the [ansible.windows.win_package](../windows/win_package_module.md#ansible-collections-ansible-windows-win-package-module) module instead.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](package_module.md#id2)

The below requirements are needed on the host that executes this module.

- Whatever is required for the package plugins specific for each system.

## [Parameters](package_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | Package name, or package specifier with version.  Syntax varies with package manager. For example `name-1.0` or `name=1.0`.  Package names also vary with package manager; this module will not “translate” them per distro. For example `libyaml-dev`, `libyaml-devel`. |
| **state**  string / required | Whether to install (`present`), or remove (`absent`) a package.  You can use other states like `latest` ONLY if they are supported by the underlying package module(s) executed. |
| **use**  string | The required package manager module to use (`yum`, `apt`, and so on). The default ‘auto’ will use existing facts or try to autodetect it.  You should only use this field if the automatic selection is not working for some reason.  **Default:** `"auto"` |

## [Attributes](package_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | **Support:** **full** | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | **Support:** **full** | Supports being used with the `async` keyword |
| **bypass_host_loop** | **Support:** **none** | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **check_mode** | **Support:**  N/A  support depends on the underlying plugin invoked | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:**  N/A  support depends on the underlying plugin invoked | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platforms:** **all**  The support depends on the availability for the specific plugin for each platform and if fact gathering is able to detect it | Target OS/families that can be operated against |

## [Notes](package_module.md#id5)

> **Note:**
>
> - While `package` abstracts package managers to ease dealing with multiple distributions, package name often differs for the same software.

## [Examples](package_module.md#id6)

```yaml+jinja
- name: Install ntpdate
  ansible.builtin.package:
    name: ntpdate
    state: present

# This uses a variable as this changes per distribution.
- name: Remove the apache package
  ansible.builtin.package:
    name: "{{ apache }}"
    state: absent

- name: Install the latest version of Apache and MariaDB
  ansible.builtin.package:
    name:
      - httpd
      - mariadb-server
    state: latest
```

### Authors

- Ansible Core Team

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
