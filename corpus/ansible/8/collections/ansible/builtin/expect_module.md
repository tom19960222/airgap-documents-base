---
collection: ansible
version: "8"
title: "ansible.builtin.expect module – Executes a command and responds to prompts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/expect_module.html
fetched_at: 2026-07-28T01:07:28+00:00
---
# ansible.builtin.expect module – Executes a command and responds to prompts

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `expect` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.expect` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](expect_module.md#synopsis)
- [Requirements](expect_module.md#requirements)
- [Parameters](expect_module.md#parameters)
- [Attributes](expect_module.md#attributes)
- [Notes](expect_module.md#notes)
- [See Also](expect_module.md#see-also)
- [Examples](expect_module.md#examples)

## [Synopsis](expect_module.md#id1)

- The `expect` module executes a command and responds to prompts.
- The given command will be executed on all selected nodes. It will not be processed through the shell, so variables like `$HOME` and operations like `"<"`, `">"`, `"|"`, and `"&"` will not work.

## [Requirements](expect_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- pexpect >= 3.3

## [Parameters](expect_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **chdir**  path | Change into this directory before running the command. |
| **command**  string / required | The command module takes command to run. |
| **creates**  path | A filename, when it already exists, this step will **not** be run. |
| **echo**  boolean | Whether or not to echo out your response strings.  **Choices:**   - `false` ← (default) - `true` |
| **removes**  path | A filename, when it does not exist, this step will **not** be run. |
| **responses**  dictionary / required | Mapping of expected string/regex and string to respond with. If the response is a list, successive matches return successive responses. List functionality is new in 2.1. |
| **timeout**  integer | Amount of time in seconds to wait for the expected strings. Use `null` to disable timeout.  **Default:** `30` |

## [Attributes](expect_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **posix** | Target OS/families that can be operated against |

## [Notes](expect_module.md#id5)

> **Note:**
>
> - If you want to run a command through the shell (say you are using `<`, `>`, `|`, and so on), you must specify a shell in the command such as `/bin/bash -c "/path/to/something | grep else"`.
> - The question, or key, under *responses* is a python regex match. Case insensitive searches are indicated with a prefix of `?i`.
> - The `pexpect` library used by this module operates with a search window of 2000 bytes, and does not use a multiline regex match. To perform a start of line bound match, use a pattern like ``(?m)^pattern``
> - By default, if a question is encountered multiple times, its string response will be repeated. If you need different responses for successive question matches, instead of a string response, use a list of strings as the response. The list functionality is new in 2.1.
> - The [ansible.builtin.expect](expect_module.md#ansible-collections-ansible-builtin-expect-module) module is designed for simple scenarios. For more complex needs, consider the use of expect code with the [ansible.builtin.shell](shell_module.md#ansible-collections-ansible-builtin-shell-module) or [ansible.builtin.script](script_module.md#ansible-collections-ansible-builtin-script-module) modules. (An example is part of the [ansible.builtin.shell](shell_module.md#ansible-collections-ansible-builtin-shell-module) module documentation).
> - If the command returns non UTF-8 data, it must be encoded to avoid issues. One option is to pipe the output through `base64`.

## [See Also](expect_module.md#id6)

> **See also:**
>
> [ansible.builtin.script](script_module.md#ansible-collections-ansible-builtin-script-module)
> :   Runs a local script on a remote node after transferring it.
>
> [ansible.builtin.shell](shell_module.md#ansible-collections-ansible-builtin-shell-module)
> :   Execute shell commands on targets.

## [Examples](expect_module.md#id7)

```yaml+jinja
- name: Case insensitive password string match
  ansible.builtin.expect:
    command: passwd username
    responses:
      (?i)password: "MySekretPa$$word"
  # you don't want to show passwords in your logs
  no_log: true

- name: Generic question with multiple different responses
  ansible.builtin.expect:
    command: /path/to/custom/command
    responses:
      Question:
        - response1
        - response2
        - response3
```

### Authors

- Matt Martz (@sivel)

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
