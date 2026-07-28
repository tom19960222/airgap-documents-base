---
collection: ansible
version: "8"
title: "ansible.builtin.debconf module – Configure a .deb package"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/debconf_module.html
fetched_at: 2026-07-28T01:07:25+00:00
---
# ansible.builtin.debconf module – Configure a .deb package

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `debconf` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.debconf` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](debconf_module.md#synopsis)
- [Requirements](debconf_module.md#requirements)
- [Parameters](debconf_module.md#parameters)
- [Attributes](debconf_module.md#attributes)
- [Notes](debconf_module.md#notes)
- [Examples](debconf_module.md#examples)

## [Synopsis](debconf_module.md#id1)

- Configure a .deb package using debconf-set-selections.
- Or just query existing selections.

## [Requirements](debconf_module.md#id2)

The below requirements are needed on the host that executes this module.

- debconf
- debconf-utils

## [Parameters](debconf_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **name**  aliases: pkg  string / required | Name of package to configure. |
| **question**  aliases: selection, setting  string | A debconf configuration setting. |
| **unseen**  boolean | Do not set ‘seen’ flag when pre-seeding.  **Choices:**   - `false` ← (default) - `true` |
| **value**  aliases: answer  string | Value to set the configuration to. |
| **vtype**  string | The type of the value supplied.  It is highly recommended to add *no_log=True* to task while specifying *vtype=password*.  `seen` was added in Ansible 2.2.  **Choices:**   - `"boolean"` - `"error"` - `"multiselect"` - `"note"` - `"password"` - `"seen"` - `"select"` - `"string"` - `"text"` - `"title"` |

## [Attributes](debconf_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **debian** | Target OS/families that can be operated against |

## [Notes](debconf_module.md#id5)

> **Note:**
>
> - This module requires the command line debconf tools.
> - A number of questions have to be answered (depending on the package). Use ‘debconf-show <package>’ on any Debian or derivative with the package installed to see questions/settings available.
> - Some distros will always record tasks involving the setting of passwords as changed. This is due to debconf-get-selections masking passwords.
> - It is highly recommended to add *no_log=True* to task while handling sensitive information using this module.
> - The debconf module does not reconfigure packages, it just updates the debconf database. An additional step is needed (typically with *notify* if debconf makes a change) to reconfigure the package and apply the changes. debconf is extensively used for pre-seeding configuration prior to installation rather than modifying configurations. So, while dpkg-reconfigure does use debconf data, it is not always authoritative and you may need to check how your package is handled.
> - Also note dpkg-reconfigure is a 3-phase process. It invokes the control scripts from the `/var/lib/dpkg/info` directory with the `<package>.prerm  reconfigure <version>`, `<package>.config reconfigure <version>` and `<package>.postinst control <version>` arguments.
> - The main issue is that the `<package>.config reconfigure` step for many packages will first reset the debconf database (overriding changes made by this module) by checking the on-disk configuration. If this is the case for your package then dpkg-reconfigure will effectively ignore changes made by debconf.
> - However as dpkg-reconfigure only executes the `<package>.config` step if the file exists, it is possible to rename it to `/var/lib/dpkg/info/<package>.config.ignore` before executing `dpkg-reconfigure -f noninteractive <package>` and then restore it. This seems to be compliant with Debian policy for the .config file.

## [Examples](debconf_module.md#id6)

```yaml+jinja
- name: Set default locale to fr_FR.UTF-8
  ansible.builtin.debconf:
    name: locales
    question: locales/default_environment_locale
    value: fr_FR.UTF-8
    vtype: select

- name: Set to generate locales
  ansible.builtin.debconf:
    name: locales
    question: locales/locales_to_be_generated
    value: en_US.UTF-8 UTF-8, fr_FR.UTF-8 UTF-8
    vtype: multiselect

- name: Accept oracle license
  ansible.builtin.debconf:
    name: oracle-java7-installer
    question: shared/accepted-oracle-license-v1-1
    value: 'true'
    vtype: select

- name: Specifying package you can register/return the list of questions and current values
  ansible.builtin.debconf:
    name: tzdata

- name: Pre-configure tripwire site passphrase
  ansible.builtin.debconf:
    name: tripwire
    question: tripwire/site-passphrase
    value: "{{ site_passphrase }}"
    vtype: password
  no_log: True
```

### Authors

- Brian Coca (@bcoca)

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
