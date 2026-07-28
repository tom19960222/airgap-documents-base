---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_system_global module – Configure global attributes in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_system_global_module.html
fetched_at: 2026-07-28T02:28:28+00:00
---
# fortinet.fortios.fortios_system_global module – Configure global attributes in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortios/) (version 2.3.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_system_global_module.md#ansible-collections-fortinet-fortios-fortios-system-global-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_global`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_global_module.md#synopsis)
- [Requirements](fortios_system_global_module.md#requirements)
- [Parameters](fortios_system_global_module.md#parameters)
- [Notes](fortios_system_global_module.md#notes)
- [Examples](fortios_system_global_module.md#examples)
- [Return Values](fortios_system_global_module.md#return-values)

## [Synopsis](fortios_system_global_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and global category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_global_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_system_global_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **system_global**  dictionary | Configure global attributes. |
| **admin_concurrent**  string | Enable/disable concurrent administrator logins. Use policy-auth-concurrent for firewall authenticated users.  **Choices:**   - `"enable"` - `"disable"` |
| **admin_console_timeout**  integer | Console login timeout that overrides the admin timeout value (15 - 300 seconds). |
| **admin_forticloud_sso_default_profile**  string | Override access profile. Source system.accprofile.name. |
| **admin_forticloud_sso_login**  string | Enable/disable FortiCloud admin login via SSO.  **Choices:**   - `"enable"` - `"disable"` |
| **admin_host**  string | Administrative host for HTTP and HTTPS. When set, will be used in lieu of the client”s Host header for any redirection. |
| **admin_hsts_max_age**  integer | HTTPS Strict-Transport-Security header max-age in seconds. A value of 0 will reset any HSTS records in the browser.When admin-https-redirect is disabled the header max-age will be 0. |
| **admin_https_pki_required**  string | Enable/disable admin login method. Enable to force administrators to provide a valid certificate to log in if PKI is enabled. Disable to allow administrators to log in with a certificate or password.  **Choices:**   - `"enable"` - `"disable"` |
| **admin_https_redirect**  string | Enable/disable redirection of HTTP administration access to HTTPS.  **Choices:**   - `"enable"` - `"disable"` |
| **admin_https_ssl_banned_ciphers**  list / elements=string | Select one or more cipher technologies that cannot be used in GUI HTTPS negotiations. Only applies to TLS 1.2 and below.  **Choices:**   - `"RSA"` - `"DHE"` - `"ECDHE"` - `"DSS"` - `"ECDSA"` - `"AES"` - `"AESGCM"` - `"CAMELLIA"` - `"3DES"` - `"SHA1"` - `"SHA256"` - `"SHA384"` - `"STATIC"` - `"CHACHA20"` - `"ARIA"` - `"AESCCM"` |
| **admin_https_ssl_ciphersuites**  list / elements=string | Select one or more TLS 1.3 ciphersuites to enable. Does not affect ciphers in TLS 1.2 and below. At least one must be enabled. To disable all, remove TLS1.3 from admin-https-ssl-versions.  **Choices:**   - `"TLS-AES-128-GCM-SHA256"` - `"TLS-AES-256-GCM-SHA384"` - `"TLS-CHACHA20-POLY1305-SHA256"` - `"TLS-AES-128-CCM-SHA256"` - `"TLS-AES-128-CCM-8-SHA256"` |
| **admin_https_ssl_versions**  list / elements=string | Allowed TLS versions for web administration.  **Choices:**   - `"tlsv1-1"` - `"tlsv1-2"` - `"tlsv1-3"` - `"tlsv1-0"` |
| **admin_lockout_duration**  integer | Amount of time in seconds that an administrator account is locked out after reaching the admin-lockout-threshold for repeated failed login attempts. |
| **admin_lockout_threshold**  integer | Number of failed login attempts before an administrator account is locked out for the admin-lockout-duration. |
| **admin_login_max**  integer | Maximum number of administrators who can be logged in at the same time (1 - 100). |
| **admin_maintainer**  string | Enable/disable maintainer administrator login. When enabled, the maintainer account can be used to log in from the console after a hard reboot. The password is “bcpb” followed by the FortiGate unit serial number. You have limited time to complete this login.  **Choices:**   - `"enable"` - `"disable"` |
| **admin_port**  integer | Administrative access port for HTTP. (1 - 65535). |
| **admin_restrict_local**  string | Enable/disable local admin authentication restriction when remote authenticator is up and running .  **Choices:**   - `"enable"` - `"disable"` |
| **admin_scp**  string | Enable/disable using SCP to download the system configuration. You can use SCP as an alternative method for backing up the configuration.  **Choices:**   - `"enable"` - `"disable"` |
| **admin_server_cert**  string | Server certificate that the FortiGate uses for HTTPS administrative connections. Source certificate.local.name. |
| **admin_sport**  integer | Administrative access port for HTTPS. (1 - 65535). |
| **admin_ssh_grace_time**  integer | Maximum time in seconds permitted between making an SSH connection to the FortiGate unit and authenticating (10 - 3600 sec (1 hour)). |
| **admin_ssh_password**  string | Enable/disable password authentication for SSH admin access.  **Choices:**   - `"enable"` - `"disable"` |
| **admin_ssh_port**  integer | Administrative access port for SSH. (1 - 65535). |
| **admin_ssh_v1**  string | Enable/disable SSH v1 compatibility.  **Choices:**   - `"enable"` - `"disable"` |
| **admin_telnet**  string | Enable/disable TELNET service.  **Choices:**   - `"enable"` - `"disable"` |
| **admin_telnet_port**  integer | Administrative access port for TELNET. (1 - 65535). |
| **admintimeout**  integer | Number of minutes before an idle administrator session times out (1 - 480 minutes (8 hours)). A shorter idle timeout is more secure. |
| **alias**  string | Alias for your FortiGate unit. |
| **allow_traffic_redirect**  string | Disable to prevent traffic with same local ingress and egress interface from being forwarded without policy check.  **Choices:**   - `"enable"` - `"disable"` |
| **anti_replay**  string | Level of checking for packet replay and TCP sequence checking.  **Choices:**   - `"disable"` - `"loose"` - `"strict"` |
| **arp_max_entry**  integer | Maximum number of dynamically learned MAC addresses that can be added to the ARP table (131072 - 2147483647). |
| **asymroute**  string | Enable/disable asymmetric route.  **Choices:**   - `"enable"` - `"disable"` |
| **auth_cert**  string | Server certificate that the FortiGate uses for HTTPS firewall authentication connections. Source certificate.local.name. |
| **auth_http_port**  integer | User authentication HTTP port. (1 - 65535). |
| **auth_https_port**  integer | User authentication HTTPS port. (1 - 65535). |
| **auth_ike_saml_port**  integer | User IKE SAML authentication port (0 - 65535). |
| **auth_keepalive**  string | Enable to prevent user authentication sessions from timing out when idle.  **Choices:**   - `"enable"` - `"disable"` |
| **auth_session_limit**  string | Action to take when the number of allowed user authenticated sessions is reached.  **Choices:**   - `"block-new"` - `"logout-inactive"` |
| **auto_auth_extension_device**  string | Enable/disable automatic authorization of dedicated Fortinet extension devices.  **Choices:**   - `"enable"` - `"disable"` |
| **autorun_log_fsck**  string | Enable/disable automatic log partition check after ungraceful shutdown.  **Choices:**   - `"enable"` - `"disable"` |
| **av_affinity**  string | Affinity setting for AV scanning (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx). |
| **av_failopen**  string | Set the action to take if the FortiGate is running low on memory or the proxy connection limit has been reached.  **Choices:**   - `"pass"` - `"off"` - `"one-shot"` |
| **av_failopen_session**  string | When enabled and a proxy for a protocol runs out of room in its session table, that protocol goes into failopen mode and enacts the action specified by av-failopen.  **Choices:**   - `"enable"` - `"disable"` |
| **batch_cmdb**  string | Enable/disable batch mode, allowing you to enter a series of CLI commands that will execute as a group once they are loaded.  **Choices:**   - `"enable"` - `"disable"` |
| **block_session_timer**  integer | Duration in seconds for blocked sessions (1 - 300 sec (5 minutes)). |
| **br_fdb_max_entry**  integer | Maximum number of bridge forwarding database (FDB) entries. |
| **cert_chain_max**  integer | Maximum number of certificates that can be traversed in a certificate chain. |
| **cfg_revert_timeout**  integer | Time-out for reverting to the last saved configuration. (10 - 4294967295 seconds). |
| **cfg_save**  string | Configuration file save mode for CLI changes.  **Choices:**   - `"automatic"` - `"manual"` - `"revert"` |
| **check_protocol_header**  string | Level of checking performed on protocol headers. Strict checking is more thorough but may affect performance. Loose checking is OK in most cases.  **Choices:**   - `"loose"` - `"strict"` |
| **check_reset_range**  string | Configure ICMP error message verification. You can either apply strict RST range checking or disable it.  **Choices:**   - `"strict"` - `"disable"` |
| **cli_audit_log**  string | Enable/disable CLI audit log.  **Choices:**   - `"enable"` - `"disable"` |
| **cloud_communication**  string | Enable/disable all cloud communication.  **Choices:**   - `"enable"` - `"disable"` |
| **clt_cert_req**  string | Enable/disable requiring administrators to have a client certificate to log into the GUI using HTTPS.  **Choices:**   - `"enable"` - `"disable"` |
| **cmdbsvr_affinity**  string | Affinity setting for cmdbsvr (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx). |
| **compliance_check**  string | Enable/disable global PCI DSS compliance check.  **Choices:**   - `"enable"` - `"disable"` |
| **compliance_check_time**  string | Time of day to run scheduled PCI DSS compliance checks. |
| **cpu_use_threshold**  integer | Threshold at which CPU usage is reported (% of total CPU). |
| **csr_ca_attribute**  string | Enable/disable the CA attribute in certificates. Some CA servers reject CSRs that have the CA attribute.  **Choices:**   - `"enable"` - `"disable"` |
| **daily_restart**  string | Enable/disable daily restart of FortiGate unit. Use the restart-time option to set the time of day for the restart.  **Choices:**   - `"enable"` - `"disable"` |
| **default_service_source_port**  string | Default service source port range . |
| **device_identification_active_scan_delay**  integer | Number of seconds to passively scan a device before performing an active scan. (20 - 3600 sec, (20 sec to 1 hour)). |
| **device_idle_timeout**  integer | Time in seconds that a device must be idle to automatically log the device user out. (30 - 31536000 sec (30 sec to 1 year)). |
| **dh_params**  string | Number of bits to use in the Diffie-Hellman exchange for HTTPS/SSH protocols.  **Choices:**   - `"1024"` - `"1536"` - `"2048"` - `"3072"` - `"4096"` - `"6144"` - `"8192"` |
| **dnsproxy_worker_count**  integer | DNS proxy worker count. For a FortiGate with multiple logical CPUs, you can set the DNS process number from 1 to the number of logical CPUs. |
| **dst**  string | Enable/disable daylight saving time.  **Choices:**   - `"enable"` - `"disable"` |
| **early_tcp_npu_session**  string | Enable/disable early TCP NPU session.  **Choices:**   - `"enable"` - `"disable"` |
| **edit_vdom_prompt**  string | Enable/disable edit new VDOM prompt.  **Choices:**   - `"enable"` - `"disable"` |
| **endpoint_control_fds_access**  string | Enable/disable access to the FortiGuard network for non-compliant endpoints.  **Choices:**   - `"enable"` - `"disable"` |
| **endpoint_control_portal_port**  integer | Endpoint control portal port (1 - 65535). |
| **extender_controller_reserved_network**  string | Configure reserved network subnet for managed LAN extension FortiExtender units. This is available when the FortiExtender daemon is running. |
| **failtime**  integer | Fail-time for server lost. |
| **faz_disk_buffer_size**  integer | Maximum disk buffer size to temporarily store logs destined for FortiAnalyzer. To be used in the event that FortiAnalyzer is unavailable. |
| **fds_statistics**  string | Enable/disable sending IPS, Application Control, and AntiVirus data to FortiGuard. This data is used to improve FortiGuard services and is not shared with external parties and is protected by Fortinet”s privacy policy.  **Choices:**   - `"enable"` - `"disable"` |
| **fds_statistics_period**  integer | FortiGuard statistics collection period in minutes. (1 - 1440 min (1 min to 24 hours)). |
| **fec_port**  integer | Local UDP port for Forward Error Correction (49152 - 65535). |
| **fgd_alert_subscription**  list / elements=string | Type of alert to retrieve from FortiGuard.  **Choices:**   - `"advisory"` - `"latest-threat"` - `"latest-virus"` - `"latest-attack"` - `"new-antivirus-db"` - `"new-attack-db"` |
| **forticarrier_bypass**  string | Enable/disable forticarrier-bypass.  **Choices:**   - `"enable"` - `"disable"` |
| **forticonverter_config_upload**  string | Enable/disable config upload to FortiConverter.  **Choices:**   - `"once"` - `"disable"` |
| **forticonverter_integration**  string | Enable/disable FortiConverter integration service.  **Choices:**   - `"enable"` - `"disable"` |
| **fortiextender**  string | Enable/disable FortiExtender.  **Choices:**   - `"disable"` - `"enable"` |
| **fortiextender_data_port**  integer | FortiExtender data port (1024 - 49150). |
| **fortiextender_discovery_lockdown**  string | Enable/disable FortiExtender CAPWAP lockdown.  **Choices:**   - `"disable"` - `"enable"` |
| **fortiextender_provision_on_authorization**  string | Enable/disable automatic provisioning of latest FortiExtender firmware on authorization.  **Choices:**   - `"enable"` - `"disable"` |
| **fortiextender_vlan_mode**  string | Enable/disable FortiExtender VLAN mode.  **Choices:**   - `"enable"` - `"disable"` |
| **fortiipam_integration**  string | Enable/disable integration with the FortiIPAM cloud service.  **Choices:**   - `"enable"` - `"disable"` |
| **fortiservice_port**  integer | FortiService port (1 - 65535). Used by FortiClient endpoint compliance. Older versions of FortiClient used a different port. |
| **fortitoken_cloud**  string | Enable/disable FortiToken Cloud service.  **Choices:**   - `"enable"` - `"disable"` |
| **fortitoken_cloud_push_status**  string | Enable/disable FTM push service of FortiToken Cloud.  **Choices:**   - `"enable"` - `"disable"` |
| **fortitoken_cloud_sync_interval**  integer | Interval in which to clean up remote users in FortiToken Cloud (0 - 336 hours (14 days)). |
| **gui_allow_default_hostname**  string | Enable/disable the factory default hostname warning on the GUI setup wizard.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_allow_incompatible_fabric_fgt**  string | Enable/disable Allow FGT with incompatible firmware to be treated as compatible in security fabric on the GUI. May cause unexpected error.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_app_detection_sdwan**  string | Enable/disable Allow app-detection based SD-WAN.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_auto_upgrade_setup_warning**  string | Enable/disable the automatic patch upgrade setup prompt on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_cdn_domain_override**  string | Domain of CDN server. |
| **gui_cdn_usage**  string | Enable/disable Load GUI static files from a CDN.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_certificates**  string | Enable/disable the System > Certificate GUI page, allowing you to add and configure certificates from the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_custom_language**  string | Enable/disable custom languages in GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_date_format**  string | Default date format used throughout GUI.  **Choices:**   - `"yyyy/MM/dd"` - `"dd/MM/yyyy"` - `"MM/dd/yyyy"` - `"yyyy-MM-dd"` - `"dd-MM-yyyy"` - `"MM-dd-yyyy"` |
| **gui_date_time_source**  string | Source from which the FortiGate GUI uses to display date and time entries.  **Choices:**   - `"system"` - `"browser"` |
| **gui_device_latitude**  string | Add the latitude of the location of this FortiGate to position it on the Threat Map. |
| **gui_device_longitude**  string | Add the longitude of the location of this FortiGate to position it on the Threat Map. |
| **gui_display_hostname**  string | Enable/disable displaying the FortiGate”s hostname on the GUI login page.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_firmware_upgrade_warning**  string | Enable/disable the firmware upgrade warning on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_forticare_registration_setup_warning**  string | Enable/disable the FortiCare registration setup warning on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_fortigate_cloud_sandbox**  string | Enable/disable displaying FortiGate Cloud Sandbox on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_fortiguard_resource_fetch**  string | Enable/disable retrieving static GUI resources from FortiGuard. Disabling it will improve GUI load time for air-gapped environments.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_fortisandbox_cloud**  string | Enable/disable displaying FortiSandbox Cloud on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_ipv6**  string | Enable/disable IPv6 settings on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_lines_per_page**  integer | Number of lines to display per page for web administration. |
| **gui_local_out**  string | Enable/disable Local-out traffic on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_replacement_message_groups**  string | Enable/disable replacement message groups on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_rest_api_cache**  string | Enable/disable REST API result caching on FortiGate.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_theme**  string | Color scheme for the administration GUI.  **Choices:**   - `"jade"` - `"neutrino"` - `"mariner"` - `"graphite"` - `"melongene"` - `"jet-stream"` - `"security-fabric"` - `"retro"` - `"dark-matter"` - `"onyx"` - `"eclipse"` - `"green"` - `"blue"` - `"red"` |
| **gui_wireless_opensecurity**  string | Enable/disable wireless open security option on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_workflow_management**  string | Enable/disable Workflow management features on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **ha_affinity**  string | Affinity setting for HA daemons (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx). |
| **honor_df**  string | Enable/disable honoring of Don”t-Fragment (DF) flag.  **Choices:**   - `"enable"` - `"disable"` |
| **hostname**  string | FortiGate unit”s hostname. Most models will truncate names longer than 24 characters. Some models support hostnames up to 35 characters. |
| **igmp_state_limit**  integer | Maximum number of IGMP memberships (96 - 64000). |
| **interface_subnet_usage**  string | Enable/disable allowing use of interface-subnet setting in firewall addresses .  **Choices:**   - `"disable"` - `"enable"` |
| **internet_service_database**  string | Configure which Internet Service database size to download from FortiGuard and use.  **Choices:**   - `"mini"` - `"standard"` - `"full"` - `"on-demand"` |
| **internet_service_download_list**  list / elements=dictionary | Configure which on-demand Internet Service IDs are to be downloaded. |
| **id**  integer / required | Internet Service ID. see <a href=’#notes’>Notes</a>. Source firewall.internet-service.id. |
| **interval**  integer | Dead gateway detection interval. |
| **ip_fragment_mem_thresholds**  integer | Maximum memory (MB) used to reassemble IPv4/IPv6 fragments. |
| **ip_src_port_range**  string | IP source port range used for traffic originating from the FortiGate unit. |
| **ips_affinity**  string | Affinity setting for IPS (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx; allowed CPUs must be less than total number of IPS engine daemons). |
| **ipsec_asic_offload**  string | Enable/disable ASIC offloading (hardware acceleration) for IPsec VPN traffic. Hardware acceleration can offload IPsec VPN sessions and accelerate encryption and decryption.  **Choices:**   - `"enable"` - `"disable"` |
| **ipsec_ha_seqjump_rate**  integer | ESP jump ahead rate (1G - 10G pps equivalent). |
| **ipsec_hmac_offload**  string | Enable/disable offloading (hardware acceleration) of HMAC processing for IPsec VPN.  **Choices:**   - `"enable"` - `"disable"` |
| **ipsec_round_robin**  string | Enable/disable round-robin redistribution to multiple CPUs for IPsec VPN traffic.  **Choices:**   - `"enable"` - `"disable"` |
| **ipsec_soft_dec_async**  string | Enable/disable software decryption asynchronization (using multiple CPUs to do decryption) for IPsec VPN traffic.  **Choices:**   - `"enable"` - `"disable"` |
| **ipv6_accept_dad**  integer | Enable/disable acceptance of IPv6 Duplicate Address Detection (DAD). |
| **ipv6_allow_anycast_probe**  string | Enable/disable IPv6 address probe through Anycast.  **Choices:**   - `"enable"` - `"disable"` |
| **ipv6_allow_local_in_slient_drop**  string | Enable/disable silent drop of IPv6 local-in traffic.  **Choices:**   - `"enable"` - `"disable"` |
| **ipv6_allow_multicast_probe**  string | Enable/disable IPv6 address probe through Multicast.  **Choices:**   - `"enable"` - `"disable"` |
| **ipv6_allow_traffic_redirect**  string | Disable to prevent IPv6 traffic with same local ingress and egress interface from being forwarded without policy check.  **Choices:**   - `"enable"` - `"disable"` |
| **irq_time_accounting**  string | Configure CPU IRQ time accounting mode.  **Choices:**   - `"auto"` - `"force"` |
| **language**  string | GUI display language.  **Choices:**   - `"english"` - `"french"` - `"spanish"` - `"portuguese"` - `"japanese"` - `"trach"` - `"simch"` - `"korean"` |
| **ldapconntimeout**  integer | Global timeout for connections with remote LDAP servers in milliseconds (1 - 300000). |
| **lldp_reception**  string | Enable/disable Link Layer Discovery Protocol (LLDP) reception.  **Choices:**   - `"enable"` - `"disable"` |
| **lldp_transmission**  string | Enable/disable Link Layer Discovery Protocol (LLDP) transmission.  **Choices:**   - `"enable"` - `"disable"` |
| **log_single_cpu_high**  string | Enable/disable logging the event of a single CPU core reaching CPU usage threshold.  **Choices:**   - `"enable"` - `"disable"` |
| **log_ssl_connection**  string | Enable/disable logging of SSL connection events.  **Choices:**   - `"enable"` - `"disable"` |
| **log_uuid**  string | Whether UUIDs are added to traffic logs. You can disable UUIDs, add firewall policy UUIDs to traffic logs, or add all UUIDs to traffic logs.  **Choices:**   - `"disable"` - `"policy-only"` - `"extended"` |
| **log_uuid_address**  string | Enable/disable insertion of address UUIDs to traffic logs.  **Choices:**   - `"enable"` - `"disable"` |
| **log_uuid_policy**  string | Enable/disable insertion of policy UUIDs to traffic logs.  **Choices:**   - `"enable"` - `"disable"` |
| **login_timestamp**  string | Enable/disable login time recording.  **Choices:**   - `"enable"` - `"disable"` |
| **long_vdom_name**  string | Enable/disable long VDOM name support.  **Choices:**   - `"enable"` - `"disable"` |
| **management_ip**  string | Management IP address of this FortiGate. Used to log into this FortiGate from another FortiGate in the Security Fabric. |
| **management_port**  integer | Overriding port for management connection (Overrides admin port). |
| **management_port_use_admin_sport**  string | Enable/disable use of the admin-sport setting for the management port. If disabled, FortiGate will allow user to specify management-port.  **Choices:**   - `"enable"` - `"disable"` |
| **management_vdom**  string | Management virtual domain name. Source system.vdom.name. |
| **max_dlpstat_memory**  integer | Maximum DLP stat memory (0 - 4294967295). |
| **max_route_cache_size**  integer | Maximum number of IP route cache entries (0 - 2147483647). |
| **mc_ttl_notchange**  string | Enable/disable no modification of multicast TTL.  **Choices:**   - `"enable"` - `"disable"` |
| **memory_use_threshold_extreme**  integer | Threshold at which memory usage is considered extreme (new sessions are dropped) (% of total RAM). |
| **memory_use_threshold_green**  integer | Threshold at which memory usage forces the FortiGate to exit conserve mode (% of total RAM). |
| **memory_use_threshold_red**  integer | Threshold at which memory usage forces the FortiGate to enter conserve mode (% of total RAM). |
| **miglog_affinity**  string | Affinity setting for logging (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx). |
| **miglogd_children**  integer | Number of logging (miglogd) processes to be allowed to run. Higher number can reduce performance; lower number can slow log processing time. |
| **multi_factor_authentication**  string | Enforce all login methods to require an additional authentication factor .  **Choices:**   - `"optional"` - `"mandatory"` |
| **multicast_forward**  string | Enable/disable multicast forwarding.  **Choices:**   - `"enable"` - `"disable"` |
| **ndp_max_entry**  integer | Maximum number of NDP table entries (set to 65,536 or higher; if set to 0, kernel holds 65,536 entries). |
| **per_user_bal**  string | Enable/disable per-user block/allow list filter.  **Choices:**   - `"enable"` - `"disable"` |
| **per_user_bwl**  string | Enable/disable per-user black/white list filter.  **Choices:**   - `"enable"` - `"disable"` |
| **pmtu_discovery**  string | Enable/disable path MTU discovery.  **Choices:**   - `"enable"` - `"disable"` |
| **policy_auth_concurrent**  integer | Number of concurrent firewall use logins from the same user (1 - 100). |
| **post_login_banner**  string | Enable/disable displaying the administrator access disclaimer message after an administrator successfully logs in.  **Choices:**   - `"disable"` - `"enable"` |
| **pre_login_banner**  string | Enable/disable displaying the administrator access disclaimer message on the login page before an administrator logs in.  **Choices:**   - `"enable"` - `"disable"` |
| **private_data_encryption**  string | Enable/disable private data encryption using an AES 128-bit key or passpharse.  **Choices:**   - `"disable"` - `"enable"` |
| **proxy_auth_lifetime**  string | Enable/disable authenticated users lifetime control. This is a cap on the total time a proxy user can be authenticated for after which re-authentication will take place.  **Choices:**   - `"enable"` - `"disable"` |
| **proxy_auth_lifetime_timeout**  integer | Lifetime timeout in minutes for authenticated users (5 - 65535 min). |
| **proxy_auth_timeout**  integer | Authentication timeout in minutes for authenticated users (1 - 300 min). |
| **proxy_cert_use_mgmt_vdom**  string | Enable/disable using management VDOM to send requests.  **Choices:**   - `"enable"` - `"disable"` |
| **proxy_cipher_hardware_acceleration**  string | Enable/disable using content processor (CP8 or CP9) hardware acceleration to encrypt and decrypt IPsec and SSL traffic.  **Choices:**   - `"disable"` - `"enable"` |
| **proxy_hardware_acceleration**  string | Enable/disable email proxy hardware acceleration.  **Choices:**   - `"disable"` - `"enable"` |
| **proxy_keep_alive_mode**  string | Control if users must re-authenticate after a session is closed, traffic has been idle, or from the point at which the user was authenticated.  **Choices:**   - `"session"` - `"traffic"` - `"re-authentication"` |
| **proxy_kxp_hardware_acceleration**  string | Enable/disable using the content processor to accelerate KXP traffic.  **Choices:**   - `"disable"` - `"enable"` |
| **proxy_re_authentication_mode**  string | Control if users must re-authenticate after a session is closed, traffic has been idle, or from the point at which the user was first created.  **Choices:**   - `"session"` - `"traffic"` - `"absolute"` |
| **proxy_re_authentication_time**  integer | The time limit that users must re-authenticate if proxy-keep-alive-mode is set to re-authenticate (1 - 86400 sec, default=30s. |
| **proxy_resource_mode**  string | Enable/disable use of the maximum memory usage on the FortiGate unit”s proxy processing of resources, such as block lists, allow lists, and external resources.  **Choices:**   - `"enable"` - `"disable"` |
| **proxy_worker_count**  integer | Proxy worker count. |
| **quic_ack_thresold**  integer | Maximum number of unacknowledged packets before sending ACK (2 - 5). |
| **quic_congestion_control_algo**  string | QUIC congestion control algorithm .  **Choices:**   - `"cubic"` - `"bbr"` - `"bbr2"` - `"reno"` |
| **quic_max_datagram_size**  integer | Maximum transmit datagram size (1200 - 1500). |
| **quic_pmtud**  string | Enable/disable path MTU discovery .  **Choices:**   - `"enable"` - `"disable"` |
| **quic_tls_handshake_timeout**  integer | Time-to-live (TTL) for TLS handshake in seconds (1 - 60). |
| **quic_udp_payload_size_shaping_per_cid**  string | Enable/disable UDP payload size shaping per connection ID .  **Choices:**   - `"enable"` - `"disable"` |
| **radius_port**  integer | RADIUS service port number. |
| **reboot_upon_config_restore**  string | Enable/disable reboot of system upon restoring configuration.  **Choices:**   - `"enable"` - `"disable"` |
| **refresh**  integer | Statistics refresh interval second(s) in GUI. |
| **remoteauthtimeout**  integer | Number of seconds that the FortiGate waits for responses from remote RADIUS, LDAP, or TACACS+ authentication servers. (1-300 sec). |
| **reset_sessionless_tcp**  string | Action to perform if the FortiGate receives a TCP packet but cannot find a corresponding session in its session table. NAT/Route mode only.  **Choices:**   - `"enable"` - `"disable"` |
| **restart_time**  string | Daily restart time (hh:mm). |
| **revision_backup_on_logout**  string | Enable/disable back-up of the latest configuration revision when an administrator logs out of the CLI or GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **revision_image_auto_backup**  string | Enable/disable back-up of the latest image revision after the firmware is upgraded.  **Choices:**   - `"enable"` - `"disable"` |
| **scanunit_count**  integer | Number of scanunits. The range and the default depend on the number of CPUs. Only available on FortiGate units with multiple CPUs. |
| **security_rating_result_submission**  string | Enable/disable the submission of Security Rating results to FortiGuard.  **Choices:**   - `"enable"` - `"disable"` |
| **security_rating_run_on_schedule**  string | Enable/disable scheduled runs of Security Rating.  **Choices:**   - `"enable"` - `"disable"` |
| **send_pmtu_icmp**  string | Enable/disable sending of path maximum transmission unit (PMTU) - ICMP destination unreachable packet and to support PMTUD protocol on your network to reduce fragmentation of packets.  **Choices:**   - `"enable"` - `"disable"` |
| **sflowd_max_children_num**  integer | Maximum number of sflowd child processes allowed to run. |
| **snat_route_change**  string | Enable/disable the ability to change the source NAT route.  **Choices:**   - `"enable"` - `"disable"` |
| **special_file_23_support**  string | Enable/disable detection of those special format files when using Data Leak Prevention.  **Choices:**   - `"disable"` - `"enable"` |
| **speedtest_server**  string | Enable/disable speed test server.  **Choices:**   - `"enable"` - `"disable"` |
| **split_port**  list / elements=string | Split port(s) to multiple 10Gbps ports. |
| **ssd_trim_date**  integer | Date within a month to run ssd trim. |
| **ssd_trim_freq**  string | How often to run SSD Trim . SSD Trim prevents SSD drive data loss by finding and isolating errors.  **Choices:**   - `"never"` - `"hourly"` - `"daily"` - `"weekly"` - `"monthly"` |
| **ssd_trim_hour**  integer | Hour of the day on which to run SSD Trim (0 - 23). |
| **ssd_trim_min**  integer | Minute of the hour on which to run SSD Trim (0 - 59, 60 for random). |
| **ssd_trim_weekday**  string | Day of week to run SSD Trim.  **Choices:**   - `"sunday"` - `"monday"` - `"tuesday"` - `"wednesday"` - `"thursday"` - `"friday"` - `"saturday"` |
| **ssh_cbc_cipher**  string | Enable/disable CBC cipher for SSH access.  **Choices:**   - `"enable"` - `"disable"` |
| **ssh_enc_algo**  list / elements=string | Select one or more SSH ciphers.  **Choices:**   - `"chacha20-poly1305@openssh.com"` - `"aes128-ctr"` - `"aes192-ctr"` - `"aes256-ctr"` - `"arcfour256"` - `"arcfour128"` - `"aes128-cbc"` - `"3des-cbc"` - `"blowfish-cbc"` - `"cast128-cbc"` - `"aes192-cbc"` - `"aes256-cbc"` - `"arcfour"` - `"rijndael-cbc@lysator.liu.se"` - `"aes128-gcm@openssh.com"` - `"aes256-gcm@openssh.com"` |
| **ssh_hmac_md5**  string | Enable/disable HMAC-MD5 for SSH access.  **Choices:**   - `"enable"` - `"disable"` |
| **ssh_hostkey_algo**  list / elements=string | Select one or more SSH hostkey algorithms.  **Choices:**   - `"ssh-rsa"` - `"ecdsa-sha2-nistp521"` - `"rsa-sha2-256"` - `"rsa-sha2-512"` - `"ssh-ed25519"` |
| **ssh_kex_algo**  list / elements=string | Select one or more SSH kex algorithms.  **Choices:**   - `"diffie-hellman-group1-sha1"` - `"diffie-hellman-group14-sha1"` - `"diffie-hellman-group14-sha256"` - `"diffie-hellman-group16-sha512"` - `"diffie-hellman-group18-sha512"` - `"diffie-hellman-group-exchange-sha1"` - `"diffie-hellman-group-exchange-sha256"` - `"curve25519-sha256@libssh.org"` - `"ecdh-sha2-nistp256"` - `"ecdh-sha2-nistp384"` - `"ecdh-sha2-nistp521"` |
| **ssh_kex_sha1**  string | Enable/disable SHA1 key exchange for SSH access.  **Choices:**   - `"enable"` - `"disable"` |
| **ssh_mac_algo**  list / elements=string | Select one or more SSH MAC algorithms.  **Choices:**   - `"hmac-md5"` - `"hmac-md5-etm@openssh.com"` - `"hmac-md5-96"` - `"hmac-md5-96-etm@openssh.com"` - `"hmac-sha1"` - `"hmac-sha1-etm@openssh.com"` - `"hmac-sha2-256"` - `"hmac-sha2-256-etm@openssh.com"` - `"hmac-sha2-512"` - `"hmac-sha2-512-etm@openssh.com"` - `"hmac-ripemd160"` - `"hmac-ripemd160@openssh.com"` - `"hmac-ripemd160-etm@openssh.com"` - `"umac-64@openssh.com"` - `"umac-128@openssh.com"` - `"umac-64-etm@openssh.com"` - `"umac-128-etm@openssh.com"` |
| **ssh_mac_weak**  string | Enable/disable HMAC-SHA1 and UMAC-64-ETM for SSH access.  **Choices:**   - `"enable"` - `"disable"` |
| **ssl_min_proto_version**  string | Minimum supported protocol version for SSL/TLS connections .  **Choices:**   - `"SSLv3"` - `"TLSv1"` - `"TLSv1-1"` - `"TLSv1-2"` - `"TLSv1-3"` |
| **ssl_static_key_ciphers**  string | Enable/disable static key ciphers in SSL/TLS connections (e.g. AES128-SHA, AES256-SHA, AES128-SHA256, AES256-SHA256).  **Choices:**   - `"enable"` - `"disable"` |
| **sslvpn_cipher_hardware_acceleration**  string | sslvpn-cipher-hardware-acceleration  **Choices:**   - `"enable"` - `"disable"` |
| **sslvpn_ems_sn_check**  string | Enable/disable verification of EMS serial number in SSL-VPN connection.  **Choices:**   - `"enable"` - `"disable"` |
| **sslvpn_kxp_hardware_acceleration**  string | sslvpn-kxp-hardware-acceleration  **Choices:**   - `"enable"` - `"disable"` |
| **sslvpn_max_worker_count**  integer | Maximum number of SSL-VPN processes. Upper limit for this value is the number of CPUs and depends on the model. Default value of zero means the SSLVPN daemon decides the number of worker processes. |
| **sslvpn_plugin_version_check**  string | sslvpn-plugin-version-check  **Choices:**   - `"enable"` - `"disable"` |
| **sslvpn_web_mode**  string | Enable/disable SSL-VPN web mode.  **Choices:**   - `"enable"` - `"disable"` |
| **strict_dirty_session_check**  string | Enable to check the session against the original policy when revalidating. This can prevent dropping of redirected sessions when web-filtering and authentication are enabled together. If this option is enabled, the FortiGate unit deletes a session if a routing or policy change causes the session to no longer match the policy that originally allowed the session.  **Choices:**   - `"enable"` - `"disable"` |
| **strong_crypto**  string | Enable to use strong encryption and only allow strong ciphers and digest for HTTPS/SSH/TLS/SSL functions.  **Choices:**   - `"enable"` - `"disable"` |
| **switch_controller**  string | Enable/disable switch controller feature. Switch controller allows you to manage FortiSwitch from the FortiGate itself.  **Choices:**   - `"disable"` - `"enable"` |
| **switch_controller_reserved_network**  string | Configure reserved network subnet for managed switches. This is available when the switch controller is enabled. |
| **sys_perf_log_interval**  integer | Time in minutes between updates of performance statistics logging. (1 - 15 min). |
| **syslog_affinity**  string | Affinity setting for syslog (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx). |
| **tcp_halfclose_timer**  integer | Number of seconds the FortiGate unit should wait to close a session after one peer has sent a FIN packet but the other has not responded (1 - 86400 sec (1 day)). |
| **tcp_halfopen_timer**  integer | Number of seconds the FortiGate unit should wait to close a session after one peer has sent an open session packet but the other has not responded (1 - 86400 sec (1 day)). |
| **tcp_option**  string | Enable SACK, timestamp and MSS TCP options.  **Choices:**   - `"enable"` - `"disable"` |
| **tcp_rst_timer**  integer | Length of the TCP CLOSE state in seconds (5 - 300 sec). |
| **tcp_timewait_timer**  integer | Length of the TCP TIME-WAIT state in seconds (1 - 300 sec). |
| **tftp**  string | Enable/disable TFTP.  **Choices:**   - `"enable"` - `"disable"` |
| **timezone**  string | Number corresponding to your time zone from 00 to 86. Enter set timezone ? to view the list of time zones and the numbers that represent them.  **Choices:**   - `"01"` - `"02"` - `"03"` - `"04"` - `"05"` - `"81"` - `"06"` - `"07"` - `"08"` - `"09"` - `"10"` - `"11"` - `"12"` - `"13"` - `"74"` - `"14"` - `"77"` - `"15"` - `"87"` - `"16"` - `"17"` - `"18"` - `"19"` - `"20"` - `"75"` - `"21"` - `"22"` - `"23"` - `"24"` - `"80"` - `"79"` - `"25"` - `"26"` - `"27"` - `"28"` - `"78"` - `"29"` - `"30"` - `"31"` - `"32"` - `"33"` - `"34"` - `"35"` - `"36"` - `"37"` - `"38"` - `"83"` - `"84"` - `"40"` - `"85"` - `"39"` - `"41"` - `"42"` - `"43"` - `"44"` - `"45"` - `"46"` - `"47"` - `"51"` - `"48"` - `"49"` - `"50"` - `"52"` - `"53"` - `"54"` - `"55"` - `"56"` - `"57"` - `"58"` - `"59"` - `"60"` - `"61"` - `"62"` - `"63"` - `"64"` - `"65"` - `"66"` - `"67"` - `"68"` - `"69"` - `"70"` - `"71"` - `"72"` - `"00"` - `"82"` - `"73"` - `"86"` - `"76"` |
| **tp_mc_skip_policy**  string | Enable/disable skip policy check and allow multicast through.  **Choices:**   - `"enable"` - `"disable"` |
| **traffic_priority**  string | Choose Type of Service (ToS) or Differentiated Services Code Point (DSCP) for traffic prioritization in traffic shaping.  **Choices:**   - `"tos"` - `"dscp"` |
| **traffic_priority_level**  string | Default system-wide level of priority for traffic prioritization.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **two_factor_email_expiry**  integer | Email-based two-factor authentication session timeout (30 - 300 seconds (5 minutes)). |
| **two_factor_fac_expiry**  integer | FortiAuthenticator token authentication session timeout (10 - 3600 seconds (1 hour)). |
| **two_factor_ftk_expiry**  integer | FortiToken authentication session timeout (60 - 600 sec (10 minutes)). |
| **two_factor_ftm_expiry**  integer | FortiToken Mobile session timeout (1 - 168 hours (7 days)). |
| **two_factor_sms_expiry**  integer | SMS-based two-factor authentication session timeout (30 - 300 sec). |
| **udp_idle_timer**  integer | UDP connection session timeout. This command can be useful in managing CPU and memory resources (1 - 86400 seconds (1 day)). |
| **url_filter_affinity**  string | URL filter CPU affinity. |
| **url_filter_count**  integer | URL filter daemon count. |
| **user_device_store_max_devices**  integer | Maximum number of devices allowed in user device store. |
| **user_device_store_max_unified_mem**  integer | Maximum unified memory allowed in user device store. |
| **user_device_store_max_users**  integer | Maximum number of users allowed in user device store. |
| **user_server_cert**  string | Certificate to use for https user authentication. Source certificate.local.name. |
| **vdom_admin**  string | vdom-admin  **Choices:**   - `"enable"` - `"disable"` |
| **vdom_mode**  string | Enable/disable support for multiple virtual domains (VDOMs).  **Choices:**   - `"no-vdom"` - `"multi-vdom"` - `"split-vdom"` |
| **vip_arp_range**  string | Controls the number of ARPs that the FortiGate sends for a Virtual IP (VIP) address range.  **Choices:**   - `"unlimited"` - `"restricted"` |
| **virtual_server_count**  integer | Maximum number of virtual server processes to create. The maximum is the number of CPU cores. This is not available on single-core CPUs. |
| **virtual_server_hardware_acceleration**  string | Enable/disable virtual server hardware acceleration.  **Choices:**   - `"disable"` - `"enable"` |
| **vpn_ems_sn_check**  string | Enable/disable verification of EMS serial number in SSL-VPN and IPsec VPN connection.  **Choices:**   - `"enable"` - `"disable"` |
| **wad_affinity**  string | Affinity setting for wad (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx). |
| **wad_csvc_cs_count**  integer | Number of concurrent WAD-cache-service object-cache processes. |
| **wad_csvc_db_count**  integer | Number of concurrent WAD-cache-service byte-cache processes. |
| **wad_memory_change_granularity**  integer | Minimum percentage change in system memory usage detected by the wad daemon prior to adjusting TCP window size for any active connection. |
| **wad_restart_end_time**  string | WAD workers daily restart end time (hh:mm). |
| **wad_restart_mode**  string | WAD worker restart mode .  **Choices:**   - `"none"` - `"time"` - `"memory"` |
| **wad_restart_start_time**  string | WAD workers daily restart time (hh:mm). |
| **wad_source_affinity**  string | Enable/disable dispatching traffic to WAD workers based on source affinity.  **Choices:**   - `"disable"` - `"enable"` |
| **wad_worker_count**  integer | Number of explicit proxy WAN optimization daemon (WAD) processes. By default WAN optimization, explicit proxy, and web caching is handled by all of the CPU cores in a FortiGate unit. |
| **wifi_ca_certificate**  string | CA certificate that verifies the WiFi certificate. Source certificate.ca.name. |
| **wifi_certificate**  string | Certificate to use for WiFi authentication. Source certificate.local.name. |
| **wimax_4g_usb**  string | Enable/disable comparability with WiMAX 4G USB devices.  **Choices:**   - `"enable"` - `"disable"` |
| **wireless_controller**  string | Enable/disable the wireless controller feature to use the FortiGate unit to manage FortiAPs.  **Choices:**   - `"enable"` - `"disable"` |
| **wireless_controller_port**  integer | Port used for the control channel in wireless controller mode (wireless-mode is ac). The data channel port is the control channel port number plus one (1024 - 49150). |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_system_global_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_global_module.md#id5)

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
  - name: Configure global attributes.
    fortios_system_global:
      vdom:  "{{ vdom }}"
      system_global:
        admin_concurrent: "enable"
        admin_console_timeout: "0"
        admin_forticloud_sso_default_profile: "<your_own_value> (source system.accprofile.name)"
        admin_forticloud_sso_login: "enable"
        admin_host: "myhostname"
        admin_hsts_max_age: "15552000"
        admin_https_pki_required: "enable"
        admin_https_redirect: "enable"
        admin_https_ssl_banned_ciphers: "RSA"
        admin_https_ssl_ciphersuites: "TLS-AES-128-GCM-SHA256"
        admin_https_ssl_versions: "tlsv1-1"
        admin_lockout_duration: "60"
        admin_lockout_threshold: "3"
        admin_login_max: "100"
        admin_maintainer: "enable"
        admin_port: "80"
        admin_restrict_local: "enable"
        admin_scp: "enable"
        admin_server_cert: "<your_own_value> (source certificate.local.name)"
        admin_sport: "443"
        admin_ssh_grace_time: "120"
        admin_ssh_password: "enable"
        admin_ssh_port: "22"
        admin_ssh_v1: "enable"
        admin_telnet: "enable"
        admin_telnet_port: "23"
        admintimeout: "5"
        alias: "<your_own_value>"
        allow_traffic_redirect: "enable"
        anti_replay: "disable"
        arp_max_entry: "131072"
        asymroute: "enable"
        auth_cert: "<your_own_value> (source certificate.local.name)"
        auth_http_port: "1000"
        auth_https_port: "1003"
        auth_ike_saml_port: "1001"
        auth_keepalive: "enable"
        auth_session_limit: "block-new"
        auto_auth_extension_device: "enable"
        autorun_log_fsck: "enable"
        av_affinity: "<your_own_value>"
        av_failopen: "pass"
        av_failopen_session: "enable"
        batch_cmdb: "enable"
        block_session_timer: "30"
        br_fdb_max_entry: "8192"
        cert_chain_max: "8"
        cfg_revert_timeout: "600"
        cfg_save: "automatic"
        check_protocol_header: "loose"
        check_reset_range: "strict"
        cli_audit_log: "enable"
        cloud_communication: "enable"
        clt_cert_req: "enable"
        cmdbsvr_affinity: "<your_own_value>"
        compliance_check: "enable"
        compliance_check_time: "<your_own_value>"
        cpu_use_threshold: "90"
        csr_ca_attribute: "enable"
        daily_restart: "enable"
        default_service_source_port: "<your_own_value>"
        device_identification_active_scan_delay: "1800"
        device_idle_timeout: "300"
        dh_params: "1024"
        dnsproxy_worker_count: "1"
        dst: "enable"
        early_tcp_npu_session: "enable"
        edit_vdom_prompt: "enable"
        endpoint_control_fds_access: "enable"
        endpoint_control_portal_port: "32767"
        extender_controller_reserved_network: "<your_own_value>"
        failtime: "5"
        faz_disk_buffer_size: "0"
        fds_statistics: "enable"
        fds_statistics_period: "60"
        fec_port: "50000"
        fgd_alert_subscription: "advisory"
        forticarrier_bypass: "enable"
        forticonverter_config_upload: "once"
        forticonverter_integration: "enable"
        fortiextender: "disable"
        fortiextender_data_port: "25246"
        fortiextender_discovery_lockdown: "disable"
        fortiextender_provision_on_authorization: "enable"
        fortiextender_vlan_mode: "enable"
        fortiipam_integration: "enable"
        fortiservice_port: "8013"
        fortitoken_cloud: "enable"
        fortitoken_cloud_push_status: "enable"
        fortitoken_cloud_sync_interval: "24"
        gui_allow_default_hostname: "enable"
        gui_allow_incompatible_fabric_fgt: "enable"
        gui_app_detection_sdwan: "enable"
        gui_auto_upgrade_setup_warning: "enable"
        gui_cdn_domain_override: "<your_own_value>"
        gui_cdn_usage: "enable"
        gui_certificates: "enable"
        gui_custom_language: "enable"
        gui_date_format: "yyyy/MM/dd"
        gui_date_time_source: "system"
        gui_device_latitude: "<your_own_value>"
        gui_device_longitude: "<your_own_value>"
        gui_display_hostname: "enable"
        gui_firmware_upgrade_warning: "enable"
        gui_forticare_registration_setup_warning: "enable"
        gui_fortigate_cloud_sandbox: "enable"
        gui_fortiguard_resource_fetch: "enable"
        gui_fortisandbox_cloud: "enable"
        gui_ipv6: "enable"
        gui_lines_per_page: "500"
        gui_local_out: "enable"
        gui_replacement_message_groups: "enable"
        gui_rest_api_cache: "enable"
        gui_theme: "jade"
        gui_wireless_opensecurity: "enable"
        gui_workflow_management: "enable"
        ha_affinity: "<your_own_value>"
        honor_df: "enable"
        hostname: "myhostname"
        igmp_state_limit: "3200"
        interface_subnet_usage: "disable"
        internet_service_database: "mini"
        internet_service_download_list:
         -
            id:  "126 (source firewall.internet-service.id)"
        interval: "5"
        ip_fragment_mem_thresholds: "32"
        ip_src_port_range: "<your_own_value>"
        ips_affinity: "<your_own_value>"
        ipsec_asic_offload: "enable"
        ipsec_ha_seqjump_rate: "10"
        ipsec_hmac_offload: "enable"
        ipsec_round_robin: "enable"
        ipsec_soft_dec_async: "enable"
        ipv6_accept_dad: "1"
        ipv6_allow_anycast_probe: "enable"
        ipv6_allow_local_in_slient_drop: "enable"
        ipv6_allow_multicast_probe: "enable"
        ipv6_allow_traffic_redirect: "enable"
        irq_time_accounting: "auto"
        language: "english"
        ldapconntimeout: "500"
        lldp_reception: "enable"
        lldp_transmission: "enable"
        log_single_cpu_high: "enable"
        log_ssl_connection: "enable"
        log_uuid: "disable"
        log_uuid_address: "enable"
        log_uuid_policy: "enable"
        login_timestamp: "enable"
        long_vdom_name: "enable"
        management_ip: "<your_own_value>"
        management_port: "443"
        management_port_use_admin_sport: "enable"
        management_vdom: "<your_own_value> (source system.vdom.name)"
        max_dlpstat_memory: "157"
        max_route_cache_size: "0"
        mc_ttl_notchange: "enable"
        memory_use_threshold_extreme: "95"
        memory_use_threshold_green: "82"
        memory_use_threshold_red: "88"
        miglog_affinity: "<your_own_value>"
        miglogd_children: "0"
        multi_factor_authentication: "optional"
        multicast_forward: "enable"
        ndp_max_entry: "0"
        per_user_bal: "enable"
        per_user_bwl: "enable"
        pmtu_discovery: "enable"
        policy_auth_concurrent: "0"
        post_login_banner: "disable"
        pre_login_banner: "enable"
        private_data_encryption: "disable"
        proxy_auth_lifetime: "enable"
        proxy_auth_lifetime_timeout: "480"
        proxy_auth_timeout: "10"
        proxy_cert_use_mgmt_vdom: "enable"
        proxy_cipher_hardware_acceleration: "disable"
        proxy_hardware_acceleration: "disable"
        proxy_keep_alive_mode: "session"
        proxy_kxp_hardware_acceleration: "disable"
        proxy_re_authentication_mode: "session"
        proxy_re_authentication_time: "30"
        proxy_resource_mode: "enable"
        proxy_worker_count: "0"
        quic_ack_thresold: "3"
        quic_congestion_control_algo: "cubic"
        quic_max_datagram_size: "1500"
        quic_pmtud: "enable"
        quic_tls_handshake_timeout: "5"
        quic_udp_payload_size_shaping_per_cid: "enable"
        radius_port: "1812"
        reboot_upon_config_restore: "enable"
        refresh: "0"
        remoteauthtimeout: "5"
        reset_sessionless_tcp: "enable"
        restart_time: "<your_own_value>"
        revision_backup_on_logout: "enable"
        revision_image_auto_backup: "enable"
        scanunit_count: "0"
        security_rating_result_submission: "enable"
        security_rating_run_on_schedule: "enable"
        send_pmtu_icmp: "enable"
        sflowd_max_children_num: "6"
        snat_route_change: "enable"
        special_file_23_support: "disable"
        speedtest_server: "enable"
        split_port: "<your_own_value>"
        ssd_trim_date: "1"
        ssd_trim_freq: "never"
        ssd_trim_hour: "1"
        ssd_trim_min: "60"
        ssd_trim_weekday: "sunday"
        ssh_cbc_cipher: "enable"
        ssh_enc_algo: "chacha20-poly1305@openssh.com"
        ssh_hmac_md5: "enable"
        ssh_hostkey_algo: "ssh-rsa"
        ssh_kex_algo: "diffie-hellman-group1-sha1"
        ssh_kex_sha1: "enable"
        ssh_mac_algo: "hmac-md5"
        ssh_mac_weak: "enable"
        ssl_min_proto_version: "SSLv3"
        ssl_static_key_ciphers: "enable"
        sslvpn_cipher_hardware_acceleration: "enable"
        sslvpn_ems_sn_check: "enable"
        sslvpn_kxp_hardware_acceleration: "enable"
        sslvpn_max_worker_count: "0"
        sslvpn_plugin_version_check: "enable"
        sslvpn_web_mode: "enable"
        strict_dirty_session_check: "enable"
        strong_crypto: "enable"
        switch_controller: "disable"
        switch_controller_reserved_network: "<your_own_value>"
        sys_perf_log_interval: "5"
        syslog_affinity: "<your_own_value>"
        tcp_halfclose_timer: "120"
        tcp_halfopen_timer: "10"
        tcp_option: "enable"
        tcp_rst_timer: "5"
        tcp_timewait_timer: "1"
        tftp: "enable"
        timezone: "01"
        tp_mc_skip_policy: "enable"
        traffic_priority: "tos"
        traffic_priority_level: "low"
        two_factor_email_expiry: "60"
        two_factor_fac_expiry: "60"
        two_factor_ftk_expiry: "60"
        two_factor_ftm_expiry: "72"
        two_factor_sms_expiry: "60"
        udp_idle_timer: "180"
        url_filter_affinity: "<your_own_value>"
        url_filter_count: "1"
        user_device_store_max_devices: "20921"
        user_device_store_max_unified_mem: "104609177"
        user_device_store_max_users: "20921"
        user_server_cert: "<your_own_value> (source certificate.local.name)"
        vdom_admin: "enable"
        vdom_mode: "no-vdom"
        vip_arp_range: "unlimited"
        virtual_server_count: "20"
        virtual_server_hardware_acceleration: "disable"
        vpn_ems_sn_check: "enable"
        wad_affinity: "<your_own_value>"
        wad_csvc_cs_count: "1"
        wad_csvc_db_count: "0"
        wad_memory_change_granularity: "10"
        wad_restart_end_time: "<your_own_value>"
        wad_restart_mode: "none"
        wad_restart_start_time: "<your_own_value>"
        wad_source_affinity: "disable"
        wad_worker_count: "0"
        wifi_ca_certificate: "<your_own_value> (source certificate.ca.name)"
        wifi_certificate: "<your_own_value> (source certificate.local.name)"
        wimax_4g_usb: "enable"
        wireless_controller: "enable"
        wireless_controller_port: "5246"
```

## [Return Values](fortios_system_global_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  **Returned:** always  **Sample:** `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  **Returned:** always  **Sample:** `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  **Returned:** always  **Sample:** `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  **Returned:** success  **Sample:** `"id"` |
| **name**  string | Name of the table used to fulfill the request  **Returned:** always  **Sample:** `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  **Returned:** always  **Sample:** `"webfilter"` |
| **revision**  string | Internal revision number  **Returned:** always  **Sample:** `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  **Returned:** always  **Sample:** `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  **Returned:** always  **Sample:** `"success"` |
| **vdom**  string | Virtual domain used  **Returned:** always  **Sample:** `"root"` |
| **version**  string | Version of the FortiGate  **Returned:** always  **Sample:** `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
- [Homepage](https://www.fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
