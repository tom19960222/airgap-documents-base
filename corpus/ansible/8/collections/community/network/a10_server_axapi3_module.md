---
collection: ansible
version: "8"
title: "community.network.a10_server_axapi3 module – Manage A10 Networks AX/SoftAX/Thunder/vThunder devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/a10_server_axapi3_module.html
fetched_at: 2026-07-28T01:54:15+00:00
---
# community.network.a10_server_axapi3 module – Manage A10 Networks AX/SoftAX/Thunder/vThunder devices

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.a10_server_axapi3`.

- [Synopsis](a10_server_axapi3_module.md#synopsis)
- [Parameters](a10_server_axapi3_module.md#parameters)
- [Notes](a10_server_axapi3_module.md#notes)
- [Examples](a10_server_axapi3_module.md#examples)

## [Synopsis](a10_server_axapi3_module.md#id1)

- Manage SLB (Server Load Balancer) server objects on A10 Networks devices via aXAPIv3.

Aliases: network.a10.a10_server_axapi3

## [Parameters](a10_server_axapi3_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, `client_key` is not required. |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If `client_cert` contains both the certificate and key, this option is not required. |
| **force**  boolean | If `yes` do not get a cached copy.  **Choices:**   - `false` ← (default) - `true` |
| **force_basic_auth**  boolean | Credentials specified with *url_username* and *url_password* should be passed in HTTP Header.  **Choices:**   - `false` ← (default) - `true` |
| **host**  string / required | Hostname or IP of the A10 Networks device. |
| **http_agent**  string | Header to identify as, generally appears in web server logs.  **Default:** `"ansible-httpget"` |
| **operation**  string | Create, Update or Remove SLB server. For create and update operation, we use the IP address and server name specified in the POST message. For delete operation, we use the server name in the request URI.  **Choices:**   - `"create"` ← (default) - `"update"` - `"remove"` |
| **password**  aliases: pass, pwd  string / required | Password for the `username` account. |
| **server_ip**  aliases: ip, address  string / required | The SLB (Server Load Balancer) server IPv4 address. |
| **server_name**  aliases: server  string / required | The SLB (Server Load Balancer) server name. |
| **server_ports**  aliases: port  string | A list of ports to create for the server. Each list item should be a dictionary which specifies the `port:` and `protocol:`.  **Default:** `[]` |
| **server_status**  aliases: action  string | The SLB (Server Load Balancer) virtual server status.  **Choices:**   - `"enable"` ← (default) - `"disable"` |
| **url**  string | HTTP, HTTPS, or FTP URL in the form (http|https|ftp)://[user[:pass]]@host.domain[:port]/path |
| **url_password**  string | The password for use in HTTP basic authentication.  If the *url_username* parameter is not specified, the *url_password* parameter will not be used. |
| **url_username**  string | The username for use in HTTP basic authentication.  This parameter can be used without *url_password* for sites that allow empty passwords |
| **use_gssapi**  boolean  *added in ansible-core 2.11* | Use GSSAPI to perform the authentication, typically this is for Kerberos or Kerberos through Negotiate authentication.  Requires the Python library [gssapi](https://github.com/pythongssapi/python-gssapi) to be installed.  Credentials for GSSAPI can be specified with *url_username*/*url_password* or with the GSSAPI env var `KRB5CCNAME` that specified a custom Kerberos credential cache.  NTLM authentication is `not` supported even if the GSSAPI mech for NTLM has been installed.  **Choices:**   - `false` ← (default) - `true` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **username**  aliases: admin, user  string / required | An account with administrator privileges. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated. This should only be used on personally controlled devices using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **write_config**  boolean | If `yes`, any changes will cause a write of the running configuration to non-volatile memory. This will save *all* configuration changes, including those that may have been made manually or through other modules, so care should be taken when specifying `yes`.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](a10_server_axapi3_module.md#id3)

> **Note:**
>
> - Requires A10 Networks aXAPI 2.1.

## [Examples](a10_server_axapi3_module.md#id4)

```yaml+jinja
- name: Create a new server
  a10_server:
    host: a10.mydomain.com
    username: myadmin
    password: mypassword
    server: test
    server_ip: 1.1.1.100
    validate_certs: false
    server_status: enable
    write_config: true
    operation: create
    server_ports:
      - port-number: 8080
        protocol: tcp
        action: enable
      - port-number: 8443
        protocol: TCP
```

### Authors

- Eric Chou (@ericchou1)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
