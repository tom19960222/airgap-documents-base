---
collection: ansible
version: "8"
title: "community.windows.win_iis_webbinding module – Configures a IIS Web site binding"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_iis_webbinding_module.html
fetched_at: 2026-07-28T02:02:01+00:00
---
# community.windows.win_iis_webbinding module – Configures a IIS Web site binding

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
> To use it in a playbook, specify: `community.windows.win_iis_webbinding`.

- [Synopsis](win_iis_webbinding_module.md#synopsis)
- [Parameters](win_iis_webbinding_module.md#parameters)
- [See Also](win_iis_webbinding_module.md#see-also)
- [Examples](win_iis_webbinding_module.md#examples)
- [Return Values](win_iis_webbinding_module.md#return-values)

## [Synopsis](win_iis_webbinding_module.md#id1)

- Creates, removes and configures a binding to an existing IIS Web site.

## [Parameters](win_iis_webbinding_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **certificate_hash**  string | Certificate hash (thumbprint) for the SSL binding. The certificate hash is the unique identifier for the certificate. |
| **certificate_store_name**  string | Name of the certificate store where the certificate for the binding is located.  **Default:** `"my"` |
| **host_header**  string | The host header to bind to / use for the new site.  If you are creating/removing a catch-all binding, omit this parameter rather than defining it as ‘\*’. |
| **ip**  string | The IP address to bind to / use for the new site.  **Default:** `"*"` |
| **name**  aliases: website  string / required | Names of web site. |
| **port**  integer | The port to bind to / use for the new site.  **Default:** `80` |
| **protocol**  string | The protocol to be used for the Web binding (usually HTTP, HTTPS, or FTP).  **Default:** `"http"` |
| **ssl_flags**  string | This parameter is only valid on Server 2012 and newer.  Primarily used for enabling and disabling server name indication (SNI).  Set to `0` to disable SNI.  Set to `1` to enable SNI. |
| **state**  string | State of the binding.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [See Also](win_iis_webbinding_module.md#id3)

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
> [community.windows.win_iis_website](win_iis_website_module.md#ansible-collections-community-windows-win-iis-website-module)
> :   Configures a IIS Web site.

## [Examples](win_iis_webbinding_module.md#id4)

```yaml+jinja
- name: Add a HTTP binding on port 9090
  community.windows.win_iis_webbinding:
    name: Default Web Site
    port: 9090
    state: present

- name: Remove the HTTP binding on port 9090
  community.windows.win_iis_webbinding:
    name: Default Web Site
    port: 9090
    state: absent

- name: Remove the default http binding
  community.windows.win_iis_webbinding:
    name: Default Web Site
    port: 80
    ip: '*'
    state: absent

- name: Add a HTTPS binding
  community.windows.win_iis_webbinding:
    name: Default Web Site
    protocol: https
    port: 443
    ip: 127.0.0.1
    certificate_hash: B0D0FA8408FC67B230338FCA584D03792DA73F4C
    state: present

- name: Add a HTTPS binding with host header and SNI enabled
  community.windows.win_iis_webbinding:
    name: Default Web Site
    protocol: https
    port: 443
    host_header: test.com
    ssl_flags: 1
    certificate_hash: D1A3AF8988FD32D1A3AF8988FD323792DA73F4C
    state: present
```

## [Return Values](win_iis_webbinding_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **binding_info**  dictionary | Information on the binding being manipulated  **Returned:** on success  **Sample:** `"\"binding_info\": {\n  \"bindingInformation\": \"127.0.0.1:443:\",\n  \"certificateHash\": \"FF3910CE089397F1B5A77EB7BAFDD8F44CDE77DD\",\n  \"certificateStoreName\": \"MY\",\n  \"hostheader\": \"\",\n  \"ip\": \"127.0.0.1\",\n  \"port\": 443,\n  \"protocol\": \"https\",\n  \"sslFlags\": \"not supported\"\n}"` |
| **operation_type**  string | The type of operation performed  Can be removed, updated, matched, or added  **Returned:** on success  **Sample:** `"removed"` |
| **website_state**  string | The state of the website being targetted  Can be helpful in case you accidentally cause a binding collision which can result in the targetted site being stopped  **Returned:** always  **Sample:** `"Started"` |

### Authors

- Noah Sparks (@nwsparks)
- Henrik Wallström (@henrikwallstrom)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
