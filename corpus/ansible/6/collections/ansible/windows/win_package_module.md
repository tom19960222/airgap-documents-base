---
collection: ansible
version: "6"
title: "ansible.windows.win_package module – Installs/uninstalls an installable package"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/windows/win_package_module.html
fetched_at: 2026-07-27T16:44:59+00:00
---
# ansible.windows.win_package module – Installs/uninstalls an installable package

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ansible/windows) (version 1.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.win_package`.

- [Synopsis](win_package_module.md#synopsis)
- [Parameters](win_package_module.md#parameters)
- [Notes](win_package_module.md#notes)
- [See Also](win_package_module.md#see-also)
- [Examples](win_package_module.md#examples)
- [Return Values](win_package_module.md#return-values)

## [Synopsis](win_package_module.md#id1)

- Installs or uninstalls software packages for Windows.
- Supports `.exe`, `.msi`, `.msp`, `.appx`, `.appxbundle`, `.msix`, and `.msixbundle`.
- These packages can be sourced from the local file system, network file share or a url.
- See *provider* for more info on each package type that is supported.

## [Parameters](win_package_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **arguments**  any | Any arguments the installer needs to either install or uninstall the package.  If the package is an MSI do not supply the `/qn`, `/log` or `/norestart` arguments.  This is only used for the `msi`, `msp`, and `registry` providers.  Can be a list of arguments and the module will escape the arguments as necessary, it is recommended to use a string when dealing with MSI packages due to the unique escaping issues with msiexec.  When using a list of arguments each item in the list is considered to be a single argument. As such, if an argument in the list contains a space then Ansible will quote this to ensure that this is seen by Windows as a single argument. Should this behaviour not be what is required, the argument should be split into two separate list items. See the examples section for more detail. |
| **chdir**  path | Set the specified path as the current working directory before installing or uninstalling a package.  This is only used for the `msi`, `msp`, and `registry` providers. |
| **client_cert**  string | The path to the client certificate (.pfx) that is used for X509 authentication. This path can either be the path to the `pfx` on the filesystem or the PowerShell certificate path `Cert:\CurrentUser\My\<thumbprint>`.  The WinRM connection must be authenticated with `CredSSP` or `become` is used on the task if the certificate file is not password protected.  Other authentication types can set *client_cert_password* when the cert is password protected. |
| **client_cert_password**  string | The password for *client_cert* if the cert is password protected. |
| **creates_path**  path | Will check the existence of the path specified and use the result to determine whether the package is already installed.  You can use this in conjunction with `product_id` and other `creates_*`. |
| **creates_service**  string | Will check the existing of the service specified and use the result to determine whether the package is already installed.  You can use this in conjunction with `product_id` and other `creates_*`. |
| **creates_version**  string | Will check the file version property of the file at `creates_path` and use the result to determine whether the package is already installed.  `creates_path` MUST be set and is a file.  You can use this in conjunction with `product_id` and other `creates_*`. |
| **expected_return_code**  list / elements=integer | One or more return codes from the package installation that indicates success.  The return codes are read as a signed integer, any values greater than 2147483647 need to be represented as the signed equivalent, i.e. `4294967295` is `-1`.  To convert a unsigned number to the signed equivalent you can run “[Int32](“0x{0:X}” -f ([UInt32]3221225477))”.  A return code of `3010` usually means that a reboot is required, the `reboot_required` return value is set if the return code is `3010`.  This is only used for the `msi`, `msp`, and `registry` providers.  Default: `[0, 3010]` |
| **follow_redirects**  string | Whether or the module should follow redirects.  `all` will follow all redirect.  `none` will not follow any redirect.  `safe` will follow only “safe” redirects, where “safe” means that the client is only doing a `GET` or `HEAD` on the URI to which it is being redirected.  When following a redirected URL, the `Authorization` header and any credentials set will be dropped and not redirected.  Choices:   - `"all"` - `"none"` - `"safe"` ← (default) |
| **force_basic_auth**  boolean | By default the authentication header is only sent when a webservice responses to an initial request with a 401 status. Since some basic auth services do not properly send a 401, logins will fail.  This option forces the sending of the Basic authentication header upon the original request.  Choices:   - `false` ← (default) - `true` |
| **headers**  dictionary | Extra headers to set on the request.  This should be a dictionary where the key is the header name and the value is the value for that header. |
| **http_agent**  string | Header to identify as, generally appears in web server logs.  This is set to the `User-Agent` header on a HTTP request.  Default: `"ansible-httpget"` |
| **log_path**  path | Specifies the path to a log file that is persisted after a package is installed or uninstalled.  This is only used for the `msi` or `msp` provider.  When omitted, a temporary log file is used instead for those providers.  This is only valid for MSI files, use `arguments` for the `registry` provider. |
| **maximum_redirection**  integer | Specify how many times the module will redirect a connection to an alternative URI before the connection fails.  If set to `0` or *follow_redirects* is set to `none`, or `safe` when not doing a `GET` or `HEAD` it prevents all redirection.  Default: `50` |
| **password**  aliases: user_password  string | The password for `user_name`, must be set when `user_name` is.  This option is deprecated in favour of using become, see examples for more information. Will be removed on the major release after `2022-07-01`. |
| **path**  string | Location of the package to be installed or uninstalled.  This package can either be on the local file system, network share or a url.  When `state=present`, `product_id` is not set and the path is a URL, this file will always be downloaded to a temporary directory for idempotency checks, otherwise the file will only be downloaded if the package has not been installed based on the `product_id` checks.  If `state=present` then this value MUST be set.  If `state=absent` then this value does not need to be set if `product_id` is. |
| **product_id**  aliases: productid  string | The product id of the installed packaged.  This is used for checking whether the product is already installed and getting the uninstall information if `state=absent`.  For msi packages, this is the `ProductCode` (GUID) of the package. This can be found under the same registry paths as the `registry` provider.  For msp packages, this is the `PatchCode` (GUID) of the package which can found under the `Details -> Revision number` of the file’s properties.  For msix packages, this is the `Name` or `PackageFullName` of the package found under the `Get-AppxPackage` cmdlet.  For registry (exe) packages, this is the registry key name under the registry paths specified in *provider*.  This value is ignored if `path` is set to a local accesible file path and the package is not an `exe`.  This SHOULD be set when the package is an `exe`, or the path is a url or a network share and credential delegation is not being used. The `creates_*` options can be used instead but is not recommended.  The alias *productid* is deprecated and will be removed on the major release after `2022-07-01`. |
| **provider**  string | Set the package provider to use when searching for a package.  The `auto` provider will select the proper provider if *path* otherwise it scans all the other providers based on the *product_id*.  The `msi` provider scans for MSI packages installed on a machine wide and current user context based on the `ProductCode` of the MSI.  The `msix` provider is used to install `.appx`, `.msix`, `.appxbundle`, or `.msixbundle` packages. These packages are only installed or removed on the current use. The host must be set to allow sideloaded apps or in developer mode. See the examples for how to enable this. If a package is already installed but `path` points to an updated package, this will be installed over the top of the existing one.  The `msp` provider scans for all MSP patches installed on a machine wide and current user context based on the `PatchCode` of the MSP. A `msp` will be applied or removed on all `msi` products that it applies to and is installed. If the patch is obsoleted or superseded then no action will be taken.  The `registry` provider is used for traditional `exe` installers and uses the following registry path to determine if a product was installed; `HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall`, `HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall`, `HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall`, and `HKCU:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall`.  Choices:   - `"auto"` ← (default) - `"msi"` - `"msix"` - `"msp"` - `"registry"` |
| **proxy_password**  string | The password for *proxy_username*. |
| **proxy_url**  string | An explicit proxy to use for the request.  By default, the request will use the IE defined proxy unless *use_proxy* is set to `no`. |
| **proxy_use_default_credential**  boolean | Uses the current user’s credentials when authenticating with a proxy host protected with `NTLM`, `Kerberos`, or `Negotiate` authentication.  Proxies that use `Basic` auth will still require explicit credentials through the *proxy_username* and *proxy_password* options.  The module will only have access to the user’s credentials if using `become` with a password, you are connecting with SSH using a password, or connecting with WinRM using `CredSSP` or `Kerberos with delegation`.  If not using `become` or a different auth method to the ones stated above, there will be no default credentials available and no proxy authentication will occur.  Choices:   - `false` ← (default) - `true` |
| **proxy_username**  string | The username to use for proxy authentication. |
| **state**  aliases: ensure  string | Whether to install or uninstall the package.  The module uses *product_id* to determine whether the package is installed or not.  For all providers but `auto`, the *path* can be used for idempotency checks if it is locally accesible filesystem path.  The alias *ensure* is deprecated and will be removed on the major release after `2022-07-01`.  Choices:   - `"absent"` - `"present"` ← (default) |
| **url_method**  string | The HTTP Method of the request. |
| **url_password**  string | The password for *url_username*. |
| **url_timeout**  integer | Specifies how long the request can be pending before it times out (in seconds).  Set to `0` to specify an infinite timeout.  Default: `30` |
| **url_username**  string | The username to use for authentication. |
| **use_default_credential**  boolean | Uses the current user’s credentials when authenticating with a server protected with `NTLM`, `Kerberos`, or `Negotiate` authentication.  Sites that use `Basic` auth will still require explicit credentials through the *url_username* and *url_password* options.  The module will only have access to the user’s credentials if using `become` with a password, you are connecting with SSH using a password, or connecting with WinRM using `CredSSP` or `Kerberos with delegation`.  If not using `become` or a different auth method to the ones stated above, there will be no default credentials available and no authentication will occur.  Choices:   - `false` ← (default) - `true` |
| **use_proxy**  boolean | If `no`, it will not use the proxy defined in IE for the current user.  Choices:   - `false` - `true` ← (default) |
| **username**  aliases: user_name  string | Username of an account with access to the package if it is located on a file share.  This is only needed if the WinRM transport is over an auth method that does not support credential delegation like Basic or NTLM or become is not used.  This option is deprecated in favour of using become, see examples for more information. Will be removed on the major release after `2022-07-01`. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **wait_for_children**  boolean  added in ansible.windows 1.3.0 | The module will wait for the process it spawns to finish but any processes spawned in that child process as ignored.  Set to `yes` to wait for all descendent processes to finish before the module returns.  This is useful if the install/uninstaller is just a wrapper which then calls the actual installer as its own child process. When this option is `yes` then the module will wait for both processes to finish before returning.  This should not be required for most installers and setting to `yes` could result in the module not returning until the process it is waiting for has been stopped manually.  Requires Windows Server 2012 or Windows 8 or newer to use.  Choices:   - `false` ← (default) - `true` |

## [Notes](win_package_module.md#id3)

> **Note:**
>
> - When `state=absent` and the product is an exe, the path may be different from what was used to install the package originally. If path is not set then the path used will be what is set under `QuietUninstallString` or `UninstallString` in the registry for that *product_id*.
> - By default all msi installs and uninstalls will be run with the arguments `/log, /qn, /norestart`.
> - All the installation checks under `product_id` and `creates_*` add together, if one fails then the program is considered to be absent.

## [See Also](win_package_module.md#id4)

> **See also:**
>
> [chocolatey.chocolatey.win_chocolatey](../../chocolatey/chocolatey/win_chocolatey_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-module)
> :   Manage packages using chocolatey.
>
> [community.windows.win_hotfix](../../community/windows/win_hotfix_module.md#ansible-collections-community-windows-win-hotfix-module)
> :   Install and uninstalls Windows hotfixes.
>
> [ansible.windows.win_updates](win_updates_module.md#ansible-collections-ansible-windows-win-updates-module)
> :   Download and install Windows updates.
>
> [community.windows.win_inet_proxy](../../community/windows/win_inet_proxy_module.md#ansible-collections-community-windows-win-inet-proxy-module)
> :   Manages proxy settings for WinINet and Internet Explorer.

## [Examples](win_package_module.md#id5)

```yaml+jinja
- name: Install the Visual C thingy
  ansible.windows.win_package:
    path: http://download.microsoft.com/download/1/6/B/16B06F60-3B20-4FF2-B699-5E9B7962F9AE/VSU_4/vcredist_x64.exe
    product_id: '{CF2BEA3C-26EA-32F8-AA9B-331F7E34BA97}'
    arguments: /install /passive /norestart

- name: Install Visual C thingy with list of arguments instead of a string
  ansible.windows.win_package:
    path: http://download.microsoft.com/download/1/6/B/16B06F60-3B20-4FF2-B699-5E9B7962F9AE/VSU_4/vcredist_x64.exe
    product_id: '{CF2BEA3C-26EA-32F8-AA9B-331F7E34BA97}'
    arguments:
    - /install
    - /passive
    - /norestart

- name: Install MSBuild thingy with arguments split to prevent quotes
  ansible.windows.win_package:
    path: https://download.visualstudio.microsoft.com/download/pr/9665567e-f580-4acd-85f2-bc94a1db745f/vs_BuildTools.exe
    product_id: '{D1437F51-786A-4F57-A99C-F8E94FBA1BD8}'
    arguments:
    - --norestart
    - --passive
    - --wait
    - --add
    - Microsoft.Net.Component.4.6.1.TargetingPack
    - --add
    - Microsoft.Net.Component.4.6.TargetingPack

- name: Install Remote Desktop Connection Manager from msi with a permanent log
  ansible.windows.win_package:
    path: https://download.microsoft.com/download/A/F/0/AF0071F3-B198-4A35-AA90-C68D103BDCCF/rdcman.msi
    product_id: '{0240359E-6A4C-4884-9E94-B397A02D893C}'
    state: present
    log_path: D:\logs\vcredist_x64-exe-{{lookup('pipe', 'date +%Y%m%dT%H%M%S')}}.log

- name: Uninstall Remote Desktop Connection Manager
  ansible.windows.win_package:
    product_id: '{0240359E-6A4C-4884-9E94-B397A02D893C}'
    state: absent

- name: Install Remote Desktop Connection Manager locally omitting the product_id
  ansible.windows.win_package:
    path: C:\temp\rdcman.msi
    state: present

- name: Uninstall Remote Desktop Connection Manager from local MSI omitting the product_id
  ansible.windows.win_package:
    path: C:\temp\rdcman.msi
    state: absent

# 7-Zip exe doesn't use a guid for the Product ID
- name: Install 7zip from a network share with specific credentials
  ansible.windows.win_package:
    path: \\domain\programs\7z.exe
    product_id: 7-Zip
    arguments: /S
    state: present
  become: yes
  become_method: runas
  become_flags: logon_type=new_credential logon_flags=netcredentials_only
  vars:
    ansible_become_user: DOMAIN\User
    ansible_become_password: Password

- name: Install 7zip and use a file version for the installation check
  ansible.windows.win_package:
    path: C:\temp\7z.exe
    creates_path: C:\Program Files\7-Zip\7z.exe
    creates_version: 16.04
    state: present

- name: Uninstall 7zip from the exe
  ansible.windows.win_package:
    path: C:\Program Files\7-Zip\Uninstall.exe
    product_id: 7-Zip
    arguments: /S
    state: absent

- name: Uninstall 7zip without specifying the path
  ansible.windows.win_package:
    product_id: 7-Zip
    arguments: /S
    state: absent

- name: Install application and override expected return codes
  ansible.windows.win_package:
    path: https://download.microsoft.com/download/1/6/7/167F0D79-9317-48AE-AEDB-17120579F8E2/NDP451-KB2858728-x86-x64-AllOS-ENU.exe
    product_id: '{7DEBE4EB-6B40-3766-BB35-5CBBC385DA37}'
    arguments: '/q /norestart'
    state: present
    expected_return_code: [0, 666, 3010]

- name: Install a .msp patch
  ansible.windows.win_package:
    path: C:\Patches\Product.msp
    state: present

- name: Remove a .msp patch
  ansible.windows.win_package:
    product_id: '{AC76BA86-A440-FFFF-A440-0C13154E5D00}'
    state: absent

- name: Enable installation of 3rd party MSIX packages
  ansible.windows.win_regedit:
    path: HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\AppModelUnlock
    name: AllowAllTrustedApps
    data: 1
    type: dword
    state: present

- name: Install an MSIX package for the current user
  ansible.windows.win_package:
    path: C:\Installers\Calculator.msix  # Can be .appx, .msixbundle, or .appxbundle
    state: present

- name: Uninstall an MSIX package using the product_id
  ansible.windows.win_package:
    product_id: InputApp
    state: absent
```

## [Return Values](win_package_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **log**  string | The contents of the MSI or MSP log.  Returned: installation/uninstallation failure for MSI or MSP packages  Sample: `"Installation completed successfully"` |
| **rc**  integer | The return code of the package process.  Returned: change occurred  Sample: `0` |
| **reboot_required**  boolean | Whether a reboot is required to finalise package. This is set to true if the executable return code is 3010.  Returned: always  Sample: `true` |
| **stderr**  string | The stderr stream of the package process.  Returned: failure during install or uninstall  Sample: `"Failed to install program"` |
| **stdout**  string | The stdout stream of the package process.  Returned: failure during install or uninstall  Sample: `"Installing program"` |

### Authors

- Trond Hindenes (@trondhindenes)
- Jordan Borean (@jborean93)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
[Communication](index.md#communication-for-ansible-windows)
