---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_pm_config_pblock_firewall_policy6 module – Configure IPv6 policies."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_pm_config_pblock_firewall_policy6_module.html
fetched_at: 2026-07-28T02:16:02+00:00
---
# fortinet.fortimanager.fmgr_pm_config_pblock_firewall_policy6 module – Configure IPv6 policies.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_pm_config_pblock_firewall_policy6`.

New in fortinet.fortimanager 2.2.0

- [Synopsis](fmgr_pm_config_pblock_firewall_policy6_module.md#synopsis)
- [Parameters](fmgr_pm_config_pblock_firewall_policy6_module.md#parameters)
- [Notes](fmgr_pm_config_pblock_firewall_policy6_module.md#notes)
- [Examples](fmgr_pm_config_pblock_firewall_policy6_module.md#examples)
- [Return Values](fmgr_pm_config_pblock_firewall_policy6_module.md#return-values)

## [Synopsis](fmgr_pm_config_pblock_firewall_policy6_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_pm_config_pblock_firewall_policy6_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **pblock**  string / required | the parameter (pblock) in requested url |
| **pm_config_pblock_firewall_policy6**  dictionary | the top level parameters set |
| **_policy_block**  integer | Assigned policy block. |
| **action**  string | Policy action  **Choices:**   - `"deny"` - `"accept"` - `"ipsec"` - `"ssl-vpn"` |
| **anti-replay**  string | Enable/disable anti-replay check.  **Choices:**   - `"disable"` - `"enable"` |
| **app-category**  any | (list) no description |
| **app-group**  any | (list) no description |
| **application**  any | (list) no description |
| **application-list**  string | Name of an existing Application list. |
| **auto-asic-offload**  string | Enable/disable policy traffic ASIC offloading.  **Choices:**   - `"disable"` - `"enable"` |
| **av-profile**  string | Name of an existing Antivirus profile. |
| **cgn-log-server-grp**  string | no description |
| **cifs-profile**  string | Name of an existing CIFS profile. |
| **comments**  string | Comment. |
| **custom-log-fields**  any | (list) no description |
| **devices**  any | (list) no description |
| **diffserv-forward**  string | Enable to change packets DiffServ values to the specified diffservcode-forward value.  **Choices:**   - `"disable"` - `"enable"` |
| **diffserv-reverse**  string | Enable to change packets reverse  **Choices:**   - `"disable"` - `"enable"` |
| **diffservcode-forward**  string | Change packets DiffServ to this value. |
| **diffservcode-rev**  string | Change packets reverse |
| **dlp-sensor**  string | Name of an existing DLP sensor. |
| **dnsfilter-profile**  string | Name of an existing DNS filter profile. |
| **dscp-match**  string | Enable DSCP check.  **Choices:**   - `"disable"` - `"enable"` |
| **dscp-negate**  string | Enable negated DSCP match.  **Choices:**   - `"disable"` - `"enable"` |
| **dscp-value**  string | DSCP value. |
| **dsri**  string | Enable DSRI to ignore HTTP server responses.  **Choices:**   - `"disable"` - `"enable"` |
| **dstaddr**  any | (list) no description |
| **dstaddr-negate**  string | When enabled dstaddr specifies what the destination address must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **dstintf**  any | (list) no description |
| **emailfilter-profile**  string | Name of an existing email filter profile. |
| **firewall-session-dirty**  string | How to handle sessions if the configuration of this firewall policy changes.  **Choices:**   - `"check-all"` - `"check-new"` |
| **fixedport**  string | Enable to prevent source NAT from changing a sessions source port.  **Choices:**   - `"disable"` - `"enable"` |
| **fsso-groups**  any | (list) no description |
| **global-label**  string | Label for the policy that appears when the GUI is in Global View mode. |
| **groups**  any | (list) no description |
| **http-policy-redirect**  string | Redirect HTTP  **Choices:**   - `"disable"` - `"enable"` |
| **icap-profile**  string | Name of an existing ICAP profile. |
| **inbound**  string | Policy-based IPsec VPN  **Choices:**   - `"disable"` - `"enable"` |
| **inspection-mode**  string | Policy inspection mode  **Choices:**   - `"proxy"` - `"flow"` |
| **ippool**  string | Enable to use IP Pools for source NAT.  **Choices:**   - `"disable"` - `"enable"` |
| **ips-sensor**  string | Name of an existing IPS sensor. |
| **label**  string | Label for the policy that appears when the GUI is in Section View mode. |
| **logtraffic**  string | Enable or disable logging.  **Choices:**   - `"disable"` - `"enable"` - `"all"` - `"utm"` |
| **logtraffic-start**  string | Record logs when a session starts.  **Choices:**   - `"disable"` - `"enable"` |
| **mms-profile**  string | Name of an existing MMS profile. |
| **name**  string / required | Policy name. |
| **nat**  string | Enable/disable source NAT.  **Choices:**   - `"disable"` - `"enable"` |
| **natinbound**  string | Policy-based IPsec VPN  **Choices:**   - `"disable"` - `"enable"` |
| **natoutbound**  string | Policy-based IPsec VPN  **Choices:**   - `"disable"` - `"enable"` |
| **np-acceleration**  string | Enable/disable UTM Network Processor acceleration.  **Choices:**   - `"disable"` - `"enable"` |
| **outbound**  string | Policy-based IPsec VPN  **Choices:**   - `"disable"` - `"enable"` |
| **per-ip-shaper**  string | Per-IP traffic shaper. |
| **policy-offload**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **policyid**  integer | Policy ID |
| **poolname**  any | (list) no description |
| **profile-group**  string | Name of profile group. |
| **profile-protocol-options**  string | Name of an existing Protocol options profile. |
| **profile-type**  string | Determine whether the firewall policy allows security profile groups or single profiles only.  **Choices:**   - `"single"` - `"group"` |
| **replacemsg-override-group**  string | Override the default replacement message group for this policy. |
| **rsso**  string | Enable/disable RADIUS single sign-on  **Choices:**   - `"disable"` - `"enable"` |
| **schedule**  string | Schedule name. |
| **send-deny-packet**  string | Enable/disable return of deny-packet.  **Choices:**   - `"disable"` - `"enable"` |
| **service**  any | (list) no description |
| **service-negate**  string | When enabled service specifies what the service must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **session-ttl**  string | Session TTL in seconds for sessions accepted by this policy. |
| **spamfilter-profile**  string | Name of an existing Spam filter profile. |
| **srcaddr**  any | (list) no description |
| **srcaddr-negate**  string | When enabled srcaddr specifies what the source address must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **srcintf**  any | (list) no description |
| **ssh-filter-profile**  string | Name of an existing SSH filter profile. |
| **ssh-policy-redirect**  string | Redirect SSH traffic to matching transparent proxy policy.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-mirror**  string | Enable to copy decrypted SSL traffic to a FortiGate interface  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-mirror-intf**  any | (list) no description |
| **ssl-ssh-profile**  string | Name of an existing SSL SSH profile. |
| **status**  string | Enable or disable this policy.  **Choices:**   - `"disable"` - `"enable"` |
| **tcp-mss-receiver**  integer | Receiver TCP maximum segment size |
| **tcp-mss-sender**  integer | Sender TCP maximum segment size |
| **tcp-session-without-syn**  string | Enable/disable creation of TCP session without SYN flag.  **Choices:**   - `"all"` - `"data-only"` - `"disable"` |
| **timeout-send-rst**  string | Enable/disable sending RST packets when TCP sessions expire.  **Choices:**   - `"disable"` - `"enable"` |
| **tos**  string | ToS |
| **tos-mask**  string | Non-zero bit positions are used for comparison while zero bit positions are ignored. |
| **tos-negate**  string | Enable negated TOS match.  **Choices:**   - `"disable"` - `"enable"` |
| **traffic-shaper**  string | Reverse traffic shaper. |
| **traffic-shaper-reverse**  string | Reverse traffic shaper. |
| **url-category**  any | (list) no description |
| **users**  any | (list) no description |
| **utm-status**  string | Enable AV/web/ips protection profile.  **Choices:**   - `"disable"` - `"enable"` |
| **uuid**  string | Universally Unique Identifier |
| **vlan-cos-fwd**  integer | VLAN forward direction user priority |
| **vlan-cos-rev**  integer | VLAN reverse direction user priority |
| **vlan-filter**  string | Set VLAN filters. |
| **voip-profile**  string | Name of an existing VoIP profile. |
| **vpntunnel**  string | Policy-based IPsec VPN |
| **waf-profile**  string | Name of an existing Web application firewall profile. |
| **webcache**  string | Enable/disable web cache.  **Choices:**   - `"disable"` - `"enable"` |
| **webcache-https**  string | Enable/disable web cache for HTTPS.  **Choices:**   - `"disable"` - `"enable"` |
| **webfilter-profile**  string | Name of an existing Web filter profile. |
| **webproxy-forward-server**  string | Web proxy forward server name. |
| **webproxy-profile**  string | Webproxy profile name. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_pm_config_pblock_firewall_policy6_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_pm_config_pblock_firewall_policy6_module.md#id4)

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
    - name: Configure IPv6 policies.
      fmgr_pm_config_pblock_firewall_policy6:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        pblock: <your own value>
        state: <value in [present, absent]>
        pm_config_pblock_firewall_policy6:
          _policy_block: <integer>
          action: <value in [deny, accept, ipsec, ...]>
          anti-replay: <value in [disable, enable]>
          app-category: <list or string>
          app-group: <list or string>
          application: <list or integer>
          application-list: <string>
          auto-asic-offload: <value in [disable, enable]>
          av-profile: <string>
          cgn-log-server-grp: <string>
          cifs-profile: <string>
          comments: <string>
          custom-log-fields: <list or string>
          diffserv-forward: <value in [disable, enable]>
          diffserv-reverse: <value in [disable, enable]>
          diffservcode-forward: <string>
          diffservcode-rev: <string>
          dlp-sensor: <string>
          dnsfilter-profile: <string>
          dsri: <value in [disable, enable]>
          dstaddr: <list or string>
          dstaddr-negate: <value in [disable, enable]>
          dstintf: <list or string>
          emailfilter-profile: <string>
          firewall-session-dirty: <value in [check-all, check-new]>
          fixedport: <value in [disable, enable]>
          fsso-groups: <list or string>
          global-label: <string>
          groups: <list or string>
          http-policy-redirect: <value in [disable, enable]>
          icap-profile: <string>
          inbound: <value in [disable, enable]>
          inspection-mode: <value in [proxy, flow]>
          ippool: <value in [disable, enable]>
          ips-sensor: <string>
          label: <string>
          logtraffic: <value in [disable, enable, all, ...]>
          logtraffic-start: <value in [disable, enable]>
          mms-profile: <string>
          name: <string>
          nat: <value in [disable, enable]>
          natinbound: <value in [disable, enable]>
          natoutbound: <value in [disable, enable]>
          np-acceleration: <value in [disable, enable]>
          outbound: <value in [disable, enable]>
          per-ip-shaper: <string>
          policy-offload: <value in [disable, enable]>
          policyid: <integer>
          poolname: <list or string>
          profile-group: <string>
          profile-protocol-options: <string>
          profile-type: <value in [single, group]>
          replacemsg-override-group: <string>
          rsso: <value in [disable, enable]>
          schedule: <string>
          send-deny-packet: <value in [disable, enable]>
          service: <list or string>
          service-negate: <value in [disable, enable]>
          session-ttl: <string>
          srcaddr: <list or string>
          srcaddr-negate: <value in [disable, enable]>
          srcintf: <list or string>
          ssh-filter-profile: <string>
          ssh-policy-redirect: <value in [disable, enable]>
          ssl-mirror: <value in [disable, enable]>
          ssl-mirror-intf: <list or string>
          ssl-ssh-profile: <string>
          status: <value in [disable, enable]>
          tcp-mss-receiver: <integer>
          tcp-mss-sender: <integer>
          tcp-session-without-syn: <value in [all, data-only, disable]>
          timeout-send-rst: <value in [disable, enable]>
          tos: <string>
          tos-mask: <string>
          tos-negate: <value in [disable, enable]>
          traffic-shaper: <string>
          traffic-shaper-reverse: <string>
          url-category: <list or string>
          users: <list or string>
          utm-status: <value in [disable, enable]>
          uuid: <string>
          vlan-cos-fwd: <integer>
          vlan-cos-rev: <integer>
          vlan-filter: <string>
          voip-profile: <string>
          vpntunnel: <string>
          waf-profile: <string>
          webcache: <value in [disable, enable]>
          webcache-https: <value in [disable, enable]>
          webfilter-profile: <string>
          webproxy-forward-server: <string>
          webproxy-profile: <string>
          dscp-negate: <value in [disable, enable]>
          devices: <list or string>
          dscp-value: <string>
          spamfilter-profile: <string>
          dscp-match: <value in [disable, enable]>
```

## [Return Values](fmgr_pm_config_pblock_firewall_policy6_module.md#id5)

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
