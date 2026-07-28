---
collection: ansible
version: "8"
title: "Community.Fortios"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/fortios/index.html
fetched_at: 2026-07-28T01:02:11+00:00
---
# Community.Fortios

Collection version 1.0.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

modules for management of FortiOS devices

**Authors:**

- Luke Weighall (github.com/lweighall)
- Andrew Welsh (github.com/Ghilli3)
- Jim Huber (github.com/p4r4n0y1ng)

**Supported ansible-core versions:**

- 2.9.10 or newer

- [Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.fortios)

## [Plugin Index](index.md#id2)

These are the plugins in the community.fortios collection:

### Modules

- [faz_device module](faz_device_module.md#ansible-collections-community-fortios-faz-device-module) – Add or remove device
- [fmgr_device module](fmgr_device_module.md#ansible-collections-community-fortios-fmgr-device-module) – Add or remove device from FortiManager.
- [fmgr_device_config module](fmgr_device_config_module.md#ansible-collections-community-fortios-fmgr-device-config-module) – Edit device configurations
- [fmgr_device_group module](fmgr_device_group_module.md#ansible-collections-community-fortios-fmgr-device-group-module) – Alter FortiManager device groups.
- [fmgr_device_provision_template module](fmgr_device_provision_template_module.md#ansible-collections-community-fortios-fmgr-device-provision-template-module) – Manages Device Provisioning Templates in FortiManager.
- [fmgr_fwobj_address module](fmgr_fwobj_address_module.md#ansible-collections-community-fortios-fmgr-fwobj-address-module) – Allows the management of firewall objects in FortiManager
- [fmgr_fwobj_ippool module](fmgr_fwobj_ippool_module.md#ansible-collections-community-fortios-fmgr-fwobj-ippool-module) – Allows the editing of IP Pool Objects within FortiManager.
- [fmgr_fwobj_ippool6 module](fmgr_fwobj_ippool6_module.md#ansible-collections-community-fortios-fmgr-fwobj-ippool6-module) – Allows the editing of IP Pool Objects within FortiManager.
- [fmgr_fwobj_service module](fmgr_fwobj_service_module.md#ansible-collections-community-fortios-fmgr-fwobj-service-module) – Manages FortiManager Firewall Service Objects.
- [fmgr_fwobj_vip module](fmgr_fwobj_vip_module.md#ansible-collections-community-fortios-fmgr-fwobj-vip-module) – Manages Virtual IPs objects in FortiManager
- [fmgr_fwpol_ipv4 module](fmgr_fwpol_ipv4_module.md#ansible-collections-community-fortios-fmgr-fwpol-ipv4-module) – Allows the add/delete of Firewall Policies on Packages in FortiManager.
- [fmgr_fwpol_package module](fmgr_fwpol_package_module.md#ansible-collections-community-fortios-fmgr-fwpol-package-module) – Manages FortiManager Firewall Policies Packages.
- [fmgr_ha module](fmgr_ha_module.md#ansible-collections-community-fortios-fmgr-ha-module) – Manages the High-Availability State of FortiManager Clusters and Nodes.
- [fmgr_provisioning module](fmgr_provisioning_module.md#ansible-collections-community-fortios-fmgr-provisioning-module) – Provision devices via FortiMananger
- [fmgr_query module](fmgr_query_module.md#ansible-collections-community-fortios-fmgr-query-module) – Query FortiManager data objects for use in Ansible workflows.
- [fmgr_script module](fmgr_script_module.md#ansible-collections-community-fortios-fmgr-script-module) – Add/Edit/Delete and execute scripts
- [fmgr_secprof_appctrl module](fmgr_secprof_appctrl_module.md#ansible-collections-community-fortios-fmgr-secprof-appctrl-module) – Manage application control security profiles
- [fmgr_secprof_av module](fmgr_secprof_av_module.md#ansible-collections-community-fortios-fmgr-secprof-av-module) – Manage security profile
- [fmgr_secprof_dns module](fmgr_secprof_dns_module.md#ansible-collections-community-fortios-fmgr-secprof-dns-module) – Manage DNS security profiles in FortiManager
- [fmgr_secprof_ips module](fmgr_secprof_ips_module.md#ansible-collections-community-fortios-fmgr-secprof-ips-module) – Managing IPS security profiles in FortiManager
- [fmgr_secprof_profile_group module](fmgr_secprof_profile_group_module.md#ansible-collections-community-fortios-fmgr-secprof-profile-group-module) – Manage security profiles within FortiManager
- [fmgr_secprof_proxy module](fmgr_secprof_proxy_module.md#ansible-collections-community-fortios-fmgr-secprof-proxy-module) – Manage proxy security profiles in FortiManager
- [fmgr_secprof_spam module](fmgr_secprof_spam_module.md#ansible-collections-community-fortios-fmgr-secprof-spam-module) – spam filter profile for FMG
- [fmgr_secprof_ssl_ssh module](fmgr_secprof_ssl_ssh_module.md#ansible-collections-community-fortios-fmgr-secprof-ssl-ssh-module) – Manage SSL and SSH security profiles in FortiManager
- [fmgr_secprof_voip module](fmgr_secprof_voip_module.md#ansible-collections-community-fortios-fmgr-secprof-voip-module) – VOIP security profiles in FMG
- [fmgr_secprof_waf module](fmgr_secprof_waf_module.md#ansible-collections-community-fortios-fmgr-secprof-waf-module) – FortiManager web application firewall security profile
- [fmgr_secprof_wanopt module](fmgr_secprof_wanopt_module.md#ansible-collections-community-fortios-fmgr-secprof-wanopt-module) – WAN optimization
- [fmgr_secprof_web module](fmgr_secprof_web_module.md#ansible-collections-community-fortios-fmgr-secprof-web-module) – Manage web filter security profiles in FortiManager

### Httpapi Plugins

- [fortianalyzer httpapi](fortianalyzer_httpapi.md#ansible-collections-community-fortios-fortianalyzer-httpapi) – HttpApi Plugin for Fortinet FortiAnalyzer Appliance or VM.
- [fortimanager httpapi](fortimanager_httpapi.md#ansible-collections-community-fortios-fortimanager-httpapi) – HttpApi Plugin for Fortinet FortiManager Appliance or VM.

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
