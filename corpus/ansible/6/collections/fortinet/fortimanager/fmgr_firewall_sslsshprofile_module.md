---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_firewall_sslsshprofile module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_firewall_sslsshprofile_module.html
fetched_at: 2026-07-27T17:31:54+00:00
---
# fortinet.fortimanager.fmgr_firewall_sslsshprofile module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_sslsshprofile`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_firewall_sslsshprofile_module.md#synopsis)
- [Parameters](fmgr_firewall_sslsshprofile_module.md#parameters)
- [Notes](fmgr_firewall_sslsshprofile_module.md#notes)
- [Examples](fmgr_firewall_sslsshprofile_module.md#examples)
- [Return Values](fmgr_firewall_sslsshprofile_module.md#return-values)

## [Synopsis](fmgr_firewall_sslsshprofile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_sslsshprofile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **firewall_sslsshprofile**  dictionary | the top level parameters set |
| **allowlist**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **block-blacklisted-certificates**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **block-blocklisted-certificates**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **caname**  string | no description |
| **comment**  string | no description |
| **dot**  dictionary | no description |
| **cert-validation-failure**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **cert-validation-timeout**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **client-certificate**  string | no description  Choices:   - `"bypass"` - `"inspect"` - `"block"` |
| **expired-server-cert**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **proxy-after-tcp-handshake**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **revoked-server-cert**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **sni-server-cert-check**  string | no description  Choices:   - `"enable"` - `"strict"` - `"disable"` |
| **status**  string | no description  Choices:   - `"disable"` - `"deep-inspection"` |
| **unsupported-ssl-cipher**  string | no description  Choices:   - `"block"` - `"allow"` |
| **unsupported-ssl-negotiation**  string | no description  Choices:   - `"block"` - `"allow"` |
| **unsupported-ssl-version**  string | no description  Choices:   - `"block"` - `"allow"` - `"inspect"` |
| **untrusted-server-cert**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **ftps**  dictionary | no description |
| **cert-validation-failure**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **cert-validation-timeout**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **client-certificate**  string | no description  Choices:   - `"bypass"` - `"inspect"` - `"block"` |
| **expired-server-cert**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **min-allowed-ssl-version**  string | no description  Choices:   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ports**  integer | no description |
| **revoked-server-cert**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **sni-server-cert-check**  string | no description  Choices:   - `"disable"` - `"enable"` - `"strict"` |
| **status**  string | no description  Choices:   - `"disable"` - `"deep-inspection"` |
| **unsupported-ssl-cipher**  string | no description  Choices:   - `"allow"` - `"block"` |
| **unsupported-ssl-negotiation**  string | no description  Choices:   - `"allow"` - `"block"` |
| **unsupported-ssl-version**  string | no description  Choices:   - `"block"` - `"allow"` - `"inspect"` |
| **untrusted-server-cert**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **https**  dictionary | no description |
| **cert-probe-failure**  string | no description  Choices:   - `"block"` - `"allow"` |
| **cert-validation-failure**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **cert-validation-timeout**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **client-certificate**  string | no description  Choices:   - `"bypass"` - `"inspect"` - `"block"` |
| **expired-server-cert**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **min-allowed-ssl-version**  string | no description  Choices:   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ports**  integer | no description |
| **proxy-after-tcp-handshake**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **revoked-server-cert**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **sni-server-cert-check**  string | no description  Choices:   - `"disable"` - `"enable"` - `"strict"` |
| **status**  string | no description  Choices:   - `"disable"` - `"certificate-inspection"` - `"deep-inspection"` |
| **unsupported-ssl-cipher**  string | no description  Choices:   - `"allow"` - `"block"` |
| **unsupported-ssl-negotiation**  string | no description  Choices:   - `"allow"` - `"block"` |
| **unsupported-ssl-version**  string | no description  Choices:   - `"block"` - `"allow"` - `"inspect"` |
| **untrusted-server-cert**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **imaps**  dictionary | no description |
| **cert-validation-failure**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **cert-validation-timeout**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **client-certificate**  string | no description  Choices:   - `"bypass"` - `"inspect"` - `"block"` |
| **expired-server-cert**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **ports**  integer | no description |
| **proxy-after-tcp-handshake**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **revoked-server-cert**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **sni-server-cert-check**  string | no description  Choices:   - `"disable"` - `"enable"` - `"strict"` |
| **status**  string | no description  Choices:   - `"disable"` - `"deep-inspection"` |
| **unsupported-ssl-cipher**  string | no description  Choices:   - `"allow"` - `"block"` |
| **unsupported-ssl-negotiation**  string | no description  Choices:   - `"allow"` - `"block"` |
| **unsupported-ssl-version**  string | no description  Choices:   - `"block"` - `"allow"` - `"inspect"` |
| **untrusted-server-cert**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **mapi-over-https**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **name**  string | no description |
| **pop3s**  dictionary | no description |
| **cert-validation-failure**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **cert-validation-timeout**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **client-certificate**  string | no description  Choices:   - `"bypass"` - `"inspect"` - `"block"` |
| **expired-server-cert**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **ports**  integer | no description |
| **proxy-after-tcp-handshake**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **revoked-server-cert**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **sni-server-cert-check**  string | no description  Choices:   - `"disable"` - `"enable"` - `"strict"` |
| **status**  string | no description  Choices:   - `"disable"` - `"deep-inspection"` |
| **unsupported-ssl-cipher**  string | no description  Choices:   - `"allow"` - `"block"` |
| **unsupported-ssl-negotiation**  string | no description  Choices:   - `"allow"` - `"block"` |
| **unsupported-ssl-version**  string | no description  Choices:   - `"block"` - `"allow"` - `"inspect"` |
| **untrusted-server-cert**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **rpc-over-https**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **server-cert**  string | no description |
| **server-cert-mode**  string | no description  Choices:   - `"re-sign"` - `"replace"` |
| **smtps**  dictionary | no description |
| **cert-validation-failure**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **cert-validation-timeout**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **client-certificate**  string | no description  Choices:   - `"bypass"` - `"inspect"` - `"block"` |
| **expired-server-cert**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **ports**  integer | no description |
| **proxy-after-tcp-handshake**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **revoked-server-cert**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **sni-server-cert-check**  string | no description  Choices:   - `"disable"` - `"enable"` - `"strict"` |
| **status**  string | no description  Choices:   - `"disable"` - `"deep-inspection"` |
| **unsupported-ssl-cipher**  string | no description  Choices:   - `"allow"` - `"block"` |
| **unsupported-ssl-negotiation**  string | no description  Choices:   - `"allow"` - `"block"` |
| **unsupported-ssl-version**  string | no description  Choices:   - `"block"` - `"allow"` - `"inspect"` |
| **untrusted-server-cert**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **ssh**  dictionary | no description |
| **inspect-all**  string | no description  Choices:   - `"disable"` - `"deep-inspection"` |
| **ports**  integer | no description |
| **proxy-after-tcp-handshake**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssh-algorithm**  string | no description  Choices:   - `"compatible"` - `"high-encryption"` |
| **ssh-tun-policy-check**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **status**  string | no description  Choices:   - `"disable"` - `"deep-inspection"` |
| **unsupported-version**  string | no description  Choices:   - `"block"` - `"bypass"` |
| **ssl**  dictionary | no description |
| **cert-probe-failure**  string | no description  Choices:   - `"block"` - `"allow"` |
| **cert-validation-failure**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **cert-validation-timeout**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **client-certificate**  string | no description  Choices:   - `"bypass"` - `"inspect"` - `"block"` |
| **expired-server-cert**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **inspect-all**  string | no description  Choices:   - `"disable"` - `"certificate-inspection"` - `"deep-inspection"` |
| **min-allowed-ssl-version**  string | no description  Choices:   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **revoked-server-cert**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **sni-server-cert-check**  string | no description  Choices:   - `"disable"` - `"enable"` - `"strict"` |
| **unsupported-ssl-cipher**  string | no description  Choices:   - `"allow"` - `"block"` |
| **unsupported-ssl-negotiation**  string | no description  Choices:   - `"allow"` - `"block"` |
| **unsupported-ssl-version**  string | no description  Choices:   - `"block"` - `"allow"` - `"inspect"` |
| **untrusted-server-cert**  string | no description  Choices:   - `"allow"` - `"block"` - `"ignore"` |
| **ssl-anomalies-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-anomaly-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-exempt**  list / elements=string | no description |
| **address**  string | no description |
| **address6**  string | no description |
| **fortiguard-category**  string | no description |
| **id**  integer | no description |
| **regex**  string | no description |
| **type**  string | no description  Choices:   - `"fortiguard-category"` - `"address"` - `"address6"` - `"wildcard-fqdn"` - `"regex"` - `"finger-print"` |
| **wildcard-fqdn**  string | no description |
| **ssl-exemption-ip-rating**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-exemption-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-exemptions-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-handshake-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-negotiation-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-server**  list / elements=string | no description |
| **ftps-client-cert-request**  string | no description  Choices:   - `"bypass"` - `"inspect"` - `"block"` |
| **ftps-client-certificate**  string | no description  Choices:   - `"bypass"` - `"inspect"` - `"block"` |
| **https-client-cert-request**  string | no description  Choices:   - `"bypass"` - `"inspect"` - `"block"` |
| **https-client-certificate**  string | no description  Choices:   - `"bypass"` - `"inspect"` - `"block"` |
| **id**  integer | no description |
| **imaps-client-cert-request**  string | no description  Choices:   - `"bypass"` - `"inspect"` - `"block"` |
| **imaps-client-certificate**  string | no description  Choices:   - `"bypass"` - `"inspect"` - `"block"` |
| **ip**  string | no description |
| **pop3s-client-cert-request**  string | no description  Choices:   - `"bypass"` - `"inspect"` - `"block"` |
| **pop3s-client-certificate**  string | no description  Choices:   - `"bypass"` - `"inspect"` - `"block"` |
| **smtps-client-cert-request**  string | no description  Choices:   - `"bypass"` - `"inspect"` - `"block"` |
| **smtps-client-certificate**  string | no description  Choices:   - `"bypass"` - `"inspect"` - `"block"` |
| **ssl-other-client-cert-request**  string | no description  Choices:   - `"bypass"` - `"inspect"` - `"block"` |
| **ssl-other-client-certificate**  string | no description  Choices:   - `"bypass"` - `"inspect"` - `"block"` |
| **ssl-server-cert-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **supported-alpn**  string | no description  Choices:   - `"none"` - `"http1-1"` - `"http2"` - `"all"` |
| **untrusted-caname**  string | no description |
| **use-ssl-server**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **whitelist**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_firewall_sslsshprofile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_sslsshprofile_module.md#id4)

```yaml+jinja
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
   - name: retrieve all the SSL/SSH protocol options
     fmgr_fact:
       facts:
           selector: 'firewall_sslsshprofile'
           params:
               adom: 'ansible'
               ssl-ssh-profile: 'your_value'
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Configure SSL/SSH protocol options.
     fmgr_firewall_sslsshprofile:
        bypass_validation: False
        adom: ansible
        state: present
        firewall_sslsshprofile:
           comment: 'ansible-comment1'
           mapi-over-https: disable #<value in [disable, enable]>
           name: 'ansible-test'
           use-ssl-server: disable #<value in [disable, enable]>
           whitelist: enable #<value in [disable, enable]>
```

## [Return Values](fmgr_firewall_sslsshprofile_module.md#id5)

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
