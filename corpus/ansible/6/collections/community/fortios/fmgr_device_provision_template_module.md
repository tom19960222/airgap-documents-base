---
collection: ansible
version: "6"
title: "community.fortios.fmgr_device_provision_template module – Manages Device Provisioning Templates in FortiManager."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/fortios/fmgr_device_provision_template_module.html
fetched_at: 2026-07-27T17:07:39+00:00
---
# community.fortios.fmgr_device_provision_template module – Manages Device Provisioning Templates in FortiManager.

> **Note:**
>
> This module is part of the [community.fortios collection](https://galaxy.ansible.com/community/fortios) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.fortios`.
>
> To use it in a playbook, specify: `community.fortios.fmgr_device_provision_template`.

- [Synopsis](fmgr_device_provision_template_module.md#synopsis)
- [Parameters](fmgr_device_provision_template_module.md#parameters)
- [Notes](fmgr_device_provision_template_module.md#notes)
- [Examples](fmgr_device_provision_template_module.md#examples)
- [Return Values](fmgr_device_provision_template_module.md#return-values)

## [Synopsis](fmgr_device_provision_template_module.md#id1)

- Allows the editing and assignment of device provisioning templates in FortiManager.

## [Parameters](fmgr_device_provision_template_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **admin_enable_fortiguard**  string | Enables FortiGuard security updates to their default settings.  Choices:   - `"none"` - `"direct"` - `"this-fmg"` |
| **admin_fortianalyzer_target**  string | Configures faz target. |
| **admin_fortiguard_target**  string | Configures fortiguard target.  admin_enable_fortiguard must be set to “direct”. |
| **admin_gui_theme**  string | Changes the admin gui theme.  Choices:   - `"green"` - `"red"` - `"blue"` - `"melongene"` - `"mariner"` |
| **admin_http_port**  string | Non-SSL admin gui port number. |
| **admin_https_port**  string | SSL admin gui port number. |
| **admin_https_redirect**  string | Enables or disables https redirect from http.  Choices:   - `"enable"` - `"disable"` |
| **admin_language**  string | Sets the admin gui language.  Choices:   - `"english"` - `"simch"` - `"japanese"` - `"korean"` - `"spanish"` - `"trach"` - `"french"` - `"portuguese"` |
| **admin_switch_controller**  string | Enables or disables the switch controller.  Choices:   - `"enable"` - `"disable"` |
| **admin_timeout**  string | Admin timeout in minutes. |
| **adom**  string / required | The ADOM the configuration should belong to. |
| **delete_provisioning_template**  string | If specified, all other options are ignored. The specified provisioning template will be deleted. |
| **device_unique_name**  string / required | The unique device’s name that you are editing. |
| **dns_primary_ipv4**  string | primary ipv4 dns forwarder. |
| **dns_secondary_ipv4**  string | secondary ipv4 dns forwarder. |
| **dns_suffix**  string | Sets the local dns domain suffix. |
| **mode**  string | Sets one of three modes for managing the object.  Allows use of soft-adds instead of overwriting existing values.  Choices:   - `"add"` ← (default) - `"set"` - `"delete"` - `"update"` |
| **ntp_auth**  string | Enables or disables ntp authentication.  Choices:   - `"enable"` - `"disable"` |
| **ntp_auth_pwd**  string | Sets the ntp auth password. |
| **ntp_server**  string | Only used with custom ntp_type – specifies IP of server to sync to – comma separated ip addresses for multiples. |
| **ntp_status**  string | Enables or disables ntp.  Choices:   - `"enable"` - `"disable"` |
| **ntp_sync_interval**  string | Sets the interval in minutes for ntp sync. |
| **ntp_type**  string | Enables fortiguard servers or custom servers are the ntp source.  Choices:   - `"fortiguard"` - `"custom"` |
| **ntp_v3**  string | Enables or disables ntpv3 (default is ntpv4).  Choices:   - `"enable"` - `"disable"` |
| **provision_targets**  string / required | The friendly names of devices in FortiManager to assign the provisioning template to. CSV separated list. |
| **provisioning_template**  string / required | The provisioning template you want to apply (default = default). |
| **smtp_conn_sec**  string | defines the ssl level for smtp.  Choices:   - `"none"` - `"starttls"` - `"smtps"` |
| **smtp_password**  string | SMTP password. |
| **smtp_port**  string | SMTP port number. |
| **smtp_replyto**  string | SMTP reply to address. |
| **smtp_server**  string | SMTP server ipv4 address. |
| **smtp_source_ipv4**  string | SMTP source ip address. |
| **smtp_username**  string | SMTP auth username. |
| **smtp_validate_cert**  string | Enables or disables valid certificate checking for smtp.  Choices:   - `"enable"` - `"disable"` |
| **snmp_status**  string | Enables or disables SNMP globally.  Choices:   - `"enable"` - `"disable"` |
| **snmp_v2c_id**  string | Primary key for the snmp community. this must be unique! |
| **snmp_v2c_name**  string | Specifies the v2c community name. |
| **snmp_v2c_query_hosts_ipv4**  string | - IPv4 addresses or subnets that are allowed to query SNMP v2c, comma separated (“10.7.220.59 255.255.255.0, 10.7.220.0 255.255.255.0”). |
| **snmp_v2c_query_port**  string | Sets the snmp v2c community query port. |
| **snmp_v2c_query_status**  string | Enables or disables the v2c community specified for queries.  Choices:   - `"enable"` - `"disable"` |
| **snmp_v2c_status**  string | Enables or disables the v2c community specified.  Choices:   - `"enable"` - `"disable"` |
| **snmp_v2c_trap_hosts_ipv4**  string | - IPv4 addresses of the hosts that should get SNMP v2c traps, comma separated, must include mask (“10.7.220.59 255.255.255.255, 10.7.220.60 255.255.255.255”). |
| **snmp_v2c_trap_port**  string | Sets the snmp v2c community trap port. |
| **snmp_v2c_trap_src_ipv4**  string | Source ip the traps should come from IPv4. |
| **snmp_v2c_trap_status**  string | Enables or disables the v2c community specified for traps.  Choices:   - `"enable"` - `"disable"` |
| **snmpv3_auth_proto**  string | SNMPv3 auth protocol.  Choices:   - `"md5"` - `"sha"` |
| **snmpv3_auth_pwd**  string | SNMPv3 auth pwd __ currently not encrypted! ensure this file is locked down permissions wise! |
| **snmpv3_name**  string | SNMPv3 user name. |
| **snmpv3_notify_hosts**  string | List of ipv4 hosts to send snmpv3 traps to. Comma separated IPv4 list. |
| **snmpv3_priv_proto**  string | SNMPv3 priv protocol.  Choices:   - `"aes"` - `"des"` - `"aes256"` - `"aes256cisco"` |
| **snmpv3_priv_pwd**  string | SNMPv3 priv pwd currently not encrypted! ensure this file is locked down permissions wise! |
| **snmpv3_queries**  string | Allow snmpv3_queries.  Choices:   - `"enable"` - `"disable"` |
| **snmpv3_query_port**  string | SNMPv3 query port. |
| **snmpv3_security_level**  string | SNMPv3 security level.  Choices:   - `"no-auth-no-priv"` - `"auth-no-priv"` - `"auth-priv"` |
| **snmpv3_source_ip**  string | SNMPv3 source ipv4 address for traps. |
| **snmpv3_status**  string | SNMPv3 user is enabled or disabled.  Choices:   - `"enable"` - `"disable"` |
| **snmpv3_trap_rport**  string | SNMPv3 trap remote port. |
| **snmpv3_trap_status**  string | SNMPv3 traps is enabled or disabled.  Choices:   - `"enable"` - `"disable"` |
| **syslog_certificate**  string | Certificate used to communicate with Syslog server if encryption on. |
| **syslog_enc_algorithm**  string | Enable/disable reliable syslogging with TLS encryption.  choice | high | SSL communication with high encryption algorithms.  choice | low | SSL communication with low encryption algorithms.  choice | disable | Disable SSL communication.  choice | high-medium | SSL communication with high and medium encryption algorithms.  Choices:   - `"high"` - `"low"` - `"disable"` ← (default) - `"high-medium"` |
| **syslog_facility**  string | Remote syslog facility.  choice | kernel | Kernel messages.  choice | user | Random user-level messages.  choice | mail | Mail system.  choice | daemon | System daemons.  choice | auth | Security/authorization messages.  choice | syslog | Messages generated internally by syslog.  choice | lpr | Line printer subsystem.  choice | news | Network news subsystem.  choice | uucp | Network news subsystem.  choice | cron | Clock daemon.  choice | authpriv | Security/authorization messages (private).  choice | ftp | FTP daemon.  choice | ntp | NTP daemon.  choice | audit | Log audit.  choice | alert | Log alert.  choice | clock | Clock daemon.  choice | local0 | Reserved for local use.  choice | local1 | Reserved for local use.  choice | local2 | Reserved for local use.  choice | local3 | Reserved for local use.  choice | local4 | Reserved for local use.  choice | local5 | Reserved for local use.  choice | local6 | Reserved for local use.  choice | local7 | Reserved for local use.  Choices:   - `"kernel"` - `"user"` - `"mail"` - `"daemon"` - `"auth"` - `"syslog"` ← (default) - `"lpr"` - `"news"` - `"uucp"` - `"cron"` - `"authpriv"` - `"ftp"` - `"ntp"` - `"audit"` - `"alert"` - `"clock"` - `"local0"` - `"local1"` - `"local2"` - `"local3"` - `"local4"` - `"local5"` - `"local6"` - `"local7"` |
| **syslog_filter**  string | Sets the logging level for syslog.  Choices:   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"information"` - `"debug"` |
| **syslog_mode**  string | Remote syslog logging over UDP/Reliable TCP.  choice | udp | Enable syslogging over UDP.  choice | legacy-reliable | Enable legacy reliable syslogging by RFC3195 (Reliable Delivery for Syslog).  choice | reliable | Enable reliable syslogging by RFC6587 (Transmission of Syslog Messages over TCP).  Choices:   - `"udp"` ← (default) - `"legacy-reliable"` - `"reliable"` |
| **syslog_port**  string | Syslog port that will be set. |
| **syslog_server**  string | Server the syslogs will be sent to. |
| **syslog_status**  string | Enables or disables syslogs.  Choices:   - `"enable"` - `"disable"` |

## [Notes](fmgr_device_provision_template_module.md#id3)

> **Note:**
>
> - Full Documentation at <https://ftnt-ansible-docs.readthedocs.io/en/latest/>.

## [Examples](fmgr_device_provision_template_module.md#id4)

```yaml+jinja
- name: SET SNMP SYSTEM INFO
  community.fortios.fmgr_device_provision_template:
    provisioning_template: "default"
    snmp_status: "enable"
    mode: "set"

- name: SET SNMP SYSTEM INFO ANSIBLE ADOM
  community.fortios.fmgr_device_provision_template:
    provisioning_template: "default"
    snmp_status: "enable"
    mode: "set"
    adom: "ansible"

- name: SET SNMP SYSTEM INFO different template (SNMPv2)
  community.fortios.fmgr_device_provision_template:
    provisioning_template: "ansibleTest"
    snmp_status: "enable"
    mode: "set"
    adom: "ansible"
    snmp_v2c_query_port: "162"
    snmp_v2c_trap_port: "161"
    snmp_v2c_status: "enable"
    snmp_v2c_trap_status: "enable"
    snmp_v2c_query_status: "enable"
    snmp_v2c_name: "ansibleV2c"
    snmp_v2c_id: "1"
    snmp_v2c_trap_src_ipv4: "10.7.220.41"
    snmp_v2c_trap_hosts_ipv4: "10.7.220.59 255.255.255.255, 10.7.220.60 255.255.255.255"
    snmp_v2c_query_hosts_ipv4: "10.7.220.59 255.255.255.255, 10.7.220.0 255.255.255.0"

- name: SET SNMP SYSTEM INFO different template (SNMPv3)
  community.fortios.fmgr_device_provision_template:
    provisioning_template: "ansibleTest"
    snmp_status: "enable"
    mode: "set"
    adom: "ansible"
    snmpv3_auth_proto: "sha"
    snmpv3_auth_pwd: "fortinet"
    snmpv3_name: "ansibleSNMPv3"
    snmpv3_notify_hosts: "10.7.220.59,10.7.220.60"
    snmpv3_priv_proto: "aes256"
    snmpv3_priv_pwd: "fortinet"
    snmpv3_queries: "enable"
    snmpv3_query_port: "161"
    snmpv3_security_level: "auth_priv"
    snmpv3_source_ip: "0.0.0.0"
    snmpv3_status: "enable"
    snmpv3_trap_rport: "162"
    snmpv3_trap_status: "enable"

- name: SET SYSLOG INFO
  community.fortios.fmgr_device_provision_template:
    provisioning_template: "ansibleTest"
    mode: "set"
    adom: "ansible"
    syslog_server: "10.7.220.59"
    syslog_port: "514"
    syslog_mode: "disable"
    syslog_status: "enable"
    syslog_filter: "information"

- name: SET NTP TO FORTIGUARD
  community.fortios.fmgr_device_provision_template:
    provisioning_template: "ansibleTest"
    mode: "set"
    adom: "ansible"
    ntp_status: "enable"
    ntp_sync_interval: "60"
    type: "fortiguard"

- name: SET NTP TO CUSTOM SERVER
  community.fortios.fmgr_device_provision_template:
    provisioning_template: "ansibleTest"
    mode: "set"
    adom: "ansible"
    ntp_status: "enable"
    ntp_sync_interval: "60"
    ntp_type: "custom"
    ntp_server: "10.7.220.32,10.7.220.1"
    ntp_auth: "enable"
    ntp_auth_pwd: "fortinet"
    ntp_v3: "disable"

- name: SET ADMIN GLOBAL SETTINGS
  community.fortios.fmgr_device_provision_template:
    provisioning_template: "ansibleTest"
    mode: "set"
    adom: "ansible"
    admin_https_redirect: "enable"
    admin_https_port: "4433"
    admin_http_port: "8080"
    admin_timeout: "30"
    admin_language: "english"
    admin_switch_controller: "enable"
    admin_gui_theme: "blue"
    admin_enable_fortiguard: "direct"
    admin_fortiguard_target: "10.7.220.128"
    admin_fortianalyzer_target: "10.7.220.61"

- name: SET CUSTOM SMTP SERVER
  community.fortios.fmgr_device_provision_template:
    provisioning_template: "ansibleTest"
    mode: "set"
    adom: "ansible"
    smtp_username: "ansible"
    smtp_password: "fortinet"
    smtp_port: "25"
    smtp_replyto: "ansible@do-not-reply.com"
    smtp_conn_sec: "starttls"
    smtp_server: "10.7.220.32"
    smtp_source_ipv4: "0.0.0.0"
    smtp_validate_cert: "disable"

- name: SET DNS SERVERS
  community.fortios.fmgr_device_provision_template:
    provisioning_template: "ansibleTest"
    mode: "set"
    adom: "ansible"
    dns_suffix: "ansible.local"
    dns_primary_ipv4: "8.8.8.8"
    dns_secondary_ipv4: "4.4.4.4"

- name: SET PROVISIONING TEMPLATE DEVICE TARGETS IN FORTIMANAGER
  community.fortios.fmgr_device_provision_template:
    provisioning_template: "ansibleTest"
    mode: "set"
    adom: "ansible"
    provision_targets: "FGT1, FGT2"

- name: DELETE ENTIRE PROVISIONING TEMPLATE
  community.fortios.fmgr_device_provision_template:
    delete_provisioning_template: "ansibleTest"
    mode: "delete"
    adom: "ansible"
```

## [Return Values](fmgr_device_provision_template_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  Returned: always |

### Authors

- Luke Weighall (@lweighall)
- Andrew Welsh (@Ghilli3)
- Jim Huber (@p4r4n0y1ng)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.fortios)
