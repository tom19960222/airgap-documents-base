---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_firewall_log_profile_network module – Configures Network Firewall related settings of the log profile"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_firewall_log_profile_network_module.html
fetched_at: 2026-07-28T02:06:08+00:00
---
# f5networks.f5_modules.bigip_firewall_log_profile_network module – Configures Network Firewall related settings of the log profile

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_firewall_log_profile_network`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_firewall_log_profile_network_module.md#synopsis)
- [Parameters](bigip_firewall_log_profile_network_module.md#parameters)
- [Notes](bigip_firewall_log_profile_network_module.md#notes)
- [Examples](bigip_firewall_log_profile_network_module.md#examples)
- [Return Values](bigip_firewall_log_profile_network_module.md#return-values)

## [Synopsis](bigip_firewall_log_profile_network_module.md#id1)

- Configures Network Firewall related settings of the log profile.

## [Parameters](bigip_firewall_log_profile_network_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **log_format_delimiter**  string | Specifies the delimiter string when using a `log_storage_format` of `field-list`.  When creating a new profile, if this parameter is not specified, the default value of `,` (the comma character) is used.  This option is valid when the `log_storage_format` is set to `field-list`. It is ignored otherwise.  Depending on the delimiter used, it may be necessary to wrap the delimiter in quotes to prevent YAML errors from occurring.  The special character `$` is reserved for internal use, and will raise an error if used.  The maximum length allowed for this parameter is `31` characters. |
| **log_ip_errors**  dictionary | Modifies log settings for logging of IP error packets. |
| **enabled**  boolean | This option enables or disables the logging of IP error packets.  **Choices:**   - `false` - `true` |
| **rate_limit**  string | This option sets rate limits for the logging of IP error packets.  This option is effective only if logging of this message type is enabled. |
| **log_matches_accept_rule**  dictionary | Modifies log settings for ACL rules configured with an “accept” or “accept decisively” action. |
| **enabled**  boolean | This option enables or disables the logging of packets that match ACL rules configured with an “accept” or “accept decisively” action.  **Choices:**   - `false` - `true` |
| **rate_limit**  string | This option sets rate limits for the logging of packets that match ACL rules configured with an “accept” or “accept decisively” action.  This option is effective only if logging of this message type is enabled. |
| **log_matches_drop_rule**  dictionary | Modifies log settings for ACL rules configured with a drop action. |
| **enabled**  boolean | This option enables or disables the logging of packets that match ACL rules configured with a drop action.  **Choices:**   - `false` - `true` |
| **rate_limit**  string | This option sets rate limits for the logging of packets that match ACL rules configured with a drop action.  This option is effective only if logging of this message type is enabled. |
| **log_matches_reject_rule**  dictionary | Modifies log settings for ACL rules configured with a reject action. |
| **enabled**  boolean | This option enables or disables the logging of packets that match ACL rules configured with a reject action.  **Choices:**   - `false` - `true` |
| **rate_limit**  string | This option sets rate limits for the logging of packets that match ACL rules configured with a reject action.  This option is effective only if logging of this message type is enabled. |
| **log_message_fields**  list / elements=string | Specifies a set of fields to be logged.  This option is valid when the `log_storage_format` is set to `field-list`. It is ignored otherwise.  The order of the list is important, as the server displays the selected traffic items in the log sequentially according to it.  **Choices:**   - `"acl_policy_name"` - `"acl_policy_type"` - `"acl_rule_name"` - `"action"` - `"bigip_hostname"` - `"context_name"` - `"context_type"` - `"date_time"` - `"dest_fqdn"` - `"dest_geo"` - `"dest_ip"` - `"dest_port"` - `"drop_reason"` - `"management_ip_address"` - `"protocol"` - `"route_domain"` - `"sa_translation_pool"` - `"sa_translation_type"` - `"source_fqdn"` - `"source_user"` - `"src_geo"` - `"src_ip"` - `"src_port"` - `"translated_dest_ip"` - `"translated_dest_port"` - `"translated_ip_protocol"` - `"translated_route_domain"` - `"translated_src_ip"` - `"translated_src_port"` - `"translated_vlan"` - `"vlan"` |
| **log_publisher**  string | Specifies the name of the log publisher used for Network events.  To specify the log_publisher on a different partition from the AFM log profile, specify the name in fullpath format, e.g. `/Foobar/log-publisher`, otherwise the partition for the log publisher is inferred from the `partition` module parameter. |
| **log_storage_format**  string | Specifies the type of the storage format.  When creating a new log profile, if this parameter is not specified, the default is `none`.  When `field-list`, specifies the log displays only the items you specify in the `log_message_fields` list with `log_format_delimiter` as the delimiter between the items.  When `none`, the messages will be logged in the default format, which is `"management_ip_address", "bigip_hostname","context_type", "context_name","src_geo","src_ip", "dest_geo","dest_ip","src_port", "dest_port","vlan","protocol","route_domain", "translated_src_ip", "translated_dest_ip", "translated_src_port","translated_dest_port", "translated_vlan","translated_ip_protocol", "translated_route_domain", "acl_policy_type", "acl_policy_name","acl_rule_name","action", "drop_reason","sa_translation_type", "sa_translation_pool","flow_id", "source_user", "source_fqdn","dest_fqdn"`.  **Choices:**   - `"field-list"` - `"none"` |
| **log_tcp_errors**  dictionary | Modifies log settings for the logging of TCP error packets. |
| **enabled**  boolean | This option enables or disables the logging of TCP error packets.  **Choices:**   - `false` - `true` |
| **rate_limit**  string | This option sets rate limits for the logging of TCP error packets.  This option is effective only if logging of this message type is enabled. |
| **log_tcp_events**  dictionary | Modifies the log settings for logging of TCP events on the client side. |
| **enabled**  boolean | This option enables or disables the logging of TCP events on the client side.  Only **Established** and **Closed** states of a TCP session are logged if this option is enabled.  **Choices:**   - `false` - `true` |
| **rate_limit**  string | This option sets rate limits for the logging of TCP events on the client side.  This option is effective only if logging of this message type is enabled. |
| **log_translation_fields**  boolean | This option enables or disables the logging of translated (i.e server side) fields in ACL match and TCP events.  Translated fields include (but are not limited to) source address/port, destination address/port, IP protocol, route domain, and VLAN.  **Choices:**   - `false` - `true` |
| **partition**  string | Device partition to create log profile on.  This parameter is also used when specifying names for log publishers, unless log publisher names are in fullpath format.  **Default:** `"Common"` |
| **profile_name**  string / required | Specifies the name of the AFM (Advanced Firewall Manager) log profile to be updated. |
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
| **rate_limit**  string | Defines a rate limit for all combined network firewall log messages per second. Beyond this rate limit, log messages are not logged.  To specify an indefinite rate, use the value `indefinite`.  If specifying a numeric rate, the value must be between `1` and `4294967295`. |
| **state**  string | When `state` is `present`, ensures the resource exists.  The only built-in profile that allows updating network log settings is global-network, attempts to do so on other built-in profiles will be ignored.  When `state` is `absent`, ensures that the resource is removed.  The `absent` state is ignored for global-network log profile.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](bigip_firewall_log_profile_network_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_firewall_log_profile_network_module.md#id4)

```yaml+jinja
- name: Add network settings to log profile
  bigip_firewall_log_profile_network:
    profile_name: barbaz
    rate_limit: "150000"
    log_publisher: local-db-pub
    log_tcp_errors:
      enabled: true
      rate_limit: "10000"
    log_tcp_events:
      enabled: true
      rate_limit: "40000"
    log_storage_format: "field-list"
    log_message_fields:
      - vlan
      - translated_vlan
      - src_ip
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Change delimiter and log fields
  bigip_firewall_log_profile_network:
    profile_name: barbaz
    log_format_delimiter: '.'
    log_message_fields:
      - translated_dest_ip
      - translated_dest_port
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Modify built-in profile
  bigip_firewall_log_profile_network:
    profile_name: "global-network"
    log_publisher: "/foobar/log1"
    log_ip_errors:
      enabled: true
      rate_limit: "60000"
    log_matches_reject_rule:
      enabled: true
      rate_limit: "2000"
    log_translation_fields: true
    log_storage_format: "field-list"
    log_format_delimiter: '.'
    log_message_fields:
      - protocol
      - dest_ip
      - dest_port
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove custom log profile network log settings
  bigip_firewall_log_profile_network:
    profile_name: "{{ log_profile }}"
    state: absent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_firewall_log_profile_network_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **log_format_delimiter**  string | The delimiter string when using a log_storage_format of field-list.  **Returned:** changed  **Sample:** `"."` |
| **log_ip_errors**  complex | Log settings for logging of IP error packets.  **Returned:** changed  **Sample:** `"hash/dictionary of values"` |
| **enabled**  boolean | Enable or disable the logging of IP error packets.  **Returned:** changed  **Sample:** `true` |
| **rate_limit**  string | The rate limit for the logging of IP error packets.  **Returned:** changed  **Sample:** `"indefinite"` |
| **log_matches_accept_rule**  complex | Log settings for ACL rules configured with an “accept” or “accept decisively” action.  **Returned:** changed  **Sample:** `"hash/dictionary of values"` |
| **enabled**  boolean | Enable or disable the logging of packets that match ACL rules.  **Returned:** changed  **Sample:** `true` |
| **rate_limit**  string | The rate limit for the logging of packets that match ACL rules.  **Returned:** changed  **Sample:** `"indefinite"` |
| **log_matches_drop_rule**  complex | Log settings for ACL rules configured with a drop action.  **Returned:** changed  **Sample:** `"hash/dictionary of values"` |
| **enabled**  boolean | Enable or disable the logging of packets that match ACL rules.  **Returned:** changed  **Sample:** `true` |
| **rate_limit**  string | The rate limit for the logging of packets that match ACL rules.  **Returned:** changed  **Sample:** `"indefinite"` |
| **log_matches_reject_rule**  complex | Log settings for ACL rules configured with a reject action.  **Returned:** changed  **Sample:** `"hash/dictionary of values"` |
| **enabled**  boolean | Enable or disable the logging of packets that match ACL rules.  **Returned:** changed  **Sample:** `true` |
| **rate_limit**  string | The rate limit for the logging of packets that match ACL rules.  **Returned:** changed  **Sample:** `"indefinite"` |
| **log_message_fields**  list / elements=string | The delimiter string when using a log_storage_format of field-list.  **Returned:** changed  **Sample:** `["acl_policy_name", "acl_policy_type"]` |
| **log_publisher**  string | The name of the log publisher used for Network events.  **Returned:** changed  **Sample:** `"/Common/log-publisher"` |
| **log_storage_format**  string | The type of the storage format.  **Returned:** changed  **Sample:** `"field-list"` |
| **log_tcp_errors**  complex | Log settings for logging of TCP error packets.  **Returned:** changed  **Sample:** `"hash/dictionary of values"` |
| **enabled**  boolean | Enable or disable the logging of TCP error packets.  **Returned:** changed  **Sample:** `true` |
| **rate_limit**  string | The rate limit for the logging of TCP error packets.  **Returned:** changed  **Sample:** `"indefinite"` |
| **log_tcp_events**  complex | Log settings for logging of TCP events on the client side.  **Returned:** changed  **Sample:** `"hash/dictionary of values"` |
| **enabled**  boolean | Enable or disable the logging of TCP events on the client side.  **Returned:** changed  **Sample:** `true` |
| **rate_limit**  string | The rate limit for the logging of TCP events on the client side.  **Returned:** changed  **Sample:** `"indefinite"` |
| **log_translation_fields**  boolean | Enable or disable the logging of translated (i.e server side) fields in ACL match and TCP events.  **Returned:** changed  **Sample:** `true` |
| **rate_limit**  string | The rate limit for all combined network firewall log messages per second.  **Returned:** changed  **Sample:** `"indefinite"` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
