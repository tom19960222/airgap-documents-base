---
collection: ansible
version: "6"
title: "cisco.meraki.meraki_mr_ssid module – Manage wireless SSIDs in the Meraki cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/meraki/meraki_mr_ssid_module.html
fetched_at: 2026-07-27T17:00:25+00:00
---
# cisco.meraki.meraki_mr_ssid module – Manage wireless SSIDs in the Meraki cloud

> **Note:**
>
> This module is part of the [cisco.meraki collection](https://galaxy.ansible.com/cisco/meraki) (version 2.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.meraki`.
>
> To use it in a playbook, specify: `cisco.meraki.meraki_mr_ssid`.

- [Synopsis](meraki_mr_ssid_module.md#synopsis)
- [Parameters](meraki_mr_ssid_module.md#parameters)
- [Notes](meraki_mr_ssid_module.md#notes)
- [Examples](meraki_mr_ssid_module.md#examples)
- [Return Values](meraki_mr_ssid_module.md#return-values)

## [Synopsis](meraki_mr_ssid_module.md#id1)

- Allows for management of SSIDs in a Meraki wireless environment.

## [Parameters](meraki_mr_ssid_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **ap_availability_tags**  list / elements=string | Set whether SSID will be broadcast by APs with tags matching any of the tags in this list.  Requires `available_on_all_aps` to be `false`. |
| **ap_tags_vlan_ids**  list / elements=dictionary | List of VLAN tags.  Requires `ip_assignment_mode` to be `Bridge mode` or `Layer 3 roaming`.  Requires `use_vlan_tagging` to be `True`. |
| **tags**  list / elements=string | List of AP tags. |
| **vlan_id**  integer | Numerical identifier that is assigned to the VLAN. |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **auth_mode**  string | Set authentication mode of network.  Choices:   - `"open"` - `"psk"` - `"open-with-radius"` - `"8021x-meraki"` - `"8021x-radius"` |
| **available_on_all_aps**  boolean | Set whether all APs should broadcast the SSID or if it should be restricted to APs matching any availability tags.  Requires `ap_availability_tags` to be defined when set to `False`.  Choices:   - `false` - `true` |
| **band_selection**  string | Set band selection mode.  Choices:   - `"Dual band operation"` - `"5 GHz band only"` - `"Dual band operation with Band Steering"` |
| **concentrator_network_id**  string | The concentrator to use for ‘Layer 3 roaming with a concentrator’ or ‘VPN’. |
| **default_vlan_id**  integer | Default VLAN ID.  Requires `ip_assignment_mode` to be `Bridge mode` or `Layer 3 roaming`. |
| **enabled**  boolean | Enable or disable SSID network.  Choices:   - `false` - `true` |
| **encryption_mode**  string | Set encryption mode of network.  Choices:   - `"wpa"` - `"eap"` - `"wpa-eap"` |
| **enterprise_admin_access**  string | Whether SSID is accessible by enterprise administrators.  Choices:   - `"access disabled"` - `"access enabled"` |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  Default: `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  Default: `60` |
| **ip_assignment_mode**  string | Method of which SSID uses to assign IP addresses.  Choices:   - `"NAT mode"` - `"Bridge mode"` - `"Layer 3 roaming"` - `"Layer 3 roaming with a concentrator"` - `"VPN"` |
| **lan_isolation_enabled**  boolean | Enable or disable Layer 2 Lan isolation.  Requires `ip_assignment_mode` to be `Bridge mode`.  Choices:   - `false` - `true` |
| **min_bitrate**  float | Minimum bitrate (Mbps) allowed on SSID.  Choices:   - `1.0` - `2.0` - `5.5` - `6.0` - `9.0` - `11.0` - `12.0` - `18.0` - `24.0` - `36.0` - `48.0` - `54.0` |
| **name**  string | Name of SSID. |
| **net_id**  string | ID of network. |
| **net_name**  string | Name of network. |
| **number**  aliases: ssid_number  integer | SSID number within network. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  Choices:   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  Choices:   - `"debug"` - `"normal"` ← (default) |
| **per_client_bandwidth_limit_down**  integer | Maximum bandwidth in Mbps devices on SSID can download. |
| **per_client_bandwidth_limit_up**  integer | Maximum bandwidth in Mbps devices on SSID can upload. |
| **psk**  string | Password for wireless network.  Requires auth_mode to be set to psk. |
| **radius_accounting_enabled**  boolean | Enable or disable RADIUS accounting.  Choices:   - `false` - `true` |
| **radius_accounting_servers**  list / elements=dictionary | List of RADIUS servers for RADIUS accounting. |
| **host**  string / required | IP address or hostname of RADIUS server. |
| **port**  integer | Port number RADIUS server is listening to. |
| **secret**  string | RADIUS password.  Setting password is not idempotent. |
| **radius_coa_enabled**  boolean | Enable or disable RADIUS CoA (Change of Authorization) on SSID.  Choices:   - `false` - `true` |
| **radius_failover_policy**  string | Set client access policy in case RADIUS servers aren’t available.  Choices:   - `"Deny access"` - `"Allow access"` |
| **radius_load_balancing_policy**  string | Set load balancing policy when multiple RADIUS servers are specified.  Choices:   - `"Strict priority order"` - `"Round robin"` |
| **radius_proxy_enabled**  boolean | Enable or disable RADIUS Proxy on SSID.  Choices:   - `false` - `true` |
| **radius_servers**  list / elements=dictionary | List of RADIUS servers. |
| **host**  string / required | IP address or hostname of RADIUS server. |
| **port**  integer | Port number RADIUS server is listening to. |
| **secret**  string | RADIUS password.  Setting password is not idempotent. |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  Default: `165` |
| **splash_guest_sponsor_domains**  list / elements=string | List of valid sponsor email domains for sponsored guest portal. |
| **splash_page**  string | Set to enable splash page and specify type of splash.  Choices:   - `"None"` - `"Click-through splash page"` - `"Billing"` - `"Password-protected with Meraki RADIUS"` - `"Password-protected with custom RADIUS"` - `"Password-protected with Active Directory"` - `"Password-protected with LDAP"` - `"SMS authentication"` - `"Systems Manager Sentry"` - `"Facebook Wi-Fi"` - `"Google OAuth"` - `"Sponsored guest"` - `"Cisco ISE"` |
| **state**  string | Specifies whether SNMP information should be queried or modified.  Choices:   - `"absent"` - `"query"` - `"present"` ← (default) |
| **timeout**  integer | Time to timeout for HTTP requests.  Default: `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` ← (default) - `true` |
| **use_vlan_tagging**  boolean | Set whether to use VLAN tagging.  Requires `default_vlan_id` to be set.  Choices:   - `false` - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  Choices:   - `false` - `true` ← (default) |
| **visible**  boolean | Enable or disable whether APs should broadcast this SSID.  Choices:   - `false` - `true` |
| **vlan_id**  integer | ID number of VLAN on SSID.  Requires `ip_assignment_mode` to be `ayer 3 roaming with a concentrator` or `VPN`. |
| **walled_garden_enabled**  boolean | Enable or disable walled garden functionality.  Choices:   - `false` - `true` |
| **walled_garden_ranges**  list / elements=string | List of walled garden ranges. |
| **wpa_encryption_mode**  string | Encryption mode within WPA specification.  Choices:   - `"WPA1 and WPA2"` - `"WPA2 only"` - `"WPA3 Transition Mode"` - `"WPA3 only"` |

## [Notes](meraki_mr_ssid_module.md#id3)

> **Note:**
>
> - Deleting an SSID does not delete RADIUS servers.
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_mr_ssid_module.md#id4)

```yaml+jinja
- name: Enable and name SSID
  meraki_ssid:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_name: WiFi
    name: GuestSSID
    enabled: true
    visible: true
  delegate_to: localhost

- name: Set PSK with invalid encryption mode
  meraki_ssid:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_name: WiFi
    name: GuestSSID
    auth_mode: psk
    psk: abc1234
    encryption_mode: eap
  ignore_errors: yes
  delegate_to: localhost

- name: Configure RADIUS servers
  meraki_ssid:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_name: WiFi
    name: GuestSSID
    auth_mode: open-with-radius
    radius_servers:
      - host: 192.0.1.200
        port: 1234
        secret: abc98765
  delegate_to: localhost

- name: Enable click-through splash page
  meraki_ssid:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_name: WiFi
    name: GuestSSID
    splash_page: Click-through splash page
  delegate_to: localhost
```

## [Return Values](meraki_mr_ssid_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | List of wireless SSIDs.  Returned: success |
| **auth_mode**  string | Authentication method.  Returned: success  Sample: `"psk"` |
| **band_selection**  string | Wireless RF frequency wireless network will be broadcast on.  Returned: success  Sample: `"5 GHz band only"` |
| **enabled**  boolean | Enabled state of wireless network.  Returned: success  Sample: `true` |
| **encryption_mode**  string | Wireless traffic encryption method.  Returned: success  Sample: `"wpa"` |
| **ip_assignment_mode**  string | Wireless client IP assignment method.  Returned: success  Sample: `"NAT mode"` |
| **min_bitrate**  integer | Minimum bitrate a wireless client can connect at.  Returned: success  Sample: `11` |
| **name**  string | Name of wireless SSID.  This value is what is broadcasted.  Returned: success  Sample: `"CorpWireless"` |
| **number**  integer | Zero-based index number for SSIDs.  Returned: success  Sample: `0` |
| **per_client_bandwidth_limit_down**  integer | Maximum download bandwidth a client can use.  Returned: success  Sample: `0` |
| **per_client_bandwidth_limit_up**  integer | Maximum upload bandwidth a client can use.  Returned: success  Sample: `1000` |
| **psk**  string | Secret wireless password.  Returned: success  Sample: `"SecretWiFiPass"` |
| **splash_page**  string | Splash page to show when user authenticates.  Returned: success  Sample: `"Click-through splash page"` |
| **ssid_admin_accessible**  boolean | Whether SSID is administratively accessible.  Returned: success  Sample: `true` |
| **wpa_encryption_mode**  string | Enabled WPA versions.  Returned: success  Sample: `"WPA2 only"` |

### Authors

- Kevin Breit (@kbreit)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-meraki/issues)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-meraki)
