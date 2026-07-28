---
collection: ansible
version: "8"
title: "ansible.builtin.package_facts module – Package information as facts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/package_facts_module.html
fetched_at: 2026-07-28T01:07:37+00:00
---
# ansible.builtin.package_facts module – Package information as facts

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `package_facts` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.package_facts` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](package_facts_module.md#synopsis)
- [Requirements](package_facts_module.md#requirements)
- [Parameters](package_facts_module.md#parameters)
- [Attributes](package_facts_module.md#attributes)
- [Examples](package_facts_module.md#examples)
- [Returned Facts](package_facts_module.md#returned-facts)

## [Synopsis](package_facts_module.md#id1)

- Return information about installed packages as facts.

## [Requirements](package_facts_module.md#id2)

The below requirements are needed on the host that executes this module.

- For ‘portage’ support it requires the `qlist` utility, which is part of ‘app-portage/portage-utils’.
- For Debian-based systems `python-apt` package must be installed on targeted hosts.
- For SUSE-based systems `python3-rpm` package must be installed on targeted hosts. This package is required because SUSE does not include RPM Python bindings by default.

## [Parameters](package_facts_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **manager**  list / elements=string | The package manager used by the system so we can query the package information.  Since 2.8 this is a list and can support multiple package managers per system.  The ‘portage’ and ‘pkg’ options were added in version 2.8.  The ‘apk’ option was added in version 2.11.  The ‘pkg_info’ option was added in version 2.13.  **Choices:**   - `"auto"` ← (default) - `"rpm"` - `"apt"` - `"portage"` - `"pkg"` - `"pacman"` - `"apk"` - `"pkg_info"`   **Default:** `["auto"]` |
| **strategy**  string  *added in Ansible 2.8* | This option controls how the module queries the package managers on the system. `first` means it will return only information for the first supported package manager available. `all` will return information for all supported and available package managers on the system.  **Choices:**   - `"first"` ← (default) - `"all"` |

## [Attributes](package_facts_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **facts** | **Support:** **full** | Action returns an `ansible_facts` dictionary that will update existing host facts |
| **platform** | **Platform:** **posix** | Target OS/families that can be operated against |

## [Examples](package_facts_module.md#id5)

```yaml+jinja
- name: Gather the package facts
  ansible.builtin.package_facts:
    manager: auto

- name: Print the package facts
  ansible.builtin.debug:
    var: ansible_facts.packages

- name: Check whether a package called foobar is installed
  ansible.builtin.debug:
    msg: "{{ ansible_facts.packages['foobar'] | length }} versions of foobar are installed!"
  when: "'foobar' in ansible_facts.packages"
```

## [Returned Facts](package_facts_module.md#id6)

Facts returned by this module are added/updated in the `hostvars` host facts and can be referenced by name just like any other host fact. They do not need to be registered in order to use them.

| Key | Description |
| --- | --- |
| **packages**  dictionary | Maps the package name to a non-empty list of dicts with package information.  Every dict in the list corresponds to one installed version of the package.  The fields described below are present for all package managers. Depending on the package manager, there might be more fields for a package.  **Returned:** when operating system level package manager is specified or auto detected manager  **Sample:** `"{\n  \"packages\": {\n    \"kernel\": [\n      {\n        \"name\": \"kernel\",\n        \"source\": \"rpm\",\n        \"version\": \"3.10.0\",\n        ...\n      },\n      {\n        \"name\": \"kernel\",\n        \"source\": \"rpm\",\n        \"version\": \"3.10.0\",\n        ...\n      },\n      ...\n    ],\n    \"kernel-tools\": [\n      {\n        \"name\": \"kernel-tools\",\n        \"source\": \"rpm\",\n        \"version\": \"3.10.0\",\n        ...\n      }\n    ],\n    ...\n  }\n}\n# Sample rpm\n{\n  \"packages\": {\n    \"kernel\": [\n      {\n        \"arch\": \"x86_64\",\n        \"epoch\": null,\n        \"name\": \"kernel\",\n        \"release\": \"514.26.2.el7\",\n        \"source\": \"rpm\",\n        \"version\": \"3.10.0\"\n      },\n      {\n        \"arch\": \"x86_64\",\n        \"epoch\": null,\n        \"name\": \"kernel\",\n        \"release\": \"514.16.1.el7\",\n        \"source\": \"rpm\",\n        \"version\": \"3.10.0\"\n      },\n      {\n        \"arch\": \"x86_64\",\n        \"epoch\": null,\n        \"name\": \"kernel\",\n        \"release\": \"514.10.2.el7\",\n        \"source\": \"rpm\",\n        \"version\": \"3.10.0\"\n      },\n      {\n        \"arch\": \"x86_64\",\n        \"epoch\": null,\n        \"name\": \"kernel\",\n        \"release\": \"514.21.1.el7\",\n        \"source\": \"rpm\",\n        \"version\": \"3.10.0\"\n      },\n      {\n        \"arch\": \"x86_64\",\n        \"epoch\": null,\n        \"name\": \"kernel\",\n        \"release\": \"693.2.2.el7\",\n        \"source\": \"rpm\",\n        \"version\": \"3.10.0\"\n      }\n    ],\n    \"kernel-tools\": [\n      {\n        \"arch\": \"x86_64\",\n        \"epoch\": null,\n        \"name\": \"kernel-tools\",\n        \"release\": \"693.2.2.el7\",\n        \"source\": \"rpm\",\n        \"version\": \"3.10.0\"\n      }\n    ],\n    \"kernel-tools-libs\": [\n      {\n        \"arch\": \"x86_64\",\n        \"epoch\": null,\n        \"name\": \"kernel-tools-libs\",\n        \"release\": \"693.2.2.el7\",\n        \"source\": \"rpm\",\n        \"version\": \"3.10.0\"\n      }\n    ],\n  }\n}\n# Sample deb\n{\n  \"packages\": {\n    \"libbz2-1.0\": [\n      {\n        \"version\": \"1.0.6-5\",\n        \"source\": \"apt\",\n        \"arch\": \"amd64\",\n        \"name\": \"libbz2-1.0\"\n      }\n    ],\n    \"patch\": [\n      {\n        \"version\": \"2.7.1-4ubuntu1\",\n        \"source\": \"apt\",\n        \"arch\": \"amd64\",\n        \"name\": \"patch\"\n      }\n    ],\n  }\n}\n# Sample pkg_info\n{\n  \"packages\": {\n    \"curl\": [\n      {\n          \"name\": \"curl\",\n          \"source\": \"pkg_info\",\n          \"version\": \"7.79.0\"\n      }\n    ],\n    \"intel-firmware\": [\n      {\n          \"name\": \"intel-firmware\",\n          \"source\": \"pkg_info\",\n          \"version\": \"20210608v0\"\n      }\n    ],\n  }\n}"` |
| **name**  string | The package’s name.  **Returned:** always |
| **source**  string | Where information on the package came from.  **Returned:** always |
| **version**  string | The package’s version.  **Returned:** always |

### Authors

- Matthew Jones (@matburt)
- Brian Coca (@bcoca)
- Adam Miller (@maxamillion)

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
