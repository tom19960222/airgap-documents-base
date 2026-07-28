---
collection: ansible
version: "6"
title: "Ansible 2.9 Porting Guide"
source_url: https://docs.ansible.com/projects/ansible/6/porting_guides/porting_guide_2.9.html
fetched_at: 2026-07-27T16:39:42+00:00
---
# [Ansible 2.9 Porting Guide](porting_guide_2.9.md#id1)

This section discusses the behavioral changes between Ansible 2.8 and Ansible 2.9.

It is intended to assist in updating your playbooks, plugins and other parts of your Ansible infrastructure so they will work with this version of Ansible.

We suggest you read this page along with [Ansible Changelog for 2.9](https://github.com/ansible/ansible/blob/stable-2.9/changelogs/CHANGELOG-v2.9.rst) to understand what updates you may need to make.

This document is part of a collection on porting. The complete list of porting guides can be found at [porting guides](porting_guides.md#porting-guides).

Topics

- [Ansible 2.9 Porting Guide](porting_guide_2.9.md#ansible-2-9-porting-guide)

  - [Playbook](porting_guide_2.9.md#playbook)

    - [Inventory](porting_guide_2.9.md#inventory)
    - [Loops](porting_guide_2.9.md#loops)
  - [Command Line](porting_guide_2.9.md#command-line)
  - [Deprecated](porting_guide_2.9.md#deprecated)
  - [Collection loader changes](porting_guide_2.9.md#collection-loader-changes)
  - [Modules](porting_guide_2.9.md#modules)

    - [Renaming from `_facts` to `_info`](porting_guide_2.9.md#renaming-from-facts-to-info)
    - [Writing modules](porting_guide_2.9.md#writing-modules)
    - [Modules removed](porting_guide_2.9.md#modules-removed)
    - [Deprecation notices](porting_guide_2.9.md#deprecation-notices)

      - [Renamed modules](porting_guide_2.9.md#renamed-modules)
    - [Noteworthy module changes](porting_guide_2.9.md#noteworthy-module-changes)
  - [Plugins](porting_guide_2.9.md#plugins)

    - [Removed Lookup Plugins](porting_guide_2.9.md#removed-lookup-plugins)
  - [Porting custom scripts](porting_guide_2.9.md#porting-custom-scripts)
  - [Networking](porting_guide_2.9.md#networking)

    - [Network resource modules](porting_guide_2.9.md#network-resource-modules)
    - [Improved `gather_facts` support for network devices](porting_guide_2.9.md#improved-gather-facts-support-for-network-devices)
    - [Top-level connection arguments removed in 2.9](porting_guide_2.9.md#top-level-connection-arguments-removed-in-2-9)

## [Playbook](porting_guide_2.9.md#id2)

### [Inventory](porting_guide_2.9.md#id3)

> - `hash_behaviour` now affects inventory sources. If you have it set to `merge`, the data you get from inventory might change and you will have to update playbooks accordingly. If you’re using the default setting (`overwrite`), you will see no changes. Inventory was ignoring this setting.

### [Loops](porting_guide_2.9.md#id4)

Ansible 2.9 handles “unsafe” data more robustly, ensuring that data marked “unsafe” is not templated. In previous versions, Ansible recursively marked all data returned by the direct use of `lookup()` as “unsafe”, but only marked structured data returned by indirect lookups using `with_X` style loops as “unsafe” if the returned elements were strings. Ansible 2.9 treats these two approaches consistently.

As a result, if you use `with_dict` to return keys with templatable values, your templates may no longer work as expected in Ansible 2.9.

To allow the old behavior, switch from using `with_X` to using `loop` with a filter as described at [Migrating from with_X to loop](../user_guide/playbooks_loops.md#migrating-to-loop).

## [Command Line](porting_guide_2.9.md#id5)

- The location of the Galaxy token file has changed from `~/.ansible_galaxy` to `~/.ansible/galaxy_token`. You can configure both path and file name with the [GALAXY_TOKEN_PATH](../reference_appendices/config.md#galaxy-token-path) config.

## [Deprecated](porting_guide_2.9.md#id6)

No notable changes

## [Collection loader changes](porting_guide_2.9.md#id7)

The way to import a PowerShell or C# module util from a collection has changed in the Ansible 2.9 release. In Ansible
2.8 a util was imported with the following syntax:

```powershell
#AnsibleRequires -CSharpUtil AnsibleCollections.namespace_name.collection_name.util_filename
#AnsibleRequires -PowerShell AnsibleCollections.namespace_name.collection_name.util_filename
```

In Ansible 2.9 this was changed to:

```powershell
#AnsibleRequires -CSharpUtil ansible_collections.namespace_name.collection_name.plugins.module_utils.util_filename
#AnsibleRequires -PowerShell ansible_collections.namespace_name.collection_name.plugins.module_utils.util_filename
```

The change in the collection import name also requires any C# util namespaces to be updated with the newer name
format. This is more verbose but is designed to make sure we avoid plugin name conflicts across separate plugin types
and to standardise how imports work in PowerShell with how Python modules work.

## [Modules](porting_guide_2.9.md#id8)

- The `win_get_url` and `win_uri` module now sends requests with a default `User-Agent` of `ansible-httpget`. This can be changed by using the `http_agent` key.
- The `apt` module now honors `update_cache=false` while installing its own dependency and skips the cache update. Explicitly setting `update_cache=true` or omitting the param `update_cache` will result in a cache update while installing its own dependency.
- Version 2.9.12 of Ansible changed the default mode of file-based tasks to `0o600 & ~umask` when the user did not specify a `mode` parameter on file-based tasks. This was in response to a CVE report which we have reconsidered. As a result, the mode change has been reverted in 2.9.13, and mode will now default to `0o666 & ~umask` as in previous versions of Ansible.
- If you changed any tasks to specify less restrictive permissions while using 2.9.12, those changes will be unnecessary (but will do no harm) in 2.9.13.
- To avoid the issue raised in CVE-2020-1736, specify a `mode` parameter in all file-based tasks that accept it.
- `dnf` and `yum` - As of version 2.9.13, the `dnf` module (and `yum` action when it uses `dnf`) now correctly validates GPG signatures of packages (CVE-2020-14365). If you see an error such as `Failed to validate GPG signature for [package name]`, please ensure that you have imported the correct GPG key for the DNF repository and/or package you are using. One way to do this is with the `rpm_key` module. Although we discourage it, in some cases it may be necessary to disable the GPG check. This can be done by explicitly adding `disable_gpg_check: yes` in your `dnf` or `yum` task.

### [Renaming from `_facts` to `_info`](porting_guide_2.9.md#id9)

Ansible 2.9 renamed a lot of modules from `<something>_facts` to `<something>_info`, because the modules do not return [Ansible facts](../user_guide/playbooks_vars_facts.md#vars-and-facts). Ansible facts relate to a specific host. For example, the configuration of a network interface, the operating system on a unix server, and the list of packages installed on a Windows box are all Ansible facts. The renamed modules return values that are not unique to the host. For example, account information or region data for a cloud provider. Renaming these modules should provide more clarity about the types of return values each set of modules offers.

### [Writing modules](porting_guide_2.9.md#id10)

- Module and module_utils files can now use relative imports to include other module_utils files.
  This is useful for shortening long import lines, especially in collections.

  Example of using a relative import in collections:

  ```python
  # File: ansible_collections/my_namespace/my_collection/plugins/modules/my_module.py
  # Old way to use an absolute import to import module_utils from the collection:
  from ansible_collections.my_namespace.my_collection.plugins.module_utils import my_util
  # New way using a relative import:
  from ..module_utils import my_util
  ```

  Modules and module_utils shipped with Ansible can use relative imports as well but the savings
  are smaller:

  ```python
  # File: ansible/modules/system/ping.py
  # Old way to use an absolute import to import module_utils from core:
  from ansible.module_utils.basic import AnsibleModule
  # New way using a relative import:
  from ...module_utils.basic import AnsibleModule
  ```

  Each single dot (`.`) represents one level of the tree (equivalent to `../` in filesystem relative links).

  > **See also:**
  >
  > [The Python Relative Import Docs](https://www.python.org/dev/peps/pep-0328/#guido-s-decision) go into more detail of how to write relative imports.

### [Modules removed](porting_guide_2.9.md#id11)

The following modules no longer exist:

- Apstra’s `aos_*` modules. See the new modules at <https://github.com/apstra>.
- ec2_ami_find use [ec2_ami_facts](https://docs.ansible.com/ansible/2.9/modules/ec2_ami_info_module.html#ec2-ami-facts-module "(in Ansible v2.9)") instead.
- kubernetes use [k8s](https://docs.ansible.com/ansible/2.9/modules/k8s_module.html#k8s-module "(in Ansible v2.9)") instead.
- nxos_ip_interface use [nxos_l3_interface](https://docs.ansible.com/ansible/2.9/modules/nxos_l3_interface_module.html#nxos-l3-interface-module "(in Ansible v2.9)") instead.
- nxos_portchannel use [nxos_linkagg](https://docs.ansible.com/ansible/2.9/modules/nxos_linkagg_module.html#nxos-linkagg-module "(in Ansible v2.9)") instead.
- nxos_switchport use [nxos_l2_interface](https://docs.ansible.com/ansible/2.9/modules/nxos_l2_interface_module.html#nxos-l2-interface-module "(in Ansible v2.9)") instead.
- oc use [k8s](https://docs.ansible.com/ansible/2.9/modules/k8s_module.html#k8s-module "(in Ansible v2.9)") instead.
- panos_nat_policy use [panos_nat_rule](https://docs.ansible.com/ansible/2.9/modules/panos_nat_rule_module.html#panos-nat-rule-module "(in Ansible v2.9)") instead.
- panos_security_policy use [panos_security_rule](https://docs.ansible.com/ansible/2.9/modules/panos_security_rule_module.html#panos-security-rule-module "(in Ansible v2.9)") instead.
- vsphere_guest use [vmware_guest](https://docs.ansible.com/ansible/2.9/modules/vmware_guest_module.html#vmware-guest-module "(in Ansible v2.9)") instead.

### [Deprecation notices](porting_guide_2.9.md#id12)

The following modules will be removed in Ansible 2.13. Please update update your playbooks accordingly.

- cs_instance_facts use [cs_instance_info](https://docs.ansible.com/ansible/2.9/modules/cs_instance_info_module.html#cs-instance-info-module "(in Ansible v2.9)") instead.
- cs_zone_facts use [cs_zone_info](https://docs.ansible.com/ansible/2.9/modules/cs_zone_info_module.html#cs-zone-info-module "(in Ansible v2.9)") instead.
- digital_ocean_sshkey_facts use [digital_ocean_sshkey_info](https://docs.ansible.com/ansible/2.9/modules/digital_ocean_sshkey_info_module.html#digital-ocean-sshkey-info-module "(in Ansible v2.9)") instead.
- eos_interface use [eos_interfaces](https://docs.ansible.com/ansible/2.9/modules/eos_interfaces_module.html#eos-interfaces-module "(in Ansible v2.9)") instead.
- eos_l2_interface use [eos_l2_interfaces](https://docs.ansible.com/ansible/2.9/modules/eos_l2_interfaces_module.html#eos-l2-interfaces-module "(in Ansible v2.9)") instead.
- eos_l3_interface use [eos_l3_interfaces](https://docs.ansible.com/ansible/2.9/modules/eos_l3_interfaces_module.html#eos-l3-interfaces-module "(in Ansible v2.9)") instead.
- eos_linkagg use [eos_lag_interfaces](https://docs.ansible.com/ansible/2.9/modules/eos_lag_interfaces_module.html#eos-lag-interfaces-module "(in Ansible v2.9)") instead.
- eos_lldp_interface use [eos_lldp_interfaces](https://docs.ansible.com/ansible/2.9/modules/eos_lldp_interfaces_module.html#eos-lldp-interfaces-module "(in Ansible v2.9)") instead.
- eos_vlan use [eos_vlans](https://docs.ansible.com/ansible/2.9/modules/eos_vlans_module.html#eos-vlans-module "(in Ansible v2.9)") instead.
- ios_interface use [ios_interfaces](https://docs.ansible.com/ansible/2.9/modules/ios_interfaces_module.html#ios-interfaces-module "(in Ansible v2.9)") instead.
- ios_l2_interface use [ios_l2_interfaces](https://docs.ansible.com/ansible/2.9/modules/ios_l2_interfaces_module.html#ios-l2-interfaces-module "(in Ansible v2.9)") instead.
- ios_l3_interface use [ios_l3_interfaces](https://docs.ansible.com/ansible/2.9/modules/ios_l3_interfaces_module.html#ios-l3-interfaces-module "(in Ansible v2.9)") instead.
- ios_vlan use [ios_vlans](https://docs.ansible.com/ansible/2.9/modules/ios_vlans_module.html#ios-vlans-module "(in Ansible v2.9)") instead.
- iosxr_interface use [iosxr_interfaces](https://docs.ansible.com/ansible/2.9/modules/iosxr_interfaces_module.html#iosxr-interfaces-module "(in Ansible v2.9)") instead.
- junos_interface use [junos_interfaces](https://docs.ansible.com/ansible/2.9/modules/junos_interfaces_module.html#junos-interfaces-module "(in Ansible v2.9)") instead.
- junos_l2_interface use [junos_l2_interfaces](https://docs.ansible.com/ansible/2.9/modules/junos_l2_interfaces_module.html#junos-l2-interfaces-module "(in Ansible v2.9)") instead.
- junos_l3_interface use [junos_l3_interfaces](https://docs.ansible.com/ansible/2.9/modules/junos_l3_interfaces_module.html#junos-l3-interfaces-module "(in Ansible v2.9)") instead.
- junos_linkagg use [junos_lag_interfaces](https://docs.ansible.com/ansible/2.9/modules/junos_lag_interfaces_module.html#junos-lag-interfaces-module "(in Ansible v2.9)") instead.
- junos_lldp use [junos_lldp_global](https://docs.ansible.com/ansible/2.9/modules/junos_lldp_global_module.html#junos-lldp-global-module "(in Ansible v2.9)") instead.
- junos_lldp_interface use [junos_lldp_interfaces](https://docs.ansible.com/ansible/2.9/modules/junos_lldp_interfaces_module.html#junos-lldp-interfaces-module "(in Ansible v2.9)") instead.
- junos_vlan use [junos_vlans](https://docs.ansible.com/ansible/2.9/modules/junos_vlans_module.html#junos-vlans-module "(in Ansible v2.9)") instead.
- lambda_facts use [lambda_info](https://docs.ansible.com/ansible/2.9/modules/lambda_info_module.html#lambda-info-module "(in Ansible v2.9)") instead.
- na_ontap_gather_facts use [na_ontap_info](https://docs.ansible.com/ansible/2.9/modules/na_ontap_info_module.html#na-ontap-info-module "(in Ansible v2.9)") instead.
- net_banner use the platform-specific [netos]_banner modules instead.
- net_interface use the new platform-specific [netos]_interfaces modules instead.
- net_l2_interface use the new platform-specific [netos]_l2_interfaces modules instead.
- net_l3_interface use the new platform-specific [netos]_l3_interfaces modules instead.
- net_linkagg use the new platform-specific [netos]_lag modules instead.
- net_lldp use the new platform-specific [netos]_lldp_global modules instead.
- net_lldp_interface use the new platform-specific [netos]_lldp_interfaces modules instead.
- net_logging use the platform-specific [netos]_logging modules instead.
- net_static_route use the platform-specific [netos]_static_route modules instead.
- net_system use the platform-specific [netos]_system modules instead.
- net_user use the platform-specific [netos]_user modules instead.
- net_vlan use the new platform-specific [netos]_vlans modules instead.
- net_vrf use the platform-specific [netos]_vrf modules instead.
- nginx_status_facts use [nginx_status_info](https://docs.ansible.com/ansible/2.9/modules/nginx_status_info_module.html#nginx-status-info-module "(in Ansible v2.9)") instead.
- nxos_interface use [nxos_interfaces](https://docs.ansible.com/ansible/2.9/modules/nxos_interfaces_module.html#nxos-interfaces-module "(in Ansible v2.9)") instead.
- nxos_l2_interface use [nxos_l2_interfaces](https://docs.ansible.com/ansible/2.9/modules/nxos_l2_interfaces_module.html#nxos-l2-interfaces-module "(in Ansible v2.9)") instead.
- nxos_l3_interface use [nxos_l3_interfaces](https://docs.ansible.com/ansible/2.9/modules/nxos_l3_interfaces_module.html#nxos-l3-interfaces-module "(in Ansible v2.9)") instead.
- nxos_linkagg use [nxos_lag_interfaces](https://docs.ansible.com/ansible/2.9/modules/nxos_lag_interfaces_module.html#nxos-lag-interfaces-module "(in Ansible v2.9)") instead.
- nxos_vlan use [nxos_vlans](https://docs.ansible.com/ansible/2.9/modules/nxos_vlans_module.html#nxos-vlans-module "(in Ansible v2.9)") instead.
- online_server_facts use [online_server_info](https://docs.ansible.com/ansible/2.9/modules/online_server_info_module.html#online-server-info-module "(in Ansible v2.9)") instead.
- online_user_facts use [online_user_info](https://docs.ansible.com/ansible/2.9/modules/online_user_info_module.html#online-user-info-module "(in Ansible v2.9)") instead.
- purefa_facts use [purefa_info](https://docs.ansible.com/ansible/2.9/modules/purefa_info_module.html#purefa-info-module "(in Ansible v2.9)") instead.
- purefb_facts use [purefb_info](https://docs.ansible.com/ansible/2.9/modules/purefb_info_module.html#purefb-info-module "(in Ansible v2.9)") instead.
- scaleway_image_facts use [scaleway_image_info](https://docs.ansible.com/ansible/2.9/modules/scaleway_image_info_module.html#scaleway-image-info-module "(in Ansible v2.9)") instead.
- scaleway_ip_facts use [scaleway_ip_info](https://docs.ansible.com/ansible/2.9/modules/scaleway_ip_info_module.html#scaleway-ip-info-module "(in Ansible v2.9)") instead.
- scaleway_organization_facts use [scaleway_organization_info](https://docs.ansible.com/ansible/2.9/modules/scaleway_organization_info_module.html#scaleway-organization-info-module "(in Ansible v2.9)") instead.
- scaleway_security_group_facts use [scaleway_security_group_info](https://docs.ansible.com/ansible/2.9/modules/scaleway_security_group_info_module.html#scaleway-security-group-info-module "(in Ansible v2.9)") instead.
- scaleway_server_facts use [scaleway_server_info](https://docs.ansible.com/ansible/2.9/modules/scaleway_server_info_module.html#scaleway-server-info-module "(in Ansible v2.9)") instead.
- scaleway_snapshot_facts use [scaleway_snapshot_info](https://docs.ansible.com/ansible/2.9/modules/scaleway_snapshot_info_module.html#scaleway-snapshot-info-module "(in Ansible v2.9)") instead.
- scaleway_volume_facts use [scaleway_volume_info](https://docs.ansible.com/ansible/2.9/modules/scaleway_volume_info_module.html#scaleway-volume-info-module "(in Ansible v2.9)") instead.
- vcenter_extension_facts use [vcenter_extension_info](https://docs.ansible.com/ansible/2.9/modules/vcenter_extension_info_module.html#vcenter-extension-info-module "(in Ansible v2.9)") instead.
- vmware_about_facts use [vmware_about_info](https://docs.ansible.com/ansible/2.9/modules/vmware_about_info_module.html#vmware-about-info-module "(in Ansible v2.9)") instead.
- vmware_category_facts use [vmware_category_info](https://docs.ansible.com/ansible/2.9/modules/vmware_category_info_module.html#vmware-category-info-module "(in Ansible v2.9)") instead.
- vmware_drs_group_facts use [vmware_drs_group_info](https://docs.ansible.com/ansible/2.9/modules/vmware_drs_group_info_module.html#vmware-drs-group-info-module "(in Ansible v2.9)") instead.
- vmware_drs_rule_facts use [vmware_drs_rule_info](https://docs.ansible.com/ansible/2.9/modules/vmware_drs_rule_info_module.html#vmware-drs-rule-info-module "(in Ansible v2.9)") instead.
- vmware_dvs_portgroup_facts use [vmware_dvs_portgroup_info](https://docs.ansible.com/ansible/2.9/modules/vmware_dvs_portgroup_info_module.html#vmware-dvs-portgroup-info-module "(in Ansible v2.9)") instead.
- vmware_guest_boot_facts use [vmware_guest_boot_info](https://docs.ansible.com/ansible/2.9/modules/vmware_guest_boot_info_module.html#vmware-guest-boot-info-module "(in Ansible v2.9)") instead.
- vmware_guest_customization_facts use [vmware_guest_customization_info](https://docs.ansible.com/ansible/2.9/modules/vmware_guest_customization_info_module.html#vmware-guest-customization-info-module "(in Ansible v2.9)") instead.
- vmware_guest_disk_facts use [vmware_guest_disk_info](https://docs.ansible.com/ansible/2.9/modules/vmware_guest_disk_info_module.html#vmware-guest-disk-info-module "(in Ansible v2.9)") instead.
- vmware_host_capability_facts use [vmware_host_capability_info](https://docs.ansible.com/ansible/2.9/modules/vmware_host_capability_info_module.html#vmware-host-capability-info-module "(in Ansible v2.9)") instead.
- vmware_host_config_facts use [vmware_host_config_info](https://docs.ansible.com/ansible/2.9/modules/vmware_host_config_info_module.html#vmware-host-config-info-module "(in Ansible v2.9)") instead.
- vmware_host_dns_facts use [vmware_host_dns_info](https://docs.ansible.com/ansible/2.9/modules/vmware_host_dns_info_module.html#vmware-host-dns-info-module "(in Ansible v2.9)") instead.
- vmware_host_feature_facts use [vmware_host_feature_info](https://docs.ansible.com/ansible/2.9/modules/vmware_host_feature_info_module.html#vmware-host-feature-info-module "(in Ansible v2.9)") instead.
- vmware_host_firewall_facts use [vmware_host_firewall_info](https://docs.ansible.com/ansible/2.9/modules/vmware_host_firewall_info_module.html#vmware-host-firewall-info-module "(in Ansible v2.9)") instead.
- vmware_host_ntp_facts use [vmware_host_ntp_info](https://docs.ansible.com/ansible/2.9/modules/vmware_host_ntp_info_module.html#vmware-host-ntp-info-module "(in Ansible v2.9)") instead.
- vmware_host_package_facts use [vmware_host_package_info](https://docs.ansible.com/ansible/2.9/modules/vmware_host_package_info_module.html#vmware-host-package-info-module "(in Ansible v2.9)") instead.
- vmware_host_service_facts use [vmware_host_service_info](https://docs.ansible.com/ansible/2.9/modules/vmware_host_service_info_module.html#vmware-host-service-info-module "(in Ansible v2.9)") instead.
- vmware_host_ssl_facts use [vmware_host_ssl_info](https://docs.ansible.com/ansible/2.9/modules/vmware_host_ssl_info_module.html#vmware-host-ssl-info-module "(in Ansible v2.9)") instead.
- vmware_host_vmhba_facts use [vmware_host_vmhba_info](https://docs.ansible.com/ansible/2.9/modules/vmware_host_vmhba_info_module.html#vmware-host-vmhba-info-module "(in Ansible v2.9)") instead.
- vmware_host_vmnic_facts use [vmware_host_vmnic_info](https://docs.ansible.com/ansible/2.9/modules/vmware_host_vmnic_info_module.html#vmware-host-vmnic-info-module "(in Ansible v2.9)") instead.
- vmware_local_role_facts use [vmware_local_role_info](https://docs.ansible.com/ansible/2.9/modules/vmware_local_role_info_module.html#vmware-local-role-info-module "(in Ansible v2.9)") instead.
- vmware_local_user_facts use [vmware_local_user_info](https://docs.ansible.com/ansible/2.9/modules/vmware_local_user_info_module.html#vmware-local-user-info-module "(in Ansible v2.9)") instead.
- vmware_portgroup_facts use [vmware_portgroup_info](https://docs.ansible.com/ansible/2.9/modules/vmware_portgroup_info_module.html#vmware-portgroup-info-module "(in Ansible v2.9)") instead.
- vmware_resource_pool_facts use [vmware_resource_pool_info](https://docs.ansible.com/ansible/2.9/modules/vmware_resource_pool_info_module.html#vmware-resource-pool-info-module "(in Ansible v2.9)") instead.
- vmware_target_canonical_facts use [vmware_target_canonical_info](https://docs.ansible.com/ansible/2.9/modules/vmware_target_canonical_info_module.html#vmware-target-canonical-info-module "(in Ansible v2.9)") instead.
- vmware_vmkernel_facts use [vmware_vmkernel_info](https://docs.ansible.com/ansible/2.9/modules/vmware_vmkernel_info_module.html#vmware-vmkernel-info-module "(in Ansible v2.9)") instead.
- vmware_vswitch_facts use [vmware_vswitch_info](https://docs.ansible.com/ansible/2.9/modules/vmware_vswitch_info_module.html#vmware-vswitch-info-module "(in Ansible v2.9)") instead.
- vultr_account_facts use [vultr_account_info](https://docs.ansible.com/ansible/2.9/modules/vultr_account_info_module.html#vultr-account-info-module "(in Ansible v2.9)") instead.
- vultr_block_storage_facts use [vultr_block_storage_info](https://docs.ansible.com/ansible/2.9/modules/vultr_block_storage_info_module.html#vultr-block-storage-info-module "(in Ansible v2.9)") instead.
- vultr_dns_domain_facts use [vultr_dns_domain_info](https://docs.ansible.com/ansible/2.9/modules/vultr_dns_domain_info_module.html#vultr-dns-domain-info-module "(in Ansible v2.9)") instead.
- vultr_firewall_group_facts use [vultr_firewall_group_info](https://docs.ansible.com/ansible/2.9/modules/vultr_firewall_group_info_module.html#vultr-firewall-group-info-module "(in Ansible v2.9)") instead.
- vultr_network_facts use [vultr_network_info](https://docs.ansible.com/ansible/2.9/modules/vultr_network_info_module.html#vultr-network-info-module "(in Ansible v2.9)") instead.
- vultr_os_facts use [vultr_os_info](https://docs.ansible.com/ansible/2.9/modules/vultr_os_info_module.html#vultr-os-info-module "(in Ansible v2.9)") instead.
- vultr_plan_facts use [vultr_plan_info](https://docs.ansible.com/ansible/2.9/modules/vultr_plan_info_module.html#vultr-plan-info-module "(in Ansible v2.9)") instead.
- vultr_region_facts use [vultr_region_info](https://docs.ansible.com/ansible/2.9/modules/vultr_region_info_module.html#vultr-region-info-module "(in Ansible v2.9)") instead.
- vultr_server_facts use [vultr_server_info](https://docs.ansible.com/ansible/2.9/modules/vultr_server_info_module.html#vultr-server-info-module "(in Ansible v2.9)") instead.
- vultr_ssh_key_facts use [vultr_ssh_key_info](https://docs.ansible.com/ansible/2.9/modules/vultr_ssh_key_info_module.html#vultr-ssh-key-info-module "(in Ansible v2.9)") instead.
- vultr_startup_script_facts use [vultr_startup_script_info](https://docs.ansible.com/ansible/2.9/modules/vultr_startup_script_info_module.html#vultr-startup-script-info-module "(in Ansible v2.9)") instead.
- vultr_user_facts use [vultr_user_info](https://docs.ansible.com/ansible/2.9/modules/vultr_user_info_module.html#vultr-user-info-module "(in Ansible v2.9)") instead.
- vyos_interface use [vyos_interfaces](https://docs.ansible.com/ansible/2.9/modules/vyos_interfaces_module.html#vyos-interfaces-module "(in Ansible v2.9)") instead.
- vyos_l3_interface use [vyos_l3_interfaces](https://docs.ansible.com/ansible/2.9/modules/vyos_l3_interfaces_module.html#vyos-l3-interfaces-module "(in Ansible v2.9)") instead.
- vyos_linkagg use [vyos_lag_interfaces](https://docs.ansible.com/ansible/2.9/modules/vyos_lag_interfaces_module.html#vyos-lag-interfaces-module "(in Ansible v2.9)") instead.
- vyos_lldp use [vyos_lldp_global](https://docs.ansible.com/ansible/2.9/modules/vyos_lldp_global_module.html#vyos-lldp-global-module "(in Ansible v2.9)") instead.
- vyos_lldp_interface use [vyos_lldp_interfaces](https://docs.ansible.com/ansible/2.9/modules/vyos_lldp_interfaces_module.html#vyos-lldp-interfaces-module "(in Ansible v2.9)") instead.

The following functionality will be removed in Ansible 2.12. Please update update your playbooks accordingly.

- `vmware_cluster` DRS, HA and VSAN configuration; use [vmware_cluster_drs](https://docs.ansible.com/ansible/2.9/modules/vmware_cluster_drs_module.html#vmware-cluster-drs-module "(in Ansible v2.9)"), [vmware_cluster_ha](https://docs.ansible.com/ansible/2.9/modules/vmware_cluster_ha_module.html#vmware-cluster-ha-module "(in Ansible v2.9)") and [vmware_cluster_vsan](https://docs.ansible.com/ansible/2.9/modules/vmware_cluster_vsan_module.html#vmware-cluster-vsan-module "(in Ansible v2.9)") instead.

The following functionality will be removed in Ansible 2.13. Please update update your playbooks accordingly.

- `openssl_certificate` deprecates the `assertonly` provider.
  Please see the [openssl_certificate](https://docs.ansible.com/ansible/2.9/modules/openssl_certificate_module.html#openssl-certificate-module "(in Ansible v2.9)") documentation examples on how to
  replace the provider with the [openssl_certificate_info](https://docs.ansible.com/ansible/2.9/modules/openssl_certificate_info_module.html#openssl-certificate-info-module "(in Ansible v2.9)"),
  [openssl_csr_info](https://docs.ansible.com/ansible/2.9/modules/openssl_csr_info_module.html#openssl-csr-info-module "(in Ansible v2.9)"), [openssl_privatekey_info](https://docs.ansible.com/ansible/2.9/modules/openssl_privatekey_info_module.html#openssl-privatekey-info-module "(in Ansible v2.9)")
  and [assert](../collections/ansible/builtin/assert_module.md#assert-module) modules.

For the following modules, the PyOpenSSL-based backend `pyopenssl` has been deprecated and will be
removed in Ansible 2.13:

- [get_certificate](https://docs.ansible.com/ansible/2.9/modules/get_certificate_module.html#get-certificate-module "(in Ansible v2.9)")
- [openssl_certificate](https://docs.ansible.com/ansible/2.9/modules/openssl_certificate_module.html#openssl-certificate-module "(in Ansible v2.9)")
- [openssl_certificate_info](https://docs.ansible.com/ansible/2.9/modules/openssl_certificate_info_module.html#openssl-certificate-info-module "(in Ansible v2.9)")
- [openssl_csr](https://docs.ansible.com/ansible/2.9/modules/openssl_csr_module.html#openssl-csr-module "(in Ansible v2.9)")
- [openssl_csr_info](https://docs.ansible.com/ansible/2.9/modules/openssl_csr_info_module.html#openssl-csr-info-module "(in Ansible v2.9)")
- [openssl_privatekey](https://docs.ansible.com/ansible/2.9/modules/openssl_privatekey_module.html#openssl-privatekey-module "(in Ansible v2.9)")
- [openssl_privatekey_info](https://docs.ansible.com/ansible/2.9/modules/openssl_privatekey_info_module.html#openssl-privatekey-info-module "(in Ansible v2.9)")
- [openssl_publickey](https://docs.ansible.com/ansible/2.9/modules/openssl_publickey_module.html#openssl-publickey-module "(in Ansible v2.9)")

#### [Renamed modules](porting_guide_2.9.md#id13)

The following modules have been renamed. The old name is deprecated and will
be removed in Ansible 2.13. Please update update your playbooks accordingly.

- The `ali_instance_facts` module was renamed to [ali_instance_info](https://docs.ansible.com/ansible/2.9/modules/ali_instance_info_module.html#ali-instance-info-module "(in Ansible v2.9)").
- The `aws_acm_facts` module was renamed to [aws_acm_info](https://docs.ansible.com/ansible/2.9/modules/aws_acm_info_module.html#aws-acm-info-module "(in Ansible v2.9)").
- The `aws_az_facts` module was renamed to [aws_az_info](https://docs.ansible.com/ansible/2.9/modules/aws_az_info_module.html#aws-az-info-module "(in Ansible v2.9)").
- The `aws_caller_facts` module was renamed to [aws_caller_info](https://docs.ansible.com/ansible/2.9/modules/aws_caller_info_module.html#aws-caller-info-module "(in Ansible v2.9)").
- The `aws_kms_facts` module was renamed to [aws_kms_info](https://docs.ansible.com/ansible/2.9/modules/aws_kms_info_module.html#aws-kms-info-module "(in Ansible v2.9)").
- The `aws_region_facts` module was renamed to [aws_region_info](https://docs.ansible.com/ansible/2.9/modules/aws_region_info_module.html#aws-region-info-module "(in Ansible v2.9)").
- The `aws_s3_bucket_facts` module was renamed to [aws_s3_bucket_info](https://docs.ansible.com/ansible/2.9/modules/aws_s3_bucket_info_module.html#aws-s3-bucket-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `aws_sgw_facts` module was renamed to [aws_sgw_info](https://docs.ansible.com/ansible/2.9/modules/aws_sgw_info_module.html#aws-sgw-info-module "(in Ansible v2.9)").
- The `aws_waf_facts` module was renamed to [aws_waf_info](https://docs.ansible.com/ansible/2.9/modules/aws_waf_info_module.html#aws-waf-info-module "(in Ansible v2.9)").
- The `azure_rm_aks_facts` module was renamed to [azure_rm_aks_info](https://docs.ansible.com/ansible/2.9/modules/azure_rm_aks_info_module.html#azure-rm-aks-info-module "(in Ansible v2.9)").
- The `azure_rm_aksversion_facts` module was renamed to [azure_rm_aksversion_info](https://docs.ansible.com/ansible/2.9/modules/azure_rm_aksversion_info_module.html#azure-rm-aksversion-info-module "(in Ansible v2.9)").
- The `azure_rm_applicationsecuritygroup_facts` module was renamed to [azure_rm_applicationsecuritygroup_info](https://docs.ansible.com/ansible/2.9/modules/azure_rm_applicationsecuritygroup_info_module.html#azure-rm-applicationsecuritygroup-info-module "(in Ansible v2.9)").
- The `azure_rm_appserviceplan_facts` module was renamed to [azure_rm_appserviceplan_info](https://docs.ansible.com/ansible/2.9/modules/azure_rm_appserviceplan_info_module.html#azure-rm-appserviceplan-info-module "(in Ansible v2.9)").
- The `azure_rm_automationaccount_facts` module was renamed to [azure_rm_automationaccount_info](https://docs.ansible.com/ansible/2.9/modules/azure_rm_automationaccount_info_module.html#azure-rm-automationaccount-info-module "(in Ansible v2.9)").
- The `azure_rm_autoscale_facts` module was renamed to [azure_rm_autoscale_info](https://docs.ansible.com/ansible/2.9/modules/azure_rm_autoscale_info_module.html#azure-rm-autoscale-info-module "(in Ansible v2.9)").
- The `azure_rm_availabilityset_facts` module was renamed to [azure_rm_availabilityset_info](https://docs.ansible.com/ansible/2.9/modules/azure_rm_availabilityset_info_module.html#azure-rm-availabilityset-info-module "(in Ansible v2.9)").
- The `azure_rm_cdnendpoint_facts` module was renamed to [azure_rm_cdnendpoint_info](https://docs.ansible.com/ansible/2.9/modules/azure_rm_cdnendpoint_info_module.html#azure-rm-cdnendpoint-info-module "(in Ansible v2.9)").
- The `azure_rm_cdnprofile_facts` module was renamed to [azure_rm_cdnprofile_info](https://docs.ansible.com/ansible/2.9/modules/azure_rm_cdnprofile_info_module.html#azure-rm-cdnprofile-info-module "(in Ansible v2.9)").
- The `azure_rm_containerinstance_facts` module was renamed to [azure_rm_containerinstance_info](https://docs.ansible.com/ansible/2.9/modules/azure_rm_containerinstance_info_module.html#azure-rm-containerinstance-info-module "(in Ansible v2.9)").
- The `azure_rm_containerregistry_facts` module was renamed to [azure_rm_containerregistry_info](https://docs.ansible.com/ansible/2.9/modules/azure_rm_containerregistry_info_module.html#azure-rm-containerregistry-info-module "(in Ansible v2.9)").
- The `azure_rm_cosmosdbaccount_facts` module was renamed to [azure_rm_cosmosdbaccount_info](https://docs.ansible.com/ansible/2.9/modules/azure_rm_cosmosdbaccount_info_module.html#azure-rm-cosmosdbaccount-info-module "(in Ansible v2.9)").
- The `azure_rm_deployment_facts` module was renamed to [azure_rm_deployment_info](https://docs.ansible.com/ansible/2.9/modules/azure_rm_deployment_info_module.html#azure-rm-deployment-info-module "(in Ansible v2.9)").
- The `azure_rm_resourcegroup_facts` module was renamed to [azure_rm_resourcegroup_info](https://docs.ansible.com/ansible/2.9/modules/azure_rm_resourcegroup_info_module.html#azure-rm-resourcegroup-info-module "(in Ansible v2.9)").
- The `bigip_device_facts` module was renamed to [bigip_device_info](https://docs.ansible.com/ansible/2.9/modules/bigip_device_info_module.html#bigip-device-info-module "(in Ansible v2.9)").
- The `bigiq_device_facts` module was renamed to [bigiq_device_info](https://docs.ansible.com/ansible/2.9/modules/bigiq_device_info_module.html#bigiq-device-info-module "(in Ansible v2.9)").
- The `cloudformation_facts` module was renamed to [cloudformation_info](https://docs.ansible.com/ansible/2.9/modules/cloudformation_info_module.html#cloudformation-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `cloudfront_facts` module was renamed to [cloudfront_info](https://docs.ansible.com/ansible/2.9/modules/cloudfront_info_module.html#cloudfront-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `cloudwatchlogs_log_group_facts` module was renamed to [cloudwatchlogs_log_group_info](https://docs.ansible.com/ansible/2.9/modules/cloudwatchlogs_log_group_info_module.html#cloudwatchlogs-log-group-info-module "(in Ansible v2.9)").
- The `digital_ocean_account_facts` module was renamed to [digital_ocean_account_info](https://docs.ansible.com/ansible/2.9/modules/digital_ocean_account_info_module.html#digital-ocean-account-info-module "(in Ansible v2.9)").
- The `digital_ocean_certificate_facts` module was renamed to [digital_ocean_certificate_info](https://docs.ansible.com/ansible/2.9/modules/digital_ocean_certificate_info_module.html#digital-ocean-certificate-info-module "(in Ansible v2.9)").
- The `digital_ocean_domain_facts` module was renamed to [digital_ocean_domain_info](https://docs.ansible.com/ansible/2.9/modules/digital_ocean_domain_info_module.html#digital-ocean-domain-info-module "(in Ansible v2.9)").
- The `digital_ocean_firewall_facts` module was renamed to [digital_ocean_firewall_info](https://docs.ansible.com/ansible/2.9/modules/digital_ocean_firewall_info_module.html#digital-ocean-firewall-info-module "(in Ansible v2.9)").
- The `digital_ocean_floating_ip_facts` module was renamed to [digital_ocean_floating_ip_info](https://docs.ansible.com/ansible/2.9/modules/digital_ocean_floating_ip_info_module.html#digital-ocean-floating-ip-info-module "(in Ansible v2.9)").
- The `digital_ocean_image_facts` module was renamed to [digital_ocean_image_info](https://docs.ansible.com/ansible/2.9/modules/digital_ocean_image_info_module.html#digital-ocean-image-info-module "(in Ansible v2.9)").
- The `digital_ocean_load_balancer_facts` module was renamed to [digital_ocean_load_balancer_info](https://docs.ansible.com/ansible/2.9/modules/digital_ocean_load_balancer_info_module.html#digital-ocean-load-balancer-info-module "(in Ansible v2.9)").
- The `digital_ocean_region_facts` module was renamed to [digital_ocean_region_info](https://docs.ansible.com/ansible/2.9/modules/digital_ocean_region_info_module.html#digital-ocean-region-info-module "(in Ansible v2.9)").
- The `digital_ocean_size_facts` module was renamed to [digital_ocean_size_info](https://docs.ansible.com/ansible/2.9/modules/digital_ocean_size_info_module.html#digital-ocean-size-info-module "(in Ansible v2.9)").
- The `digital_ocean_snapshot_facts` module was renamed to [digital_ocean_snapshot_info](https://docs.ansible.com/ansible/2.9/modules/digital_ocean_snapshot_info_module.html#digital-ocean-snapshot-info-module "(in Ansible v2.9)").
- The `digital_ocean_tag_facts` module was renamed to [digital_ocean_tag_info](https://docs.ansible.com/ansible/2.9/modules/digital_ocean_tag_info_module.html#digital-ocean-tag-info-module "(in Ansible v2.9)").
- The `digital_ocean_volume_facts` module was renamed to [digital_ocean_volume_info](https://docs.ansible.com/ansible/2.9/modules/digital_ocean_volume_info_module.html#digital-ocean-volume-info-module "(in Ansible v2.9)").
- The `ec2_ami_facts` module was renamed to [ec2_ami_info](https://docs.ansible.com/ansible/2.9/modules/ec2_ami_info_module.html#ec2-ami-info-module "(in Ansible v2.9)").
- The `ec2_asg_facts` module was renamed to [ec2_asg_info](https://docs.ansible.com/ansible/2.9/modules/ec2_asg_info_module.html#ec2-asg-info-module "(in Ansible v2.9)").
- The `ec2_customer_gateway_facts` module was renamed to [ec2_customer_gateway_info](https://docs.ansible.com/ansible/2.9/modules/ec2_customer_gateway_info_module.html#ec2-customer-gateway-info-module "(in Ansible v2.9)").
- The `ec2_eip_facts` module was renamed to [ec2_eip_info](https://docs.ansible.com/ansible/2.9/modules/ec2_eip_info_module.html#ec2-eip-info-module "(in Ansible v2.9)").
- The `ec2_elb_facts` module was renamed to [ec2_elb_info](https://docs.ansible.com/ansible/2.9/modules/ec2_elb_info_module.html#ec2-elb-info-module "(in Ansible v2.9)").
- The `ec2_eni_facts` module was renamed to [ec2_eni_info](https://docs.ansible.com/ansible/2.9/modules/ec2_eni_info_module.html#ec2-eni-info-module "(in Ansible v2.9)").
- The `ec2_group_facts` module was renamed to [ec2_group_info](https://docs.ansible.com/ansible/2.9/modules/ec2_group_info_module.html#ec2-group-info-module "(in Ansible v2.9)").
- The `ec2_instance_facts` module was renamed to [ec2_instance_info](https://docs.ansible.com/ansible/2.9/modules/ec2_instance_info_module.html#ec2-instance-info-module "(in Ansible v2.9)").
- The `ec2_lc_facts` module was renamed to [ec2_lc_info](https://docs.ansible.com/ansible/2.9/modules/ec2_lc_info_module.html#ec2-lc-info-module "(in Ansible v2.9)").
- The `ec2_placement_group_facts` module was renamed to [ec2_placement_group_info](https://docs.ansible.com/ansible/2.9/modules/ec2_placement_group_info_module.html#ec2-placement-group-info-module "(in Ansible v2.9)").
- The `ec2_snapshot_facts` module was renamed to [ec2_snapshot_info](https://docs.ansible.com/ansible/2.9/modules/ec2_snapshot_info_module.html#ec2-snapshot-info-module "(in Ansible v2.9)").
- The `ec2_vol_facts` module was renamed to [ec2_vol_info](https://docs.ansible.com/ansible/2.9/modules/ec2_vol_info_module.html#ec2-vol-info-module "(in Ansible v2.9)").
- The `ec2_vpc_dhcp_option_facts` module was renamed to [ec2_vpc_dhcp_option_info](https://docs.ansible.com/ansible/2.9/modules/ec2_vpc_dhcp_option_info_module.html#ec2-vpc-dhcp-option-info-module "(in Ansible v2.9)").
- The `ec2_vpc_endpoint_facts` module was renamed to [ec2_vpc_endpoint_info](https://docs.ansible.com/ansible/2.9/modules/ec2_vpc_endpoint_info_module.html#ec2-vpc-endpoint-info-module "(in Ansible v2.9)").
- The `ec2_vpc_igw_facts` module was renamed to [ec2_vpc_igw_info](https://docs.ansible.com/ansible/2.9/modules/ec2_vpc_igw_info_module.html#ec2-vpc-igw-info-module "(in Ansible v2.9)").
- The `ec2_vpc_nacl_facts` module was renamed to [ec2_vpc_nacl_info](https://docs.ansible.com/ansible/2.9/modules/ec2_vpc_nacl_info_module.html#ec2-vpc-nacl-info-module "(in Ansible v2.9)").
- The `ec2_vpc_nat_gateway_facts` module was renamed to [ec2_vpc_nat_gateway_info](https://docs.ansible.com/ansible/2.9/modules/ec2_vpc_nat_gateway_info_module.html#ec2-vpc-nat-gateway-info-module "(in Ansible v2.9)").
- The `ec2_vpc_net_facts` module was renamed to [ec2_vpc_net_info](https://docs.ansible.com/ansible/2.9/modules/ec2_vpc_net_info_module.html#ec2-vpc-net-info-module "(in Ansible v2.9)").
- The `ec2_vpc_peering_facts` module was renamed to [ec2_vpc_peering_info](https://docs.ansible.com/ansible/2.9/modules/ec2_vpc_peering_info_module.html#ec2-vpc-peering-info-module "(in Ansible v2.9)").
- The `ec2_vpc_route_table_facts` module was renamed to [ec2_vpc_route_table_info](https://docs.ansible.com/ansible/2.9/modules/ec2_vpc_route_table_info_module.html#ec2-vpc-route-table-info-module "(in Ansible v2.9)").
- The `ec2_vpc_subnet_facts` module was renamed to [ec2_vpc_subnet_info](https://docs.ansible.com/ansible/2.9/modules/ec2_vpc_subnet_info_module.html#ec2-vpc-subnet-info-module "(in Ansible v2.9)").
- The `ec2_vpc_vgw_facts` module was renamed to [ec2_vpc_vgw_info](https://docs.ansible.com/ansible/2.9/modules/ec2_vpc_vgw_info_module.html#ec2-vpc-vgw-info-module "(in Ansible v2.9)").
- The `ec2_vpc_vpn_facts` module was renamed to [ec2_vpc_vpn_info](https://docs.ansible.com/ansible/2.9/modules/ec2_vpc_vpn_info_module.html#ec2-vpc-vpn-info-module "(in Ansible v2.9)").
- The `ecs_service_facts` module was renamed to [ecs_service_info](https://docs.ansible.com/ansible/2.9/modules/ecs_service_info_module.html#ecs-service-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ecs_taskdefinition_facts` module was renamed to [ecs_taskdefinition_info](https://docs.ansible.com/ansible/2.9/modules/ecs_taskdefinition_info_module.html#ecs-taskdefinition-info-module "(in Ansible v2.9)").
- The `efs_facts` module was renamed to [efs_info](https://docs.ansible.com/ansible/2.9/modules/efs_info_module.html#efs-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `elasticache_facts` module was renamed to [elasticache_info](https://docs.ansible.com/ansible/2.9/modules/elasticache_info_module.html#elasticache-info-module "(in Ansible v2.9)").
- The `elb_application_lb_facts` module was renamed to [elb_application_lb_info](https://docs.ansible.com/ansible/2.9/modules/elb_application_lb_info_module.html#elb-application-lb-info-module "(in Ansible v2.9)").
- The `elb_classic_lb_facts` module was renamed to [elb_classic_lb_info](https://docs.ansible.com/ansible/2.9/modules/elb_classic_lb_info_module.html#elb-classic-lb-info-module "(in Ansible v2.9)").
- The `elb_target_facts` module was renamed to [elb_target_info](https://docs.ansible.com/ansible/2.9/modules/elb_target_info_module.html#elb-target-info-module "(in Ansible v2.9)").
- The `elb_target_group_facts` module was renamed to [elb_target_group_info](https://docs.ansible.com/ansible/2.9/modules/elb_target_group_info_module.html#elb-target-group-info-module "(in Ansible v2.9)").
- The `gcp_bigquery_dataset_facts` module was renamed to [gcp_bigquery_dataset_info](https://docs.ansible.com/ansible/2.9/modules/gcp_bigquery_dataset_info_module.html#gcp-bigquery-dataset-info-module "(in Ansible v2.9)").
- The `gcp_bigquery_table_facts` module was renamed to [gcp_bigquery_table_info](https://docs.ansible.com/ansible/2.9/modules/gcp_bigquery_table_info_module.html#gcp-bigquery-table-info-module "(in Ansible v2.9)").
- The `gcp_cloudbuild_trigger_facts` module was renamed to [gcp_cloudbuild_trigger_info](https://docs.ansible.com/ansible/2.9/modules/gcp_cloudbuild_trigger_info_module.html#gcp-cloudbuild-trigger-info-module "(in Ansible v2.9)").
- The `gcp_compute_address_facts` module was renamed to [gcp_compute_address_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_address_info_module.html#gcp-compute-address-info-module "(in Ansible v2.9)").
- The `gcp_compute_backend_bucket_facts` module was renamed to [gcp_compute_backend_bucket_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_backend_bucket_info_module.html#gcp-compute-backend-bucket-info-module "(in Ansible v2.9)").
- The `gcp_compute_backend_service_facts` module was renamed to [gcp_compute_backend_service_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_backend_service_info_module.html#gcp-compute-backend-service-info-module "(in Ansible v2.9)").
- The `gcp_compute_disk_facts` module was renamed to [gcp_compute_disk_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_disk_info_module.html#gcp-compute-disk-info-module "(in Ansible v2.9)").
- The `gcp_compute_firewall_facts` module was renamed to [gcp_compute_firewall_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_firewall_info_module.html#gcp-compute-firewall-info-module "(in Ansible v2.9)").
- The `gcp_compute_forwarding_rule_facts` module was renamed to [gcp_compute_forwarding_rule_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_forwarding_rule_info_module.html#gcp-compute-forwarding-rule-info-module "(in Ansible v2.9)").
- The `gcp_compute_global_address_facts` module was renamed to [gcp_compute_global_address_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_global_address_info_module.html#gcp-compute-global-address-info-module "(in Ansible v2.9)").
- The `gcp_compute_global_forwarding_rule_facts` module was renamed to [gcp_compute_global_forwarding_rule_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_global_forwarding_rule_info_module.html#gcp-compute-global-forwarding-rule-info-module "(in Ansible v2.9)").
- The `gcp_compute_health_check_facts` module was renamed to [gcp_compute_health_check_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_health_check_info_module.html#gcp-compute-health-check-info-module "(in Ansible v2.9)").
- The `gcp_compute_http_health_check_facts` module was renamed to [gcp_compute_http_health_check_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_http_health_check_info_module.html#gcp-compute-http-health-check-info-module "(in Ansible v2.9)").
- The `gcp_compute_https_health_check_facts` module was renamed to [gcp_compute_https_health_check_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_https_health_check_info_module.html#gcp-compute-https-health-check-info-module "(in Ansible v2.9)").
- The `gcp_compute_image_facts` module was renamed to [gcp_compute_image_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_image_info_module.html#gcp-compute-image-info-module "(in Ansible v2.9)").
- The `gcp_compute_instance_facts` module was renamed to [gcp_compute_instance_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_instance_info_module.html#gcp-compute-instance-info-module "(in Ansible v2.9)").
- The `gcp_compute_instance_group_facts` module was renamed to [gcp_compute_instance_group_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_instance_group_info_module.html#gcp-compute-instance-group-info-module "(in Ansible v2.9)").
- The `gcp_compute_instance_group_manager_facts` module was renamed to [gcp_compute_instance_group_manager_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_instance_group_manager_info_module.html#gcp-compute-instance-group-manager-info-module "(in Ansible v2.9)").
- The `gcp_compute_instance_template_facts` module was renamed to [gcp_compute_instance_template_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_instance_template_info_module.html#gcp-compute-instance-template-info-module "(in Ansible v2.9)").
- The `gcp_compute_interconnect_attachment_facts` module was renamed to [gcp_compute_interconnect_attachment_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_interconnect_attachment_info_module.html#gcp-compute-interconnect-attachment-info-module "(in Ansible v2.9)").
- The `gcp_compute_network_facts` module was renamed to [gcp_compute_network_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_network_info_module.html#gcp-compute-network-info-module "(in Ansible v2.9)").
- The `gcp_compute_region_disk_facts` module was renamed to [gcp_compute_region_disk_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_region_disk_info_module.html#gcp-compute-region-disk-info-module "(in Ansible v2.9)").
- The `gcp_compute_route_facts` module was renamed to [gcp_compute_route_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_route_info_module.html#gcp-compute-route-info-module "(in Ansible v2.9)").
- The `gcp_compute_router_facts` module was renamed to [gcp_compute_router_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_router_info_module.html#gcp-compute-router-info-module "(in Ansible v2.9)").
- The `gcp_compute_ssl_certificate_facts` module was renamed to [gcp_compute_ssl_certificate_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_ssl_certificate_info_module.html#gcp-compute-ssl-certificate-info-module "(in Ansible v2.9)").
- The `gcp_compute_ssl_policy_facts` module was renamed to [gcp_compute_ssl_policy_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_ssl_policy_info_module.html#gcp-compute-ssl-policy-info-module "(in Ansible v2.9)").
- The `gcp_compute_subnetwork_facts` module was renamed to [gcp_compute_subnetwork_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_subnetwork_info_module.html#gcp-compute-subnetwork-info-module "(in Ansible v2.9)").
- The `gcp_compute_target_http_proxy_facts` module was renamed to [gcp_compute_target_http_proxy_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_target_http_proxy_info_module.html#gcp-compute-target-http-proxy-info-module "(in Ansible v2.9)").
- The `gcp_compute_target_https_proxy_facts` module was renamed to [gcp_compute_target_https_proxy_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_target_https_proxy_info_module.html#gcp-compute-target-https-proxy-info-module "(in Ansible v2.9)").
- The `gcp_compute_target_pool_facts` module was renamed to [gcp_compute_target_pool_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_target_pool_info_module.html#gcp-compute-target-pool-info-module "(in Ansible v2.9)").
- The `gcp_compute_target_ssl_proxy_facts` module was renamed to [gcp_compute_target_ssl_proxy_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_target_ssl_proxy_info_module.html#gcp-compute-target-ssl-proxy-info-module "(in Ansible v2.9)").
- The `gcp_compute_target_tcp_proxy_facts` module was renamed to [gcp_compute_target_tcp_proxy_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_target_tcp_proxy_info_module.html#gcp-compute-target-tcp-proxy-info-module "(in Ansible v2.9)").
- The `gcp_compute_target_vpn_gateway_facts` module was renamed to [gcp_compute_target_vpn_gateway_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_target_vpn_gateway_info_module.html#gcp-compute-target-vpn-gateway-info-module "(in Ansible v2.9)").
- The `gcp_compute_url_map_facts` module was renamed to [gcp_compute_url_map_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_url_map_info_module.html#gcp-compute-url-map-info-module "(in Ansible v2.9)").
- The `gcp_compute_vpn_tunnel_facts` module was renamed to [gcp_compute_vpn_tunnel_info](https://docs.ansible.com/ansible/2.9/modules/gcp_compute_vpn_tunnel_info_module.html#gcp-compute-vpn-tunnel-info-module "(in Ansible v2.9)").
- The `gcp_container_cluster_facts` module was renamed to [gcp_container_cluster_info](https://docs.ansible.com/ansible/2.9/modules/gcp_container_cluster_info_module.html#gcp-container-cluster-info-module "(in Ansible v2.9)").
- The `gcp_container_node_pool_facts` module was renamed to [gcp_container_node_pool_info](https://docs.ansible.com/ansible/2.9/modules/gcp_container_node_pool_info_module.html#gcp-container-node-pool-info-module "(in Ansible v2.9)").
- The `gcp_dns_managed_zone_facts` module was renamed to [gcp_dns_managed_zone_info](https://docs.ansible.com/ansible/2.9/modules/gcp_dns_managed_zone_info_module.html#gcp-dns-managed-zone-info-module "(in Ansible v2.9)").
- The `gcp_dns_resource_record_set_facts` module was renamed to [gcp_dns_resource_record_set_info](https://docs.ansible.com/ansible/2.9/modules/gcp_dns_resource_record_set_info_module.html#gcp-dns-resource-record-set-info-module "(in Ansible v2.9)").
- The `gcp_iam_role_facts` module was renamed to [gcp_iam_role_info](https://docs.ansible.com/ansible/2.9/modules/gcp_iam_role_info_module.html#gcp-iam-role-info-module "(in Ansible v2.9)").
- The `gcp_iam_service_account_facts` module was renamed to [gcp_iam_service_account_info](https://docs.ansible.com/ansible/2.9/modules/gcp_iam_service_account_info_module.html#gcp-iam-service-account-info-module "(in Ansible v2.9)").
- The `gcp_pubsub_subscription_facts` module was renamed to [gcp_pubsub_subscription_info](https://docs.ansible.com/ansible/2.9/modules/gcp_pubsub_subscription_info_module.html#gcp-pubsub-subscription-info-module "(in Ansible v2.9)").
- The `gcp_pubsub_topic_facts` module was renamed to [gcp_pubsub_topic_info](https://docs.ansible.com/ansible/2.9/modules/gcp_pubsub_topic_info_module.html#gcp-pubsub-topic-info-module "(in Ansible v2.9)").
- The `gcp_redis_instance_facts` module was renamed to [gcp_redis_instance_info](https://docs.ansible.com/ansible/2.9/modules/gcp_redis_instance_info_module.html#gcp-redis-instance-info-module "(in Ansible v2.9)").
- The `gcp_resourcemanager_project_facts` module was renamed to [gcp_resourcemanager_project_info](https://docs.ansible.com/ansible/2.9/modules/gcp_resourcemanager_project_info_module.html#gcp-resourcemanager-project-info-module "(in Ansible v2.9)").
- The `gcp_sourcerepo_repository_facts` module was renamed to [gcp_sourcerepo_repository_info](https://docs.ansible.com/ansible/2.9/modules/gcp_sourcerepo_repository_info_module.html#gcp-sourcerepo-repository-info-module "(in Ansible v2.9)").
- The `gcp_spanner_database_facts` module was renamed to [gcp_spanner_database_info](https://docs.ansible.com/ansible/2.9/modules/gcp_spanner_database_info_module.html#gcp-spanner-database-info-module "(in Ansible v2.9)").
- The `gcp_spanner_instance_facts` module was renamed to [gcp_spanner_instance_info](https://docs.ansible.com/ansible/2.9/modules/gcp_spanner_instance_info_module.html#gcp-spanner-instance-info-module "(in Ansible v2.9)").
- The `gcp_sql_database_facts` module was renamed to [gcp_sql_database_info](https://docs.ansible.com/ansible/2.9/modules/gcp_sql_database_info_module.html#gcp-sql-database-info-module "(in Ansible v2.9)").
- The `gcp_sql_instance_facts` module was renamed to [gcp_sql_instance_info](https://docs.ansible.com/ansible/2.9/modules/gcp_sql_instance_info_module.html#gcp-sql-instance-info-module "(in Ansible v2.9)").
- The `gcp_sql_user_facts` module was renamed to [gcp_sql_user_info](https://docs.ansible.com/ansible/2.9/modules/gcp_sql_user_info_module.html#gcp-sql-user-info-module "(in Ansible v2.9)").
- The `gcp_tpu_node_facts` module was renamed to [gcp_tpu_node_info](https://docs.ansible.com/ansible/2.9/modules/gcp_tpu_node_info_module.html#gcp-tpu-node-info-module "(in Ansible v2.9)").
- The `gcpubsub_facts` module was renamed to [gcpubsub_info](https://docs.ansible.com/ansible/2.9/modules/gcpubsub_info_module.html#gcpubsub-info-module "(in Ansible v2.9)").
- The `github_webhook_facts` module was renamed to [github_webhook_info](https://docs.ansible.com/ansible/2.9/modules/github_webhook_info_module.html#github-webhook-info-module "(in Ansible v2.9)").
- The `gluster_heal_facts` module was renamed to [gluster_heal_info](https://docs.ansible.com/ansible/2.9/modules/gluster_heal_info_module.html#gluster-heal-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `hcloud_datacenter_facts` module was renamed to [hcloud_datacenter_info](https://docs.ansible.com/ansible/2.9/modules/hcloud_datacenter_info_module.html#hcloud-datacenter-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `hcloud_floating_ip_facts` module was renamed to [hcloud_floating_ip_info](https://docs.ansible.com/ansible/2.9/modules/hcloud_floating_ip_info_module.html#hcloud-floating-ip-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `hcloud_image_facts` module was renamed to [hcloud_image_info](https://docs.ansible.com/ansible/2.9/modules/hcloud_image_info_module.html#hcloud-image-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `hcloud_location_facts` module was renamed to [hcloud_location_info](https://docs.ansible.com/ansible/2.9/modules/hcloud_location_info_module.html#hcloud-location-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `hcloud_server_facts` module was renamed to [hcloud_server_info](https://docs.ansible.com/ansible/2.9/modules/hcloud_server_info_module.html#hcloud-server-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `hcloud_server_type_facts` module was renamed to [hcloud_server_type_info](https://docs.ansible.com/ansible/2.9/modules/hcloud_server_type_info_module.html#hcloud-server-type-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `hcloud_ssh_key_facts` module was renamed to [hcloud_ssh_key_info](https://docs.ansible.com/ansible/2.9/modules/hcloud_ssh_key_info_module.html#hcloud-ssh-key-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `hcloud_volume_facts` module was renamed to [hcloud_volume_info](https://docs.ansible.com/ansible/2.9/modules/hcloud_volume_info_module.html#hcloud-volume-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `hpilo_facts` module was renamed to [hpilo_info](https://docs.ansible.com/ansible/2.9/modules/hpilo_info_module.html#hpilo-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `iam_mfa_device_facts` module was renamed to [iam_mfa_device_info](https://docs.ansible.com/ansible/2.9/modules/iam_mfa_device_info_module.html#iam-mfa-device-info-module "(in Ansible v2.9)").
- The `iam_role_facts` module was renamed to [iam_role_info](https://docs.ansible.com/ansible/2.9/modules/iam_role_info_module.html#iam-role-info-module "(in Ansible v2.9)").
- The `iam_server_certificate_facts` module was renamed to [iam_server_certificate_info](https://docs.ansible.com/ansible/2.9/modules/iam_server_certificate_info_module.html#iam-server-certificate-info-module "(in Ansible v2.9)").
- The `idrac_redfish_facts` module was renamed to [idrac_redfish_info](https://docs.ansible.com/ansible/2.9/modules/idrac_redfish_info_module.html#idrac-redfish-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `intersight_facts` module was renamed to [intersight_info](https://docs.ansible.com/ansible/2.9/modules/intersight_info_module.html#intersight-info-module "(in Ansible v2.9)").
- The `jenkins_job_facts` module was renamed to [jenkins_job_info](https://docs.ansible.com/ansible/2.9/modules/jenkins_job_info_module.html#jenkins-job-info-module "(in Ansible v2.9)").
- The `k8s_facts` module was renamed to [k8s_info](https://docs.ansible.com/ansible/2.9/modules/k8s_info_module.html#k8s-info-module "(in Ansible v2.9)").
- The `memset_memstore_facts` module was renamed to [memset_memstore_info](https://docs.ansible.com/ansible/2.9/modules/memset_memstore_info_module.html#memset-memstore-info-module "(in Ansible v2.9)").
- The `memset_server_facts` module was renamed to [memset_server_info](https://docs.ansible.com/ansible/2.9/modules/memset_server_info_module.html#memset-server-info-module "(in Ansible v2.9)").
- The `one_image_facts` module was renamed to [one_image_info](https://docs.ansible.com/ansible/2.9/modules/one_image_info_module.html#one-image-info-module "(in Ansible v2.9)").
- The `onepassword_facts` module was renamed to [onepassword_info](https://docs.ansible.com/ansible/2.9/modules/onepassword_info_module.html#onepassword-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `oneview_datacenter_facts` module was renamed to [oneview_datacenter_info](https://docs.ansible.com/ansible/2.9/modules/oneview_datacenter_info_module.html#oneview-datacenter-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `oneview_enclosure_facts` module was renamed to [oneview_enclosure_info](https://docs.ansible.com/ansible/2.9/modules/oneview_enclosure_info_module.html#oneview-enclosure-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `oneview_ethernet_network_facts` module was renamed to [oneview_ethernet_network_info](https://docs.ansible.com/ansible/2.9/modules/oneview_ethernet_network_info_module.html#oneview-ethernet-network-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `oneview_fc_network_facts` module was renamed to [oneview_fc_network_info](https://docs.ansible.com/ansible/2.9/modules/oneview_fc_network_info_module.html#oneview-fc-network-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `oneview_fcoe_network_facts` module was renamed to [oneview_fcoe_network_info](https://docs.ansible.com/ansible/2.9/modules/oneview_fcoe_network_info_module.html#oneview-fcoe-network-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `oneview_logical_interconnect_group_facts` module was renamed to [oneview_logical_interconnect_group_info](https://docs.ansible.com/ansible/2.9/modules/oneview_logical_interconnect_group_info_module.html#oneview-logical-interconnect-group-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `oneview_network_set_facts` module was renamed to [oneview_network_set_info](https://docs.ansible.com/ansible/2.9/modules/oneview_network_set_info_module.html#oneview-network-set-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `oneview_san_manager_facts` module was renamed to [oneview_san_manager_info](https://docs.ansible.com/ansible/2.9/modules/oneview_san_manager_info_module.html#oneview-san-manager-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `os_flavor_facts` module was renamed to [os_flavor_info](https://docs.ansible.com/ansible/2.9/modules/os_flavor_info_module.html#os-flavor-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `os_image_facts` module was renamed to [os_image_info](https://docs.ansible.com/ansible/2.9/modules/os_image_info_module.html#os-image-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `os_keystone_domain_facts` module was renamed to [os_keystone_domain_info](https://docs.ansible.com/ansible/2.9/modules/os_keystone_domain_info_module.html#os-keystone-domain-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `os_networks_facts` module was renamed to [os_networks_info](https://docs.ansible.com/ansible/2.9/modules/os_networks_info_module.html#os-networks-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `os_port_facts` module was renamed to [os_port_info](https://docs.ansible.com/ansible/2.9/modules/os_port_info_module.html#os-port-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `os_project_facts` module was renamed to [os_project_info](https://docs.ansible.com/ansible/2.9/modules/os_project_info_module.html#os-project-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `os_server_facts` module was renamed to [os_server_info](https://docs.ansible.com/ansible/2.9/modules/os_server_info_module.html#os-server-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `os_subnets_facts` module was renamed to [os_subnets_info](https://docs.ansible.com/ansible/2.9/modules/os_subnets_info_module.html#os-subnets-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `os_user_facts` module was renamed to [os_user_info](https://docs.ansible.com/ansible/2.9/modules/os_user_info_module.html#os-user-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ovirt_affinity_label_facts` module was renamed to [ovirt_affinity_label_info](https://docs.ansible.com/ansible/2.9/modules/ovirt_affinity_label_info_module.html#ovirt-affinity-label-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ovirt_api_facts` module was renamed to [ovirt_api_info](https://docs.ansible.com/ansible/2.9/modules/ovirt_api_info_module.html#ovirt-api-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ovirt_cluster_facts` module was renamed to [ovirt_cluster_info](https://docs.ansible.com/ansible/2.9/modules/ovirt_cluster_info_module.html#ovirt-cluster-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ovirt_datacenter_facts` module was renamed to [ovirt_datacenter_info](https://docs.ansible.com/ansible/2.9/modules/ovirt_datacenter_info_module.html#ovirt-datacenter-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ovirt_disk_facts` module was renamed to [ovirt_disk_info](https://docs.ansible.com/ansible/2.9/modules/ovirt_disk_info_module.html#ovirt-disk-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ovirt_event_facts` module was renamed to [ovirt_event_info](https://docs.ansible.com/ansible/2.9/modules/ovirt_event_info_module.html#ovirt-event-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ovirt_external_provider_facts` module was renamed to [ovirt_external_provider_info](https://docs.ansible.com/ansible/2.9/modules/ovirt_external_provider_info_module.html#ovirt-external-provider-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ovirt_group_facts` module was renamed to [ovirt_group_info](https://docs.ansible.com/ansible/2.9/modules/ovirt_group_info_module.html#ovirt-group-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ovirt_host_facts` module was renamed to [ovirt_host_info](https://docs.ansible.com/ansible/2.9/modules/ovirt_host_info_module.html#ovirt-host-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ovirt_host_storage_facts` module was renamed to [ovirt_host_storage_info](https://docs.ansible.com/ansible/2.9/modules/ovirt_host_storage_info_module.html#ovirt-host-storage-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ovirt_network_facts` module was renamed to [ovirt_network_info](https://docs.ansible.com/ansible/2.9/modules/ovirt_network_info_module.html#ovirt-network-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ovirt_nic_facts` module was renamed to [ovirt_nic_info](https://docs.ansible.com/ansible/2.9/modules/ovirt_nic_info_module.html#ovirt-nic-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ovirt_permission_facts` module was renamed to [ovirt_permission_info](https://docs.ansible.com/ansible/2.9/modules/ovirt_permission_info_module.html#ovirt-permission-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ovirt_quota_facts` module was renamed to [ovirt_quota_info](https://docs.ansible.com/ansible/2.9/modules/ovirt_quota_info_module.html#ovirt-quota-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ovirt_scheduling_policy_facts` module was renamed to [ovirt_scheduling_policy_info](https://docs.ansible.com/ansible/2.9/modules/ovirt_scheduling_policy_info_module.html#ovirt-scheduling-policy-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ovirt_snapshot_facts` module was renamed to [ovirt_snapshot_info](https://docs.ansible.com/ansible/2.9/modules/ovirt_snapshot_info_module.html#ovirt-snapshot-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ovirt_storage_domain_facts` module was renamed to [ovirt_storage_domain_info](https://docs.ansible.com/ansible/2.9/modules/ovirt_storage_domain_info_module.html#ovirt-storage-domain-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ovirt_storage_template_facts` module was renamed to [ovirt_storage_template_info](https://docs.ansible.com/ansible/2.9/modules/ovirt_storage_template_info_module.html#ovirt-storage-template-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ovirt_storage_vm_facts` module was renamed to [ovirt_storage_vm_info](https://docs.ansible.com/ansible/2.9/modules/ovirt_storage_vm_info_module.html#ovirt-storage-vm-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ovirt_tag_facts` module was renamed to [ovirt_tag_info](https://docs.ansible.com/ansible/2.9/modules/ovirt_tag_info_module.html#ovirt-tag-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ovirt_template_facts` module was renamed to [ovirt_template_info](https://docs.ansible.com/ansible/2.9/modules/ovirt_template_info_module.html#ovirt-template-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ovirt_user_facts` module was renamed to [ovirt_user_info](https://docs.ansible.com/ansible/2.9/modules/ovirt_user_info_module.html#ovirt-user-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ovirt_vm_facts` module was renamed to [ovirt_vm_info](https://docs.ansible.com/ansible/2.9/modules/ovirt_vm_info_module.html#ovirt-vm-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `ovirt_vmpool_facts` module was renamed to [ovirt_vmpool_info](https://docs.ansible.com/ansible/2.9/modules/ovirt_vmpool_info_module.html#ovirt-vmpool-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `python_requirements_facts` module was renamed to [python_requirements_info](https://docs.ansible.com/ansible/2.9/modules/python_requirements_info_module.html#python-requirements-info-module "(in Ansible v2.9)").
- The `rds_instance_facts` module was renamed to [rds_instance_info](https://docs.ansible.com/ansible/2.9/modules/rds_instance_info_module.html#rds-instance-info-module "(in Ansible v2.9)").
- The `rds_snapshot_facts` module was renamed to [rds_snapshot_info](https://docs.ansible.com/ansible/2.9/modules/rds_snapshot_info_module.html#rds-snapshot-info-module "(in Ansible v2.9)").
- The `redfish_facts` module was renamed to [redfish_info](https://docs.ansible.com/ansible/2.9/modules/redfish_info_module.html#redfish-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `redshift_facts` module was renamed to [redshift_info](https://docs.ansible.com/ansible/2.9/modules/redshift_info_module.html#redshift-info-module "(in Ansible v2.9)").
- The `route53_facts` module was renamed to [route53_info](https://docs.ansible.com/ansible/2.9/modules/route53_info_module.html#route53-info-module "(in Ansible v2.9)").
- The `smartos_image_facts` module was renamed to [smartos_image_info](https://docs.ansible.com/ansible/2.9/modules/ali_instance_info_module.html#ali-instance-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `vertica_facts` module was renamed to [vertica_info](https://docs.ansible.com/ansible/2.9/modules/vertica_info_module.html#vertica-info-module "(in Ansible v2.9)").
  When called with the new name, the module no longer returns `ansible_facts`.
  To access return values, [register a variable](../user_guide/playbooks_variables.md#registered-variables).
- The `vmware_cluster_facts` module was renamed to [vmware_cluster_info](https://docs.ansible.com/ansible/2.9/modules/vmware_cluster_info_module.html#vmware-cluster-info-module "(in Ansible v2.9)").
- The `vmware_datastore_facts` module was renamed to [vmware_datastore_info](https://docs.ansible.com/ansible/2.9/modules/vmware_datastore_info_module.html#vmware-datastore-info-module "(in Ansible v2.9)").
- The `vmware_guest_facts` module was renamed to [vmware_guest_info](https://docs.ansible.com/ansible/2.9/modules/vmware_guest_info_module.html#vmware-guest-info-module "(in Ansible v2.9)").
- The `vmware_guest_snapshot_facts` module was renamed to [vmware_guest_snapshot_info](https://docs.ansible.com/ansible/2.9/modules/vmware_guest_snapshot_info_module.html#vmware-guest-snapshot-info-module "(in Ansible v2.9)").
- The `vmware_tag_facts` module was renamed to [vmware_tag_info](https://docs.ansible.com/ansible/2.9/modules/vmware_tag_info_module.html#vmware-tag-info-module "(in Ansible v2.9)").
- The `vmware_vm_facts` module was renamed to [vmware_vm_info](https://docs.ansible.com/ansible/2.9/modules/vmware_vm_info_module.html#vmware-vm-info-module "(in Ansible v2.9)").
- The `xenserver_guest_facts` module was renamed to [xenserver_guest_info](https://docs.ansible.com/ansible/2.9/modules/xenserver_guest_info_module.html#xenserver-guest-info-module "(in Ansible v2.9)").
- The `zabbix_group_facts` module was renamed to [zabbix_group_info](https://docs.ansible.com/ansible/2.9/modules/zabbix_group_info_module.html#zabbix-group-info-module "(in Ansible v2.9)").
- The `zabbix_host_facts` module was renamed to [zabbix_host_info](https://docs.ansible.com/ansible/2.9/modules/zabbix_host_info_module.html#zabbix-host-info-module "(in Ansible v2.9)").

### [Noteworthy module changes](porting_guide_2.9.md#id14)

- [vmware_cluster](https://docs.ansible.com/ansible/2.9/modules/vmware_cluster_module.html#vmware-cluster-module "(in Ansible v2.9)") was refactored for easier maintenance/bugfixes. Use the three new, specialized modules to configure clusters. Configure DRS with [vmware_cluster_drs](https://docs.ansible.com/ansible/2.9/modules/vmware_cluster_drs_module.html#vmware-cluster-drs-module "(in Ansible v2.9)"), HA with [vmware_cluster_ha](https://docs.ansible.com/ansible/2.9/modules/vmware_cluster_ha_module.html#vmware-cluster-ha-module "(in Ansible v2.9)") and vSAN with [vmware_cluster_vsan](https://docs.ansible.com/ansible/2.9/modules/vmware_cluster_vsan_module.html#vmware-cluster-vsan-module "(in Ansible v2.9)").
- [vmware_dvswitch](https://docs.ansible.com/ansible/2.9/modules/vmware_dvswitch_module.html#vmware-dvswitch-module "(in Ansible v2.9)") accepts `folder` parameter to place dvswitch in user defined folder. This option makes `datacenter` as an optional parameter.
- [vmware_datastore_cluster](https://docs.ansible.com/ansible/2.9/modules/vmware_datastore_cluster_module.html#vmware-datastore-cluster-module "(in Ansible v2.9)") accepts `folder` parameter to place datastore cluster in user defined folder. This option makes `datacenter` as an optional parameter.
- [mysql_db](https://docs.ansible.com/ansible/2.9/modules/mysql_db_module.html#mysql-db-module "(in Ansible v2.9)") returns new `db_list` parameter in addition to `db` parameter. This `db_list` parameter refers to list of database names. `db` parameter will be deprecated in version 2.13.
- [snow_record](https://docs.ansible.com/ansible/2.9/modules/snow_record_module.html#snow-record-module "(in Ansible v2.9)") and [snow_record_find](https://docs.ansible.com/ansible/2.9/modules/snow_record_find_module.html#snow-record-find-module "(in Ansible v2.9)") now takes environment variables for `instance`, `username` and `password` parameters. This change marks these parameters as optional.
- The deprecated `force` option in `win_firewall_rule` has been removed.
- [openssl_certificate](https://docs.ansible.com/ansible/2.9/modules/openssl_certificate_module.html#openssl-certificate-module "(in Ansible v2.9)")’s `ownca` provider creates authority key identifiers if not explicitly disabled with `ownca_create_authority_key_identifier: no`. This is only the case for the `cryptography` backend, which is selected by default if the `cryptography` library is available.
- [openssl_certificate](https://docs.ansible.com/ansible/2.9/modules/openssl_certificate_module.html#openssl-certificate-module "(in Ansible v2.9)")’s `ownca` and `selfsigned` providers create subject key identifiers if not explicitly disabled with `ownca_create_subject_key_identifier: never_create` resp. `selfsigned_create_subject_key_identifier: never_create`. If a subject key identifier is provided by the CSR, it is taken; if not, it is created from the public key. This is only the case for the `cryptography` backend, which is selected by default if the `cryptography` library is available.
- [openssh_keypair](https://docs.ansible.com/ansible/2.9/modules/openssh_keypair_module.html#openssh-keypair-module "(in Ansible v2.9)") now applies the same file permissions and ownership to both public and private keys (both get the same `mode`, `owner`, `group`, and so on). If you need to change permissions / ownership on one key, use the [file](../collections/ansible/builtin/file_module.md#file-module) to modify it after it is created.

## [Plugins](porting_guide_2.9.md#id15)

### [Removed Lookup Plugins](porting_guide_2.9.md#id16)

- `redis_kv` use [redis](https://docs.ansible.com/ansible/2.9/plugins/lookup/redis.html#redis-lookup "(in Ansible v2.9)") instead.

## [Porting custom scripts](porting_guide_2.9.md#id17)

No notable changes

## [Networking](porting_guide_2.9.md#id18)

### [Network resource modules](porting_guide_2.9.md#id19)

Ansible 2.9 introduced the first batch of network resource modules. Sections of a network device’s configuration can be thought of as a resource provided by that device. Network resource modules are intentionally scoped to configure a single resource and you can combine them as building blocks to configure complex network services. The older modules are deprecated in Ansible 2.9 and will be removed in Ansible 2.13. You should scan the list of deprecated modules above and replace them with the new network resource modules in your playbooks. See [Ansible Network Features in 2.9](https://www.ansible.com/blog/network-features-coming-soon-in-ansible-engine-2.9) for details.

### [Improved `gather_facts` support for network devices](porting_guide_2.9.md#id20)

In Ansible 2.9, the `gather_facts` keyword now supports gathering network device facts in standardized key/value pairs. You can feed these network facts into further tasks to manage the network device. You can also use the new `gather_network_resources` parameter with the network `*_facts` modules (such as [eos_facts](https://docs.ansible.com/ansible/2.9/modules/eos_facts_module.html#eos-facts-module "(in Ansible v2.9)")) to return just a subset of the device configuration. See [Gathering facts from network devices](../network/getting_started/first_playbook.md#network-gather-facts) for an example.

### [Top-level connection arguments removed in 2.9](porting_guide_2.9.md#id21)

Top-level connection arguments like `username`, `host`, and `password` are removed in version 2.9.

**OLD** In Ansible < 2.4

```yaml
- name: example of using top-level options for connection properties
  ios_command:
    commands: show version
    host: "{{ inventory_hostname }}"
    username: cisco
    password: cisco
    authorize: yes
    auth_pass: cisco
```

Change your playbooks to the connection types `network_cli` and `netconf` using standard Ansible connection properties, and setting those properties in inventory by group. As you update your playbooks and inventory files, you can easily make the change to `become` for privilege escalation (on platforms that support it). For more information, see the [using become with network modules](../user_guide/become.md#become-network) guide and the [platform documentation](../network/user_guide/platform_index.md#platform-options).
