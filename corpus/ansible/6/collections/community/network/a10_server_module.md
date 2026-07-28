---
collection: ansible
version: "6"
title: "community.network.a10_server module – Manage A10 Networks AX/SoftAX/Thunder/vThunder devices’ server object."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/a10_server_module.html
fetched_at: 2026-07-27T17:16:20+00:00
---
# community.network.a10_server module – Manage A10 Networks AX/SoftAX/Thunder/vThunder devices’ server object.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.a10_server`.

- [Synopsis](a10_server_module.md#synopsis)
- [Parameters](a10_server_module.md#parameters)
- [Notes](a10_server_module.md#notes)
- [Examples](a10_server_module.md#examples)
- [Return Values](a10_server_module.md#return-values)

## [Synopsis](a10_server_module.md#id1)

- Manage SLB (Server Load Balancer) server objects on A10 Networks devices via aXAPIv2.

## [Parameters](a10_server_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, `client_key` is not required. |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If `client_cert` contains both the certificate and key, this option is not required. |
| **force**  boolean | If `yes` do not get a cached copy.  Choices:   - `false` ← (default) - `true` |
| **force_basic_auth**  boolean | Credentials specified with *url_username* and *url_password* should be passed in HTTP Header.  Choices:   - `false` ← (default) - `true` |
| **host**  string / required | Hostname or IP of the A10 Networks device. |
| **http_agent**  string | Header to identify as, generally appears in web server logs.  Default: `"ansible-httpget"` |
| **partition**  string | set active-partition  Default: `[]` |
| **password**  aliases: pass, pwd  string / required | Password for the `username` account. |
| **server_ip**  aliases: ip, address  string | The SLB server IPv4 address. |
| **server_name**  aliases: server  string / required | The SLB (Server Load Balancer) server name. |
| **server_ports**  aliases: port  string | A list of ports to create for the server. Each list item should be a dictionary which specifies the `port:` and `protocol:`, but can also optionally specify the `status:`. See the examples below for details. This parameter is required when `state` is `present`.  Default: `[]` |
| **server_status**  aliases: status  string | The SLB virtual server status.  Choices:   - `"enabled"` ← (default) - `"disabled"` |
| **state**  string | This is to specify the operation to create, update or remove SLB server.  Choices:   - `"present"` ← (default) - `"absent"` |
| **url**  string | HTTP, HTTPS, or FTP URL in the form (http|https|ftp)://[user[:pass]]@host.domain[:port]/path |
| **url_password**  string | The password for use in HTTP basic authentication.  If the *url_username* parameter is not specified, the *url_password* parameter will not be used. |
| **url_username**  string | The username for use in HTTP basic authentication.  This parameter can be used without *url_password* for sites that allow empty passwords |
| **use_gssapi**  boolean  added in ansible-core 2.11 | Use GSSAPI to perform the authentication, typically this is for Kerberos or Kerberos through Negotiate authentication.  Requires the Python library [gssapi](https://github.com/pythongssapi/python-gssapi) to be installed.  Credentials for GSSAPI can be specified with *url_username*/*url_password* or with the GSSAPI env var `KRB5CCNAME` that specified a custom Kerberos credential cache.  NTLM authentication is `not` supported even if the GSSAPI mech for NTLM has been installed.  Choices:   - `false` ← (default) - `true` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` - `true` ← (default) |
| **username**  aliases: admin, user  string / required | An account with administrator privileges. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated. This should only be used on personally controlled devices using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **write_config**  boolean | If `yes`, any changes will cause a write of the running configuration to non-volatile memory. This will save *all* configuration changes, including those that may have been made manually or through other modules, so care should be taken when specifying `yes`.  Choices:   - `false` ← (default) - `true` |

## [Notes](a10_server_module.md#id3)

> **Note:**
>
> - Requires A10 Networks aXAPI 2.1.
> - Requires A10 Networks aXAPI 2.1.

## [Examples](a10_server_module.md#id4)

```yaml+jinja
- name: Create a new server
  community.network.a10_server:
    host: a10.mydomain.com
    username: myadmin
    password: mypassword
    partition: mypartition
    server: test
    server_ip: 1.1.1.100
    server_ports:
      - port_num: 8080
        protocol: tcp
      - port_num: 8443
        protocol: TCP
```

## [Return Values](a10_server_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **content**  string | the full info regarding the slb_server  Returned: success  Sample: `"mynewserver"` |

### Authors

- Eric Chou (@ericchou1)
- Mischa Peters (@mischapeters)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
