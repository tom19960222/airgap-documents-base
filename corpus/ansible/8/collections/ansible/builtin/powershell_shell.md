---
collection: ansible
version: "8"
title: "ansible.builtin.powershell shell – Windows PowerShell"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/powershell_shell.html
fetched_at: 2026-07-28T01:03:55+00:00
---
# ansible.builtin.powershell shell – Windows PowerShell

> **Note:**
>
> This shell plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `powershell`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.powershell` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same shell plugin name.

- [Synopsis](powershell_shell.md#synopsis)
- [Parameters](powershell_shell.md#parameters)

## [Synopsis](powershell_shell.md#id1)

- The only option when using ‘winrm’ or ‘psrp’ as a connection plugin.
- Can also be used when using ‘ssh’ as a connection plugin and the `DefaultShell` has been configured to PowerShell.

Aliases: formerly_core_powershell

## [Parameters](powershell_shell.md#id2)

| Parameter | Comments |
| --- | --- |
| **async_dir**  string  *added in Ansible 2.8* | Directory in which ansible will keep async job information.  Before Ansible 2.8, this was set to `remote_tmp + "\.ansible_async"`.  **Default:** `"%USERPROFILE%\\.ansible_async"`  **Configuration:**   - INI entry:  ```YAML+Jinja   [powershell]   async_dir = %USERPROFILE%\.ansible_async   ``` - Variable: ansible_async_dir |
| **environment**  list / elements=dictionary | List of dictionaries of environment variables and their values to use when executing commands.  **Default:** `[{}]` |
| **remote_tmp**  string | Temporary directory to use on targets when copying files to the host.  **Default:** `"%TEMP%"`  **Configuration:**   - INI entry:  ```YAML+Jinja   [powershell]   remote_tmp = %TEMP%   ``` - Variable: ansible_remote_tmp |
| **set_module_language**  boolean | Controls if we set the locale for modules when executing on the target.  Windows only supports `no` as an option.  **Choices:**   - `false` ← (default) - `true` |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
