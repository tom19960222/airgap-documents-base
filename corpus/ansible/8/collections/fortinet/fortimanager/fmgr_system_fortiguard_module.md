---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_system_fortiguard module – Configure FortiGuard services."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_system_fortiguard_module.html
fetched_at: 2026-07-28T02:18:32+00:00
---
# fortinet.fortimanager.fmgr_system_fortiguard module – Configure FortiGuard services.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_fortiguard`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_system_fortiguard_module.md#synopsis)
- [Parameters](fmgr_system_fortiguard_module.md#parameters)
- [Notes](fmgr_system_fortiguard_module.md#notes)
- [Examples](fmgr_system_fortiguard_module.md#examples)
- [Return Values](fmgr_system_fortiguard_module.md#return-values)

## [Synopsis](fmgr_system_fortiguard_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_fortiguard_module.md#id2)

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
| **system_fortiguard**  dictionary | the top level parameters set |
| **antispam-cache**  string | Enable/disable FortiGuard antispam request caching.  **Choices:**   - `"disable"` - `"enable"` |
| **antispam-cache-mpercent**  integer | Maximum percent of FortiGate memory the antispam cache is allowed to use |
| **antispam-cache-mpermille**  integer | Maximum permille of FortiGate memory the antispam cache is allowed to use |
| **antispam-cache-ttl**  integer | Time-to-live for antispam cache entries in seconds |
| **antispam-expiration**  integer | Antispam-Expiration. |
| **antispam-force-off**  string | Enable/disable turning off the FortiGuard antispam service.  **Choices:**   - `"disable"` - `"enable"` |
| **antispam-license**  integer | Antispam-License. |
| **antispam-timeout**  integer | Antispam query time out |
| **anycast-sdns-server-ip**  string | IP address of the FortiGuard anycast DNS rating server. |
| **anycast-sdns-server-port**  integer | Port to connect to on the FortiGuard anycast DNS rating server. |
| **auto-firmware-upgrade**  string | Enable/disable automatic patch-level firmware upgrade from FortiGuard.  **Choices:**   - `"disable"` - `"enable"` |
| **auto-firmware-upgrade-day**  list / elements=string | no description  **Choices:**   - `"sunday"` - `"monday"` - `"tuesday"` - `"wednesday"` - `"thursday"` - `"friday"` - `"saturday"` |
| **auto-firmware-upgrade-delay**  integer | Delay of day |
| **auto-firmware-upgrade-end-hour**  integer | End time in the designated time window for automatic patch-level firmware upgrade from FortiGuard in 24 hour time |
| **auto-firmware-upgrade-start-hour**  integer | Start time in the designated time window for automatic patch-level firmware upgrade from FortiGuard in 24 hour time |
| **auto-join-forticloud**  string | Automatically connect to and login to FortiCloud.  **Choices:**   - `"disable"` - `"enable"` |
| **avquery-cache**  string | Enable/disable the FortiGuard antivirus cache.  **Choices:**   - `"disable"` - `"enable"` |
| **avquery-cache-mpercent**  integer | Maximum percent of memory the antivirus cache can use |
| **avquery-cache-ttl**  integer | Time-to-live for antivirus cache entries |
| **avquery-force-off**  string | Turn off the FortiGuard antivirus service.  **Choices:**   - `"disable"` - `"enable"` |
| **avquery-license**  integer | Interval of time between license checks for the FortiGuard antivirus contract. |
| **avquery-timeout**  integer | Antivirus query time out |
| **ddns-server-ip**  string | IP address of the FortiDDNS server. |
| **ddns-server-ip6**  string | IPv6 address of the FortiDDNS server. |
| **ddns-server-port**  integer | Port used to communicate with FortiDDNS servers. |
| **FDS-license-expiring-days**  integer | Threshold for number of days before FortiGuard license expiration to generate license expiring event log |
| **fortiguard-anycast**  string | Enable/disable use of FortiGuards anycast network.  **Choices:**   - `"disable"` - `"enable"` |
| **fortiguard-anycast-source**  string | Configure which of Fortinets servers to provide FortiGuard services in FortiGuards anycast network.  **Choices:**   - `"fortinet"` - `"aws"` - `"debug"` |
| **gui-prompt-auto-upgrade**  string | Enable/disable prompting of automatic patch-level firmware upgrade recommendation.  **Choices:**   - `"disable"` - `"enable"` |
| **interface**  string | Specify outgoing interface to reach server. |
| **interface-select-method**  string | Specify how to select outgoing interface to reach server.  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **load-balance-servers**  integer | Number of servers to alternate between as first FortiGuard option. |
| **outbreak-prevention-cache**  string | Enable/disable FortiGuard Virus Outbreak Prevention cache.  **Choices:**   - `"disable"` - `"enable"` |
| **outbreak-prevention-cache-mpercent**  integer | Maximum percent of memory FortiGuard Virus Outbreak Prevention cache can use |
| **outbreak-prevention-cache-mpermille**  integer | Maximum permille of memory FortiGuard Virus Outbreak Prevention cache can use |
| **outbreak-prevention-cache-ttl**  integer | Time-to-live for FortiGuard Virus Outbreak Prevention cache entries |
| **outbreak-prevention-expiration**  integer | Outbreak-Prevention-Expiration. |
| **outbreak-prevention-force-off**  string | Turn off FortiGuard Virus Outbreak Prevention service.  **Choices:**   - `"disable"` - `"enable"` |
| **outbreak-prevention-license**  integer | Outbreak-Prevention-License. |
| **outbreak-prevention-timeout**  integer | FortiGuard Virus Outbreak Prevention time out |
| **persistent-connection**  string | Enable/disable use of persistent connection to receive update notification from FortiGuard.  **Choices:**   - `"disable"` - `"enable"` |
| **port**  string | Port used to communicate with the FortiGuard servers.  **Choices:**   - `"53"` - `"80"` - `"8888"` - `"443"` |
| **protocol**  string | Protocol used to communicate with the FortiGuard servers.  **Choices:**   - `"udp"` - `"http"` - `"https"` |
| **proxy-password**  any | (list) Proxy user password. |
| **proxy-server-ip**  string | IP address of the proxy server. |
| **proxy-server-port**  integer | Port used to communicate with the proxy server. |
| **proxy-username**  string | Proxy user name. |
| **sandbox-inline-scan**  string | Enable/disable FortiCloud Sandbox inline-scan.  **Choices:**   - `"disable"` - `"enable"` |
| **sandbox-region**  string | Cloud sandbox region. |
| **sdns-options**  list / elements=string | Customization options for the FortiGuard DNS service.  **Choices:**   - `"include-question-section"` |
| **sdns-server-ip**  any | (list) IP address of the FortiDNS server. |
| **sdns-server-port**  integer | Port used to communicate with FortiDNS servers. |
| **service-account-id**  string | Service account ID. |
| **source-ip**  string | Source IPv4 address used to communicate with FortiGuard. |
| **source-ip6**  string | Source IPv6 address used to communicate with FortiGuard. |
| **update-build-proxy**  string | Enable/disable proxy dictionary rebuild.  **Choices:**   - `"disable"` - `"enable"` |
| **update-dldb**  string | Enable/disable DLP signature update.  **Choices:**   - `"disable"` - `"enable"` |
| **update-extdb**  string | Enable/disable external resource update.  **Choices:**   - `"disable"` - `"enable"` |
| **update-ffdb**  string | Enable/disable Internet Service Database update.  **Choices:**   - `"disable"` - `"enable"` |
| **update-server-location**  string | Signature update server location.  **Choices:**   - `"any"` - `"usa"` - `"automatic"` - `"eu"` |
| **update-uwdb**  string | Enable/disable allowlist update.  **Choices:**   - `"disable"` - `"enable"` |
| **vdom**  string | FortiGuard Service virtual domain name. |
| **videofilter-expiration**  integer | Videofilter-Expiration. |
| **videofilter-license**  integer | Videofilter-License. |
| **webfilter-cache**  string | Enable/disable FortiGuard web filter caching.  **Choices:**   - `"disable"` - `"enable"` |
| **webfilter-cache-ttl**  integer | Time-to-live for web filter cache entries in seconds |
| **webfilter-expiration**  integer | Webfilter-Expiration. |
| **webfilter-force-off**  string | Enable/disable turning off the FortiGuard web filtering service.  **Choices:**   - `"disable"` - `"enable"` |
| **webfilter-license**  integer | Webfilter-License. |
| **webfilter-timeout**  integer | Web filter query time out |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_system_fortiguard_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_fortiguard_module.md#id4)

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
    - name: Configure FortiGuard services.
      fmgr_system_fortiguard:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        system_fortiguard:
          antispam-cache: <value in [disable, enable]>
          antispam-cache-mpercent: <integer>
          antispam-cache-ttl: <integer>
          antispam-expiration: <integer>
          antispam-force-off: <value in [disable, enable]>
          antispam-license: <integer>
          antispam-timeout: <integer>
          auto-join-forticloud: <value in [disable, enable]>
          ddns-server-ip: <string>
          ddns-server-port: <integer>
          load-balance-servers: <integer>
          outbreak-prevention-cache: <value in [disable, enable]>
          outbreak-prevention-cache-mpercent: <integer>
          outbreak-prevention-cache-ttl: <integer>
          outbreak-prevention-expiration: <integer>
          outbreak-prevention-force-off: <value in [disable, enable]>
          outbreak-prevention-license: <integer>
          outbreak-prevention-timeout: <integer>
          port: <value in [53, 80, 8888, ...]>
          sdns-server-ip: <list or string>
          sdns-server-port: <integer>
          service-account-id: <string>
          source-ip: <string>
          source-ip6: <string>
          update-server-location: <value in [any, usa, automatic, ...]>
          webfilter-cache: <value in [disable, enable]>
          webfilter-cache-ttl: <integer>
          webfilter-expiration: <integer>
          webfilter-force-off: <value in [disable, enable]>
          webfilter-license: <integer>
          webfilter-timeout: <integer>
          protocol: <value in [udp, http, https]>
          proxy-password: <list or string>
          proxy-server-ip: <string>
          proxy-server-port: <integer>
          proxy-username: <string>
          sandbox-region: <string>
          avquery-cache-ttl: <integer>
          avquery-timeout: <integer>
          avquery-cache: <value in [disable, enable]>
          avquery-cache-mpercent: <integer>
          avquery-license: <integer>
          avquery-force-off: <value in [disable, enable]>
          fortiguard-anycast: <value in [disable, enable]>
          fortiguard-anycast-source: <value in [fortinet, aws, debug]>
          interface: <string>
          interface-select-method: <value in [auto, sdwan, specify]>
          sdns-options:
            - include-question-section
          anycast-sdns-server-ip: <string>
          anycast-sdns-server-port: <integer>
          persistent-connection: <value in [disable, enable]>
          update-build-proxy: <value in [disable, enable]>
          update-extdb: <value in [disable, enable]>
          update-ffdb: <value in [disable, enable]>
          update-uwdb: <value in [disable, enable]>
          videofilter-expiration: <integer>
          videofilter-license: <integer>
          ddns-server-ip6: <string>
          vdom: <string>
          auto-firmware-upgrade: <value in [disable, enable]>
          auto-firmware-upgrade-day:
            - sunday
            - monday
            - tuesday
            - wednesday
            - thursday
            - friday
            - saturday
          auto-firmware-upgrade-end-hour: <integer>
          auto-firmware-upgrade-start-hour: <integer>
          sandbox-inline-scan: <value in [disable, enable]>
          auto-firmware-upgrade-delay: <integer>
          gui-prompt-auto-upgrade: <value in [disable, enable]>
          FDS-license-expiring-days: <integer>
          antispam-cache-mpermille: <integer>
          outbreak-prevention-cache-mpermille: <integer>
          update-dldb: <value in [disable, enable]>
```

## [Return Values](fmgr_system_fortiguard_module.md#id5)

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
