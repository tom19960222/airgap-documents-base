---
collection: ansible
version: "6"
title: "ansible.windows.win_get_url module – Downloads file from HTTP, HTTPS, or FTP to node"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/windows/win_get_url_module.html
fetched_at: 2026-07-27T16:44:57+00:00
---
# ansible.windows.win_get_url module – Downloads file from HTTP, HTTPS, or FTP to node

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
> To use it in a playbook, specify: `ansible.windows.win_get_url`.

- [Synopsis](win_get_url_module.md#synopsis)
- [Parameters](win_get_url_module.md#parameters)
- [Notes](win_get_url_module.md#notes)
- [See Also](win_get_url_module.md#see-also)
- [Examples](win_get_url_module.md#examples)
- [Return Values](win_get_url_module.md#return-values)

## [Synopsis](win_get_url_module.md#id1)

- Downloads files from HTTP, HTTPS, or FTP to the remote server.
- The remote server *must* have direct access to the remote resource.
- For non-Windows targets, use the [ansible.builtin.get_url](../builtin/get_url_module.md#ansible-collections-ansible-builtin-get-url-module) module instead.

## [Parameters](win_get_url_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **checksum**  string | If a *checksum* is passed to this parameter, the digest of the destination file will be calculated after it is downloaded to ensure its integrity and verify that the transfer completed successfully.  This option cannot be set with *checksum_url*. |
| **checksum_algorithm**  string | Specifies the hashing algorithm used when calculating the checksum of the remote and destination file.  Choices:   - `"md5"` - `"sha1"` ← (default) - `"sha256"` - `"sha384"` - `"sha512"` |
| **checksum_url**  string | Specifies a URL that contains the checksum values for the resource at *url*.  Like `checksum`, this is used to verify the integrity of the remote transfer.  This option cannot be set with *checksum*. |
| **client_cert**  string | The path to the client certificate (.pfx) that is used for X509 authentication. This path can either be the path to the `pfx` on the filesystem or the PowerShell certificate path `Cert:\CurrentUser\My\<thumbprint>`.  The WinRM connection must be authenticated with `CredSSP` or `become` is used on the task if the certificate file is not password protected.  Other authentication types can set *client_cert_password* when the cert is password protected. |
| **client_cert_password**  string | The password for *client_cert* if the cert is password protected. |
| **dest**  path / required | The location to save the file at the URL.  Be sure to include a filename and extension as appropriate. |
| **follow_redirects**  string | Whether or the module should follow redirects.  `all` will follow all redirect.  `none` will not follow any redirect.  `safe` will follow only “safe” redirects, where “safe” means that the client is only doing a `GET` or `HEAD` on the URI to which it is being redirected.  When following a redirected URL, the `Authorization` header and any credentials set will be dropped and not redirected.  Choices:   - `"all"` - `"none"` - `"safe"` ← (default) |
| **force**  boolean | If `yes`, will download the file every time and replace the file if the contents change. If `no`, will only download the file if it does not exist or the remote file has been modified more recently than the local file.  This works by sending an http HEAD request to retrieve last modified time of the requested resource, so for this to work, the remote web server must support HEAD requests.  Choices:   - `false` - `true` ← (default) |
| **force_basic_auth**  boolean | By default the authentication header is only sent when a webservice responses to an initial request with a 401 status. Since some basic auth services do not properly send a 401, logins will fail.  This option forces the sending of the Basic authentication header upon the original request.  Choices:   - `false` ← (default) - `true` |
| **headers**  dictionary | Extra headers to set on the request.  This should be a dictionary where the key is the header name and the value is the value for that header. |
| **http_agent**  string | Header to identify as, generally appears in web server logs.  This is set to the `User-Agent` header on a HTTP request.  Default: `"ansible-httpget"` |
| **maximum_redirection**  integer | Specify how many times the module will redirect a connection to an alternative URI before the connection fails.  If set to `0` or *follow_redirects* is set to `none`, or `safe` when not doing a `GET` or `HEAD` it prevents all redirection.  Default: `50` |
| **proxy_password**  string | The password for *proxy_username*. |
| **proxy_url**  string | An explicit proxy to use for the request.  By default, the request will use the IE defined proxy unless *use_proxy* is set to `no`. |
| **proxy_use_default_credential**  boolean | Uses the current user’s credentials when authenticating with a proxy host protected with `NTLM`, `Kerberos`, or `Negotiate` authentication.  Proxies that use `Basic` auth will still require explicit credentials through the *proxy_username* and *proxy_password* options.  The module will only have access to the user’s credentials if using `become` with a password, you are connecting with SSH using a password, or connecting with WinRM using `CredSSP` or `Kerberos with delegation`.  If not using `become` or a different auth method to the ones stated above, there will be no default credentials available and no proxy authentication will occur.  Choices:   - `false` ← (default) - `true` |
| **proxy_username**  string | The username to use for proxy authentication. |
| **url**  string / required | The full URL of a file to download. |
| **url_method**  aliases: method  string | The HTTP Method of the request. |
| **url_password**  aliases: password  string | The password for *url_username*.  The alias *password* is deprecated and will be removed on the major release after `2022-07-01`. |
| **url_timeout**  aliases: timeout  integer | Specifies how long the request can be pending before it times out (in seconds).  Set to `0` to specify an infinite timeout.  Default: `30` |
| **url_username**  aliases: user, username  string | The username to use for authentication.  The alias *user* and *username* is deprecated and will be removed on the major release after `2022-07-01`. |
| **use_default_credential**  boolean | Uses the current user’s credentials when authenticating with a server protected with `NTLM`, `Kerberos`, or `Negotiate` authentication.  Sites that use `Basic` auth will still require explicit credentials through the *url_username* and *url_password* options.  The module will only have access to the user’s credentials if using `become` with a password, you are connecting with SSH using a password, or connecting with WinRM using `CredSSP` or `Kerberos with delegation`.  If not using `become` or a different auth method to the ones stated above, there will be no default credentials available and no authentication will occur.  Choices:   - `false` ← (default) - `true` |
| **use_proxy**  boolean | If `no`, it will not use the proxy defined in IE for the current user.  Choices:   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](win_get_url_module.md#id3)

> **Note:**
>
> - If your URL includes an escaped slash character (%2F) this module will convert it to a real slash. This is a result of the behaviour of the System.Uri class as described in [the documentation](https://docs.microsoft.com/en-us/dotnet/framework/configure-apps/file-schema/network/schemesettings-element-uri-settings#remarks).

## [See Also](win_get_url_module.md#id4)

> **See also:**
>
> [ansible.builtin.get_url](../builtin/get_url_module.md#ansible-collections-ansible-builtin-get-url-module)
> :   Downloads files from HTTP, HTTPS, or FTP to node.
>
> [ansible.builtin.uri](../builtin/uri_module.md#ansible-collections-ansible-builtin-uri-module)
> :   Interacts with webservices.
>
> [ansible.windows.win_uri](win_uri_module.md#ansible-collections-ansible-windows-win-uri-module)
> :   Interacts with webservices.
>
> [community.windows.win_inet_proxy](../../community/windows/win_inet_proxy_module.md#ansible-collections-community-windows-win-inet-proxy-module)
> :   Manages proxy settings for WinINet and Internet Explorer.

## [Examples](win_get_url_module.md#id5)

```yaml+jinja
- name: Download earthrise.jpg to specified path
  ansible.windows.win_get_url:
    url: http://www.example.com/earthrise.jpg
    dest: C:\Users\RandomUser\earthrise.jpg

- name: Download earthrise.jpg to specified path only if modified
  ansible.windows.win_get_url:
    url: http://www.example.com/earthrise.jpg
    dest: C:\Users\RandomUser\earthrise.jpg
    force: no

- name: Download earthrise.jpg to specified path through a proxy server.
  ansible.windows.win_get_url:
    url: http://www.example.com/earthrise.jpg
    dest: C:\Users\RandomUser\earthrise.jpg
    proxy_url: http://10.0.0.1:8080
    proxy_username: username
    proxy_password: password

- name: Download file from FTP with authentication
  ansible.windows.win_get_url:
    url: ftp://server/file.txt
    dest: '%TEMP%\ftp-file.txt'
    url_username: ftp-user
    url_password: ftp-password

- name: Download src with sha256 checksum url
  ansible.windows.win_get_url:
    url: http://www.example.com/earthrise.jpg
    dest: C:\temp\earthrise.jpg
    checksum_url: http://www.example.com/sha256sum.txt
    checksum_algorithm: sha256
    force: True

- name: Download src with sha256 checksum url
  ansible.windows.win_get_url:
    url: http://www.example.com/earthrise.jpg
    dest: C:\temp\earthrise.jpg
    checksum: a97e6837f60cec6da4491bab387296bbcd72bdba
    checksum_algorithm: sha1
    force: True
```

## [Return Values](win_get_url_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **checksum_dest**  string | <algorithm> checksum of the file after the download  Returned: success and dest has been downloaded  Sample: `"6e642bb8dd5c2e027bf21dd923337cbb4214f827"` |
| **checksum_src**  string | <algorithm> checksum of the remote resource  Returned: force=yes or dest did not exist  Sample: `"6e642bb8dd5c2e027bf21dd923337cbb4214f827"` |
| **dest**  string | destination file/path  Returned: always  Sample: `"C:\\Users\\RandomUser\\earthrise.jpg"` |
| **elapsed**  float | The elapsed seconds between the start of poll and the end of the module.  Returned: always  Sample: `2.1406487` |
| **msg**  string | Error message, or HTTP status message from web-server  Returned: always  Sample: `"OK"` |
| **size**  integer | size of the dest file  Returned: success  Sample: `1220` |
| **status_code**  integer | HTTP status code  Returned: always  Sample: `200` |
| **url**  string | requested url  Returned: always  Sample: `"http://www.example.com/earthrise.jpg"` |

### Authors

- Paul Durivage (@angstwad)
- Takeshi Kuramochi (@tksarah)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
[Communication](index.md#communication-for-ansible-windows)
