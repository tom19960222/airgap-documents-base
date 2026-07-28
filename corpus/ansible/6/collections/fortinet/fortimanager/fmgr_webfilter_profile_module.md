---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_webfilter_profile module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_webfilter_profile_module.html
fetched_at: 2026-07-27T17:39:24+00:00
---
# fortinet.fortimanager.fmgr_webfilter_profile module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_webfilter_profile`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_webfilter_profile_module.md#synopsis)
- [Parameters](fmgr_webfilter_profile_module.md#parameters)
- [Notes](fmgr_webfilter_profile_module.md#notes)
- [Examples](fmgr_webfilter_profile_module.md#examples)
- [Return Values](fmgr_webfilter_profile_module.md#return-values)

## [Synopsis](fmgr_webfilter_profile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_webfilter_profile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **webfilter_profile**  dictionary | the top level parameters set |
| **antiphish**  dictionary | no description |
| **authentication**  string | no description  Choices:   - `"domain-controller"` - `"ldap"` |
| **check-basic-auth**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **check-uri**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **check-username-only**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **custom-patterns**  list / elements=string | no description |
| **category**  string | no description  Choices:   - `"username"` - `"password"` |
| **pattern**  string | no description |
| **type**  string | no description  Choices:   - `"regex"` - `"literal"` |
| **default-action**  string | no description  Choices:   - `"log"` - `"block"` - `"exempt"` |
| **domain-controller**  string | no description |
| **inspection-entries**  list / elements=string | no description |
| **action**  string | no description  Choices:   - `"log"` - `"block"` - `"exempt"` |
| **fortiguard-category**  string | no description |
| **name**  string | no description |
| **ldap**  string | no description |
| **max-body-len**  integer | no description |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **comment**  string | no description |
| **extended-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **feature-set**  string | no description  Choices:   - `"proxy"` - `"flow"` |
| **ftgd-wf**  dictionary | no description |
| **exempt-quota**  string | no description |
| **filters**  list / elements=string | no description |
| **action**  string | no description  Choices:   - `"block"` - `"monitor"` - `"warning"` - `"authenticate"` |
| **auth-usr-grp**  string | no description |
| **category**  string | no description |
| **id**  integer | no description |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **override-replacemsg**  string | no description |
| **warn-duration**  string | no description |
| **warning-duration-type**  string | no description  Choices:   - `"session"` - `"timeout"` |
| **warning-prompt**  string | no description  Choices:   - `"per-domain"` - `"per-category"` |
| **max-quota-timeout**  integer | no description |
| **options**  list / elements=string | no description  Choices:   - `"error-allow"` - `"http-err-detail"` - `"rate-image-urls"` - `"strict-blocking"` - `"rate-server-ip"` - `"redir-block"` - `"connect-request-bypass"` - `"log-all-url"` - `"ftgd-disable"` |
| **ovrd**  string | no description |
| **quota**  list / elements=string | no description |
| **category**  string | no description |
| **duration**  string | no description |
| **id**  integer | no description |
| **override-replacemsg**  string | no description |
| **type**  string | no description  Choices:   - `"time"` - `"traffic"` |
| **unit**  string | no description  Choices:   - `"B"` - `"KB"` - `"MB"` - `"GB"` |
| **value**  integer | no description |
| **rate-crl-urls**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **rate-css-urls**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **rate-image-urls**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **rate-javascript-urls**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **https-replacemsg**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **inspection-mode**  string | no description  Choices:   - `"proxy"` - `"flow-based"` - `"dns"` |
| **log-all-url**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **name**  string | no description |
| **options**  list / elements=string | no description  Choices:   - `"block-invalid-url"` - `"jscript"` - `"js"` - `"vbs"` - `"unknown"` - `"wf-referer"` - `"https-scan"` - `"intrinsic"` - `"wf-cookie"` - `"per-user-bwl"` - `"activexfilter"` - `"cookiefilter"` - `"https-url-scan"` - `"javafilter"` - `"rangeblock"` - `"contenttype-check"` - `"per-user-bal"` |
| **override**  dictionary | no description |
| **ovrd-cookie**  string | no description  Choices:   - `"deny"` - `"allow"` |
| **ovrd-dur**  string | no description |
| **ovrd-dur-mode**  string | no description  Choices:   - `"constant"` - `"ask"` |
| **ovrd-scope**  string | no description  Choices:   - `"user"` - `"user-group"` - `"ip"` - `"ask"` - `"browser"` |
| **ovrd-user-group**  string | no description |
| **profile**  string | no description |
| **profile-attribute**  string | no description  Choices:   - `"User-Name"` - `"User-Password"` - `"CHAP-Password"` - `"NAS-IP-Address"` - `"NAS-Port"` - `"Service-Type"` - `"Framed-Protocol"` - `"Framed-IP-Address"` - `"Framed-IP-Netmask"` - `"Framed-Routing"` - `"Filter-Id"` - `"Framed-MTU"` - `"Framed-Compression"` - `"Login-IP-Host"` - `"Login-Service"` - `"Login-TCP-Port"` - `"Reply-Message"` - `"Callback-Number"` - `"Callback-Id"` - `"Framed-Route"` - `"Framed-IPX-Network"` - `"State"` - `"Class"` - `"Vendor-Specific"` - `"Session-Timeout"` - `"Idle-Timeout"` - `"Termination-Action"` - `"Called-Station-Id"` - `"Calling-Station-Id"` - `"NAS-Identifier"` - `"Proxy-State"` - `"Login-LAT-Service"` - `"Login-LAT-Node"` - `"Login-LAT-Group"` - `"Framed-AppleTalk-Link"` - `"Framed-AppleTalk-Network"` - `"Framed-AppleTalk-Zone"` - `"Acct-Status-Type"` - `"Acct-Delay-Time"` - `"Acct-Input-Octets"` - `"Acct-Output-Octets"` - `"Acct-Session-Id"` - `"Acct-Authentic"` - `"Acct-Session-Time"` - `"Acct-Input-Packets"` - `"Acct-Output-Packets"` - `"Acct-Terminate-Cause"` - `"Acct-Multi-Session-Id"` - `"Acct-Link-Count"` - `"CHAP-Challenge"` - `"NAS-Port-Type"` - `"Port-Limit"` - `"Login-LAT-Port"` |
| **profile-type**  string | no description  Choices:   - `"list"` - `"radius"` |
| **ovrd-perm**  list / elements=string | no description  Choices:   - `"bannedword-override"` - `"urlfilter-override"` - `"fortiguard-wf-override"` - `"contenttype-check-override"` |
| **post-action**  string | no description  Choices:   - `"normal"` - `"comfort"` - `"block"` |
| **replacemsg-group**  string | no description |
| **url-extraction**  dictionary | no description |
| **redirect-header**  string | no description |
| **redirect-no-content**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **redirect-url**  string | no description |
| **server-fqdn**  string | no description |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **web**  dictionary | no description |
| **allowlist**  list / elements=string | no description  Choices:   - `"exempt-av"` - `"exempt-webcontent"` - `"exempt-activex-java-cookie"` - `"exempt-dlp"` - `"exempt-rangeblock"` - `"extended-log-others"` |
| **blacklist**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **blocklist**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **bword-table**  string | no description |
| **bword-threshold**  integer | no description |
| **content-header-list**  string | no description |
| **keyword-match**  string | no description |
| **log-search**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **safe-search**  list / elements=string | no description  Choices:   - `"google"` - `"yahoo"` - `"bing"` - `"url"` - `"header"` |
| **urlfilter-table**  string | no description |
| **vimeo-restrict**  string | no description |
| **whitelist**  list / elements=string | no description  Choices:   - `"exempt-av"` - `"exempt-webcontent"` - `"exempt-activex-java-cookie"` - `"exempt-dlp"` - `"exempt-rangeblock"` - `"extended-log-others"` |
| **youtube-restrict**  string | no description  Choices:   - `"strict"` - `"none"` - `"moderate"` |
| **web-antiphishing-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **web-content-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **web-extended-all-action-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **web-filter-activex-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **web-filter-applet-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **web-filter-command-block-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **web-filter-cookie-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **web-filter-cookie-removal-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **web-filter-js-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **web-filter-jscript-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **web-filter-referer-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **web-filter-unknown-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **web-filter-vbs-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **web-ftgd-err-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **web-ftgd-quota-usage**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **web-invalid-domain-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **web-url-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **wisp**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **wisp-algorithm**  string | no description  Choices:   - `"auto-learning"` - `"primary-secondary"` - `"round-robin"` |
| **wisp-servers**  string | no description |
| **youtube-channel-filter**  list / elements=string | no description |
| **channel-id**  string | no description |
| **comment**  string | no description |
| **id**  integer | no description |
| **youtube-channel-status**  string | no description  Choices:   - `"disable"` - `"blacklist"` - `"whitelist"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_webfilter_profile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_webfilter_profile_module.md#id4)

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
     fmgr_webfilter_profile:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        webfilter_profile:
           comment: <value of string>
           extended-log: <value in [disable, enable]>
           https-replacemsg: <value in [disable, enable]>
           inspection-mode: <value in [proxy, flow-based, dns]>
           log-all-url: <value in [disable, enable]>
           name: <value of string>
           options:
             - block-invalid-url
             - jscript
             - js
             - vbs
             - unknown
             - wf-referer
             - https-scan
             - intrinsic
             - wf-cookie
             - per-user-bwl
             - activexfilter
             - cookiefilter
             - https-url-scan
             - javafilter
             - rangeblock
             - contenttype-check
             - per-user-bal
           ovrd-perm:
             - bannedword-override
             - urlfilter-override
             - fortiguard-wf-override
             - contenttype-check-override
           post-action: <value in [normal, comfort, block]>
           replacemsg-group: <value of string>
           web-content-log: <value in [disable, enable]>
           web-extended-all-action-log: <value in [disable, enable]>
           web-filter-activex-log: <value in [disable, enable]>
           web-filter-applet-log: <value in [disable, enable]>
           web-filter-command-block-log: <value in [disable, enable]>
           web-filter-cookie-log: <value in [disable, enable]>
           web-filter-cookie-removal-log: <value in [disable, enable]>
           web-filter-js-log: <value in [disable, enable]>
           web-filter-jscript-log: <value in [disable, enable]>
           web-filter-referer-log: <value in [disable, enable]>
           web-filter-unknown-log: <value in [disable, enable]>
           web-filter-vbs-log: <value in [disable, enable]>
           web-ftgd-err-log: <value in [disable, enable]>
           web-ftgd-quota-usage: <value in [disable, enable]>
           web-invalid-domain-log: <value in [disable, enable]>
           web-url-log: <value in [disable, enable]>
           wisp: <value in [disable, enable]>
           wisp-algorithm: <value in [auto-learning, primary-secondary, round-robin]>
           wisp-servers: <value of string>
           youtube-channel-filter:
             -
                 channel-id: <value of string>
                 comment: <value of string>
                 id: <value of integer>
           youtube-channel-status: <value in [disable, blacklist, whitelist]>
           feature-set: <value in [proxy, flow]>
           web-antiphishing-log: <value in [disable, enable]>
           antiphish:
              check-basic-auth: <value in [disable, enable]>
              check-uri: <value in [disable, enable]>
              check-username-only: <value in [disable, enable]>
              custom-patterns:
                -
                    category: <value in [username, password]>
                    pattern: <value of string>
                    type: <value in [regex, literal]>
              default-action: <value in [log, block, exempt]>
              domain-controller: <value of string>
              inspection-entries:
                -
                    action: <value in [log, block, exempt]>
                    fortiguard-category: <value of string>
                    name: <value of string>
              max-body-len: <value of integer>
              status: <value in [disable, enable]>
              authentication: <value in [domain-controller, ldap]>
              ldap: <value of string>
           ftgd-wf:
              exempt-quota: <value of string>
              filters:
                -
                    action: <value in [block, monitor, warning, ...]>
                    auth-usr-grp: <value of string>
                    category: <value of string>
                    id: <value of integer>
                    log: <value in [disable, enable]>
                    override-replacemsg: <value of string>
                    warn-duration: <value of string>
                    warning-duration-type: <value in [session, timeout]>
                    warning-prompt: <value in [per-domain, per-category]>
              max-quota-timeout: <value of integer>
              options:
                - error-allow
                - http-err-detail
                - rate-image-urls
                - strict-blocking
                - rate-server-ip
                - redir-block
                - connect-request-bypass
                - log-all-url
                - ftgd-disable
              ovrd: <value of string>
              quota:
                -
                    category: <value of string>
                    duration: <value of string>
                    id: <value of integer>
                    override-replacemsg: <value of string>
                    type: <value in [time, traffic]>
                    unit: <value in [B, KB, MB, ...]>
                    value: <value of integer>
              rate-crl-urls: <value in [disable, enable]>
              rate-css-urls: <value in [disable, enable]>
              rate-image-urls: <value in [disable, enable]>
              rate-javascript-urls: <value in [disable, enable]>
           override:
              ovrd-cookie: <value in [deny, allow]>
              ovrd-dur: <value of string>
              ovrd-dur-mode: <value in [constant, ask]>
              ovrd-scope: <value in [user, user-group, ip, ...]>
              ovrd-user-group: <value of string>
              profile: <value of string>
              profile-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
              profile-type: <value in [list, radius]>
           url-extraction:
              redirect-header: <value of string>
              redirect-no-content: <value in [disable, enable]>
              redirect-url: <value of string>
              server-fqdn: <value of string>
              status: <value in [disable, enable]>
           web:
              blacklist: <value in [disable, enable]>
              bword-table: <value of string>
              bword-threshold: <value of integer>
              content-header-list: <value of string>
              keyword-match: <value of string>
              log-search: <value in [disable, enable]>
              safe-search:
                - google
                - yahoo
                - bing
                - url
                - header
              urlfilter-table: <value of string>
              whitelist:
                - exempt-av
                - exempt-webcontent
                - exempt-activex-java-cookie
                - exempt-dlp
                - exempt-rangeblock
                - extended-log-others
              youtube-restrict: <value in [strict, none, moderate]>
              allowlist:
                - exempt-av
                - exempt-webcontent
                - exempt-activex-java-cookie
                - exempt-dlp
                - exempt-rangeblock
                - extended-log-others
              blocklist: <value in [disable, enable]>
              vimeo-restrict: <value of string>
```

## [Return Values](fmgr_webfilter_profile_module.md#id5)

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
