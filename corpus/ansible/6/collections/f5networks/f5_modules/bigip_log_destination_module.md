---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_log_destination module – Manages log destinations on a BIG-IP."
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_log_destination_module.html
fetched_at: 2026-07-27T17:27:03+00:00
---
# f5networks.f5_modules.bigip_log_destination module – Manages log destinations on a BIG-IP.

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/f5networks/f5_modules) (version 1.21.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_log_destination`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_log_destination_module.md#synopsis)
- [Parameters](bigip_log_destination_module.md#parameters)
- [Notes](bigip_log_destination_module.md#notes)
- [Examples](bigip_log_destination_module.md#examples)
- [Return Values](bigip_log_destination_module.md#return-values)

## [Synopsis](bigip_log_destination_module.md#id1)

- Manages log destinations on a BIG-IP device.

## [Parameters](bigip_log_destination_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address**  string | Specifies the IP address that will receive messages from the specified local Log Destination.  This parameter is only available when `type` is `management-port`.  When creating a new log destination and `type` is `management-port`, this parameter is required. |
| **description**  string | The description of the log destination. |
| **distribution**  string | Specifies the distribution method used by the Remote High Speed Log destination to send messages to pool members.  When `adaptive`, connections to pool members will be added as required to provide enough logging bandwidth. This can have the undesirable effect of logs accumulating on only one pool member when it provides sufficient logging bandwidth on its own.  When `balanced`, sends each successive log to a new pool member, balancing the logs among them according to the pool’s load balancing method.  When `replicated`, replicates each log to all pool members, for redundancy.  When creating a new log destination and `type` is `remote-high-speed-log`, if this parameter is not specified, the default is `adaptive`.  Choices:   - `"adaptive"` - `"balanced"` - `"replicated"` |
| **forward_to**  string | When `type` is `remote-syslog`, specifies the management port log destination, which will be used to forward the logs to a single log server, or a remote high-speed log destination, which will be used to forward the logs to a pool of remote log servers.  When `type` is `splunk` or `arcsight`, specifies the log destination to which logs are forwarded. This log destination may be a management port destination, a remote high-speed log destination, or a remote Syslog destination which is configured to send logs to an ArcSight or Splunk server.  When creating a new log destination and `type` is `remote-syslog`, `splunk`, or `arcsight`, this parameter is required. |
| **name**  string / required | Specifies the name of the log destination. |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **pool**  string | When `type` is `remote-high-speed-log`, specifies the existing pool of remote high-speed log servers where logs will be sent.  When `type` is `ipfix`, specifies the existing LTM pool of remote IPFIX collectors. Any BIG-IP application that uses this log destination sends its IP-traffic logs to this pool of collectors.  When creating a new destination and `type` is `remote-high-speed-log` or `ipfix`, this parameter is required. |
| **port**  integer | Specifies the port of the IP address that will receive messages from the specified local Log Destination.  This parameter is only available when `type` is `management-port`.  When creating a new log destination and `type` is `management-port`, this parameter is required. |
| **protocol**  string | When `type` is `remote-high-speed-log`, specifies the protocol for the system to use to send logs to the pool of remote high-speed log servers, where the logs are stored.  When `type` is `ipfix`, can be IPFIX or Netflow v9, depending on the type of collectors you have in the pool that you specify.  When `type` is `management-port`, specifies the protocol used to send messages to the specified location.  When `type` is `management-port`, only `tcp` and `udp` are valid values.  Choices:   - `"tcp"` - `"udp"` - `"ipfix"` - `"netflow-9"` |
| **provider**  dictionary  added in f5networks.f5_modules 1.0.0 | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  Choices:   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  Default: `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP with. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  Choices:   - `false` - `true` ← (default) |
| **server_ssl_profile**  string | If the `transport_profile` is a TCP profile, you can use this field to choose a Secure Socket Layer (SSL) profile for sending logs to the IPFIX collectors.  An SSL server profile defines how to communicate securely over SSL or Transport Layer Security (TLS).  This parameter is only available when `type` is `ipfix`. |
| **state**  string | When `present`, ensures the resource exists.  When `absent`, ensures the resource is removed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **syslog_format**  string | Specifies the method to use to format the logs associated with the remote Syslog log destination.  When creating a new log destination (and `type` is `remote-syslog`), if this parameter is not specified, the default is `bsd-syslog`.  The `syslog` and `rfc5424` choices are the same.  The `bsd-syslog` and `rfc3164` choices are the same.  Choices:   - `"bsd-syslog"` - `"syslog"` - `"legacy-bigip"` - `"rfc5424"` - `"rfc3164"` |
| **template_delete_delay**  integer | Enter the time (in seconds) that the BIG-IP device should pause between deleting an obsolete IPFIX template and reusing its template ID.  This feature is useful for systems where you use iRules to create customized IPFIX templates. |
| **template_retransmit_interval**  integer | Enter the time (in seconds) between each transmission of IPFIX templates to the pool of IPFIX collectors.  The logging destination periodically retransmits all of its IPFIX templates at the interval you set in this field. These retransmissions are helpful for UDP, a lossy transport mechanism.  This parameter is only available when `type` is `ipfix`. |
| **transport_profile**  string | Is a transport profile based on either TCP or UDP.  This profile defines the TCP or UDP options used to send IP-traffic logs to the pool of collectors.  This parameter is only available when `type` is `ipfix`. |
| **type**  string / required | Specifies the type of log destination.  Once created, this parameter cannot be changed.  Choices:   - `"remote-high-speed-log"` - `"remote-syslog"` - `"arcsight"` - `"splunk"` - `"management-port"` - `"ipfix"` |

## [Notes](bigip_log_destination_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_log_destination_module.md#id4)

```yaml+jinja
- name: Create a high-speed logging destination
  bigip_log_destination:
    name: foo
    type: remote-high-speed-log
    pool: my-ltm-pool
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Create a remote-syslog logging destination
  bigip_log_destination:
    name: foo
    type: remote-syslog
    syslog_format: rfc5424
    forward_to: my-destination
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_log_destination_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **address**  string | The new Address value.  Returned: changed  Sample: `"1.2.3.2"` |
| **distribution**  string | The new Distribution Method value.  Returned: changed  Sample: `"balanced"` |
| **forward_to**  string | The new Forward To value.  Returned: changed  Sample: `"/Common/dest1"` |
| **pool**  string | The new Pool value.  Returned: changed  Sample: `"/Common/pool1"` |
| **port**  integer | The new Port value.  Returned: changed  Sample: `2020` |
| **protocol**  string | The new Protocol value.  Returned: changed  Sample: `"tcp"` |
| **server_ssl_profile**  string | The new Server SSL Profile value.  Returned: changed  Sample: `"/Common/serverssl"` |
| **syslog_format**  string | The new Syslog format value.  Returned: changed  Sample: `"syslog"` |
| **template_delete_delay**  integer | The new Template Delete Delay value.  Returned: changed  Sample: `20` |
| **template_retransmit_interval**  integer | The new Template Retransmit Interval value.  Returned: changed  Sample: `200` |
| **transport_profile**  string | The new Transport Profile value.  Returned: changed  Sample: `"/Common/tcp"` |

### Authors

- Tim Rupp (@caphrim007)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
