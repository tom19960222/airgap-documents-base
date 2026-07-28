---
collection: ansible
version: "8"
title: "ansible.windows.quote filter – Quotes argument(s) for various Windows shells"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/windows/quote_filter.html
fetched_at: 2026-07-28T01:05:32+00:00
---
# ansible.windows.quote filter – Quotes argument(s) for various Windows shells

> **Note:**
>
> This filter plugin is part of the [ansible.windows collection](https://galaxy.ansible.com/ui/repo/published/ansible/windows/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.quote`.

- [Synopsis](quote_filter.md#synopsis)
- [Input](quote_filter.md#input)
- [Keyword parameters](quote_filter.md#keyword-parameters)
- [See Also](quote_filter.md#see-also)
- [Examples](quote_filter.md#examples)
- [Return Value](quote_filter.md#return-value)

## [Synopsis](quote_filter.md#id1)

- Quotes argument(s) for the various Windows command line shells.
- Defaults to escaping arguments based on the Win32 C argv parsing rules that [ansible.windows.win_command](win_command_module.md#ansible-collections-ansible-windows-win-command-module) uses.
- Using *shell=’cmd’* or *shell=’powershell’* can be set to escape arguments for those respective shells.
- Each value is escaped in a way to ensure the process gets the literal argument passed in and meta chars escaped.

## [Input](quote_filter.md#id2)

This describes the input of the filter, the value before `| ansible.windows.quote`.

| Parameter | Comments |
| --- | --- |
| **Input**  any / required | The string, list, or dict of values to quote.  A string or list of strings will be quoted.  When using a dict as the input, the final form will be in `KEY="value"` to match the MSI parameter format. |

## [Keyword parameters](quote_filter.md#id3)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.windows.quote(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **shell**  string | The shell to quote the arguments for.  By default no shell is used and the arguments are quoted with the Win32 C quoting rules.  **Choices:**   - `"None"` ← (default) - `"cmd"` - `"powershell"` |

## [See Also](quote_filter.md#id4)

> **See also:**
>
> [ansible.windows.win_command](win_command_module.md#ansible-collections-ansible-windows-win-command-module)
> :   Executes a command on a remote Windows node.
>
> [ansible.windows.win_shell](win_shell_module.md#ansible-collections-ansible-windows-win-shell-module)
> :   Execute shell commands on target hosts.

## [Examples](quote_filter.md#id5)

```yaml+jinja
- name: Escape an argument for win_command
  ansible.windows.win_command:
    cmd: my.exe {{ argument1 | ansible.windows.quote }}

- name: Escape an argument for PowerShell
  ansible.windows.win_shell: |
    $var = {{ argument1 | ansible.windows.quote(shell='powershell') }}
    Write-Host $var
```

## [Return Value](quote_filter.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  string | The quoted input value(s) as a single space delimited string.  **Returned:** success |

### Authors

- Jordan Borean (@jborean93)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
- [Communication](index.md#communication-for-ansible-windows)
