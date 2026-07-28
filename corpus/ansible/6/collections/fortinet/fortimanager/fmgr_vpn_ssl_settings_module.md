---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_vpn_ssl_settings module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_vpn_ssl_settings_module.html
fetched_at: 2026-07-27T17:38:29+00:00
---
# fortinet.fortimanager.fmgr_vpn_ssl_settings module – no description

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/fortinet/fortimanager) (version 2.1.7).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_vpn_ssl_settings`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_vpn_ssl_settings_module.md#synopsis)
- [Parameters](fmgr_vpn_ssl_settings_module.md#parameters)
- [Notes](fmgr_vpn_ssl_settings_module.md#notes)
- [Examples](fmgr_vpn_ssl_settings_module.md#examples)
- [Return Values](fmgr_vpn_ssl_settings_module.md#return-values)

## [Synopsis](fmgr_vpn_ssl_settings_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_vpn_ssl_settings_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **device**  string / required | the parameter (device) in requested url |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **vdom**  string / required | the parameter (vdom) in requested url |
| **vpn_ssl_settings**  dictionary | the top level parameters set |
| **algorithm**  string | no description  Choices:   - `"default"` - `"high"` - `"low"` - `"medium"` |
| **auth-session-check-source-ip**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **auth-timeout**  integer | no description |
| **authentication-rule**  list / elements=string | description |
| **auth**  string | no description  Choices:   - `"any"` - `"local"` - `"radius"` - `"ldap"` - `"tacacs+"` |
| **cipher**  string | no description  Choices:   - `"any"` - `"high"` - `"medium"` |
| **client-cert**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **groups**  string | no description |
| **id**  integer | no description |
| **portal**  string | no description |
| **realm**  string | no description |
| **source-address**  string | no description |
| **source-address-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **source-address6**  string | no description |
| **source-address6-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **source-interface**  string | no description |
| **user-peer**  string | no description |
| **users**  string | no description |
| **auto-tunnel-static-route**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **banned-cipher**  list / elements=string | description  Choices:   - `"RSA"` - `"DH"` - `"DHE"` - `"ECDH"` - `"ECDHE"` - `"DSS"` - `"ECDSA"` - `"AES"` - `"AESGCM"` - `"CAMELLIA"` - `"3DES"` - `"SHA1"` - `"SHA256"` - `"SHA384"` - `"STATIC"` |
| **check-referer**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **default-portal**  string | no description |
| **deflate-compression-level**  integer | no description |
| **deflate-min-data-size**  integer | no description |
| **dns-server1**  string | no description |
| **dns-server2**  string | no description |
| **dns-suffix**  string | no description |
| **dtls-hello-timeout**  integer | no description |
| **dtls-max-proto-ver**  string | no description  Choices:   - `"dtls1-0"` - `"dtls1-2"` |
| **dtls-min-proto-ver**  string | no description  Choices:   - `"dtls1-0"` - `"dtls1-2"` |
| **dtls-tunnel**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **encode-2f-sequence**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **encrypt-and-store-password**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **force-two-factor-auth**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **header-x-forwarded-for**  string | no description  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **hsts-include-subdomains**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **http-compression**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **http-only-cookie**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **http-request-body-timeout**  integer | no description |
| **http-request-header-timeout**  integer | no description |
| **https-redirect**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **idle-timeout**  integer | no description |
| **ipv6-dns-server1**  string | no description |
| **ipv6-dns-server2**  string | no description |
| **ipv6-wins-server1**  string | no description |
| **ipv6-wins-server2**  string | no description |
| **login-attempt-limit**  integer | no description |
| **login-block-time**  integer | no description |
| **login-timeout**  integer | no description |
| **port**  integer | no description |
| **port-precedence**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **reqclientcert**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **route-source-interface**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **servercert**  string | no description |
| **source-address**  string | no description |
| **source-address-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **source-address6**  string | no description |
| **source-address6-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **source-interface**  string | no description |
| **ssl-client-renegotiation**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-insert-empty-fragment**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-max-proto-ver**  string | no description  Choices:   - `"tls1-0"` - `"tls1-1"` - `"tls1-2"` - `"tls1-3"` |
| **ssl-min-proto-ver**  string | no description  Choices:   - `"tls1-0"` - `"tls1-1"` - `"tls1-2"` - `"tls1-3"` |
| **tlsv1-0**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **tlsv1-1**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **tlsv1-2**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **tlsv1-3**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **transform-backward-slashes**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **tunnel-connect-without-reauth**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **tunnel-ip-pools**  string | no description |
| **tunnel-ipv6-pools**  string | no description |
| **tunnel-user-session-timeout**  integer | no description |
| **unsafe-legacy-renegotiation**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **url-obscuration**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **user-peer**  string | no description |
| **wins-server1**  string | no description |
| **wins-server2**  string | no description |
| **x-content-type-options**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_vpn_ssl_settings_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_vpn_ssl_settings_module.md#id4)

```yaml+jinja
- hosts: fortimanager-inventory
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: no description
     fmgr_vpn_ssl_settings:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        device: <your own value>
        vdom: <your own value>
        vpn_ssl_settings:
           algorithm: <value in [default, high, low, ...]>
           auth-session-check-source-ip: <value in [disable, enable]>
           auth-timeout: <value of integer>
           authentication-rule:
             -
                 auth: <value in [any, local, radius, ...]>
                 cipher: <value in [any, high, medium]>
                 client-cert: <value in [disable, enable]>
                 groups: <value of string>
                 id: <value of integer>
                 portal: <value of string>
                 realm: <value of string>
                 source-address: <value of string>
                 source-address-negate: <value in [disable, enable]>
                 source-address6: <value of string>
                 source-address6-negate: <value in [disable, enable]>
                 source-interface: <value of string>
                 user-peer: <value of string>
                 users: <value of string>
           auto-tunnel-static-route: <value in [disable, enable]>
           banned-cipher:
             - RSA
             - DH
             - DHE
             - ECDH
             - ECDHE
             - DSS
             - ECDSA
             - AES
             - AESGCM
             - CAMELLIA
             - 3DES
             - SHA1
             - SHA256
             - SHA384
             - STATIC
           check-referer: <value in [disable, enable]>
           default-portal: <value of string>
           deflate-compression-level: <value of integer>
           deflate-min-data-size: <value of integer>
           dns-server1: <value of string>
           dns-server2: <value of string>
           dns-suffix: <value of string>
           dtls-hello-timeout: <value of integer>
           dtls-max-proto-ver: <value in [dtls1-0, dtls1-2]>
           dtls-min-proto-ver: <value in [dtls1-0, dtls1-2]>
           dtls-tunnel: <value in [disable, enable]>
           encode-2f-sequence: <value in [disable, enable]>
           encrypt-and-store-password: <value in [disable, enable]>
           force-two-factor-auth: <value in [disable, enable]>
           header-x-forwarded-for: <value in [pass, add, remove]>
           hsts-include-subdomains: <value in [disable, enable]>
           http-compression: <value in [disable, enable]>
           http-only-cookie: <value in [disable, enable]>
           http-request-body-timeout: <value of integer>
           http-request-header-timeout: <value of integer>
           https-redirect: <value in [disable, enable]>
           idle-timeout: <value of integer>
           ipv6-dns-server1: <value of string>
           ipv6-dns-server2: <value of string>
           ipv6-wins-server1: <value of string>
           ipv6-wins-server2: <value of string>
           login-attempt-limit: <value of integer>
           login-block-time: <value of integer>
           login-timeout: <value of integer>
           port: <value of integer>
           port-precedence: <value in [disable, enable]>
           reqclientcert: <value in [disable, enable]>
           route-source-interface: <value in [disable, enable]>
           servercert: <value of string>
           source-address: <value of string>
           source-address-negate: <value in [disable, enable]>
           source-address6: <value of string>
           source-address6-negate: <value in [disable, enable]>
           source-interface: <value of string>
           ssl-client-renegotiation: <value in [disable, enable]>
           ssl-insert-empty-fragment: <value in [disable, enable]>
           ssl-max-proto-ver: <value in [tls1-0, tls1-1, tls1-2, ...]>
           ssl-min-proto-ver: <value in [tls1-0, tls1-1, tls1-2, ...]>
           tlsv1-0: <value in [disable, enable]>
           tlsv1-1: <value in [disable, enable]>
           tlsv1-2: <value in [disable, enable]>
           tlsv1-3: <value in [disable, enable]>
           transform-backward-slashes: <value in [disable, enable]>
           tunnel-connect-without-reauth: <value in [disable, enable]>
           tunnel-ip-pools: <value of string>
           tunnel-ipv6-pools: <value of string>
           tunnel-user-session-timeout: <value of integer>
           unsafe-legacy-renegotiation: <value in [disable, enable]>
           url-obscuration: <value in [disable, enable]>
           user-peer: <value of string>
           wins-server1: <value of string>
           wins-server2: <value of string>
           x-content-type-options: <value in [disable, enable]>
```

## [Return Values](fmgr_vpn_ssl_settings_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **request_url**  string | The full url requested  Returned: always  Sample: `"/sys/login/user"` |
| **response_code**  integer | The status of api request  Returned: always  Sample: `0` |
| **response_message**  string | The descriptive message of the api response  Returned: always  Sample: `"OK."` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
[Homepage](https://fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/tree/galaxy/2.1.7)
