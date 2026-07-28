---
collection: ansible
version: "8"
title: "community.network.a10_service_group module – Manage A10 Networks AX/SoftAX/Thunder/vThunder devices’ service groups."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/a10_service_group_module.html
fetched_at: 2026-07-28T01:54:15+00:00
---
# community.network.a10_service_group module – Manage A10 Networks AX/SoftAX/Thunder/vThunder devices’ service groups.

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
> To use it in a playbook, specify: `community.network.a10_service_group`.

- [Synopsis](a10_service_group_module.md#synopsis)
- [Parameters](a10_service_group_module.md#parameters)
- [Notes](a10_service_group_module.md#notes)
- [Examples](a10_service_group_module.md#examples)
- [Return Values](a10_service_group_module.md#return-values)

## [Synopsis](a10_service_group_module.md#id1)

- Manage SLB (Server Load Balancing) service-group objects on A10 Networks devices via aXAPIv2.

Aliases: network.a10.a10_service_group

## [Parameters](a10_service_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, `client_key` is not required. |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If `client_cert` contains both the certificate and key, this option is not required. |
| **force**  boolean | If `yes` do not get a cached copy.  **Choices:**   - `false` ← (default) - `true` |
| **force_basic_auth**  boolean | Credentials specified with *url_username* and *url_password* should be passed in HTTP Header.  **Choices:**   - `false` ← (default) - `true` |
| **host**  string / required | Hostname or IP of the A10 Networks device. |
| **http_agent**  string | Header to identify as, generally appears in web server logs.  **Default:** `"ansible-httpget"` |
| **partition**  string | set active-partition  **Default:** `[]` |
| **password**  aliases: pass, pwd  string / required | Password for the `username` account. |
| **servers**  aliases: server, member  string | A list of servers to add to the service group. Each list item should be a dictionary which specifies the `server:` and `port:`, but can also optionally specify the `status:`. See the examples below for details.  **Default:** `[]` |
| **service_group**  aliases: service, pool, group  string / required | The SLB (Server Load Balancing) service-group name |
| **service_group_method**  aliases: method  string | The SLB service-group load balancing method, such as round-robin or weighted-rr.  **Choices:**   - `"round-robin"` ← (default) - `"weighted-rr"` - `"least-connection"` - `"weighted-least-connection"` - `"service-least-connection"` - `"service-weighted-least-connection"` - `"fastest-response"` - `"least-request"` - `"round-robin-strict"` - `"src-ip-only-hash"` - `"src-ip-hash"` |
| **service_group_protocol**  aliases: proto, protocol  string | The SLB service-group protocol of TCP or UDP.  **Choices:**   - `"tcp"` ← (default) - `"udp"` |
| **state**  string | If the specified service group should exists.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **url**  string | HTTP, HTTPS, or FTP URL in the form (http|https|ftp)://[user[:pass]]@host.domain[:port]/path |
| **url_password**  string | The password for use in HTTP basic authentication.  If the *url_username* parameter is not specified, the *url_password* parameter will not be used. |
| **url_username**  string | The username for use in HTTP basic authentication.  This parameter can be used without *url_password* for sites that allow empty passwords |
| **use_gssapi**  boolean  *added in ansible-core 2.11* | Use GSSAPI to perform the authentication, typically this is for Kerberos or Kerberos through Negotiate authentication.  Requires the Python library [gssapi](https://github.com/pythongssapi/python-gssapi) to be installed.  Credentials for GSSAPI can be specified with *url_username*/*url_password* or with the GSSAPI env var `KRB5CCNAME` that specified a custom Kerberos credential cache.  NTLM authentication is `not` supported even if the GSSAPI mech for NTLM has been installed.  **Choices:**   - `false` ← (default) - `true` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **username**  aliases: admin, user  string / required | An account with administrator privileges. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated. This should only be used on personally controlled devices using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **write_config**  boolean | If `yes`, any changes will cause a write of the running configuration to non-volatile memory. This will save *all* configuration changes, including those that may have been made manually or through other modules, so care should be taken when specifying `yes`.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](a10_service_group_module.md#id3)

> **Note:**
>
> - Requires A10 Networks aXAPI 2.1.
> - When a server doesn’t exist and is added to the service-group the server will be created.
> - Requires A10 Networks aXAPI 2.1.

## [Examples](a10_service_group_module.md#id4)

```yaml+jinja
- name: Create a new service-group
  community.network.a10_service_group:
    host: a10.mydomain.com
    username: myadmin
    password: mypassword
    partition: mypartition
    service_group: sg-80-tcp
    servers:
      - server: foo1.mydomain.com
        port: 8080
      - server: foo2.mydomain.com
        port: 8080
      - server: foo3.mydomain.com
        port: 8080
      - server: foo4.mydomain.com
        port: 8080
        status: disabled
```

## [Return Values](a10_service_group_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **content**  string | the full info regarding the slb_service_group  **Returned:** success  **Sample:** `"mynewservicegroup"` |

### Authors

- Eric Chou (@ericchou1)
- Mischa Peters (@mischapeters)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
