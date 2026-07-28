---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_firewall_accessproxy_apigateway6 module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_firewall_accessproxy_apigateway6_module.html
fetched_at: 2026-07-27T17:30:40+00:00
---
# fortinet.fortimanager.fmgr_firewall_accessproxy_apigateway6 module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_accessproxy_apigateway6`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_firewall_accessproxy_apigateway6_module.md#synopsis)
- [Parameters](fmgr_firewall_accessproxy_apigateway6_module.md#parameters)
- [Notes](fmgr_firewall_accessproxy_apigateway6_module.md#notes)
- [Examples](fmgr_firewall_accessproxy_apigateway6_module.md#examples)
- [Return Values](fmgr_firewall_accessproxy_apigateway6_module.md#return-values)

## [Synopsis](fmgr_firewall_accessproxy_apigateway6_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_accessproxy_apigateway6_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access-proxy**  string / required | the parameter (access-proxy) in requested url |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **firewall_accessproxy_apigateway6**  dictionary | the top level parameters set |
| **http-cookie-age**  integer | no description |
| **http-cookie-domain**  string | no description |
| **http-cookie-domain-from-host**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **http-cookie-generation**  integer | no description |
| **http-cookie-path**  string | no description |
| **http-cookie-share**  string | no description  Choices:   - `"disable"` - `"same-ip"` |
| **https-cookie-secure**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **id**  integer | no description |
| **ldb-method**  string | no description  Choices:   - `"static"` - `"round-robin"` - `"weighted"` - `"first-alive"` - `"http-host"` |
| **persistence**  string | no description  Choices:   - `"none"` - `"http-cookie"` |
| **realservers**  list / elements=string | description |
| **addr-type**  string | no description  Choices:   - `"fqdn"` - `"ip"` |
| **address**  string | no description |
| **domain**  string | no description |
| **health-check**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **health-check-proto**  string | no description  Choices:   - `"ping"` - `"http"` - `"tcp-connect"` |
| **holddown-interval**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **http-host**  string | no description |
| **id**  integer | no description |
| **ip**  string | no description |
| **mappedport**  string | no description |
| **port**  integer | no description |
| **ssh-client-cert**  string | no description |
| **ssh-host-key**  string | description |
| **ssh-host-key-validation**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **status**  string | no description  Choices:   - `"active"` - `"standby"` - `"disable"` |
| **type**  string | no description  Choices:   - `"tcp-forwarding"` - `"ssh"` |
| **weight**  integer | no description |
| **saml-redirect**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **saml-server**  string | no description |
| **service**  string | no description  Choices:   - `"http"` - `"https"` - `"tcp-forwarding"` - `"samlsp"` - `"web-portal"` |
| **ssl-algorithm**  string | no description  Choices:   - `"high"` - `"medium"` - `"low"` |
| **ssl-cipher-suites**  list / elements=string | description |
| **cipher**  string | no description  Choices:   - `"TLS-RSA-WITH-RC4-128-MD5"` - `"TLS-RSA-WITH-RC4-128-SHA"` - `"TLS-RSA-WITH-DES-CBC-SHA"` - `"TLS-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-RSA-WITH-AES-256-CBC-SHA256"` - `"TLS-RSA-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-RSA-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-RSA-WITH-SEED-CBC-SHA"` - `"TLS-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-DHE-RSA-WITH-DES-CBC-SHA"` - `"TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-AES-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-SEED-CBC-SHA"` - `"TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-RC4-128-SHA"` - `"TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-DHE-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-DHE-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-DHE-DSS-WITH-AES-128-CBC-SHA"` - `"TLS-DHE-DSS-WITH-AES-256-CBC-SHA"` - `"TLS-DHE-DSS-WITH-AES-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-AES-128-GCM-SHA256"` - `"TLS-DHE-DSS-WITH-AES-256-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-AES-256-GCM-SHA384"` - `"TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384"` - `"TLS-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-SEED-CBC-SHA"` - `"TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA"` - `"TLS-DHE-DSS-WITH-DES-CBC-SHA"` - `"TLS-AES-128-GCM-SHA256"` - `"TLS-AES-256-GCM-SHA384"` - `"TLS-CHACHA20-POLY1305-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA"` |
| **priority**  integer | no description |
| **versions**  list / elements=string | description  Choices:   - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl-dh-bits**  string | no description  Choices:   - `"768"` - `"1024"` - `"1536"` - `"2048"` - `"3072"` - `"4096"` |
| **ssl-max-version**  string | no description  Choices:   - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl-min-version**  string | no description  Choices:   - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl-vpn-web-portal**  string | no description |
| **url-map**  string | no description |
| **url-map-type**  string | no description  Choices:   - `"sub-string"` - `"wildcard"` - `"regex"` |
| **virtual-host**  string | no description |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_firewall_accessproxy_apigateway6_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_accessproxy_apigateway6_module.md#id4)

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
     fmgr_firewall_accessproxy_apigateway6:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        access-proxy: <your own value>
        state: <value in [present, absent]>
        firewall_accessproxy_apigateway6:
           http-cookie-age: <value of integer>
           http-cookie-domain: <value of string>
           http-cookie-domain-from-host: <value in [disable, enable]>
           http-cookie-generation: <value of integer>
           http-cookie-path: <value of string>
           http-cookie-share: <value in [disable, same-ip]>
           https-cookie-secure: <value in [disable, enable]>
           id: <value of integer>
           ldb-method: <value in [static, round-robin, weighted, ...]>
           persistence: <value in [none, http-cookie]>
           realservers:
             -
                 addr-type: <value in [fqdn, ip]>
                 address: <value of string>
                 domain: <value of string>
                 health-check: <value in [disable, enable]>
                 health-check-proto: <value in [ping, http, tcp-connect]>
                 holddown-interval: <value in [disable, enable]>
                 http-host: <value of string>
                 id: <value of integer>
                 ip: <value of string>
                 mappedport: <value of string>
                 port: <value of integer>
                 ssh-client-cert: <value of string>
                 ssh-host-key: <value of string>
                 ssh-host-key-validation: <value in [disable, enable]>
                 status: <value in [active, standby, disable]>
                 type: <value in [tcp-forwarding, ssh]>
                 weight: <value of integer>
           saml-redirect: <value in [disable, enable]>
           saml-server: <value of string>
           service: <value in [http, https, tcp-forwarding, ...]>
           ssl-algorithm: <value in [high, medium, low]>
           ssl-cipher-suites:
             -
                 cipher: <value in [TLS-RSA-WITH-RC4-128-MD5, TLS-RSA-WITH-RC4-128-SHA, TLS-RSA-WITH-DES-CBC-SHA, ...]>
                 priority: <value of integer>
                 versions:
                   - tls-1.0
                   - tls-1.1
                   - tls-1.2
                   - tls-1.3
           ssl-dh-bits: <value in [768, 1024, 1536, ...]>
           ssl-max-version: <value in [tls-1.0, tls-1.1, tls-1.2, ...]>
           ssl-min-version: <value in [tls-1.0, tls-1.1, tls-1.2, ...]>
           ssl-vpn-web-portal: <value of string>
           url-map: <value of string>
           url-map-type: <value in [sub-string, wildcard, regex]>
           virtual-host: <value of string>
```

## [Return Values](fmgr_firewall_accessproxy_apigateway6_module.md#id5)

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
