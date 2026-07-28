---
collection: ansible
version: "8"
title: "community.general.osx_defaults module – Manage macOS user defaults"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/osx_defaults_module.html
fetched_at: 2026-07-28T01:48:45+00:00
---
# community.general.osx_defaults module – Manage macOS user defaults

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.osx_defaults`.

- [Synopsis](osx_defaults_module.md#synopsis)
- [Parameters](osx_defaults_module.md#parameters)
- [Attributes](osx_defaults_module.md#attributes)
- [Notes](osx_defaults_module.md#notes)
- [Examples](osx_defaults_module.md#examples)

## [Synopsis](osx_defaults_module.md#id1)

- osx_defaults allows users to read, write, and delete macOS user defaults from Ansible scripts.
- macOS applications and other programs use the defaults system to record user preferences and other information that must be maintained when the applications are not running (such as default font for new documents, or the position of an Info panel).

Aliases: system.osx_defaults

## [Parameters](osx_defaults_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **array_add**  boolean | Add new elements to the array for a key which has an array as its value.  **Choices:**   - `false` ← (default) - `true` |
| **domain**  string | The domain is a domain name of the form `com.companyname.appname`.  **Default:** `"NSGlobalDomain"` |
| **host**  string | The host on which the preference should apply.  The special value `currentHost` corresponds to the `-currentHost` switch of the defaults commandline tool. |
| **key**  string | The key of the user preference. |
| **path**  string | The path in which to search for `defaults`.  **Default:** `"/usr/bin:/usr/local/bin"` |
| **state**  string | The state of the user defaults.  If set to `list` will query the given parameter specified by `key`. Returns `null` is nothing found or mis-spelled.  `list` added in Ansible 2.8.  **Choices:**   - `"absent"` - `"list"` - `"present"` ← (default) |
| **type**  string | The type of value to write.  **Choices:**   - `"array"` - `"bool"` - `"boolean"` - `"date"` - `"float"` - `"int"` - `"integer"` - `"string"` ← (default) |
| **value**  any | The value to write.  Only required when `state=present`. |

## [Attributes](osx_defaults_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](osx_defaults_module.md#id4)

> **Note:**
>
> - Apple Mac caches defaults. You may need to logout and login to apply the changes.

## [Examples](osx_defaults_module.md#id5)

```yaml+jinja
- name: Set boolean valued key for application domain
  community.general.osx_defaults:
    domain: com.apple.Safari
    key: IncludeInternalDebugMenu
    type: bool
    value: true
    state: present

- name: Set string valued key for global domain
  community.general.osx_defaults:
    domain: NSGlobalDomain
    key: AppleMeasurementUnits
    type: string
    value: Centimeters
    state: present

- name: Set int valued key for arbitrary plist
  community.general.osx_defaults:
    domain: /Library/Preferences/com.apple.SoftwareUpdate
    key: AutomaticCheckEnabled
    type: int
    value: 1
  become: true

- name: Set int valued key only for the current host
  community.general.osx_defaults:
    domain: com.apple.screensaver
    host: currentHost
    key: showClock
    type: int
    value: 1

- name: Defaults to global domain and setting value
  community.general.osx_defaults:
    key: AppleMeasurementUnits
    type: string
    value: Centimeters

- name: Setting an array valued key
  community.general.osx_defaults:
    key: AppleLanguages
    type: array
    value:
      - en
      - nl

- name: Removing a key
  community.general.osx_defaults:
    domain: com.geekchimp.macable
    key: ExampleKeyToRemove
    state: absent
```

### Authors

- Franck Nijhof

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
