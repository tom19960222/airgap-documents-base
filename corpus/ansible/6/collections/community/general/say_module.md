---
collection: ansible
version: "6"
title: "community.general.say module – Makes a computer to speak"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/say_module.html
fetched_at: 2026-07-27T17:12:52+00:00
---
# community.general.say module – Makes a computer to speak

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
> see [Requirements](say_module.md#ansible-collections-community-general-say-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.say`.

- [Synopsis](say_module.md#synopsis)
- [Requirements](say_module.md#requirements)
- [Parameters](say_module.md#parameters)
- [Notes](say_module.md#notes)
- [Examples](say_module.md#examples)

## [Synopsis](say_module.md#id1)

- makes a computer speak! Amuse your friends, annoy your coworkers!

## [Requirements](say_module.md#id2)

The below requirements are needed on the host that executes this module.

- say or espeak or espeak-ng

## [Parameters](say_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **msg**  string / required | What to say |
| **voice**  string | What voice to use |

## [Notes](say_module.md#id4)

> **Note:**
>
> - In 2.5, this module has been renamed from `osx_say` to [community.general.say](say_module.md#ansible-collections-community-general-say-module).
> - If you like this module, you may also be interested in the osx_say callback plugin.
> - A list of available voices, with language, can be found by running `say -v ?` on a OSX host and `espeak --voices` on a Linux host.

## [Examples](say_module.md#id5)

```yaml+jinja
- name: Makes a computer to speak
  community.general.say:
    msg: '{{ inventory_hostname }} is all done'
    voice: Zarvox
  delegate_to: localhost
```

### Authors

- Ansible Core Team
- Michael DeHaan (@mpdehaan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
