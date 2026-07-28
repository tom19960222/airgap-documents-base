---
collection: ansible
version: "6"
title: "ansible.windows.win_uri module – Interacts with webservices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/windows/win_uri_module.html
fetched_at: 2026-07-27T16:45:04+00:00
---
# ansible.windows.win_uri module – Interacts with webservices

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
> To use it in a playbook, specify: `ansible.windows.win_uri`.

- [Synopsis](win_uri_module.md#synopsis)
- [Parameters](win_uri_module.md#parameters)
- [See Also](win_uri_module.md#see-also)
- [Examples](win_uri_module.md#examples)
- [Return Values](win_uri_module.md#return-values)

## [Synopsis](win_uri_module.md#id1)

- Interacts with FTP, HTTP and HTTPS web services.
- Supports Digest, Basic and WSSE HTTP authentication mechanisms.
- For non-Windows targets, use the [ansible.builtin.uri](../builtin/uri_module.md#ansible-collections-ansible-builtin-uri-module) module instead.

## [Parameters](win_uri_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **body**  any | The body of the HTTP request/response to the web service. |
| **client_cert**  string | The path to the client certificate (.pfx) that is used for X509 authentication. This path can either be the path to the `pfx` on the filesystem or the PowerShell certificate path `Cert:\CurrentUser\My\<thumbprint>`.  The WinRM connection must be authenticated with `CredSSP` or `become` is used on the task if the certificate file is not password protected.  Other authentication types can set *client_cert_password* when the cert is password protected. |
| **client_cert_password**  string | The password for *client_cert* if the cert is password protected. |
| **content_type**  string | Sets the “Content-Type” header. |
| **creates**  path | A filename, when it already exists, this step will be skipped. |
| **dest**  path | Output the response body to a file. |
| **follow_redirects**  string | Whether or the module should follow redirects.  `all` will follow all redirect.  `none` will not follow any redirect.  `safe` will follow only “safe” redirects, where “safe” means that the client is only doing a `GET` or `HEAD` on the URI to which it is being redirected.  When following a redirected URL, the `Authorization` header and any credentials set will be dropped and not redirected.  Choices:   - `"all"` - `"none"` - `"safe"` ← (default) |
| **force_basic_auth**  boolean | By default the authentication header is only sent when a webservice responses to an initial request with a 401 status. Since some basic auth services do not properly send a 401, logins will fail.  This option forces the sending of the Basic authentication header upon the original request.  Choices:   - `false` ← (default) - `true` |
| **headers**  dictionary | Extra headers to set on the request.  This should be a dictionary where the key is the header name and the value is the value for that header. |
| **http_agent**  string | Header to identify as, generally appears in web server logs.  This is set to the `User-Agent` header on a HTTP request.  Default: `"ansible-httpget"` |
| **maximum_redirection**  integer | Specify how many times the module will redirect a connection to an alternative URI before the connection fails.  If set to `0` or *follow_redirects* is set to `none`, or `safe` when not doing a `GET` or `HEAD` it prevents all redirection.  Default: `50` |
| **proxy_password**  string | The password for *proxy_username*. |
| **proxy_url**  string | An explicit proxy to use for the request.  By default, the request will use the IE defined proxy unless *use_proxy* is set to `no`. |
| **proxy_use_default_credential**  boolean | Uses the current user’s credentials when authenticating with a proxy host protected with `NTLM`, `Kerberos`, or `Negotiate` authentication.  Proxies that use `Basic` auth will still require explicit credentials through the *proxy_username* and *proxy_password* options.  The module will only have access to the user’s credentials if using `become` with a password, you are connecting with SSH using a password, or connecting with WinRM using `CredSSP` or `Kerberos with delegation`.  If not using `become` or a different auth method to the ones stated above, there will be no default credentials available and no proxy authentication will occur.  Choices:   - `false` ← (default) - `true` |
| **proxy_username**  string | The username to use for proxy authentication. |
| **removes**  path | A filename, when it does not exist, this step will be skipped. |
| **return_content**  boolean | Whether or not to return the body of the response as a “content” key in the dictionary result. If the reported Content-type is “application/json”, then the JSON is additionally loaded into a key called `json` in the dictionary results.  Choices:   - `false` ← (default) - `true` |
| **status_code**  list / elements=integer | A valid, numeric, HTTP status code that signifies success of the request.  Can also be comma separated list of status codes.  Default: `[200]` |
| **url**  string / required | Supports FTP, HTTP or HTTPS URLs in the form of (ftp|http|https)://host.domain:port/path. |
| **url_method**  aliases: method  string | The HTTP Method of the request.  Default: `"GET"` |
| **url_password**  aliases: password  string | The password for *url_username*.  The alias *password* is deprecated and will be removed on the major release after `2022-07-01`. |
| **url_timeout**  aliases: timeout  integer | Specifies how long the request can be pending before it times out (in seconds).  Set to `0` to specify an infinite timeout.  Default: `30` |
| **url_username**  aliases: user, username  string | The username to use for authentication.  The alias *user* and *username* is deprecated and will be removed on the major release after `2022-07-01`. |
| **use_default_credential**  boolean | Uses the current user’s credentials when authenticating with a server protected with `NTLM`, `Kerberos`, or `Negotiate` authentication.  Sites that use `Basic` auth will still require explicit credentials through the *url_username* and *url_password* options.  The module will only have access to the user’s credentials if using `become` with a password, you are connecting with SSH using a password, or connecting with WinRM using `CredSSP` or `Kerberos with delegation`.  If not using `become` or a different auth method to the ones stated above, there will be no default credentials available and no authentication will occur.  Choices:   - `false` ← (default) - `true` |
| **use_proxy**  boolean | If `no`, it will not use the proxy defined in IE for the current user.  Choices:   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [See Also](win_uri_module.md#id3)

> **See also:**
>
> [ansible.builtin.uri](../builtin/uri_module.md#ansible-collections-ansible-builtin-uri-module)
> :   Interacts with webservices.
>
> [ansible.windows.win_get_url](win_get_url_module.md#ansible-collections-ansible-windows-win-get-url-module)
> :   Downloads file from HTTP, HTTPS, or FTP to node.
>
> [community.windows.win_inet_proxy](../../community/windows/win_inet_proxy_module.md#ansible-collections-community-windows-win-inet-proxy-module)
> :   Manages proxy settings for WinINet and Internet Explorer.

## [Examples](win_uri_module.md#id4)

```yaml+jinja
- name: Perform a GET and Store Output
  ansible.windows.win_uri:
    url: http://example.com/endpoint
  register: http_output

# Set a HOST header to hit an internal webserver:
- name: Hit a Specific Host on the Server
  ansible.windows.win_uri:
    url: http://example.com/
    method: GET
    headers:
      host: www.somesite.com

- name: Perform a HEAD on an Endpoint
  ansible.windows.win_uri:
    url: http://www.example.com/
    method: HEAD

- name: POST a Body to an Endpoint
  ansible.windows.win_uri:
    url: http://www.somesite.com/
    method: POST
    body: "{ 'some': 'json' }"
```

## [Return Values](win_uri_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **content**  string | The raw content of the HTTP response.  Returned: success and return_content is True  Sample: `"{\"foo\": \"bar\"}"` |
| **content_length**  integer | The byte size of the response.  Returned: success  Sample: `54447` |
| **elapsed**  float | The number of seconds that elapsed while performing the download.  Returned: always  Sample: `23.2` |
| **json**  dictionary | The json structure returned under content as a dictionary.  Returned: success and Content-Type is “application/json” or “application/javascript” and return_content is True  Sample: `{"this-is-dependent": "on the actual return content"}` |
| **status_code**  integer | The HTTP Status Code of the response.  Returned: success  Sample: `200` |
| **status_description**  string | A summary of the status.  Returned: success  Sample: `"OK"` |
| **url**  string | The Target URL.  Returned: always  Sample: `"https://www.ansible.com"` |

### Authors

- Corwin Brown (@blakfeld)
- Dag Wieers (@dagwieers)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
[Communication](index.md#communication-for-ansible-windows)
