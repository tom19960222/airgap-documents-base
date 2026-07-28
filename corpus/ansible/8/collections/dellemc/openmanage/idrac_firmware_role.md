---
collection: ansible
version: "8"
title: "dellemc.openmanage.idrac_firmware role – Firmware update from a repository on a network share (CIFS, NFS, HTTP, HTTPS, FTP)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/idrac_firmware_role.html
fetched_at: 2026-07-28T02:05:01+00:00
---
# dellemc.openmanage.idrac_firmware role – Firmware update from a repository on a network share (CIFS, NFS, HTTP, HTTPS, FTP)

> **Note:**
>
> This role is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/ui/repo/published/dellemc/openmanage/) (version 7.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it use: `ansible-galaxy collection install dellemc.openmanage`.
>
> To use it in a playbook, specify: `dellemc.openmanage.idrac_firmware`.

- [Entry point `main` – Firmware update from a repository on a network share (CIFS, NFS, HTTP, HTTPS, FTP)](idrac_firmware_role.md#entry-point-main-firmware-update-from-a-repository-on-a-network-share-cifs-nfs-http-https-ftp)

  - [Synopsis](idrac_firmware_role.md#synopsis)
  - [Parameters](idrac_firmware_role.md#parameters)

## [Entry point `main` – Firmware update from a repository on a network share (CIFS, NFS, HTTP, HTTPS, FTP)](idrac_firmware_role.md#id1)

New in dellemc.openmanage 7.5.0

### [Synopsis](idrac_firmware_role.md#id2)

- Update the Firmware by connecting to a network share (CIFS, NFS, HTTP, HTTPS, FTP) that contains a catalog of available updates.

### [Parameters](idrac_firmware_role.md#id3)

| Parameter | Comments |
| --- | --- |
| **apply_update**  boolean | If *apply_update* is set to `true`, then the packages are applied.  If *apply_update* is set to `false`, no updates are applied, and a catalog report of packages is generated and returned.  **Choices:**   - `false` - `true` ← (default) |
| **ca_path**  path | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **catalog_file_name**  string | Catalog file name relative to the *share_name*.  **Default:** `"Catalog.xml"` |
| **hostname**  string / required | iDRAC IP Address or hostname. |
| **http_timeout**  integer | The socket level timeout in seconds.  **Default:** `30` |
| **https_port**  integer | iDRAC port.  **Default:** `443` |
| **ignore_cert_warning**  boolean | Specifies if certificate warnings are ignored when HTTPS share is used. If `true` option is set, then the certificate warnings are ignored.  **Choices:**   - `false` - `true` ← (default) |
| **job_wait**  boolean | Whether to wait for job completion or not.  **Choices:**   - `false` - `true` ← (default) |
| **password**  string / required | iDRAC user password. |
| **proxy_passwd**  string | The password for the proxy server. |
| **proxy_port**  integer | The Port for the proxy server.  This is required when *proxy_support* is `ParametersProxy`. |
| **proxy_server**  string | The IP address of the proxy server.  This IP will not be validated. The download job will be created even for invalid *proxy_server*. Please check the results of the job for error details.  This is required when *proxy_support* is `ParametersProxy`. |
| **proxy_support**  string | Specifies if a proxy should be used.  Proxy parameters are applicable on `HTTP`, `HTTPS`, and `FTP` share type of repositories.  `ParametersProxy`, sets the proxy parameters for the current firmware operation.  `DefaultProxy`, iDRAC uses the proxy values set by default.  Default Proxy can be set in the Lifecycle Controller attributes using [dellemc.openmanage.idrac_attributes](idrac_attributes_module.md#ansible-collections-dellemc-openmanage-idrac-attributes-module).  `Off`, will not use the proxy.  For iDRAC7 and iDRAC8 based servers, use proxy server with basic authentication.  For iDRAC9 based servers, ensure that you use digest authentication for the proxy server, basic authentication is not supported.  **Choices:**   - `"ParametersProxy"` - `"DefaultProxy"` - `"Off"` ← (default) |
| **proxy_type**  string | The proxy type of the proxy server.  This is required when *proxy_support* is `ParametersProxy`.  **Choices:**   - `"HTTP"` - `"SOCKS"` |
| **proxy_uname**  string | The user name for the proxy server. |
| **reboot**  boolean | Provides the option to apply the update packages immediately or in the next reboot.  If *reboot* is set to `true`, then the packages are applied immediately.  If *reboot* is set to `false`, then the packages are staged and applied in the next reboot.  Packages that do not require a reboot are applied immediately irrespective of I (reboot).  **Choices:**   - `false` ← (default) - `true` |
| **share_name**  string / required | Network share path of update repository. CIFS, NFS, HTTP, HTTPS and FTP share types are supported. |
| **share_password**  string | Network share user password. This option is mandatory for CIFS Network Share. |
| **share_user**  string | Network share user in the format [‘user@domain](mailto:'user%40domain)’ or ‘domain\\user’ if user is part of a domain else ‘user’. This option is mandatory for CIFS Network Share. |
| **username**  string / required | iDRAC username with admin privileges. |
| **validate_certs**  boolean | If `false`, the SSL certificates will not be validated.  Configure `false` only on personally controlled sites where self-signed certificates are used.  **Choices:**   - `false` - `true` ← (default) |

#### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
