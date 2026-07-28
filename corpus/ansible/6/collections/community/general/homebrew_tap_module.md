---
collection: ansible
version: "6"
title: "community.general.homebrew_tap module – Tap a Homebrew repository"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/homebrew_tap_module.html
fetched_at: 2026-07-27T17:09:19+00:00
---
# community.general.homebrew_tap module – Tap a Homebrew repository

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
> see [Requirements](homebrew_tap_module.md#ansible-collections-community-general-homebrew-tap-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.homebrew_tap`.

- [Synopsis](homebrew_tap_module.md#synopsis)
- [Requirements](homebrew_tap_module.md#requirements)
- [Parameters](homebrew_tap_module.md#parameters)
- [Examples](homebrew_tap_module.md#examples)

## [Synopsis](homebrew_tap_module.md#id1)

- Tap external Homebrew repositories.

## [Requirements](homebrew_tap_module.md#id2)

The below requirements are needed on the host that executes this module.

- homebrew

## [Parameters](homebrew_tap_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **name**  aliases: tap  list / elements=string / required | The GitHub user/organization repository to tap. |
| **path**  path  added in community.general 2.1.0 | A `:` separated list of paths to search for `brew` executable.  Default: `"/usr/local/bin:/opt/homebrew/bin:/home/linuxbrew/.linuxbrew/bin"` |
| **state**  string | state of the repository.  Choices:   - `"present"` ← (default) - `"absent"` |
| **url**  string | The optional git URL of the repository to tap. The URL is not assumed to be on GitHub, and the protocol doesn’t have to be HTTP. Any location and protocol that git can handle is fine.  *name* option may not be a list of multiple taps (but a single tap instead) when this option is provided. |

## [Examples](homebrew_tap_module.md#id4)

```yaml+jinja
- name: Tap a Homebrew repository, state present
  community.general.homebrew_tap:
    name: homebrew/dupes

- name: Tap a Homebrew repository, state absent
  community.general.homebrew_tap:
    name: homebrew/dupes
    state: absent

- name: Tap a Homebrew repository, state present
  community.general.homebrew_tap:
    name: homebrew/dupes,homebrew/science
    state: present

- name: Tap a Homebrew repository using url, state present
  community.general.homebrew_tap:
    name: telemachus/brew
    url: 'https://bitbucket.org/telemachus/brew'
```

### Authors

- Indrajit Raychaudhuri (@indrajitr)
- Daniel Jaouen (@danieljaouen)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
