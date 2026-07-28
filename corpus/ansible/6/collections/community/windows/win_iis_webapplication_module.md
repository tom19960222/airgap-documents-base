---
collection: ansible
version: "6"
title: "community.windows.win_iis_webapplication module – Configures IIS web applications"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_iis_webapplication_module.html
fetched_at: 2026-07-27T17:23:30+00:00
---
# community.windows.win_iis_webapplication module – Configures IIS web applications

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_iis_webapplication`.

- [Synopsis](win_iis_webapplication_module.md#synopsis)
- [Parameters](win_iis_webapplication_module.md#parameters)
- [See Also](win_iis_webapplication_module.md#see-also)
- [Examples](win_iis_webapplication_module.md#examples)
- [Return Values](win_iis_webapplication_module.md#return-values)

## [Synopsis](win_iis_webapplication_module.md#id1)

- Creates, removes, and configures IIS web applications.

## [Parameters](win_iis_webapplication_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **application_pool**  string | The application pool in which the new site executes.  If not specified, the application pool of the current website will be used. |
| **connect_as**  string | The type of authentication to use for this application. Either `pass_through` or `specific_user`  If `pass_through`, IIS will use the identity of the user or application pool identity to access the file system or network.  If `specific_user`, IIS will use the credentials provided in *username* and *password* to access the file system or network.  Choices:   - `"pass_through"` - `"specific_user"` |
| **name**  string / required | Name of the web application. |
| **password**  string | The password associated with *username*.  Required when *connect_as* is set to `specific_user`. |
| **physical_path**  string | The physical path on the remote host to use for the new application.  The specified folder must already exist. |
| **site**  string / required | Name of the site on which the application is created. |
| **state**  string | State of the web application.  Choices:   - `"absent"` - `"present"` ← (default) |
| **username**  string | Specifies the user name of an account that can access configuration files and content for this application.  Required when *connect_as* is set to `specific_user`. |

## [See Also](win_iis_webapplication_module.md#id3)

> **See also:**
>
> [community.windows.win_iis_virtualdirectory](win_iis_virtualdirectory_module.md#ansible-collections-community-windows-win-iis-virtualdirectory-module)
> :   Configures a virtual directory in IIS.
>
> [community.windows.win_iis_webapppool](win_iis_webapppool_module.md#ansible-collections-community-windows-win-iis-webapppool-module)
> :   Configure IIS Web Application Pools.
>
> [community.windows.win_iis_webbinding](win_iis_webbinding_module.md#ansible-collections-community-windows-win-iis-webbinding-module)
> :   Configures a IIS Web site binding.
>
> [community.windows.win_iis_website](win_iis_website_module.md#ansible-collections-community-windows-win-iis-website-module)
> :   Configures a IIS Web site.

## [Examples](win_iis_webapplication_module.md#id4)

```yaml+jinja
- name: Add ACME webapplication on IIS.
  community.windows.win_iis_webapplication:
    name: api
    site: acme
    state: present
    physical_path: C:\apps\acme\api
```

## [Return Values](win_iis_webapplication_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **application_pool**  string | The used/implemented application_pool value.  Returned: success  Sample: `"DefaultAppPool"` |
| **connect_as**  string | How IIS will try to authenticate to the physical_path.  Returned: when the application exists  Sample: `"specific_user"` |
| **physical_path**  string | The used/implemented physical_path value.  Returned: success  Sample: `"C:\\apps\\acme\\api"` |

### Authors

- Henrik Wallström (@henrikwallstrom)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
