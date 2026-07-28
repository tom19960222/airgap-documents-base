---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_webfilter_profile module – Configure Web filter profiles in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_webfilter_profile_module.html
fetched_at: 2026-07-27T17:46:51+00:00
---
# fortinet.fortios.fortios_webfilter_profile module – Configure Web filter profiles in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/fortinet/fortios) (version 2.2.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_webfilter_profile_module.md#ansible-collections-fortinet-fortios-fortios-webfilter-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_webfilter_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_webfilter_profile_module.md#synopsis)
- [Requirements](fortios_webfilter_profile_module.md#requirements)
- [Parameters](fortios_webfilter_profile_module.md#parameters)
- [Notes](fortios_webfilter_profile_module.md#notes)
- [Examples](fortios_webfilter_profile_module.md#examples)
- [Return Values](fortios_webfilter_profile_module.md#return-values)

## [Synopsis](fortios_webfilter_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify webfilter feature and profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_webfilter_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_webfilter_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |
| **webfilter_profile**  dictionary | Configure Web filter profiles. |
| **antiphish**  dictionary | AntiPhishing profile. |
| **authentication**  string | Authentication methods.  Choices:   - `"domain-controller"` - `"ldap"` |
| **check_basic_auth**  string | Enable/disable checking of HTTP Basic Auth field for known credentials.  Choices:   - `"enable"` - `"disable"` |
| **check_uri**  string | Enable/disable checking of GET URI parameters for known credentials.  Choices:   - `"enable"` - `"disable"` |
| **check_username_only**  string | Enable/disable username only matching of credentials. Action will be taken for valid usernames regardless of password validity.  Choices:   - `"enable"` - `"disable"` |
| **custom_patterns**  list / elements=dictionary | Custom username and password regex patterns. |
| **category**  string | Category that the pattern matches.  Choices:   - `"username"` - `"password"` |
| **pattern**  string | Target pattern. |
| **type**  string | Pattern will be treated either as a regex pattern or literal string.  Choices:   - `"regex"` - `"literal"` |
| **default_action**  string | Action to be taken when there is no matching rule.  Choices:   - `"exempt"` - `"log"` - `"block"` |
| **domain_controller**  string | Domain for which to verify received credentials against. Source user.domain-controller.name credential-store.domain-controller .server-name. |
| **inspection_entries**  list / elements=dictionary | AntiPhishing entries. |
| **action**  string | Action to be taken upon an AntiPhishing match.  Choices:   - `"exempt"` - `"log"` - `"block"` |
| **fortiguard_category**  list / elements=string | FortiGuard category to match. |
| **name**  string | Inspection target name. |
| **ldap**  string | LDAP server for which to verify received credentials against. Source user.ldap.name. |
| **max_body_len**  integer | Maximum size of a POST body to check for credentials. |
| **status**  string | Toggle AntiPhishing functionality.  Choices:   - `"enable"` - `"disable"` |
| **comment**  string | Optional comments. |
| **extended_log**  string | Enable/disable extended logging for web filtering.  Choices:   - `"enable"` - `"disable"` |
| **feature_set**  string | Flow/proxy feature set.  Choices:   - `"flow"` - `"proxy"` |
| **file_filter**  dictionary | File filter. |
| **entries**  list / elements=dictionary | File filter entries. |
| **action**  string | Action taken for matched file.  Choices:   - `"log"` - `"block"` |
| **comment**  string | Comment. |
| **direction**  string | Match files transmitted in the session”s originating or reply direction.  Choices:   - `"incoming"` - `"outgoing"` - `"any"` |
| **file_type**  list / elements=dictionary | Select file type. |
| **name**  string | File type name. Source antivirus.filetype.name. |
| **filter**  string | Add a file filter. |
| **password_protected**  string | Match password-protected files.  Choices:   - `"yes"` - `"any"` |
| **protocol**  list / elements=string | Protocols to apply with.  Choices:   - `"http"` - `"ftp"` |
| **log**  string | Enable/disable file filter logging.  Choices:   - `"enable"` - `"disable"` |
| **scan_archive_contents**  string | Enable/disable file filter archive contents scan.  Choices:   - `"enable"` - `"disable"` |
| **status**  string | Enable/disable file filter.  Choices:   - `"enable"` - `"disable"` |
| **ftgd_wf**  dictionary | FortiGuard Web Filter settings. |
| **exempt_quota**  list / elements=string | Do not stop quota for these categories. |
| **filters**  list / elements=dictionary | FortiGuard filters. |
| **action**  string | Action to take for matches.  Choices:   - `"block"` - `"authenticate"` - `"monitor"` - `"warning"` |
| **auth_usr_grp**  list / elements=dictionary | Groups with permission to authenticate. |
| **name**  string | User group name. Source user.group.name. |
| **category**  integer | Categories and groups the filter examines. |
| **id**  integer | ID number. |
| **log**  string | Enable/disable logging.  Choices:   - `"enable"` - `"disable"` |
| **override_replacemsg**  string | Override replacement message. |
| **warn_duration**  string | Duration of warnings. |
| **warning_duration_type**  string | Re-display warning after closing browser or after a timeout.  Choices:   - `"session"` - `"timeout"` |
| **warning_prompt**  string | Warning prompts in each category or each domain.  Choices:   - `"per-domain"` - `"per-category"` |
| **max_quota_timeout**  integer | Maximum FortiGuard quota used by single page view in seconds (excludes streams). |
| **options**  list / elements=string | Options for FortiGuard Web Filter.  Choices:   - `"error-allow"` - `"rate-server-ip"` - `"connect-request-bypass"` - `"ftgd-disable"` |
| **ovrd**  list / elements=string | Allow web filter profile overrides. |
| **quota**  list / elements=dictionary | FortiGuard traffic quota settings. |
| **category**  list / elements=string | FortiGuard categories to apply quota to (category action must be set to monitor). |
| **duration**  string | Duration of quota. |
| **id**  integer | ID number. |
| **override_replacemsg**  string | Override replacement message. |
| **type**  string | Quota type.  Choices:   - `"time"` - `"traffic"` |
| **unit**  string | Traffic quota unit of measurement.  Choices:   - `"B"` - `"KB"` - `"MB"` - `"GB"` |
| **value**  integer | Traffic quota value. |
| **rate_crl_urls**  string | Enable/disable rating CRL by URL.  Choices:   - `"disable"` - `"enable"` |
| **rate_css_urls**  string | Enable/disable rating CSS by URL.  Choices:   - `"disable"` - `"enable"` |
| **rate_image_urls**  string | Enable/disable rating images by URL.  Choices:   - `"disable"` - `"enable"` |
| **rate_javascript_urls**  string | Enable/disable rating JavaScript by URL.  Choices:   - `"disable"` - `"enable"` |
| **https_replacemsg**  string | Enable replacement messages for HTTPS.  Choices:   - `"enable"` - `"disable"` |
| **inspection_mode**  string | Web filtering inspection mode.  Choices:   - `"proxy"` - `"flow-based"` |
| **log_all_url**  string | Enable/disable logging all URLs visited.  Choices:   - `"enable"` - `"disable"` |
| **name**  string / required | Profile name. |
| **options**  list / elements=string | Options.  Choices:   - `"activexfilter"` - `"cookiefilter"` - `"javafilter"` - `"block-invalid-url"` - `"jscript"` - `"js"` - `"vbs"` - `"unknown"` - `"intrinsic"` - `"wf-referer"` - `"wf-cookie"` - `"per-user-bal"` - `"per-user-bwl"` |
| **override**  dictionary | Web Filter override settings. |
| **ovrd_cookie**  string | Allow/deny browser-based (cookie) overrides.  Choices:   - `"allow"` - `"deny"` |
| **ovrd_dur**  string | Override duration. |
| **ovrd_dur_mode**  string | Override duration mode.  Choices:   - `"constant"` - `"ask"` |
| **ovrd_scope**  string | Override scope.  Choices:   - `"user"` - `"user-group"` - `"ip"` - `"browser"` - `"ask"` |
| **ovrd_user_group**  list / elements=dictionary | User groups with permission to use the override. |
| **name**  string | User group name. Source user.group.name. |
| **profile**  list / elements=dictionary | Web filter profile with permission to create overrides. |
| **name**  string | Web profile. Source webfilter.profile.name. |
| **profile_attribute**  string | Profile attribute to retrieve from the RADIUS server.  Choices:   - `"User-Name"` - `"NAS-IP-Address"` - `"Framed-IP-Address"` - `"Framed-IP-Netmask"` - `"Filter-Id"` - `"Login-IP-Host"` - `"Reply-Message"` - `"Callback-Number"` - `"Callback-Id"` - `"Framed-Route"` - `"Framed-IPX-Network"` - `"Class"` - `"Called-Station-Id"` - `"Calling-Station-Id"` - `"NAS-Identifier"` - `"Proxy-State"` - `"Login-LAT-Service"` - `"Login-LAT-Node"` - `"Login-LAT-Group"` - `"Framed-AppleTalk-Zone"` - `"Acct-Session-Id"` - `"Acct-Multi-Session-Id"` |
| **profile_type**  string | Override profile type.  Choices:   - `"list"` - `"radius"` |
| **ovrd_perm**  list / elements=string | Permitted override types.  Choices:   - `"bannedword-override"` - `"urlfilter-override"` - `"fortiguard-wf-override"` - `"contenttype-check-override"` |
| **post_action**  string | Action taken for HTTP POST traffic.  Choices:   - `"normal"` - `"block"` |
| **replacemsg_group**  string | Replacement message group. Source system.replacemsg-group.name. |
| **url_extraction**  dictionary | Configure URL Extraction |
| **redirect_header**  string | HTTP header name to use for client redirect on blocked requests |
| **redirect_no_content**  string | Enable / Disable empty message-body entity in HTTP response  Choices:   - `"enable"` - `"disable"` |
| **redirect_url**  string | HTTP header value to use for client redirect on blocked requests |
| **server_fqdn**  string | URL extraction server FQDN (fully qualified domain name) |
| **status**  string | Enable URL Extraction  Choices:   - `"enable"` - `"disable"` |
| **web**  dictionary | Web content filtering settings. |
| **allowlist**  list / elements=string | FortiGuard allowlist settings.  Choices:   - `"exempt-av"` - `"exempt-webcontent"` - `"exempt-activex-java-cookie"` - `"exempt-dlp"` - `"exempt-rangeblock"` - `"extended-log-others"` |
| **blacklist**  string | Enable/disable automatic addition of URLs detected by FortiSandbox to blacklist.  Choices:   - `"enable"` - `"disable"` |
| **blocklist**  string | Enable/disable automatic addition of URLs detected by FortiSandbox to blocklist.  Choices:   - `"enable"` - `"disable"` |
| **bword_table**  integer | Banned word table ID. Source webfilter.content.id. |
| **bword_threshold**  integer | Banned word score threshold. |
| **content_header_list**  integer | Content header list. Source webfilter.content-header.id. |
| **keyword_match**  list / elements=dictionary | Search keywords to log when match is found. |
| **pattern**  string | Pattern/keyword to search for. |
| **log_search**  string | Enable/disable logging all search phrases.  Choices:   - `"enable"` - `"disable"` |
| **safe_search**  list / elements=string | Safe search type.  Choices:   - `"url"` - `"header"` |
| **urlfilter_table**  integer | URL filter table ID. Source webfilter.urlfilter.id. |
| **vimeo_restrict**  string | Set Vimeo-restrict (“7” = don”t show mature content, “134” = don”t show unrated and mature content). A value of cookie “content_rating”. |
| **whitelist**  list / elements=string | FortiGuard whitelist settings.  Choices:   - `"exempt-av"` - `"exempt-webcontent"` - `"exempt-activex-java-cookie"` - `"exempt-dlp"` - `"exempt-rangeblock"` - `"extended-log-others"` |
| **youtube_restrict**  string | YouTube EDU filter level.  Choices:   - `"none"` - `"strict"` - `"moderate"` |
| **web_antiphishing_log**  string | Enable/disable logging of AntiPhishing checks.  Choices:   - `"enable"` - `"disable"` |
| **web_content_log**  string | Enable/disable logging logging blocked web content.  Choices:   - `"enable"` - `"disable"` |
| **web_extended_all_action_log**  string | Enable/disable extended any filter action logging for web filtering.  Choices:   - `"enable"` - `"disable"` |
| **web_filter_activex_log**  string | Enable/disable logging ActiveX.  Choices:   - `"enable"` - `"disable"` |
| **web_filter_applet_log**  string | Enable/disable logging Java applets.  Choices:   - `"enable"` - `"disable"` |
| **web_filter_command_block_log**  string | Enable/disable logging blocked commands.  Choices:   - `"enable"` - `"disable"` |
| **web_filter_cookie_log**  string | Enable/disable logging cookie filtering.  Choices:   - `"enable"` - `"disable"` |
| **web_filter_cookie_removal_log**  string | Enable/disable logging blocked cookies.  Choices:   - `"enable"` - `"disable"` |
| **web_filter_js_log**  string | Enable/disable logging Java scripts.  Choices:   - `"enable"` - `"disable"` |
| **web_filter_jscript_log**  string | Enable/disable logging JScripts.  Choices:   - `"enable"` - `"disable"` |
| **web_filter_referer_log**  string | Enable/disable logging referrers.  Choices:   - `"enable"` - `"disable"` |
| **web_filter_unknown_log**  string | Enable/disable logging unknown scripts.  Choices:   - `"enable"` - `"disable"` |
| **web_filter_vbs_log**  string | Enable/disable logging VBS scripts.  Choices:   - `"enable"` - `"disable"` |
| **web_ftgd_err_log**  string | Enable/disable logging rating errors.  Choices:   - `"enable"` - `"disable"` |
| **web_ftgd_quota_usage**  string | Enable/disable logging daily quota usage.  Choices:   - `"enable"` - `"disable"` |
| **web_invalid_domain_log**  string | Enable/disable logging invalid domain names.  Choices:   - `"enable"` - `"disable"` |
| **web_url_log**  string | Enable/disable logging URL filtering.  Choices:   - `"enable"` - `"disable"` |
| **wisp**  string | Enable/disable web proxy WISP.  Choices:   - `"enable"` - `"disable"` |
| **wisp_algorithm**  string | WISP server selection algorithm.  Choices:   - `"primary-secondary"` - `"round-robin"` - `"auto-learning"` |
| **wisp_servers**  list / elements=dictionary | WISP servers. |
| **name**  string | Server name. Source web-proxy.wisp.name. |
| **youtube_channel_filter**  list / elements=dictionary | YouTube channel filter. |
| **channel_id**  string | YouTube channel ID to be filtered. |
| **comment**  string | Comment. |
| **id**  integer | ID. |
| **youtube_channel_status**  string | YouTube channel filter status.  Choices:   - `"disable"` - `"blacklist"` - `"whitelist"` |

## [Notes](fortios_webfilter_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_webfilter_profile_module.md#id5)

```yaml+jinja
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Configure Web filter profiles.
    fortios_webfilter_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      webfilter_profile:
        antiphish:
            authentication: "domain-controller"
            check_basic_auth: "enable"
            check_uri: "enable"
            check_username_only: "enable"
            custom_patterns:
             -
                category: "username"
                pattern: "<your_own_value>"
                type: "regex"
            default_action: "exempt"
            domain_controller: "<your_own_value> (source user.domain-controller.name credential-store.domain-controller.server-name)"
            inspection_entries:
             -
                action: "exempt"
                fortiguard_category: "<your_own_value>"
                name: "default_name_17"
            ldap: "<your_own_value> (source user.ldap.name)"
            max_body_len: "65536"
            status: "enable"
        comment: "Optional comments."
        extended_log: "enable"
        feature_set: "flow"
        file_filter:
            entries:
             -
                action: "log"
                comment: "Comment."
                direction: "incoming"
                file_type:
                 -
                    name: "default_name_30 (source antivirus.filetype.name)"
                filter: "<your_own_value>"
                password_protected: "yes"
                protocol: "http"
            log: "enable"
            scan_archive_contents: "enable"
            status: "enable"
        ftgd_wf:
            exempt_quota: "<your_own_value>"
            filters:
             -
                action: "block"
                auth_usr_grp:
                 -
                    name: "default_name_42 (source user.group.name)"
                category: "0"
                id:  "44"
                log: "enable"
                override_replacemsg: "<your_own_value>"
                warn_duration: "<your_own_value>"
                warning_duration_type: "session"
                warning_prompt: "per-domain"
            max_quota_timeout: "300"
            options: "error-allow"
            ovrd: "<your_own_value>"
            quota:
             -
                category: "<your_own_value>"
                duration: "<your_own_value>"
                id:  "56"
                override_replacemsg: "<your_own_value>"
                type: "time"
                unit: "B"
                value: "1024"
            rate_crl_urls: "disable"
            rate_css_urls: "disable"
            rate_image_urls: "disable"
            rate_javascript_urls: "disable"
        https_replacemsg: "enable"
        inspection_mode: "proxy"
        log_all_url: "enable"
        name: "default_name_68"
        options: "activexfilter"
        override:
            ovrd_cookie: "allow"
            ovrd_dur: "<your_own_value>"
            ovrd_dur_mode: "constant"
            ovrd_scope: "user"
            ovrd_user_group:
             -
                name: "default_name_76 (source user.group.name)"
            profile:
             -
                name: "default_name_78 (source webfilter.profile.name)"
            profile_attribute: "User-Name"
            profile_type: "list"
        ovrd_perm: "bannedword-override"
        post_action: "normal"
        replacemsg_group: "<your_own_value> (source system.replacemsg-group.name)"
        url_extraction:
            redirect_header: "<your_own_value>"
            redirect_no_content: "enable"
            redirect_url: "<your_own_value>"
            server_fqdn: "<your_own_value>"
            status: "enable"
        web:
            allowlist: "exempt-av"
            blacklist: "enable"
            blocklist: "enable"
            bword_table: "0"
            bword_threshold: "10"
            content_header_list: "0"
            keyword_match:
             -
                pattern: "<your_own_value>"
            log_search: "enable"
            safe_search: "url"
            urlfilter_table: "0"
            vimeo_restrict: "<your_own_value>"
            whitelist: "exempt-av"
            youtube_restrict: "none"
        web_antiphishing_log: "enable"
        web_content_log: "enable"
        web_extended_all_action_log: "enable"
        web_filter_activex_log: "enable"
        web_filter_applet_log: "enable"
        web_filter_command_block_log: "enable"
        web_filter_cookie_log: "enable"
        web_filter_cookie_removal_log: "enable"
        web_filter_js_log: "enable"
        web_filter_jscript_log: "enable"
        web_filter_referer_log: "enable"
        web_filter_unknown_log: "enable"
        web_filter_vbs_log: "enable"
        web_ftgd_err_log: "enable"
        web_ftgd_quota_usage: "enable"
        web_invalid_domain_log: "enable"
        web_url_log: "enable"
        wisp: "enable"
        wisp_algorithm: "primary-secondary"
        wisp_servers:
         -
            name: "default_name_125 (source web-proxy.wisp.name)"
        youtube_channel_filter:
         -
            channel_id: "<your_own_value>"
            comment: "Comment."
            id:  "129"
        youtube_channel_status: "disable"
```

## [Return Values](fortios_webfilter_profile_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  Returned: always  Sample: `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  Returned: always  Sample: `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  Returned: always  Sample: `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  Returned: success  Sample: `"id"` |
| **name**  string | Name of the table used to fulfill the request  Returned: always  Sample: `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  Returned: always  Sample: `"webfilter"` |
| **revision**  string | Internal revision number  Returned: always  Sample: `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  Returned: always  Sample: `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  Returned: always  Sample: `"success"` |
| **vdom**  string | Virtual domain used  Returned: always  Sample: `"root"` |
| **version**  string | Version of the FortiGate  Returned: always  Sample: `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
[Homepage](https://www.fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
