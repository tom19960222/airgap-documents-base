---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_webfilter_profile module – Configure Web filter profiles."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_webfilter_profile_module.html
fetched_at: 2026-07-28T02:22:44+00:00
---
# fortinet.fortimanager.fmgr_webfilter_profile module – Configure Web filter profiles.

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortimanager/) (version 2.3.0).
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
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **webfilter_profile**  dictionary | the top level parameters set |
| **antiphish**  dictionary | no description |
| **authentication**  string | Authentication methods.  **Choices:**   - `"domain-controller"` - `"ldap"` |
| **check-basic-auth**  string | Enable/disable checking of HTTP Basic Auth field for known credentials.  **Choices:**   - `"disable"` - `"enable"` |
| **check-uri**  string | Enable/disable checking of GET URI parameters for known credentials.  **Choices:**   - `"disable"` - `"enable"` |
| **check-username-only**  string | Enable/disable acting only on valid username credentials.  **Choices:**   - `"disable"` - `"enable"` |
| **custom-patterns**  list / elements=dictionary | Custom-Patterns. |
| **category**  string | Category that the pattern matches.  **Choices:**   - `"username"` - `"password"` |
| **pattern**  string | Target pattern. |
| **type**  string | Pattern will be treated either as a regex pattern or literal string.  **Choices:**   - `"regex"` - `"literal"` |
| **default-action**  string | Action to be taken when there is no matching rule.  **Choices:**   - `"log"` - `"block"` - `"exempt"` |
| **domain-controller**  string | Domain for which to verify received credentials against. |
| **inspection-entries**  list / elements=dictionary | Inspection-Entries. |
| **action**  string | Action to be taken upon an AntiPhishing match.  **Choices:**   - `"log"` - `"block"` - `"exempt"` |
| **fortiguard-category**  any | (list) FortiGuard category to match. |
| **name**  string | Inspection target name. |
| **ldap**  string | LDAP server for which to verify received credentials against. |
| **max-body-len**  integer | Maximum size of a POST body to check for credentials. |
| **status**  string | Toggle AntiPhishing functionality.  **Choices:**   - `"disable"` - `"enable"` |
| **comment**  string | Optional comments. |
| **extended-log**  string | Enable/disable extended logging for web filtering.  **Choices:**   - `"disable"` - `"enable"` |
| **feature-set**  string | Flow/proxy feature set.  **Choices:**   - `"proxy"` - `"flow"` |
| **file-filter**  dictionary | no description |
| **entries**  list / elements=dictionary | no description |
| **action**  string | Action taken for matched file.  **Choices:**   - `"log"` - `"block"` |
| **comment**  string | Comment. |
| **direction**  string | Match files transmitted in the sessions originating or reply direction.  **Choices:**   - `"any"` - `"incoming"` - `"outgoing"` |
| **encryption**  string | no description  **Choices:**   - `"any"` - `"yes"` |
| **file-type**  any | (list) no description |
| **filter**  string | Add a file filter. |
| **password-protected**  string | Match password-protected files.  **Choices:**   - `"any"` - `"yes"` |
| **protocol**  list / elements=string | no description  **Choices:**   - `"http"` - `"ftp"` |
| **log**  string | Enable/disable file filter logging.  **Choices:**   - `"disable"` - `"enable"` |
| **scan-archive-contents**  string | Enable/disable file filter archive contents scan.  **Choices:**   - `"disable"` - `"enable"` |
| **status**  string | Enable/disable file filter.  **Choices:**   - `"disable"` - `"enable"` |
| **ftgd-wf**  dictionary | no description |
| **category-override**  string | Local categories take precedence over FortiGuard categories. |
| **exempt-quota**  any | (list or str) Do not stop quota for these categories. |
| **filters**  list / elements=dictionary | Filters. |
| **action**  string | Action to take for matches.  **Choices:**   - `"block"` - `"monitor"` - `"warning"` - `"authenticate"` |
| **auth-usr-grp**  any | (list or str) Groups with permission to authenticate. |
| **category**  string | Categories and groups the filter examines. |
| **id**  integer | ID number. |
| **log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **override-replacemsg**  string | Override replacement message. |
| **warn-duration**  string | Duration of warnings. |
| **warning-duration-type**  string | Re-display warning after closing browser or after a timeout.  **Choices:**   - `"session"` - `"timeout"` |
| **warning-prompt**  string | Warning prompts in each category or each domain.  **Choices:**   - `"per-domain"` - `"per-category"` |
| **max-quota-timeout**  integer | Maximum FortiGuard quota used by single page view in seconds |
| **options**  list / elements=string | Options for FortiGuard Web Filter.  **Choices:**   - `"error-allow"` - `"http-err-detail"` - `"rate-image-urls"` - `"strict-blocking"` - `"rate-server-ip"` - `"redir-block"` - `"connect-request-bypass"` - `"log-all-url"` - `"ftgd-disable"` |
| **ovrd**  any | (list or str) Allow web filter profile overrides. |
| **quota**  list / elements=dictionary | Quota. |
| **category**  any | (list or str) FortiGuard categories to apply quota to |
| **duration**  string | Duration of quota. |
| **id**  integer | ID number. |
| **override-replacemsg**  string | Override replacement message. |
| **type**  string | Quota type.  **Choices:**   - `"time"` - `"traffic"` |
| **unit**  string | Traffic quota unit of measurement.  **Choices:**   - `"B"` - `"KB"` - `"MB"` - `"GB"` |
| **value**  integer | Traffic quota value. |
| **rate-crl-urls**  string | Enable/disable rating CRL by URL.  **Choices:**   - `"disable"` - `"enable"` |
| **rate-css-urls**  string | Enable/disable rating CSS by URL.  **Choices:**   - `"disable"` - `"enable"` |
| **rate-image-urls**  string | Enable/disable rating images by URL.  **Choices:**   - `"disable"` - `"enable"` |
| **rate-javascript-urls**  string | Enable/disable rating JavaScript by URL.  **Choices:**   - `"disable"` - `"enable"` |
| **https-replacemsg**  string | Enable replacement messages for HTTPS.  **Choices:**   - `"disable"` - `"enable"` |
| **inspection-mode**  string | Web filtering inspection mode.  **Choices:**   - `"proxy"` - `"flow-based"` - `"dns"` |
| **log-all-url**  string | Enable/disable logging all URLs visited.  **Choices:**   - `"disable"` - `"enable"` |
| **name**  string / required | Profile name. |
| **options**  list / elements=string | Options.  **Choices:**   - `"block-invalid-url"` - `"jscript"` - `"js"` - `"vbs"` - `"unknown"` - `"wf-referer"` - `"https-scan"` - `"intrinsic"` - `"wf-cookie"` - `"per-user-bwl"` - `"activexfilter"` - `"cookiefilter"` - `"https-url-scan"` - `"javafilter"` - `"rangeblock"` - `"contenttype-check"` - `"per-user-bal"` |
| **override**  dictionary | no description |
| **ovrd-cookie**  string | Allow/deny browser-based  **Choices:**   - `"deny"` - `"allow"` |
| **ovrd-dur**  string | Override duration. |
| **ovrd-dur-mode**  string | Override duration mode.  **Choices:**   - `"constant"` - `"ask"` |
| **ovrd-scope**  string | Override scope.  **Choices:**   - `"user"` - `"user-group"` - `"ip"` - `"ask"` - `"browser"` |
| **ovrd-user-group**  any | (list or str) User groups with permission to use the override. |
| **profile**  any | (list or str) Web filter profile with permission to create overrides. |
| **profile-attribute**  string | Profile attribute to retrieve from the RADIUS server.  **Choices:**   - `"User-Name"` - `"User-Password"` - `"CHAP-Password"` - `"NAS-IP-Address"` - `"NAS-Port"` - `"Service-Type"` - `"Framed-Protocol"` - `"Framed-IP-Address"` - `"Framed-IP-Netmask"` - `"Framed-Routing"` - `"Filter-Id"` - `"Framed-MTU"` - `"Framed-Compression"` - `"Login-IP-Host"` - `"Login-Service"` - `"Login-TCP-Port"` - `"Reply-Message"` - `"Callback-Number"` - `"Callback-Id"` - `"Framed-Route"` - `"Framed-IPX-Network"` - `"State"` - `"Class"` - `"Vendor-Specific"` - `"Session-Timeout"` - `"Idle-Timeout"` - `"Termination-Action"` - `"Called-Station-Id"` - `"Calling-Station-Id"` - `"NAS-Identifier"` - `"Proxy-State"` - `"Login-LAT-Service"` - `"Login-LAT-Node"` - `"Login-LAT-Group"` - `"Framed-AppleTalk-Link"` - `"Framed-AppleTalk-Network"` - `"Framed-AppleTalk-Zone"` - `"Acct-Status-Type"` - `"Acct-Delay-Time"` - `"Acct-Input-Octets"` - `"Acct-Output-Octets"` - `"Acct-Session-Id"` - `"Acct-Authentic"` - `"Acct-Session-Time"` - `"Acct-Input-Packets"` - `"Acct-Output-Packets"` - `"Acct-Terminate-Cause"` - `"Acct-Multi-Session-Id"` - `"Acct-Link-Count"` - `"CHAP-Challenge"` - `"NAS-Port-Type"` - `"Port-Limit"` - `"Login-LAT-Port"` |
| **profile-type**  string | Override profile type.  **Choices:**   - `"list"` - `"radius"` |
| **ovrd-perm**  list / elements=string | Permitted override types.  **Choices:**   - `"bannedword-override"` - `"urlfilter-override"` - `"fortiguard-wf-override"` - `"contenttype-check-override"` |
| **post-action**  string | Action taken for HTTP POST traffic.  **Choices:**   - `"normal"` - `"comfort"` - `"block"` |
| **replacemsg-group**  string | Replacement message group. |
| **url-extraction**  dictionary | no description |
| **redirect-header**  string | HTTP header name to use for client redirect on blocked requests |
| **redirect-no-content**  string | Enable / Disable empty message-body entity in HTTP response  **Choices:**   - `"disable"` - `"enable"` |
| **redirect-url**  string | HTTP header value to use for client redirect on blocked requests |
| **server-fqdn**  string | URL extraction server FQDN |
| **status**  string | Enable URL Extraction  **Choices:**   - `"disable"` - `"enable"` |
| **web**  dictionary | no description |
| **allowlist**  list / elements=string | FortiGuard allowlist settings.  **Choices:**   - `"exempt-av"` - `"exempt-webcontent"` - `"exempt-activex-java-cookie"` - `"exempt-dlp"` - `"exempt-rangeblock"` - `"extended-log-others"` |
| **blacklist**  string | Enable/disable automatic addition of URLs detected by FortiSandbox to blacklist.  **Choices:**   - `"disable"` - `"enable"` |
| **blocklist**  string | Enable/disable automatic addition of URLs detected by FortiSandbox to blocklist.  **Choices:**   - `"disable"` - `"enable"` |
| **bword-table**  string | Banned word table ID. |
| **bword-threshold**  integer | Banned word score threshold. |
| **content-header-list**  string | Content header list. |
| **keyword-match**  any | (list) Search keywords to log when match is found. |
| **log-search**  string | Enable/disable logging all search phrases.  **Choices:**   - `"disable"` - `"enable"` |
| **safe-search**  list / elements=string | Safe search type.  **Choices:**   - `"google"` - `"yahoo"` - `"bing"` - `"url"` - `"header"` |
| **urlfilter-table**  string | URL filter table ID. |
| **vimeo-restrict**  string | Set Vimeo-restrict |
| **whitelist**  list / elements=string | FortiGuard whitelist settings.  **Choices:**   - `"exempt-av"` - `"exempt-webcontent"` - `"exempt-activex-java-cookie"` - `"exempt-dlp"` - `"exempt-rangeblock"` - `"extended-log-others"` |
| **youtube-restrict**  string | YouTube EDU filter level.  **Choices:**   - `"strict"` - `"none"` - `"moderate"` |
| **web-antiphishing-log**  string | Enable/disable logging of AntiPhishing checks.  **Choices:**   - `"disable"` - `"enable"` |
| **web-content-log**  string | Enable/disable logging logging blocked web content.  **Choices:**   - `"disable"` - `"enable"` |
| **web-extended-all-action-log**  string | Enable/disable extended any filter action logging for web filtering.  **Choices:**   - `"disable"` - `"enable"` |
| **web-filter-activex-log**  string | Enable/disable logging ActiveX.  **Choices:**   - `"disable"` - `"enable"` |
| **web-filter-applet-log**  string | Enable/disable logging Java applets.  **Choices:**   - `"disable"` - `"enable"` |
| **web-filter-command-block-log**  string | Enable/disable logging blocked commands.  **Choices:**   - `"disable"` - `"enable"` |
| **web-filter-cookie-log**  string | Enable/disable logging cookie filtering.  **Choices:**   - `"disable"` - `"enable"` |
| **web-filter-cookie-removal-log**  string | Enable/disable logging blocked cookies.  **Choices:**   - `"disable"` - `"enable"` |
| **web-filter-js-log**  string | Enable/disable logging Java scripts.  **Choices:**   - `"disable"` - `"enable"` |
| **web-filter-jscript-log**  string | Enable/disable logging JScripts.  **Choices:**   - `"disable"` - `"enable"` |
| **web-filter-referer-log**  string | Enable/disable logging referrers.  **Choices:**   - `"disable"` - `"enable"` |
| **web-filter-unknown-log**  string | Enable/disable logging unknown scripts.  **Choices:**   - `"disable"` - `"enable"` |
| **web-filter-vbs-log**  string | Enable/disable logging VBS scripts.  **Choices:**   - `"disable"` - `"enable"` |
| **web-ftgd-err-log**  string | Enable/disable logging rating errors.  **Choices:**   - `"disable"` - `"enable"` |
| **web-ftgd-quota-usage**  string | Enable/disable logging daily quota usage.  **Choices:**   - `"disable"` - `"enable"` |
| **web-invalid-domain-log**  string | Enable/disable logging invalid domain names.  **Choices:**   - `"disable"` - `"enable"` |
| **web-url-log**  string | Enable/disable logging URL filtering.  **Choices:**   - `"disable"` - `"enable"` |
| **wisp**  string | Enable/disable web proxy WISP.  **Choices:**   - `"disable"` - `"enable"` |
| **wisp-algorithm**  string | WISP server selection algorithm.  **Choices:**   - `"auto-learning"` - `"primary-secondary"` - `"round-robin"` |
| **wisp-servers**  any | (list or str) WISP servers. |
| **youtube-channel-filter**  list / elements=dictionary | Youtube-Channel-Filter. |
| **channel-id**  string | YouTube channel ID to be filtered. |
| **comment**  string | Comment. |
| **id**  integer | ID. |
| **youtube-channel-status**  string | YouTube channel filter status.  **Choices:**   - `"disable"` - `"blacklist"` - `"whitelist"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

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
    - name: Configure Web filter profiles.
      fmgr_webfilter_profile:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        webfilter_profile:
          comment: <string>
          extended-log: <value in [disable, enable]>
          https-replacemsg: <value in [disable, enable]>
          inspection-mode: <value in [proxy, flow-based, dns]>
          log-all-url: <value in [disable, enable]>
          name: <string>
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
          replacemsg-group: <string>
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
          wisp-servers: <list or string>
          youtube-channel-filter:
            -
              channel-id: <string>
              comment: <string>
              id: <integer>
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
                pattern: <string>
                type: <value in [regex, literal]>
            default-action: <value in [log, block, exempt]>
            domain-controller: <string>
            inspection-entries:
              -
                action: <value in [log, block, exempt]>
                fortiguard-category: <list or string>
                name: <string>
            max-body-len: <integer>
            status: <value in [disable, enable]>
            authentication: <value in [domain-controller, ldap]>
            ldap: <string>
          ftgd-wf:
            exempt-quota: <list or string>
            filters:
              -
                action: <value in [block, monitor, warning, ...]>
                auth-usr-grp: <list or string>
                category: <string>
                id: <integer>
                log: <value in [disable, enable]>
                override-replacemsg: <string>
                warn-duration: <string>
                warning-duration-type: <value in [session, timeout]>
                warning-prompt: <value in [per-domain, per-category]>
            max-quota-timeout: <integer>
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
            ovrd: <list or string>
            quota:
              -
                category: <list or string>
                duration: <string>
                id: <integer>
                override-replacemsg: <string>
                type: <value in [time, traffic]>
                unit: <value in [B, KB, MB, ...]>
                value: <integer>
            rate-crl-urls: <value in [disable, enable]>
            rate-css-urls: <value in [disable, enable]>
            rate-image-urls: <value in [disable, enable]>
            rate-javascript-urls: <value in [disable, enable]>
            category-override: <string>
          override:
            ovrd-cookie: <value in [deny, allow]>
            ovrd-dur: <string>
            ovrd-dur-mode: <value in [constant, ask]>
            ovrd-scope: <value in [user, user-group, ip, ...]>
            ovrd-user-group: <list or string>
            profile: <list or string>
            profile-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
            profile-type: <value in [list, radius]>
          url-extraction:
            redirect-header: <string>
            redirect-no-content: <value in [disable, enable]>
            redirect-url: <string>
            server-fqdn: <string>
            status: <value in [disable, enable]>
          web:
            blacklist: <value in [disable, enable]>
            bword-table: <string>
            bword-threshold: <integer>
            content-header-list: <string>
            keyword-match: <list or string>
            log-search: <value in [disable, enable]>
            safe-search:
              - google
              - yahoo
              - bing
              - url
              - header
            urlfilter-table: <string>
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
            vimeo-restrict: <string>
          file-filter:
            entries:
              -
                action: <value in [log, block]>
                comment: <string>
                direction: <value in [any, incoming, outgoing]>
                encryption: <value in [any, yes]>
                file-type: <list or string>
                filter: <string>
                password-protected: <value in [any, yes]>
                protocol:
                  - http
                  - ftp
            log: <value in [disable, enable]>
            scan-archive-contents: <value in [disable, enable]>
            status: <value in [disable, enable]>
```

## [Return Values](fmgr_webfilter_profile_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meta**  dictionary | The result of the request.  **Returned:** always |
| **request_url**  string | The full url requested.  **Returned:** always  **Sample:** `"/sys/login/user"` |
| **response_code**  integer | The status of api request.  **Returned:** always  **Sample:** `0` |
| **response_data**  list / elements=string | The api response.  **Returned:** always |
| **response_message**  string | The descriptive message of the api response.  **Returned:** always  **Sample:** `"OK."` |
| **system_information**  dictionary | The information of the target system.  **Returned:** always |
| **rc**  integer | The status the request.  **Returned:** always  **Sample:** `0` |
| **version_check_warning**  list / elements=string | Warning if the parameters used in the playbook are not supported by the current FortiManager version.  **Returned:** complex |

### Authors

- Xinwei Du (@dux-fortinet)
- Xing Li (@lix-fortinet)
- Jie Xue (@JieX19)
- Link Zheng (@chillancezen)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
- [Homepage](https://fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection)
