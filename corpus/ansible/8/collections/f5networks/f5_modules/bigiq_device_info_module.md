---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigiq_device_info module – Collect information from F5 BIG-IQ devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigiq_device_info_module.html
fetched_at: 2026-07-28T02:07:41+00:00
---
# f5networks.f5_modules.bigiq_device_info module – Collect information from F5 BIG-IQ devices

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/ui/repo/published/f5networks/f5_modules/) (version 1.27.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigiq_device_info`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigiq_device_info_module.md#synopsis)
- [Parameters](bigiq_device_info_module.md#parameters)
- [Notes](bigiq_device_info_module.md#notes)
- [Examples](bigiq_device_info_module.md#examples)
- [Return Values](bigiq_device_info_module.md#return-values)

## [Synopsis](bigiq_device_info_module.md#id1)

- Collect information from F5 BIG-IQ devices.
- This module was called `bigiq_device_facts` before Ansible 2.9. The usage did not change.

Aliases: bigia_device_facts

## [Parameters](bigiq_device_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **gather_subset**  list / elements=string / required | When supplied, this argument restricts the information returned to a given subset.  You can specify a list of values to include a larger subset.  Values can also be used with an initial `!` to specify a specific subset should not be collected.  **Choices:**   - `"all"` - `"applications"` - `"managed-devices"` - `"purchased-pool-licenses"` - `"regkey-pools"` - `"system-info"` - `"vlans"` - `"!all"` - `"!applications"` - `"!managed-devices"` - `"!purchased-pool-licenses"` - `"!regkey-pools"` - `"!system-info"` - `"!vlans"` |
| **provider**  dictionary  *added in f5networks.f5_modules 1.0.0* | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  **Choices:**   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP or the BIG-IQ.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host or the BIG-IQ host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  **Default:** `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  **Choices:**   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP or the BIG-IQ. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](bigiq_device_info_module.md#id3)

> **Note:**
>
> - This module is supported with all BIG-IQ versions
> - With BIGIQ 7.0 and later, a few metadata fields not included/supported (for example, uptime, product_changelist, product_jobid)
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigiq_device_info_module.md#id4)

```yaml+jinja
- name: Collect BIG-IQ information
  bigiq_device_info:
    gather_subset:
      - system-info
      - vlans
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Collect all BIG-IQ information
  bigiq_device_info:
    gather_subset:
      - all
    provider:
      server: cm.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Collect all BIG-IP information except trunks
  bigiq_device_info:
    gather_subset:
      - all
      - "!trunks"
    provider:
      server: cm.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
```

## [Return Values](bigiq_device_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **applications**  complex | Application related information  **Returned:** When `managed-devices` is specified in `gather_subset`.  **Sample:** `"hash/dictionary of values"` |
| **active_alerts**  integer | Number of alerts active on the application.  **Returned:** changed  **Sample:** `0` |
| **bad_traffic**  float | Percent of traffic to application that is determined to be ‘bad’.  This value is dependent on `protection_mode` being enabled.  **Returned:** changed  **Sample:** `1.7498` |
| **bad_traffic_growth**  boolean | Whether or not Bad Traffic Growth alerts are configured to be triggered or not.  **Returned:** changed  **Sample:** `false` |
| **connections**  float | Current number of connections established to the application.  **Returned:** changed  **Sample:** `3.06` |
| **enhanced_analytics**  boolean | Whether enhanced analytics is enabled for the application or not.  **Returned:** changed  **Sample:** `true` |
| **health**  string | Health of the application.  **Returned:** changed  **Sample:** `"Good"` |
| **id**  string | ID of the application as known to the BIG-IQ.  **Returned:** changed  **Sample:** `"996baae8-5d1d-3662-8a2d-3612fa2aceae"` |
| **name**  string | Name of the application.  **Returned:** changed  **Sample:** `"site12http.example.com"` |
| **new_connections**  float | Number of new connections being established per second.  **Returned:** changed  **Sample:** `0.35` |
| **protection_mode**  string | The type of F5 Web Application Security Service protection on the application.  **Returned:** changed  **Sample:** `"Not Protected"` |
| **response_time**  float | Measured response time of the application in milliseconds.  **Returned:** changed  **Sample:** `0.02` |
| **status**  string | Current state of the application.  **Returned:** changed  **Sample:** `"DEPLOYED"` |
| **transactions_per_second**  float | Current measurement of Transactions Per second being handled by the application.  **Returned:** changed  **Sample:** `0.87` |
| **managed_devices**  complex | Managed device related information.  **Returned:** When `managed-devices` is specified in `gather_subset`.  **Sample:** `"hash/dictionary of values"` |
| **address**  string | Address where the device was discovered.  **Returned:** changed  **Sample:** `"10.10.10.10"` |
| **build**  string | Build of the version.  **Returned:** changed  **Sample:** `"0.0.4"` |
| **device_uri**  string | URI to reach the management interface of the device.  **Returned:** changed  **Sample:** `"https://10.10.10.10:443"` |
| **edition**  string | Edition string of the product version.  **Returned:** changed  **Sample:** `"Final"` |
| **group_name**  string | BIG-IQ group that the device is a member of.  **Returned:** changed  **Sample:** `"cm-bigip-allBigIpDevices"` |
| **hostname**  string | Discovered hostname of the device.  **Returned:** changed  **Sample:** `"tier2labB1.lab.fp.foo.com"` |
| **https_port**  integer | HTTPS port available on the management interface of the device.  **Returned:** changed  **Sample:** `443` |
| **is_clustered**  boolean | Whether the device is clustered or not.  **Returned:** changed  **Sample:** `false` |
| **is_license_expired**  boolean | Whether the license on the device is expired or not.  **Returned:** changed  **Sample:** `true` |
| **is_virtual**  boolean | Whether the device is a virtual edition or not.  **Returned:** changed  **Sample:** `true` |
| **machine_id**  string | Machine specific ID assigned to this device by BIG-IQ.  **Returned:** changed  **Sample:** `"c141bc88-f734-4434-be64-a3e9ea98356e"` |
| **management_address**  string | IP address of the management interface on the device.  **Returned:** changed  **Sample:** `"10.10.10.10"` |
| **mcp_device_name**  string | Device name as known by MCPD on the BIG-IP.  **Returned:** changed  **Sample:** `"/Common/tier2labB1.lab.fp.foo.com"` |
| **product**  string | Product that the managed device is identified as.  **Returned:** changed  **Sample:** `"BIG-IP"` |
| **rest_framework_version**  string | REST framework version running on the device  **Returned:** changed  **Sample:** `"13.1.1-0.0.4"` |
| **self_link**  string | Internal reference to the managed device in BIG-IQ.  **Returned:** changed  **Sample:** `"https://localhost/mgmt/shared/resolver/device-groups/cm-bigip-allBigIpDevices/devices/c141bc88-f734-4434-be64-a3e9ea98356e"` |
| **slots**  dictionary | Volumes on the device and versions of software installed in those volumes.  **Returned:** changed  **Sample:** `{"build": "0.0.4", "isActive": "yes", "product": "BIG-IP", "version": "13.1.1", "volume": "HD1.1"}` |
| **state**  string | State of the device.  **Returned:** changed  **Sample:** `"ACTIVE"` |
| **tags**  dictionary | Misc tags that are assigned to the device.  **Returned:** changed  **Sample:** `{"BIGIQ_SSG_name": "tim-ssg", "BIGIQ_tier_2_device": "2018-08-22T13:30:47.693-07:00"}` |
| **trust_domain_guid**  string | GUID of the trust domain the device is part of.  **Returned:** changed  **Sample:** `"40ddf541-e604-4905-bde3005056813e36"` |
| **uuid**  string | UUID of the device in BIG-IQ.  **Returned:** changed  **Sample:** `"c141bc88-f734-4434-be64-a3e9ea98356e"` |
| **version**  string | Version of TMOS installed on the device.  **Returned:** changed  **Sample:** `"13.1.1"` |
| **purchased_pool_licenses**  complex | Purchased Pool License related information.  **Returned:** When `purchased-pool-licenses` is specified in `gather_subset`.  **Sample:** `"hash/dictionary of values"` |
| **base_reg_key**  string | Base registration key of the purchased pool  **Returned:** changed  **Sample:** `"XXXXX-XXXXX-XXXXX-XXXXX-XXXXXXX"` |
| **dossier**  string | Dossier of the purchased pool license  **Returned:** changed  **Sample:** `"d6bd4b8ba5...e9a1a1199b73af9932948a"` |
| **evaluation_end_date_time**  string | Date that evaluation license ends.  **Returned:** changed  **Sample:** `"2018-10-11T00:00:00-07:00"` |
| **evaluation_start_date_time**  string | Date that evaluation license starts.  **Returned:** changed  **Sample:** `"2018-09-09T00:00:00-07:00"` |
| **free_device_licenses**  integer | Number of free licenses remaining.  **Returned:** changed  **Sample:** `34` |
| **license_end_date_time**  string | Date that the license expires.  **Returned:** changed  **Sample:** `"2018-10-11T00:00:00-07:00"` |
| **license_start_date_time**  string | Date that the license starts.  **Returned:** changed  **Sample:** `"2018-09-09T00:00:00-07:00"` |
| **licensed_date_time**  string | Timestamp that the pool was licensed.  **Returned:** changed  **Sample:** `"2018-09-10T00:00:00-07:00"` |
| **licensed_version**  string | Version of BIG-IQ that is licensed.  **Returned:** changed  **Sample:** `"6.0.1"` |
| **name**  string | Name of the purchased pool  **Returned:** changed  **Sample:** `"my-pool1"` |
| **registration_key**  string | Purchased pool license key.  **Returned:** changed  **Sample:** `"XXXXX-XXXXX-XXXXX-XXXXX-XXXXXXX"` |
| **state**  string | State of the purchased pool license  **Returned:** changed  **Sample:** `"LICENSED"` |
| **total_device_licenses**  integer | Total number of licenses in the pool.  **Returned:** changed  **Sample:** `40` |
| **uuid**  string | UUID of the purchased pool license  **Returned:** changed  **Sample:** `"b2112329-cba7-4f1f-9a26-fab9be416d60"` |
| **vendor**  string | Vendor who provided the license  **Returned:** changed  **Sample:** `"F5 Networks, Inc"` |
| **regkey_pools**  complex | Regkey Pool related information.  **Returned:** When `regkey-pools` is specified in `gather_subset`.  **Sample:** `"hash/dictionary of values"` |
| **id**  string | ID of the regkey pool.  **Returned:** changed  **Sample:** `"4f9b565c-0831-4657-b6c2-6dde6182a502"` |
| **name**  string | Name of the regkey pool.  **Returned:** changed  **Sample:** `"pool1"` |
| **offerings**  complex | List of the offerings in the pool.  **Returned:** success  **Sample:** `"hash/dictionary of values"` |
| **dossier**  string | Dossier of the license.  **Returned:** changed  **Sample:** `"d6bd4b8ba5...e9a1a1199b73af9932948a"` |
| **evaluation_end_date_time**  string | Date that evaluation license ends.  **Returned:** changed  **Sample:** `"2018-10-11T00:00:00-07:00"` |
| **evaluation_start_date_time**  string | Date that evaluation license starts.  **Returned:** changed  **Sample:** `"2018-09-09T00:00:00-07:00"` |
| **license_end_date_time**  string | Date that the license expires.  **Returned:** changed  **Sample:** `"2018-10-11T00:00:00-07:00"` |
| **license_start_date_time**  string | Date that the license starts.  **Returned:** changed  **Sample:** `"2018-09-09T00:00:00-07:00"` |
| **licensed_date_time**  string | Timestamp that the regkey was licensed.  **Returned:** changed  **Sample:** `"2018-09-10T00:00:00-07:00"` |
| **licensed_version**  string | Version of BIG-IQ that is licensed.  **Returned:** changed  **Sample:** `"6.0.1"` |
| **name**  string | Name of the regkey.  **Returned:** changed  **Sample:** `"regkey1"` |
| **registration_key**  string | Registration license key.  **Returned:** changed  **Sample:** `"XXXXX-XXXXX-XXXXX-XXXXX-XXXXXXX"` |
| **state**  string | State of the regkey license  **Returned:** changed  **Sample:** `"LICENSED"` |
| **total_offerings**  integer | Total number of offerings in the pool  **Returned:** changed  **Sample:** `10` |
| **system_info**  complex | System info related information.  **Returned:** When `system-info` is specified in `gather_subset`.  **Sample:** `"hash/dictionary of values"` |
| **base_mac_address**  string | Media Access Control address (MAC address) of the device.  **Returned:** changed  **Sample:** `"fa:16:3e:c3:42:6f"` |
| **chassis_serial**  string | Serial of the chassis  **Returned:** success  **Sample:** `"11111111-2222-3333-444444444444"` |
| **hardware_information**  complex | Information related to the hardware (drives and CPUs) of the system.  **Returned:** changed |
| **model**  string | The model of the hardware.  **Returned:** success  **Sample:** `"Virtual Disk"` |
| **name**  string | The name of the hardware.  **Returned:** success  **Sample:** `"HD1"` |
| **type**  string | The type of hardware.  **Returned:** success  **Sample:** `"physical-disk"` |
| **versions**  complex | Hardware specific properties  **Returned:** success |
| **name**  string | Name of the property  **Returned:** success  **Sample:** `"Size"` |
| **version**  string | Value of the property  **Returned:** success  **Sample:** `"154.00G"` |
| **host_board_part_revision**  string | Revision of the host board.  **Returned:** success |
| **host_board_serial**  string | Serial of the host board.  **Returned:** success |
| **is_admin_password_changed**  boolean | Whether the admin password was changed from its default or not.  **Returned:** changed  **Sample:** `true` |
| **is_root_password_changed**  boolean | Whether the root password was changed from its default or not.  **Returned:** changed  **Sample:** `false` |
| **is_system_setup**  boolean | Whether the system has been setup or not.  **Returned:** changed  **Sample:** `true` |
| **marketing_name**  string | Marketing name of the device platform.  **Returned:** changed  **Sample:** `"BIG-IQ Virtual Edition"` |
| **package_edition**  string | Displays the software edition.  **Returned:** changed  **Sample:** `"Point Release 7"` |
| **package_version**  string | A string combining the `product_build` and `product_build_date`.  **Returned:** success  **Sample:** `"Build 0.0.1 - Tue May 15 15:26:30 PDT 2018"` |
| **platform**  string | Platform identifier.  **Returned:** success  **Sample:** `"Z100"` |
| **product_build**  string | Build version of the release version.  **Returned:** success  **Sample:** `"0.0.1"` |
| **product_build_date**  string | Human readable build date.  **Returned:** success  **Sample:** `"Tue May 15 15:26:30 PDT 2018"` |
| **product_built**  integer | Unix timestamp of when the product was built.  **Returned:** success  **Sample:** `180515152630` |
| **product_changelist**  integer | Changelist that product branches from.  Not supported with BIGIQ 7.0 and later versions  **Returned:** success  **Sample:** `2557198` |
| **product_code**  string | Code identifying the product.  **Returned:** success  **Sample:** `"BIG-IQ"` |
| **product_jobid**  integer | ID of the job that built the product version.  Not supported with BIGIQ 7.0 and later versions  **Returned:** success  **Sample:** `1012030` |
| **product_version**  string | Major product version of the running software.  **Returned:** success  **Sample:** `"6.0.0"` |
| **switch_board_part_revision**  string | Switch board revision.  **Returned:** success |
| **switch_board_serial**  string | Serial of the switch board.  **Returned:** success |
| **time**  complex | Mapping of the current time information to specific time-named keys.  **Returned:** changed |
| **day**  integer | The current day of the month, in numeric form.  **Returned:** changed  **Sample:** `7` |
| **hour**  integer | The current hour of the day in 24-hour form.  **Returned:** changed  **Sample:** `18` |
| **minute**  integer | The current minute of the hour.  **Returned:** changed  **Sample:** `16` |
| **month**  integer | The current month, in numeric form.  **Returned:** changed  **Sample:** `6` |
| **second**  integer | The current second of the minute.  **Returned:** changed  **Sample:** `51` |
| **year**  integer | The current year in 4-digit form.  **Returned:** changed  **Sample:** `2018` |
| **uptime**  integer | Time, in seconds, since the system booted.  Not supported with BIGIQ 7.0 and later versions  **Returned:** success  **Sample:** `603202` |
| **vlans**  complex | List of VLAN information.  **Returned:** When `vlans` is specified in `gather_subset`.  **Sample:** `"hash/dictionary of values"` |
| **auto_lasthop**  string | Allows the system to send return traffic to the MAC address that transmitted the request, even if the routing table points to a different network or interface.  **Returned:** changed  **Sample:** `"enabled"` |
| **cmp_hash_algorithm**  string | Specifies how the traffic on the VLAN will be disaggregated.  **Returned:** changed  **Sample:** `"default"` |
| **description**  string | Description of the VLAN.  **Returned:** changed  **Sample:** `"My vlan"` |
| **failsafe_action**  string | Action for the system to take when the fail-safe mechanism is triggered.  **Returned:** changed  **Sample:** `"reboot"` |
| **failsafe_enabled**  boolean | Whether failsafe is enabled or not.  **Returned:** changed  **Sample:** `true` |
| **failsafe_timeout**  integer | Number of seconds that an active unit can run without detecting network traffic on this VLAN before it starts a failover.  **Returned:** changed  **Sample:** `90` |
| **if_index**  integer | Index assigned to this VLAN. It is a unique identifier assigned for all objects displayed in the SNMP IF-MIB.  **Returned:** changed  **Sample:** `176` |
| **interfaces**  complex | List of tagged or untagged interfaces and trunks that you want to configure for the VLAN.  **Returned:** changed |
| **full_path**  string | Full name of the resource as known to BIG-IP.  **Returned:** changed  **Sample:** `"1.3"` |
| **name**  string | Relative name of the resource in BIG-IP.  **Returned:** changed  **Sample:** `"1.3"` |
| **tagged**  boolean | Whether the interface is tagged or not.  **Returned:** changed  **Sample:** `false` |
| **learning_mode**  string | Whether switch ports placed in the VLAN are configured for switch learning, forwarding only, or dropped.  **Returned:** changed  **Sample:** `"enable-forward"` |
| **mtu**  integer | Specific maximum transition unit (MTU) for the VLAN.  **Returned:** changed  **Sample:** `1500` |
| **sflow_poll_interval**  integer | Maximum interval in seconds between two pollings.  **Returned:** changed  **Sample:** `0` |
| **sflow_poll_interval_global**  boolean | Whether the global VLAN poll-interval setting, overrides the object-level poll-interval setting.  **Returned:** changed  **Sample:** `false` |
| **sflow_sampling_rate**  integer | Ratio of packets observed to the samples generated.  **Returned:** changed  **Sample:** `0` |
| **sflow_sampling_rate_global**  boolean | Whether the global VLAN sampling-rate setting, overrides the object-level sampling-rate setting.  **Returned:** changed  **Sample:** `true` |
| **source_check_enabled**  boolean | Specifies that only connections that have a return route in the routing table are accepted.  **Returned:** changed  **Sample:** `true` |
| **tag**  integer | Tag number for the VLAN.  **Returned:** changed  **Sample:** `30` |
| **true_mac_address**  string | Media access control (MAC) address for the lowest-numbered interface assigned to this VLAN.  **Returned:** changed  **Sample:** `"fa:16:3e:10:da:ff"` |

### Authors

- Tim Rupp (@caphrim007)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
