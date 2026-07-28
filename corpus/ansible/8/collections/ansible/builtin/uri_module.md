---
collection: ansible
version: "8"
title: "ansible.builtin.uri module – Interacts with webservices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/uri_module.html
fetched_at: 2026-07-28T01:07:47+00:00
---
# ansible.builtin.uri module – Interacts with webservices

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `uri` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.uri` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](uri_module.md#synopsis)
- [Parameters](uri_module.md#parameters)
- [Attributes](uri_module.md#attributes)
- [Notes](uri_module.md#notes)
- [See Also](uri_module.md#see-also)
- [Examples](uri_module.md#examples)
- [Return Values](uri_module.md#return-values)

## [Synopsis](uri_module.md#id1)

- Interacts with HTTP and HTTPS web services and supports Digest, Basic and WSSE HTTP authentication mechanisms.
- For Windows targets, use the [ansible.windows.win_uri](../windows/win_uri_module.md#ansible-collections-ansible-windows-win-uri-module) module instead.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](uri_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **body**  any | The body of the http request/response to the web service. If `body_format` is set to ‘json’ it will take an already formatted JSON string or convert a data structure into JSON.  If `body_format` is set to ‘form-urlencoded’ it will convert a dictionary or list of tuples into an ‘application/x-www-form-urlencoded’ string. (Added in v2.7)  If `body_format` is set to ‘form-multipart’ it will convert a dictionary into ‘multipart/form-multipart’ body. (Added in v2.10) |
| **body_format**  string | The serialization format of the body. When set to `json`, `form-multipart`, or `form-urlencoded`, encodes the body argument, if needed, and automatically sets the Content-Type header accordingly.  As of v2.3 it is possible to override the `Content-Type` header, when set to `json` or `form-urlencoded` via the *headers* option.  The ‘Content-Type’ header cannot be overridden when using `form-multipart`  `form-urlencoded` was added in v2.7.  `form-multipart` was added in v2.10.  **Choices:**   - `"form-urlencoded"` - `"json"` - `"raw"` ← (default) - `"form-multipart"` |
| **ca_path**  path  *added in ansible-core 2.11* | PEM formatted file that contains a CA certificate to be used for validation |
| **ciphers**  list / elements=string  *added in ansible-core 2.14* | SSL/TLS Ciphers to use for the request.  When a list is provided, all ciphers are joined in order with `:`  See the [OpenSSL Cipher List Format](https://www.openssl.org/docs/manmaster/man1/openssl-ciphers.html#CIPHER-LIST-FORMAT) for more details.  The available ciphers is dependent on the Python and OpenSSL/LibreSSL versions |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, *client_key* is not required |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If *client_cert* contains both the certificate and key, this option is not required. |
| **creates**  path | A filename, when it already exists, this step will not be run. |
| **decompress**  boolean  *added in ansible-core 2.14* | Whether to attempt to decompress gzip content-encoded responses  **Choices:**   - `false` - `true` ← (default) |
| **dest**  path | A path of where to download the file to (if desired). If *dest* is a directory, the basename of the file on the remote server will be used. |
| **follow_redirects**  string | Whether or not the URI module should follow redirects. `all` will follow all redirects. `safe` will follow only “safe” redirects, where “safe” means that the client is only doing a GET or HEAD on the URI to which it is being redirected. `none` will not follow any redirects. Note that `true` and `false` choices are accepted for backwards compatibility, where `true` is the equivalent of `all` and `false` is the equivalent of `safe`. `true` and `false` are deprecated and will be removed in some future version of Ansible.  **Choices:**   - `"all"` - `"no"` - `"none"` - `"safe"` ← (default) - `"urllib2"` - `"yes"` |
| **force**  boolean | If `true` do not get a cached copy.  **Choices:**   - `false` ← (default) - `true` |
| **force_basic_auth**  boolean | Force the sending of the Basic authentication header upon initial request.  When this setting is `false`, this module will first try an unauthenticated request, and when the server replies with an `HTTP 401` error, it will submit the Basic authentication header.  When this setting is `true`, this module will immediately send a Basic authentication header on the first request.  Use this setting in any of the following scenarios:  You know the webservice endpoint always requires HTTP Basic authentication, and you want to speed up your requests by eliminating the first roundtrip.  The web service does not properly send an HTTP 401 error to your client, so Ansible’s HTTP library will not properly respond with HTTP credentials, and logins will fail.  The webservice bans or rate-limits clients that cause any HTTP 401 errors.  **Choices:**   - `false` ← (default) - `true` |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **headers**  dictionary | Add custom HTTP headers to a request in the format of a YAML hash. As of `2.3` supplying `Content-Type` here will override the header generated by supplying `json` or `form-urlencoded` for *body_format*.  **Default:** `{}` |
| **http_agent**  string | Header to identify as, generally appears in web server logs.  **Default:** `"ansible-httpget"` |
| **method**  string | The HTTP method of the request or response.  In more recent versions we do not restrict the method at the module level anymore but it still must be a valid method accepted by the service handling the request.  **Default:** `"GET"` |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must give Ansible enough information to parse them correctly. For consistent results, quote octal numbers (for example, `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number. Adding a leading zero (for example, `0755`) works sometimes, but can fail in loops and some other circumstances.  Giving Ansible a number without following either of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership.  Specifying a numeric username will be assumed to be a user ID and not a username. Avoid numeric usernames to avoid this confusion. |
| **remote_src**  boolean  *added in Ansible 2.7* | If `false`, the module will search for the `src` on the controller node.  If `true`, the module will search for the `src` on the managed (remote) node.  **Choices:**   - `false` ← (default) - `true` |
| **removes**  path | A filename, when it does not exist, this step will not be run. |
| **return_content**  boolean | Whether or not to return the body of the response as a “content” key in the dictionary result no matter it succeeded or failed.  Independently of this option, if the reported Content-type is “application/json”, then the JSON is always loaded into a key called `json` in the dictionary results.  **Choices:**   - `false` ← (default) - `true` |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **src**  path  *added in Ansible 2.7* | Path to file to be submitted to the remote server.  Cannot be used with *body*.  Should be used with *force_basic_auth* to ensure success when the remote end sends a 401. |
| **status_code**  list / elements=integer | A list of valid, numeric, HTTP status codes that signifies success of the request.  **Default:** `[200]` |
| **timeout**  integer | The socket level timeout in seconds  **Default:** `30` |
| **unix_socket**  path  *added in Ansible 2.8* | Path to Unix domain socket to use for connection |
| **unredirected_headers**  list / elements=string  *added in ansible-core 2.12* | A list of header names that will not be sent on subsequent redirected requests. This list is case insensitive. By default all headers will be redirected. In some cases it may be beneficial to list headers such as `Authorization` here to avoid potential credential exposure.  **Default:** `[]` |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  **Choices:**   - `false` ← (default) - `true` |
| **url**  string / required | HTTP or HTTPS URL in the form (http|https)://host.domain[:port]/path |
| **url_password**  aliases: password  string | A password for the module to use for Digest, Basic or WSSE authentication. |
| **url_username**  aliases: user  string | A username for the module to use for Digest, Basic or WSSE authentication. |
| **use_gssapi**  boolean  *added in ansible-core 2.11* | Use GSSAPI to perform the authentication, typically this is for Kerberos or Kerberos through Negotiate authentication.  Requires the Python library [gssapi](https://github.com/pythongssapi/python-gssapi) to be installed.  Credentials for GSSAPI can be specified with *url_username*/*url_password* or with the GSSAPI env var `KRB5CCNAME` that specified a custom Kerberos credential cache.  NTLM authentication is `not` supported even if the GSSAPI mech for NTLM has been installed.  **Choices:**   - `false` ← (default) - `true` |
| **use_netrc**  boolean  *added in ansible-core 2.14* | Determining whether to use credentials from ``~/.netrc`` file  By default .netrc is used with Basic authentication headers  When set to False, .netrc credentials are ignored  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `false`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only set to `false` used on personally controlled sites using self-signed certificates.  Prior to 1.9.2 the code defaulted to `false`.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](uri_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **posix** | Target OS/families that can be operated against |

## [Notes](uri_module.md#id4)

> **Note:**
>
> - The dependency on httplib2 was removed in Ansible 2.1.
> - The module returns all the HTTP headers in lower-case.
> - For Windows targets, use the [ansible.windows.win_uri](../windows/win_uri_module.md#ansible-collections-ansible-windows-win-uri-module) module instead.

## [See Also](uri_module.md#id5)

> **See also:**
>
> [ansible.builtin.get_url](get_url_module.md#ansible-collections-ansible-builtin-get-url-module)
> :   Downloads files from HTTP, HTTPS, or FTP to node.
>
> [ansible.windows.win_uri](../windows/win_uri_module.md#ansible-collections-ansible-windows-win-uri-module)
> :   Interacts with webservices.

## [Examples](uri_module.md#id6)

```yaml+jinja
- name: Check that you can connect (GET) to a page and it returns a status 200
  ansible.builtin.uri:
    url: http://www.example.com

- name: Check that a page returns successfully but fail if the word AWESOME is not in the page contents
  ansible.builtin.uri:
    url: http://www.example.com
    return_content: true
  register: this
  failed_when: this is failed or "'AWESOME' not in this.content"

- name: Create a JIRA issue
  ansible.builtin.uri:
    url: https://your.jira.example.com/rest/api/2/issue/
    user: your_username
    password: your_pass
    method: POST
    body: "{{ lookup('ansible.builtin.file','issue.json') }}"
    force_basic_auth: true
    status_code: 201
    body_format: json

- name: Login to a form based webpage, then use the returned cookie to access the app in later tasks
  ansible.builtin.uri:
    url: https://your.form.based.auth.example.com/index.php
    method: POST
    body_format: form-urlencoded
    body:
      name: your_username
      password: your_password
      enter: Sign in
    status_code: 302
  register: login

- name: Login to a form based webpage using a list of tuples
  ansible.builtin.uri:
    url: https://your.form.based.auth.example.com/index.php
    method: POST
    body_format: form-urlencoded
    body:
    - [ name, your_username ]
    - [ password, your_password ]
    - [ enter, Sign in ]
    status_code: 302
  register: login

- name: Upload a file via multipart/form-multipart
  ansible.builtin.uri:
    url: https://httpbin.org/post
    method: POST
    body_format: form-multipart
    body:
      file1:
        filename: /bin/true
        mime_type: application/octet-stream
      file2:
        content: text based file content
        filename: fake.txt
        mime_type: text/plain
      text_form_field: value

- name: Connect to website using a previously stored cookie
  ansible.builtin.uri:
    url: https://your.form.based.auth.example.com/dashboard.php
    method: GET
    return_content: true
    headers:
      Cookie: "{{ login.cookies_string }}"

- name: Queue build of a project in Jenkins
  ansible.builtin.uri:
    url: http://{{ jenkins.host }}/job/{{ jenkins.job }}/build?token={{ jenkins.token }}
    user: "{{ jenkins.user }}"
    password: "{{ jenkins.password }}"
    method: GET
    force_basic_auth: true
    status_code: 201

- name: POST from contents of local file
  ansible.builtin.uri:
    url: https://httpbin.org/post
    method: POST
    src: file.json

- name: POST from contents of remote file
  ansible.builtin.uri:
    url: https://httpbin.org/post
    method: POST
    src: /path/to/my/file.json
    remote_src: true

- name: Create workspaces in Log analytics Azure
  ansible.builtin.uri:
    url: https://www.mms.microsoft.com/Embedded/Api/ConfigDataSources/LogManagementData/Save
    method: POST
    body_format: json
    status_code: [200, 202]
    return_content: true
    headers:
      Content-Type: application/json
      x-ms-client-workspace-path: /subscriptions/{{ sub_id }}/resourcegroups/{{ res_group }}/providers/microsoft.operationalinsights/workspaces/{{ w_spaces }}
      x-ms-client-platform: ibiza
      x-ms-client-auth-token: "{{ token_az }}"
    body:

- name: Pause play until a URL is reachable from this host
  ansible.builtin.uri:
    url: "http://192.0.2.1/some/test"
    follow_redirects: none
    method: GET
  register: _result
  until: _result.status == 200
  retries: 720 # 720 * 5 seconds = 1hour (60*60/5)
  delay: 5 # Every 5 seconds

- name: Provide SSL/TLS ciphers as a list
  uri:
    url: https://example.org
    ciphers:
      - '@SECLEVEL=2'
      - ECDH+AESGCM
      - ECDH+CHACHA20
      - ECDH+AES
      - DHE+AES
      - '!aNULL'
      - '!eNULL'
      - '!aDSS'
      - '!SHA1'
      - '!AESCCM'

- name: Provide SSL/TLS ciphers as an OpenSSL formatted cipher list
  uri:
    url: https://example.org
    ciphers: '@SECLEVEL=2:ECDH+AESGCM:ECDH+CHACHA20:ECDH+AES:DHE+AES:!aNULL:!eNULL:!aDSS:!SHA1:!AESCCM'
```

## [Return Values](uri_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **content**  string | The response body content.  **Returned:** status not in status_code or return_content is true  **Sample:** `"{}"` |
| **cookies**  dictionary | The cookie values placed in cookie jar.  **Returned:** on success  **Sample:** `{"SESSIONID": "[SESSIONID]"}` |
| **cookies_string**  string | The value for future request Cookie headers.  **Returned:** on success  **Sample:** `"SESSIONID=[SESSIONID]"` |
| **elapsed**  integer | The number of seconds that elapsed while performing the download.  **Returned:** on success  **Sample:** `23` |
| **msg**  string | The HTTP message from the request.  **Returned:** always  **Sample:** `"OK (unknown bytes)"` |
| **path**  string | destination file/path  **Returned:** dest is defined  **Sample:** `"/path/to/file.txt"` |
| **redirected**  boolean | Whether the request was redirected.  **Returned:** on success  **Sample:** `false` |
| **status**  integer | The HTTP status code from the request.  **Returned:** always  **Sample:** `200` |
| **url**  string | The actual URL used for the request.  **Returned:** always  **Sample:** `"https://www.ansible.com/"` |

### Authors

- Romeo Theriault (@romeotheriault)

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
