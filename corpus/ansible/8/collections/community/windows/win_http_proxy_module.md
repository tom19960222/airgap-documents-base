---
collection: ansible
version: "8"
title: "community.windows.win_http_proxy module – Manages proxy settings for WinHTTP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_http_proxy_module.html
fetched_at: 2026-07-28T02:01:58+00:00
---
# community.windows.win_http_proxy module – Manages proxy settings for WinHTTP

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
> To use it in a playbook, specify: `community.windows.win_http_proxy`.

- [Synopsis](win_http_proxy_module.md#synopsis)
- [Parameters](win_http_proxy_module.md#parameters)
- [Notes](win_http_proxy_module.md#notes)
- [See Also](win_http_proxy_module.md#see-also)
- [Examples](win_http_proxy_module.md#examples)

## [Synopsis](win_http_proxy_module.md#id1)

- Used to set, remove, or import proxy settings for Windows HTTP Services `WinHTTP`.
- WinHTTP is a framework used by applications or services, typically .NET applications or non-interactive services, to make web requests.

## [Parameters](win_http_proxy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bypass**  list / elements=string | A list of hosts that will bypass the set proxy when being accessed.  Use `<local>` to match hostnames that are not fully qualified domain names. This is useful when needing to connect to intranet sites using just the hostname.  Omit, set to null or an empty string/list to remove the bypass list.  If this is set then *proxy* must also be set. |
| **proxy**  any | A string or dict that specifies the proxy to be set.  If setting a string, should be in the form `hostname`, `hostname:port`, or `protocol=hostname:port`.  If the port is undefined, the default port for the protocol in use is used.  If setting a dict, the keys should be the protocol and the values should be the hostname and/or port for that protocol.  Valid protocols are `http`, `https`, `ftp`, and `socks`.  Omit, set to null or an empty string to remove the proxy settings. |
| **source**  string | Instead of manually specifying the *proxy* and/or *bypass*, set this to import the proxy from a set source like Internet Explorer.  Using `ie` will import the Internet Explorer proxy settings for the current active network connection of the current user.  Only IE’s proxy URL and bypass list will be imported into WinHTTP.  This is like running `netsh winhttp import proxy source=ie`.  The value is imported when the module runs and will not automatically be updated if the IE configuration changes in the future. The module will have to be run again to sync the latest changes.  **Choices:**   - `"ie"` |

## [Notes](win_http_proxy_module.md#id3)

> **Note:**
>
> - This is not the same as the proxy settings set in Internet Explorer, also known as `WinINet`; use the [community.windows.win_inet_proxy](win_inet_proxy_module.md#ansible-collections-community-windows-win-inet-proxy-module) module to manage that instead.
> - These settings are set system wide and not per user, it will require Administrative privileges to run.

## [See Also](win_http_proxy_module.md#id4)

> **See also:**
>
> [community.windows.win_inet_proxy](win_inet_proxy_module.md#ansible-collections-community-windows-win-inet-proxy-module)
> :   Manages proxy settings for WinINet and Internet Explorer.

## [Examples](win_http_proxy_module.md#id5)

```yaml+jinja
- name: Set a proxy to use for all protocols
  community.windows.win_http_proxy:
    proxy: hostname

- name: Set a proxy with a specific port with a bypass list
  community.windows.win_http_proxy:
    proxy: hostname:8080
    bypass:
    - server1
    - server2
    - <local>

- name: Set the proxy based on the IE proxy settings
  community.windows.win_http_proxy:
    source: ie

- name: Set a proxy for specific protocols
  community.windows.win_http_proxy:
    proxy:
      http: hostname:8080
      https: hostname:8443

- name: Set a proxy for specific protocols using a string
  community.windows.win_http_proxy:
    proxy: http=hostname:8080;https=hostname:8443
    bypass: server1,server2,<local>

- name: Remove any proxy settings
  community.windows.win_http_proxy:
    proxy: ''
    bypass: ''
```

### Authors

- Jordan Borean (@jborean93)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
