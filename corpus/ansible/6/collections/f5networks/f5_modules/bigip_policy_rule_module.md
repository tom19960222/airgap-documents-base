---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_policy_rule module – Manage LTM policy rules on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_policy_rule_module.html
fetched_at: 2026-07-27T17:27:24+00:00
---
# f5networks.f5_modules.bigip_policy_rule module – Manage LTM policy rules on a BIG-IP

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/f5networks/f5_modules) (version 1.21.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
> You need further requirements to be able to use this module,
> see [Requirements](bigip_policy_rule_module.md#ansible-collections-f5networks-f5-modules-bigip-policy-rule-module-requirements) for details.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_policy_rule`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_policy_rule_module.md#synopsis)
- [Requirements](bigip_policy_rule_module.md#requirements)
- [Parameters](bigip_policy_rule_module.md#parameters)
- [Notes](bigip_policy_rule_module.md#notes)
- [Examples](bigip_policy_rule_module.md#examples)
- [Return Values](bigip_policy_rule_module.md#return-values)

## [Synopsis](bigip_policy_rule_module.md#id1)

- This module manages LTM policy rules on a BIG-IP.

## [Requirements](bigip_policy_rule_module.md#id2)

The below requirements are needed on the host that executes this module.

- BIG-IP >= v12.1.0

## [Parameters](bigip_policy_rule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **actions**  list / elements=dictionary | The actions you want the policy rule to perform.  The available attributes vary by the action, however, each action requires you specify a `type`.  These conditions can be specified in any order. Despite the fact they are in a list, the order in the list does not matter to the BIG-IP. |
| **asm_policy**  string | ASM policy to enable.  This parameter is only valid with the `enable` type. |
| **cookie_expiry**  integer  added in f5networks.f5_modules 1.1.0 | Optional argument, specifying the time for which the session is persisted.  This parameter is only valid with the `persist` type. |
| **cookie_insert**  string  added in f5networks.f5_modules 1.1.0 | Cookie name on which you want to persist.  This parameter is only valid with the `persist` type. |
| **disable_target**  string  added in f5networks.f5_modules 1.8.0 | Target you want to disable.  This parameter is only valid with the `disable` type.  Choices:   - `"server_ssl"` - `"persist"` |
| **event**  string | Events on which actions, such as reset and forward, can be triggered.  With the `set_variable` action, it is used for specifying an action event, such as request or response.  Valid event choices for `forward` action type are: client_accepted, proxy_request request, ssl_client_hello and ssl_client_server_hello_send.  Valid event choices for `reset` acton type are: client_accepted, proxy_connect proxy_request, proxy_response, request, response, server_connected, ssl_client_hello, ssl_client_server_hello_send, ssl_server_handshake, ssl_server_hello, websocket_request, websocket_response.  Valid event choices for `disable` acton type are: client_accepted, proxy_connect proxy_request, proxy_response, request, server_connected. |
| **expression**  string | A Tcl expression used with the `set_variable` action. |
| **http_connect**  dictionary  added in f5networks.f5_modules 1.8.0 | HTTP Connect header you want to replace.  This parameter is only valid with the `replace` type. |
| **event**  string / required | Type of event when the `http_connect` header is replaced.  Choices:   - `"client_accepted"` - `"proxy_connect"` - `"proxy_request"` - `"proxy_response"` - `"request"` - `"server_connected"` - `"ssl_client_hello"` |
| **port**  integer | The port number.  If a port number is not provided, the value is set to 0 by default.  Be explicit when defining rules, so the system does not override port values. |
| **value**  string / required | The value of `http_connect`. |
| **http_cookie**  dictionary  added in f5networks.f5_modules 1.8.0 | HTTP Cookie header you want to remove or insert.  This parameter is only valid with the `remove` and `insert` type. |
| **event**  string / required | Type of event when the `http_cookie` is removed or inserted.  Choices:   - `"request"` - `"proxy_connect"` - `"proxy_request"` |
| **name**  string / required | The name of `http_cookie`. |
| **value**  string | The value of `http_cookie`.  This is a mandatory parameter when configured with `insert` type action. |
| **http_header**  dictionary  added in f5networks.f5_modules 1.8.0 | HTTP Header that you want to remove or insert.  This parameter is only valid with the `remove`, `insert` and `replace` type. |
| **event**  string / required | Type of event when the `http_header` is removed, replaced, or inserted.  The `request` and `response` events are only choices with `remove` and `insert` type.  All of events are valid with `replace` type action.  Choices:   - `"request"` - `"response"` - `"proxy_connect"` - `"proxy_request"` - `"proxy_response"` |
| **name**  string / required | The name of `http_header`. |
| **value**  string | The value of `http_header`.  Mandatory parameter when configured with `insert` or `replace` type. |
| **http_host**  dictionary  added in f5networks.f5_modules 1.8.0 | HTTP Host header you want to replace.  This parameter is only valid with the `replace` type. |
| **event**  string / required | Type of event when the `http_host` is replaced.  Choices:   - `"request"` - `"proxy_connect"` - `"proxy_request"` |
| **value**  string / required | The value of `http_host`. |
| **http_referer**  dictionary  added in f5networks.f5_modules 1.8.0 | HTTP Referer header you want to remove, replace, or insert.  This parameter is only valid with the `remove`, `insert` and `replace` type. |
| **event**  string / required | Type of event when the c(http_referer) is removed, replaced, or inserted.  Choices:   - `"request"` - `"proxy_connect"` - `"proxy_request"` |
| **value**  string | The value of `http_referer`.  This is a mandatory parameter when configured with `insert` type action.  This parameter is ignored for the `remove` type.  This parameter is optional for the `replace` type. |
| **http_set_cookie**  dictionary  added in f5networks.f5_modules 1.8.0 | HTTP Set-Cookie header you want to remove or insert.  This parameter is only valid with the `remove` or c(insert) type. |
| **name**  string / required | The name of `http_set_cookie`. |
| **value**  string | The value of `http_set_cookie`.  This is a mandatory parameter when configured with `insert` type action. |
| **http_uri**  dictionary  added in f5networks.f5_modules 1.8.0 | Replaces HTTP URI, path, or string.  This parameter is only valid with the `replace` type. |
| **event**  string / required | Type of event when the `http_uri` is replaced.  Choices:   - `"request"` - `"proxy_connect"` - `"proxy_request"` |
| **type**  string / required | Specifies the part of the `http_uri` to be replaced.  Choices:   - `"path"` - `"query_string"` - `"full_string"` |
| **value**  string / required | The value of `http_uri`. |
| **location**  string | The new URL for which a redirect response is sent.  A Tcl command substitution can be used for this field. |
| **node**  string  added in f5networks.f5_modules 1.2.0 | Node to which you want to forward traffic.  This parameter is only valid with the `forward` type. |
| **pool**  string | Pool to which you want to forward traffic.  This parameter is only valid with the `forward` type. |
| **type**  string / required | The action type. This value controls which of the following options are required.  When `type` is `forward`, the system associates a given `pool`, or `virtual`, or `node` with this rule.  When `type` is `enable`, the system associates a given `asm_policy` with this rule.  When `type` is `ignore`, the system removes all existing actions from this rule.  When `type` is `redirect`, the system redirects an HTTP request to a different URL.  When `type` is `reset`, the system resets the connection upon `event`.  When `type` is `persist`, the system associates `cookie_insert` and `cookie_expiry` with this rule.  When `type` is `set_variable`, the system sets a variable based on the evaluated Tcl `expression` based on `event`.  When `type` is `remove`, the system removes `http_set_cookie`, `http_referer`, `http_header` or `http_cookie` with this rule.  When `type` is `insert`, the system inserts `http_set_cookie`, `http_referer`, `http_header` or `http_cookie` with this rule.  When `type` is `replace`, the system replaces `http_connect`, `http_referer`, `http_header`, `http_uri` or `http_host` with this rule.  When `type` is `disable`, the system disables `disable_target` with this rule.  Choices:   - `"forward"` - `"enable"` - `"ignore"` - `"redirect"` - `"reset"` - `"persist"` - `"set_variable"` - `"remove"` - `"insert"` - `"replace"` - `"disable"` |
| **variable_name**  string | Variable name used with the `set_variable` action. |
| **virtual**  string | Virtual server to which you want to forward traffic.  This parameter is only valid with the `forward` type. |
| **conditions**  list / elements=dictionary | A list of attributes that describe the condition.  See suboptions for details on how to construct each list entry.  The ordering of this list is important, the module ensures the order is kept when modifying the task.  The suboption options below are not required for all condition types, read the description for more details.  These conditions can be specified in any order. Despite the fact they are in a list, the order in the list does not matter to the BIG-IP. |
| **address_matches_with_any**  list / elements=string  added in f5networks.f5_modules 1.8.0 | A list of IP Subnet address strings the IP address should match.  This parameter is only valid with the `tcp` type. |
| **address_matches_with_datagroup**  list / elements=string  added in f5networks.f5_modules 1.8.0 | A list of internal datagroup strings the IP address should match.  This parameter is only valid with the `tcp` type. |
| **address_matches_with_external_datagroup**  list / elements=string  added in f5networks.f5_modules 1.10.0 | A list of external datagroup strings the IP address should match.  This parameter is only valid with the `tcp` type. |
| **event**  string | Events on which conditions type match rules can be triggered.  Supported only for `http_header`, `http_method`, `ssl_extension` and `tcp`.  Valid choices for `http_header` condition types are: `proxy_connect`, `proxy_request`, `proxy_response`, `request` and `response`.  Valid choices for `http_method` condition types are: `proxy_connect`, `proxy_request`, `proxy_response`, `request` and `response`.  Valid choices for `tcp` condition types are: `request`, `client_accepted`, `proxy_connect`, `proxy_request`, `proxy_response`, `ssl_client_hello`, and `ssl_client_server_hello_send`.  Valid choices for `ssl_extension` are: `ssl_client_hello`, and `ssl_client_server_hello_send`. |
| **header_is_any**  list / elements=string  added in f5networks.f5_modules 1.8.0 | A list of strings of characters the HTTP Header value should match.  This parameter is only valid with the `http_header` type. |
| **header_name**  string  added in f5networks.f5_modules 1.8.0 | A name of `http_header`.  This parameter is only valid with the `http_header` type. |
| **host_begins_with_any**  list / elements=string | A list of strings of characters the HTTP Host should start with.  This parameter is only valid with the `http_host` type. |
| **host_ends_with_any**  list / elements=string  added in f5networks.f5_modules 1.8.0 | A list of strings of characters the HTTP Host should end with.  This parameter is only valid with the `http_host` type. |
| **host_is_any**  list / elements=string | A list of strings of characters the HTTP Host should match.  This parameter is only valid with the `http_host` type. |
| **host_is_not_any**  list / elements=string | A list of strings of characters the HTTP Host should not match.  This parameter is only valid with the `http_host` type. |
| **method_matches_with_any**  list / elements=string  added in f5networks.f5_modules 1.10.0 | A list of strings of characters the HTTP Method value should match.  This parameter is only valid with the `http_method` type. |
| **path_begins_with_any**  list / elements=string | A list of strings of characters the HTTP URI should start with.  This parameter is only valid with the `http_uri` type. |
| **path_contains**  list / elements=string  added in f5networks.f5_modules 1.8.0 | A list of strings of characters the HTTP URI should contain.  This parameter is only valid with the `http_uri` type. |
| **path_is_any**  list / elements=string  added in f5networks.f5_modules 1.8.0 | A list of strings of characters the HTTP URI should match.  This parameter is only valid with the `http_uri` type. |
| **server_name_is_any**  list / elements=string | A list of strings of characters the SSL Extension should match.  This parameter is only valid with the `ssl_extension` type. |
| **type**  string / required | The condition type. This value controls which of the following options are required.  When `type` is `http_uri`, the valid choices are: `path_begins_with_any`, `path_contains` or `path_is_any`.  When `type` is `http_host`, the valid choices are: `host_is_any`, `host_is_not_any`, `host_begins_with_any` or `host_ends_with_any`.  When `type` is `http_header`, the `header_name` parameter is mandatory and the valid choice is: `header_is_any`.  When `type` is `http_method`, the valid choices are: `method_matches_with_any`.  When `type` is `all_traffic`, the system removes all existing conditions from this rule.  Choices:   - `"http_uri"` - `"all_traffic"` - `"http_host"` - `"http_header"` - `"http_method"` - `"ssl_extension"` - `"tcp"` |
| **description**  string | Description of the policy rule. |
| **name**  string / required | The name of the rule. |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **policy**  string / required | The name of the policy you want to associate this rule with. |
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
| **replace_with**  boolean | Specifies if the `conditions`/`actions` given by the user should overwrite what exists on the device.  The option is useful when a subset of `conditions`/`actions` needs to be removed. This option is similar to the replace-all-with flag available in TMSH commands.  Using this option is not idempotent.  Choices:   - `false` ← (default) - `true` |
| **rule_order**  integer  added in f5networks.f5_modules 1.10.0 | Specifies a number that indicates the order of this rule relative to other rules in the policy.  When not set, the device sets the parameter to 0.  If there are rules with the same rule order number, the device uses rule names to determine how the rules are ordered.  The lower the number, the lower the rule is in the general order, with the lowest number `0` being the topmost one.  Valid range of values is between `0` and `4294967295` inclusive. |
| **state**  string | When `present`, ensures the key is uploaded to the device. When `absent`, ensures the key is removed from the device. If the key is currently in use, the module will not be able to remove the key.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](bigip_policy_rule_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_policy_rule_module.md#id5)

```yaml+jinja
- name: Create policies
  bigip_policy:
    name: Policy-Foo
    state: present
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Add a rule to the new policy
  bigip_policy_rule:
    policy: Policy-Foo
    name: rule3
    conditions:
      - type: http_uri
        path_begins_with_any:
          - /ABC
    actions:
      - type: forward
        pool: pool-svrs
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Add multiple rules to the new policy
  bigip_policy_rule:
    policy: Policy-Foo
    name: "{{ item.name }}"
    conditions: "{{ item.conditions }}"
    actions: "{{ item.actions }}"
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
  loop:
    - name: rule1
      actions:
        - type: forward
          pool: pool-svrs
      conditions:
        - type: http_uri
          path_begins_with_any:
            - /euro
    - name: rule2
      actions:
        - type: forward
          pool: pool-svrs
      conditions:
        - type: http_uri
          path_begins_with_any:
            - /HomePage/
    - name: rule3
      actions:
        - type: set_variable
          variable_name: user-agent
          expression: tcl:[HTTP::header User-Agent]
          event: request
      conditions:
        - type: http_uri
          path_begins_with_any:
            - /HomePage/

- name: Remove all rules and conditions from the rule
  bigip_policy_rule:
    policy: Policy-Foo
    name: rule1
    conditions:
      - type: all_traffic
    actions:
      - type: ignore
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
```

## [Return Values](bigip_policy_rule_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **actions**  complex | The new list of actions applied to the rule.  Returned: changed  Sample: `"hash/dictionary of values"` |
| **pool**  string | Pool for forwarding to.  Returned: changed  Sample: `"foo-pool"` |
| **type**  string | The action type.  Returned: changed  Sample: `"forward"` |
| **conditions**  complex | The new list of conditions applied to the rule.  Returned: changed  Sample: `"hash/dictionary of values"` |
| **path_begins_with_any**  list / elements=string | List of strings the URI begins with.  Returned: changed  Sample: `["foo", "bar"]` |
| **type**  string | The condition type.  Returned: changed  Sample: `"http_uri"` |
| **description**  string | The new description of the rule.  Returned: changed  Sample: `"My rule"` |
| **rule_order**  integer | Specifies a number that indicates the order of this rule relative to other rules in the policy.  Returned: changed  Sample: `10` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
