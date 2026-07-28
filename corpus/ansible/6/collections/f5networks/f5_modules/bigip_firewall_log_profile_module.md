---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_firewall_log_profile module – Manages AFM logging profiles configured in the system"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_firewall_log_profile_module.html
fetched_at: 2026-07-27T17:26:41+00:00
---
# f5networks.f5_modules.bigip_firewall_log_profile module – Manages AFM logging profiles configured in the system

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_firewall_log_profile`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_firewall_log_profile_module.md#synopsis)
- [Parameters](bigip_firewall_log_profile_module.md#parameters)
- [Notes](bigip_firewall_log_profile_module.md#notes)
- [Examples](bigip_firewall_log_profile_module.md#examples)
- [Return Values](bigip_firewall_log_profile_module.md#return-values)

## [Synopsis](bigip_firewall_log_profile_module.md#id1)

- Manages AFM (Advanced Firewall Manager) logging profiles configured in the system along with basic information about each profile.

## [Parameters](bigip_firewall_log_profile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | Description of the log profile. |
| **dos_protection**  dictionary | Configures DoS related settings of the log profile. |
| **dns_publisher**  string | Specifies the name of the log publisher used for DNS DoS events.  To specify the log_publisher on a different partition from the AFM log profile, specify the name in fullpath format, e.g. `/Foobar/log-publisher`, otherwise the partition for the log publisher is inferred from the `partition` module parameter. |
| **network_publisher**  string | Specifies the name of the log publisher used for DoS Network events.  To specify the log_publisher on a different partition from the AFM log profile, specify the name in fullpath format, e.g. `/Foobar/log-publisher`, otherwise the partition for the log publisher is inferred from the `partition` module parameter. |
| **sip_publisher**  string | Specifies the name of the log publisher used for SIP DoS events.  To specify the log_publisher on a different partition from the AFM log profile, specify the name in fullpath format, e.g. `/Foobar/log-publisher`, otherwise the partition for the log publisher is inferred from the `partition` module parameter. |
| **ip_intelligence**  dictionary | Configures IP Intelligence related settings of the log profile. |
| **log_publisher**  string | Specifies the name of the log publisher used for IP Intelligence events.  To specify the log_publisher on a different partition from the AFM log profile, specify the name in fullpath format, e.g. `/Foobar/log-publisher`, otherwise the partition for the log publisher is inferred the from `partition` module parameter. |
| **log_rtbh**  boolean | When `yes`, specifies remotely triggered blackholing events are logged.  Choices:   - `false` - `true` |
| **log_shun**  boolean | When `yes`, specifies IP Intelligence shun list events are logged.  This option can only be set on the `global-network` built-in profile.  Choices:   - `false` - `true` |
| **log_translation_fields**  boolean | This option is used to enable or disable the logging of translated (i.e server side) fields in IP Intelligence log messages.  Translated fields include (but are not limited to) source address/port, destination address/port, IP protocol, route domain, and VLAN.  Choices:   - `false` - `true` |
| **rate_limit**  string | Defines a rate limit for all combined IP intelligence log messages per second. Beyond this rate limit, log messages are not logged until the threshold drops below the specified rate.  To specify an indefinite rate, use the value `indefinite`.  If specifying a numeric rate, the value must be between `1` and `4294967295`. |
| **name**  string / required | Specifies the name of the log profile. |
| **partition**  string | Device partition to create log profile on.  Parameter also used when specifying names for log publishers, unless log publisher names are in fullpath format.  Default: `"Common"` |
| **port_misuse**  dictionary | Port Misuse log configuration. |
| **log_publisher**  string | Specifies the name of the log publisher used for Port Misuse events.  To specify the log_publisher on a different partition from the AFM log profile, specify the name in fullpath format, e.g. `/Foobar/log-publisher`, otherwise the partition for the log publisher is inferred from the `partition` module parameter. |
| **rate_limit**  string | Defines a rate limit for all combined port misuse log messages per second. Beyond this rate limit, log messages are not logged until the threshold drops below the specified rate.  To specify an indefinite rate, use the value `indefinite`.  If specifying a numeric rate, the value must be between `1` and `4294967295`. |
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
| **state**  string | When `state` is `present`, ensures the resource exists.  When `state` is `absent`, ensures the resource is removed. Attempts to remove built-in system profiles are ignored and no change is returned.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](bigip_firewall_log_profile_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_firewall_log_profile_module.md#id4)

```yaml+jinja
- name: Create a basic log profile with port misuse
  bigip_firewall_log_profile:
    name: barbaz
    port_misuse:
      rate_limit: 30000
      log_publisher: local-db-pub
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Change ip_intelligence settings, publisher on different partition, remove port misuse
  bigip_firewall_log_profile:
    name: barbaz
    ip_intelligence:
      rate_limit: 400000
      log_translation_fields: yes
      log_rtbh: yes
      log_publisher: "/foobar/non-local-db"
    port_misuse:
      log_publisher: ""
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Create a log profile with dos protection, different partition
  bigip_firewall_log_profile:
    name: foobar
    partition: foobar
    dos_protection:
      dns_publisher: "/Common/local-db-pub"
      sip_publisher: "non-local-db"
      network_publisher: "/Common/local-db-pub"
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove log profile
  bigip_firewall_log_profile:
    name: barbaz
    partition: Common
    state: absent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_firewall_log_profile_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | New description of the AFM log profile.  Returned: changed  Sample: `"This is my description"` |
| **dos_protection**  complex | Log publishers used in DoS related settings of the log profile.  Returned: changed  Sample: `"hash/dictionary of values"` |
| **dns_publisher**  string | The name of the log publisher used for DNS DoS events.  Returned: changed  Sample: `"/Common/local-db-publisher"` |
| **network_publisher**  string | The name of the log publisher used for DoS Network events.  Returned: changed  Sample: `"/Common/local-db-publisher"` |
| **sip_publisher**  string | The name of the log publisher used for SIP DoS events.  Returned: changed  Sample: `"/Common/local-db-publisher"` |
| **ip_intelligence**  complex | IP Intelligence related settings of the log profile.  Returned: changed  Sample: `"hash/dictionary of values"` |
| **log_publisher**  string | The name of the log publisher used for IP Intelligence events.  Returned: changed  Sample: `"/Common/local-db-publisher"` |
| **log_rtbh**  boolean | Logging of remotely triggered blackholing events.  Returned: changed  Sample: `true` |
| **log_shun**  boolean | Logging of IP Intelligence shun list events.  Returned: changed  Sample: `false` |
| **log_translation_fields**  boolean | Logging of translated fields in IP Intelligence log messages.  Returned: changed  Sample: `false` |
| **rate_limit**  string | The rate limit for all combined IP intelligence log messages per second.  Returned: changed  Sample: `"indefinite"` |
| **port_misuse**  complex | Port Misuse related settings of the log profile.  Returned: changed  Sample: `"hash/dictionary of values"` |
| **log_publisher**  string | The name of the log publisher used for Port Misuse events.  Returned: changed  Sample: `"/Common/local-db-publisher"` |
| **rate_limit**  string | The rate limit for all combined Port Misuse log messages per second.  Returned: changed  Sample: `"indefinite"` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
