---
collection: ansible
version: "8"
title: "ansible.builtin.get_url module – Downloads files from HTTP, HTTPS, or FTP to node"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/get_url_module.html
fetched_at: 2026-07-28T01:07:30+00:00
---
# ansible.builtin.get_url module – Downloads files from HTTP, HTTPS, or FTP to node

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `get_url` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.get_url` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](get_url_module.md#synopsis)
- [Parameters](get_url_module.md#parameters)
- [Attributes](get_url_module.md#attributes)
- [Notes](get_url_module.md#notes)
- [See Also](get_url_module.md#see-also)
- [Examples](get_url_module.md#examples)
- [Return Values](get_url_module.md#return-values)

## [Synopsis](get_url_module.md#id1)

- Downloads files from HTTP, HTTPS, or FTP to the remote server. The remote server *must* have direct access to the remote resource.
- By default, if an environment variable `<protocol>_proxy` is set on the target host, requests will be sent through that proxy. This behaviour can be overridden by setting a variable for this task (see [setting the environment](../../../playbook_guide/playbooks_environment.md#playbooks-environment)), or by using the use_proxy option.
- HTTP redirects can redirect from HTTP to HTTPS so you should be sure that your proxy environment for both protocols is correct.
- From Ansible 2.4 when run with `--check`, it will do a HEAD request to validate the URL but will not download the entire file or verify it against hashes and will report incorrect changed status.
- For Windows targets, use the [ansible.windows.win_get_url](../windows/win_get_url_module.md#ansible-collections-ansible-windows-win-get-url-module) module instead.

## [Parameters](get_url_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **backup**  boolean | Create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.  **Choices:**   - `false` ← (default) - `true` |
| **checksum**  string | If a checksum is passed to this parameter, the digest of the destination file will be calculated after it is downloaded to ensure its integrity and verify that the transfer completed successfully. Format: <algorithm>:<checksum|url>, e.g. checksum=”sha256:D98291AC[…]B6DC7B97”, checksum=”sha256:http://example.com/path/sha256sum.txt”  If you worry about portability, only the sha1 algorithm is available on all platforms and python versions.  The Python ``hashlib`` module is responsible for providing the available algorithms. The choices vary based on Python version and OpenSSL version.  On systems running in FIPS compliant mode, the ``md5`` algorithm may be unavailable.  Additionally, if a checksum is passed to this parameter, and the file exist under the `dest` location, the *destination_checksum* would be calculated, and if checksum equals *destination_checksum*, the file download would be skipped (unless `force` is true). If the checksum does not equal *destination_checksum*, the destination file is deleted.  **Default:** `""` |
| **ciphers**  list / elements=string  *added in ansible-core 2.14* | SSL/TLS Ciphers to use for the request  When a list is provided, all ciphers are joined in order with `:`  See the [OpenSSL Cipher List Format](https://www.openssl.org/docs/manmaster/man1/openssl-ciphers.html#CIPHER-LIST-FORMAT) for more details.  The available ciphers is dependent on the Python and OpenSSL/LibreSSL versions |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, `client_key` is not required. |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If `client_cert` contains both the certificate and key, this option is not required. |
| **decompress**  boolean  *added in ansible-core 2.14* | Whether to attempt to decompress gzip content-encoded responses  **Choices:**   - `false` - `true` ← (default) |
| **dest**  path / required | Absolute path of where to download the file to.  If `dest` is a directory, either the server provided filename or, if none provided, the base name of the URL on the remote server will be used. If a directory, `force` has no effect.  If `dest` is a directory, the file will always be downloaded (regardless of the `force` and `checksum` option), but replaced only if the contents changed. |
| **force**  boolean | If `true` and `dest` is not a directory, will download the file every time and replace the file if the contents change. If `false`, the file will only be downloaded if the destination does not exist. Generally should be `true` only for small local files.  Prior to 0.6, this module behaved as if `true` was the default.  **Choices:**   - `false` ← (default) - `true` |
| **force_basic_auth**  boolean | Force the sending of the Basic authentication header upon initial request.  httplib2, the library used by the uri module only sends authentication information when a webservice responds to an initial request with a 401 status. Since some basic auth services do not properly send a 401, logins will fail.  **Choices:**   - `false` ← (default) - `true` |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **headers**  dictionary | Add custom HTTP headers to a request in hash/dict format.  The hash/dict format was added in Ansible 2.6.  Previous versions used a `"key:value,key:value"` string format.  The `"key:value,key:value"` string format is deprecated and has been removed in version 2.10. |
| **http_agent**  string | Header to identify as, generally appears in web server logs.  **Default:** `"ansible-httpget"` |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must give Ansible enough information to parse them correctly. For consistent results, quote octal numbers (for example, `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number. Adding a leading zero (for example, `0755`) works sometimes, but can fail in loops and some other circumstances.  Giving Ansible a number without following either of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership.  Specifying a numeric username will be assumed to be a user ID and not a username. Avoid numeric usernames to avoid this confusion. |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **timeout**  integer | Timeout in seconds for URL request.  **Default:** `10` |
| **tmp_dest**  path | Absolute path of where temporary file is downloaded to.  When run on Ansible 2.5 or greater, path defaults to ansible’s remote_tmp setting  When run on Ansible prior to 2.5, it defaults to `TMPDIR`, `TEMP` or `TMP` env variables or a platform specific value.  <https://docs.python.org/3/library/tempfile.html#tempfile.tempdir> |
| **unredirected_headers**  list / elements=string  *added in ansible-core 2.12* | A list of header names that will not be sent on subsequent redirected requests. This list is case insensitive. By default all headers will be redirected. In some cases it may be beneficial to list headers such as `Authorization` here to avoid potential credential exposure.  **Default:** `[]` |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  **Choices:**   - `false` ← (default) - `true` |
| **url**  string / required | HTTP, HTTPS, or FTP URL in the form (http|https|ftp)://[user[:pass]]@host.domain[:port]/path |
| **url_password**  aliases: password  string | The password for use in HTTP basic authentication.  If the `url_username` parameter is not specified, the `url_password` parameter will not be used.  Since version 2.8 you can also use the ‘password’ alias for this option. |
| **url_username**  aliases: username  string | The username for use in HTTP basic authentication.  This parameter can be used without `url_password` for sites that allow empty passwords.  Since version 2.8 you can also use the `username` alias for this option. |
| **use_gssapi**  boolean  *added in ansible-core 2.11* | Use GSSAPI to perform the authentication, typically this is for Kerberos or Kerberos through Negotiate authentication.  Requires the Python library [gssapi](https://github.com/pythongssapi/python-gssapi) to be installed.  Credentials for GSSAPI can be specified with *url_username*/*url_password* or with the GSSAPI env var `KRB5CCNAME` that specified a custom Kerberos credential cache.  NTLM authentication is *not* supported even if the GSSAPI mech for NTLM has been installed.  **Choices:**   - `false` ← (default) - `true` |
| **use_netrc**  boolean  *added in ansible-core 2.14* | Determining whether to use credentials from ``~/.netrc`` file  By default .netrc is used with Basic authentication headers  When set to False, .netrc credentials are ignored  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | if `false`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](get_url_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **partial**  the changed status will reflect comparison to an empty source file | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **posix** | Target OS/families that can be operated against |

## [Notes](get_url_module.md#id4)

> **Note:**
>
> - For Windows targets, use the [ansible.windows.win_get_url](../windows/win_get_url_module.md#ansible-collections-ansible-windows-win-get-url-module) module instead.

## [See Also](get_url_module.md#id5)

> **See also:**
>
> [ansible.builtin.uri](uri_module.md#ansible-collections-ansible-builtin-uri-module)
> :   Interacts with webservices.
>
> [ansible.windows.win_get_url](../windows/win_get_url_module.md#ansible-collections-ansible-windows-win-get-url-module)
> :   Downloads file from HTTP, HTTPS, or FTP to node.

## [Examples](get_url_module.md#id6)

```yaml+jinja
- name: Download foo.conf
  ansible.builtin.get_url:
    url: http://example.com/path/file.conf
    dest: /etc/foo.conf
    mode: '0440'

- name: Download file and force basic auth
  ansible.builtin.get_url:
    url: http://example.com/path/file.conf
    dest: /etc/foo.conf
    force_basic_auth: yes

- name: Download file with custom HTTP headers
  ansible.builtin.get_url:
    url: http://example.com/path/file.conf
    dest: /etc/foo.conf
    headers:
      key1: one
      key2: two

- name: Download file with check (sha256)
  ansible.builtin.get_url:
    url: http://example.com/path/file.conf
    dest: /etc/foo.conf
    checksum: sha256:b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b878ae4944c

- name: Download file with check (md5)
  ansible.builtin.get_url:
    url: http://example.com/path/file.conf
    dest: /etc/foo.conf
    checksum: md5:66dffb5228a211e61d6d7ef4a86f5758

- name: Download file with checksum url (sha256)
  ansible.builtin.get_url:
    url: http://example.com/path/file.conf
    dest: /etc/foo.conf
    checksum: sha256:http://example.com/path/sha256sum.txt

- name: Download file from a file path
  ansible.builtin.get_url:
    url: file:///tmp/afile.txt
    dest: /tmp/afilecopy.txt

- name: < Fetch file that requires authentication.
        username/password only available since 2.8, in older versions you need to use url_username/url_password
  ansible.builtin.get_url:
    url: http://example.com/path/file.conf
    dest: /etc/foo.conf
    username: bar
    password: '{{ mysecret }}'
```

## [Return Values](get_url_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_file**  string | name of backup file created after download  **Returned:** changed and if backup=yes  **Sample:** `"/path/to/file.txt.2015-02-12@22:09~"` |
| **checksum_dest**  string | sha1 checksum of the file after copy  **Returned:** success  **Sample:** `"6e642bb8dd5c2e027bf21dd923337cbb4214f827"` |
| **checksum_src**  string | sha1 checksum of the file  **Returned:** success  **Sample:** `"6e642bb8dd5c2e027bf21dd923337cbb4214f827"` |
| **dest**  string | destination file/path  **Returned:** success  **Sample:** `"/path/to/file.txt"` |
| **elapsed**  integer | The number of seconds that elapsed while performing the download  **Returned:** always  **Sample:** `23` |
| **gid**  integer | group id of the file  **Returned:** success  **Sample:** `100` |
| **group**  string | group of the file  **Returned:** success  **Sample:** `"httpd"` |
| **md5sum**  string | md5 checksum of the file after download  **Returned:** when supported  **Sample:** `"2a5aeecc61dc98c4d780b14b330e3282"` |
| **mode**  string | permissions of the target  **Returned:** success  **Sample:** `"0644"` |
| **msg**  string | the HTTP message from the request  **Returned:** always  **Sample:** `"OK (unknown bytes)"` |
| **owner**  string | owner of the file  **Returned:** success  **Sample:** `"httpd"` |
| **secontext**  string | the SELinux security context of the file  **Returned:** success  **Sample:** `"unconfined_u:object_r:user_tmp_t:s0"` |
| **size**  integer | size of the target  **Returned:** success  **Sample:** `1220` |
| **src**  string | source file used after download  **Returned:** always  **Sample:** `"/tmp/tmpAdFLdV"` |
| **state**  string | state of the target  **Returned:** success  **Sample:** `"file"` |
| **status_code**  integer | the HTTP status code from the request  **Returned:** always  **Sample:** `200` |
| **uid**  integer | owner id of the file, after execution  **Returned:** success  **Sample:** `100` |
| **url**  string | the actual URL used for the request  **Returned:** always  **Sample:** `"https://www.ansible.com/"` |

### Authors

- Jan-Piet Mens (@jpmens)

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
