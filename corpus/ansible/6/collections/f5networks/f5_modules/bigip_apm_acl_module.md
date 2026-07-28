---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_apm_acl module – Manage user-defined APM ACLs"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_apm_acl_module.html
fetched_at: 2026-07-27T17:26:09+00:00
---
# f5networks.f5_modules.bigip_apm_acl module – Manage user-defined APM ACLs

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_apm_acl`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_apm_acl_module.md#synopsis)
- [Parameters](bigip_apm_acl_module.md#parameters)
- [Notes](bigip_apm_acl_module.md#notes)
- [Examples](bigip_apm_acl_module.md#examples)
- [Return Values](bigip_apm_acl_module.md#return-values)

## [Synopsis](bigip_apm_acl_module.md#id1)

- Manage user-defined APM ACLs.

## [Parameters](bigip_apm_acl_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **acl_order**  integer | Specifies a number that indicates the order of this ACL relative to other ACLs.  When not set, the device will always place the ACL after the last one created.  The lower the number, the higher the ACL will be in the general order, with the lowest number `0` being the topmost one.  Valid range of values is between `0` and `65535` inclusive. |
| **description**  string | User created ACL description. |
| **entries**  list / elements=dictionary | Access control entries that define the ACL matching and its respective behavior.  The order in which the rules are placed as arguments to this parameter determines their order in the ACL, in other words changing the order of the same elements will cause a change on the unit.  Changes in the number of rules will always trigger device change. This means user input will take precedence over what is on device. |
| **action**  string / required | Specifies the action that the access control entry takes when a match for this access control entry is encountered.  Choices:   - `"allow"` - `"reject"` - `"discard"` - `"continue"` |
| **dst_addr**  string | Specifies the destination IP address for the access control entry.  When set to `any` the ACL will match any destination address, `dst_mask` is ignored in this case. |
| **dst_mask**  string | Optional parameter that specifies the destination network mask for the access control entry.  If not specified and `dst_addr` is not `any`, the `dst_addr` is deemed to be host address. |
| **dst_port**  string | Specifies the destination port for the access control entry.  Can be set to `*` to indicate all ports.  Parameter is mutually exclusive with `dst_port_range`. |
| **dst_port_range**  string | Specifies the destination port range for the access control entry.  Parameter is mutually exclusive with `dst_port_range`.  To indicate all ports the `dst_port` parameter must be used and set to `*`. |
| **host_name**  string | This parameter applies to Layer 7 access control entries only.  Specifies a host to which the access control entry applies. |
| **log**  string | Specifies the log level that is logged when actions of this type occur.  When `none` it will log nothing, which is a default action.  When `packet` it will log the matched packet.  Choices:   - `"none"` - `"packet"` |
| **paths**  string | This parameter applies to Layer 7 access control entries only.  Specifies the path or paths to which the access control entry applies. |
| **protocol**  string | This parameter applies to Layer 4 access control entries only.  Specifies the protocol: `tcp`, `udp`, `icmp` or `all` protocols, to which the access control entry applies.  Choices:   - `"tcp"` - `"icmp"` - `"udp"` - `"all"` |
| **scheme**  string | This parameter applies to Layer 7 access control entries only.  Specifies the URI scheme: `http`, `https` or `any` on which the access control entry operates.  Choices:   - `"http"` - `"https"` - `"any"` |
| **src_addr**  string | Specifies the source IP address for the access control entry.  When set to `any` the ACL will match any source address, `src_mask` is ignored in this case. |
| **src_mask**  string | Optional parameter that specifies the source network mask for the access control entry.  If not specified and `src_addr` is not `any`, the `src_addr` is deemed to be host address. |
| **src_port**  string | Specifies the source port for the access control entry.  Can be set to `*` to indicate all ports.  Parameter is mutually exclusive with `src_port_range`. |
| **src_port_range**  string | Specifies the source port range for the access control entry.  Parameter is mutually exclusive with `src_port_range`.  To indicate all ports the `src_port` parameter must be used and set to `*`. |
| **name**  string / required | Specifies the name of the ACL to manage. |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **path_match_case**  boolean | Specifies whether alphabetic case is considered when matching paths in an access control entry.  Choices:   - `false` - `true` |
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
| **state**  string | When `state` is `present`, ensures that the ACL exists.  When `state` is `absent`, ensures that the ACL is removed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **type**  string | Specifies the type of ACL to create.  Once the type is set it cannot be changed.  Choices:   - `"static"` - `"dynamic"` |

## [Notes](bigip_apm_acl_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_apm_acl_module.md#id4)

```yaml+jinja
- name: Create a static ACL with L4 entries
  bigip_apm_acl:
    name: L4foo
    acl_order: 0
    type: static
    entries:
      - action: allow
        dst_port: '80'
        dst_addr: '192.168.1.1'
        src_port: '443'
        src_addr: '10.10.10.0'
        src_mask: '255.255.255.128'
        protocol: tcp
      - action: reject
        dst_port: '*'
        dst_addr: '192.168.1.1'
        src_port: '*'
        src_addr: '10.10.10.0'
        src_mask: '255.255.255.128'
        protocol: tcp
        log: packet
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Create a static ACL with L7 entries
  bigip_apm_acl:
    name: L7foo
    acl_order: 1
    type: static
    path_match_case: no
    entries:
      - action: allow
        host_name: 'foobar.com'
        paths: '/shopfront'
        scheme: https
      - action: reject
        host_name: 'internal_foobar.com'
        paths: '/admin'
        scheme: any
        log: packet
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Create a static ACL with L7/L4 entries
  bigip_apm_acl:
    name: L7L4foo
    acl_order: 2
    type: static
    path_match_case: no
    entries:
      - action: allow
        host_name: 'foobar.com'
        paths: '/shopfront'
        scheme: https
        dst_port: '8181'
        dst_addr: '192.168.1.1'
        protocol: tcp
      - action: reject
        dst_addr: '192.168.1.1'
        host_name: 'internal_foobar.com'
        paths: '/admin'
        scheme: any
        protocol: all
        log: packet
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Modify a static ACL entries
  bigip_apm_acl:
    name: L4foo
    entries:
      - action: allow
        dst_port: '80'
        dst_addr: '192.168.1.1'
        src_port: '443'
        src_addr: '10.10.10.0'
        src_mask: '255.255.255.128'
        protocol: tcp
      - action: discard
        dst_port: '*'
        dst_addr: 192.168.1.1
        src_port: '*'
        src_addr: '10.10.10.0'
        src_mask: '255.2155.255.128'
        protocol: all
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Remove static ACL
  bigip_apm_acl:
    name: L4foo
    state: absent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_apm_acl_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **acl_order**  integer | The order of this ACL relative to other ACLs.  Returned: changed  Sample: `10` |
| **description**  string | The new description of the ACL.  Returned: changed  Sample: `"My ACL"` |
| **entries**  complex | Access control entries that define the ACL matching and its respective behavior.  Returned: changed  Sample: `"hash/dictionary of values"` |
| **action**  string | Action the access control entry takes when a match for this access control entry is encountered.  Returned: changed  Sample: `"allow"` |
| **dst_addr**  string | The destination IP address for the access control entry.  Returned: changed  Sample: `"192.168.0.1"` |
| **dst_mask**  string | The destination network mask for the access control entry.  Returned: changed  Sample: `"255.255.255.128"` |
| **dst_port**  string | The destination port for the access control entry.  Returned: changed  Sample: `"80"` |
| **dst_port_range**  string | The destination port range for the access control entry.  Returned: changed  Sample: `"80-81"` |
| **host_name**  string | The host to which the access control entry applies.  Returned: changed  Sample: `"foobar.com"` |
| **log**  string | The log level that is logged when actions of this type occur.  Returned: changed  Sample: `"packet"` |
| **paths**  string | The path or paths to which the access control entry applies.  Returned: changed  Sample: `"/fooshop"` |
| **protocol**  string | The protocol to which the access control entry applies.  Returned: changed  Sample: `"tcp"` |
| **scheme**  string | The URI scheme on which the access control entry operates.  Returned: changed  Sample: `"https"` |
| **src_addr**  string | The source IP address for the access control entry.  Returned: changed  Sample: `"192.168.0.1"` |
| **src_mask**  string | The source network mask for the access control entry.  Returned: changed  Sample: `"255.255.255.128"` |
| **src_port**  string | The source port for the access control entry.  Returned: changed  Sample: `"80"` |
| **src_port_range**  string | The source port range for the access control entry.  Returned: changed  Sample: `"80-81"` |
| **path_match_case**  boolean | Specifies whether alphabetic case is considered when matching paths in an access control entry.  Returned: changed  Sample: `true` |
| **type**  string | The type of ACL to create.  Returned: changed  Sample: `"static"` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
