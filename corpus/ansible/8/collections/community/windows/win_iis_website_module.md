---
collection: ansible
version: "8"
title: "community.windows.win_iis_website module – Configures a IIS Web site"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_iis_website_module.html
fetched_at: 2026-07-28T02:02:02+00:00
---
# community.windows.win_iis_website module – Configures a IIS Web site

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
> To use it in a playbook, specify: `community.windows.win_iis_website`.

- [Synopsis](win_iis_website_module.md#synopsis)
- [Parameters](win_iis_website_module.md#parameters)
- [See Also](win_iis_website_module.md#see-also)
- [Examples](win_iis_website_module.md#examples)

## [Synopsis](win_iis_website_module.md#id1)

- Creates, Removes and configures a IIS Web site.

## [Parameters](win_iis_website_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **application_pool**  string | The application pool in which the new site executes. |
| **hostname**  string | The host header to bind to / use for the new site. |
| **ip**  string | The IP address to bind to / use for the new site. |
| **name**  string / required | Names of web site. |
| **parameters**  string | Custom site Parameters from string where properties are separated by a pipe and property name/values by colon Ex. “foo:1|bar:2”  Some custom parameters that you can use are listed below, this isn’t a definitive list but some common parameters.  `logfile.directory` - Physical path to store Logs, e.g. `D:\IIS-LOGs\`.  `logfile.period` - Log file rollover scheduled accepting these values, how frequently the log file should be rolled-over, e.g. `Hourly, Daily, Weekly, Monthly`.  `logfile.LogFormat` - Log file format, by default IIS uses `W3C`.  `logfile.truncateSize` - The size at which the log file contents will be trunsted, expressed in bytes. |
| **physical_path**  string | The physical path on the remote host to use for the new site.  The specified folder must already exist. |
| **port**  integer | The port to bind to / use for the new site. |
| **site_id**  string | Explicitly set the IIS numeric ID for a site.  Note that this value cannot be changed after the website has been created. |
| **state**  string | State of the web site  **Choices:**   - `"absent"` - `"started"` - `"stopped"` - `"restarted"` |

## [See Also](win_iis_website_module.md#id3)

> **See also:**
>
> [community.windows.win_iis_virtualdirectory](win_iis_virtualdirectory_module.md#ansible-collections-community-windows-win-iis-virtualdirectory-module)
> :   Configures a virtual directory in IIS.
>
> [community.windows.win_iis_webapplication](win_iis_webapplication_module.md#ansible-collections-community-windows-win-iis-webapplication-module)
> :   Configures IIS web applications.
>
> [community.windows.win_iis_webapppool](win_iis_webapppool_module.md#ansible-collections-community-windows-win-iis-webapppool-module)
> :   Configure IIS Web Application Pools.
>
> [community.windows.win_iis_webbinding](win_iis_webbinding_module.md#ansible-collections-community-windows-win-iis-webbinding-module)
> :   Configures a IIS Web site binding.

## [Examples](win_iis_website_module.md#id4)

```yaml+jinja
# Start a website

- name: Acme IIS site
  community.windows.win_iis_website:
    name: Acme
    state: started
    port: 80
    ip: 127.0.0.1
    hostname: acme.local
    application_pool: acme
    physical_path: C:\sites\acme
    parameters: logfile.directory:C:\sites\logs
  register: website

# Remove Default Web Site and the standard port 80 binding
- name: Remove Default Web Site
  community.windows.win_iis_website:
    name: "Default Web Site"
    state: absent

# Create a WebSite with custom Logging configuration (Logs Location, Format and Rolling Over).

- name: Creating WebSite with Custom Log location, Format 3WC and rolling over every hour.
  community.windows.win_iis_website:
    name: MyCustom_Web_Shop_Site
    state: started
    port: 80
    ip: '*'
    hostname: '*'
    physical_path: D:\wwwroot\websites\my-shop-site
    parameters: logfile.directory:D:\IIS-LOGS\websites\my-shop-site|logfile.period:Hourly|logFile.logFormat:W3C
    application_pool: my-shop-site

# Some commandline examples:

# This return information about an existing host
# $ ansible -i vagrant-inventory -m community.windows.win_iis_website -a "name='Default Web Site'" window
# host | success >> {
#     "changed": false,
#     "site": {
#         "ApplicationPool": "DefaultAppPool",
#         "Bindings": [
#             "*:80:"
#         ],
#         "ID": 1,
#         "Name": "Default Web Site",
#         "PhysicalPath": "%SystemDrive%\\inetpub\\wwwroot",
#         "State": "Stopped"
#     }
# }

# This stops an existing site.
# $ ansible -i hosts -m community.windows.win_iis_website -a "name='Default Web Site' state=stopped" host

# This creates a new site.
# $ ansible -i hosts -m community.windows.win_iis_website -a "name=acme physical_path=C:\\sites\\acme" host

# Change logfile.
# $ ansible -i hosts -m community.windows.win_iis_website -a "name=acme physical_path=C:\\sites\\acme" host
```

### Authors

- Henrik Wallström (@henrikwallstrom)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
