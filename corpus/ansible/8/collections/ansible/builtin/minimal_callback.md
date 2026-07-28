---
collection: ansible
version: "8"
title: "ansible.builtin.minimal callback – minimal Ansible screen output"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/minimal_callback.html
fetched_at: 2026-07-28T01:07:54+00:00
---
# ansible.builtin.minimal callback – minimal Ansible screen output

> **Note:**
>
> This callback plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `minimal`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.minimal` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same callback plugin name.

- [Callback plugin](minimal_callback.md#callback-plugin)
- [Synopsis](minimal_callback.md#synopsis)
- [Parameters](minimal_callback.md#parameters)

## [Callback plugin](minimal_callback.md#id1)

This plugin is a **stdout callback**. You can use only use one stdout callback at a time. Additional aggregate or notification callbacks can be enabled though.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](minimal_callback.md#id2)

- This is the default output callback used by the ansible command (ad-hoc)

## [Parameters](minimal_callback.md#id3)

| Parameter | Comments |
| --- | --- |
| **pretty_results**  boolean  *added in ansible-core 2.13* | Configure the result format to be more readable  When the result format is set to `yaml` this option defaults to `True`, and defaults to `False` when configured to `json`.  Setting this option to `True` will force `json` and `yaml` results to always be pretty printed regardless of verbosity.  When set to `True` and used with the `yaml` result format, this option will modify module responses in an attempt to produce a more human friendly output at the expense of correctness, and should not be relied upon to aid in writing variable manipulations or conditionals. For correctness, set this option to `False` or set the result format to `json`.  **Choices:**   - `false` - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   callback_format_pretty = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_FORMAT_PRETTY`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_FORMAT_PRETTY) |
| **result_format**  string  *added in ansible-core 2.13* | Define the task result format used in the callback output.  These formats do not cause the callback to emit valid JSON or YAML formats.  The output contains these formats interspersed with other non-machine parsable data.  **Choices:**   - `"json"` ← (default) - `"yaml"`   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   callback_result_format = json   ``` - Environment variable: [`ANSIBLE_CALLBACK_RESULT_FORMAT`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_RESULT_FORMAT) |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
