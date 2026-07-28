---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_firewall_vip6_dynamicmapping module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_firewall_vip6_dynamicmapping_module.html
fetched_at: 2026-07-27T17:32:08+00:00
---
# fortinet.fortimanager.fmgr_firewall_vip6_dynamicmapping module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_vip6_dynamicmapping`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_firewall_vip6_dynamicmapping_module.md#synopsis)
- [Parameters](fmgr_firewall_vip6_dynamicmapping_module.md#parameters)
- [Notes](fmgr_firewall_vip6_dynamicmapping_module.md#notes)
- [Examples](fmgr_firewall_vip6_dynamicmapping_module.md#examples)
- [Return Values](fmgr_firewall_vip6_dynamicmapping_module.md#return-values)

## [Synopsis](fmgr_firewall_vip6_dynamicmapping_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_vip6_dynamicmapping_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **firewall_vip6_dynamicmapping**  dictionary | the top level parameters set |
| **_scope**  list / elements=string | description |
| **name**  string | no description |
| **vdom**  string | no description |
| **add-nat64-route**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **arp-reply**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **color**  integer | no description |
| **comment**  string | no description |
| **embedded-ipv4-address**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **extip**  string | no description |
| **extport**  string | no description |
| **http-cookie-age**  integer | no description |
| **http-cookie-domain**  string | no description |
| **http-cookie-domain-from-host**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **http-cookie-generation**  integer | no description |
| **http-cookie-path**  string | no description |
| **http-cookie-share**  string | no description  Choices:   - `"disable"` - `"same-ip"` |
| **http-ip-header**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **http-ip-header-name**  string | no description |
| **http-multiplex**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **http-redirect**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **https-cookie-secure**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **id**  integer | no description |
| **ipv4-mappedip**  string | no description |
| **ipv4-mappedport**  string | no description |
| **ldb-method**  string | no description  Choices:   - `"static"` - `"round-robin"` - `"weighted"` - `"least-session"` - `"least-rtt"` - `"first-alive"` - `"http-host"` |
| **mappedip**  string | no description |
| **mappedport**  string | no description |
| **max-embryonic-connections**  integer | no description |
| **monitor**  string | no description |
| **nat-source-vip**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **nat64**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **nat66**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **outlook-web-access**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **persistence**  string | no description  Choices:   - `"none"` - `"http-cookie"` - `"ssl-session-id"` |
| **portforward**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **protocol**  string | no description  Choices:   - `"tcp"` - `"udp"` - `"sctp"` |
| **realservers**  list / elements=string | description |
| **client-ip**  string | no description |
| **healthcheck**  string | no description  Choices:   - `"disable"` - `"enable"` - `"vip"` |
| **holddown-interval**  integer | no description |
| **http-host**  string | no description |
| **id**  integer | no description |
| **ip**  string | no description |
| **max-connections**  integer | no description |
| **monitor**  string | description |
| **port**  integer | no description |
| **status**  string | no description  Choices:   - `"active"` - `"standby"` - `"disable"` |
| **weight**  integer | no description |
| **server-type**  string | no description  Choices:   - `"http"` - `"https"` - `"ssl"` - `"tcp"` - `"udp"` - `"ip"` - `"imaps"` - `"pop3s"` - `"smtps"` |
| **src-filter**  string | description |
| **ssl-accept-ffdhe-groups**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-algorithm**  string | no description  Choices:   - `"high"` - `"low"` - `"medium"` - `"custom"` |
| **ssl-certificate**  string | no description |
| **ssl-cipher-suites**  list / elements=string | description |
| **cipher**  string | no description  Choices:   - `"TLS-RSA-WITH-RC4-128-MD5"` - `"TLS-RSA-WITH-RC4-128-SHA"` - `"TLS-RSA-WITH-DES-CBC-SHA"` - `"TLS-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-RSA-WITH-AES-256-CBC-SHA256"` - `"TLS-RSA-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-RSA-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-RSA-WITH-SEED-CBC-SHA"` - `"TLS-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-DHE-RSA-WITH-DES-CBC-SHA"` - `"TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-AES-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-SEED-CBC-SHA"` - `"TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-RC4-128-SHA"` - `"TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-DHE-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-DHE-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-DHE-DSS-WITH-AES-128-CBC-SHA"` - `"TLS-DHE-DSS-WITH-AES-256-CBC-SHA"` - `"TLS-DHE-DSS-WITH-AES-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-AES-128-GCM-SHA256"` - `"TLS-DHE-DSS-WITH-AES-256-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-AES-256-GCM-SHA384"` - `"TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384"` - `"TLS-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-SEED-CBC-SHA"` - `"TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA"` - `"TLS-DHE-DSS-WITH-DES-CBC-SHA"` - `"TLS-AES-128-GCM-SHA256"` - `"TLS-AES-256-GCM-SHA384"` - `"TLS-CHACHA20-POLY1305-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA"` |
| **priority**  integer | no description |
| **versions**  list / elements=string | description  Choices:   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl-client-fallback**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-client-rekey-count**  integer | no description |
| **ssl-client-renegotiation**  string | no description  Choices:   - `"deny"` - `"allow"` - `"secure"` |
| **ssl-client-session-state-max**  integer | no description |
| **ssl-client-session-state-timeout**  integer | no description |
| **ssl-client-session-state-type**  string | no description  Choices:   - `"disable"` - `"time"` - `"count"` - `"both"` |
| **ssl-dh-bits**  string | no description  Choices:   - `"768"` - `"1024"` - `"1536"` - `"2048"` - `"3072"` - `"4096"` |
| **ssl-hpkp**  string | no description  Choices:   - `"disable"` - `"enable"` - `"report-only"` |
| **ssl-hpkp-age**  integer | no description |
| **ssl-hpkp-backup**  string | no description |
| **ssl-hpkp-include-subdomains**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-hpkp-primary**  string | no description |
| **ssl-hpkp-report-uri**  string | no description |
| **ssl-hsts**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-hsts-age**  integer | no description |
| **ssl-hsts-include-subdomains**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-http-location-conversion**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-http-match-host**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-max-version**  string | no description  Choices:   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl-min-version**  string | no description  Choices:   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl-mode**  string | no description  Choices:   - `"half"` - `"full"` |
| **ssl-pfs**  string | no description  Choices:   - `"require"` - `"deny"` - `"allow"` |
| **ssl-send-empty-frags**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-server-algorithm**  string | no description  Choices:   - `"high"` - `"low"` - `"medium"` - `"custom"` - `"client"` |
| **ssl-server-max-version**  string | no description  Choices:   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"client"` - `"tls-1.3"` |
| **ssl-server-min-version**  string | no description  Choices:   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"client"` - `"tls-1.3"` |
| **ssl-server-session-state-max**  integer | no description |
| **ssl-server-session-state-timeout**  integer | no description |
| **ssl-server-session-state-type**  string | no description  Choices:   - `"disable"` - `"time"` - `"count"` - `"both"` |
| **type**  string | no description  Choices:   - `"static-nat"` - `"server-load-balance"` - `"access-proxy"` |
| **uuid**  string | no description |
| **weblogic-server**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **websphere-server**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **vip6**  string / required | the parameter (vip6) in requested url |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_firewall_vip6_dynamicmapping_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_vip6_dynamicmapping_module.md#id4)

```yaml+jinja
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Configure dynamic mappings of virtual IP for IPv6
     fmgr_firewall_vip6_dynamicmapping:
        bypass_validation: False
        adom: ansible
        vip6: 'ansible-test-vip6' # name
        state: present
        firewall_vip6_dynamicmapping:
           _scope:
             -
                 name: FGT_AWS # need a valid device name
                 vdom: root # need a valid vdom name under the device
           arp-reply: disable
           color: 1
           comment: 'ansible-comment'
           id: 1

- name: gathering fortimanager facts
  hosts: fortimanager00
  gather_facts: no
  connection: httpapi
  collections:
    - fortinet.fortimanager
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
   - name: retrieve all the dynamic mappings of virtual IP for IPv6
     fmgr_fact:
       facts:
           selector: 'firewall_vip6_dynamicmapping'
           params:
               adom: 'ansible'
               vip6: 'ansible-test-vip6' # name
               dynamic_mapping: 'your_value'
```

## [Return Values](fmgr_firewall_vip6_dynamicmapping_module.md#id5)

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
