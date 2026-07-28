---
collection: ansible
version: "6"
title: "community.windows.win_inet_proxy module – Manages proxy settings for WinINet and Internet Explorer"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_inet_proxy_module.html
fetched_at: 2026-07-27T17:23:33+00:00
---
# community.windows.win_inet_proxy module – Manages proxy settings for WinINet and Internet Explorer

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
> To use it in a playbook, specify: `community.windows.win_inet_proxy`.

- [Synopsis](win_inet_proxy_module.md#synopsis)
- [Parameters](win_inet_proxy_module.md#parameters)
- [Notes](win_inet_proxy_module.md#notes)
- [See Also](win_inet_proxy_module.md#see-also)
- [Examples](win_inet_proxy_module.md#examples)

## [Synopsis](win_inet_proxy_module.md#id1)

- Used to set or remove proxy settings for Windows INet which includes Internet Explorer.
- WinINet is a framework used by interactive applications to submit web requests through.
- The proxy settings can also be used by other applications like Firefox, Chrome, and others but there is no definitive list.

## [Parameters](win_inet_proxy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auto_config_url**  string | The URL of a proxy configuration script.  Proxy configuration scripts are typically JavaScript files with the `.pac` extension that implement the `FindProxyForURL(url, host` function.  Omit, set to null or an empty string to remove the auto config URL.  This corresponds to the checkbox *Use automatic configuration script* in the connection settings window. |
| **auto_detect**  boolean | Whether to configure WinINet to automatically detect proxy settings through Web Proxy Auto-Detection `WPAD`.  This corresponds to the checkbox *Automatically detect settings* in the connection settings window.  Choices:   - `false` - `true` ← (default) |
| **bypass**  list / elements=string | A list of hosts that will bypass the set proxy when being accessed.  Use `<local>` to match hostnames that are not fully qualified domain names. This is useful when needing to connect to intranet sites using just the hostname. If defined, this should be the last entry in the bypass list.  Use `<-loopback>` to stop automatically bypassing the proxy when connecting through any loopback address like `127.0.0.1`, `localhost`, or the local hostname.  Omit, set to null or an empty string/list to remove the bypass list.  If this is set then *proxy* must also be set. |
| **connection**  string | The name of the IE connection to set the proxy settings for.  These are the connections under the *Dial-up and Virtual Private Network* header in the IE settings.  When omitted, the default LAN connection is used. |
| **proxy**  any | A string or dict that specifies the proxy to be set.  If setting a string, should be in the form `hostname`, `hostname:port`, or `protocol=hostname:port`.  If the port is undefined, the default port for the protocol in use is used.  If setting a dict, the keys should be the protocol and the values should be the hostname and/or port for that protocol.  Valid protocols are `http`, `https`, `ftp`, and `socks`.  Omit, set to null or an empty string to remove the proxy settings. |

## [Notes](win_inet_proxy_module.md#id3)

> **Note:**
>
> - This is not the same as the proxy settings set in WinHTTP through the `netsh` command. Use the [community.windows.win_http_proxy](win_http_proxy_module.md#ansible-collections-community-windows-win-http-proxy-module) module to manage that instead.
> - These settings are by default set per user and not system wide. A registry property must be set independently from this module if you wish to apply the proxy for all users. See examples for more detail.
> - If per user proxy settings are desired, use *become* to become any local user on the host. No password is needed to be set for this to work.
> - If the proxy requires authentication, set the credentials using the [community.windows.win_credential](win_credential_module.md#ansible-collections-community-windows-win-credential-module) module. This requires *become* to be used so the credential store can be accessed.

## [See Also](win_inet_proxy_module.md#id4)

> **See also:**
>
> [community.windows.win_http_proxy](win_http_proxy_module.md#ansible-collections-community-windows-win-http-proxy-module)
> :   Manages proxy settings for WinHTTP.
>
> [community.windows.win_credential](win_credential_module.md#ansible-collections-community-windows-win-credential-module)
> :   Manages Windows Credentials in the Credential Manager.

## [Examples](win_inet_proxy_module.md#id5)

```yaml+jinja
# This should be set before running the win_inet_proxy module
- name: Configure IE proxy settings to apply to all users
  ansible.windows.win_regedit:
    path: HKLM:\SOFTWARE\Policies\Microsoft\Windows\CurrentVersion\Internet Settings
    name: ProxySettingsPerUser
    data: 0
    type: dword
    state: present

# This should be set before running the win_inet_proxy module
- name: Configure IE proxy settings to apply per user
  ansible.windows.win_regedit:
    path: HKLM:\SOFTWARE\Policies\Microsoft\Windows\CurrentVersion\Internet Settings
    name: ProxySettingsPerUser
    data: 1
    type: dword
    state: present

- name: Configure IE proxy to use auto detected settings without an explicit proxy
  win_inet_proxy:
    auto_detect: yes

- name: Configure IE proxy to use auto detected settings with a configuration script
  win_inet_proxy:
    auto_detect: yes
    auto_config_url: http://proxy.ansible.com/proxy.pac

- name: Configure IE to use explicit proxy host
  win_inet_proxy:
    auto_detect: yes
    proxy: ansible.proxy

- name: Configure IE to use explicit proxy host with port and without auto detection
  win_inet_proxy:
    auto_detect: no
    proxy: ansible.proxy:8080

- name: Configure IE to use a specific proxy per protocol
  win_inet_proxy:
    proxy:
      http: ansible.proxy:8080
      https: ansible.proxy:8443

- name: Configure IE to use a specific proxy per protocol using a string
  win_inet_proxy:
    proxy: http=ansible.proxy:8080;https=ansible.proxy:8443

- name: Set a proxy with a bypass list
  win_inet_proxy:
    proxy: ansible.proxy
    bypass:
    - server1
    - server2
    - <-loopback>
    - <local>

- name: Remove any explicit proxies that are set
  win_inet_proxy:
    proxy: ''
    bypass: ''

# This should be done after setting the IE proxy with win_inet_proxy
- name: Import IE proxy configuration to WinHTTP
  win_http_proxy:
    source: ie

# Explicit credentials can only be set per user and require become to work
- name: Set credential to use for proxy auth
  win_credential:
    name: ansible.proxy  # The name should be the FQDN of the proxy host
    type: generic_password
    username: proxyuser
    secret: proxypass
    state: present
  become: yes
  become_user: '{{ ansible_user }}'
  become_method: runas
```

### Authors

- Jordan Borean (@jborean93)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
