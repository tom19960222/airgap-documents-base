---
collection: ansible
version: "8"
title: "community.fortios.fmgr_secprof_web module – Manage web filter security profiles in FortiManager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/fortios/fmgr_secprof_web_module.html
fetched_at: 2026-07-28T01:44:27+00:00
---
# community.fortios.fmgr_secprof_web module – Manage web filter security profiles in FortiManager

> **Note:**
>
> This module is part of the [community.fortios collection](https://galaxy.ansible.com/ui/repo/published/community/fortios/) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.fortios`.
>
> To use it in a playbook, specify: `community.fortios.fmgr_secprof_web`.

- [Synopsis](fmgr_secprof_web_module.md#synopsis)
- [Parameters](fmgr_secprof_web_module.md#parameters)
- [Notes](fmgr_secprof_web_module.md#notes)
- [Examples](fmgr_secprof_web_module.md#examples)
- [Return Values](fmgr_secprof_web_module.md#return-values)

## [Synopsis](fmgr_secprof_web_module.md#id1)

- Manage web filter security profiles in FortiManager through playbooks using the FMG API

## [Parameters](fmgr_secprof_web_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string | The ADOM the configuration should belong to.  **Default:** `"root"` |
| **comment**  string | Optional comments. |
| **extended_log**  string | Enable/disable extended logging for web filtering.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **ftgd_wf**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **ftgd_wf_exempt_quota**  string | Do not stop quota for these categories. |
| **ftgd_wf_filters_action**  string | Action to take for matches.  choice | block | Block access.  choice | monitor | Allow access while logging the action.  choice | warning | Allow access after warning the user.  choice | authenticate | Authenticate user before allowing access.  **Choices:**   - `"block"` - `"monitor"` - `"warning"` - `"authenticate"` |
| **ftgd_wf_filters_auth_usr_grp**  string | Groups with permission to authenticate. |
| **ftgd_wf_filters_category**  string | Categories and groups the filter examines. |
| **ftgd_wf_filters_log**  string | Enable/disable logging.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **ftgd_wf_filters_override_replacemsg**  string | Override replacement message. |
| **ftgd_wf_filters_warn_duration**  string | Duration of warnings. |
| **ftgd_wf_filters_warning_duration_type**  string | Re-display warning after closing browser or after a timeout.  choice | session | After session ends.  choice | timeout | After timeout occurs.  **Choices:**   - `"session"` - `"timeout"` |
| **ftgd_wf_filters_warning_prompt**  string | Warning prompts in each category or each domain.  choice | per-domain | Per-domain warnings.  choice | per-category | Per-category warnings.  **Choices:**   - `"per-domain"` - `"per-category"` |
| **ftgd_wf_max_quota_timeout**  string | Maximum FortiGuard quota used by single page view in seconds (excludes streams). |
| **ftgd_wf_options**  string | Options for FortiGuard Web Filter.  FLAG Based Options. Specify multiple in list form.  flag | error-allow | Allow web pages with a rating error to pass through.  flag | rate-server-ip | Rate the server IP in addition to the domain name.  flag | connect-request-bypass | Bypass connection which has CONNECT request.  flag | ftgd-disable | Disable FortiGuard scanning.  **Choices:**   - `"error-allow"` - `"rate-server-ip"` - `"connect-request-bypass"` - `"ftgd-disable"` |
| **ftgd_wf_ovrd**  string | Allow web filter profile overrides. |
| **ftgd_wf_quota_category**  string | FortiGuard categories to apply quota to (category action must be set to monitor). |
| **ftgd_wf_quota_duration**  string | Duration of quota. |
| **ftgd_wf_quota_override_replacemsg**  string | Override replacement message. |
| **ftgd_wf_quota_type**  string | Quota type.  choice | time | Use a time-based quota.  choice | traffic | Use a traffic-based quota.  **Choices:**   - `"time"` - `"traffic"` |
| **ftgd_wf_quota_unit**  string | Traffic quota unit of measurement.  choice | B | Quota in bytes.  choice | KB | Quota in kilobytes.  choice | MB | Quota in megabytes.  choice | GB | Quota in gigabytes.  **Choices:**   - `"B"` - `"KB"` - `"MB"` - `"GB"` |
| **ftgd_wf_quota_value**  string | Traffic quota value. |
| **ftgd_wf_rate_crl_urls**  string | Enable/disable rating CRL by URL.  choice | disable | Disable rating CRL by URL.  choice | enable | Enable rating CRL by URL.  **Choices:**   - `"disable"` - `"enable"` |
| **ftgd_wf_rate_css_urls**  string | Enable/disable rating CSS by URL.  choice | disable | Disable rating CSS by URL.  choice | enable | Enable rating CSS by URL.  **Choices:**   - `"disable"` - `"enable"` |
| **ftgd_wf_rate_image_urls**  string | Enable/disable rating images by URL.  choice | disable | Disable rating images by URL (blocked images are replaced with blanks).  choice | enable | Enable rating images by URL (blocked images are replaced with blanks).  **Choices:**   - `"disable"` - `"enable"` |
| **ftgd_wf_rate_javascript_urls**  string | Enable/disable rating JavaScript by URL.  choice | disable | Disable rating JavaScript by URL.  choice | enable | Enable rating JavaScript by URL.  **Choices:**   - `"disable"` - `"enable"` |
| **https_replacemsg**  string | Enable replacement messages for HTTPS.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **inspection_mode**  string | Web filtering inspection mode.  choice | proxy | Proxy.  choice | flow-based | Flow based.  **Choices:**   - `"proxy"` - `"flow-based"` |
| **log_all_url**  string | Enable/disable logging all URLs visited.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **mode**  string | Sets one of three modes for managing the object.  Allows use of soft-adds instead of overwriting existing values  **Choices:**   - `"add"` ← (default) - `"set"` - `"delete"` - `"update"` |
| **name**  string | Profile name. |
| **options**  string | FLAG Based Options. Specify multiple in list form.  flag | block-invalid-url | Block sessions contained an invalid domain name.  flag | jscript | Javascript block.  flag | js | JS block.  flag | vbs | VB script block.  flag | unknown | Unknown script block.  flag | wf-referer | Referring block.  flag | intrinsic | Intrinsic script block.  flag | wf-cookie | Cookie block.  flag | per-user-bwl | Per-user black/white list filter  flag | activexfilter | ActiveX filter.  flag | cookiefilter | Cookie filter.  flag | javafilter | Java applet filter.  **Choices:**   - `"block-invalid-url"` - `"jscript"` - `"js"` - `"vbs"` - `"unknown"` - `"wf-referer"` - `"intrinsic"` - `"wf-cookie"` - `"per-user-bwl"` - `"activexfilter"` - `"cookiefilter"` - `"javafilter"` |
| **override**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **override_ovrd_cookie**  string | Allow/deny browser-based (cookie) overrides.  choice | deny | Deny browser-based (cookie) override.  choice | allow | Allow browser-based (cookie) override.  **Choices:**   - `"deny"` - `"allow"` |
| **override_ovrd_dur**  string | Override duration. |
| **override_ovrd_dur_mode**  string | Override duration mode.  choice | constant | Constant mode.  choice | ask | Prompt for duration when initiating an override.  **Choices:**   - `"constant"` - `"ask"` |
| **override_ovrd_scope**  string | Override scope.  choice | user | Override for the user.  choice | user-group | Override for the user’s group.  choice | ip | Override for the initiating IP.  choice | ask | Prompt for scope when initiating an override.  choice | browser | Create browser-based (cookie) override.  **Choices:**   - `"user"` - `"user-group"` - `"ip"` - `"ask"` - `"browser"` |
| **override_ovrd_user_group**  string | User groups with permission to use the override. |
| **override_profile**  string | Web filter profile with permission to create overrides. |
| **override_profile_attribute**  string | Profile attribute to retrieve from the RADIUS server.  choice | User-Name | Use this attribute.  choice | NAS-IP-Address | Use this attribute.  choice | Framed-IP-Address | Use this attribute.  choice | Framed-IP-Netmask | Use this attribute.  choice | Filter-Id | Use this attribute.  choice | Login-IP-Host | Use this attribute.  choice | Reply-Message | Use this attribute.  choice | Callback-Number | Use this attribute.  choice | Callback-Id | Use this attribute.  choice | Framed-Route | Use this attribute.  choice | Framed-IPX-Network | Use this attribute.  choice | Class | Use this attribute.  choice | Called-Station-Id | Use this attribute.  choice | Calling-Station-Id | Use this attribute.  choice | NAS-Identifier | Use this attribute.  choice | Proxy-State | Use this attribute.  choice | Login-LAT-Service | Use this attribute.  choice | Login-LAT-Node | Use this attribute.  choice | Login-LAT-Group | Use this attribute.  choice | Framed-AppleTalk-Zone | Use this attribute.  choice | Acct-Session-Id | Use this attribute.  choice | Acct-Multi-Session-Id | Use this attribute.  **Choices:**   - `"User-Name"` - `"NAS-IP-Address"` - `"Framed-IP-Address"` - `"Framed-IP-Netmask"` - `"Filter-Id"` - `"Login-IP-Host"` - `"Reply-Message"` - `"Callback-Number"` - `"Callback-Id"` - `"Framed-Route"` - `"Framed-IPX-Network"` - `"Class"` - `"Called-Station-Id"` - `"Calling-Station-Id"` - `"NAS-Identifier"` - `"Proxy-State"` - `"Login-LAT-Service"` - `"Login-LAT-Node"` - `"Login-LAT-Group"` - `"Framed-AppleTalk-Zone"` - `"Acct-Session-Id"` - `"Acct-Multi-Session-Id"` |
| **override_profile_type**  string | Override profile type.  choice | list | Profile chosen from list.  choice | radius | Profile determined by RADIUS server.  **Choices:**   - `"list"` - `"radius"` |
| **ovrd_perm**  string | FLAG Based Options. Specify multiple in list form.  flag | bannedword-override | Banned word override.  flag | urlfilter-override | URL filter override.  flag | fortiguard-wf-override | FortiGuard Web Filter override.  flag | contenttype-check-override | Content-type header override.  **Choices:**   - `"bannedword-override"` - `"urlfilter-override"` - `"fortiguard-wf-override"` - `"contenttype-check-override"` |
| **post_action**  string | Action taken for HTTP POST traffic.  choice | normal | Normal, POST requests are allowed.  choice | block | POST requests are blocked.  **Choices:**   - `"normal"` - `"block"` |
| **replacemsg_group**  string | Replacement message group. |
| **url_extraction**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **url_extraction_redirect_header**  string | HTTP header name to use for client redirect on blocked requests |
| **url_extraction_redirect_no_content**  string | Enable / Disable empty message-body entity in HTTP response  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **url_extraction_redirect_url**  string | HTTP header value to use for client redirect on blocked requests |
| **url_extraction_server_fqdn**  string | URL extraction server FQDN (fully qualified domain name) |
| **url_extraction_status**  string | Enable URL Extraction  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **web**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **web_blacklist**  string | Enable/disable automatic addition of URLs detected by FortiSandbox to blacklist.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **web_bword_table**  string | Banned word table ID. |
| **web_bword_threshold**  string | Banned word score threshold. |
| **web_content_header_list**  string | Content header list. |
| **web_content_log**  string | Enable/disable logging logging blocked web content.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **web_extended_all_action_log**  string | Enable/disable extended any filter action logging for web filtering.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **web_filter_activex_log**  string | Enable/disable logging ActiveX.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **web_filter_applet_log**  string | Enable/disable logging Java applets.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **web_filter_command_block_log**  string | Enable/disable logging blocked commands.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **web_filter_cookie_log**  string | Enable/disable logging cookie filtering.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **web_filter_cookie_removal_log**  string | Enable/disable logging blocked cookies.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **web_filter_js_log**  string | Enable/disable logging Java scripts.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **web_filter_jscript_log**  string | Enable/disable logging JScripts.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **web_filter_referer_log**  string | Enable/disable logging referrers.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **web_filter_unknown_log**  string | Enable/disable logging unknown scripts.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **web_filter_vbs_log**  string | Enable/disable logging VBS scripts.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **web_ftgd_err_log**  string | Enable/disable logging rating errors.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **web_ftgd_quota_usage**  string | Enable/disable logging daily quota usage.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **web_invalid_domain_log**  string | Enable/disable logging invalid domain names.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **web_keyword_match**  string | Search keywords to log when match is found. |
| **web_log_search**  string | Enable/disable logging all search phrases.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **web_safe_search**  string | Safe search type.  FLAG Based Options. Specify multiple in list form.  flag | url | Insert safe search string into URL.  flag | header | Insert safe search header.  **Choices:**   - `"url"` - `"header"` |
| **web_url_log**  string | Enable/disable logging URL filtering.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **web_urlfilter_table**  string | URL filter table ID. |
| **web_whitelist**  string | FortiGuard whitelist settings.  FLAG Based Options. Specify multiple in list form.  flag | exempt-av | Exempt antivirus.  flag | exempt-webcontent | Exempt web content.  flag | exempt-activex-java-cookie | Exempt ActiveX-JAVA-Cookie.  flag | exempt-dlp | Exempt DLP.  flag | exempt-rangeblock | Exempt RangeBlock.  flag | extended-log-others | Support extended log.  **Choices:**   - `"exempt-av"` - `"exempt-webcontent"` - `"exempt-activex-java-cookie"` - `"exempt-dlp"` - `"exempt-rangeblock"` - `"extended-log-others"` |
| **web_youtube_restrict**  string | YouTube EDU filter level.  choice | strict | Strict access for YouTube.  choice | none | Full access for YouTube.  choice | moderate | Moderate access for YouTube.  **Choices:**   - `"strict"` - `"none"` - `"moderate"` |
| **wisp**  string | Enable/disable web proxy WISP.  choice | disable | Disable web proxy WISP.  choice | enable | Enable web proxy WISP.  **Choices:**   - `"disable"` - `"enable"` |
| **wisp_algorithm**  string | WISP server selection algorithm.  choice | auto-learning | Select the lightest loading healthy server.  choice | primary-secondary | Select the first healthy server in order.  choice | round-robin | Select the next healthy server.  **Choices:**   - `"auto-learning"` - `"primary-secondary"` - `"round-robin"` |
| **wisp_servers**  string | WISP servers. |
| **youtube_channel_filter**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **youtube_channel_filter_channel_id**  string | YouTube channel ID to be filtered. |
| **youtube_channel_filter_comment**  string | Comment. |
| **youtube_channel_status**  string | YouTube channel filter status.  choice | disable | Disable YouTube channel filter.  choice | blacklist | Block matches.  choice | whitelist | Allow matches.  **Choices:**   - `"disable"` - `"blacklist"` - `"whitelist"` |

## [Notes](fmgr_secprof_web_module.md#id3)

> **Note:**
>
> - Full Documentation at <https://ftnt-ansible-docs.readthedocs.io/en/latest/>.

## [Examples](fmgr_secprof_web_module.md#id4)

```yaml+jinja
- name: DELETE Profile
  community.fortios.fmgr_secprof_web:
    name: "Ansible_Web_Filter_Profile"
    mode: "delete"

- name: CREATE Profile
  community.fortios.fmgr_secprof_web:
    name: "Ansible_Web_Filter_Profile"
    comment: "Created by Ansible Module TEST"
    mode: "set"
    extended_log: "enable"
    inspection_mode: "proxy"
    log_all_url: "enable"
    options: "js"
    ovrd_perm: "bannedword-override"
    post_action: "block"
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
    wisp_algorithm: "auto-learning"
    youtube_channel_status: "blacklist"
```

## [Return Values](fmgr_secprof_web_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  **Returned:** always |

### Authors

- Luke Weighall (@lweighall)
- Andrew Welsh (@Ghilli3)
- Jim Huber (@p4r4n0y1ng)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.fortios)
