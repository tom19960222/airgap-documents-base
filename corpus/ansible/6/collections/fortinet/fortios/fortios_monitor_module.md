---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_monitor module – Ansible Module for FortiOS Monitor API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_monitor_module.html
fetched_at: 2026-07-27T17:42:47+00:00
---
# fortinet.fortios.fortios_monitor module – Ansible Module for FortiOS Monitor API

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
> see [Requirements](fortios_monitor_module.md#ansible-collections-fortinet-fortios-fortios-monitor-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_monitor`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_monitor_module.md#synopsis)
- [Requirements](fortios_monitor_module.md#requirements)
- [Parameters](fortios_monitor_module.md#parameters)
- [Notes](fortios_monitor_module.md#notes)
- [Examples](fortios_monitor_module.md#examples)
- [Return Values](fortios_monitor_module.md#return-values)

## [Synopsis](fortios_monitor_module.md#id1)

- Request FortiOS appliances to perform specific actions or procedures. This module contain all the FortiOS monitor API.

## [Requirements](fortios_monitor_module.md#id2)

The below requirements are needed on the host that executes this module.

- install galaxy collection fortinet.fortios >= 2.0.0.

## [Parameters](fortios_monitor_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **params**  dictionary | the parameter for each selector, see definition in above list. |
| **selector**  string / required | selector of the retrieved fortimanager facts  Choices:   - `"check.endpoint-control.registration-password"` - `"quarantine.endpoint-control.registration"` - `"unquarantine.endpoint-control.registration"` - `"block.endpoint-control.registration"` - `"unblock.endpoint-control.registration"` - `"deregister.endpoint-control.registration"` - `"clear_counters.firewall.acl"` - `"clear_counters.firewall.acl6"` - `"reset.firewall.policy"` - `"clear_counters.firewall.policy"` - `"reset.firewall.policy6"` - `"clear_counters.firewall.policy6"` - `"clear_counters.firewall.proxy-policy"` - `"clear_all.firewall.session"` - `"close.firewall.session"` - `"reset.firewall.shaper"` - `"reset.firewall.per-ip-shaper"` - `"cancel.fortiview.session"` - `"upgrade.license.database"` - `"reset.log.stats"` - `"login.registration.forticloud"` - `"create.registration.forticloud"` - `"logout.registration.forticloud"` - `"login.registration.forticare"` - `"create.registration.forticare"` - `"add-license.registration.forticare"` - `"add-license.registration.vdom"` - `"toggle-vdom-mode.system.admin"` - `"generate-key.system.api-user"` - `"update-comments.system.config-revision"` - `"delete.system.config-revision"` - `"save.system.config-revision"` - `"system.disconnect-admins"` - `"set.system.time"` - `"reboot.system.os"` - `"shutdown.system.os"` - `"revoke.system.dhcp"` - `"revoke.system.dhcp6"` - `"upgrade.system.firmware"` - `"start.system.fsck"` - `"system.change-password"` - `"system.password-policy-conform"` - `"reset.system.modem"` - `"connect.system.modem"` - `"disconnect.system.modem"` - `"update.system.modem"` - `"restart.system.sniffer"` - `"start.system.sniffer"` - `"stop.system.sniffer"` - `"test.system.automation-stitch"` - `"update.switch-controller.managed-switch"` - `"restart.switch-controller.managed-switch"` - `"poe-reset.switch-controller.managed-switch"` - `"factory-reset.switch-controller.managed-switch"` - `"download.switch-controller.fsw-firmware"` - `"push.switch-controller.fsw-firmware"` - `"upload.switch-controller.fsw-firmware"` - `"dhcp-renew.system.interface"` - `"start.system.usb-log"` - `"stop.system.usb-log"` - `"eject.system.usb-device"` - `"update.system.fortiguard"` - `"clear-statistics.system.fortiguard"` - `"test-availability.system.fortiguard"` - `"config.system.fortimanager"` - `"backup-action.system.fortimanager"` - `"dump.system.com-log"` - `"update.system.ha-peer"` - `"disconnect.system.ha-peer"` - `"run.system.compliance"` - `"restore.system.config"` - `"upload.system.vmlicense"` - `"trigger.system.security-rating"` - `"reset.extender-controller.extender"` - `"validate-gcp-key.system.sdn-connector"` - `"deauth.user.firewall"` - `"clear_users.user.banned"` - `"add_users.user.banned"` - `"clear_all.user.banned"` - `"activate.user.fortitoken"` - `"refresh.user.fortitoken"` - `"provision.user.fortitoken"` - `"send-activation.user.fortitoken"` - `"import-trial.user.fortitoken"` - `"import-mobile.user.fortitoken"` - `"import-seed.user.fortitoken"` - `"refresh-server.user.fsso"` - `"test-connect.user.radius"` - `"test.user.tacacs-plus"` - `"delete.webfilter.override"` - `"reset.webfilter.category-quota"` - `"tunnel_up.vpn.ipsec"` - `"tunnel_down.vpn.ipsec"` - `"tunnel_reset_stats.vpn.ipsec"` - `"clear_tunnel.vpn.ssl"` - `"delete.vpn.ssl"` - `"import.vpn-certificate.ca"` - `"import.vpn-certificate.crl"` - `"import.vpn-certificate.local"` - `"import.vpn-certificate.remote"` - `"generate.vpn-certificate.csr"` - `"reset.wanopt.history"` - `"reset.wanopt.webcache"` - `"reset.wanopt.peer_stats"` - `"reset.webcache.stats"` - `"set_status.wifi.managed_ap"` - `"download.wifi.firmware"` - `"push.wifi.firmware"` - `"upload.wifi.firmware"` - `"restart.wifi.managed_ap"` - `"reset.wifi.euclid"` - `"clear_all.wifi.rogue_ap"` - `"set_status.wifi.rogue_ap"` - `"reset.firewall.consolidated-policy"` - `"clear_counters.firewall.consolidated-policy"` - `"clear_counters.firewall.security-policy"` - `"add.firewall.clearpass-address"` - `"delete.firewall.clearpass-address"` - `"delete.log.local-report"` - `"migrate.registration.forticloud"` - `"change-vdom-mode.system.admin"` - `"delete.system.config-script"` - `"run.system.config-script"` - `"upload.system.config-script"` - `"diagnose.extender-controller.extender"` - `"upgrade.extender-controller.extender"` - `"add.nsx.service"` - `"update.system.sdn-connector"` - `"import.web-ui.language"` - `"create.web-ui.custom-language"` - `"update.web-ui.custom-language"` - `"email.user.guest"` - `"sms.user.guest"` - `"utm.rating-lookup"` - `"connect.wifi.network"` - `"scan.wifi.network"` - `"upload.wifi.region-image"` - `"refresh.azure.application-list"` - `"verify-cert.endpoint-control.ems"` - `"geoip.geoip-query"` - `"transfer.registration.forticare"` - `"register-device.registration.forticloud"` - `"register-appliance.system.csf"` - `"clear.system.sniffer"` - `"webhook.system.automation-stitch"` - `"format.system.logdisk"` - `"speed-test-trigger.system.interface"` - `"read-info.system.certificate"` - `"provision-user.vpn.ssl"` - `"upload.webproxy.pacfile"` - `"disassociate.wifi.client"` - `"start.wifi.spectrum"` - `"keep-alive.wifi.spectrum"` - `"stop.wifi.spectrum"` - `"start.wifi.vlan-probe"` - `"stop.wifi.vlan-probe"` - `"generate-keys.wifi.ssid"` - `"save.system.config"` - `"led-blink.wifi.managed_ap"` - `"auth.user.firewall"` - `"remove.user.device"` - `"clear.vpn.ike"` - `"reset.firewall.multicast-policy"` - `"reset.firewall.multicast-policy6"` - `"clear_counters.firewall.multicast-policy"` - `"clear_counters.firewall.multicast-policy6"` - `"clear-soft-in.router.bgp"` - `"clear-soft-out.router.bgp"` - `"enable-app-bandwidth-tracking.system.traffic-history"` - `"refresh.system.external-resource"` - `"reset.firewall.central-snat-map"` - `"clear-counters.firewall.central-snat-map"` - `"reset.firewall.dnat"` - `"clear-counters.firewall.dnat"` - `"close-multiple.firewall.session"` - `"close-multiple.firewall.session6"` - `"close-all.firewall.session"` - `"clear.system.crash-log"` - `"backup.system.config"` - `"abort.user.query"` - `"create.vpn-certificate.local"` - `"flush.firewall.gtp"` - `"kill.system.process"` - `"upload.system.hscalefw-license"` - `"download.system.vmlicense"` - `"start.network.debug-flow"` - `"stop.network.debug-flow"` - `"upload.system.lte-modem"` - `"upgrade.system.lte-modem"` - `"port-stats-reset.switch-controller.managed-switch"` - `"bounce-port.switch-controller.managed-switch"` - `"set-tier1.switch-controller.mclag-icl"` - `"wake-on-lan.system.interface"` - `"manual-update.system.fortiguard"` - `"purdue-level.user.device"` - `"deregister-device.registration.forticare"` - `"soft-reset-neighbor.router.bgp"` - `"download-eval.system.vmlicense"` - `"dynamic.system.external-resource"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_monitor_module.md#id4)

> **Note:**
>
> - Different selector may have different parameters, users are expected to look up them for a specific selector.
> - For some selectors, the objects are global, no params are allowed to appear.
> - Not all parameters are required for a selector.
> - This module is exclusivly for FortiOS monitor API.
> - The result of API request is stored in results.

## [Examples](fortios_monitor_module.md#id5)

```yaml+jinja
- hosts: fortigate03
  connection: httpapi
  collections:
  - fortinet.fortios
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:

  - name: Activate FortiToken
    fortios_monitor:
       vdom: "root"
       access_token: "<fortios_access_token>"
       selector: 'activate.user.fortitoken'
       params:
           tokens: '<token string>'

  - name: Reboot This Device
    fortios_monitor:
       vdom: "root"
       access_token: "<fortios_access_token>"
       selector: 'reboot.system.os'
       params:
           event_log_message: 'Reboot Request From Ansible'
```

## [Return Values](fortios_monitor_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  Returned: always  Sample: `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  Returned: always  Sample: `"GET"` |
| **name**  string | Name of the table used to fulfill the request  Returned: always  Sample: `"firmware"` |
| **path**  string | Path of the table used to fulfill the request  Returned: always  Sample: `"system"` |
| **revision**  string | Internal revision number  Returned: always  Sample: `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  Returned: always  Sample: `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  Returned: always  Sample: `"success"` |
| **vdom**  string | Virtual domain used  Returned: always  Sample: `"root"` |
| **version**  string | Version of the FortiGate  Returned: always  Sample: `"v5.6.3"` |

### Authors

- Jie Xue (@JieX19)
- Link Zheng (@chillancezen)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@fshen01)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
[Homepage](https://www.fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
