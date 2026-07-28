---
collection: ansible
version: "8"
title: "community.windows.win_iis_virtualdirectory module – Configures a virtual directory in IIS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_iis_virtualdirectory_module.html
fetched_at: 2026-07-28T02:01:59+00:00
---
# community.windows.win_iis_virtualdirectory module – Configures a virtual directory in IIS

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
> To use it in a playbook, specify: `community.windows.win_iis_virtualdirectory`.

- [Synopsis](win_iis_virtualdirectory_module.md#synopsis)
- [Parameters](win_iis_virtualdirectory_module.md#parameters)
- [See Also](win_iis_virtualdirectory_module.md#see-also)
- [Examples](win_iis_virtualdirectory_module.md#examples)

## [Synopsis](win_iis_virtualdirectory_module.md#id1)

- Creates, Removes and configures a virtual directory in IIS.

## [Parameters](win_iis_virtualdirectory_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **application**  string | The application under which the virtual directory is created or exists. |
| **connect_as**  string  *added in community.windows 1.9.0* | The type of authentication to use for the virtual directory. Either `pass_through` or `specific_user`  If `pass_through`, IIS will use the identity of the user or application pool identity to access the physical path.  If `specific_user`, IIS will use the credentials provided in *username* and *password* to access the physical path.  **Choices:**   - `"pass_through"` - `"specific_user"` |
| **name**  string / required | The name of the virtual directory to create or remove. |
| **password**  string  *added in community.windows 1.9.0* | The password associated with *username*.  Required when *connect_as* is set to `specific_user`. |
| **physical_path**  string | The physical path to the folder in which the new virtual directory is created.  The specified folder must already exist. |
| **site**  string / required | The site name under which the virtual directory is created or exists. |
| **state**  string | Whether to add or remove the specified virtual directory.  Removing will remove the virtual directory and all under it (Recursively).  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **username**  string  *added in community.windows 1.9.0* | Specifies the user name of an account that can access configuration files and content for the virtual directory.  Required when *connect_as* is set to `specific_user`. |

## [See Also](win_iis_virtualdirectory_module.md#id3)

> **See also:**
>
> [community.windows.win_iis_webapplication](win_iis_webapplication_module.md#ansible-collections-community-windows-win-iis-webapplication-module)
> :   Configures IIS web applications.
>
> [community.windows.win_iis_webapppool](win_iis_webapppool_module.md#ansible-collections-community-windows-win-iis-webapppool-module)
> :   Configure IIS Web Application Pools.
>
> [community.windows.win_iis_webbinding](win_iis_webbinding_module.md#ansible-collections-community-windows-win-iis-webbinding-module)
> :   Configures a IIS Web site binding.
>
> [community.windows.win_iis_website](win_iis_website_module.md#ansible-collections-community-windows-win-iis-website-module)
> :   Configures a IIS Web site.

## [Examples](win_iis_virtualdirectory_module.md#id4)

```yaml+jinja
- name: Create a virtual directory if it does not exist
  community.windows.win_iis_virtualdirectory:
    name: somedirectory
    site: somesite
    state: present
    physical_path: C:\virtualdirectory\some

- name: Remove a virtual directory if it exists
  community.windows.win_iis_virtualdirectory:
    name: somedirectory
    site: somesite
    state: absent

- name: Create a virtual directory on an application if it does not exist
  community.windows.win_iis_virtualdirectory:
    name: somedirectory
    site: somesite
    application: someapp
    state: present
    physical_path: C:\virtualdirectory\some
```

### Authors

- Henrik Wallström (@henrikwallstrom)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
