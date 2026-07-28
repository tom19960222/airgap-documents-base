---
collection: ansible
version: "8"
title: "community.windows.win_dotnet_ngen module – Runs ngen to recompile DLLs after .NET  updates"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_dotnet_ngen_module.html
fetched_at: 2026-07-28T02:01:51+00:00
---
# community.windows.win_dotnet_ngen module – Runs ngen to recompile DLLs after .NET updates

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_dotnet_ngen`.

- [Synopsis](win_dotnet_ngen_module.md#synopsis)
- [Notes](win_dotnet_ngen_module.md#notes)
- [Examples](win_dotnet_ngen_module.md#examples)
- [Return Values](win_dotnet_ngen_module.md#return-values)

## [Synopsis](win_dotnet_ngen_module.md#id1)

- After .NET framework is installed/updated, Windows will probably want to recompile things to optimise for the host.
- This happens via scheduled task, usually at some inopportune time.
- This module allows you to run this task on your own schedule, so you incur the CPU hit at some more convenient and controlled time.
- <https://docs.microsoft.com/en-us/dotnet/framework/tools/ngen-exe-native-image-generator#native-image-service>
- <http://blogs.msdn.com/b/dotnet/archive/2013/08/06/wondering-why-mscorsvw-exe-has-high-cpu-usage-you-can-speed-it-up.aspx>

## [Notes](win_dotnet_ngen_module.md#id2)

> **Note:**
>
> - There are in fact two scheduled tasks for ngen but they have no triggers so aren’t a problem.
> - There’s no way to test if they’ve been completed.
> - The stdout is quite likely to be several megabytes.

## [Examples](win_dotnet_ngen_module.md#id3)

```yaml+jinja
- name: Run ngen tasks
  community.windows.win_dotnet_ngen:
```

## [Return Values](win_dotnet_ngen_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dotnet_ngen64_eqi_exit_code**  integer | The exit code after running the 64-bit ngen.exe executeQueuedItems command.  **Returned:** 64-bit ngen executable exists  **Sample:** `0` |
| **dotnet_ngen64_eqi_output**  string | The stdout after running the 64-bit ngen.exe executeQueuedItems command.  **Returned:** 64-bit ngen executable exists  **Sample:** `"sample output"` |
| **dotnet_ngen64_update_exit_code**  integer | The exit code after running the 64-bit ngen.exe update /force command.  **Returned:** 64-bit ngen executable exists  **Sample:** `0` |
| **dotnet_ngen64_update_output**  string | The stdout after running the 64-bit ngen.exe update /force command.  **Returned:** 64-bit ngen executable exists  **Sample:** `"sample output"` |
| **dotnet_ngen_eqi_exit_code**  integer | The exit code after running the 32-bit ngen.exe executeQueuedItems command.  **Returned:** 32-bit ngen executable exists  **Sample:** `0` |
| **dotnet_ngen_eqi_output**  string | The stdout after running the 32-bit ngen.exe executeQueuedItems command.  **Returned:** 32-bit ngen executable exists  **Sample:** `"sample output"` |
| **dotnet_ngen_update_exit_code**  integer | The exit code after running the 32-bit ngen.exe update /force command.  **Returned:** 32-bit ngen executable exists  **Sample:** `0` |
| **dotnet_ngen_update_output**  string | The stdout after running the 32-bit ngen.exe update /force command.  **Returned:** 32-bit ngen executable exists  **Sample:** `"sample output"` |

### Authors

- Peter Mounce (@petemounce)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
