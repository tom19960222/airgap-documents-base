---
collection: ansible
version: "8"
title: "community.general.pear module – Manage pear/pecl packages"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/pear_module.html
fetched_at: 2026-07-28T01:48:59+00:00
---
# community.general.pear module – Manage pear/pecl packages

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
> To use it in a playbook, specify: `community.general.pear`.

- [Synopsis](pear_module.md#synopsis)
- [Parameters](pear_module.md#parameters)
- [Attributes](pear_module.md#attributes)
- [Examples](pear_module.md#examples)

## [Synopsis](pear_module.md#id1)

- Manage PHP packages with the pear package manager.

Aliases: packaging.language.pear

## [Parameters](pear_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **executable**  path | Path to the pear executable. |
| **name**  aliases: pkg  string / required | Name of the package to install, upgrade, or remove. |
| **prompts**  list / elements=any  *added in community.general 0.2.0* | List of regular expressions that can be used to detect prompts during pear package installation to answer the expected question.  Prompts will be processed in the same order as the packages list.  You can optionally specify an answer to any question in the list.  If no answer is provided, the list item will only contain the regular expression.  To specify an answer, the item will be a dict with the regular expression as key and the answer as value `my_regular_expression: 'an_answer'`.  You can provide a list containing items with or without answer.  A prompt list can be shorter or longer than the packages list but will issue a warning.  If you want to specify that a package will not need prompts in the middle of a list, `null`. |
| **state**  string | Desired state of the package.  **Choices:**   - `"present"` ← (default) - `"installed"` - `"latest"` - `"absent"` - `"removed"` |

## [Attributes](pear_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](pear_module.md#id4)

```yaml+jinja
- name: Install pear package
  community.general.pear:
    name: Net_URL2
    state: present

- name: Install pecl package
  community.general.pear:
    name: pecl/json_post
    state: present

- name: Install pecl package with expected prompt
  community.general.pear:
    name: pecl/apcu
    state: present
    prompts:
        - (.*)Enable internal debugging in APCu \[no\]

- name: Install pecl package with expected prompt and an answer
  community.general.pear:
    name: pecl/apcu
    state: present
    prompts:
        - (.*)Enable internal debugging in APCu \[no\]: "yes"

- name: Install multiple pear/pecl packages at once with prompts.
    Prompts will be processed on the same order as the packages order.
    If there is more prompts than packages, packages without prompts will be installed without any prompt expected.
    If there is more packages than prompts, additional prompts will be ignored.
  community.general.pear:
    name: pecl/gnupg, pecl/apcu
    state: present
    prompts:
      - I am a test prompt because gnupg doesnt asks anything
      - (.*)Enable internal debugging in APCu \[no\]: "yes"

- name: Install multiple pear/pecl packages at once skipping the first prompt.
    Prompts will be processed on the same order as the packages order.
    If there is more prompts than packages, packages without prompts will be installed without any prompt expected.
    If there is more packages than prompts, additional prompts will be ignored.
  community.general.pear:
    name: pecl/gnupg, pecl/apcu
    state: present
    prompts:
      - null
      - (.*)Enable internal debugging in APCu \[no\]: "yes"

- name: Upgrade package
  community.general.pear:
    name: Net_URL2
    state: latest

- name: Remove packages
  community.general.pear:
    name: Net_URL2,pecl/json_post
    state: absent
```

### Authors

- Jonathan Lestrelin (@jle64)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
